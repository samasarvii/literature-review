#!/usr/bin/env python3
"""Check the sources table of a literature-review report.

For every row in the "## Sources" table (or its localized heading) that
links to a URL:
  1. fetch the URL and report the HTTP status (resolves / redirects / fails);
  2. if the row's notes carry a quoted passage ("...") or a `quote:` field,
     check that the passage actually appears on the fetched page.

Stdlib only. Usage:
    python3 check_sources.py docs/research/2026-10-16-slug.md [--timeout 15]

Exit code 0 when every link resolves and every quoted passage is found,
1 otherwise. The summary is printed as Markdown so it can be pasted into
the report's "Verification" line.
"""
import argparse
import html
import re
import sys
import urllib.error
import urllib.request

UA = "literature-review-check/0.3 (+https://github.com/samasarvii/literature-review)"
ROW_RE = re.compile(r"^\|\s*(S\d+)\s*\|(.*)$")
URL_RE = re.compile(r"\((https?://[^)\s]+)\)")
QUOTE_RE = re.compile(r"[\"“]([^\"”]{12,})[\"”]")


def fetch(url, timeout):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(2_000_000).decode(r.headers.get_content_charset() or "utf-8", "replace")
            return r.status, r.geturl(), body
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception as e:  # noqa: BLE001
        return None, url, str(e)


def normalize(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"\s+", " ", s).strip().lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--timeout", type=int, default=15)
    args = ap.parse_args()

    rows = []
    for line in open(args.report, encoding="utf-8"):
        m = ROW_RE.match(line)
        if not m:
            continue
        sid, rest = m.group(1), m.group(2)
        urls = URL_RE.findall(rest)
        quotes = [q.strip() for q in QUOTE_RE.findall(rest)]
        rows.append((sid, urls[0] if urls else None, quotes, rest))

    if not rows:
        print("No sources table rows (| S1 | ... ) found.")
        return 1

    ok = True
    print("| # | status | final URL | quote |")
    print("|---|---|---|---|")
    for sid, url, quotes, rest in rows:
        if not url:
            print(f"| {sid} | no link | — | — |")
            ok = False
            continue
        status, final, body = fetch(url, args.timeout)
        resolves = status is not None and status < 400
        if not resolves:
            ok = False
        qres = "—"
        if quotes:
            text = normalize(body)
            hits = [normalize(q) in text for q in quotes]
            qres = f"{sum(hits)}/{len(hits)} found"
            if not all(hits):
                ok = False
        red = "" if final == url else f" → {final}"
        print(f"| {sid} | {status if status is not None else 'ERR'} | {url}{red} | {qres} |")

    print()
    print("All links resolve and all quoted passages were found." if ok else "Some links or passages failed; fix the rows above before calling the report done.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
