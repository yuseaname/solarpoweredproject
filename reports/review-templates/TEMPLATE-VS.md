# TEMPLATE — Product-vs-Product / X-vs-Y Comparison Page

*Authored by the Boss 2026-09-05 from seat rt-vs's 8-page audit synthesis (run rt-vs, dsv4-wing-1). Benchmark: `content/pages/mppt-vs-pwm.md` (20/20). Each element below is proven by named live pages; the four pages currently failing it are listed under "Known debt".*

**Scope:** this template covers both product-vs-product (e.g., MPPT vs PWM controller classes) and concept-vs-concept (Li-ion vs lead-acid, 12V vs 24V vs 48V) pages. The reader arrives mid-decision; the page's job is to finish it, fairly, with arithmetic.

**Fairness rule (non-negotiable):** no overall winner is crowned. Both (or all) sides get a genuine "when this one wins" section. The honest caveats section must shrink the page's own headline claim before the reader reaches a box.

---

## Ordered sections

### 0. Affiliate disclosure — MANDATORY
`{{< affiliate-disclosure >}}` immediately after front matter.

### 1. Short answer = stated decision rule — MANDATORY, first body block
- A bolded "**Short answer:**" (or "## Quick answer") naming WHO should pick each side, by condition, before any physics or market content.
- Benchmark: "*pick MPPT when your panel voltage runs meaningfully above battery voltage, your array is bigger than about 200W, or your bank is 24V or 48V. Pick PWM when…* The arithmetic is below."
- Proven by: mppt-vs-pwm, pure-sine (decision checklist up top), 12v-vs-24v-vs-48v (quick-decision table). Anti-pattern: solar-battery-backup-vs-generator opens with three narrative paragraphs (scored 0 on above-the-fold).

### 2. Key takeaways — MANDATORY (3–6 bullets, caveat attached)
- Bullets, not a wall of text (li-ion's inline paragraph is the known miss). At least one bullet must carry the range/caveat that defuses the headline number ("real-world MPPT gain: near zero on a hot roof, 15–30% cold-clear").

### 3. Comparison table — MANDATORY, within the first ~25% of body
- Factor × option matrix; rows include at minimum: the decisive spec, typical cost band (T4, labeled), voltage/sizing compatibility, best fit, main sizing risk.
- Proven by: mppt-vs-pwm, micro-vs-string ("Side-by-side"), li-ion, 12/24/48. The two table-less pages (series-vs-parallel, fuses-vs-breakers) read thin — the table is the fix.

### 4. Worked arithmetic, both directions — MANDATORY
- Show the chain, both sides: mppt-vs-pwm's "12.8V × 5.56A ≈ 71W" vs "100W ÷ 12.8V ≈ 7.8A before losses"; li-ion's 600Wh vs 960Wh → lifetime $/kWh. All inputs stated so the reader can re-run with their numbers.
- Numbers asserted without work or source are failure mode #1 on this site (found on 5 of 8 pages).

### 5. "The honest caveats" — MANDATORY
- The section that shrinks the headline claim ("That 35% is a best-case snapshot, not an everyday average. Three things shrink it: …"). If the page has no headline claim to shrink, it has no argument — write one.

### 6. "When [the underdog] wins" — MANDATORY, named section
- "When PWM actually wins", "When lead-acid still wins", "When a string inverter wins". Conditions, not concessions: real dollar or sizing reasons the weaker-on-paper option is the right buy.

### 7. Scenario table with ranges — RECOMMENDED
- Rows = conditions, cells = ranges not point truths (benchmark's harvest-gain table: hot 0–10%, mild 10–20%, cold 15–30%, deep-discharge 30–40%, 24V/48V "not viable"). Note in prose why the extreme rows exist.

### 8. Decision restated as a checklist / threshold rule — MANDATORY near end
- "Modified sine is acceptable if ALL of these are true…", "upgrade triggers", "Decide with a shade assessment first." The reader should be able to act without re-reading.

### 9. Product box — OPTIONAL, only after the decision logic is complete
- Place after the checklist (benchmark: 95%; 12/24/48: ~90%; pure-sine: 96%). House anatomy required ("per manufacturer spec" / "Not for:" / "The honest tradeoff:"). The box should DEFER to the page's checks ("the sizing checks in this guide decide that, not the label").
- A vs page with no purchasable answer (li-ion vs lead-acid chemistry, 12/24/48) may omit the box — but if purchase intent is real (li-ion's drop-in LiFePO4 path), one late box is the monetization the audit found missing on 4 of 8 pages.

### 10. FAQ + schema — MANDATORY
- 4–6 `{{< faq >}}` items answering the query's natural follow-ups, incl. the threshold question ("When is X good enough?"). Then `{{< faq-schema >}}`.

### 11. Next logical reads — house convention
- Link the roundup (the "which model" next step), the cost guide, and the sizing/checklist pages. `.html` URLs.

---

## Sourcing rules specific to vs pages

- Every number is either: worked on-page from stated inputs (label the formula), manufacturer-stated (T2, mark it), or third-party-cited (T3, URL + date). Editorial bands (T4) must say "band"/"typically".
- Cost bands need a date or a link to the dated cost guide ("~$25 for a basic 10A unit — see our cost guide" beats a bare "~$25").
- Incentive/time-fragile facts carry dates (ITC expired 2025-12-31, P.L. 119-21). No "pays for itself" ROI claims — payback math belongs to the cost guides, stated as bands.

## Known debt (as of 2026-09-05 — feed the rewrite queue)

1. `solar-battery-backup-vs-generator.md` — 8/20; needs full template rewrite (compliance patches already applied 2026-09-05: ROI claim, superlative, lead-gen closer).
2. `solar-panels-series-vs-parallel.md`, `solar-fuses-vs-breakers.md` — no comparison table; decisive numbers asserted.
3. `pure-sine-vs-modified-sine-inverter.md` — device-compatibility and temperature figures unsourced ("~60–70% of devices", "15–25°F hotter").
4. `li-ion-vs-lead-acid.md`, `micro-vs-string-inverters.md` — strong pages missing only a late box (monetization gap, not a trust gap).

## Pre-publish compliance checklist (vs page)

1. Short answer first body block; decision rule stated by condition; no overall winner.
2. Comparison table in first 25%; worked arithmetic both directions with stated inputs; honest-caveats section present.
3. Named "when the underdog wins" section; scenario ranges not point truths.
4. Every figure worked, T2-marked, T3-cited, or labeled editorial band; money facts dated.
5. Box (if any) after the decision checklist with full house anatomy; uniform button text.
6. FAQ + `{{< faq-schema >}}`; internal links `.html`; no existing URL changed.
