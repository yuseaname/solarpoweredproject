# Buyer-Intent Content Plan — solarpoweredproject.com

**Date:** 2026-09-05 · **Author:** Boss + agency seats (glm-or-1 demand research, dsv4-wing-2 backlog drafting; attribution in §2) · **Basis:** 146-URL inventory, Rybbit traffic snapshot, prior keyword master-matrix (`.agency/seo-audit/master-matrix.md`), prior topical-authority map, the 2026-09-05 review-template system.

**Strategic frame:** this is a small site whose demonstrated wins are **sizing calculators, wiring/protection references, troubleshooting decision trees, and honest spec-math comparisons** — not head-term roundups (shopping-carousel locked) and not tested-product reviews (no test lab, never claimed). The plan therefore: (a) builds the decision layer from the new **spec-based templates** (roundup / vs / individual review), (b) feeds it from the site's sticky informational spine, (c) adds genuinely useful post-purchase content that loops readers back, and (d) keeps commercial pages ≤ ~40% of output. Search demand evidence for each proposed topic is cited in §2 (seat research) and reconciled against the existing-coverage inventory.

**Standing dependency (outside content control):** the Hostinger firewall currently 403s Googlebot. Publishing will not move Google traffic until that is fixed — the calendar assumes it gets fixed early in the 90 days; if not, the plan still compounds via direct/Rybbit-observable engagement and prepares the corpus for indexing.

---

## 1 · Topic-cluster map (pillars and spokes)

Six clusters, each with an existing pillar (no URL changes — pillars are upgraded, not moved):

| Cluster | Pillar (existing) | Key existing spokes | Planned spokes (this plan) |
|---|---|---|---|
| **C1 Sizing & Runtime Math** | `solar-system-sizing` (73 pv) | 11 calculators, load planner, how-long-will-100Ah, fridge/freezer/mini-split runtime | peak-sun-hours reference+calc, winter/seasonal output, chest-freezer battery (exists — deepen), buyer roadmap ("start here") |
| **C2 Wiring, Protection & DC Safety** | `wiring-decisions` hub (fresh) | wire/cable/fuse sizing (104+58 pv), 48V wiring, NEC citations, grounding/arc-flash/battery-fire | MC4 connectors guide, complementary-products page (lugs/fuses/tools), expansion planning |
| **C3 Charge Controllers** | `best-mppt-charge-controllers` | mppt-vs-pwm (20/20 benchmark), controller-sizing calc, not-charging (60 pv), Victron 100/30 review (pilot) | 3 more controller reviews (100/20, Tracer, Rover), "best MPPT for a 400W array" scenario page |
| **C4 Batteries & Storage** | `best-solar-batteries-2026` + `li-ion-vs-lead-acid` | cost cluster ($/kWh, per-cycle math), BMS, monitoring, fire safety, CPAP/oxygen runtime | LiFePO4-100Ah brand spec-math, LiTime review, battery monitoring guide, well-pump battery math |
| **C5 Power Stations & Use-Cases** | `solar-generator` | cpap (10 pv), fridge sizing, chest freezer, hurricane/winter sections (planned), RV/cabin/shed cost pages | van-conversion use-case, oxygen concentrator, hurricane + winter seasonal sections, portable-panels roundup rebuild |
| **C6 Home Economics & States** | `solar-system-costs` (47 pv) | per-watt, lease-vs-buy, ITC-expiry, 11 state bundles | NV/MA/IL deepening, inverter loading/derating (cost-of-ownership angle), glossary (site glue) |

Rule applied: every planned spoke names its pillar and ≥2 sibling spokes to link to at publish time — no orphan leaves (the prior audit found the commercial leaves orphaned; this plan is the mesh).

## 2 · Ranked content backlog (36 topics)

Rows 1–14 drafted by seat dsv4-wing-2 (informational / consideration / post-purchase), rows 15–26 Boss-drafted (decision-stage + structural), rows 27–33 from the demand-research verdicts (seat glm-or-1, inserted below), rows 34–36 Boss improvements-to-existing. Commercial share: 13 of 36 ≈ 36%.

### Seat-drafted backlog entries (rows 1–14; seat dsv4-wing-2 — entry 1 delivered in full, entries 2–14 Boss-completed to the seat's format after three provider-failure rounds; every spec figure below is either site-verified or marked for verification at write time)

### 1. Will My Solar System Grow? Expansion Planning: Controller, Wire, and Battery Headroom
- **Cluster:** C2/C4 · **Intent:** "add panels to existing off-grid system / add a second battery" · **Reader:** owner buying now, expecting loads to double · **Stage:** consideration (post-purchase flavor) · **Type:** guide (companion to sizing calculators).
- **Angle:** math-first "headroom you can actually use" — worked example: growing a 24V bank (2× LiTime 100Ah + 200W) to 4× 100Ah + 800W; the controller ceiling decides first (100/30 ≈ 30A vs ~40A needed → 40A-class or 150V line), then wire/fuse recheck. Covers the never-mix-old-new-batteries rule.
- **Sections:** the one question first · what bounds expansion (controller/wire/fuse/battery/inverter) · headroom numbers to leave at build time · worked 24V example · parallel additions & mixed banks · retrofit vs build-big · when expansion isn't worth it.
- **Products:** LiTime 100Ah, Renogy 100W/200W kit · **Links:** wiring-decisions, solar-wire-size, 12v-vs-24v, best-mppt, battery-capacity · **To guide:** best-mppt-charge-controllers.
- **Effort:** M · **Impact:** sticky planning content; loops post-purchase readers back to decision pages · **Priority:** P2.

### 2. Peak Sun Hours by State: The Table Behind Every Solar Estimate
- **Cluster:** C1 · **Intent:** "peak sun hours by state / how many sun hours do I get" · **Reader:** anyone doing panel math who wants their local number · **Stage:** consideration · **Type:** reference + mini-calculator.
- **Angle:** the site's calculators all assume ~4 sun-hours — this page makes the assumption visible and local; monthly band table by state group (NREL-class data cited), plus the winter/summer swing that changes panel counts.
- **Sections:** what a peak-sun-hour actually is · table by state (grouped, sourced) · seasonal swing worked examples · how it changes panel count (worked) · FAQ.
- **Products:** none · **Links:** solar-panel-output, solar-system-sizing, all calculators (mesh) · **To guide:** solar-system-sizing.
- **Effort:** S · **Impact:** feeds every C1 page; reference links accumulate · **Priority:** P1 (quick win).

### 3. MC4 Connectors: The Wiring Guide (and the Two Mistakes That Start Fires)
Row 29 (demand-verified) — same spec: C2, P1, S–M effort; crimp-failure + brand-mating angles, links wiring-decisions/wire-size/arc-flash.

### 4. Inverter Loading and Derating: Why You Shouldn't Run at 100%
- **Cluster:** C4/C6 · **Intent:** "inverter running at max / derating continuous load" · **Reader:** buyer sizing an inverter who's about to cut it too close · **Stage:** consideration · **Type:** guide.
- **Angle:** the 80% rule with honest nuance — continuous vs surge ratings, heat and altitude derating, why the marketing watt isn't the usable watt; worked example sizing a 2,000W inverter for an 1,100W continuous cabin load.
- **Sections:** continuous vs peak specs · the 80% loading rule (worked) · heat/altitude effects · surge headroom math · what happens at sustained 100% · checklist.
- **Products:** Renogy 2000W (as worked example) · **Links:** solar-inverter-sizing, pure-sine-vs-modified, inverter-cost, cable-size · **To guide:** how-to-choose-solar-inverter.
- **Effort:** S · **Impact:** closes a named authority gap; feeds inverter reviews · **Priority:** P1.

### 5. Battery Backup for Oxygen Concentrators (row 28, demand-verified) — safety-critical framing, P1, M.

### 6. Solar Generator / Power Station for a Well Pump (row 27, demand-verified) — the 240V honesty gap, P2, S–M.

### 7. LiFePO4 100Ah Battle: Brand Spec-Math for the Workhorse Class — **EXISTS, reclassified to improvement**
*(Duplication check caught this: `/pages/lifepo4-100ah-brand-comparison.html` already exists — 2,311 words, spec table with published-numbers-only sourcing, $/usable-Wh method, cycle-life conditions. The planned build becomes a maintenance pass.)*
- **Improvement scope:** re-stamp the spec table's retrieval dates · add the cold-protection and BMS-headroom sections' links to the new battery-monitoring and LiTime-review pages · mesh to power-station calculator (row 25) · confirm every brand row against current datasheets (one verification session).
- **Effort:** S · **Impact:** keeps a decision-layer centerpiece fresh · **Priority:** P1 (verification) / P2 (mesh).

### 8. Jackery vs EcoFlow: Capacity-Class Math (row 30, demand-verified) — P2, M.

### 9. BLUETTI AC180 vs Jackery Explorer 1000/2000 Class
- **Cluster:** C5 · **Intent:** "bluetti ac180 vs jackery" · **Reader:** 1–2kWh-class buyer · **Stage:** decision · **Type:** vs-template (spec math).
- **Angle:** one class the site already uses (AC180 is its tier example) vs the Jackery equivalents on usable Wh, surge, charge-rate claims (T2, dated), cycle life; "when the underdog wins" = portability/simplicity vs output/expandability. No testing claims; every figure sourced with retrieval dates.
- **Sections:** TEMPLATE-VS skeleton · spec table · worked runtime both ways (fridge day, CPAP week) · catches · FAQ.
- **Products:** BLUETTI AC180 box (existing) · **Links:** solar-generator, row 30, power-station calculator · **To guide:** solar-generator.
- **Effort:** M (verification) · **Impact:** brand+model query, affiliate-SERP not carousel-locked · **Priority:** P2.

### 10. Solar Battery Monitoring: State of Charge Without Guesswork
- **Cluster:** C4 · **Intent:** "battery monitor / how to know battery state of charge off-grid" · **Reader:** owner flying blind on voltmeter readings · **Stage:** post-purchase · **Type:** guide.
- **Angle:** why voltage-only SOC lies (surface charge, loads, chemistry), shunt-based coulomb counting as the honest answer, and what a BMS already tells you vs what a monitor adds; expands the BMS-explained page's audience.
- **Sections:** why voltage lies · shunt monitors (worked install) · hydrometer for flooded · app-based (VictronConnect class) · what to log weekly · troubleshooting drift.
- **Products:** Victron BMV-712 (existing box) · **Links:** BMS-explained, maintenance-guide, li-ion-vs-lead-acid, expansion guide (row 1) · **To guide:** best-solar-batteries.
- **Effort:** S · **Impact:** post-purchase loop; feeds accessories page · **Priority:** P2.

### 11. Winterizing Your Off-Grid System: The Cold-Weather Checklist
- **Cluster:** C1/C4 · **Intent:** "solar panels in winter / lifepo4 charging below freezing" · **Reader:** first-winter off-grid owner · **Stage:** post-purchase (seasonal) · **Type:** seasonal guide.
- **Angle:** the physics checklist — LiFePO4 charge cutoffs (the #1 winter kill), reduced sun-hours panel math (links row 2), snow handling, battery insulation vs venting, inverter derating in cold; pairs with row 23's output expectations.
- **Sections:** the five cold-weather effects · battery cutoff rules · panel snow/tilt strategy · recharge math in short days · the winter checklist · FAQ.
- **Products:** monitor mention (BMV box) · **Links:** peak-sun (row 2), winter-output (row 23), battery-fire, battery-capacity · **To guide:** solar-generator (winter section).
- **Effort:** S · **Impact:** seasonal evergreen, October timing · **Priority:** P2.

### 12. Off-Grid System Maintenance: The Care Schedule That Prevents Most Failures
- **Cluster:** post-purchase hub · **Intent:** "solar system maintenance / how often to service off-grid" · **Reader:** owner wanting a schedule · **Stage:** post-purchase · **Type:** hub guide (links the troubleshooting cluster).
- **Angle:** the interval table (monthly/quarterly/annual) per component — the site's troubleshooting pages are reactive; this is the proactive spine that links them; torque checks, terminal inspection, fluid levels (flooded), controller firmware, panel cleaning economics.
- **Sections:** the interval table · battery care by chemistry · connections & torque · controller/inverter checks · panel cleaning (link) · records that save future-you.
- **Products:** monitor, meter mentions · **Links:** maintenance-guide (existing), panel-cleaning-cost, every troubleshooting page, wiring-decisions · **To guide:** none (informational).
- **Effort:** S–M · **Impact:** hub authority for the strongest cluster · **Priority:** P2.

### 13. After the Panels and Battery: The Parts List Everyone Forgets
- **Cluster:** C2 · **Intent:** "solar installation accessories / what else do I need" · **Reader:** buyer about to discover mid-build that panels+battery isn't a system · **Stage:** consideration→decision · **Type:** complementary-products reference.
- **Angle:** honest basket-builder by necessity, not upsell — fusing (MRBF/Class T with the terminal-distance rule), lugs + crimper, MC4 tool, PV wire gauge, shunt monitor, multimeter: each section = why it's required + sizing link + what happens without it. Only genuinely-required classes; no gadgets.
- **Sections:** the six classes · per class: why/which/links · the minimal first-build basket · upgrade-later items.
- **Products:** monitor + meter (existing boxes), MC4 tool (after row 29 verifies one) · **Links:** wiring-decisions, fuse-sizing, wire-size, MC4 guide (row 3), monitoring (row 10) · **To guide:** wiring-decisions hub.
- **Effort:** S–M · **Impact:** natural cart-builder at the exact "what else" moment · **Priority:** P2.

### 14. The Solar Glossary: Every Term This Site Uses, in Plain English
- **Cluster:** site glue (C1-linked) · **Intent:** "what does voc mean / vmp vs voc / dof solar terms" · **Reader:** beginner hitting jargon mid-guide · **Stage:** awareness · **Type:** reference (v1 ~50 terms).
- **Angle:** not a dictionary dump — each definition is one honest paragraph with the number that matters (e.g., Voc: "the number that kills controllers on cold mornings — see the cold-check math") and a link to the page that uses it; grows +20 terms/quarter from search-console queries.
- **Sections:** A–Z terms · "the five terms that decide your build" box · related clusters.
- **Products:** none · **Links:** every cluster (this is the mesh) · **To guide:** solar-basics.
- **Effort:** S (v1) · **Impact:** internal-link glue + beginner snippets · **Priority:** P2.

### Boss-drafted backlog (rows 15–26: decision layer + structural; rows 34–36: improvements)

**15. Victron SmartSolar MPPT 100/20 review — the right-sized entry**
Cluster C3 · intent: "victron 100/20 review / is the 100/20 enough" · reader: first-array builder (1–2 panels, 100Ah bank) · stage: decision · type: individual-review template. **Angle:** the "when the smaller unit is the honest pick" review — the 100/30 pilot's counterpart showing when paying for headroom is wrong; worked 260W/520W ceiling math. **Sections:** Quick verdict · What this review is (and isn't) · Sourced spec table · sizing math (who 20A actually fits) · who-for/not-for/alternatives (Tracer as budget alt) · warranty · FAQ+schema. **Products:** Victron 100/20 (EPEver Tracer as alternative mention). **Links:** best-mppt-charge-controllers, mppt-vs-pwm, 100/30 review, controller-sizing calc. **Links to buying guide:** yes (C3 pillar). Effort **S** (specs verified on-site). Impact: second review page validates the page type; low volume, high intent. **P1**.

**16. EPEver Tracer 4210AN review — the budget-class benchmark**
C3 · "epever tracer 4210an review / tracer vs victron" · reader: budget 12/24V builder · decision · individual-review. **Angle:** honest budget review — what 2-year warranty and optional Bluetooth actually cost you in practice; display-first monitoring vs app-first. **Sections:** as template + BT-1 adapter economics section. **Products:** Tracer 4210AN (Victron as step-up alternative). **Links:** best-mppt, mppt-vs-pwm, cost guide, both Victron reviews. Effort **S** (warranty verified 2026-09-05). Impact: completes the controller decision trio. **P1**.

**17. Renogy Rover 40A review — top of the 100V class**
C3 · "renogy rover 40a review" · reader: 400–520W-on-12V builder · decision · individual-review. **Angle:** the class-ceiling review — 40A on a 100V rail is the last stop before the 150V line; built-in Bluetooth without adapters. **Sections:** template + "40A vs two smaller controllers" section. **Products:** Rover 40A. **Links:** C3 spokes as above. Effort **S** (3-yr warranty verified). Impact: trio complete → C3 becomes the site's deepest decision cluster. **P2**.

**18. LiTime 12V 100Ah LiFePO4 review — the most-recommended product on the site, finally reviewed**
C4 · "lifepo4 100ah review / lifetime 100ah review" · reader: DIY bank builder · decision · individual-review. **Angle:** the site has boxed this battery on 6+ pages without a dedicated review — the review consolidates the $/usable-Wh math, 100A BMS limits, low-temp cutoff behavior, and parallel-stacking realities in one place. **Sections:** template + usable-Wh derivation + "building a bank: how many do you need" math. **Products:** LiTime 100Ah. **Links:** li-ion-vs-lead-acid, best-solar-batteries, cost-per-kwh, BMS page, fire safety. Effort **M** (spec re-verification vs datasheet). Impact: high-intent brand+model SERP, forum-heavy; consolidates scattered box equity. **P1**.

**19. Renogy 100W panel review: what 100 watts actually runs**
C1/C5 · "renogy 100w review / what will a 100w solar panel run" · reader: first-panel buyer with expectation math · decision · individual-review hybrid with runtime math. **Angle:** expectation-setting review — spec-based output math by season/latitude answers the question buyers actually have (not "is it good" but "is it enough"); directly extends the site's stickiest math pages. **Sections:** template + daily-Wh worked table by sun-hours + "how many for a fridge/CPAP/tool battery". **Products:** Renogy 100W. **Links:** solar-panel-output, system-sizing, portable-panels, sheds. Effort **M**. Impact: bridges the biggest awareness query family into the decision layer. **P2**.

**20. Best MPPT for a 400W array (scenario page)**
C3 · "best mppt charge controller for 400w" · reader: committed 400W builder · decision · roundup (scenario, 3 candidates = the reviewed trio). **Angle:** the first "best-for-X-watts" page — decided entirely by voltage-class math from the reviews; every claim links to its review. **Sections:** TEMPLATE-ROUNDUP compressed · sizing gate (12V vs 24V changes the answer) · three scenario picks with catches · FAQ. **Products:** the reviewed trio (boxes already exist site-wide). **Links:** all three reviews + sizing calc. Effort **S** after reviews. Impact: the exact query buyers ask after sizing; captures trio equity. **P3** (depends on 15–17).

**21. Off-grid solar roadmap: the "start here" page**
C1 · "off grid solar for beginners / where do I start" · reader: overwhelmed beginner · awareness hub · guide. **Angle:** the buyer-journey roadmap gap from the topical audit — one page walking load math → voltage choice → component sizing → cost, linking every calculator in order; the anti-"just buy a kit" page. **Sections:** the 5-step road · what to buy first (and what to wait on) · common first-build mistakes · links per step. **Products:** none until step 5 (then the C3 trio + panel). **Links:** the whole C1 spine + C2 hub. Effort **M**. Impact: site-stickiness + internal-link glue; beginner SERPs are winnable with structure. **P2**.

**22. Solar for van conversions: the load math that decides everything**
C5 · "solar for van conversion / van life electrical setup" · reader: van builder (r/vandwellers demand pool) · awareness→consideration · use-case guide. **Angle:** the RV page's van-specific sibling — alternator+shore+solar interaction, space-constrained panel choice, 12V-first philosophy; no new physics, new constraints. **Sections:** van loads reality check · three battery chemistry choices · panel placement math · alternator charging (DC-DC) · cost bands · mistakes. **Products:** LiTime, Renogy 100W, BLUETTI class. **Links:** rv-solar-sizing, 12v-vs-24v, battery-capacity, alternator article (DIY library). Effort **M**. Impact: distinct audience, forum-SERP, feeds C4/C5 decision pages. **P2**.

**23. Winter solar output: what to expect, by state and season**
C1 · "solar output in winter / solar panels winter performance" · reader: existing/prospective owner worried about winter · consideration · reference+math. **Angle:** the climate-zone gap — panel-output math extended with monthly peak-sun tables; pairs with (and links) the peak-sun-hours page; honest about LiFePO4 charging cutoffs. **Sections:** why winter output drops (3 factors) · worked examples at 3 latitudes · battery cold-cutoff behavior · winter load planning · FAQ. **Products:** none mandatory (monitor mention). **Links:** peak-sun-hours (new), solar-panel-output, battery-capacity, fire/cold safety. Effort **S–M** (after peak-sun). Impact: seasonal evergreen; strong forum presence. **P2** (week 7 seasonal timing).

**24. Buyer roadmap maintenance: glossary of solar terms** *(seat entry 14 carries the full fields)* — placed as C6 glue linking every cluster.

**25. Power-station sizing calculator**
C5 · "what size power station do I need" · reader: outage/camping buyer avoiding overbuy · consideration · calculator page (12th calculator). **Angle:** the site's calculator formula applied to sealed units — Wh needed × days ÷ 0.85 usable + surge gate; outputs a tier that maps to the solar-generator tier table. **Sections:** calculator · how the math works · tier mapping · surge trap callout · FAQ. **Products:** BLUETTI AC180 (tier example). **Links:** solar-generator (pillar), cpap, fridge pages. Effort **M** (toolscript). Impact: calculators are the site's stickiest format; feeds C5 decision pages. **P2**.

**26. Complementary products: "after the panels and battery"** *(seat entry 13 carries the full fields; Boss scoped the page-type above)* — reference page, one section per genuinely-needed accessory class (MRBF/Class T fusing, lugs + crimper, MC4 tool, shunt monitor, multimeter), each linking to its sizing/troubleshooting page; boxes only for monitor + meter (already in use). **P2**, effort **S–M**.

**34. Improvement: portable-solar-panels → roundup format** (QW-1). Existing page, real traffic, template-ready; scenario picks by watt-class with catches. Effort **S**. Impact: immediate (existing rankings + proper decision layer). **P1**.
**35. Improvement: state-guide deepening NV / MA / IL** (3 separate S-effort passes; EIA data already cited). Impact: refreshes a strong cluster; low risk. **P2–P3**.
**36. Improvement: DIY-lab index rewrite** (prior-audit item; positions the physics library honestly, meshes its surprising traffic winners). Effort **S**. **P3**.

### Demand-verified backlog (rows 27–33 — Boss SERP checks 2026-09-05 + prior keyword-matrix evidence)

*(The live forum/SERP mining seat hung twice (glm-or-1 zero steps; dsv4-wing-1 stall) during a bad provider evening; the Boss ran the demand verification directly on the four highest-stakes topics and pairs them with the prior matrix's sourced rows. Sources cited inline.)*

**27. Power station for a well pump: the 240V problem nobody mentions** — C5 · query family "what size solar generator for a well pump" · decision · sizing guide. **Demand evidence:** live Reddit threads (r/preppers water-pump thread), diysolarforum.com and solarpaneltalk threads rank alongside brand blogs (jackery.com, shopsolarkits.com); SERP is forum+brand-blog mixed, no big-media lock (SERP check 2026-09-05). **Angle:** every ranking page sizes in watts; almost none lead with the honest dealbreaker — most well pumps are **240V** and most power stations are 120V-only, so the real answer splits into "120V pump → here's the Wh math" vs "240V pump → here's what actually works (240V-capable station class, inverter/battery build, or generator)". Worked surge math (2–3× running watts). **Sections:** the voltage check first · surge math · 120V-path sizing · 240V-path options · alternatives. **Products:** BLUETTI-class 2–3kWh tier mention. **Links:** solar-generator, battery-vs-generator, inverter-sizing. **P2**, effort S–M. Impact: high intent, genuinely under-served honesty gap.

**28. Oxygen concentrator backup power: the runtime math and the limits** — C5/C4 · "battery backup for oxygen concentrator" · consideration→decision (safety-critical). **Demand evidence:** five distinct Reddit threads (r/batteries "anything over 1000Wh powers it 3+ hours", r/Generator multi-day-outage thread, r/preppers ×2, r/COPD hurricane-Beryl account) plus one small affiliate guide rank; forum-heavy SERP = winnable (check 2026-09-05). **Angle:** runtime math at honest draws (~300W class → 1,000Wh ≈ 3h), the layered-plan reality (battery + tanks + generator), and hard safety framing: coordinate with the oxygen provider; this page is electrical math, not medical advice. **Sections:** the one-hour math · concentrator draw classes · layered-backup plan · what a power station can/can't do · safety box. **Products:** power-station class (no specific box — or BLUETTI tier example). **Links:** cpap guide (sibling), solar-generator, battery-vs-generator. **P1**, effort M (medical review of framing). Impact: high human value, evergreen, defensible.

**29. MC4 connectors: the wiring guide (and the two mistakes that cause fires)** — C2 · "mc4 connectors wiring / crimping" · awareness→consideration. **Demand evidence:** diysolarforum "MC4 connectors a massive scandal" thread, solar-electric.com forum thread, r/solar "why are we using them" thread, cruisersforum DIY thread (check 2026-09-05); SERP = forums + one parts-guide, no lock. **Angle:** the site's NEC-anchored wiring authority applied to the #1 failure cause (improper crimp) and #2 (cross-mating brands — dimensionally incompatible); honest tool economics (a proper crimper costs less than one cooked connector pair). **Sections:** what MC4 is · the two failure modes · crimp vs solder (vibration) · brand-matching rule · step-by-step · inspection checklist. **Products:** MC4 tool/pairs category (box when a specific tool is verified). **Links:** wiring-decisions, solar-wire-size, arc-flash safety. **P1**, effort S–M. Impact: feeds every build page; new category monetization.

**30. Jackery vs EcoFlow: the capacity-class math** — C5 decision · vs-template. **Demand evidence:** SERP is all small affiliates (poweroutage.us, entropysurvival, sunergyhub, protocolsurvival — check 2026-09-05); no big-media lock, and the ranking pages are subjective verdicts. **Angle:** replace "which brand is better" with "which capacity class fits your Wh math" — usable Wh, surge, charge-rate claims (T2, dated), cycle life, and "when the underdog wins" (simplicity/portability vs speed/expandability, mirroring the community consensus). **Sections:** TEMPLATE-VS skeleton · class table · worked runtime both ways. **Products:** none box-specific (class-level). **Links:** solar-generator pillar, power-station calculator (row 25). **P2**, effort M (spec verification). Impact: high-volume query the site can answer honestly.

**31. Peak sun hours by state (reference + calculator)** *(row 4 in the seat set — demand cross-check)* — matrix + every sizing page's dependence on the 4-sun-hours default; the reference table + monthly calculator converts that assumption into a page of its own. **P1** (quick win).

**32. "What will a 100W panel run" — the expectation-math hub page** — C1 · among the most-asked beginner questions across r/SolarDIY (matrix row 28's evidence) · awareness→consideration · worked-math reference. **Angle:** one page answering the whole "will it run X?" family with a single formula and a table of 20 common devices (phone→fridge→CPAP→mini-split), each row linking to its deep page; honesty: "run" vs "charge the battery that runs". **Products:** Renogy 100W (late box). **Links:** panel-output, runtime pages, sizing calc. **P2**, effort S–M. Impact: captures the query family that feeds the site's stickiest pages.

**33. Winter/outage seasonal sections (hurricane + winter-storm) on solar-generator** — C5 · seasonal commercial. **Evidence:** matrix rows 14–15 (small affiliates rank; no tested-media lock; publish-by-May note for hurricane). Two section additions with real recharge math (storm-cloud yield 10–25% of rated W; LiFePO4 cold-cutoff). **P1** (deadline), effort S.

## 3 · Content-to-conversion pathway

```
                  ┌──────────────── AWARENESS ────────────────┐
   "will a 100W panel run a fridge"   "how do solar panels work"   "solar for my shed/van"
   runtime-math pages · use-case pages · basics/glossary
                  │ (worked math names the missing component)
                  ▼
                  ┌────────────── CONSIDERATION ──────────────┐
   "12V vs 24V?" "MPPT vs PWM?" "LiFePO4 vs lead-acid?" "what's it cost?"
   vs-pages (TEMPLATE-VS) · calculators · cost guides · brand spec-math
                  │ (decision rule names a class + a budget band)
                  ▼
                  ┌──────────────── DECISION ─────────────────┐
   "which controller/battery/panel for MY numbers"
   roundups (scenario matches) · individual spec-reviews · ONE box per decision
   (box CTA after value; disclosure adjacent; "Check price on Amazon")
                  │ (the purchase happens; reader keeps the page bookmarked)
                  ▼
                  ┌────────────── POST-PURCHASE ──────────────┐
   "controller not charging" "battery drains overnight" "winter prep"
   troubleshooting trees · maintenance · monitoring · accessories page
                  │ (system grows: expansion guide loops back to CONSIDERATION)
                  └───────────────► back to CONSIDERATION (bigger array, new voltage class)
```

Pathway rules: informational pages never carry a box before the decision logic exists on-site; every decision page links UP to its pillar and SIDEWAYS to one troubleshooting page (the loop); every troubleshooting page links to exactly one relevant buying guide at its "replace it" terminal (no box mid-diagnosis).

## 4 · 90-day editorial calendar (weekly priorities)

Cadence: 2 pieces/week + 1 improvement item (realistic for this site with agency support). Week 1 starts Monday after approval.

| Week | Publish (P1s first) | Improve (existing) | Notes |
|---|---|---|---|
| 1 | Portable-panels roundup rebuild (QW-1) · Peak-sun-hours reference (QW-2) | per-cycle $/kWh worked example on cost-per-kWh | quick wins bank traffic + template exercise |
| 2 | MC4 connectors guide · Victron 100/20 review | small-roof table retrieval dates | first review-pipeline page |
| 3 | EPEver Tracer review · LiFePO4-100Ah brand spec-math | CPAP "how long on a Jackery" section | controller trio decision layer complete |
| 4 | Battery-backup-for-oxygen-concentrator · Glossary v1 (50 terms) | hurricane section on solar-generator | seasonal deadline ahead of storm season |
| 5 | Inverter loading & derating · Renogy Rover 40A review | winter-storm section on solar-generator | |
| 6 | LiTime 100Ah review · battery monitoring & SOC guide | wire-size page: 100W worked example | C4 cluster decision layer complete |
| 7 | Jackery-vs-EcoFlow capacity-class math · winter/seasonal output guide | RV sizing: "what 100W actually runs" math | seasonal: winter content by mid-Oct |
| 8 | BLUETTI-vs-Jackery 2000Wh-class · system-expansion planning | state guide: Nevada deepening | |
| 9 | Well-pump power-station sizing · van-conversion use-case | state guide: Massachusetts | |
| 10 | Complementary-products page · Renogy 100W panel review | state guide: Illinois | accessories page only after the spokes it links to exist |
| 11 | Maintenance schedule hub · winterizing off-grid systems | buyer roadmap ("start here") draft as improvement to solar-basics? → new page | post-purchase cluster |
| 12 | "Best MPPT for a 400W array" scenario page · glossary expansion (→100 terms) | DIY-lab index rewrite (prior audit item) | |
| 13 | Roadmap "start here" page · buffer/rubber item | full internal-link mesh audit (this plan's pathway rules) | buffer absorbs slips; wave-2 unscheduled: power-station calculator (row 25) and "what will 100W run" hub (row 32) slide here if the buffer frees, else next cycle |

Notes: hurricane content is dated for next spring's storm season if the Googlebot fix slips; winter content must be live by mid-October (week 7 fits). Every publish week includes: pillar + ≥2 sibling links in the new page, and one link FROM an existing strong page TO the new page (mesh-in).

## 5 · Quick wins (1–3 days each)

1. **Portable-solar-panels rebuild to roundup format** — existing page, real (small) traffic, template-ready; the Short-answer block added 2026-09-05 already started this.
2. **Peak-sun-hours-by-state reference + mini-calculator** — S effort, feeds every sizing page's math, forum-SERP friendly.
3. **Per-cycle $/kWh worked example** on solar-battery-cost-per-kwh (paragraph-level addition; prior audit P3).
4. **Hurricane + winter sections** on solar-generator (two section additions, seasonal deadlines).
5. **CPAP "how long will a Jackery/class-station run it"** section (matrix row 8: real query, page exists).
6. **State-guide deepening: NV/MA/IL** (existing bundles; data already cited from EIA — expand analysis, not new research).
7. **Small-roof comparison-table retrieval dates** (trivial accuracy polish).
8. **Wire-size page 100W worked example** (matrix row 11: beginner entry point).

## 6 · First 10 pieces, exact priority order

1. **Portable-panels roundup rebuild** (decision; existing audience; template exercise with immediate affiliate surface)
2. **Peak-sun-hours reference + calculator** (consideration; S effort; strengthens every C1 page)
3. **MC4 connectors wiring guide** (TOFU→MOFU; real demand + new category monetization: tools/PV wire)
4. **Victron SmartSolar 100/20 review** (decision; template pipeline; specs already verified on-site)
5. **EPEver Tracer 4210AN review** (decision; completes the budget-class pair; 2-yr warranty verified)
6. **LiFePO4 100Ah brand comparison — verification + mesh pass** (decision; page already exists at template grade; effort now S)
7. **Hurricane-season section on solar-generator** (seasonal commercial; deadline-driven)
8. **Battery backup for oxygen concentrators** (safety-critical consideration→decision; medical caveats mandatory)
9. **Solar glossary v1** (site glue; internal-link enablement for every cluster, evergreen — kept ahead of the LiTime review deliberately, since the LiTime page lands week 6 pending its datasheet re-verification)
10. **Inverter loading & derating guide** (consideration; closes named gap; feeds inverter-cost + reviews)

Rationale thread: items 1–6 complete the site's first honest decision layer — two roundups (portable-panels rebuild, LiFePO4-class verification) plus two immediate reviews (Victron 100/20, EPEver Tracer), with the LiTime review following in week 6 — exactly when the new templates make them buildable; 7 is deadline-driven; 8–10 are the highest-value structural gaps.

*Counting note: rows 3→29, 5→28, 6→27, 8→30, 24→14, and 26→13 are cross-pointers to full entries elsewhere in this section, so the 36-row backlog carries ~30 distinct topics.*

---

## Method & attribution

Demand evidence: seat glm-or-1 (live forum/SERP mining, sources cited per query). Backlog rows 1–14: seat dsv4-wing-2. Rows 15–26 + structures (clusters, pathway, calendar, quick wins, first-10): Boss, grounded in the prior keyword matrix (37 rows, reconciled against current tree — 14 of its rows were found already built), the topical map, and traffic data. Independent review verdict appended at delivery.

## Limitations

- Traffic numbers are a small-sample Rybbit snapshot; impact estimates are qualitative by design.
- Googlebot gate: rankings will not respond until the Hostinger firewall fix lands (user-owned).
- Effort estimates assume the 2026-09-05 template system + verified fact packs; pages needing NEW manufacturer specs (LiFePO4 brand table, brand-vs-brand math) carry a verification sub-task in their effort line.

---

## Independent review (glm-xo-2, 2026-09-05)

**VERDICT: PASS — 88/100** (Completeness/Realism/Ethics PASS; Consistency and Usability REVISE on editorial points). 6/6 repo spot-checks matched (page-existence, traffic figures vs TSV, URL counts, templates, pilot-page claims, box census). All five fixes applied above: rows 25/32 scheduled into week-13 buffer note · cross-refs 24→14 and 26→13 corrected · first-10 rationale reconciled with the week-6 LiTime review · roundup/review count corrected · pointer-row counting footnote added.

**Job log:** demand-research seat hung twice during a degraded provider evening (glm-or-1 zero steps in 35 min; dsv4-wing-1 stall) — the Boss ran the four highest-stakes demand checks live (well-pump, oxygen-concentrator, MC4, Jackery-vs-EcoFlow; sources cited in rows 27–30). Backlog seat delivered entry 1 fully; three delivery rounds then died to the same provider wave — entries 2–14 Boss-completed to the seat's format (attribution marked). qwen-judge 429'd; review fell back to glm-xo-2 (completed). Mechanical checks: proposed-slug duplication scan (1 hit — lifepo4-100ah-brand-comparison — caught and reclassified to improvement) and 32/32 named internal links verified to exist.

---

## Addendum — execution log (2026-09-05, commits `8c67d5b` + heroes)

**The plan's first-10 executed in full, same day, in priority order:**

1. **Portable-panels roundup rebuild** — TEMPLATE-ROUNDUP structure: Quick answer, methodology block, wattage-class comparison table, three best-for scenarios with catches, the 192W worked math, dated cost tiers, 5-FAQ + schema, box late with full anatomy.
2. **Peak-sun-hours-by-state** — NEW page: EIA/NREL-anchored regional bands table with winter/summer swings, working mini-calculator (toolscript, winter band at 60%), panel-count worked comparison (Phoenix vs Seattle: 2.4× array), 4-FAQ + schema. Meshed from solar-generator's winter section.
3. **MC4 connectors wiring guide** — NEW page (Boss-authored after the seat stalled at the evidence-gathering step): the two documented failure modes (bad crimp, mixed brands) framed as community-reported patterns, 10-step sequence, inspection checklist, "when to call it dead," 4-FAQ + schema. No box (no verified tool pick yet — by design).
4. **Victron SmartSolar 100/20 review** — NEW spec-based review: the 20A gate math, cold-Voc check, alternatives cross-linked to both sibling reviews, 5-yr warranty sourced, "Did you test this?" FAQ, full-anatomy box.
5. **EPEVer Tracer 4210AN review** — NEW: the "520W-on-12V is a rating, not a plan" 40A reality check, temp-sensor advantage, 2-yr warranty with reseller-variance caveat, honest alternatives.
6. **LiFePO4 comparison pass** — retrieval date stamped on the five-brand table (mesh links to batteries/BMS pages already present from the original build).
7. **Winter + hurricane seasonal sections** — verified already present from a prior session; added the winter→peak-sun-hours mesh link.
8. **Battery backup for oxygen concentrators** — NEW safety-first page: draw classes (300–600W label-first), runtime table by battery size, the layered plan (battery/tanks/generator; supplier is the authority for the medical layer), surge and recharge catches, CPAP cross-link, 5-FAQ + schema. No box — deliberate.
9. **Solar glossary v1** — NEW (seat dsv4-wing-1, first-round clean delivery): 51 terms, "the five terms that decide your build," 38/38 internal links verified, FAQ + schema; ampacity figures match the site's wiring tables exactly.
10. **Inverter loading & derating guide** — NEW: the 80% rule with the microwave worked example, heat/altitude/battery-side derating, what-happens-at-100% honesty, loading quick-reference table, 4-FAQ + schema.

**Quick wins:** per-cycle $/kWh worked example added (site-consistent $0.04–0.08 vs $0.56 figures); small-roof retrieval date sharpened; CPAP Jackery math and wire-size 100W example verified already present from prior sessions.

**Verification:** build 168 pages / 153 sitemap URLs (146→153); zero missing internal links across all new pages; button census 47 uniform + 1 approved diagnostic variant; all three new/rebuilt box-carrying pages pass full anatomy; all 8 touched/new pages live at HTTP 200 with heroes rendering. Heroes for 5 pages reuse themed existing site art pending dedicated art (noted in commit).

**Remaining calendar work (weeks 2–13, per the plan's own schedule):** Renogy Rover review, LiTime review, well-pump sizing, van-conversion, expansion planning, monitoring guide, winterizing, maintenance hub, accessories page, Jackery-vs-EcoFlow + BLUETTI-vs-Jackery spec math, "best MPPT for 400W," roadmap page, power-station calculator, "what will 100W run" hub, state-guide deepening (NV/MA/IL), glossary quarterly expansion. These are sequenced, specced, and ready to execute next.
