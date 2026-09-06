# Editorial Audit — Buyer-Intent Core (seat glm-xo-1, ca-buyer-core)

Auditor: editorial-auditor seat glm-xo-1 · Session 20260905T235849Z-ca-buyer-core-291ddd
Scope: buyer-intent pages with product boxes, per assignment. Fact pack read first (Boss ground truth 2026-09-05). Claim tiers use fact-pack taxonomy: T1 firsthand-tested · T2 manufacturer-stated · T3 reputable third-party · T4 editorial judgment · T5 unknown/unverified.

**COUNT DISCREPANCY (flagged up front):** the assignment says "13 highest-stakes buyer-intent pages" but lists **12 filenames**. All 12 named files are audited below. To reconcile the count, I additionally audited `what-size-solar-generator-run-refrigerator.md` (box present, high attribution density, natural member of this cluster) as the 13th — clearly labeled as auditor's addition. If the Boss intended a different 13th page, the per-page method below transfers directly.

Scoring: 1–5 per dimension (a) intent satisfaction, (b) per-product guidance (count of 5 elements: who-for / who-NOT-for / tradeoffs / specs+compat / alternative-if-no-fit), (c) methodology visibility, (d) claim tiers, (e) Amazon compliance, (f) honesty, (g) structure, (h) AI/templated passages, (i) staleness risk.

---

## 1. best-mppt-charge-controllers.md — "Best MPPT Charge Controllers for Solar (2026 Buyer Guide)" (1,487 w, 4 boxes, FAQ, 1 table, date 2026-08-18)

**(a) Intent satisfaction: 4/5.** Answer-first works: dek promises "picked by voltage class and budget. Includes the decision flow so you can size one yourself instead of picking a brand first," and "Key takeaways" opens with the actual decision rule: "Size the controller from your **array voltage** and **battery charging current** first; brand comes second." Worked math present ("`Panel watts ÷ Battery voltage × 1.25`"). Depth gap: **no 48 V pick at all** — all four boxes are 12/24 V / 100 V-input class, yet "Common buying mistakes" itself warns "a 4 kW array at 48 V draws very different current from a 4 kW array at 12 V." A careful 48 V buyer gets methodology but no product answer.

**(b) Per-product guidance (avg 4.25/5):**
- EPEver Tracer 4210AN — who-for ✔ ("covers most small-to-mid builds on 12/24 V"), NOT-for ✘ (only implied), tradeoffs ✔ ("**Where it stings:** firmware quirks…wireless monitoring costs extra"), specs/compat ✔ (40 A, 100 V, BT-1, temp input), alternative ✘. **4/5**
- Renogy Rover 40 A — who-for ✔ ("If your array runs at higher voltage than battery…this is the natural budget pick"), NOT-for ✔ (implied by "you will run out of headroom faster than with a 150 V controller as arrays grow"), tradeoffs ✔, specs ✔, alternative ✔ (150 V class named). **5/5**
- Victron 100/20 — who-for ✔ ("For one or two panels and a 100Ah bank"), NOT-for ✔ ("without paying for headroom you will not use"), tradeoffs ✔, specs ✔, alternative ✘. **4/5**
- Victron 100/30 — who-for ✔ ("If your sizing math landed at 20–30 A on a 100 V rail"), NOT-for ✔ ("once you need higher array voltage, you move to the Victron 150 V line or a different brand entirely"), tradeoffs ✔, specs ✔, alternative ✔. **5/5**

**(c) Methodology: 5/5, scenario-match, visible and fair.** Quoted: "Size the controller from your **array voltage** and **battery charging current** first; brand comes second." Selection is by sizing math → class → budget tier, not a ranked top-10. The head-to-head table compares on specs, and the prose explicitly de-ranks spec-sheet thinking: "The Victron's advantage is not in spec sheets — it shows up in firmware maturity and ecosystem depth."

**(d) Claim tiers:**
- Specs (40 A/100 V, 520 W@12 V/1040 W@24 V, "lithium presets, remote battery temperature input") — **T2 presented as bare fact, no attribution language** ("per manufacturer spec" absent). Confirms Boss finding #2 for this page.
- "Panels gain ~0.3% V<sub>oc</sub> per °C below 25°C" — **T2/T3 stated as universal fact without source**; real coefficients span roughly −0.25 to −0.5 %/°C by cell tech. Should be "typically ~0.3%/°C; check the datasheet."
- "The Tracer line has been the budget reference for years" — T4, fine as judgment.
- "The most copied controller family in the DIY community" — **T5 as written** (no source for "most copied"); soften to T4 ("widely used in the DIY community") or cite.
- "documented limits you can trust" (Victron) — T4, acceptable.
- No T1 claims on page; none implied. Good.

**(e) Amazon compliance: PASS.** No prices (table uses "Typical price class: Budget/Mid-range" — compliant), no star ratings, no review quotes. Boxes carry shortcode disclosure + rel=sponsored (verified rendering per fact pack). Button text "Check price on Amazon" — compliant.

**(f) Honesty: 4/5.** Real limitations named per pick (headroom caps, firmware quirks, price-per-amp). Gaps: (1) "known-quantity device that will not lie to you about its limits" (EPEver intro) is an overstated T4 — budget units' measured behavior varies; (2) **no counterfeit warning** — Victron is the most-counterfeited controller brand on Amazon marketplaces; a buyer page sending people to Amazon for Victron should say "buy from the official Victron store or verify seller"; (3) no low-temperature lithium charging caveat (charging LiFePO4 below 0 °C damages cells; several of these controllers' lithium profiles handle it, but the page never raises it — safety-relevant omission).

**(g) Structure: 4/5.** Dek + key takeaways + manual anchor-link nav line + worked sizing math + comparison table + FAQ. Scannable and honest depth for the class covered; thin only for 48 V.

**(h) AI/templated: low.** "Where it wins / Where it stings" is a consistent but purposeful format, not filler. One repetition: "genuinely useful" appears twice ("its monitoring stack (VictronConnect) is genuinely useful" and FAQ "it is genuinely useful for verifying"). No AI-tell passages found.

**(i) Staleness: LOW.** Picks (Tracer 4210AN, Rover 40, SmartSolar 100/20 & 100/30) are long-lived models; "2026" only in title. Note: zero `updated` front matter site-wide (Boss finding #3) means the "2026 Buyer Guide" title carries the freshness signal alone.

**ACTION: update · PRIORITY: P3 · Highest-impact fix:** add one 150 V-class / 48 V-capable pick (or an explicit "beyond 100 V" pointer with a named model) so the page's own 48 V warning has an answer, and add "per manufacturer spec" attribution to the spec lines.

---

## 2. best-solar-batteries-2026.md — "Best Solar Batteries for Home 2026: Brand Comparison Guide" (2,427 w, 1 box, FAQ, 2 tables, date 2026-08-09)

**(a) Intent satisfaction: 5/5.** Answer-first, literally: "There is no single 'best' home battery in 2026 — there are best *matches*." Then a "How to read this page" methodology block, the dated ITC fact ("the 30% federal ITC expired December 31, 2025 — a battery installed in 2026 gets **$0 federal credit**"), a spec table, four scenario picks, worked $/kWh math, installer questions, and FAQ. This is the depth a careful buyer needs; nothing important is buried.

**(b) Per-product guidance (avg 4.5/5):**
- Tesla Powerwall 3 — who-for ✔ ("homeowners going Tesla end-to-end"), NOT-for ◑ (only via tradeoff: "you're buying Tesla's software, gateway, and service path, and 10 years is a shorter warranty"), tradeoffs ✔, specs ✔, alternative ✔ (LFP competitors named). **4.5/5**
- Enphase IQ Battery 5P — who-for ✔ ("retrofits — you already have solar"), NOT-for ✔ ("you'll stack several modules to run big motor loads"), tradeoffs ✔ ("The catch is cost per kWh and power per module"), specs ✔, alternative ✔. **5/5**
- FranklinWH aPower 2 — who-for ✔, NOT-for ✔ ("it wants FranklinWH's aGate controller, so it's its own ecosystem — confirm your installer carries it"), tradeoffs ✔, specs ✔, alternative ✔. **5/5**
- EG4 48V rack class — who-for ✔, NOT-for ✔✔ (strongest on page: "If that's not you, stop reading here and stay in the installed rows"), tradeoffs ✔ ("*you* are now the installer and the warranty is pack-level"), specs ✔, alternative ✔ (diy-vs-installer link). **5/5**
- LiTime 12V 100Ah (box) — who-for ✔ ("DIY bank building block"), NOT-for ✔ ("Not a substitute for an installed whole-home system"), tradeoffs ✘ (no con named for the product itself), specs ✔ (1.28 kWh, 100A BMS, low-temp protection), alternative ✘. **3/5** — and a coherence gap: the DIY section is about **48 V** EG4 modules, but the box is a **12 V** LiTime block; a buyer following the section's math lands on a different voltage class than the section teaches.

**(c) Methodology: 5/5, scenario-match, the cluster's gold standard.** Quoted: "every pick is a 'best for' scenario match, not a ranking. The full criteria behind how products earn a mention on this site are on our how we recommend page." Plus "this is a spec-based comparison — we have not lab-tested these."

**(d) Claim tiers: exemplary — this is one of the 3 pages Boss flagged as having attribution language, and it uses it well.**
- "per manufacturer spec" ×10; retrieval dates ("franklinwh.com product page (retrieved 2026-09-05)"); derived figures flagged as derived ("100 A × 51.2 V — derived from the 100 A continuous BMS rating"); "manufacturer-listed" for FranklinWH 15 kWh. T2 properly labeled throughout.
- Cost bands ($1,000–$1,400/kWh installed; $150–$300/kWh DIY) — T3/T4 hybrid, correctly framed: "Those are planning bands, not quotes."
- ITC expiry — T3, matches Boss-verified sitewide purge.
- Weak point: Powerwall chemistry sourced to "spec roundups (tesla.com; thegreenwatt.com, retrieved 2026-09-05)" — thegreenwatt.com is a low-authority aggregator; the table itself hedges ("chemistry not broken out on Tesla's public spec sheet"). Acceptable but the weakest citation on the page; source-rot risk if the aggregator dies.
- "LFP packs commonly spec 6,000+ cycles at 80% depth of discharge" — T2-generic with "commonly spec" hedge. Fine.

**(e) Amazon compliance: PASS — and the best compliance posture in the cluster.** No prices, no ratings, no review quotes; box discloses via shortcode. Page goes further and manages expectations explicitly: "you cannot order a Powerwall 3, an IQ Battery 5P, or an aPower 2 off Amazon… What *is* orderable online is the DIY path."

**(f) Honesty: 5/5.** "we have not lab-tested these," "specs drift," "Verify every number against the current datasheet," DIY risks named, ITC loss stated plainly, "Get three installed quotes *and* run the DIY math." Minor: the LiTime box description sells ("beat lead-acid ~7×") harder than the body's careful tone — T4 math reference, acceptable but tonally off.

**(g) Structure: 5/5.** Two tables, two worked cost examples, comparison table with "What's missing" column (rare honesty device), installer-question list, FAQ + faq-schema shortcode.

**(h) AI/templated: none found.** Prose is specific and hedged where hedging is due.

**(i) Staleness: MEDIUM-HIGH, but self-managed.** Model names (Powerwall 3, IQ 5P, aPower 2, EG4 SKUs), warranty terms, price bands, ITC dates are all time-sensitive; the page itself says "treat the table as a point-in-time snapshot." Zero `updated` front matter (Boss finding #3) means none of this maintenance is visible.

**ACTION: keep · PRIORITY: P4 · Highest-impact fix:** add `updated` front matter (site-wide template fix) and put a recurring annual task on the calendar to re-verify EG4 SKU names/warranties — SKU churn is this page's main rot vector; also reconcile the 12 V LiTime box with the 48 V DIY section (either swap to a 48 V module box or add one sentence bridging the voltage classes).

---

## 3. best-solar-panels-for-home-2026.md — "Best Solar Panels for Home in 2026: Future-Proofing Your Solar Investment" (1,106 w, 1 box, no tables, no FAQ schema, date 2026-05-31, **canonical → best-solar-panels-small-roof.html**)

**Status note: this is one of the site's 5 canonicalized duplicates** (front matter: `canonical = "https://solarpoweredproject.com/pages/best-solar-panels-small-roof.html"`). Audited as it stands because it still renders, still carries a product box, and still receives internal links.

**(a) Intent satisfaction: 1/5.** The dek/answer box is "Discover the top-rated home solar panels of 2026…" — a non-answer. The body never names a current buyable residential model with specs; the "Leading Solar Panel Models to Watch in 2026" list is three vague blurbs with zero wattages, efficiencies, or prices. A buyer searching "best solar panels for home" gets technology forecasting, not a decision aid.

**(b) Per-product guidance (avg 0.6/5):** The three "models to watch" get one sentence each — no who-for, no NOT-for, no tradeoffs, no specs, no alternatives. The single product box (Renogy 100W 12V Monocrystalline) gets a description that is close to incoherent: "Not a roof replacement — the panel future-proofers start with. Add-by-add scaling without a re-roof contract, and the efficiency tier that makes 2026 shortlists." "The efficiency tier that makes 2026 shortlists" is not a sentence a human editor signs off on, and a 100 W 12 V RV-style panel is an intent mismatch on a page nominally about whole-home rooftop solar. **0–1/5 across the board.**

**(c) Methodology: 1/5 — none visible.** No selection basis, no criteria, no scenario matching. The word "best" in the H1 is unsupported by any stated basis.

**(d) Claim tiers — the worst tier hygiene in the cluster:**
- "Some manufacturers estimate performance improvements of up to 15% compared to current market models" — **T5 as written** (no manufacturer named, no source).
- "degradation rates…are expected to drop significantly" — T5 (unquantified, unsourced).
- "the cost floor may reach between $1.00 and $1.50 per watt by 2026" — **T5 projection presented as trend fact**; also dubious: $1.00–1.50/W is not a residential installed-cost figure (residential installed runs several times that; the figure resembles module-level or utility-scale economics). No source, no distinction between module cost and installed cost.
- "SunPower Maxeon LX" — **T5/unverified model name**; I cannot confirm a "Maxeon LX" residential model exists (flag for Boss verification).
- "LG NeON R: This panel integrates heterojunction cell architecture…" — **stale/likely wrong**: LG publicly exited the solar module business in 2022 (T3, widely reported at the time; Boss should re-verify). Presenting an LG panel as a 2026 model "to watch" is the kind of error that destroys buyer trust.
- "REC Alpha Pure Series" — real product line (T2), but described with marketing adjectives ("excellent performance in low-light environments") and no specs.
- "High-voltage off-grid panels are the premier choice for remote locations" — T4, and "high-voltage off-grid panels" is not a meaningful category phrase.
- Typo evidence of unedited generation: "**heterojostunction**" (for heterojunction), in "the transition to Tunnel Oxide Passivated Contact (TOPCon) and heterojostunction cell architectures."

**(e) Amazon compliance: mechanically PASS** (no prices, no ratings, no review text; box shortcode carries disclosure + sponsored rel) — **but substantively poor**: the box's product class (100 W 12 V off-grid panel) does not match the page's stated topic (whole-home 2026 rooftop panels), which is a mismatched-recommendation risk even if disclosure is technically present.

**(f) Honesty: 1/5.** No limitations anywhere (caveat-word count: 0 per quality-signals scan). "there has never been a better time to plan your solar future" is promotional boilerplate; the FAQ answer "it is highly recommended" (battery) is unqualified advice-without-context. No mention that the page duplicates the small-roof guide.

**(g) Structure: 2/5.** No tables, no worked math, no TOC anchors, broken FAQ formatting (first two Qs use `**Q:**`, the third drops it: "What is the main benefit of a battery for solar?" — inconsistent), and the H1 line is escaped (`\# Best Solar Panels…`), part of a **10-page repo-wide `\#` escaping bug** I found (also hits install-solar-panels-yourself, ground-mount-vs-roof-mount, how-many-solar-panels, solar-lease-vs-buy-2026, solar-battery-backup-vs-generator, solar-net-metering-explained, how-much-do-solar-batteries-cost, solar-panel-degradation-rate, best-solar-panels-for-small-homes) — the H1 renders as literal text, not a heading.

**(h) AI/templated: YES — the clearest AI-flavored page in the cluster.** Quoted tells: "The era of energy independence is undergoing a massive transformation." / "As we approach 2026, the solar industry stands on the cusp of a technological revolution that promises to redefine residential energy systems." / "offering unprecedented efficiency" / "Discover the top-rated…" — plus future-tense forecasting ("By 2026, significant advancements will make home solar systems both more efficient and more affordable than ever before") that is now grammatically stale (it is 2026) and factually empty.

**(i) Staleness: CRITICAL.** The entire premise is forecasting 2026 from a pre-2026 vantage; "models to watch" include a brand that left the market; the "2026" cost projection is unsourced.

**ACTION: merge-canonical (already canonicalized — finish the job) · PRIORITY: P1 · Highest-impact fix:** reduce the live body to the site's stub pattern (short honest note: "this topic now lives in [best-solar-panels-small-roof]") and remove/relocate the mismatched Renogy box — a canonical tag does not fix what a human who lands here actually reads. (Site rule: no URL removals; canonical-only consolidation is the sanctioned mechanism and it is already half-done.)

---

## 4. best-solar-panels-for-small-homes.md — "Best Solar Panels for Small Homes: Maximizing Energy Density & Cost-Effectiveness" (1,052 w, 1 box, no tables, no FAQ schema, date 2026-05-31, **canonical → best-solar-panels-small-roof.html**)

Second canonicalized duplicate of the small-roof guide; same generation era as page 3.

**(a) Intent satisfaction: 2/5.** Better than page 3 (it has real sizing guidance) but still no answer-first dek ("Discover the best solar panels for small homes…" is a non-answer) and no named buyable product with specs until you hit brand-name blurbs.

**(b) Per-product guidance (avg 0.8/5):** Brand mentions are one-liners with no who-for/NOT-for/tradeoffs/specs/alternatives: "consider high-output monocrystalline panels such as the **SunPower Maxeon series** or the **LG NeON series**… the gold standard for small, space-constrained roofs" / "cost-effective options like **Canadian Solar HiKu** and **Jinko Tiger Pro**… efficiencies between 18% and 20%". The Renogy 100 W box gets a label and a one-line description only. **0–1/5 per product.**

**(c) Methodology: 1/5.** No selection basis stated. "Best" is unsupported; the only quasi-criterion is "prioritize panels with an efficiency rating of 21% or higher" (T4 threshold, unexplained origin).

**(d) Claim tiers — two P1-grade problems:**
- **"The Federal Investment Tax Credit (ITC) allows you to deduct 26% of your solar installation costs directly from your federal taxes" — STALE AND WRONG (P1).** Boss ground truth: the 30% ITC expired Dec 31, 2025; the sitewide ITC purge is done. This page still carries a pre-2022 rate (26%) and directly contradicts the site's own corrected pages (e.g., best-solar-batteries-2026: "a battery installed in 2026 gets $0 federal credit"). A buyer reading both pages gets opposite tax answers. T3 claim, badly outdated.
- **Worked math error (P1):** "if your daily energy consumption is 5 kWh and you use panels averaging 300 watts each, you would need approximately 17 panels (assuming 8 hours of peak sunlight per day)." By the page's own numbers: 300 W × 8 h = 2.4 kWh/panel/day → 5 kWh needs ~2–3 panels, not 17. The figure appears to be a misapplied "1 kW per daily-kWh" sizing rule; either way it is off by roughly 4–8× and would scare a small-home buyer off solar entirely.
- "$2.50 to $3.50" per watt, "payback period of 5 to 10 years" — T5, unsourced, undated.
- "LG NeON series" — stale brand (LG exited solar modules in 2022; see page 3 finding). "SunPower Maxeon series" — real line, but SunPower's residential business underwent major restructuring in 2024–25 (T5 here — Boss to verify current status before any re-publication).
- "efficiencies between 18% and 20%" for HiKu/Tiger Pro — T5 and dated; current HiKu/Tiger-class modules commonly spec ≥21%.
- Typo evidence: "a **sleunck**, black design" — garbled word, unedited generation.

**(e) Amazon compliance: mechanically PASS** (no prices/ratings/review text; shortcode disclosure) — **substantively poor:** the Renogy 100 W 12 V box again mismatches a page whose own cost section discusses 3 kW home systems and federal tax credits.

**(f) Honesty: 2/5.** No limitations section; "the financial landscape for small-scale systems is surprisingly favorable" is promotional; the ITC error is the honesty killer — it inflates the value case by a now-nonexistent credit.

**(g) Structure: 2/5.** No tables, no TOC anchors, no FAQ schema, escaped `\#` H1 (renders as literal text — repo-wide bug, 10 pages). One worked example — and it's wrong.

**(h) AI/templated: YES.** "In this comprehensive guide, we will explore…" / "transform your small home into a self-sustaining powerhouse." / "it is a necessity" framing without evidence. Same register as page 3.

**(i) Staleness: CRITICAL.** ITC rate two generations out of date; LG defunct in solar; efficiency bands dated; canonicalized yet still fully live.

**ACTION: merge-canonical (stub the body) · PRIORITY: P1 · Highest-impact fix:** stub to the small-roof canonical — but **first** fix or neutralize the 26% ITC sentence and the 17-panel math even in stub form, because both are live factual errors on a rendering page today.

---

## 5. best-solar-panels-small-roof.md — "Best Solar Panels for Small Roofs and Small Homes (2026)" (1,860 w, 1 box, no tables, no FAQ schema, date 2026-05-31 — **canonical target for pages 3 & 4**)

**(a) Intent satisfaction: 2/5.** The title promises a "best panels" comparison; the body names **zero panel models** and gives zero spec comparisons. What it delivers instead is solid generic guidance (power density, shading, microinverters, rough math, net metering) — useful, but it does not answer "which panels." The dek is honest about the pivot ("High-efficiency solar panels compared for small roofs… output per square foot, realistic costs, and how many panels actually fit") but "compared" overstates: nothing is compared.

**(b) Per-product guidance (avg 0.5/5):** No products except the Renogy 100 W box (label + one-line description; no who-for/NOT-for/tradeoffs/alternative). Technology categories (solar shingles, thin-film, microinverters) get pros/cons lists — the strongest guidance on the page, but category-level, not product-level.

**(c) Methodology: 1/5.** No selection basis for "best." The closest is "you should almost exclusively look at **monocrystalline solar panels**" (T4, reasonable but asserted, not derived).

**(d) Claim tiers:**
- "A standard high-efficiency solar panel is roughly 17.5 square feet" paired with "If each panel is 400W" — **internally inconsistent (T5)**: 400 W over 17.5 sq ft implies ~24.6% module efficiency, above any mass-market panel (commercial leaders ~22–24.5%). Either the area or the wattage in the worked example is wrong; the 4 kW / 5,000–6,000 kWh/yr outcome survives only because the panel count is what drives it.
- "Check for the **Federal Solar Tax Credit (ITC)**. Currently, this allows US homeowners to deduct a significant percentage of their solar installation costs" — **STALE (P1)**: post-Dec 31 2025 the residential ITC is $0. "Currently…a significant percentage" is now false even without a number. The sitewide ITC purge missed this page.
- "In many US states, **Net Metering** allows you to send excess energy…back to the grid in exchange for credits" — T3 but increasingly outdated (net billing successors in CA and elsewhere); the site's own net-metering-by-state-2026 page is not linked in the body.
- "you should insist on **Microinverters** or **DC Power Optimizers**" — T4 overstated ("insist"); contradicts nuance available on the site's own micro-vs-string-inverters page (also unlinked in body).
- "The answer is almost always **yes**" (ROI worth it) — T4, overstated; ignores small-system fixed-cost penalty and high-rate vs low-rate market variance.
- "a solar installation increases the resale value of your home" — T3-able claim (studies exist, e.g., Zillow/LBNL) but stated with no source; T5 as written.
- PERC explanation — T2/T3, technically fine, but PERC is being displaced by TOPCon in the current market; "Look for panels that feature PERC" is 2022-era advice (T4 staleness).

**(e) Amazon compliance: mechanically PASS** (no prices/ratings/review text; box discloses) — **substantively weak:** the Renogy 100 W 12 V panel is an off-grid/RV-class product on a page about grid-tied residential rooftops (net metering, installers, resale value). Same mismatch across all three panel pages — likely one box template reused.

**(f) Honesty: 2/5.** Limitations exist for thin-film and shingles (good), but the page oversells: "The answer is almost always yes," "a system that 'pays for itself,'" "provides a competitive edge in the real estate market" — all T4 with no hedging, no counter-scenarios (e.g., small systems carrying high fixed costs, low-credit net-billing states).

**(g) Structure: 3/5.** Good H2/H3 skeleton (8/17), step-by-step audit, worked math, pros/cons lists — but no tables, no FAQ schema (site pattern is 103/104 pages with FAQ), no TOC anchors, and the strongest internal links (efficiency page) appear only once.

**(h) AI/templated: YES — heavy.** Quoted tells: "Are you dreaming of lower electricity bills and energy independence but worried that your limited rooftop real estate will prevent you from going green?" (AI-question opener) / "Don't let the size of your roof dictate the size of your sustainable future. The technology exists to make even the smallest homes part of the clean energy revolution." / "Your journey to lower bills and a smaller carbon footprint starts with a single, well-placed panel." / "Every square inch of your roof should be evaluated for 'Solar Harvest Potential'" (invented-jargon flavor). Also keyword-stuffing tell: "finding the **best solar panels small roof** owners can utilize" — the head term jammed into prose ungrammatically.

**(i) Staleness: HIGH.** ITC "currently," PERC-as-frontier, net metering as universal, 2026 title with no updated date, and it is the canonical target — so its errors propagate to two URLs.

**ACTION: expand (it is the canonical survivor — the cluster's panel traffic should land here) · PRIORITY: P1 · Highest-impact fix:** (1) correct the ITC sentence to the post-2025 reality and (2) add an actual comparison — 3–4 named current panels with W, dimensions, efficiency, temp coefficient (T2, "per manufacturer spec") — because a "best panels" page with zero named panels cannot satisfy its own title.

---

## 6. mppt-vs-pwm.md — "MPPT vs PWM Charge Controllers (Comparison)" (1,992 w, 1 box, 3 tables, FAQ, date 2026-05-31)

**(a) Intent satisfaction: 5/5.** Short answer in the first paragraph ("pick MPPT when your panel voltage runs meaningfully above battery voltage, your array is bigger than about 200W, or your bank is 24V or 48V…"), then physics, worked math, honest caveats, a scenario-gain table, sizing checks, cost bands, FAQ. Nothing a serious buyer needs is missing; nothing is padded.

**(b) Per-product guidance: 2.5/5 for the single box — but appropriate for a comparison page.** The Victron 100/30 box ("Our MPPT pick") gets specs ✔ (100 V/30 A, Bluetooth, lithium presets), who-for ◑ ("most DIY builds standardize on"), alternative ✔ (the 4-model table directly above supplies the alternatives with price classes), NOT-for ✘, tradeoffs ✘. The comparison work is done at category level, which is the right shape for this query.

**(c) Methodology: 5/5.** Not a "best" page — selection basis is physics plus an explicit scenario table ("How much harvest MPPT actually gains, by scenario") with honest ranges. Fair by construction: it argues *for* PWM where PWM wins ("When PWM actually wins" section), which is the strongest fairness signal a comparison page can show.

**(d) Claim tiers:**
- Worked math (100 W panel: "12.8V × 5.56A ≈ **71W**" PWM vs "~7.4–7.6A" MPPT → "roughly **35% more charge current**") — T3-physics/T4, transparently derived with assumptions stated ("At a conservative 95–97% conversion efficiency"). Model of how to present derived numbers.
- "Panel open-circuit voltage rises roughly 0.3% per °C below 25°C" — T2/T3 generic coefficient stated as universal; same fix as page 1 ("typically ~0.3%; check the datasheet"). **Sitewide pattern — appears on at least 2 audited pages.**
- Price bands ("A basic 10A unit runs around $25, while the cheapest MPPT worth buying starts near $120"; "$120–$250 for the small class…") — T4 market bands, hedged ("roughly"), no source/date; drift-prone but framed as bands. Compliant (not Amazon listing prices).
- "Marketing says 'up to 30%.' Reality is a range" — T4 myth-busting, good.
- "an 18V-Vmp panel cannot charge a 24V bank…through PWM at all" — T3 physics, correct.
- "Victron 100/30 is what most small builds converge on" — T4, acceptable.
- FAQ adds the low-temperature lithium caveat ("lithium must not be charged below freezing") — the safety caveat missing from the buyer guide (page 1). Cross-reference noted.

**(e) Amazon compliance: PASS.** No prices in the box; tables use "Price class" (Budget/Mid-range), not dollars; no ratings or review text; box carries shortcode disclosure + sponsored rel. Body dollar bands are generic market bands, not listing prices — compliant.

**(f) Honesty: 5/5.** A section literally titled "**The honest caveats.**" ("That 35% is a best-case snapshot, not an everyday average"); PWM defended on its merits; failure mode named ("you end up on our not-charging checklist, or worse, with a dead controller").

**(g) Structure: 5/5.** Short answer → takeaways → 3 tables → step-by-step math → sizing checks → FAQ → dense contextual internal links. Minor: the product box sits after the FAQ, an odd terminal position.

**(h) AI/templated: none found.** Voice is specific and opinionated in the right places.

**(i) Staleness: LOW-MEDIUM.** The 4-model table mirrors the buyer guide (single point of update); price bands will drift; no `updated` front matter.

**ACTION: keep · PRIORITY: P3 · Highest-impact fix:** add "per manufacturer spec" attribution to the model table and the datasheet hedge on the 0.3 %/°C coefficient (both one-line edits).

---

## 7. pure-sine-vs-modified-sine-inverter.md — "Pure Sine Wave vs Modified Sine Wave Inverter (Which to Choose?)" (1,725 w, 1 box, 3 HTML tables, FAQ, date 2026-05-31)

**(a) Intent satisfaction: 5/5.** Short answer names device classes immediately ("Get a **pure sine wave inverter** if you run laptops, TVs, CPAP machines, refrigerators, microwaves, or any device with a motor or AC adapter"), and the "Device-by-device compatibility guide" table is precisely the artifact searchers want. Right depth for a serious buyer.

**(b) Per-product guidance: 2/5 for the single box.** Renogy 2000W Pure Sine ("Our pure sine pick"): specs ✔ ("2000W continuous pure sine with remote switch and cables included"), who-for ◑ ("mid-size off-grid loads where waveform quality actually matters"), NOT-for ✘, tradeoffs ✘, alternative ✘ (brand list in FAQ — "Victron, Renogy, AIMS, Samlex, Xantrex" — partially covers it). Acceptable for a comparison page, but the box is the page's only product and it's thin.

**(c) Methodology: 4/5.** Decision guide is criteria-based and fair: "**Choose pure sine wave if you run ANY of:** … **Modified sine is acceptable if ALL of these are true:** …" — an explicit AND-list that makes modified sine hard to qualify for honestly, which is the correct editorial stance. No ranking pretense.

**(d) Claim tiers — one serious violation:**
- **"Real-world measurements show 10–20% efficiency loss in motorized devices on modified sine" — T5 dressed as T1 (P2).** "Real-world measurements" implies firsthand testing; the site's own trust pages state no test lab exists and "assume nothing here has been bench-tested by us," and this page documents no build. This is the fact-pack's hard boundary ("Never present T2-T5 as T1") violated in one sentence. Fix: reword to research-framed ("commonly cited engineering estimates put…") or attribute a source.
- "~99% of devices work fine" / "~60–70% of devices work; many run poorly" — **T5 with invented-looking precision** (no basis given for device-population percentages).
- "may run **15–25°F hotter**" — T5, specific number, no source.
- "A fridge that lasts 12 years on grid power may last 2–4 years on modified sine" — T5, unsourced lifespan numbers.
- "ResMed, Philips, and most CPAP manufacturers explicitly require pure sine wave" — T2-plausible and checkable, but unattributed as written; the site's own cpap-battery-backup-guide should be linked/cited here (currently is not).
- Price tables ("300W: $35–$70 / $25–$45…") — T4 market bands, hedged ("typical"), no date/source beyond "in 2026"; drift-prone.
- "85–92% conversion" — T2/T3 typical range, acceptable.
- FAQ THD passage is self-contradictory as written: "Cheap inverters labeled 'pure sine' may deliver <3% total harmonic distortion (THD) — good enough for almost everything. Ultra-cheap units may claim pure sine but measure 5–8% THD" — the first sentence praises cheap units with a *good* THD figure; presumably ">3%" was meant. T5 numbers, clarity defect.

**(e) Amazon compliance: PASS with one placement defect.** No prices in the box, no ratings, no review quotes; body dollar tables are generic market bands (compliant). **Defect: the product box is nested INSIDE the last FAQ answer** — the shortcode sits between the THD answer text and its `{{< /faq >}}` closing tag, so the box renders inside an FAQ answer block (layout/semantics wrong; FAQ schema pollution risk). Move it to a standalone position.

**(f) Honesty: 4/5.** Strong: "Damage is cumulative, not instant," "The risk is real and unpredictable," modified sine given genuine use cases, "Trusting old forum advice" myth-busted. Deduct for the T1-impersonating measurement claim and the device-percentage fiction.

**(g) Structure: 4/5.** Three tables (device compatibility is excellent), decision lists, FAQ. Tables are raw HTML `<table>` blocks rather than markdown — renders, but note the quality-signals scan counted this page at **0 tables** (it only counts markdown tables), so Boss dashboards undercount HTML-table pages. Box-in-FAQ is the structural defect.

**(h) AI/templated: none found.** Specific, opinionated, device-level detail reads human-edited.

**(i) Staleness: MEDIUM.** Price bands and "in 2026" framing; brand list stable; no `updated`.

**ACTION: update · PRIORITY: P2 · Highest-impact fix:** reword the "Real-world measurements show 10–20% efficiency loss" sentence to research-framed attribution (it currently claims firsthand testing the site disclaims), and move the product box out of the FAQ answer.

---

## 8. 12v-vs-24v-vs-48v-solar.md — "12V vs 24V vs 48V Solar Systems: Key Differences" (1,983 w, 2 boxes, calculator, 2 md + 1 HTML tables, FAQ, date 2026-05-31; traffic 70 pv / 80.4% bounce)

**(a) Intent satisfaction: 5/5.** Key takeaways answer-first ("**12V** is the standard for small systems… **24V** is the sweet spot… **48V** is the right choice for whole-home backup"), then a literal decision table ("If your max continuous load is… Choose"), an interactive pick-your-voltage calculator, worked wire-cost math, use-case sections, mistakes, FAQ. Depth is right; the calculator adds stickiness the page-level bounce rate doesn't reflect (calculators cluster bounce 6–33% per fact pack).

**(b) Per-product guidance (avg 3/5):**
- LiTime 12V 100Ah — who-for ✔ ("value benchmark for starting a 12V bank"), NOT-for ◑ ("Going 24V/48V? Series/parallel-match these"), tradeoffs ✘, specs ✔ (100A BMS, low-temp protection), alternative ✘. **3/5**
- Victron SmartSolar 100/30 — who-for ✔ ("the controller that grows with a voltage upgrade"), NOT-for ✘, tradeoffs ✘, specs ✔ ("Auto-detects 12V/24V (48V-capable across the range)"), alternative ✘. **3/5**

**(c) Methodology: 5/5.** Selection basis is encoded as an explicit decision table plus a calculator that "applies the decision table above" — scenario-match, transparent, reproducible. "Whole-home backup → 48V (no exceptions)" is assertive but consistent with its own table.

**(d) Claim tiers:**
- Current math (1,200 W → 100 A / 50 A / 25 A) — T3 physics, correct.
- Wire sizes/costs ("2 AWG ($6/ft)", "~$5–$7/ft", "20-foot round-trip…$100–$140") — T4/T5 market bands, no source or date; plausible, drift-prone (copper prices).
- "server-rack lithium batteries (like EG4, SOK, or rack-mount LiFePO₄) which are the cheapest per-kWh option on the market" — **T4 stated as market fact, unhedged**; true for the new DIY class but "on the market" overreaches. Add "in the new DIY class."
- "Max practical inverter size ~2,000W (12V)" — T4 consensus, fine.
- Safety honesty is strong: "Undersized wire at these currents is a serious fire risk," "Get this wrong and you'll damage equipment or create a fire hazard."
- Calculator output self-hedges: "Planning guidance; confirm equipment availability before committing." Good.

**(e) Amazon compliance: PASS.** No prices in boxes, no ratings, no review text; wire-cost tables are generic bands, not listing prices; boxes disclose via shortcode.

**(f) Honesty: 4.5/5.** Upgrade-cost honesty ("It's cheaper to choose the right voltage upfront than to upgrade later"), DC-DC converter costs named ($30–$60), exceptions given (mega RVs → 24V). Minor deduction for the unhedged "cheapest per-kWh" claim.

**(g) Structure: 5/5.** Decision table + calculator + comparison table + worked example table + mistakes + FAQ. Tied with best-solar-batteries-2026 as the cluster's best-structured page. Note: comparison table is raw HTML — the quality-signals scan (markdown-table counter) undercounts it (6 counted vs 7 actual); same scan blind spot as the pure-sine page.

**(h) AI/templated: low.** "bus bars the size of a brick," "welding-cable territory" — human-voiced. No AI-tell passages.

**(i) Staleness: LOW-MEDIUM.** Copper/wire prices drift; brand mentions stable; no `updated`. High-traffic page — freshness matters more here than elsewhere.

**ACTION: update · PRIORITY: P3 · Highest-impact fix:** move the two product boxes out of the FAQ answer (same nesting defect as the pure-sine page) and fix the twice-repeated "How to choose solar system voltage" links that point at this page's own slug instead of how-to-choose-solar-system-voltage.html.

---

## 9. solar-components.md — "Solar Components Explained: Panels, Inverters, Batteries" (2,397 w, 2 boxes, 2 HTML tables, FAQ, date 2026-05-31; traffic 30 pv / 24.1% bounce)

**(a) Intent satisfaction: 5/5.** "Quick answer" reframes the query usefully ("A solar-electric system is **eight jobs, not eight brand decisions**"), then a components table with cost shares, a "one spec that matters most" table, per-component sections each ending in a worked example, and a build-order path. The 24.1% bounce (2nd-lowest in the traffic table) confirms it satisfies.

**(b) Per-product guidance (avg 2.5/5):**
- Renogy 100W panel — who-for ◑ ("The module most component guides describe by default"), NOT-for ✘, tradeoffs ✘, specs ◑ ("monocrystalline, IP67"), alternative ✘. **2/5**
- Victron 100/30 — who-for ◑ ("The charge controller component diagrams are drawn around"), NOT-for ✘, tradeoffs ✘, specs ✔ (MPPT, 12/24V auto-detect, lithium presets, Bluetooth), alternative ✘. **3/5**
- Defensible for a foundations page — the boxes are framed as reference components, not picks — but the descriptions are circular ("most component guides describe by default" / "component diagrams are drawn around" — which component guides? whose diagrams? T5 self-reference).

**(c) Methodology: 4/5.** Not a "best" page; selection basis is the "one spec that matters most" table — a defensible editorial framework, consistently applied. No ranking claims.

**(d) Claim tiers:**
- ITC handled correctly and twice: "there is **no federal tax credit for 2026 installs** (the 30% ITC expired December 31, 2025 under P.L. 119-21 — budget full price, payback about 10–13 years in high-cost states)" — T3 with statute citation; the cluster's most precise ITC statement. (Note: payback 10–13 years is T4, unhedged but plausible.)
- Cost shares ("panels and the battery dominate… roughly **25–40% each**", "inverter runs 10–18%") — T4, framed as "roughly," internally consistent across sections (though the table says panels 25–45% vs prose 25–40% — minor inconsistency).
- Worked math (625 W panel example; 73 V cold Voc; 3.5 kWh usable; 250 A battery cable) — T3-physics, transparently derived. The 0.8 system-efficiency penalty and 3% voltage-drop target are stated as conventions — fine.
- "10–25% of rating under heavy cloud" — T3-plausible, hedged.
- "AC-rated breakers may not clear DC arcs" — T3 (NEC-grounded), correct and safety-relevant.
- "lead-acid ruined by chronic under- or over-charging is the classic off-grid failure" — T4, fair.
- No T1 impersonation; no T5 found. Cleanest tier hygiene of the 12V-class pages.

**(e) Amazon compliance: PASS.** No prices, no ratings, no review text; boxes disclose; body cost figures are generic bands.

**(f) Honesty: 5/5.** Safety-forward throughout ("This is where DIY solar fires start," "Protection…is not optional — it is what keeps a wiring fault from becoming a fire," NEC rapid-shutdown named, links to safety/permits pages). Limitations of each topology stated.

**(g) Structure: 5/5.** Two tables, worked math per section, 41 internal links (highest in cluster), FAQ + faq-schema, build-order line. The hub page done right.

**(h) AI/templated: none found.** "Voltage-only 'battery percentage' lies under load" — human voice.

**(i) Staleness: LOW.** ITC statement is current and dated; cost bands drift slowly; no `updated`.

**ACTION: keep · PRIORITY: P4 · Highest-impact fix:** reconcile the 25–40% vs 25–45% panels-share inconsistency between prose and table, and give the two boxes one real tradeoff line each (e.g., Renogy: "not the cheapest per watt in 2026 — check current per-watt leaders").

---

## 10. how-to-choose-solar-inverter.md — "How to Choose a Solar Inverter: Types, Sizing, and What Matters in 2026" (1,565 w, 1 box, 2 HTML tables, FAQ-as-H3, date 2026-05-31)

**(a) Intent satisfaction: 4/5.** Type-comparison table up top with the right framing ("Your use case — grid-tied vs off-grid, with or without batteries, shaded vs unshaded — largely determines which type you need before you even look at brands or models"), per-type sections, sizing rules with a worked surge example. Deduct: no quick-answer paragraph (the table must do that work) and the FAQ is plain H3 markdown — no `{{< faq >}}` shortcode or trailing `{{< faq-schema >}}`, deviating from the site's own pattern.

**(b) Per-product guidance: 3/5 for the single box.** Renogy 2000W ("A safe default choice"): who-for ✔ ("If the sizing math in this guide points you at 2000W continuous"), NOT-for ✘, tradeoffs ✘, specs ✔ ("pure sine, remote switch, cables in the box"), alternative ✔ (the 5-type table plus brand lists). Brand mentions (Victron, Outback, SMA, Enphase, SolarEdge, Generac) include named models ("An Outback FXR3048A or Victron MultiPlus-II 48/3000 would both work") but with zero specs or attribution.

**(c) Methodology: 4/5.** Type-first decision framework, explicit and fair; "safe default choice" is honest box framing. No ranking pretense.

**(d) Claim tiers — two math passages that contradict each other (P2):**
- Body: "Over 20 years, a 1% efficiency difference on a 6kW system at $0.15/kWh = approximately **$1,600** in production value." Check: a 6 kW system produces ~8,500–9,500 kWh/yr in most US markets; 1% ≈ 85–95 kWh/yr → 20 years ≈ 1,700–1,900 kWh ≈ **$260–$290**, not $1,600. Off by ~6×.
- FAQ: "on a 6kW system in a **1,700kWh/year** production environment, that's about 51 kWh/year, worth roughly $7.65/year… a 40-year payback." The arithmetic is internally consistent, but 1,700 kWh/yr for 6 kW is ~5× too low (real US residential yield ≈ 1,300–1,600 kWh per kW per year). So the two passages disagree with each other by an order of magnitude, and both rest on wrong baselines. T5 math presented as fact.
- "90–120% of your panel array's STC wattage" (body) vs "90–110%" (FAQ) — internal inconsistency, minor.
- "Enphase dominates the US microinverter market" — T3-plausible but unsourced/undated → T5 as written.
- "**Top brands:** SolarEdge…, SMA, Fronius, Growatt, Huawei/iStore" — T5; "Huawei/iStore" is an Australian-market pairing and reads as a copy artifact in a US-focused guide (flag for Boss verification).
- "25 years for Enphase microinverters" — T2, checkable, unattributed.
- "from a brand that honors warranties" (box) — T4/T5 unverifiable service-quality claim.
- Worked surge example ("roughly 950 + 4,000 ≈ **5,000W**") — T3-physics, correct (fridge+AC running plus pump surge).

**(e) Amazon compliance: PASS.** No prices in the box; body cost bands are generic ranges; no ratings or review text; disclosure present.

**(f) Honesty: 3.5/5.** Good: array-clipping explained honestly, "don't pay a premium for 97% vs 96.5%," grid-code compliance check, replacement-cost planning ("expect to replace a string inverter once… ~$1,000–$2,500"). Deduct for the contradictory efficiency math and the warranty-service claim.

**(g) Structure: 3.5/5.** Anchor nav, two tables, worked example, FAQ. No FAQ schema shortcode; tables are HTML (scan undercount applies here too).

**(h) AI/templated: low.** "This is the fastest-growing inverter category in 2026 as home battery storage becomes mainstream" is generic market-speak; the rest is specific.

**(i) Staleness: MEDIUM.** Brand lists (Huawei oddity), price bands, "fastest-growing in 2026," no `updated`.

**ACTION: update · PRIORITY: P2 · Highest-impact fix:** reconcile the two efficiency-dollar passages onto one correct baseline (a 6 kW system at ~9,000 kWh/yr makes 1% worth ~$270 over 20 years — which actually *strengthens* the page's "don't pay for efficiency" advice), and drop or re-verify the Huawei/iStore brand entry.

---

## 11. solar-system-sizing.md — "How to Size a Solar System (Step-by-Step Load Planner)" (1,362 w, 3 boxes, interactive planner, FAQ, date 2026-05-31, **updated 2026-08-09**; traffic 73 pv / 19.8% bounce — lowest in the site's top-traffic list)

**(a) Intent satisfaction: 5/5.** Key takeaways → five steps → an interactive load planner that outputs array, battery, inverter, and controller sizes with assumptions labeled. The 19.8% bounce (best in the traffic table) is empirical confirmation of intent fit.

**(b) Per-product guidance (avg 2.3/5):**
- Renogy 100W — who-for ◑ ("the module to check the number against"), NOT-for ✘, tradeoffs ✘, specs ✘ (description contains no specs), alternative ✘. **1.5/5** — weakest box in the cluster. Its description also embeds a price claim: "the **$1/Watt benchmark**" — T5, drift-prone, and the closest any box comes to a price statement (see (e)).
- LiTime 12V 100Ah — who-for ✔ ("the unit most DIY banks multiply by"), NOT-for ✘, tradeoffs ✘, specs ✔ (1.28 kWh, 100A BMS, low-temp protection), alternative ✘. **2.5/5** ("come standard in the arithmetic" is a strained phrase).
- Victron 100/30 — who-for ✔ ("If your controller sizing lands in the 20–30A range"), NOT-for ✘, tradeoffs ✘, specs ✔ (100V ceiling, lithium presets, Bluetooth), alternative ✘. **3/5**
- Coherence note: the calculator defaults to **48 V** and the worked controller example lands at **104 A** — both outside the 30 A box pick's class. The description hedges honestly ("If your controller sizing lands in the 20–30A range"), but the page's own default path leads away from its own box.

**(c) Methodology: 5/5.** The calculator is the methodology, with formulas printed in prose ("**Controller amps ≈ (Panel watts ÷ Battery voltage) × 1.25**") and assumptions shown in the results table ("80% DoD LiFePO4 assumed," "Sized for daily load + 20% losses," "2× peak running load + surge headroom"). Transparent and reproducible.

**(d) Claim tiers:**
- Calculator formulas — T3-physics/T4 conventions, disclosed. **One internal inconsistency (P3): the tool sizes the inverter at "2× peak running load" while Step 4 prose says "add ~25% headroom… then verify the worst startup moment."** Two different rules, one page; a user comparing them gets different answers.
- "the $1/Watt benchmark" — T5 price claim (drift-prone; also the only box text in the cluster that characterizes price at all).
- "the unit most DIY banks multiply by" — T4, acceptable.
- Mistakes list (winter undersizing, inverter efficiency ~10%, surge 3–7×) — T4, sound, consistent with the cluster.

**(e) Amazon compliance: PASS with one flag.** No listing prices, no ratings, no review text; boxes disclose. The "$1/Watt benchmark" phrase is a market-price characterization rather than an Amazon price — compliant, but it will silently rot as panel prices move; reword to a class description.

**(f) Honesty: 4/5.** Winter undersizing, surge, expansion planning all named. Deduct for the tool-vs-prose inverter-rule conflict and the price claim.

**(g) Structure: 5/5.** Interactive planner + 5 steps + mistakes + FAQ + faq-schema. Empirically the stickiest page in the cluster.

**(h) AI/templated: none found.**

**(i) Staleness: LOW-MEDIUM.** Carries `updated = 2026-08-09` — see synthesis correction to Boss finding #3 (7 pages site-wide do set it; this is one). The $1/W box claim is the main drift vector.

**ACTION: keep · PRIORITY: P3 · Highest-impact fix:** align the calculator's inverter rule (2× peak) with the prose rule (~25% headroom + surge verification) so tool and text give one answer, and replace the "$1/Watt benchmark" box phrase with a class description.

---

## 12. solar-generator.md — "Solar generator guide" (2,028 w, 2 boxes, 3 tables, FAQ, date 2026-05-31)

**(a) Intent satisfaction: 5/5.** Quick answer defines the product class honestly ("it is a *finite* energy store, not a fuel machine… If your goal is whole-house backup through multi-day outages, a power station is usually the wrong tool"), then capacity tiers with honest runtimes, surge math, recharge math, DIY comparison, and seasonal sections. Complete for the buyer intent.

**(b) Per-product guidance (avg 4.5/5 — best box treatment in the cluster):**
- BLUETTI AC180 — who-for ✔ ("The 1kWh-class benchmark"), NOT-for ◑ (covered at class level by "Who should NOT buy"), tradeoffs ✔ ("Power stations sell integration; DIY sells watt-hours per dollar"), specs ✔ with attribution ("1,152Wh LiFePO4 with 1,800W continuous and 2,700W surge… **Per manufacturer spec**"), alternative ✔ (the LiTime DIY box directly below with the cost tradeoff). **4.5/5**
- LiTime 12V 100Ah — who-for ✔ ("The DIY-path building block"), NOT-for ✔ ("You supply the inverter, charging, and fusing"), tradeoffs ✔ ("more usable watt-hours than a 1kWh power station, at a lower cost per Wh"), specs ✔, alternative ✔. **4.5/5**

**(c) Methodology: 5/5.** Class-tier selection ("Capacity tiers: what each class actually runs" with a runtime table), plus the cluster's only dedicated "**Who should NOT buy a solar generator**" section ("Whole-home backup buyers… Anyone who hasn't done the load math"). Scenario-match, not ranking.

**(d) Claim tiers:**
- "Per manufacturer spec" on the BLUETTI box — T2 attributed ✓ (confirms Boss finding #2's exception list).
- "current-generation units use LiFePO4 rated 3,000–6,000 cycles… Older NMC units age out in 500–800 cycles" — T2-generic, hedged ("rated"), fine.
- "a 200W panel returns roughly 700–900Wh on a good day" — T3-physics, derating shown (×0.8).
- "most LiFePO4 packs refuse or strictly limit charging below 0°C / 32°F — the BMS uses a low-temperature cutoff to prevent lithium plating" — T2/T3, correct and safety-relevant; "Some stations have self-heating cells; plan as if yours does not" is model-agnostic honesty.
- "northern states get 2–3 peak sun hours in winter versus 5–6 in summer" — T3 planning range; an HTML comment in the source documents corroboration ("Corroborated live: DOE Solar Radiation Basics… ENERGY STAR Refrigerators…") — good practice, but the comment also carries internal scaffolding: "per work order w3-seasonal (2026-09-05)" — invisible to users, should still be cleaned from source.
- "Storm-day panel yield (10–25% of rated)… are planning ranges, not guarantees" — T4, hedged ✓.
- "a fridge or freezer in an unheated garage or porch draws less in cold air" — T3-plausible, correctly paired with "Just don't store the battery itself in that unheated space."

**(e) Amazon compliance: PASS.** No prices, no ratings, no review quotes; boxes disclose; T2 attribution inside the box description.

**(f) Honesty: 5/5.** "a big station with a small panel is a slow tank," "Buy the notebook before the battery," gas-generator hybrid recommended for medical loads, "brush, don't scrape" (snow), day-2 recharge framing. No overstatements found.

**(g) Structure: 5/5.** Four tables (tiers, DIY comparison, outage planning, seasonal yield), worked math, FAQ. Long but dense.

**(h) AI/templated: none found.** Strong human voice throughout.

**(i) Staleness: MEDIUM.** Model-specific (AC180), seasonal ranges stable; internal work-order comment in source; no `updated` param.

**ACTION: keep · PRIORITY: P3 · Highest-impact fix:** remove the internal HTML comment ("Seasonal-planning ranges per work order w3-seasonal…") from the source and add `updated` front matter; content-wise this page needs nothing.

---

## 13. what-size-solar-generator-run-refrigerator.md — "What Size Solar Generator to Run a Refrigerator?" (1,945 w, 1 box, 3 HTML tables, FAQ, date 2026-08-19) — **auditor's addition to reconcile the 13-page count**

**(a) Intent satisfaction: 5/5.** The cluster's best answer-first execution: "Most full-size refrigerators need a solar generator rated for **at least the fridge's running watts — typically 100–250W…** with **surge capacity 2–4× that**… and roughly **1–2.4kWh of battery per 24 hours**… But do not size from averages." Then three measurement methods, three worked examples, surge section, runtime formulas, recharge reality, buying checklist.

**(b) Per-product guidance: 3/5 for the single box.** Jackery Explorer 1000 v2: who-for ✔ ("Mid-size fridge class pick… covers the modern-fridge class from the worked examples"), NOT-for ✘, tradeoffs ✘, specs ✔ with attribution ("1070Wh LiFePO4 with 1500W continuous / 3000W surge… 4,000-cycle rated cells **per manufacturer spec**"), alternative ✘ (the spec checklist partially covers). 

**(c) Methodology: 5/5.** The section header is the methodology statement: "**Buying checklist (no brands bought here — specs you verify)**" and "Before you buy, verify these specs on the datasheet — not the marketing page." Measure-your-own-fridge framing ("buy for your worst day, not the label") is the fairest possible basis for a product page.

**(d) Claim tiers:**
- Duty-cycle math ("150 × 0.40 × 24 = **1,440 Wh/day**") — T3-physics, transparent; I re-checked every worked number on the page (1,440 / 4,200 / 840 / 2,280 Wh; 0.30 days ≈ 7 h; 22%; 450 W) — all correct.
- "running roughly **30–50% of the time**" — T3-plausible, hedged.
- "Soft-start kits… cutting start surge by roughly 50–70%. They cost $100–300" — T4/T5 bands, no source; plausible, drift-prone.
- "A fridge with 6.5A running might pull 30–40A for a fraction of a second at start — that's 3,450–4,600W at 115V" — T3-physics, correct LRA framing.
- "Per manufacturer spec" on the box cycle rating — T2 attributed ✓ (confirms Boss finding #2's exception list).
- "A 450W array on a fully overcast day might deliver 10–20% of rated output" — T4, hedged ✓.
- EnergyGuide method ("500 ÷ 365 = **1.37 kWh/day**… Use it as a floor, not a ceiling") — T3, program-grounded.

**(e) Amazon compliance: PASS.** No prices, no ratings, no review text; box discloses; T2 attribution present.

**(f) Honesty: 4.5/5.** A section literally titled "**Cloudy-day honesty**," "**Red flags in marketing**" ("A '2,000W peak' station that only delivers 1,000W continuous will not start a fridge needing 1,800W surge"), "500Wh is a short-term buffer, not an outage solution," soft-start safety framed as "installed per the manufacturer's instructions." Deduct for the scaffolding defect below.

**(g) Structure: 4/5 — with one P2 defect: a leftover "## Image Prompts" section renders in the live page.** Quoted: "## Image Prompts / 1. **Placement: H2-1, after the intro paragraph.** Concept: a clean three-number diagram (Running Watts / Surge Watts / Daily Wh) overlaid on a modern refrigerator… photorealistic, 16:9." Three AI-image-generation prompts sit as visible page content after the FAQ. This is production scaffolding exposed to readers — a trust-killer for exactly the careful buyers this cluster targets, and it also means the page has no trailing `{{< faq-schema >}}` (pattern deviation vs. sibling pages; verify schema impact in layouts).

**(h) AI/templated: the Image Prompts section is literal AI-workflow residue** (quoted above). Body prose itself is clean, specific, and human-voiced.

**(i) Staleness: LOW.** Newest page in the cluster (2026-08-19); Jackery model naming is the only churn vector.

**ACTION: update · PRIORITY: P2 · Highest-impact fix:** delete the "## Image Prompts" scaffolding section from the live page (it renders today), and add a NOT-for/tradeoff line to the Jackery box.

---

# SYNTHESIS — Is the buyer cluster trustworthy to a careful buyer?

**Verdict: split down the middle, and the split is generational.** Twelve of the thirteen pages carry `date = 2026-05-31`; the cluster contains two clearly distinct editorial generations. **Generation 2** (best-solar-batteries-2026, solar-generator, what-size-solar-generator-run-refrigerator, mppt-vs-pwm, best-mppt-charge-controllers, solar-components, 12v-vs-24v-vs-48v-solar, solar-system-sizing) is genuinely good: answer-first, scenario-matched methodology, hedged claims, worked math that checks out, safety caveats, and — on 3 pages — real T2 attribution ("per manufacturer spec," retrieval dates). **Generation 1** (the three panel pages, plus defects inside how-to-choose-solar-inverter and pure-sine-vs-modified-sine) is the opposite: AI-flavored prose, unsourced T5 numbers, zero named products with specs, and — worst — **three pages still telling buyers the federal ITC exists** after the Boss-verified Dec 31 2025 expiry. A careful buyer who lands on the panel trio gets a materially wrong tax picture and a "17 panels for 5 kWh/day" math error; the same buyer on the batteries or fridge pages gets honest, verifiable guidance. The cluster as a whole is **not yet uniformly trustworthy — the panel trio is the trust hole**, and because two of them are canonicalized duplicates that still render with product boxes, the hole is three URLs wide.

**3 WORST (with reasons):**
1. **best-solar-panels-for-home-2026 (P1)** — canonical duplicate still fully live with a mismatched box; "heterojostunction" typo; unsourced 15%-gain and $1.00–1.50/W claims; **LG NeON R presented as a 2026 model "to watch" — LG exited the solar panel business in 2022 (verified: lg.com newsroom, Feb 23 2022, production ceased June 2022; retrieved 2026-09-05)**; zero named buyable products; the cluster's clearest AI-generated prose.
2. **best-solar-panels-for-small-homes (P1)** — live page says "The Federal Investment Tax Credit (ITC) allows you to deduct **26%**" (two generations stale; contradicts the site's own corrected pages) and carries an off-by-4–8× sizing example ("5 kWh… approximately 17 panels"); "sleunck" typo; LG again.
3. **best-solar-panels-small-roof (P1)** — the canonical survivor, so its errors propagate: "Currently… deduct a significant percentage" (false post-2025), a "best panels" page that names zero panels, 400 W-on-17.5-sq-ft internal inconsistency, PERC-as-frontier staleness, heavy AI phrasing.

**3 BEST (with reasons):**
1. **best-solar-batteries-2026** — the cluster's methodology gold standard ("every pick is a 'best for' scenario match, not a ranking"), full T2 attribution with retrieval dates, derived figures labeled derived, "Installed batteries are not Amazon items" expectation-setting, honest DIY-risk framing. Only fix: the 12 V-box/48 V-section mismatch.
2. **solar-generator** — best per-product guidance in the cluster (4.5/5 both boxes, "Per manufacturer spec" in-box), a dedicated "Who should NOT buy" section, seasonal honesty with DOE-corroborated planning ranges, zero overstatements found.
3. **mppt-vs-pwm** — a comparison page that argues *for the option it doesn't sell* ("When PWM actually wins"), publishes its own math with assumptions, and labels the industry's "30%" claim as best-case. (Runners-up: what-size-solar-generator-run-refrigerator — best answer-first execution, all worked math verified correct, but marred by the live "## Image Prompts" scaffolding; solar-system-sizing — best engagement metrics, 19.8% bounce, but tool-vs-prose rule conflict.)

**Cross-cutting findings for the Boss (beyond per-page notes):**
- **Fact-pack correction #3:** `updated` front matter is NOT zero site-wide — **7 pages set it** (solar-system-sizing, battery-capacity, net-metering-by-state-2026, solar-panel-tax-credit, read-solar-panel-specs-sheet, solar-panel-output, solar-inverter-sizing; verified by regex). The finding should read "133 of 140 lack it," and the 7 existing uses prove the template already supports it — rollout is config, not code.
- **Fact-pack confirmation #2:** spec attribution exists on exactly the 3 pages the Boss listed; the other 10 audited box pages state T2 specs bare. The one-line fix ("per manufacturer spec") is proven viable by the existing 3.
- **Amazon compliance is 13/13 PASS mechanically** (no prices, no ratings, no review text; shortcode disclosure + sponsored rel verified in fact pack). Substantive issues are mismatch/misplacement, not disclosure: the same Renogy 100 W box (asin B07GF5JY35) is reused on 4 pages with 4 different rationales, 3 of which mismatch the page topic; 2 pages nest boxes inside FAQ answers.
- **Repo-wide hygiene bugs found:** (1) escaped `\#` H1 renders as literal text on 10 pages; (2) "## Image Prompts" scaffolding renders live on the fridge page; (3) internal work-order HTML comment in solar-generator source; (4) quality-signals.tsv counts only markdown tables, so HTML-table pages (pure-sine, 12v-vs-24v, components, inverter) are undercounted in Boss dashboards.
- **Recurring T2/T3-as-fact pattern:** the ~0.3%/°C Voc temperature coefficient appears on 2+ pages as a universal constant (datasheets range ~0.25–0.5); "per manufacturer spec" should be paired with a datasheet hedge wherever coefficients appear.
- **Staleness posture:** 12/13 pages dated 2026-05-31 with no visible review date; the "2026" titles now carry the entire freshness signal. The ITC purge (Boss-verified as done) missed 3 pages in this cluster — recommend a sitewide grep for "ITC"/"tax credit" as a completeness check beyond it.

**Checks performed:** all 13 files read in full (multi-window where truncated); every worked math example re-computed (2 errors found: 17-panel example, inverter-efficiency dollars); claim tiers tagged with verbatim quotes; box/FAQ nesting verified in source; `updated` front matter verified sitewide by regex; LG solar exit verified via Brave search (lg.com newsroom, retrieved 2026-09-05); Amazon-compliance checked per page against fact-pack rendering facts. **Unresolved blockers:** (1) "SunPower Maxeon LX" model existence and SunPower's current residential status — could not verify with available tools (T5, flagged for Boss); (2) whether FAQ-schema output is affected by boxes nested inside `{{< faq >}}` blocks — requires a rendered-HTML check outside my roots; (3) the intended 13th page if my reconciliation (fridge page) differs from the Boss's list — method transfers directly.