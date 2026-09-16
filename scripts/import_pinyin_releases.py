#!/usr/bin/env python3
"""Build browser Pinyin manifest from uploaded GitHub Release assets.

Release assets are the upload/archive layer. The generated manifest points the
Mini App to versioned raw.githubusercontent.com files, which can be fetched and
stored in IndexedDB for offline learning.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

REPO = "hurt56631-ui/talkami-learning-content"
EXTS = {".mp3", ".m4a", ".aac", ".wav", ".ogg", ".opus"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fp:
        for chunk in iter(lambda: fp.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", required=True)
    parser.add_argument("--parts", type=int, choices=[2, 3], default=3)
    parser.add_argument("--expected", type=int, default=1338)
    args = parser.parse_args()

    root = Path.cwd()
    out = root / "audio" / "pinyin" / f"v{args.version}"
    manifest_path = root / "manifests" / "pinyin" / "pinyin-manifest.json"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)

    items = []
    parts = []
    seen = set()
    total_bytes = 0

    for part in range(1, args.parts + 1):
        src = root / ".pinyin-release-staging" / f"part{part}"
        files = sorted([p for p in src.iterdir() if p.is_file() and p.suffix.lower() in EXTS], key=lambda x: x.name)
        if not files:
            raise SystemExit(f"Missing audio in {src}")

        target = out / f"part{part}"
        target.mkdir(parents=True)
        part_bytes = 0
        for file in files:
            if file.name in seen:
                raise SystemExit(f"Duplicate audio name: {file.name}")
            seen.add(file.name)
            dst = target / file.name
            shutil.copy2(file, dst)
            size = dst.stat().st_size
            total_bytes += size
            part_bytes += size
            items.append({
                "id": f"part{part}:{file.name}",
                "name": file.name,
                "url": f"https://raw.githubusercontent.com/{REPO}/main/audio/pinyin/v{args.version}/part{part}/{quote(file.name, safe='')}",
                "size": size,
                "digest": f"sha256:{sha256_file(dst)}",
                "part": part,
            })
        parts.append({
            "part": part,
            "release_tag": f"pinyin-audio-v{args.version}-part{part}",
            "count": len(files),
            "bytes": part_bytes,
        })

    if len(items) != args.expected:
        raise SystemExit(f"Expected {args.expected} audio files, got {len(items)}")

    items.sort(key=lambda x: x["name"].casefold())
    manifest = {
        "schema_version": 1,
        "ready": True,
        "content_version": str(args.version),
        "generated_at": datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
        "repository": REPO,
        "storage": "indexeddb",
        "runtime_source": "github-raw",
        "download_concurrency": 4,
        "total_items": len(items),
        "total_bytes": total_bytes,
        "parts": parts,
        "items": items,
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
