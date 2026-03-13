#!/usr/bin/env python3
import json
import re
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "posts"
OUT = ROOT / "data" / "posts.json"


def extract(pattern: str, text: str, default: str = "") -> str:
    m = re.search(pattern, text, re.S)
    return m.group(1).strip() if m else default


def main():
    entries = []
    for p in sorted(POSTS_DIR.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        s = p.read_text(encoding="utf-8", errors="ignore")

        title = extract(r"<h1>(.*?)</h1>", s) or extract(r"<title>(.*?)</title>", s)
        meta = extract(r"<div class=\"meta\">(.*?)</div>", s)
        date = ""
        topic = ""
        if "·" in meta:
            parts = [x.strip() for x in meta.split("·")]
            if parts:
                date = parts[0]
            if len(parts) >= 3:
                topic = parts[2]

        source = extract(r"<strong>Source:</strong>\s*<a[^>]*href=\"([^\"]+)\"", s)
        image = extract(r"<img class=\"post-image\"[^>]*src=\"([^\"]+)\"", s)

        slug = p.stem
        lc_id = None
        m = re.match(r"leetcode-(\d+)-", slug)
        if m:
            lc_id = int(m.group(1))

        entries.append(
            {
                "slug": slug,
                "path": rel,
                "title": title,
                "date": date,
                "topic": topic,
                "leetcodeId": lc_id,
                "sourceUrl": source,
                "image": image,
            }
        )

    entries.sort(key=lambda x: (x.get("date", ""), x.get("slug", "")), reverse=True)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(
            {
                "generatedAt": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
                "count": len(entries),
                "posts": entries,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUT} ({len(entries)} posts)")


if __name__ == "__main__":
    main()
