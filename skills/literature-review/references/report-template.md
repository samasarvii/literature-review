# Report template

Headings and body follow the language the user asked in (the English
headings below are a scaffold). Keep the sources table complete: it is the part a reader
returns to.

```markdown
---
title: <question, as a short phrase>
date: <yyyy-mm-dd>
decision: <the decision this review serves, one sentence>
confidence: high | medium | low
---

# <Title>

## Frame
The decision, the user's context as understood (stack, scale,
constraints, settled decisions), and the sub-questions. State any
inference about context so it can be corrected.

## Summary
Five to ten lines. The recommendation, its confidence, and the one or
two findings that drive it. A reader who stops here knows what to do.

## Findings
One subsection per sub-question. Within each:

### <Sub-question>
**Consensus.** What rungs 1–2 agree on, with [S1], [S4] style links to
the sources table.
**Disagreement.** Both sides and the separating condition, if found.
**Open.** What is thin or unsourced. Folklore is named as folklore.

## Recommendation
For this context. Then:
- **Confidence**: level, and why in one line.
- **What would change it**: the fact or measurement that flips it.
- **Tensions**: conflicts with the user's settled decisions, if any.

## Sources
| # | Title | Author / org | Date | Rung | Evidence type | Notes |
|---|---|---|---|---|---|---|
| S1 | … | … | yyyy-mm (v3) | 1 | specification | read |
| S2 | … | … | yyyy | 2 | production experience | abstract only |
| S3 | … | … | yyyy | 2 | opinion | not fetched (paywall); cited only as "reported by" |

Each row: a link in the title, the rung from the source ladder, the
evidence type from the claim card, the version read when a source has
several, the final URL if redirected, and the status *read* /
*abstract only* / *not fetched*.

**Rejected / not cited.** One line per source seen but not used, with
the reason (rung 4, duplicate of Sn, not fetched within cap).
```
