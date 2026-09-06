# TEMPLATE — Best-of Roundup (multi-product scenario guide)

*Authored by the Boss 2026-09-05. Benchmark: `content/pages/best-solar-batteries-2026.md` (the site's gold standard). Section order maps 1:1 to it. Derived from seat rt-vs/rt-buyer findings + the 33-page structural scan.*

**Page types:** (A) installed/quote-based picks — batteries, whole systems, not Amazon-orderable; (B) Amazon-buyable picks — controllers, drop-in batteries, panels, power stations; (C) mixed. Mandatory/optional flags are per type.

**Core rule:** a roundup is a set of scenario matches, never a ranking. "Best for X" — with the criteria visible — or nothing. No "winner", no "#1", no "top-rated".

---

## Front matter skeleton (TOML)

```
+++
title = "Best [category] for [use case] [year]: [honest descriptor]"
slug = "best-[category]-[qualifier]"        # existing slug if rebuilding; NEW slug only for new pages
date = YYYY-MM-DD
draft = false
description = "[140–160 chars: the picks' classes, the scenario split, and the sourcing basis. No superlatives.]"
image = "/assets/images/[slug]/hero.jpg"
image_alt = "[Factual description]"
author = "Solar Powered Project"
image_width = 1200
image_height = 630
related = [
  "/pages/[cost-guide].html",
  "/pages/[comparison-page].html"
]
+++
```

---

## Ordered sections

### 0. Affiliate disclosure — MANDATORY
`{{< affiliate-disclosure >}}` immediately after front matter.

### 1. Quick answer — MANDATORY, first body block
- 2–5 sentences that (a) refuse the single "best" ("there are best *matches*"), (b) name the scenario axes readers split on, (c) state the one honest contrarian pick if one exists (batteries page: "the DIY path wins on math — but it is a build, not a purchase").
- Benchmark: "There is no single 'best' home battery in 2026 — there are best *matches*."

### 2. "How to read this page" methodology block — MANDATORY
- Must state: this is a spec-based comparison, not a test-lab review; where the numbers come from (manufacturer pages/datasheets, marked "per manufacturer spec"); how costs are banded (link to the site's cost guide); that picks are scenario matches, not rankings; link to `/pages/how-we-recommend.html`.
- Benchmark: "**How to read this page:** this is a spec-based comparison — we have not lab-tested these. Here is how we compared…"

### 3. Dated money-fact callout — MANDATORY when incentives/tax facts touch the category
- One short paragraph, dated, with the statutory basis. Current ground truth: "the 30% federal ITC expired December 31, 2025 (P.L. 119-21) — a 2026 install gets $0 federal credit." Never state incentive facts without a date.

### 4. Key takeaways — MANDATORY (4–6 bullets)
- Must include: the scenario-match rule; the research-not-tested honesty line; the dominant technology shift if one exists (e.g., "LiFePO4 dominates the 2026 home field"); the cost bands (labeled as bands, e.g., "$1,000–$1,400/kWh installed"); the not-Amazon clarification for type A pages ("installed batteries are quoted and installed by certified contractors — generally not Amazon items").

### 5. Comparison table — MANDATORY
- One row per pick/class; columns per `TABLE-FIELDS.md` for the niche; a "best for" column.
- Every spec column header or footnote carries sourcing: "per manufacturer spec"; table footnote lists sources with retrieval dates ("tesla.com; retrieved 2026-09-05") and an as-of caveat ("specs drift — verify against the current datasheet").
- No price column. A "typical price class" column (Budget/Mid/Premium) is allowed as T4 editorial band.

### 6. "Best for: N scenarios, not one winner" — MANDATORY
- One `### Best [scenario]: [product/class]` subsection per pick (3–5 typical).
- Each subsection: (a) 2–4 sentences of why — specs with "(per manufacturer spec)" attribution; (b) a closing "**Best for:**" sentence naming the reader it serves; (c) the tradeoff or catch ("The catch is…", "The tradeoff is…") — a pick without a stated catch fails review.
- Cross-link the decision guides that route readers here (e.g., diy-vs-installer).

### 7. Worked $ math — MANDATORY for cost-sensitive categories
- The site's reproducible arithmetic (usable kWh × $/kWh bands; $/usable-kWh over cycle life). Bands, never point prices. End with "planning bands, not quotes" + the get-three-quotes advice.

### 8. Questions to ask an installer/dealer — MANDATORY type A, optional type B
- 4–5 questions that separate a thoughtful quote from a price list (usable vs nameplate; continuous/surge; warranty terms in writing; outage behavior; expansion path).

### 9. "Not Amazon items" honesty block — MANDATORY type A
- Say plainly what cannot be ordered online and what can (the DIY path). This block is what earns the one box on a type A page.

### 10. Product boxes — type B/C: one per pick is allowed, but each box must pass the house anatomy
- `{{< product-box >}}` after its pick's subsection (not before the comparison table); target ≥60% into body; description must contain "(per manufacturer spec)", "Not for:", "The honest tradeoff:". Type A: at most ONE box (the DIY/building-block path), placed after the honesty block. Button is always `Check price on Amazon`.
- Ceiling: one box per distinct purchase decision. A roundup with 5 Amazon-orderable picks may carry up to 5 boxes ONLY if every pick's subsection earns its own; otherwise fewer.

### 11. FAQ + schema — MANDATORY
- 4–6 `{{< faq >}}` items incl. one honesty FAQ ("Did you test these?" → no; spec-based; how-we-recommend link) and one time-sensitive FAQ (incentive/status as of date). Then `{{< faq-schema >}}`.

### 12. Next logical reads — house convention
- 3–6 text links, `.html` URLs, to the cost/comparison/methodology pages that route into this decision.

---

## Pre-publish compliance checklist (roundup)

1. Quick answer refuses the single "best"; every pick is a "best for [scenario]" with a stated catch.
2. "How to read this page" block present; every table spec sourced ("per manufacturer spec") with retrieval-dated footnote; "specs drift" caveat present.
3. No prices, ratings, review text, availability, urgency, or "winner/#1/top-rated" anywhere; cost figures are labeled bands.
4. Any incentive/money fact carries its date and statute; `updated` front matter only on genuine revision.
5. Every box: house anatomy + uniform button + placement after its pick's argument; type A pages carry at most the one DIY-path box.
6. FAQ + `{{< faq-schema >}}` present incl. the honesty FAQ; internal links end `.html`; no URL of an existing page changed.
