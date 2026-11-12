#!/usr/bin/env python3
"""Repackage older Talkami batch TTS exports with the Mini App canonical IDs.

python remap_tts_zip.py <TTS_export.zip> <01_id_mapping.json> [01.zip]
"""
import hashlib, json, sys, zipfile
from pathlib import Path

def main():
    if len(sys.argv) not in (3, 4):
        sys.exit("Usage: python remap_tts_zip.py TTS_export.zip 01_id_mapping.json [01.zip]")
    source = Path(sys.argv[1])
    index = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    dest = Path(sys.argv[3]) if len(sys.argv) == 4 else Path(index["theme_id"] + ".zip")
    if source.resolve() == dest.resolve():
        sys.exit("Input and output must have different paths")
    names = index["legacy_to_canonical"]
    done = set()
    with zipfile.ZipFile(source) as src, zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as out:
        for entry in src.infolist():
            if entry.is_dir() or not entry.filename.lower().endswith(".mp3"):
                continue
            old_id = Path(entry.filename).stem
            if old_id not in names: sys.exit("Unknown audio ID: " + old_id)
            new_id = names[old_id]
            if new_id in done: sys.exit("Duplicated canonical ID: " + new_id)
            clip = src.read(entry)
            if len(clip) > 512*1024: sys.exit("Audio >512 KB: " + old_id)
            if len(clip) <= 16 or not (clip.startswith(b"ID3") or (clip[0]==255 and clip[1] & 224 == 224)):
                sys.exit("Invalid MP3 file: " + old_id)
            out.writestr("audio/" + new_id + ".mp3", clip)
            done.add(new_id)
    print("Output:", dest)
    print("Audio clips:", len(done), "/", index["expected_total_mp3"])
    print("SHA256:", hashlib.sha256(dest.read_bytes()).hexdigest())
    print("ZIP size:", dest.stat().st_size)
    if len(done)!=index["expected_total_mp3"]:
        print("Incomplete recordings: do NOT enable this ZIP for in-app playback yet.")
    if dest.stat().st_size>30*1024*1024:
        print("ZIP too large for current app (30 MB maximum).")
if __name__ == "__main__": main()
