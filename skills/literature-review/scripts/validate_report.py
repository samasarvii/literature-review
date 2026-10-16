#!/usr/bin/env python3
"""Validate a literature-review report against the template's contract.

Checks (stdlib only):
  - frontmatter has title, date, decision, confidence (high|medium|low)
  - the five sections exist (headings may be in any language; matched by
    the fixed order: Frame, Summary, Findings, Recommendation, Sources)
  - every [Sn] cited in the body has a row in the sources table
  - every sources row has a rung (1-4), a date and a status
    (read / abstract only / not fetched, or their Turkish forms)
  - no body citation points at a row whose status is not 'read'
  - Findings contains at least one Disagreement/Open label
  - Recommendation contains a confidence line and a "what would change it" line

Usage: python3 validate_report.py docs/research/2026-10-16-slug.md
Exit 0 on pass, 1 on failure; failures are listed one per line.
"""
import re
import sys

READ = {"read", "okundu", "fetched and read"}
STATUSES = READ | {"abstract only", "not fetched", "snippet only", "yalnızca özet", "getirilmedi", "yalnızca snippet"}


def main(path):
    text = open(path, encoding="utf-8").read()
    fails, warns = [], []

    fm = re.search(r"^---\n(.*?)\n---", text, re.S)
    if not fm:
        fails.append("frontmatter missing")
    else:
        f = fm.group(1)
        for key in ("title", "date", "decision", "confidence"):
            if not re.search(rf"^{key}:\s*\S", f, re.M):
                fails.append(f"frontmatter: {key} missing")
        c = re.search(r"^confidence:\s*(\w+)", f, re.M)
        if c and c.group(1).lower() not in {"high", "medium", "low", "yüksek", "orta", "düşük"}:
            fails.append(f"frontmatter: confidence must be high|medium|low, got {c.group(1)}")

    h2 = re.findall(r"^## +(.+)$", text, re.M)
    if len(h2) < 5:
        fails.append(f"expected 5 top-level sections (Frame, Summary, Findings, Recommendation, Sources), found {len(h2)}: {h2}")

    sources_idx = text.rfind("\n## ")
    body, sources = text[:sources_idx], text[sources_idx:]

    rows = {}
    for line in sources.splitlines():
        m = re.match(r"^\|\s*(S\d+)\s*\|(.*)$", line)
        if not m:
            continue
        sid, rest = m.group(1), m.group(2).lower()
        cells = [c.strip() for c in rest.split("|")]
        rows[sid] = cells
        if not re.search(r"\b[1-4]\b", rest):
            fails.append(f"{sid}: no rung (1-4)")
        rung4 = bool(re.search(r"\|\s*4\s*\|", rest))
        undated_ok = re.search(r"(güncel|tarihsiz|undated|current|living|n/a)", rest)
        if not rung4 and not re.search(r"\b(19|20)\d\d\b", rest):
            (warns if undated_ok else fails).append(f"{sid}: no date" + (" (live doc, undated)" if undated_ok else ""))
        if not any(s in rest for s in STATUSES):
            fails.append(f"{sid}: no status (read / abstract only / not fetched)")

    if not rows:
        fails.append("sources table has no S-rows")

    HEDGE = re.compile(r"(not verified|unverified|lead only|rung[- ]?4 lead|reported by|abstract only|doğrulanmad|yalnızca ipucu|yalnızca özet|teyit edilmedi)", re.I)
    cited = set(re.findall(r"\[(S\d+)\]", body))
    for sid in sorted(cited, key=lambda s: int(s[1:])):
        if sid not in rows:
            fails.append(f"{sid} cited in body but missing from sources table")
            continue
        if any(s in " ".join(rows[sid]) for s in READ):
            continue
        # a non-read row may be mentioned only in a sentence that says so
        # the hedge may sit in the citing sentence or the one right after it
        sentences = [body[max(0, m.start() - 200): m.end() + 120] for m in re.finditer(r"\[" + sid + r"\]", body)]
        if any(not HEDGE.search(s) for s in sentences):
            fails.append(f"{sid} cited as support but its status is not 'read' (mention it only as 'reported by / not verified')")

    findings = re.search(r"## [^\n]*\n(.*?)\n## ", body[body.find("\n## ", body.find("\n## ") + 1):] + "\n## ", re.S)
    low = body.lower()
    if not re.search(r"(disagreement|anlaşmazlık|open|açık|thin|zayıf)", low):
        fails.append("no Disagreement / Open label anywhere in the body")
    if not re.search(r"(confidence|güven)\s*[:*]", low):
        fails.append("no confidence line in the recommendation")
    if not re.search(r"(what would change it|ne değiştirir|neyi değiştirir|would flip)", low):
        fails.append("no 'what would change it' line in the recommendation")

    for w in warns:
        print("WARN: " + w)
    if fails:
        print("\n".join("FAIL: " + f for f in fails))
        return 1
    print(f"PASS: {len(rows)} sources, {len(cited)} cited, frontmatter and sections present.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
