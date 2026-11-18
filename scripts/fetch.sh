#!/bin/sh
# Mirror the LightAct 4 user docs as markdown into docs/.
# Source index: https://docs.lightact.com/llms.txt
# Every docs page is served as markdown when .md is appended to its URL.
# Usage: scripts/fetch.sh   (run from the repo root)
# Pages are overwritten in place. Nothing is deleted: pages that have gone
# from the live docs are listed at the end so a person can decide.
set -e
BASE=https://docs.lightact.com
mkdir -p docs
curl -sfL -A "Mozilla/5.0" -o docs/llms.txt "$BASE/llms.txt"
grep -oE "$BASE/[^) ]+\.md" docs/llms.txt | sort -u > docs/.urls

fetch_one() {
  u="$1"; rel=${u#https://docs.lightact.com/}; out="docs/$rel"
  mkdir -p "$(dirname "$out")"
  tmp=$(mktemp)   # left in the system temp folder, which the OS clears
  if curl -sfL -A "Mozilla/5.0" --max-time 40 --retry 3 "$u" > "$tmp"; then
    # Drop the boilerplate first line, images and GitBook block tags.
    sed -e '1{/^> For the complete documentation index/d;}' \
        -e 's/<figure>.*<\/figure>//g' -e 's/<img[^>]*>//g' \
        -e 's/!\[[^]]*\]([^)]*)//g' -e 's/{% [^%]*%}//g' "$tmp" \
      | cat -s > "$out"
  else
    echo "FAILED $u" >&2
  fi
}

# Run up to 8 fetches at a time.
i=0
while read -r u; do
  fetch_one "$u" &
  i=$((i + 1))
  [ $((i % 8)) -eq 0 ] && wait
done < docs/.urls
wait

want=$(wc -l < docs/.urls | tr -d ' ')
have=$(find docs -name '*.md' -size +0 | wc -l | tr -d ' ')
echo "live pages: $want, local pages: $have"
sed "s#^$BASE/#docs/#" docs/.urls | sort > docs/.live
find docs -name '*.md' | sort > docs/.local
comm -13 docs/.live docs/.local > docs/STALE.txt
[ -s docs/STALE.txt ] && echo "pages no longer in the live docs: see docs/STALE.txt"
date -u +%Y-%m-%d > docs/FETCHED; cp docs/FETCHED FETCHED

# Checksums of every page, so anyone can see which pages changed since the
# digests were written without the manual itself being published.
if command -v sha256sum >/dev/null 2>&1; then SUM="sha256sum"; else SUM="shasum -a 256"; fi
( cd docs && find . -name '*.md' | sort | while read -r f; do $SUM "$f"; done ) > manifest.sha256
echo "wrote manifest.sha256 ($(wc -l < manifest.sha256 | tr -d ' ') pages)"
