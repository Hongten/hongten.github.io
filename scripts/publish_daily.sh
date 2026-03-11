#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT_DIR"

if [[ $# -lt 2 ]]; then
  cat <<'USAGE'
Usage:
  scripts/publish_daily.sh --id <leetcode_id> --title <problem_title> [options]

Required:
  --id            LeetCode id, e.g. 20
  --title         Problem title, e.g. "Valid Parentheses"

Optional (forwarded to generator):
  --topic         e.g. Stack
  --tag1          e.g. String
  --tag2          e.g. Stack
  --source-url    e.g. https://leetcode.com/problems/valid-parentheses/
  --summary-en    card summary on index

Example:
  scripts/publish_daily.sh \
    --id 155 \
    --title "Min Stack" \
    --topic "Stack" \
    --tag1 "Stack" \
    --tag2 "Design" \
    --source-url "https://leetcode.com/problems/min-stack/" \
    --summary-en "Bilingual interview-grade walkthrough of LeetCode 155: design decisions, constant-time operations, pitfalls, and 5-language code tabs."
USAGE
  exit 1
fi

LC_ID=""
TITLE=""
GEN_ARGS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --id)
      LC_ID="${2:-}"
      GEN_ARGS+=("--id" "${2:-}")
      shift 2
      ;;
    --title)
      TITLE="${2:-}"
      GEN_ARGS+=("--title" "${2:-}")
      shift 2
      ;;
    --topic|--tag1|--tag2|--source-url|--summary-en|--summary-zh)
      GEN_ARGS+=("$1" "${2:-}")
      shift 2
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

if [[ -z "$LC_ID" || -z "$TITLE" ]]; then
  echo "Error: --id and --title are required." >&2
  exit 2
fi

python3 scripts/gen_leetcode_post.py "${GEN_ARGS[@]}"

git add index.html posts/ assets/img/

if git diff --cached --quiet; then
  echo "No changes to commit."
  exit 0
fi

COMMIT_MSG="publish: leetcode ${LC_ID} ${TITLE,,}"
git commit -m "$COMMIT_MSG"
git push origin master

echo "✅ Published with commit: $COMMIT_MSG"
