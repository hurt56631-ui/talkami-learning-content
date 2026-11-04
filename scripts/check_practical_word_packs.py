#!/usr/bin/env python3
"""Validate the 16 practical dictionary packs, audio manifest and release covers."""
import csv
import json
import re
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORDS = ROOT / "content" / "words"
PACKS = WORDS / "packs" / "practical_16_v5"
COVERS = WORDS / "covers"
EXPECTED = {f"{i:02}": n for i, n in enumerate(
    [225, 378, 137, 350, 250, 195, 291, 254,
     467, 254, 221, 180, 239, 184, 108, 767], start=1
)}
EXAMPLE_COUNTS = {"01": 299, "02": 594, "03": 213, "04": 413,
                  "05": 277, "06": 218, "07": 320, "08": 332, "12": 180}
REQUIRED = ("id", "hanzi", "pinyin", "phonetic_my", "burmese",
            "category_id", "subcategory_id", "source_order", "content_status")


def check(condition, message):
    if not condition:
        raise AssertionError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def verify_png(path):
    content = path.read_bytes()
    check(content.startswith(b"\x89PNG\r\n\x1a\n"), f"invalid PNG signature: {path}")
    check(len(content) > 100, f"cover too small: {path}")
    offset = 8
    ihdr = None
    has_idat = False
    has_iend = False
    while offset + 12 <= len(content):
        count = struct.unpack_from(">I", content, offset)[0]
        tag = content[offset+4:offset+8]
        end = offset + 12 + count
        check(end <= len(content), f"truncated PNG chunk: {path}")
        payload = content[offset+8:offset+8+count]
        got_crc = struct.unpack_from(">I", content, offset+8+count)[0]
        expected_crc = zlib.crc32(tag + payload) & 0xFFFFFFFF
        check(got_crc == expected_crc, f"PNG CRC failed: {path}")
        if tag == b"IHDR":
            ihdr = payload
        elif tag == b"IDAT":
            has_idat = True
        elif tag == b"IEND":
            has_iend = True
            check(end == len(content), f"extraneous PNG bytes: {path}")
            break
        offset = end
    check(ihdr is not None and has_idat and has_iend, f"incomplete PNG: {path}")
    width, height, depth, image_type = struct.unpack_from(">IIBB", ihdr)
    check(width >= 240 and height >= 144 and depth == 8 and image_type in (2, 3, 6),
          f"unsupported PNG format: {path}")


def main():
    catalog = read_json(WORDS / "catalog.json")
    check(catalog.get("version", 0) >= 10, "catalog version must be >=10")
    items = catalog.get("items", [])
    practical = {item["id"]: item for item in items if str(item.get("id", "")).startswith("practical_")}
    check(len(practical) == 16, "expected exactly 16 practical catalog entries")
    check(len({item["id"] for item in items}) == len(items), "duplicate catalog IDs")
    assets = set()
    ids, headwords, subcategories = set(), set(), set()
    by_id = {}
    total = 0
    example_count = 0
    example_ids = set()
    examples_by_category = {}

    for code, declared in EXPECTED.items():
        item_id = f"practical_{code}"
        item = practical.get(item_id)
        check(item is not None, f"missing catalog entry: {item_id}")
        check(item.get("level") == item_id and item.get("target") == "word",
              f"invalid catalog level/target: {item_id}")
        pack = f"content/words/packs/practical_16_v5/category_{code}.json"
        cover = f"content/words/covers/practical_{code}.png"
        check(item.get("source_data") == pack, f"invalid source_data for {code}")
        check(item.get("source_cover") == cover, f"invalid source_cover for {code}")
        example_enabled = code in EXAMPLE_COUNTS
        data_version = 3 if example_enabled else 2
        asset_version = 6 if example_enabled else 5
        check(item.get("data_version") == data_version and item.get("cover_version") == 1,
              f"invalid version for {code}")
        check(item.get("data_url") == f"talkami-practical-{code}-v{asset_version}.json",
              f"unexpected release filename for {code}")
        for field, suffix in (("data_url", ".json"), ("cover_url", ".png")):
            name = item.get(field, "")
            check(isinstance(name, str) and name.endswith(suffix)
                  and "/" not in name and "\\" not in name
                  and re.fullmatch(r"[A-Za-z0-9._-]+", name),
                  f"invalid release asset {field}: {code}")
            check(name not in assets, f"duplicate asset: {name}")
            assets.add(name)
        verify_png(ROOT / cover)
        rows = read_json(ROOT / pack)
        check(isinstance(rows, list) and len(rows) == declared,
              f"pack count incorrect for {code}")
        check(item.get("item_count") == declared, f"catalog count incorrect for {code}")
        category_examples = 0
        for row in rows:
            check(isinstance(row, dict) and all(row.get(k) not in (None, "") for k in REQUIRED),
                  f"missing word field in {code}")
            ident = row["id"]
            check(isinstance(ident, int) and ident == 1_000_000 + row["source_order"],
                  f"unstable ID: {ident}")
            check(ident not in ids, f"duplicate word ID: {ident}")
            check(row["hanzi"] not in headwords, f"duplicate word: {row['hanzi']}")
            ids.add(ident)
            headwords.add(row["hanzi"])
            by_id[ident] = row
            check(row["category_id"] == code
                  and row["subcategory_id"].startswith(code + "."),
                  f"wrong category: {ident}")
            subcategories.add(row["subcategory_id"])
            status = "examples_ready" if example_enabled else "dictionary_only"
            check(row.get("level") == "practical"
                  and row.get("content_status") == status,
                  f"unexpected word content status: {ident}")
            for k in ("collocations", "collocations_pinyin", "collocations_my"):
                check(row.get(k) == [], f"unexpected {k} at {ident}")
            check(row.get("collocation_ids") == {}, f"unexpected collocation IDs at {ident}")
            examples = row.get("examples")
            if example_enabled:
                check(isinstance(examples, list) and 1 <= len(examples) <= 2,
                      f"expected 1–2 examples for {ident}")
                for index, example in enumerate(examples, start=1):
                    check(isinstance(example, dict), f"invalid example object for {ident}")
                    exid = f"{ident}_ex{index:02d}"
                    check(example.get("id") == exid and exid not in example_ids,
                          f"invalid or repeated example ID: {exid}")
                    example_ids.add(exid)
                    hanzi = example.get("hanzi", "")
                    pinyin = example.get("pinyin", "")
                    burmese = example.get("burmese", "")
                    check(isinstance(hanzi, str) and row["hanzi"] in hanzi,
                          f"target word missing from example: {exid}")
                    check(isinstance(pinyin, str) and bool(pinyin.strip()),
                          f"missing pinyin in example: {exid}")
                    check(isinstance(burmese, str) and bool(burmese.strip())
                          and re.search(r"[\u1000-\u109F\uAA60-\uAA7F]", burmese),
                          f"missing Myanmar example translation: {exid}")
                category_examples += len(examples)
            else:
                check(examples == [], f"unexpected examples at {ident}")
        expected_examples = EXAMPLE_COUNTS.get(code, 0)
        check(category_examples == expected_examples,
              f"example count incorrect for {code}: {category_examples} != {expected_examples}")
        examples_by_category[code] = category_examples
        example_count += category_examples
        total += len(rows)

    check(total == 4500 and len(ids) == 4500 and len(headwords) == 4500,
          "word count/uniqueness mismatch")
    check(ids == set(range(1_000_001, 1_004_501)), "noncontiguous stable IDs")
    check(len(subcategories) == 163, "wrong subcategory count")
    check(example_count == 2846 and len(example_ids) == 2846,
          "total example count/uniqueness mismatch")
    manifest = WORDS / "practical_16_v5_audio_words_only.csv"
    with manifest.open(encoding="utf-8", newline="") as handle:
        csv_rows = list(csv.DictReader(handle))
    check(len(csv_rows) == 4500, "audio manifest must list 4500 word-only jobs")
    csv_ids = set()
    for item in csv_rows:
        ident = int(item["id"])
        check(ident in by_id and ident not in csv_ids, "invalid manifest ID")
        csv_ids.add(ident)
        word = by_id[ident]
        check(item["hanzi"] == word["hanzi"]
              and item["pinyin"] == word["pinyin"]
              and item["category_id"] == word["category_id"]
              and item["tts_text"] == word["hanzi"]
              and item["audio_filename"] == f"practical_{ident}.mp3",
              f"incorrect manifest row: {ident}")
    print(f"PASS: {total} words, 16 categories, 163 subcategories, 16 PNG covers, "
          f"{len(csv_rows)} word-only audio rows, 0 collocations, "
          f"{example_count} bilingual examples in categories 01–08 and 12")


if __name__ == "__main__":
    main()
