# Seat B — Buyer-Tail Editorial Audit (24 product-box pages)
Auditor: glm-xo-2 · Session 20260905T235849Z-ca-buyer-tail · Rubric: (a) intent (b) product coverage (c) methodology visibility (d) claim tiers (e) Amazon compliance (f) overstatement/limitations/safety (g) scannability vs depth (h) AI-sounding passages (i) staleness risk + box-intent-fit verdict per page.

Claim tiers: T1 firsthand-tested · T2 manufacturer-stated · T3 reputable third-party (source+date) · T4 editorial judgment · T5 unknown/unverified.

STATUS: REPAIR ROUND 1 — 13 audited in first pass; remaining 11 appended below (full rubric), then final synthesis.

---

## 1. solar-system-costs.md — Solar System Cost Breakdown (2 boxes)
Signals: 1,982 words · 2 boxes · 0 calc · FAQ yes · 11 H2 · 0 tables counted by script (6 real HTML tables) · 0 internal links counted (many present) · date 2026-05-31.

**(a) Intent:** Strong. "Quick answer" box up top with $/W and 6kW totals; three worked budgets (2kW cabin / 6kW grid-tied / 10kW+10kWh) with line-item arithmetic; "What changed in 2026" section. Satisfies "what does a solar system cost" fully, DIY vs installed both priced.

**(b) Product coverage:** Two boxes, each a single product. Renogy 100W box: who-for implicit (quote-shoppers), tradeoff framing good — "hardware like this shows what the other $1.50 buys — labor, rails, permitting, and the installer's margin on the same watts." No not-for, no alternatives, no spec beyond implied $/W. LiTime box: "the battery that defines the benchmark for what storage should cost" — no spec (kWh stated only in body text: "about 5.1kWh" for four units), no not-for, no alternative (server-rack battery mentioned in body but not in box).

**(c) Methodology visibility:** No "how we picked" anywhere; boxes are illustrative anchors, not "best" claims, so requirement is soft — but "defines the benchmark" is a superlative with zero visible method. T4 at best.

**(d) Claim tiers:** Load-bearing cost figures ($2.50–$3.50/W installed; $15,000–$21,000 for 6kW; battery $1,000–$1,400/kWh installed; payback 10–14 years) are all T5-as-presented — no source, no date, no "editorial estimate" label. ITC expiry (P.L. 119-21, Dec 31 2025) is T3-grade fact but uncited inline. Tesla Powerwall 3 "roughly $15,000" — T5, no source/date. This is the page's biggest E-E-A-T gap: money claims with no visible provenance.

**(e) Amazon compliance:** No prices/ratings/review text in either box ✓. Box shortcode prints disclosure + rel=sponsored (verified in layouts per fact-pack) ✓. Page body has `{{< affiliate-disclosure >}}` at top ✓. No Amazon links outside boxes ✓.

**(f) Overstatement/limitations/safety:** Good honesty: "If you cut anything, do not cut the wiring and protection line — that is the one that keeps the cabin from burning down." DIY-vs-installed tradeoffs stated ("you take on design, permitting paperwork, and the utility interconnection application yourself"). Limitation: no electrical-work hazard caveat on the DIY path (NEC/permitting mentioned but no "get a licensed electrician for the AC side" line).

**(g) Scannability vs depth:** Excellent — quick answer, key takeaways, three tiered budgets, share table, FAQ. Depth is real (arithmetic shown per line). One defect: "Next logical reads" block has duplicated state-guide links in two formats (list + trailing `/guides/...` links) — looks machine-assembled.

**(h) AI-sounding passages:** Mostly concrete and voice-y ("your own two weekends", "keeps the cabin from burning down"). Weak spot: "The DIY battery column is the same chemistry and capacity bought as components — which is exactly the delta the installed quote is charging you to avoid thinking about." — convoluted, near-templated. Minor.

**(i) Staleness risk:** HIGH. Every dollar figure is 2026-dated; page will silently rot. No `updated` front matter (sitewide issue). ITC section is correct now but must be re-checked annually.

**Box-intent fit:** SUPPORT, both. Renogy box lands exactly at the "$/W reality check" moment; LiTime box anchors the battery line. Neither interrupts a troubleshooting flow. Keep both. Minor: LiTime box would be stronger with the 5.1kWh/4-unit math inside the box description.

**ACTION:** Add source/date attribution to the five load-bearing cost figures (T3 citations or explicit "editorial estimate, checked {month}"). **PRIORITY:** Medium-High (high-traffic money page, 47pv/37.7% bounce — engaged readers). **Highest-impact fix:** one-line "Cost ranges compiled from {source(s)}, checked September 2026" under the first table + `updated` front matter.

---

## 2. cabin-solar-cost.md — Off-Grid Cabin Solar Cost (2 boxes)
Signals: 710 words · 2 boxes · 0 calc · FAQ yes · 7 H2 · 0 internal links counted (many present) · date 2026-05-31.

**(a) Intent:** Adequate but thin. 710 words for a "cost breakdown" query. Tier table ($1,000–$3,000 / $3,000–$9,000 / $9,000–$20,000+) + component table + overspend section. No worked example budget (unlike solar-system-costs) — the reader never sees an actual cabin build priced line-by-line. Intent satisfied at overview level only.

**(b) Product coverage:** LiTime box: spec given ("1.28 kWh per unit, scale by stacking") ✓, who-for implicit, tradeoff = "Low-temp protection matters more in cabins than anywhere else" ✓ (good, specific). No not-for, no alternatives. Victron 100/30 box: "The 30A tier covers most weekend-cabin arrays" — sizing guidance ✓, who-for ✓, but no spec table, no not-for (e.g., not for >800W arrays at 12V — actually 30A×14.4V≈432W charging; "most weekend-cabin arrays" is doing unexamined work), no alternative (PWM for tiny budgets unmentioned).

**(c) Methodology visibility:** None. "Right-sized cabin controller" is a recommendation-flavored label with no visible selection method. T4.

**(d) Claim tiers:** Component ranges ($0.40–$1.20/W panels, $200–$900/kWh batteries, $120–$900 controllers) — T5-as-presented, no source/date. "30A tier covers most weekend-cabin arrays" — T4 editorial judgment, unflagged. "Bluetooth lets you check charging from town — the feature cabin owners actually use" — T4 presented as observed fact ("actually use" implies evidence; none exists) — this is the page's worst sentence.

**(e) Amazon compliance:** No prices/ratings in boxes ✓; shortcode disclosure ✓; `{{< affiliate-disclosure >}}` present ✓.

**(f) Overstatement/limitations/safety:** Good: "Disconnects, breakers, fuses, bus bars, and quality cable are not optional in a safe off-grid system." Winter limitation covered in FAQ. No safety-critical gap.

**(g) Scannability vs depth:** Scannable (anchor link row at top is a nice touch) but depth is the problem — 710 words vs 1,982 on the sibling page. The "cost breakdown table" is ranges only; no worked budget. Feels like a summary of solar-system-costs without the payoff.

**(h) AI-sounding passages:** "These ranges are intentionally broad. The point is to set expectations before you build a parts list." — fine. "The most expensive mistakes happen when parts are chosen before you know your daily energy use and peak load." — generic but true. Low AI-smell overall; the thinness is the issue, not the voice.

**(i) Staleness risk:** Medium — dollar ranges undated, will rot quietly.

**Box-intent fit:** SUPPORT with repositioning. Boxes sit AFTER the overspend section, before FAQ — acceptable placement, but the LiTime box would earn more inside/next to the component table (battery row) and the Victron box next to the charge-controller row. Keep both; reposition up one section.

**ACTION:** Add one worked cabin budget (mirror solar-system-costs Budget 1) + fix "the feature cabin owners actually use" (either cite or soften to "the feature most useful from town"). **PRIORITY:** Medium. **Highest-impact fix:** the worked budget — it converts the page from range-listing to breakdown, which is what the query promises.

---

## 3. inverter-keeps-shutting-off-troubleshooting.md — Inverter Keeps Shutting Off (2 boxes)
Signals: 1,786 words · 2 boxes · 0 calc · FAQ yes · 10 H2 · 5 tables · 0 internal links counted (many present) · date 2026-05-31. Traffic: 41pv/75.9% bounce.

**(a) Intent:** Excellent. Answer-first structure ("First: capture the shutdown clue"), four causes with safe checks, plus a deep "alarm-to-shutdown ladder" section with a worked voltage-drop example (12.4V rest → 10.8V at inverter, 10 AWG math shown). This is the strongest troubleshooting page in the set so far. The worked example is genuinely differentiated content.

**(b) Product coverage:** Box 1 Klein MM600 multimeter: who-for = anyone diagnosing ("Measure before you guess"), spec = "1000V-rated auto-ranging", tradeoff framing = "settles overload vs undervoltage". No not-for (a $100+ meter is overkill if you only need a $20 DC clamp reading — unmentioned), no alternatives. Box 2 iCrimp lug crimper: "A proper hex crimper for 12–2/0 AWG turns tighten-by-hope lugs into the low-resistance joints the math assumes" — good tradeoff framing, spec = die range. No not-for (if your lugs are already factory-crimped, this tool is irrelevant — the page never says "only buy this if you're making your own lugs").

**(c) Methodology visibility:** No "how we chose these tools" — but these are diagnostic tools, not ranked recommendations; labels are use-case-framed, not "best". Acceptable, though a one-line "tools we keep on the bench" framing would help.

**(d) Claim tiers:** "~11.0–11.5V on a 12V system (rule of thumb; exact setpoints vary by brand, and many are adjustable)" — properly hedged, T4/T2 hybrid, good. "commonly around 10.5V at 12V" — T4, hedged with "commonly". "10 AWG copper is ≈ 1.0 Ω per 1,000 ft" — T2-grade physics fact (NEC chapter 9 table), uncited but verifiable and standard; acceptable as engineering constant, would be T3 with a cite. "A difference of more than ~0.5V at 12V points to cabling — the same threshold our cable guide uses" — self-referential T4, fine. Overall tier hygiene is the best in the set so far.

**(e) Amazon compliance:** No prices/ratings/review text ✓; shortcode disclosure ✓; affiliate-disclosure banner ✓.

**(f) Overstatement/limitations/safety:** Very good. "Power down and disconnect the battery first", "Heat at a connection is a safety clue, not just an efficiency loss", FAQ: "If you see melted insulation, smell burning, find hot terminals, or can't safely isolate the battery/inverter circuit, stop and contact a qualified professional." This is the model the other troubleshooting pages should copy.

**(g) Scannability vs depth:** Strong. Anchor nav, cause-numbered H2s, tables for the ladder and rest-vs-load diagnosis. The alarm section is long but earns it.

**(h) AI-sounding passages:** "Voltage-drop shutdowns are usually a connection problem dressed up as a battery problem" — vivid, human. "tighten-by-hope lugs" — human. No templated passages found. One duplicate link pair: "How to choose solar system voltage" and "12V vs 24V vs 48V" both point to 12v-vs-24v-vs-48v-solar.html with different anchor text — machine-assembled link row.

**(i) Staleness risk:** Low — physics and thresholds don't rot. Best-in-set.

**Box-intent fit:** SUPPORT, both, and this page is the exemplar of "right tool at the right moment": the multimeter box appears exactly where the reader is told to measure, the crimper box exactly where voltage-drop-at-lugs is diagnosed. Neither obstructs. Keep both as-is.

**ACTION:** Add not-for lines to both boxes (MM600: "overkill if you only need occasional DC checks"; crimper: "only if you're crimping your own lugs"). **PRIORITY:** Low-Medium (page already strong; 41pv/75.9% bounce suggests readers get answers). **Highest-impact fix:** the not-for lines — they're the only rubric dimension this page fails.

---

## 4. solar-fuse-and-breaker-sizing.md — Fuse & Breaker Sizing (2 boxes)
Signals: 2,190 words · 2 boxes · 1 calc (fuse calculator) · FAQ yes · 11 H2 · 5 tables · date 2026-05-31. Traffic: 58pv/90.9% bounce.

**(a) Intent:** Strong. Circuit-by-circuit planning flow, quick reference table (wire gauge → fuse size), interactive calculator with copy/print, "sizing using labels (avoid guesswork)", DC-rated checklist, plus a "breaker keeps tripping" diagnostic subsection. Covers the query well.

**(b) Product coverage:** BougeRV MC4 inline fuse kit: who-for = DIY array builders, spec = "Waterproof IP68", tradeoff = "Match the fuse rating to your string current" ✓. No not-for (single series string usually needs NO string fuse — the calculator itself says "A single series string usually needs no string fuse" but the box sells a 5-pack of string fuses without that caveat — internal contradiction). Blue Sea busbar: spec = "Four-stud tinned-copper busbar with cover", tradeoff = "the tidy, inspectable alternative to stacked ring terminals" ✓. No not-for, no alternatives (MRBF blocks, Class-T + terminal covers unmentioned).

**(c) Methodology visibility:** No "how we picked" — but these are generic component recommendations, not ranked "best" claims. Acceptable.

**(d) Claim tiers:** "Match to panel Isc × 1.56" — T3-grade NEC-derived rule (NEC 690.8), uncited inline but standard; calculator repeats it with arithmetic shown. "max output × 1.25" — same. "At this size use a Class T fuse or MRBF — the interrupt rating matters" — T4, correct and hedged. "the cheapest insurance a DIY array can buy" — T4 marketing-ish, unflagged. Table values ("Battery → 2000W inverter (12V) | 4/0 AWG | 200–250A") — T4 planning-level, labeled "planning-level" ✓ good.

**(e) Amazon compliance:** No prices/ratings ✓; shortcode disclosure ✓; affiliate banner ✓. **DEFECT:** line 288 ends with `}}}}` — a doubled shortcode close inside the FAQ answer. If Hugo parses this as text, stray "}}" renders on the page; if it parses as shortcode, the FAQ close tag may misbehave. Needs a render check. Also the two boxes are nested INSIDE the last FAQ answer (between the answer text and `{{< /faq >}}`) — unusual placement; boxes render inside an FAQ accordion context.

**(f) Overstatement/limitations/safety:** Excellent. "the fuse protects the wire. If a fuse keeps blowing, the answer is never 'install a bigger fuse'", "Using AC-only breakers on DC: not interchangeable; DC arc behavior is different", "If a product page doesn't clearly state DC ratings, treat that as a red flag", calculator footer: "Planning-level. Follow the equipment manuals and local code; when in doubt, ask a qualified installer." Model safety hygiene.

**(g) Scannability vs depth:** Good. Calculator is a genuine utility (bounce 90.9% though — see below). Tables are tight.

**(h) AI-sounding passages:** "overcurrent protection exists to reduce the chance that a fault turns wiring into a heater" — vivid, human. No templated passages. The `}}}}` artifact is the only smell.

**(i) Staleness risk:** Low — rules of thumb are stable. NEC edition changes could touch the 1.56 factor eventually.

**Box-intent fit:** MIXED. The busbar box SUPPORTS (distribution hygiene is a real fuse/breaker-adjacent need). The BougeRV string-fuse box PARTIALLY OBSTRUCTS: the page's own calculator says a single series string usually needs no string fuse, yet the box sells a 5-pack of string fuses without that caveat — the box contradicts the page's best advice. **Recommendation: keep busbar; keep BougeRV only if the description adds "only if you run parallel strings" — otherwise soften to text link in the parallel-strings section.** Also move both boxes out of the FAQ answer body.

**ACTION:** Fix the `}}}}` artifact (verify rendered output), add parallel-string caveat to the fuse-kit box, relocate boxes out of FAQ. **PRIORITY:** Medium-High (58pv traffic, 90.9% bounce — highest-bounce sizing page in the set; a broken-looking artifact may contribute). **Highest-impact fix:** the `}}}}` render check — a visible artifact on a safety page is a trust wound.

**RENDER CHECK (verified):** Built the site with Hugo v0.141.0 to a temp destination. The `}}}}` does NOT leak into visible body HTML — but it DOES corrupt the FAQ schema: the last FAQ's JSON-LD `acceptedAnswer.text` ends with `...we may earn a commission. }}"` — a stray `}}` inside the structured data, and the two product boxes are baked into the FAQ answer text (schema now contains "Check price on Amazon Price & availability shown on Amazon.com — we may earn a commission." as answer content). This is a real schema-pollution defect: Google may show product-box boilerplate as the FAQ answer. Fix the `}}}}` and move the boxes out of the FAQ body.

---

## 5. battery-cable-size-for-inverter.md — Battery Cable Size for Inverters (1 box)
Signals: 2,343 words · 1 box · 1 calc (cable calculator) · FAQ yes · 12 H2 · 11 tables · date 2026-05-31. Traffic: 104pv/86.9% bounce — #2 page on the site.

**(a) Intent:** Excellent. Quick-reference chart (11 inverter/voltage combos), 4-step decision flow, interactive calculator with voltage-drop check against a stated 3% target, "why 24V/48V makes this easier", common mistakes, FAQ. This is the site's most-visited page and it delivers.

**(b) Product coverage:** Single box — iCrimp lug crimper (same ASIN B017S9EINA as page 3's box). Spec = "12 AWG to 2/0 battery lugs", who-for = "If you are building inverter cables, this is the tool" ✓ (explicit who-for). Tradeoff = "the difference between a connection you trust at 100A and one that heats" ✓. Not-for = absent (if you buy pre-made cables with factory-crimped lugs — the common case — this tool is unnecessary; unmentioned). Alternatives = absent (hammer-style crimpers, hydraulic tools, or simply buying pre-made cables).

**(c) Methodology visibility:** Single-tool utility pick, not a ranked list; no method needed. OK.

**(d) Claim tiers:** Chart values — T4 planning-level, explicitly labeled ("planning-level starting point", "assume an inverter efficiency of ~85%", "Always verify against the inverter manufacturer's specs and local codes") — good tier hygiene. Calculator notes: "Real current runs higher on surge and low battery; verify against the inverter manual" ✓. "copper cost drops similarly" with 4x cross-section — T3-grade physics, fine. No unflagged T2/T4 problems found.

**(e) Amazon compliance:** No prices/ratings ✓; shortcode disclosure ✓; affiliate banner ✓. **DEFECT:** the box is again nested inside the last FAQ answer (between answer text and `{{< /faq >}}`) — same pattern as page 4. Schema pollution likely (box text baked into FAQ JSON-LD).

**(f) Overstatement/limitations/safety:** Very good. "Non-DC-rated hardware: DC interrupt ratings and voltage ratings matter for safety", "Bad terminations: heat at lugs and bus bars is a symptom; fix the connection, not just the cable", calculator: "use a DC-rated fuse sized to the cable". No gaps.

**(g) Scannability vs depth:** Excellent — chart first, calculator second, steps after. Deserves its traffic.

**(h) AI-sounding passages:** "this is exactly the cable pain the 12V vs 24V vs 48V decision predicts" (calculator note) — slightly overwrought but human. "The crimp tool lugs deserve" — human. Clean.

**(i) Staleness risk:** Low.

**Box-intent fit:** SUPPORT with repositioning. The crimper is the right tool for this page's actual task (making inverter cables), but it's buried in the FAQ. It belongs at Step 4 ("Choose cable + lugs + protection as a system") where lug quality is discussed. **Recommendation: move box from FAQ to Step 4; keep as box.**

**ACTION:** Move the box to Step 4; add a not-for line ("skip it if you're using pre-made cables with factory lugs"). **PRIORITY:** Medium (highest-traffic page in the set — 104pv). **Highest-impact fix:** box placement at the moment of need + FAQ-schema cleanup.

---

## 6. battery-capacity.md — Battery Capacity Calculator (1 box)
Signals: 909 words · 1 box · 1 calc · FAQ yes · 6 H2 · 0 tables (calc result table) · date 2026-05-31, **`updated = 2026-08-09` present in front matter** — this is the ONLY page in the 24 with an `updated` param (fact-pack says zero pages set it; this one does — fact-pack needs a correction, or this was added after the Boss scan; either way the template will now show "Reviewed 2026-08-09" here).

**(a) Intent:** Good. Calculator + formula + worked example + tips + FAQ. The formula is shown explicitly with a worked example (2,000 Wh × 2 ÷ 0.90 ÷ 0.80 = 5,556 Wh). Satisfies "battery capacity calculator" intent directly.

**(b) Product coverage:** LiTime 12V 100Ah box: spec = "at 12.8V nominal, 100Ah is 1.28 kWh" ✓ (accurate: 12.8 × 100 = 1,280 Wh). Who-for = implicit ("the formula's most common real-world answer"). No not-for (a 12V 100Ah unit is NOT the answer for whole-home banks — the page's own FAQ says "Whole-home storage runs at 48V or 400V"; the box contradicts nothing but doesn't scope itself), no alternatives (server-rack 48V options, lead-acid budget path).

**(c) Methodology visibility:** Single illustrative unit, not a "best" claim. OK.

**(d) Claim tiers:** "Li-ion/LiFePO4 often supports 80–90% DoD with 4,000–6,000 cycles. Lead-acid is usually limited to 50% DoD" — T2/T4 hybrid, hedged with "often"/"usually", acceptable but uncited (manufacturer datasheets would make it T2 with names). "Cold temperatures reduce usable capacity" — T3-grade, uncited, fine. 1.28 kWh math — T3 arithmetic, verifiable. No unflagged problems.

**(e) Amazon compliance:** No prices/ratings ✓; shortcode disclosure ✓; affiliate banner ✓. Box is NOT inside FAQ here — placed after "The formula" section. Good placement.

**(f) Overstatement/limitations/safety:** Good: "Size for the coldest month if off-grid year-round", "100% (theoretical only)" DoD option labeled honestly. No safety-critical content needed here; none missing.

**(g) Scannability vs depth:** Calculator-first, formula second — right order for the query. 909 words is lean but sufficient for a calculator page.

**(h) AI-sounding passages:** "the unit that makes bank-sizing multiplication concrete" — slightly precious but human. Clean overall.

**(i) Staleness risk:** Low. Formula is timeless.

**Box-intent fit:** SUPPORT. The box lands right after the formula, converting abstract Wh into a purchasable unit — textbook "right tool at the right moment." Keep as-is. Minor: add "stack units for larger banks; for 24/48V systems use series/parallel or higher-voltage units" to the description to close the not-for gap.

**ACTION:** Add stackability/48V note to box description. **PRIORITY:** Low. **Highest-impact fix:** the not-for line — otherwise this page is the cleanest box integration in the set.

---

## 7. cpap-battery-backup-guide.md — CPAP Battery Backup (1 box)
Signals: 2,464 words · 1 box · 0 calc · FAQ yes · 12 H2 · 2 tables · 10 internal links · date 2026-08-19.

**(a) Intent:** Excellent — best-in-set candidate. One formula, label-reading instructions, worked examples both with/without humidifier, nights-per-battery table, outage playbook, airline rules, honest power-station math ("treat any quoted runtime with no visible Wh-and-watts arithmetic as an ad"). Repeatedly refuses medical claims: "we are not giving medical advice", "Any question about your treatment goes to your prescriber, not a battery guide."

**(b) Product coverage:** LiTime 12V 100Ah box: spec = "1,280Wh of usable-capacity chemistry (100Ah at 12.8V, 80-100% DoD)" — spec accurate (12.8×100=1,280Wh nameplate; "usable-capacity" phrasing slightly overstates since 80% DoD gives ~1,024Wh usable — minor). Who-for = CPAP users + "doubles as the cabin/RV bank the rest of the year" ✓. Tradeoff = "Pair with a 12V DC cable for your machine to skip inverter losses" ✓. Not-for = absent (flyers — the page's own travel section says a 100Ah unit "can't fly"; the box doesn't say it). Alternatives = power stations discussed extensively in body but not in box.

**(c) Methodology visibility:** Single pick framed by the page's own math ("at 40-60Wh per CPAP night that is over a week of runtime") — the box's claim is derived from the page's formula, which is visible methodology. Good.

**(d) Claim tiers:** "30–60W while running" / "heated humidifier can roughly double that" — T4 hedged ("typically", "roughly"), acceptable. TSA/FAA rules: "Up to 100Wh: generally allowed in carry-on... 101–160Wh: need airline approval... Over 160Wh: forbidden" — T3 with source comment in file ("Sources verified 2026-09-05: TSA 'Power Banks'...") — the ONLY page in the set with an inline source-verification comment. "Below about 0°C, lithium capacity drops roughly 20%" — T4, hedged, uncited. "26,800mAh USB-C power bank works out to ~99.2Wh (26.8Ah × 3.7V)" — T3 arithmetic, shown. Tier hygiene: strong.

**(e) Amazon compliance:** No prices/ratings/review text ✓; shortcode disclosure ✓; affiliate banner ✓. Box placed after safety section, before power-station math — reasonable.

**(f) Overstatement/limitations/safety:** Excellent. "Use manufacturer-approved DC cables... Third-party cables can be electrically incompatible", "Avoid cheap modified-sine inverters on sensitive electronics", "Don't touch pressure settings or firmware", "keep battery terminals protected (tape or a case) so they can't short out", "the TSA officer has the final word". Medical boundary maintained throughout. Model page.

**(g) Scannability vs depth:** Strong. Quick answer up top, hero table, playbook numbered list, two tables. 2,464 words but every section earns its place.

**(h) AI-sounding passages:** "so an outage is a plan, not a panic" — human. "That rehearsal is worth more than any table" — human. **DEFECT (non-editorial but real):** an "## Image Prompts" section with three AI-image-generation prompts sits at the very bottom of the published markdown — internal production notes leaked into content. If rendered, this is visible junk; even if Hugo renders it, it's in the source and possibly in the page. Must check render.

**(i) Staleness risk:** Medium — TSA/airline rules flagged as changeable with source date ✓; watt ranges stable.

**Box-intent fit:** SUPPORT. The box lands after the safety notes, right where a reader who's absorbed the math is ready to pick a bank. Keep. Add "not flyable — see travel section" to the description to close the not-for gap.

**ACTION:** Delete the leaked "## Image Prompts" section (verify it doesn't render); add not-flyable note to box. **PRIORITY:** Medium-High (leaked production notes on a published page is a professionalism defect regardless of render). **Highest-impact fix:** remove Image Prompts.

**RENDER CHECK (verified):** The Image Prompts section DOES render — `<h2 id="image-prompts">Image Prompts</h2>` plus the three full AI-image prompts appear in the built HTML, AND it's added to the TOC rail as a nav item. This is user-visible leaked production scaffolding on a published page. Highest-priority cleanup in the set so far.

---

## 8. how-much-do-solar-batteries-cost.md — How Much Do Solar Batteries Cost (1 box)
Signals: 1,113 words · 1 box · 0 calc · **0 FAQ** · 7 H2 · 0 tables · 3 internal links · date 2026-05-31.

**(a) Intent:** WEAK — this is the worst page in the set so far. The query is "how much do solar batteries cost" and the page answers in vague bands with zero worked examples, zero tables, zero per-brand reality. Compare solar-system-costs (worked line-item budgets) and solar-battery-cost-2026 (3,666 words) — this page is a thin middle child. **CRITICAL STALENESS DEFECT:** the ITC section says "the Federal Investment Tax Credit (ITC) allows homeowners to deduct a significant portion of their solar battery system costs from their federal taxes" — the 30% residential ITC expired Dec 31 2025 (sitewide purge was supposedly done; this page was MISSED). This is now factually wrong on a money page.

**(b) Product coverage:** LiTime box: no spec (no kWh/Ah stated), who-for implicit ("DIY alternative"), tradeoff = "value benchmark" framing. No not-for, no alternatives. Weakest box description of the LiTime boxes seen so far.

**(c) Methodology visibility:** None. "the value benchmark for what a kWh of storage should cost" — superlative with no method.

**(d) Claim tiers:** "$800 to $1,500 per kWh before installation" (Li-ion), "$200 and $400 per kWh" (lead-acid), "5kWh Systems: $4,000 to $7,500", "10kWh: $8,000 and $15,000" — ALL T5-as-presented: no source, no date, no hedge. Note internal inconsistency: solar-system-costs says DIY components run $200–$900/kWh and installed $1,000–$1,400/kWh; this page says $800–$1,500/kWh "before installation" — the two pages' ranges don't reconcile. "Professional installation is non-negotiable" — T4 stated as absolute; contradicts the site's own DIY-first positioning elsewhere.

**(e) Amazon compliance:** No prices/ratings ✓; shortcode disclosure ✓; affiliate banner ✓.

**(f) Overstatement/limitations/safety:** "Professional installation is non-negotiable for ensuring safety" — overstatement that also contradicts the site's DIY content cluster. No safety content needed beyond that; nothing hazardous missing.

**(g) Scannability vs depth:** Bullet-list pricing, no tables, no calculator link, no FAQ. Thinnest money page in the set.

**(h) AI-sounding passages:** SEVERE — this page reads as unedited AI output. Evidence: escaped heading artifact `\# How Much Do Solar Batteries Cost? A Comprehensive Guide to TCO and ROI` rendered as literal text right under the H1 (markdown escape leaked); title-case "A Comprehensive Guide to TCO and ROI"; "As homeowners increasingly seek energy independence, solar power has become a cornerstone of modern sustainability" — classic AI opener; "This guide demystifies the expenses"; "transform a complex technical decision into a clear financial strategy"; "When determining how much do solar batteries cost, you must distinguish..." (grammatically awkward interrogative-as-noun repeated twice); "Total Cost of-Ownership" (hyphen typo). Multiple AI-voice markers in one page.

**(i) Staleness risk:** CRITICAL — ITC claim is already wrong (post-Dec 2025 expiry), and the page shows no updated date.

**Box-intent fit:** OBSTRUCTS (mildly). The box sells a DIY component battery on a page that just told readers professional installation is "non-negotiable" — the page undercuts its own box. **Recommendation: keep box only after fixing the DIY/installed framing; the box itself is fine once the page stops contradicting it.**

**ACTION:** (1) Fix the ITC-expired error immediately — this is a live factual error on a money page; (2) rewrite the AI-voice passages; (3) remove the `\#` artifact; (4) reconcile $/kWh ranges with solar-system-costs; (5) add FAQ + a worked TCO example. **PRIORITY:** HIGH — the only page so far with a live factual error. **Highest-impact fix:** the ITC correction.

---

## 9. how-much-do-solar-panels-cost.md — How Much Do Solar Panels Cost (1 box)
Signals: 1,492 words · 1 box · 0 calc · 0 FAQ schema (H3-style FAQ present) · 6 H2 · 3 tables · date 2026-05-31.

**(a) Intent:** Good. Key takeaways with $/W and system totals, cost breakdown by hardware/labor/soft costs, quote factors, financing comparison table, FAQ. Satisfies the query. **But see (d)/(i): the FAQ contains a live factual error.**

**(b) Product coverage:** Renogy 100W box: same ASIN as solar-system-costs box, different description. Spec = "$1/Watt panel" (price-adjacent but no actual price stated — compliant). Who-for = DIY/benchmark shoppers. Tradeoff = "shows exactly what the labor and overhead line items cost you" ✓. No not-for, no alternatives.

**(c) Methodology visibility:** "The panel most cost tables are built around" — implies site-wide methodology, not shown. T4.

**(d) Claim tiers:** "$2.50 and $3.50 per watt (installed)" — T5-as-presented (no source/date; consistent with solar-system-costs at least). "7kW to 10kW system generally costs between $18,000 and $30,000 installed in 2026" — T5. "Payback... 6 to 10 years" — T5, and INCONSISTENT with solar-system-costs which says "the realistic national band is 10–14 years" post-ITC. Two pages, two payback ranges — one of them is wrong; the post-ITC math favors 10–14. **LIVE ERROR:** FAQ answer "Does the 30% Federal Tax Credit apply to the whole cost?" begins "Yes, the Federal Investment Tax Credit (ITC) applies to the total cost..." — answered in present tense as if the credit still exists, directly contradicting the page's own Key Takeaways ("No federal credit in 2026: The 30% ITC expired December 31, 2025"). The ITC purge missed this FAQ. "Zillow... increase home resale value by approximately 4%" — T3-grade claim with source named but no date/link; acceptable but should link the study.

**(e) Amazon compliance:** No prices/ratings ✓; shortcode disclosure ✓; affiliate banner ✓.

**(f) Overstatement/limitations/safety:** Roof-replacement-before-solar advice is good and honest. Lease/PPA section is balanced ("you never received the federal tax credit under this structure" — tense is off but the point stands). No safety gaps.

**(g) Scannability vs depth:** Good structure; financing table is useful. Some typos: "as or much as $1.00", "This includes-", "Many-specialized solar loans", "no-upfront-cost" quote marks scattered — signs of hasty edit/merge.

**(h) AI-sounding passages:** Opener "Understanding the cost of solar energy is the most critical step in determining whether a transition to renewable energy is financially viable for your household" — AI-flavored (also truncated in the meta description with "..."). "The 'price per watt' is the industry standard for comparing quotes" — fine. Moderate AI-smell in opener; body is more concrete.

**(i) Staleness risk:** HIGH — ITC FAQ error is live NOW; payback range conflicts with sibling page.

**Box-intent fit:** SUPPORT. The box lands after the financing sections, framing DIY panel cost against installer quotes — consistent with the page's $/W theme. Keep.

**ACTION:** (1) Rewrite the ITC FAQ answer to state the credit expired Dec 31 2025 (2025 installs can still claim); (2) reconcile payback range with solar-system-costs (10–14 years post-ITC); (3) fix typos; (4) date/link the Zillow claim. **PRIORITY:** HIGH — second live ITC error in the set. **Highest-impact fix:** the ITC FAQ answer.

---

## 10. mppt-charge-controller-cost.md — MPPT Charge Controller Cost (1 box)
Signals: 718 words · 1 box · 0 calc · FAQ yes · 7 H2 · 0 tables counted (2 real) · date 2026-05-31.

**(a) Intent:** Adequate. Price-band table (3 classes), MPPT-vs-PWM comparison, cost drivers, wrong-size checks, FAQ. 718 words is thin for a cost query but the bands + checks cover the core. No worked budget example (e.g., "a 400W cabin array needs a 30A class controller ≈ $X").

**(b) Product coverage:** Victron 100/30 box: spec = "Bluetooth monitoring and lithium presets" ✓, who-for = implicit mid-tier, tradeoff = "where the diminishing-returns curve flattens" ✓ (nice framing). No not-for (small PWM-suitable systems unmentioned in box), no alternatives (Renogy/EPEver budget tier absent — the page links best-mppt-charge-controllers but the box doesn't).

**(c) Methodology visibility:** "The controller every MPPT cost table benchmarks against" — claims site-wide benchmark status; no visible method. T4. Same pattern as the LiTime "benchmark" boxes — a house style that asserts authority without showing it.

**(d) Claim tiers:** "$120–$250 / $250–$600 / $600–$1,200+" — T5-as-presented, no source/date. "MPPT controllers... often improve harvest in mixed conditions" — T4 hedged ✓. "a controller at the edge of specs can trip or run hot" — T4, reasonable. No severe problems.

**(e) Amazon compliance:** No prices/ratings ✓; shortcode disclosure ✓; affiliate banner ✓.

**(f) Overstatement/limitations/safety:** "Add headroom for safety and real-world conditions" ✓; "a controller at the edge of specs can trip or run hot" ✓. Adequate.

**(g) Scannability vs depth:** Scannable; thin. The two tables carry most of the value.

**(h) AI-sounding passages:** "MPPT controllers often land in a broad band depending on voltage class, current rating, and features" — vague-but-harmless. Low AI-smell. Duplicate link pair again (12V vs 24V vs 48V linked twice with different anchors).

**(i) Staleness risk:** Medium — price bands undated.

**Box-intent fit:** SUPPORT. Box after "common mistakes", before FAQ — reasonable position; the reader has just been told what specs matter, and the box shows a concrete mid-tier unit. Keep. Add a not-for ("if your array is a single 12V panel, PWM may serve you cheaper") to align with the page's own MPPT-vs-PWM table.

**ACTION:** Add PWM-not-for line to box; date the price bands; add one worked sizing→price example. **PRIORITY:** Low-Medium. **Highest-impact fix:** the worked example — it's what separates a cost page from a range list.

---

## 11. mppt-charge-controller-not-charging.md — MPPT Not Charging (1 box)
Signals: 3,031 words · 1 box · 0 calc · FAQ yes · 14 H2 · 10 tables · 9 caveat hits · date 2026-05-31. Traffic: 60pv/87.1% bounce.

**(a) Intent:** Excellent — the deepest troubleshooting page in the set. Ordered diagnostic flowchart, expected-voltage table with red-flag column, 5 steps each with "Most common cause" + "Check", seasonal patterns table, replace-vs-repair section, 4-branch "no output" decision tree. "90% of 'my MPPT isn't charging' cases are solved by steps 1–3" — concrete, falsifiable framing.

**(b) Product coverage:** Klein MM600 box (same ASIN as page 3): spec = "auto-ranging 1000V meter", who-for = anyone at step one. Tradeoff = implicit. No not-for, no alternatives (a $25 DC-only meter would answer most of this page's checks — unmentioned).

**(c) Methodology visibility:** Single diagnostic tool, use-case framed. OK.

**(d) Claim tiers:** "A panel shaded by just 10% can lose 50–80% of its output" — T3-grade shading fact, uncited (would be T3 with a source; as-is T4). "Panel Voc rises as temperature drops. A panel rated at 46V Voc at STC can hit 55V+ at -10°C" — T3 arithmetic with stated coefficient (-0.3%/°C), verifiable, good. "Lithium needs 14.2–14.6V bulk/absorb and 13.5–13.6V float; lead-acid needs 14.4–14.8V bulk" — T2/T4, presented as flat fact; ranges vary by brand — should carry "check your battery's spec sheet" (the page does say "verify the battery type matches your actual battery" but not "check manufacturer voltage specs"). "panels lose ~0.4%/°C above 25°C" — T2-grade typical coefficient, hedged with "~", acceptable. "90% of cases" — T4 editorial judgment presented as a statistic; harmless but technically unsourced.

**(e) Amazon compliance:** No prices/ratings ✓; shortcode disclosure ✓; affiliate banner ✓. **DEFECT:** box again nested inside the last FAQ answer (same pattern as pages 4/5) — schema pollution risk.

**(f) Overstatement/limitations/safety:** Excellent. "This is correct behavior — the battery is protecting itself", "If you can't verify PV voltage/current within safe procedures... stop and contact a qualified professional", cold-weather Voc warning with 10% margin rule. Model safety hygiene.

**(g) Scannability vs depth:** Excellent — flowchart first, tables throughout, branch logic. 3,031 words justified.

**(h) AI-sounding passages:** "Knowing these saves you hours of troubleshooting" — mild. "Most 'broken controller' diagnoses are wrong" — punchy, human. Clean.

**(i) Staleness risk:** Low — physics and behavior patterns.

**Box-intent fit:** SUPPORT with repositioning. The multimeter is exactly the right tool for this page (steps 2–3 require Voc measurement), but it's buried in the FAQ. It belongs at Step 2 ("Confirm PV voltage is high enough") where the "Quick test: measure open-circuit voltage" instruction lives. **Recommendation: move box from FAQ to Step 2; keep as box.**

**ACTION:** Move box to Step 2; add budget-meter alternative line ("a basic DC-capable multimeter covers most of these checks"); fix FAQ nesting. **PRIORITY:** Medium (60pv traffic). **Highest-impact fix:** box placement at the measurement moment.

---

## 12. portable-solar-panels.md — Portable Solar Panels Guide (1 box)
Signals: 926 words · 1 box · 0 calc · **0 FAQ** · 3 H2 · 0 tables · 0 internal links · date 2026-05-31.

**(a) Intent:** PARTIAL. Covers cell technologies, form factors, sizing math with a worked example, cost tiers. But the page ENDS abruptly after the product box — no FAQ, no "next reads", no summary. The file is 105 lines and simply stops. A "portable solar panels guide" that ends mid-thought feels unfinished. Also: no internal links at all (0 counted) — orphaned from the cluster.

**(b) Product coverage:** Renogy 100W box: spec = "monocrystalline cells, IP67 weather rating" ✓, who-for = "every RV build" (narrow — the page is broader than RV), tradeoff = "compatibility footprint... every RV build already assumes". No not-for, no alternatives (the page's own 3-tier pricing lists Goal Zero/Jackery premium and generic budget — box ignores both).

**(c) Methodology visibility:** "Solid mid-range pick" — no method. T4.

**(d) Claim tiers:** "Monocrystalline... 20% to 23%" / "Polycrystalline... 15% and 17%" / "Thin-film... often below 12%" — T2/T3-grade typical specs, uncited, presented as flat fact. "generally 10-15% more expensive" — T4. "3.5 to 4 usable sun hours" — T4 planning assumption, reasonable. "20-30% loss in the charging process" — T4, hedged. "$3-$5 / $6-$10 / $12+ per watt" — T5-as-presented, no date. **TYPO/FACT:** "Bougevert" — misspelled brand (should be BougeRV); a brand misspelling on a buyer page is an E-E-A-T wound.

**(e) Amazon compliance:** No prices/ratings ✓; shortcode disclosure ✓; affiliate banner ✓.

**(f) Overstatement/limitations/safety:** "a 100W panel will fail you" — overstated for lighter loads (the page's own phone/laptop-only example would be fine on 100W; the 575Wh example includes a fridge). Slightly overbroad. No safety content needed; none missing.

**(g) Scannability vs depth:** Decent structure (tech → form factor → sizing → cost) but the abrupt ending and 0 FAQ hurt. LaTeX `$$...$$` formulas — Hugo's default markdown renderer does NOT render LaTeX; these likely display as raw `$$\text{...}$$` code on the page. Needs render check.

**(h) AI-sounding passages:** "In an era of increasing outdoor adventure and a growing need for energy independence during power outages, portable solar panels have transitioned from niche camping gear to essential utility tools" — textbook AI opener (also truncated in meta description). "Understanding the distinction is critical for calculating your energy harvest" — AI-ish. Moderate-high AI-smell.

**(i) Staleness risk:** Medium — price tiers undated; brand mentions rot.

**Box-intent fit:** SUPPORT (placement is good — right after the cost tiers, where a mid-range pick is contextually apt) but the page's abrupt ending makes the box feel like the page exists to host it. **Recommendation: keep box; add FAQ + closing section after it so the page doesn't end on a sales unit.**

**ACTION:** (1) Fix "Bougevert" → BougeRV; (2) verify LaTeX rendering (likely raw `$$` visible); (3) add FAQ + next-reads; (4) rewrite AI opener; (5) add internal links to the cluster. **PRIORITY:** Medium-High. **Highest-impact fix:** the LaTeX render check — raw formula code on the page would be the worst visible artifact in the set.

**RENDER CHECK (verified):** The LaTeX formulas DO render as raw code — `$$\text{Required Panel Wattage} = \frac{\text{Daily Wh Require...` appears verbatim in the built HTML, with no KaTeX/MathJax loaded (0 hits). Users see broken formula markup mid-page. Combined with the "Bougevert" misspelling (also confirmed in built HTML), this page has two visible defects. The abrupt ending is confirmed: the built page ends at the product box with no FAQ/next-reads.

---

## 13. rv-solar-cost.md — RV Solar Cost Breakdown (1 box)
Signals: 1,303 words · 1 box · 0 calc · **0 FAQ** · 8 H2 · 19 tables · 0 internal links counted (many present) · date 2026-05-31. Traffic: 33pv/58.6% bounce (low bounce for the set).

**(a) Intent:** Excellent. Three complete worked builds (budget/mid/high) with per-component costs and "what it runs", DIY-vs-pro table, category breakdown, usage-pattern quick-reference table, hidden-costs section. The best cost page in the set alongside solar-system-costs. Low bounce (58.6%) corroborates.

**(b) Product coverage:** Victron BMV-712 box: spec = "Exact state-of-charge at a glance" (function, not spec — no measurement precision/Bluetooth mention), who-for = implicit, tradeoff = "The component most often skipped and most often regretted" ✓ (T4, unflagged but plausible). No not-for (a shunt monitor is unnecessary on tiny budget builds with a $30 voltmeter — unmentioned), no alternatives (Victron SmartShunt, cheap DC meters).

**(c) Methodology visibility:** "Worth-it upgrade" — no method. T4. Mild.

**(d) Claim tiers:** "Prices reflect 2026 retail from major solar retailers (Renogy, Rich Solar, Battle Born, Victron, etc.)" — explicit sourcing statement ✓ (rare in this set; T2-grade with date). "Professional installation adds $500–$2,000+" vs later table "$1,000–$3,000+" — internal inconsistency (two different pro-install ranges on one page). "Most RV owners go DIY" — T4, unsourced. "Add 1W of solar for every 1Ah of lithium battery capacity" — T4 rule of thumb, hedged as "rule of thumb" ✓. "A mistake on a high-power system can cause fires" — T4 safety, fine.

**(e) Amazon compliance:** No prices/ratings ✓; shortcode disclosure ✓; affiliate banner ✓. Box at page end after hidden costs — fine placement.

**(f) Overstatement/limitations/safety:** Very good. "Don't cheap out on undersized wire — it's a fire risk", "When to hire a pro" section with concrete triggers (3000W+, transfer switch, 48V), insurance disclosure note. Model.

**(g) Scannability vs depth:** Excellent — tables carry the page; each build has a "what it runs" line. 0 FAQ is the only structural gap.

**(h) AI-sounding passages:** "You can't manage what you can't measure" — cliché but earned. "essentially grid-quality off-grid living" — fine. Low AI-smell.

**(i) Staleness risk:** Medium — "Prices reflect 2026 retail" is dated ✓ but will need annual refresh.

**Box-intent fit:** SUPPORT. The BMV-712 box lands exactly in the hidden-costs section that names it ("Battery monitor and shunt ($150–$200)") — the box is the productized version of the page's own advice. Textbook fit. Keep as-is.

**ACTION:** Reconcile the two pro-install ranges ($500–$2,000 vs $1,000–$3,000); add FAQ; add not-for line to box ("overkill for weekend builds — a $30 voltmeter covers the basics"). **PRIORITY:** Low-Medium. **Highest-impact fix:** the internal price-range consistency fix.

---

## 14. solar-battery-cost-2026.md — Solar Battery Cost 2026 (1 box)
Signals: 3,746 words · 1 box · 6 FAQs + faq-schema · 20 H2/H3 · date 2026-05-31 · **no `updated`** · **1 internal link in entire body** · canonical twin at /guides/solar-battery-cost-2026/.

**(a) Intent:** Broadly strong (averages, per-kWh, 5-model comparison table, incentives, hidden fees, DIY-vs-pro, FAQ) with one money-question gap: **"## Calculating ROI and Payback Period" never states a payback figure** — only TOU-arbitrage savings ("$480 to $960" annual, "$5,000–$10,000" over 10 years) and a "peace of mind" premium. The section title promises payback; the reader never gets a number.

**(b) Product coverage / box:** The page analyzes grid-scale home batteries (Powerwall 3, Enphase IQ 5P, FranklinWH aPower2, Sonnen Eco, LG Chem RESU 15H). **The box sells a LiTime 12V 100Ah LiFePO4 (B084DB36KW, 1.28 kWh DIY battery)** — a product absent from the page's own comparison table, placed immediately after "When to Hire a Pro," which states "You should always hire a professional for battery installation" and "DIY installation generally inadvisable for the average homeowner." Box label: "Best cost-per-kWh in the 2026 field… defines the budget tier of every 2026 battery cost comparison." No not-for, no alternatives, no reconciliation with the anti-DIY advice two paragraphs earlier.

**(c) Methodology:** None visible for "Best cost-per-kWh in the 2026 field" or "defines the budget tier of every 2026 battery cost comparison" — the latter asserts site-wide comparative authority no page shows. T4-as-presented, unflagged.

**(d) Claim tiers — CNTEpower verdict (Boss question):** "A 2026 report from CNTEpower notes that for a typical 10 kWh system, the installed cost ranges from **$10,000 to $14,000** before incentives." **CNTEpower is a battery-component vendor's content-marketing blog, not independent market research — this is a T2-grade (manufacturer-stated) source dressed in T3 clothing ("a 2026 report… notes"), used circularly to "confirm" the page's own $1,000–$1,400/kWh anchor.** Not reputable enough to carry a money-page cost claim unqualified. Same problem, milder: NRG Clean Power (an installer, $8,000–$11,000) and Beny.com (component vendor, $10,000–$20,000) — commercial sources, none linked or dated inline. EnergySage ("approximately $15,228 before incentives" for Powerwall 3) is genuinely reputable (T3-grade) but the oddly precise figure needs a dated link. ITC section is **CORRECT and consistent** ("the 30% federal credit (Section 25D) ended for expenditures after December 31, 2025 under the One Big Beautiful Bill Act" — intro, dedicated section, and 2 FAQs all agree): this page got the ITC purge its two sibling cost pages missed. "TOU arbitrage can save 20% to 40%" — T5-as-presented.

**(e) Amazon compliance:** No prices/ratings/review text in box ✓; disclosure shortcode present ✓; standard button ✓.

**(f) Overstatement/safety:** DIY section is genuinely strong (400V DC, thermal runaway, warranty-void, insurance-invalidation) — which is exactly what makes the box contradiction a real defect, not a nitpick.

**(g) Scannability/structure defects:** Same chart image (`solar-battery-cost-chart-2026.jpg`) embedded **twice** (Price Trends + after Budget-Friendly Alternatives) — assembly error. **Zero body internal links**; the only link is machine-glued onto the end of the last FAQ answer: "…throughout its lifespan. - <a href=\"/pages/best-solar-batteries-2026.html\" class=\"text-link\">Best solar batteries 2026 comparison</a>" — same defect family as the fuse page's FAQ-schema pollution. A 3,746-word flagship orphan.

**(h) AI-voice:** "The market for home energy storage has matured rapidly, shifting from a luxury add-on to a critical component of modern home energy management"; "not just a luxury; it is a necessity"; "Smart batteries in 2026 often come with AI-driven software." Moderate-to-high AI-smell — worse than the audited engineering pages.

**(i) Staleness:** HIGH — "2026" title clock, every figure year-stamped, no `updated`, CNTEpower "2026 report" undated. **Twin handling verdict: directionally correct** — /guides/solar-battery-cost-2026/_index.md is a near-exact body copy carrying `canonical = "https://solarpoweredproject.com/pages/solar-battery-cost-2026.html"`, so **the /pages/ version is canonical and correctly carries the full content, box, and FAQ schema**. Residual risks: the twin remains a full-body duplicate (crawlable if canonical is ignored) and a sync hazard — any CNTEpower fix must be applied to **both** copies (verified currently identical). Recommend stub-or-301 the twin long-term.

**Box-intent fit: OBSTRUCTS (mixed).** A DIY 12V battery sold directly under "always hire a professional" is premature selling plus internal contradiction. **Fix:** move the box into a clearly-labeled off-grid/DIY-budget aside with a bridging caveat ("why budget 12V batteries exist despite the warranty/insurance tradeoffs above"), or soften to a text link; add not-for ("grid-tied home backup — see the pro-installed models above").

**ACTION:** Replace/relabel the CNTEpower citation (EnergySage/Wood Mackenzie/NREL-style source, or "editorial estimate, checked {month}"); resolve box contradiction; add an actual payback number or retitle the ROI section; dedupe the chart image; move the FAQ-glued link into the body; add internal links; add `updated` (both copies). **PRIORITY: High** (canonical flagship money page, live vendor-sourced cost claim, zero internal links). **Highest-impact fix:** the CNTEpower replacement + box contradiction.

---

---

## 3. Final cluster synthesis (24 pages: 14 fully audited, 10 signals-based)

**Pattern strengths (evidence-backed across the 14 audited):** (1) Engineering pages carry real worked math — voltage-drop proof, capacity formula, three costed RV builds — with honest "planning-level" disclaimers and a consistent safety ladder ("stop and contact a qualified professional" triggers). (2) Amazon compliance is clean everywhere audited: no prices/ratings/review text, shortcode disclosure on every page. (3) Where boxes land at the reader's need-moment (battery-capacity, inverter-shutoff, rv-solar-cost), the fit is textbook. (4) Two pages prove the house can source claims (cpap's dated TSA check; rv-solar-cost's "Prices reflect 2026 retail from major solar retailers"). (5) The ITC purge was applied correctly on solar-system-costs and solar-battery-cost-2026.

**Pattern defects:** (1) **The ITC purge missed two money pages** (how-much-do-solar-batteries-cost, how-much-do-solar-panels-cost) — live factual errors. (2) **Claim-tier invisibility is the set-wide disease**: ~12/14 audited pages present costs with no source/date/hedge; solar-battery-cost-2026 shows the failure mode at its worst — vendor blogs (CNTEpower, Beny) and installers (NRG Clean Power) cited as if independent research. (3) **Box-vs-body contradictions** where the page's own advice contradicts the box (fuse-sizing string-fuse; solar-battery-cost-2026 DIY battery under "always hire a pro"). (4) **Machine-assembly artifacts**: FAQ-glued links/schema pollution, duplicated chart image, box-in-faq-shortcode pattern (3 pages), duplicated link rows, 0-internal-link orphans including the 3,746-word flagship. (5) Thin middle tier (607–828w cost pages) vs. a 3,746w flagship — depth is uncorrelated with importance. (6) AI-voice concentrates on "how-much-do" pages and the 2026 flagship. (7) No `updated` front matter except battery-capacity (2026-08-09) on any audited page.

**3 WORST:** 1) **how-much-do-solar-batteries-cost** — live ITC error, severe AI voice, leaked artifacts, contradicts its own box. 2) **portable-solar-panels** — two verified visible render defects (raw LaTeX, "Bougevert" misspelling), page structurally exists to host the sale, 0 internal links. 3) **how-much-do-solar-panels-cost** — live ITC FAQ self-contradiction + payback inconsistency + typo cluster. *(Newly promoted contender just missing the cut: solar-battery-cost-2026 — vendor-sourced flagship cost claim + box contradiction + zero internal links; it lacks only the verified live factual error the three above have.)*

**3 BEST:** 1) **cpap-battery-backup-guide** — formula-first math, maintained medical boundary, sourced-and-dated TSA rules, model safety section. 2) **inverter-keeps-shutting-off-troubleshooting** — worked voltage-drop proof, best tier hygiene, boxes at exact-need moments. 3) **rv-solar-cost** — explicit retail sourcing statement, three costed builds, lowest bounce in set (58.6%).

---

---

*(Sections 15-24 below are Boss-authored after two seat budget failures on this scope; same rubric, compact form. The fridge page adapts seat A's full verdict from ca-buyer-core §13.)*

## 15. rv-solar-sizing.md — How to Size an RV Solar System (686w body, 1 box)
Intent 3/5 — right 4-step skeleton (Wh/day → battery → panels → inverter) with scenario ranges, but thin for the topic's complexity; no worked wiring/fusing note; matrix row 33 already targets the expectation-math expansion. Box (Renogy 200W kit) fits intent at the entry tier. Claims: scenario ranges T4 hedged; no attribution language; no safety caveats on inverter sizing current (12V@2000W ≈ 170A+) — the set's zero-caveat anomaly. **ACTION: expand (row 33) · P2 · fix: add 12V current-draw reality check + surge note + one caveat line.**

## 16. solar-battery-cost-per-kwh.md — Solar Battery Cost Per kWh (607w, 1 box)
Intent 4/5 — genuinely useful method page: "cost per usable kWh (not nameplate)" + lifetime-usable-kWh comparison matches the site's house method (li-ion-vs-lead-acid). Thin (607w): "$200–$900 per kWh" T4 band with no source/date/derivation; no worked $/lifetime example with real numbers spelled out beyond the method. Box (LiTime "The $/kWh reference point… the battery we benchmark cost-per-kWh against") — coherent, method-tied framing. **ACTION: expand · P3 · fix: one dated source or "editorial band, checked 2026-09" line + a fully worked $/usable-kWh-×-cycles example.**

## 17. solar-battery-management-system-explained.md — BMS Explained (1,519w, 1 box, date 2026-08-10)
Intent 5/5 — Gen-2: what a BMS does, lithium-requires-BMS safety framing, types, when needed; box (BMS parts/balancer class) fits the page's "when you need one" moment. Claims hedged appropriately ("can catch fire" is correct T3). FAQ via shortcode (schema present). **ACTION: keep · P4 · fix: add "per manufacturer spec" to the box line and one not-for (integrated-BMS batteries don't need an add-on).**

## 18. solar-inverter-cost.md — Solar Inverter Cost (828w, 1 box)
Intent 4/5 — honest type-by-type cost drivers, "common mistakes that increase cost," replacement-cost budgeting (rare, good). Thin-middle-tier: all cost bands T4 with no date/source ("price is often driven by power rating"); box (Renogy 2000W "Mid-size cost anchor") coherent with the page's mid-size framing. **ACTION: expand · P3 · fix: date the bands ("2026 street-price bands, checked Sept 2026") and add one sentence on when cheap inverters cost more (surge margin, idle draw).**

## 19. solar-inverter-sizing.md — Inverter Sizing (2,015w, 1 box, calc, updated=2026-08-15)
Intent 5/5 — the set's model page: calculator + 4 steps + surge treatment + battery-side current check + worked cabin example; box framed conditionally ("When the math says 2000W… If your load list lands in the 1500-2…") — the correct conditional-box pattern the rest of the set should copy. Sets `updated` (one of 7). **ACTION: keep · P4 · fix: add NOT-for line to box (grid-tied whole-home — different page) and cross-link inverter-cable-size-chart in Step 3.**

## 20. solar-lights-for-yard.md — Solar Lights for Yard (1,441w, 1 box)
Intent 4/5 — type taxonomy, spec-sheet guidance (lumens/IP/battery chemistry), maintenance, integrated-vs-remote comparison table. Defects: FAQ is H3 markdown (no faq shortcode → no schema — deviates from 103-page site pattern); "$25–$60 per unit for quality" T4 band undated; box (SOLPEX 16-pack) fits the pathway-light intent. **ACTION: update · P3 · fix: convert FAQ to shortcode (schema) and date the cost band.**

## 21. solar-panel-output.md — Solar Panel Output (1,610w, 1 box, calc, updated=2026-08-09)
Intent 5/5 — calculator + formula + efficiency-factor table + seasonal 30-50% honesty + "what can this actually power"; box is the set's BEST intent fit (Klein multimeter, "Estimated output is theory; a meter is truth" — a measurement tool, not the thing being sized: sells nothing the page pushes). **ACTION: keep · P4 · fix: none required; optional attribution line on the efficiency-factor table (derate conventions).**

## 22. solar-panels-for-sheds.md — Solar for Sheds (1,543w, 1 box)
Intent 4/5 — Gen-2 rebuild: load audit → architectures (off-grid/grid-tied/hybrid) → components → 300W budget example; Renogy kit box ("The 100W shed baseline") fits. Matrix row 16 already targets the decision-math refresh (1pv/100% bounce was pre-rebuild). Claims: budget breakdown T4 hedged; permit FAQ answer appropriately local ("check your AHJ"). **ACTION: update (row 16 depth pass) · P3 · fix: add who-should-not-DIY note in wiring section + one per-product caveat on the kit (PWM controller limit for expansion).**

## 23. solar-phone-charger.md — Solar Phone Charger (1,464w, 1 box)
Intent 4/5 — type architecture (power bank vs foldable), spec-sheet literacy (mA at USB vs panel watts), environment/durability; box (Nekteck 28W "travel-tier workhorse") fits. Defects: no worked "charge a 5,000mAh phone from X" math with derate (the site's signature move); FAQ H3s (no schema? — verify); "Slow Charging" FAQ is genuinely useful. **ACTION: update · P3 · fix: add one worked charge-time example (5,000mAh ÷ (panel A × 0.7)) + faq shortcode.**

## 24. what-size-solar-generator-run-refrigerator.md — Fridge Sizing (1,945w, 1 box, date 2026-08-19)
Per seat A's full verdict (ca-buyer-core §13): intent 5/5, best answer-first execution, every worked number independently recomputed correct, "Buying checklist (no brands bought here — specs you verify)" is the fairest methodology statement on site; box (Jackery 1000 v2) carries "per manufacturer spec." Image-Prompts scaffolding leak found by seat A was REMOVED by Boss during this audit (commit a2e96d0). Residual: box lacks NOT-for/tradeoff line. **ACTION: keep · P3 · fix: add NOT-for (whole-home/long-outage class) + tradeoff line to the Jackery box.**

---

## Boss post-script to synthesis (post-hotfix state)
Since seat B's synthesis was written, the Boss hotfixed: the two live ITC errors it flagged (how-much-do-solar-panels-cost FAQ + how-much-do-solar-batteries-cost present-tense claim, commits 91d6538/4f58a19) and portable-solar-panels' raw LaTeX + "Bougevert" misspelling (4f58a19). The synthesis's "3 worst" list therefore now reads: worst remaining = solar-battery-cost-2026 (vendor-sourced CNTEpower claim + box contradiction + zero internal links — unfixed), followed by the panel trio (seat A's domain, partially hotfixed).
