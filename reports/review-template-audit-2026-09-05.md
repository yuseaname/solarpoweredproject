# Product-Review & Comparison-Page Template Audit — solarpoweredproject.com

**Date:** 2026-09-05 · **Method:** agency multi-seat audit (Boss + 5 seats) · **Repo state at start:** `1c86404`
**Companion files (this directory):** `TEMPLATE-INDIVIDUAL-REVIEW.md` · `TEMPLATE-ROUNDUP.md` · `TEMPLATE-VS.md` · `TABLE-FIELDS.md` · `CTA-COPY-LIBRARY.md`

**The site's review surface, inventoried:** 3 live roundups ("best X"), 14 "vs" comparison pages, ~16 buyer guides with embedded product boxes (33 pages carry 48 boxes total), and **zero standalone individual-review pages** — the individual-review template below defines a new page type. Two canonicalized stubs (best-solar-panels-for-home-2026, -for-small-homes) were excluded; URLs are frozen per standing constraint.

**Attribution & honesty:** vs-page audits (8 pages) by seat dsv4-wing-1 and box-integration audits (10 pages) by seat dsv4-wing-2 delivered complete and were Boss-verified against the files. The roundup/choose-guide audits (6 pages) are **Boss-authored** after four provider-failure dispatches (2× glm-xo-1, 2× dsv4-wing-3, all "empty replies"); every load-bearing quote below was read in the source file by the Boss. The UX seat (glm-xo-2) completed a live above-the-fold check of 6 pages before its own truncation; its Parts B–D are Boss-rebuilt from its evidence plus the structural scan. The template seat (glm-xo-3) delivered the individual-review template in full (extracted verbatim); the other three template files are Boss-authored from the seat syntheses.

---

## 1 · Per-page audit

### 1.1 Roundups & choose-guides (Boss-audited, 10 criteria × 0–2)

| Page | /20 | Above-the-fold | Methodology | Tables/boxes | Weakest sections (evidence) |
|---|---|---|---|---|---|
| `best-solar-batteries-2026` | **19** | "Quick answer… there are best *matches*" — exemplary | **The site's gold standard** ("we have not lab-tested these… every pick is a 'best for' scenario match") | Spec table + source notes + retrieval dates; single late box (79%) | Residual: no inline jump links (TOC rail only); Powerwall chemistry row necessarily hedged |
| `solar-generator` | **18** | "Quick answer" defines the product, kills the big myth ("finite energy store, not a fuel machine"), routes whole-home buyers away | Implicit, not stated (no "how to read this page") | Honest capacity-tier table w/ runtimes; "Who should NOT buy" section; 2 contextualized boxes (26%/43%) | Cost claims ("3,000–6,000 cycles") undated; no jump links |
| `best-mppt-charge-controllers` | **17** | Jump-link row + Key takeaways; dek sells the decision flow | **Absent** — the gap vs the batteries benchmark | Head-to-head table lacks warranty row; "Typical price class" vague; 4 boxes each with wins/stings | No methodology/as-of line; table thin ("Remote temp input: Yes/No/Yes" with no why-it-matters) |
| `best-solar-panels-small-roof` (2026-09-05 rebuild) | **17** | "How to read this page" methodology block present | Present, mirrors benchmark | 4-row comparison table w/ per-manufacturer footnotes; W/ft² worked math | Final Renogy 100W 12V box is a *shed-class* product on a roof-install page — label "Small-roof friendly footprint" overstates the fit; dead-brand FAQ good |
| `portable-solar-panels` | **15** | Dek was essay-style & truncated (now fixed); Key takeaways but no quick-answer block | Absent | Sizing formula + worked 575Wh→192W example is excellent; box honest ("a single 100W panel underperforms… you'd want two") | No jump links; cost tiers ("$3–$5/W… $12+/W") undated; intro "In an era of…" throat-clearing |
| `how-to-choose-solar-inverter` | **13** | Jump links + type table (Type/Best-for/Cost) up front — good; but no quick-answer block | Absent | Tables good; single box late (77%) | "Top brands: **Victron Energy (highest quality)**" — unsupported superlative; "Top brands: SolarEdge, SMA, Fronius…" lists without scenario-matching; named models (FXR3048A, MultiPlus-II 48/3000) asserted without sourcing |

### 1.2 "Vs" comparison pages (seat rt-vs, dsv4-wing-1 — Boss-verified)

| Page | /20 | Verdict |
|---|---|---|
| `mppt-vs-pwm` | **20/20** | The benchmark: short-answer decision rule, worked arithmetic both ways (71W vs 96W), caveats that shrink the headline 35%, "When PWM actually wins", box at 95% deferring to the page's own checks. Only gap: undated price bands. |
| `micro-vs-string-inverters` | **20** | Equally strong ("Two honest caveats cut both ways"); **no box — monetization gap, not a trust gap** |
| `12v-vs-24v-vs-48v-solar` | **19** | Quick-decision table + wire-economics chains; boxes at ~90% citing "this page's wire math" |
| `li-ion-vs-lead-acid` | **18** | Quick answer + lifetime $/kWh math + "When lead-acid still wins"; takeaways are a wall of text, not bullets; **no box** |
| `pure-sine-vs-modified-sine` | **18** | Decision checklist up front; but "~60–70% of devices work" and "15–25°F hotter" asserted, unsourced |
| `solar-panels-series-vs-parallel` | **18** | Sound electrical content; **no comparison table**, decisive numbers asserted |
| `solar-fuses-vs-breakers` | **18** | Good NEC-adjacent guidance; no table, no worked ratting examples |
| `solar-battery-backup-vs-generator` | **8/20 — the outlier** | Three narrative paragraphs before any decision; zero arithmetic anywhere; unsupported "the battery pays for itself through monthly savings"; "highest level of-energy security possible" (superlative + typo); savings-tease lead-gen closer. **Compliance patches applied 2026-09-05 (see §7); full rewrite remains the top implementation item.** |

### 1.3 Box-embedding buyer pages (seat rt-buyer, dsv4-wing-2 — Boss-verified; scores on criteria 4/7/9/10, /8)

| Page | /8 pre-fix | Box verdict | Status after same-day fixes |
|---|---|---|---|
| `solar-phone-charger` | 8 | Full anatomy; hybrid-strategy fit; **fixed:** wall-charger-speed claim now hedged as editorial estimate | ✅ fixed |
| `solar-lights-for-yard` | 8 | Class-archetype box, "Not for" names the security tier | clean |
| `what-size-solar-generator-run-refrigerator` | 8 | Checklist→box handoff; "Not for" quotes the page's own table row | clean |
| `battery-capacity` | 7 | Formula→box ("1.28 kWh, exactly"); alternatives only implied | clean |
| `solar-panel-output` | 7 | Diagnostic multimeter box with a *safety* not-for + "you may not need this" honesty | clean |
| `rv-solar-sizing` | 7 | "a **proven** single-kit solution" — unsupported; appendix placement | P4 item |
| `cpap-battery-backup-guide` | 6→8 | Box claimed "over a week of runtime… at 40-60Wh per CPAP night" vs the page's own table (360Wh/night → 2.7 nights) — order-of-magnitude contradiction; "80-100% DoD" garbled | ✅ fixed — box now quotes the table's 2.7/1.3 nights |
| `solar-inverter-sizing` | 5→7 | Box sat **before** the worked example it cited ("the worked example below"), contradicting the calculator's default output | ✅ fixed — moved after the example, "above" |
| `solar-panels-for-sheds` | 4→7 | Manual price ("~$150 per kit") + box after forked link blocks + tradeoff duplicating the Not-for | ✅ fixed — price removed, box moved with handoff lead-in, tradeoff rewritten |
| `how-much-do-solar-panels-cost` | 2→n/a | Category mismatch: DIY panel CTA inside an installed-financing decision; zero box anatomy | ✅ fixed — box removed (page's decision has no box-sized answer) |

### 1.4 UX layer (seat rt-ux live checks, 6 pages, + Boss structural scan)

- **Template render order confirmed live:** kicker → H1 → dek → byline/dates → "System brief" → TOC rail → "In brief" (dek) → disclosure banner → first body block. **No CTA above the fold on any checked page; disclosure always precedes the first box.** CTA-after-value holds sitewide.
- **Decision-block coverage:** 24/33 box pages open with Quick-answer/Short-answer/Key-takeaways; **9/33 have inline jump links** (the best pages do: mppt-controllers, inverter-chooser, fuse-sizing, cable-sizing…). mppt-vs-pwm and how-to-choose pass the "decide without scrolling" test; **portable-solar-panels and solar-phone-charger fail it** (spec takeaways but no pick/verdict until ~90%).
- **New defect found & fixed during audit:** 10 pages shipped **machine-truncated meta descriptions** (cut at exactly 158 chars: "…provides a …", "…from nic…") rendering as the on-page "In brief" dek and SERP snippet. All 10 rewritten (see §7).

### 1.5 Compliance sweep (Boss, then seat-verified — cleaned same day)

Zero star ratings, zero review text, zero scarcity copy, zero deceptive winner labels sitewide. CTA text uniform. **Five boxes pinned product prices** ("~$150 per kit", "the $200 that saves…", three "$1/Watt panel like this" class-pins) — all removed/reframed 2026-09-05 (commit `ca10afb`). Editorial cost *bands* (labeled) remain allowed and are unchanged.

---

## 2 · Reusable individual product-review outline → `TEMPLATE-INDIVIDUAL-REVIEW.md`

Seat-authored (glm-xo-3), Boss-extracted verbatim. Defines the new page type: Quick verdict → **"What this review is (and isn't)"** honesty block (mandatory, before any claim) → sourced spec table ("per manufacturer spec, retrieved [date]") → worked build math → Who-for/Not-for/**Alternatives** → warranty (T2 + verify note) → one box after value → FAQ incl. "Did you test this?" → schema. Includes a filled Victron SmartSolar 100/30 micro-example (warranty figure flagged illustrative — re-verify before real use).

## 3 · Roundup template → `TEMPLATE-ROUNDUP.md`

Generalizes the gold standard: Quick answer (no single best) → "How to read this page" methodology → dated money-fact callout → takeaways → sourced comparison table + as-of line → "Best for: N scenarios, not one winner" (each with a stated catch) → worked $ math → installer questions → "not Amazon items" block (type A) → boxes late → FAQ+schema. Type A/B/C (installed / Amazon-buyable / mixed) flags included.

## 4 · Vs-comparison template → `TEMPLATE-VS.md`

From the 8-page synthesis: **short-answer decision rule first** → bulleted takeaways with caveats → table in first 25% → worked arithmetic both directions → "honest caveats" that shrink the headline claim → named "when the underdog wins" → scenario ranges → decision checklist → box only after the logic (90%+) → FAQ+schema. Includes the fairness rules, sourcing rules, and the known-debt queue.

## 5 · Table fields → `TABLE-FIELDS.md`

Per-niche column specs (panels, controllers, installed batteries, DIY batteries, inverters, power stations, wiring/fusing, consumer small-solar) with source tiers (T2/T3/DERIVED/T4), verification notes, and the **never-display list** (price, availability, ratings, review counts, badges, savings claims). Code fields (NEC 310.16/690.8/690.9, ABYC E-11) are T3-cited.

## 6 · CTA copy → `CTA-COPY-LIBRARY.md`

Keep the uniform "Check price on Amazon" (consistency = trust; never goes stale); variation lives in the handoff sentence. Approved alternates ("See specs on Amazon" for diagnostic boxes), handoff patterns per context, non-examples with reasons, and placement rules (never before the decision logic; never after forked links; never referencing unreached content).

---

## 7 · Before/after rewrites (all applied and committed 2026-09-05, commit `ca10afb` + this session)

1. **Manual price (sheds):** "The honest tradeoff: **at ~$150 per kit the price is low**, but…" → "The honest tradeoff: the kit's 30A PWM controller and single-kit wiring are a closed loop — once your loads grow past lights and tool charging, the controller is the first part you'll replace." *(price removed; tradeoff de-duplicated from the Not-for)*
2. **Runtime contradiction (CPAP):** "1,280Wh of usable-capacity chemistry (…80-100% DoD…) — **at 40-60Wh per CPAP night that is over a week of runtime**" → "100Ah at 12.8V — 1,280Wh nameplate (per manufacturer spec), the 100Ah-lithium class **the runtime table above sizes at about 2.7 nights without the humidifier and 1.3 with it**." *(box now agrees with the page's own math)*
3. **Price pin (BMS page):** "this is **the $200** that saves a $1,000 bank" → "this is the monitor that saves a $1,000 bank."
4. **Class-price pin:** "a $1/Watt panel like this" → "a panel in the ~$1/Watt DIY hardware class"; label "The $1/Watt reality check" → "The commodity-hardware reality check"; "the $1/Watt benchmark" → "the $1/Watt-class benchmark."
5. **Unsupported claim (battery-vs-generator):** "the battery **pays for itself** through monthly savings" → time-of-use framing + "on backup duty alone, a battery is a resiliency purchase, not a payback play"; "highest level of-energy security possible" → "the strongest of the three options for riding out long outages without giving up daily battery benefits"; lead-gen savings tease → "get quotes from two or three local installers and ask each for a written load analysis and a line-item quote."
6. **Unattributed estimate (phone-charger):** "charges a phone in roughly the same time as a wall charger" → "should land in everyday wall-charger territory — our estimate from the rated output (makers don't publish charge times)."
7. **Truncated deks (10 pages):** e.g. "…a solar phone charger provides a …" → "How to pick a solar phone charger: integrated power banks vs foldable panels, the wattage and port specs that matter, and durability ratings."
8. **Mismatched box (panels-cost):** removed entirely — the financing decision had no box-sized answer.

## 8 · Prioritized implementation list

| # | Item | Urgency | Impact | Effort |
|---|---|---|---|---|
| 1 | Rewrite `solar-battery-backup-vs-generator.md` to TEMPLATE-VS (8/20; patches already in) | **High** | High | Medium |
| 2 | Add "how to read this page" methodology blocks + source-tier the asserted figures on pure-sine, series-parallel, fuses-vs-breakers | **High** | High | Low-Med |
| 3 | Add late product boxes to li-ion-vs-lead-acid + micro-vs-string (proven pages, zero monetization) | Med | Med (revenue) | Low |
| 4 | Jump-link nav rows on box pages lacking them (24 of 33); standard: ≥1,500 words or ≥5 H2s | Med | Med-High | Low |
| 5 | Comparison tables + worked numbers for series-parallel and fuses-vs-breakers | Med | Med | Medium |
| 6 | best-mppt-charge-controllers: methodology block; add warranty row + as-of line to head-to-head table | Med | Med | Low |
| 7 | Small-roof: reframe or remove the Renogy 100W box (shed-class product on a roof-install page) | Med | Med | Low |
| 8 | how-to-choose-solar-inverter: replace "Top brands" lists (incl. "Victron (highest quality)") with scenario-matched, sourced picks | Med | Med | Medium |
| 9 | portable-solar-panels + solar-phone-charger: add quick-answer/pick blocks (currently fail the decide-without-scrolling test); date the cost tiers | Med | Med | Low |
| 10 | rv-solar-sizing: drop "proven" from the kit lead-in; move box before FAQ | Low | Low | Trivial |
| 11 | Stamp bare cost figures sitewide with dates or cost-guide links ("~$25 PWM unit") | Low | Low-Med | Low |
| 12 | Pilot ONE individual-review page (Victron 100/30) from TEMPLATE-INDIVIDUAL-REVIEW to validate the new page type | Low | Potentially high | Medium |
| 13 | Optional CTA variant "See specs on Amazon" for diagnostic boxes only | Low | Low | Trivial |

**Standing ops gate (user-owned, unchanged):** the Hostinger firewall returning 403 to Googlebot remains the #1 blocker to Google-side gains; none of the above moves search traffic until it is fixed (`curl -s -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://solarpoweredproject.com/`).

---

## Audit limitations

- Roundup/choose-guide audits (§1.1) are Boss-authored without independent second-seat challenge (four consecutive provider failures); quotes were verified in-source, but no independent reviewer re-scored them.
- rt-ux's Parts B–D were reconstructed by the Boss from the seat's Part A evidence and the structural scan; the CTA library is Boss editorial judgment, not seat-validated copy testing.
- The template files are documents, not yet exercised on a live page; item #12 (pilot) is the validation step.
- Traffic/Rybbit data was not re-pulled; page-value judgments use the 2026-09-05 snapshot in the prior audit's TSV.
