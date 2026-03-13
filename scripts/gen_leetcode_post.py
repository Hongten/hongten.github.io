#!/usr/bin/env python3
import argparse
import datetime as dt
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "templates" / "leetcode-post.html.tpl"
INDEX = ROOT / "index.html"
POSTS = ROOT / "posts"
IMAGES = ROOT / "assets" / "img"


def slugify(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def escape_code(code: str) -> str:
    return html.escape(code, quote=False)


def collect_existing_leetcode_ids() -> set[int]:
    ids = set()
    for p in POSTS.rglob("leetcode-*.html"):
        m = re.match(r"leetcode-(\d+)-", p.stem)
        if m:
            ids.add(int(m.group(1)))
    return ids


def build_svg(path: Path, post_title: str, topic: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630" role="img" aria-label="{html.escape(post_title)} diagram">
  <defs>
    <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <text x="60" y="110" fill="#e5e7eb" font-size="48" font-family="Inter,Arial,sans-serif" font-weight="700">{html.escape(post_title)}</text>
  <text x="60" y="170" fill="#9ca3af" font-size="30" font-family="Inter,Arial,sans-serif">Interview-grade bilingual template</text>
  <rect x="60" y="230" width="1080" height="320" rx="18" fill="#1f2937" stroke="#374151"/>
  <text x="100" y="300" fill="#93c5fd" font-size="34" font-family="Inter,Arial,sans-serif">Topic: {html.escape(topic)}</text>
  <text x="100" y="360" fill="#e5e7eb" font-size="30" font-family="Inter,Arial,sans-serif">EN-first · CN-second · 5 language tabs</text>
  <text x="100" y="420" fill="#86efac" font-size="30" font-family="Inter,Arial,sans-serif">Author: Tom🦞</text>
</svg>
'''
    path.write_text(svg, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Generate LeetCode blog post + prepend index card")
    parser.add_argument("--id", required=True, help="LeetCode problem id, e.g. 155")
    parser.add_argument("--title", required=True, help="Problem title, e.g. Min Stack")
    parser.add_argument("--topic", default="Array", help="Topic shown in meta")
    parser.add_argument("--tag1", default="Array")
    parser.add_argument("--tag2", default="Algorithm")
    parser.add_argument("--source-url", help="LeetCode source URL")
    parser.add_argument("--summary-en", default="Bilingual interview-grade walkthrough with baseline, optimal approach, pitfalls, and 5-language code tabs.")
    parser.add_argument("--summary-zh", default="双语面试级讲解：包含基线思路、最优解、常见陷阱与 5 语言代码标签页。")
    args = parser.parse_args()

    lc_id = int(str(args.id).strip())
    problem_name = args.title.strip()
    slug = f"leetcode-{lc_id}-{slugify(problem_name)}"
    post_file = f"{slug}.html"

    existing_ids = collect_existing_leetcode_ids()
    if lc_id in existing_ids:
        raise SystemExit(f"LeetCode {lc_id} already exists. Abort to prevent duplicates.")

    now = dt.datetime.now(dt.timezone(dt.timedelta(hours=8)))
    year = now.strftime("%Y")
    date_str = now.strftime("%Y-%m-%d")
    iso_str = now.strftime("%Y-%m-%dT%H:%M:%S+08:00")

    source_url = args.source_url or f"https://leetcode.com/problems/{slugify(problem_name)}/"
    post_title = f"LeetCode {lc_id}: {problem_name}"
    full_post_title = f"{post_title} ({args.topic})"

    image_rel = f"leetcode/{year}/leetcode-{lc_id}-{date_str.replace('-', '')}.svg"

    template = TEMPLATE.read_text(encoding="utf-8")

    replacements = {
        "POST_TITLE": full_post_title,
        "META_DESCRIPTION": f"Interview-grade bilingual tutorial for LeetCode {lc_id} with brute-force baseline, optimization, pitfalls, and 5-language implementations.",
        "OG_DESCRIPTION": "Detailed English + 中文 guide with insight, algorithm steps, complexity, pitfalls, and code tabs.",
        "POST_FILE": post_file,
        "META_LINE": f"{date_str} · LeetCode · {args.topic}",
        "LC_ID": str(lc_id),
        "TAG_1": args.tag1,
        "TAG_2": args.tag2,
        "PROBLEM_NAME": problem_name,
        "SOURCE_URL": source_url,
        "IMAGE_FILE": image_rel,
        "IMAGE_ALT": f"LeetCode {lc_id} {problem_name} diagram",
        "EN_PROBLEM_SUMMARY": f"Given problem LeetCode {lc_id} - {problem_name}, return the required output under problem constraints.",
        "EN_KEY_INSIGHT": "Identify the invariant first, then choose data structure / traversal strategy that enforces it with minimal overhead.",
        "EN_BRUTE_FORCE": "Start from a direct simulation or enumeration baseline. It is easy to reason about but often too slow for larger input sizes.",
        "EN_STEPS": "1) Clarify state/invariant.<br/>2) Traverse input once or with bounded revisits.<br/>3) Update structure/state by invariant.<br/>4) Derive answer from maintained state.",
        "EN_COMPLEXITY": "Time: <code>O(n)</code> (or best achievable for this strategy).<br/>Space: <code>O(n)</code> worst case depending on auxiliary structure.",
        "EN_PITFALLS": "- Missing edge cases (empty/min size).<br/>- Off-by-one boundaries.<br/>- Incomplete state reset/update.",
        "ZH_PROBLEM_SUMMARY": f"给定 LeetCode {lc_id} - {problem_name}，在题目约束下返回正确结果。",
        "ZH_KEY_INSIGHT": "先找不变量，再选能稳定维护不变量的数据结构/遍历方式。",
        "ZH_BRUTE_FORCE": "可先从直接模拟或枚举入手，便于验证正确性，但在大输入下通常性能不足。",
        "ZH_STEPS": "1）明确状态与不变量。<br/>2）一次遍历或有限回看。<br/>3）按不变量更新状态。<br/>4）由状态推导最终答案。",
        "ZH_COMPLEXITY": "时间复杂度：<code>O(n)</code>（或该策略可达最优）。<br/>空间复杂度：<code>O(n)</code>（取决于辅助结构）。",
        "ZH_PITFALLS": "- 漏掉边界输入（空、最小规模）。<br/>- 下标越界或 off-by-one。<br/>- 状态更新不完整。",
        "CODE_JAVA": escape_code("// TODO: Replace with final Java solution\nclass Solution {\n    public int solve(...) {\n        return 0;\n    }\n}"),
        "CODE_GO": escape_code("// TODO: Replace with final Go solution\nfunc solve(...) int {\n    return 0\n}"),
        "CODE_CPP": escape_code("// TODO: Replace with final C++ solution\nclass Solution {\npublic:\n    int solve(...) {\n        return 0;\n    }\n};"),
        "CODE_PYTHON": escape_code("# TODO: Replace with final Python solution\nclass Solution:\n    def solve(self, ...):\n        return 0"),
        "CODE_JS": escape_code("// TODO: Replace with final JavaScript solution\nfunction solve(...) {\n  return 0;\n}"),
    }

    content = template
    for k, v in replacements.items():
        content = content.replace("{{" + k + "}}", v)

    post_path = POSTS / post_file
    if post_path.exists():
        raise SystemExit(f"Post already exists: {post_path}")

    post_path.write_text(content, encoding="utf-8")
    build_svg(IMAGES / image_rel, full_post_title, args.topic)

    index_content = INDEX.read_text(encoding="utf-8")
    marker = '<section id="posts">\n'
    if marker not in index_content:
        raise SystemExit("Cannot find posts section marker in index.html")

    card = f'''      <article class="card post-card" data-date="{iso_str}">
        <h2><a href="./posts/{post_file}">{full_post_title}</a></h2>
        <div class="meta">{date_str} · LeetCode · {args.topic}</div>
        <p>{args.summary_en}</p>
        <a href="./posts/{post_file}">Read more →</a>
      </article>

'''

    INDEX.write_text(index_content.replace(marker, marker + card, 1), encoding="utf-8")

    print(f"Generated: posts/{post_file}")
    print(f"Generated: assets/img/{image_rel}")
    print("Updated: index.html")


if __name__ == "__main__":
    main()
