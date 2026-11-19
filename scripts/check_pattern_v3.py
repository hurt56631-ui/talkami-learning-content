#!/usr/bin/env python3
"""Validate the V3 Burmese sentence-pattern card packs before publishing."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "content" / "patterns" / "catalog.json"
EXPECTED_PAGES = ("overview", "focus", "usage")

def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def require(value, message):
    if not value:
        raise AssertionError(message)

def check_text(obj, field, ctx):
    require(isinstance(obj, dict), f"{ctx}: expected object")
    require(isinstance(obj.get(field), str) and obj[field].strip(), f"{ctx}: missing {field}")

def check_item(obj, ctx):
    check_text(obj, "zh", ctx)
    check_text(obj, "my", ctx)

def validate():
    catalog = load(CATALOG)
    categories = catalog.get("items", [])
    require(len(categories) == 16, "Expected 16 pattern categories")
    require(catalog.get("item_count") == 500, "Catalog item_count must be 500")
    ids = set()
    numbers = set()
    examples = 0
    templates = 0
    dialogues = 0
    mistakes = 0
    for descriptor in categories:
        cid = descriptor["id"]
        assert descriptor.get("target") == "pattern_pack", cid
        source_path = ROOT / descriptor["source_data"]
        assert source_path.is_file(), source_path
        pack = load(source_path)
        assert pack["type"] == "pattern_pack", cid
        assert pack["category_id"] == cid, cid
        assert pack["version"] == descriptor["data_version"] == 3, cid
        items = pack["items"]
        assert len(items) == descriptor["item_count"] == pack["item_count"], cid
        for item in items:
            pid = item["id"]
            number = item["number"]
            assert pid == "pattern_" + number, pid
            assert pid not in ids and number not in numbers, pid
            ids.add(pid)
            numbers.add(number)
            for key in ("title", "formula", "example", "introduction"):
                check_text(item, key, pid)
            my = item.get("myanmar", {})
            check_text(my, "example_my", pid)
            check_text(my, "usage_my", pid)
            pages = item.get("card", {}).get("pages", [])
            assert len(pages) == 3, pid
            assert tuple(p.get("type") for p in pages) == EXPECTED_PAGES, pid
            overview, focus, usage = pages
            for p in pages:
                check_text(p, "note_my", pid)
            example_items = overview.get("items", [])
            assert len(example_items) == 3, pid
            for ex in example_items:
                check_item(ex, pid)
                examples += 1
            assert example_items[0]["zh"] == item["example"], pid
            assert example_items[0]["my"] == my["example_my"], pid
            templates_on_page = focus.get("templates", [])
            assert len(templates_on_page) == 2, pid
            for t in templates_on_page:
                check_text(t, "formula", pid)
                assert 1 <= len(t.get("examples", [])) <= 2, pid
                for ex in t["examples"]:
                    check_item(ex, pid)
                templates += 1
            dialogs = usage.get("dialogues", [])
            assert len(dialogs) == 1, pid
            for d in dialogs:
                turns = d.get("turns", [])
                assert len(turns) == 2, pid
                for turn in turns:
                    check_text(turn, "zh", pid)
                    check_text(turn, "my", pid)
                dialogues += 1
            wrongs = usage.get("mistakes", [])
            assert len(wrongs) <= 2, pid
            for mistake in wrongs:
                for key in ("wrong", "correct", "note_my"):
                    check_text(mistake, key, pid)
                mistakes += 1
    expected_numbers = {f"{i:03d}" for i in range(1, 501)}
    assert numbers == expected_numbers, "Pattern numbers must be continuous 001..500"
    assert len(ids) == 500, len(ids)
    assert examples == 1500, examples
    assert templates == 1000, templates
    assert dialogues == 500, dialogues
    print(f"OK: categories={len(categories)}, patterns={len(ids)}, "
          f"examples={examples}, templates={templates}, dialogues={dialogues}, "
          f"mistake_notes={mistakes}")
    print("NOTE: Structural validation does not replace Myanmar-native editorial review.")

if __name__ == "__main__":
    validate()
