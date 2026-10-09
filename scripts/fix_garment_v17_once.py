#!/usr/bin/env python3
"""One-time correction of two inherited secondary pinyin punctuation errors."""
from __future__ import annotations

import hashlib
import json
import pathlib
import zipfile

ROOT=pathlib.Path(__file__).resolve().parents[1]
DIRECTORY=ROOT / "content" / "interactive-books" / "garment_factory_1000"
MAIN=DIRECTORY / "book_latest.zip"
ARCHIVE=DIRECTORY / "archive" / "garment_factory_1000_v1_7.zip"
MANIFEST=ROOT / "content" / "interactive-books" / "catalog.json"

FIXES={
    (722,"alternatives",0):("有没有哪道工序漏做？","yǒu méi yǒu nǎ dào gōng xù? lòu zuò?","yǒu méi yǒu nǎ dào gōng xù lòu zuò?"),
    (845,"replies",1):("还差几件没登记。","hái chà jǐ jiàn? méi dēng jì.","hái chà jǐ jiàn méi dēng jì."),
}
assert MAIN.is_file()
with zipfile.ZipFile(MAIN) as archive:
    names=archive.namelist()
    assert names==[f"garment_{i:02d}.json" for i in range(1,12)],names
    packs=[json.loads(archive.read(name)) for name in names]
applied=[]
for pack in packs:
    for phrase in pack["phrases"]:
        n=phrase["number"]
        for (num,key,index),(expected,old,new) in FIXES.items():
            if n!=num:continue
            node=phrase[key][index]
            assert node["text"]==expected,(n,node)
            if node["pinyin"]==old:
                node["pinyin"]=new
                applied.append((n,key,index))
            else:
                assert node["pinyin"]==new,(n,node)
assert len(applied)==2 or len(applied)==0,applied
temp=MAIN.with_suffix(".tmp")
with zipfile.ZipFile(temp,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for i,pack in enumerate(packs,1):
        archive.writestr(f"garment_{i:02d}.json",
                         (json.dumps(pack,ensure_ascii=False,separators=(",",":"))+"\n").encode("utf-8"))
with zipfile.ZipFile(temp) as archive:
    assert archive.testzip() is None
    numbers=[p["number"] for pack in packs for p in pack["phrases"]]
    assert numbers==list(range(1,1001))
preview=json.loads((DIRECTORY/"free_preview.json").read_text(encoding="utf-8"))
assert preview["phrases"]==packs[0]["phrases"][:30]
data=temp.read_bytes()
sha=hashlib.sha256(data).hexdigest()
temp.replace(MAIN)
ARCHIVE.write_bytes(data)
catalog=json.loads(MANIFEST.read_text(encoding="utf-8"))
item=next(v for v in catalog["items"] if v["id"]=="garment_factory_1000")
item["bundle_sha256"]=sha
item["bundle_size"]=len(data)
item["content_version"]=7
MANIFEST.write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("Applied",applied,"sha256",sha,"bytes",len(data))
