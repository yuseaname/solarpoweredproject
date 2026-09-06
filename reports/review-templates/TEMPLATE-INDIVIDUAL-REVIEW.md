<!-- Authored by agency seat glm-xo-3 (run rt-template), extracted and reviewed by the Boss 2026-09-05.
     NOTE: the Victron micro-example's warranty line ("5-year") is ILLUSTRATIVE — re-verify against
     the manufacturer's warranty page before publishing any real page from this template. -->

```markdown
# TEMPLATE — Individual Product Review (single-product page)

**Page type status:** NEW. The site has zero standalone individual-review pages; this template defines the type. It is buildable entirely with existing shortcodes (`affiliate-disclosure`, `product-box`, `faq`, `faq-schema`, `callout`) and the default `single.html` layout. Use for NEW slugs only — never change an existing URL.

**Honesty frame (non-negotiable):** this site tests NOTHING. An individual review here is a **spec-based evaluation**: manufacturer-published facts (T2), third-party sources only with URL + retrieval date (T3), and clearly labeled editorial judgment (T4). The "What this review is (and isn't)" block is mandatory and must appear before any product claim.

---

## Front matter skeleton (TOML — site conventions)

```
+++
title = "[Product name] review: specs, system fit, and honest limits"
slug = "[new-slug]"                      # NEW slug; uglyURLs add .html automatically
date = YYYY-MM-DD
draft = true                             # flip to false at publish
description = "[150–160 chars: what it is, the scenario it fits, the main tradeoff. No superlatives, no 'best', no urgency.]"
image = "/assets/images/[slug]/[slug]-hero.jpg"
image_alt = "[Factual description of the image]"
author = "Solar Powered Project"
image_width = 1200
image_height = 630
# updated = YYYY-MM-DD                   # uncomment ONLY when the page is actually revised
related = [
  "/pages/[sizing-or-cost-guide].html",
  "/pages/[comparison-page].html"
]
+++
```

Notes: `description` becomes the "In brief" dek — the only above-the-fold summary the layout guarantees, so the body must open with its own decision block. `single.html` renders kicker / H1 / dek / By {author} / Published {date} / Updated (only if `updated` set) / reading time / TOC rail (>800 words).

---

## Ordered sections

### 0. Affiliate disclosure — MANDATORY
Immediately after front matter: `{{< affiliate-disclosure >}}`. Present on all money pages.

### 1. Quick verdict (decision block) — MANDATORY
- **Purpose:** the dek is only a summary; the body must supply the decision immediately (house norm: quick-answer block in the first ~25 lines).
- **Must appear:** 2–4 sentences naming (a) what the product is, (b) the specific scenario it fits, (c) the one spec that decides fit, (d) the main tradeoff. Scenario-match framing only — never "the best X".
- **Compliance:** no star ratings, no "winner" language without conditions, no urgency.

### 2. "What this review is (and isn't)" — MANDATORY, before any product claim
- **Purpose:** structure the honesty in. This block is what makes the page type legitimate.
- **Must appear, verbatim pattern:**
  > This is a **spec-based review**. We did not bench-test this unit, and no manufacturer sent it to us. Every number below comes from the manufacturer's published documentation (marked "per manufacturer spec" with the retrieval date); anything from a third party carries its own URL and retrieval date; anything that is our judgment is labeled as such. How products earn a mention: [how we recommend](/pages/how-we-recommend.html).
- **Compliance:** never imply hands-on use, ownership, or measurement. Retrieval dates required on first mention of each fact family.

### 3. Key specifications table — MANDATORY
- **Purpose:** the evidence base. Columns per TABLE-FIELDS.md for the niche.
- **Must appear:** every spec row carries a per-row sourcing placeholder — `per manufacturer spec, retrieved [YYYY-MM-DD]` (T2), or `per [third party], [URL], retrieved [date]` (T3), or `editorial estimate` (T4, bands only).
- **Compliance:** NO price row, NO rating row, NO availability row. End the table with an as-of line: "Specs verified as of [date] against the manufacturer's current published documentation — verify against the live datasheet before buying; specs drift."

### 4. What the specs mean for your build — MANDATORY
- **Purpose:** the value section. Turn specs into the reader's arithmetic: sizing check, compatibility check, runtime/harvest math using the site's standard formulas (e.g., controller amps ≈ watts ÷ battery voltage × 1.25; cold-adjusted Voc; usable Wh = Ah × V × DoD).
- **Must appear:** at least one fully worked example with the reader's variables shown. All math must be reproducible from stated inputs.
- **Compliance:** physics and arithmetic are site-derived (T4 method, T2 inputs) — label assumptions.

### 5. Who it's for / Not for / Alternatives to consider — MANDATORY (three labeled sub-blocks)
- **Who it's for:** specific scenarios tied to specs ("your sizing math lands at 20–30 A on a 100 V rail").
- **Not for:** the honest ceiling — the array/bank/load size where this product stops being the answer, and what class takes over.
- **Alternatives to consider:** name ≥1 real alternative with a one-line spec reason (T2), even without a link. A review that names no alternative is a brochure.

### 6. Warranty & durability — MANDATORY
- **Must appear:** warranty years; what's covered (product vs performance; capacity-retention or throughput terms if stated); installation requirements attached to the warranty; prorated vs full replacement if known. Close with: "Warranty terms change — verify current terms on the manufacturer's warranty page before purchase."
- **Compliance:** T2 only; never characterize reliability from reviews or anecdotes (that would be T5-grade hearsay — not allowed).

### 7. Time-sensitivity handling — MANDATORY
- The "Specs verified as of [date]" line (section 3) plus: any money-adjacent fact (incentives, cost bands) carries its own as-of date; the `updated` front-matter field is bumped only on real revision; no urgency copy ever ("limited time", "prices going up").

### 8. Known limits and failure modes — OPTIONAL but recommended
- Only documented limits: manufacturer-published deratings/cutoffs (T2) or cited third-party documentation (T3). No invented anecdotes, no review summaries.

### 9. Product box — MANDATORY, PLACEMENT RULE: CTA AFTER VALUE
- **Rule:** exactly one `{{< product-box >}}`, placed **after** the spec table, the worked math, and who-for/not-for — target ≥60% into the body (house norm from the 33-page structural scan; hard floor: never before section 5).
- **Params:** `asin`, `name`, `label`, `description`, `button="Check price on Amazon"` (uniform sitewide string — never vary it).
- **Description house style (all three required):** "(per manufacturer spec)" + a "Not for: …" sentence + "The honest tradeoff: …" sentence. No prices, no ratings, no urgency in the description. The box renders its own disclosure line and `rel="sponsored nofollow noopener"`.

### 10. FAQ + schema — MANDATORY
- 4–6 `{{< faq "Question" >}}…{{< /faq >}}` items, then `{{< faq-schema >}}` (sitewide convention; the FAQPage JSON-LD is emitted from the collected questions).
- Must include one honesty FAQ: "Did you test this?" → the no-testing answer.

### 11. Next logical reads — house convention
- Text-link anchors to sizing/cost/comparison pages, `.html` URLs (uglyURLs — never bare slugs in hrefs).

---

## FILLED MICRO-EXAMPLE — Victron SmartSolar MPPT 100/30

```
+++
title = "Victron SmartSolar MPPT 100/30 review: specs, sizing fit, and honest limits"
slug = "victron-smartsolar-100-30-review"
date = 2026-09-06
draft = false
description = "Spec-based review of the Victron SmartSolar 100/30: 100V input, 30A output, where it fits a 12V or 24V build, and the array ceilings that disqualify it."
image = "/assets/images/victron-smartsolar-100-30-review/hero.jpg"
image_alt = "Victron SmartSolar MPPT 100/30 charge controller on a workshop bench"
author = "Solar Powered Project"
image_width = 1200
image_height = 630
related = [
  "/pages/best-mppt-charge-controllers.html",
  "/pages/mppt-vs-pwm.html"
]
+++

{{< affiliate-disclosure >}}

## Quick verdict

The Victron SmartSolar 100/30 is a 100V-input, 30A-output MPPT charge controller
(per manufacturer spec) that fits small-to-mid 12V and 24V builds — roughly arrays
up to ~400W on a 12V bank or ~800W on 24V. The spec that decides fit is your
cold-morning string voltage against that 100V input ceiling: cross it and you need
the 150V line, not this unit. The tradeoff is price per amp — budget controllers
deliver the same charge current for less.

**What this review is (and isn't).** This is a spec-based review. We did not
bench-test this unit, and no manufacturer sent it to us. Every number below comes
from the manufacturer's published documentation, marked "per manufacturer spec"
with the retrieval date; third-party figures carry their own source and date; our
judgments are labeled as such. How products earn a mention on this site:
[how we recommend](/pages/how-we-recommend.html).

## Key specifications

| Spec | Value | Source |
| :-- | :-- | :-- |
| Max PV input voltage | 100 V | per manufacturer spec, retrieved 2026-09-06 |
| Max charge current | 30 A | per manufacturer spec, retrieved 2026-09-06 |
| Rated max PV power | ~400 W @ 12 V / ~800 W @ 24 V | per manufacturer spec, retrieved 2026-09-06 |
| Battery systems | 12 V / 24 V auto-detect | per manufacturer spec, retrieved 2026-09-06 |
| Monitoring | Bluetooth built-in (VictronConnect) | per manufacturer spec, retrieved 2026-09-06 |
| Lithium charging profiles | Yes (presets incl. LiFePO4) | per manufacturer spec, retrieved 2026-09-06 |
| Typical price class | Mid-range (bottom of the $250–$600 MPPT band) | editorial band — see our [MPPT cost guide](mppt-charge-controller-cost.html) |

Specs verified as of 2026-09-06 against the manufacturer's current published
documentation — verify against the live datasheet before buying; specs drift.

## What the specs mean for your build

**Charge-current check.** Controller amps ≈ panel watts ÷ battery voltage × 1.25.
A 300W array on a 12V bank: 300 ÷ 12.8 × 1.25 ≈ **29 A** — inside the 30A rating
with the headroom rule satisfied. The same 400W array: 400 ÷ 12.8 × 1.25 ≈ **39 A**
— past 30A once headroom is applied, which is why ~400W @ 12V is this unit's
practical ceiling, not its marketing number.

**Cold-morning voltage check.** Panel Voc rises ~0.3% per °C below 25°C. Three
100W panels in series at 22V Voc each = 66V at STC; on a −10°C morning:
66 × (1 + 0.003 × 35) ≈ **73 V** — comfortably under the 100V input. Four panels:
88 × 1.105 ≈ **97 V** — under the limit with almost no margin. That is a
"step up to the 150V class" situation, not a "close enough" one.

## Who it's for / Not for / Alternatives

**Who it's for:** builds whose sizing math lands at 20–30 A on a 100 V rail —
~400W on 12V or ~800W on 24V — who want built-in Bluetooth monitoring and lithium
presets without adding a separate monitor (per manufacturer spec).

**Not for:** 48V banks, arrays above ~400W @ 12V / ~800W @ 24V, or strings whose
cold-adjusted Voc can exceed 100V — the Victron 150V line (or another brand's
higher-voltage class) is the next step. Also not for budget-first builds under
~200W of array, where a ~$25 PWM unit can be the honest choice — see
[MPPT vs PWM](mppt-vs-pwm.html) for the threshold math.

**Alternatives to consider:** EPEver Tracer 4210AN (40A/100V, display, wireless
monitoring via optional BT-1 — per manufacturer spec) and Renogy Rover 40A
(40A/100V, built-in Bluetooth — per manufacturer spec) both deliver more charge
current in the budget class; the Victron premium buys firmware maturity and the
monitoring ecosystem, not amps.

## Warranty & durability

Victron publishes a 5-year warranty period for the SmartSolar line (per
manufacturer spec, retrieved 2026-09-06) — verify current terms on the
manufacturer's warranty page before purchase. The documented-limits pattern of
the spec sheet (published self-consumption, efficiency curves, and operating
ranges) is the durability signal we can honestly point to; we make no
reliability claims beyond it.

## Frequently Asked Questions

{{< faq "Did you test this charge controller?" >}}
No. This is a spec-based review built from the manufacturer's published
documentation, retrieved 2026-09-06. We run no test lab and accept no review
units; the sizing and compatibility math above is arithmetic you can re-run
with your own array numbers.
{{< /faq >}}

{{< faq "Will the 100/30 run my 48V bank?" >}}
No. It auto-detects 12V/24V systems (per manufacturer spec); 48V banks need a
controller rated for 48V — Victron's 150V-class units are the usual next step.
{{< /faq >}}

{{< faq "How much more harvest does MPPT give over PWM?" >}}
It depends on conditions: roughly 0–10% on a hot roof, 10–20% on a mild day,
15–30% on cold clear days. The often-quoted "30% more" is a best-case snapshot,
not an everyday average — the full math is in [MPPT vs PWM](mppt-vs-pwm.html).
{{< /faq >}}

{{< faq "What size array maxes out this controller?" >}}
Apply the headroom rule: watts ÷ battery voltage × 1.25 ≤ 30 A. That is ~300W
comfortably and ~400W at the edge on a 12V bank; ~800W on 24V.
{{< /faq >}}

{{< faq-schema >}}

## Next logical reads

<a href="best-mppt-charge-controllers.html" class="text-link">Best MPPT charge controllers (2026 buyer guide)</a> <a href="mppt-vs-pwm.html" class="text-link">MPPT vs PWM</a> <a href="mppt-charge-controller-cost.html" class="text-link">MPPT controller cost guide</a> <a href="solar-fuse-and-breaker-sizing.html" class="text-link">Fuse and breaker sizing</a>

{{< product-box asin="B073ZJ3L13" name="Victron Energy SmartSolar MPPT 100V 30A 12/24V Solar Charge Controller with Bluetooth" label="The standard reference" description="The 100 V / 30 A model most small builds converge on (per manufacturer spec). Bluetooth monitoring, lithium charging profiles built in, and the Victron quality floor — where diminishing returns start to flatten. Not for: arrays above ~400 W on 12 V or ~800 W on 24 V, or 48 V banks — the 150 V line is the next step. The honest tradeoff: still capped at 100 V input." button="Check price on Amazon" >}}
```

---

## Pre-publish compliance checklist (individual review)

1. "What this review is (and isn't)" block present before any product claim; zero testing/ownership implications anywhere.
2. Every spec row carries a tier label + retrieval date; "Specs verified as of [date]" line present; no price, rating, availability, or urgency copy anywhere.
3. Who-for / Not-for / Alternatives all present with spec-based reasons; at least one named alternative.
4. Single product-box placed after spec table + worked math + who-for (≥60% into body); description contains "(per manufacturer spec)", "Not for:", and "The honest tradeoff:"; button text exactly "Check price on Amazon".
5. TOML front matter matches site conventions (title/slug/date/draft/description/image/author/related; `updated` only if genuinely revised); FAQ block + `{{< faq-schema >}}` present; all internal links end `.html`.
