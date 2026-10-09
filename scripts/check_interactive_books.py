#!/usr/bin/env python3
"""Validate all public garment v1.7 teaching data against its declared manifest."""
import collections
import hashlib
import json
import pathlib
import re
import zipfile

BASE=pathlib.Path(__file__).resolve().parents[1]/"content"/"interactive-books"
manifest=json.loads((BASE/"catalog.json").read_text(encoding="utf-8"))
assert manifest["type"]=="interactive_books"
item=next(x for x in manifest["items"] if x["id"]=="garment_factory_1000")
root=BASE/"garment_factory_1000"
archive=root/"book_latest.zip"
data=archive.read_bytes()
assert len(data)==item["bundle_size"],"ZIP size differs from manifest"
assert hashlib.sha256(data).hexdigest()==item["bundle_sha256"],"ZIP hash differs from manifest"
assert item["bundle_path"]=="content/interactive-books/garment_factory_1000/book_latest.zip"
with zipfile.ZipFile(archive) as z:
    names=z.namelist()
    assert names==[f"garment_{i:02d}.json" for i in range(1,12)]
    assert z.testzip() is None
    packs=[json.loads(z.read(name)) for name in names]
    assert all(info.file_size<=2*1024*1024 for info in z.infolist())
assert all(p["pack_id"]==f"garment_factory_{i:02d}" for i,p in enumerate(packs,1))
counts=[172,108,106,240,27,80,30,57,48,56,76]
assert [len(p["phrases"]) for p in packs]==counts
cards=[p for pack in packs for p in pack["phrases"]]
assert len(cards)==1000 and [x["number"] for x in cards]==list(range(1,1001))
assert len({x["id"] for x in cards})==1000
assert len({x["text"].strip() for x in cards})==1000
for x in cards:
    for k in ("text","pinyin","phonetic_my","meaning_my","when_to_use_my","scene_id"):
        assert isinstance(x.get(k),str) and x[k].strip(),(x["number"],k)
    for k in ("replies","alternatives","breakdown"):
        assert isinstance(x.get(k),list) and x[k],(x["number"],k)
        for v in x[k]:
            for fld in ("text","pinyin","phonetic_my","meaning_my"):
                assert isinstance(v.get(fld),str) and v[fld].strip(),(x["number"],k,fld)
            assert not re.search(r"[?!]\s+[a-zA-Z]",v["pinyin"]),(x["number"],k,"mid-phrase punctuation")
preview=json.loads((root/"free_preview.json").read_text(encoding="utf-8"))
assert preview["phrases"]==cards[:30] and item["free_count"]==30
catalog=json.loads((root/"web_catalog.json").read_text(encoding="utf-8"))
assert len(catalog["categories"])==11 and catalog["item_count"]==1000
scene_counts=collections.Counter(x["scene_id"] for x in cards)
scenes=[s for c in catalog["categories"] for s in c["scenes"]]
assert len(scenes)==40 and len(scene_counts)==40
assert {x["scene_id"] for x in scenes}==set(scene_counts)
for s in scenes:
    sub=[x["number"] for x in cards if x["scene_id"]==s["scene_id"]]
    assert len(sub)==s["count"] and min(sub)==s["start_number"] and max(sub)==s["end_number"],s
assert sum(len(x["replies"]) for x in cards)==1904
assert sum(len(x["alternatives"]) for x in cards)==1003
assert sum(len(x["breakdown"]) for x in cards)==2816
assert (root/"archive"/"garment_factory_1000_v1_7.zip").read_bytes()==data,"archived copy differs"
print("PASS: 11 packs / 40 scenes / 1000 distinct phrases / 30 exact free phrases.")
print("PASS: 1904 replies / 1003 alternatives / 2816 breakdowns; SHA256",item["bundle_sha256"])
print("NOTE: Native speaker translation and phonetic accuracy requires human review.")
