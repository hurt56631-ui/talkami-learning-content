#!/usr/bin/env python3
"""Validate Myanmar phonetic cues in HSK 3.0 levels 1-4."""
import json
from pathlib import Path

PACKS = Path(__file__).resolve().parents[1] / "content" / "words" / "packs"
LEVELS = (
    ("hsk1_3_0.json", 300, 1),
    ("hsk2_3_0.json", 200, 301),
    ("hsk3_3_0.json", 500, 501),
    ("hsk4_3_0.json", 1000, 1001),
)


def ensure(ok, message):
    if not ok:
        raise AssertionError(message)


def main():
    all_ids = set()
    for filename, expected_count, first_id in LEVELS:
        entries = json.loads((PACKS / filename).read_text(encoding="utf-8"))
        ensure(isinstance(entries, list) and len(entries) == expected_count,
               f"{filename}: expected {expected_count} words")
        ids = []
        for word in entries:
            ident = word.get("id")
            ids.append(ident)
            for field in ("hanzi", "pinyin", "burmese", "phonetic_my"):
                ensure(isinstance(word.get(field), str) and word[field].strip(),
                       f"{filename} ID={ident}: missing {field}")
            phonetic = word["phonetic_my"].strip()
            ensure(any("\u1000" <= ch <= "\u109f" for ch in phonetic),
                   f"{filename} ID={ident}: Myanmar script missing")
            ensure(not any(ch.isascii() and ch.isalnum() for ch in phonetic),
                   f"{filename} ID={ident}: Latin letter/digit in phonetic")
            ensure(isinstance(word.get("examples"), list) and bool(word["examples"]),
                   f"{filename} ID={ident}: missing original examples")
            if filename != "hsk1_3_0.json":
                hanzi = [ch for ch in word["hanzi"] if "\u3400" <= ch <= "\u9fff"]
                pinyin = word["pinyin"].replace(" ", "").lower()
                erhua = word["hanzi"].endswith("儿") and pinyin.endswith("r")
                expected_syllables = len(hanzi) - int(erhua)
                ensure(len(phonetic.split()) == expected_syllables,
                       f"{filename} ID={ident}: phonetic syllable count mismatch")
        ensure(len(ids) == len(set(ids)), f"{filename}: duplicate word IDs")
        ensure(set(ids) == set(range(first_id, first_id + expected_count)),
               f"{filename}: stable ID range changed")
        ensure(not all_ids.intersection(ids), f"{filename}: duplicate across HSK levels")
        all_ids.update(ids)
        print(f"PASS {filename}: {len(ids)} IDs and Myanmar phonetics complete")
    ensure(len(all_ids) == 2000, "HSK 3.0 total is not 2000")
    print("PASS HSK 3.0: 2000/2000 Myanmar phonetics present; IDs intact")


if __name__ == "__main__":
    main()
