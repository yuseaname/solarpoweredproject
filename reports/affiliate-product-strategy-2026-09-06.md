# Affiliate Product & Content Strategy — solarpoweredproject.com

**Date:** 2026-09-06 · **Program:** United States / Amazon.com (tag `slrpwp-20`)
**Team:** Boss (fact-pack, verification, integration) + 5 seats — glm-xo-2 (audience/competitive), glm-xo-3 (category scorecard), glm-or-1 (compliance), glm-xo-1 (keyword map), dsv4-wing-3 (clusters/roadmap; Boss-completed after two seat truncations) — + independent review (verdict at end). Raw deliverables: `.agency/affiliate-strategy/w1..w5*.md`.
**Extends, does not replace:** market-research-2026-09-05 · seo-keyword-audit-2026-09-05 · buyer-intent-content-plan-2026-09-05 · affiliate-cro-audit-2026-09-06.
**Evidence labels:** [S] site-verified (repo path, 2026-09-06) · [K] SERP evidence (Brave captures 2026-09-05/06 — search API was degraded both days; Brave/DuckDuckGo HTML = working proxy) · [V] live web-verified by Boss 2026-09-06 (URL + date) · [E] estimate — no keyword tools, no GSC data; **no search volumes or KD numbers are invented anywhere in this report.**

---

## 1. Executive Summary

**The niche opportunity.** US DIY/small-scale solar sits in a rare state: the SERPs for exactly the queries that end in component purchases — sizing, troubleshooting, brand-vs-brand, calculator intents — are still owned by forums (Reddit appeared in 17/18 captured SERPs; YouTube 13/18 [K]) and thin vendor blogs, with **no trusted editorial result**. Re-checked live 2026-09-06: still true, with more low-quality noise entering, which raises the quality bar rather than closing the gap [K]. Meanwhile both ends are genuinely locked: head "best [big-ticket]" roundups belong to lab-testing media, cost queries to EnergySage-class marketplaces [K]. The winnable middle is precisely where this site already lives.

**The strongest monetization direction.** Component-level spec-math commerce built on the honest no-test-lab model: the **LiFePO4 100Ah class** (anchor: LiTime B084DB36KW, already the site's most-placed product at 15 placements/12 pages [S]), **MPPT controllers** (4 spec-math reviews already live [S]; component roundup SERPs demonstrably open to small sites [K]), and **wiring hardware** — fuses, busbars, cable, tools (the site's two stickiest pages are cable-size and fuse-sizing calculator intents [K], and the sizing answer *is* the purchase spec). Power stations monetize through sizing/runtime pages only, never roundup attempts.

**Top 3 product categories to prioritize** (from the 18-category scorecard, §3): 1) LiFePO4 100Ah batteries (Overall 9/10); 2) MPPT charge controllers (8/10); 3) fuses/breakers/busbars + cable hardware (8/10).

**The monetization math (verified rate card).** Amazon's official public **Associates Program Standard Commission Income Statement** — `affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ`, retrieved 2026-09-06, Boss-fetched twice (access note: W3's legacy paths `/help/operating/schedule` and `/help/operating/advertisingfees` now 302 to sign-in/bot-walls; this separate public help node still serves the full table) — shows **fixed category rates, no volume tiers**: Tools / Home Improvement / Outdoors / Lawn & Garden **3.00%**, Kitchen / Automotive **4.50%**, "All Other Categories" **4.00%** [V]. Most of this niche's components sit in the 3% rows; some gear may land in the 4% catch-all — **per-ASIN categorization is Amazon-internal and should be glanced at in Associates Central (user action, 2 min; the logged-in Commission Income Statement remains the authoritative per-account view)**. At a 3–4% effective rate, the $2,000/month target (AC-001) requires roughly **$50k–67k/month in referred sales** — e.g. ~7–15 orders/day at $300 AOV, or 2–5/day at $900 power-station AOV [E on mix]. That is far more reachable than the 1–2.5% worst case ($80k–200k) — but it only compounds after Google indexing ramps (Googlebot unblocked 2026-09-06; GSC submission is the pending user lever).

**Biggest risks and constraints.** (1) Traffic is still near-zero — the strategy's phase-4 depends on GSC/Rybbit data that only starts accumulating once the user's two dashboard levers land. (2) Commission dependency: rates are category-fixed but per-ASIN assignment is opaque; program-policy change risk stays flagged. (3) The honesty model forbids testing claims — which caps some formats (no "we tested" roundups) and is simultaneously the site's differentiation. (4) Seasonal deadline pressure: the winter cluster must be live by ~Oct 10 to catch the Nov–Feb peak. (5) ~40% of sessions are non-US and currently leak (OneLink/marketplace setup unverified [W3 §4]).

---

## 2. Niche & Audience Analysis

### 2.1 Audience segments (Amazon-fit view; full evidence in market-research §2)

| Segment | Journey | Amazon fit | Basket sequence (1st → 2nd → 3rd) |
|---|---|---|---|
| **RV/van builders** | sizing → component compare → buy, urgent, budget-conscious | **Excellent** | 100W panel + MPPT + 100Ah LiFePO4 → monitor, fusing/MC4, multimeter → pure-sine inverter, 2nd battery, DC-DC [W1 §2.1] |
| **Cabin/off-grid homesteaders** | long research, phased buying | **Excellent** | 2–4× 100Ah + right-sized MPPT → 2kW+ inverter, monitor, combiner/fusing → array expansion, transfer switch, 48V migration [W1 §2.2] |
| **Appliance-runtime / preparedness** (CPAP, fridge, well, outage) | research-then-buy fast, event-driven | **Excellent** | station sized to the appliance (or 100Ah + DC cable) → 100–200W portable panel + car charging → 2nd battery / multi-appliance kit [W1 §2.3] |
| Beginner homeowners (cost research) | trust-anxious quote-checking | Poor — trust layer only; attach monitors/components | — |
| DIY makers (TEG/pedal/wind) | experiment-driven, loyal | Small | bench meters, components |

**Common objections:** installer scams; wiring/fire fear; junk panels and brand-price inflation; "will it run MY thing" uncertainty. **Decision criteria:** verified math over marketing; $/usable-Wh transparency; NEC-grounded safety; warranty track record [W1 §2, market-research §2].

### 2.2 Competitive landscape (fetched 2026-09-05/06; detail in market-research §3)

| Player | Angle | Our differentiation |
|---|---|---|
| EnergySage | marketplace lead-gen; owns cost SERPs | zero DIY/12V depth; no quote funnel here |
| SolarReviews | weighted criteria for whole-home | component-level criteria a $150 buyer can use |
| mobile-solarpower.com (Will Prowse) | tested-to-its-limit curation + 1.14M-sub YT | a shop, not a library; we're the math library — never claim testing |
| Footprint Hero | solo creator, own-gear reviews + calculators | one-person bandwidth; we out-depth on runtime cluster + interactive tools on 12 pages [S] + corrections layer |
| Clean Energy Reviews | deep technical + own forum | AU lens; we are US/NEC/Amazon.com-native |
| Brand blogs (EcoFlow/Jackery/Redodo/BougeRV) | SKU-centric runtime pages | cross-brand $/usable-Wh math they can't do |
| Forum layer (Reddit in 17/18 SERPs) | peer experience | we build the canonical decision tree a thread can't |

**What shifted in the 24h re-check [K]:** thin affiliate/vendor pages now flood the troubleshooting tail (quality bar rising); shopping carousels sit atop some component "best" queries; a small independent (poweroutage.us) now ranks a CPAP-backup roundup — proof the preparedness roundup layer is enterable without a lab; calculator SERPs are crowding with thin tools (solarmathlab-class). Net: strategy unchanged; quality signals (worked math, cited code, honest methodology) and early entry into runtime/preparedness space are more urgent.

### 2.3 Positioning

**The neutral, written, math-first US decision layer for small-scale solar.** Everything routes through sizing arithmetic the reader can check: calculator → sizing page → comparison → spec-math review → tagged link at the decision moment. No testing theater, no price displays, corrections page public.

### 2.4 Areas flagged as too broad / risky / misaligned

Whole-home install expansion (no Amazon path) · national cost queries (locked + unsourceable price claims) · SKU-framed station queries (brand-blog lock) · deep-well pumping (specialist, weak catalog) · policy/net-metering wars (freshness treadmill) · anything requiring testing claims or price display. Full list with reasons in §10.

---

## 3. Product-Category Opportunity Scorecard

18 categories, scored 1–10 (traffic potential · buyer intent · monetization suitability · competition realism · content depth · trust/experience fit · **overall**). Evidence per row in `.agency/affiliate-strategy/w2-categories.md`.

| # | Category | Traf | Intent | Monet | Comp | Depth | Trust | **Ovr** | Key risk |
|---|---|---|---|---|---|---|---|---|---|
| 1 | LiFePO4 100Ah batteries | 8 | 9 | 8 | 6 | 8 | 9 | **9** | price volatility, model churn, thermal claims |
| 2 | MPPT controllers | 7 | 9 | 8 | 5 | 9 | 9 | **8** | clone churn, spec drift |
| 3 | Fuses/breakers/busbars/MC4 fuse kits | 6 | 8 | 8 | 6 | 8 | 9 | **8** | safety-critical math errors = trust damage |
| 4 | Battery monitors/shunts | 5 | 8 | 8 | 6 | 8 | 9 | **8** | low AOV |
| 5 | Cable/lugs/tray cable | 6 | 8 | 7 | 6 | 8 | 8 | **8** | AWG/ampacity liability, counterfeits |
| 6 | MC4 connectors + crimp tools | 6 | 8 | 7 | 5 | 8 | 8 | **7.5** | video-carousel how-to lock; cross-mating safety |
| 7 | Winter/cold-weather kit | 5 | 8 | 7 | 6 | 8 | 8 | **7.5** | cold-charge safety claims; seasonal |
| 8 | DC-DC chargers (van/RV) | 6 | 8 | 8 | 6 | 7 | 8 | **7.5** | alternator-compat claims; vehicle wiring |
| 9 | Pure-sine inverters (12V) | 7 | 8 | 7 | 5 | 7 | 8 | **7** | surge-claim inflation |
| 10 | Hand tools/meters | 5 | 7 | 8 | 6 | 7 | 8 | **7** | CAT-rating claims; low basket |
| 11 | Battery enclosures/boxes | 4 | 7 | 7 | 5 | 8 | 8 | **6.5** | narrow demand; venting safety |
| 12 | Transfer switches/interlocks | 5 | 8 | 6 | 5 | 7 | 7 | **6.5** | electrician territory |
| 13 | Surge protectors / SPDs | 4 | 6 | 7 | 6 | 7 | 8 | **6.5** | NEC nuance |
| 14 | Controller accessories (dongles, remotes) | 4 | 6 | 7 | 6 | 7 | 8 | **6.5** | tiny AOV, fit confusion |
| 15 | 100W panels/starter kits | 7 | 7 | 7 | 4 | 6 | 8 | **6.5** | shopping-carousel heads; shipping returns |
| 16 | Mounting/racking | 5 | 7 | 6 | 5 | 6 | 7 | **6** | roof-penetration liability; video SERPs |
| 17 | Power stations 1–2kWh | 9 | 8 | 8 | 2 | 7 | 6 | **6** | traffic 9 = demand size, not entry feasibility — head SERPs lab-media locked; fast churn; sizing-page access only |
| 18 | Small solar electronics (lights/USB) | 6 | 5 | 4 | 5 | 4 | 6 | **4.5** | low AOV × low intent; deprioritized |

**Commission notes (per the verified fixed-rate card [V]):** rate does not vary by our effort — only Amazon's internal category per ASIN does (3% Tools/Home-Improv/Outdoors rows vs 4% catch-all; per-ASIN truth needs a dashboard glance). So category priority above is driven by demand × fit × attach, not rate-shopping. AOV bands [E]: LiFePO4 100Ah class ~$170–300; MPPT $90–260; fuse/busbar hardware $15–90; monitors $60–200; inverters $150–450; stations $300–1,100.

---

## 4. Top Recommended Product Opportunities

Model-level rows within the top categories. **Testing verdict for every row: not feasible → spec-math angle** (house rule: manufacturer datasheets + worked sizing math; never imply bench testing). Current 18-ASIN inventory (69 placements, **37 files** [S — grep-verified; the earlier "36 monetized pages" figure in the 09-05 CRO audit and fact-pack undercounted by one; includes B0816BTL82 SOLPEX lights, which the fact-pack table omitted) is the base; new verified candidates below extend it.

### A. LiFePO4 100Ah class
| Product | Status | Buyer / why considered | Criteria & tradeoffs | Angle |
|---|---|---|---|---|
| LiTime 12V 100Ah (B084DB36KW) | boxed, 12 pages [S] | DIY bank builders; site default block | $/usable-Wh over cycle life; 100A BMS ceiling; low-temp cutoff | **T-002 spec-math review — first-10 #1** |
| LiTime 100Ah self-heating, Group 24 (B0DJ957H39) | **[V]** new | cold-climate cabin/RV | heater draw vs charge acceptance; 2 heating modes; IP65 | winterizing + below-freezing pages (Oct 10) |
| Redodo 100Ah self-heating (B0F9YHLVJK; Group-31 variant B0CNR87Q1P) | **[V]** new | price-first cold-climate DIYer | warranty enforceability; -4°F charge claim verification | budget alternative section, same pages |
| 2×/4× parallel bank builds (same ASIN) | [S] | growers | never-mix-old-new; busbar balancing | worked-math section, expansion-planning piece |
| Group-24/31 form-factor LiFePO4 | **[V]** exists | RV drop-in upgraders | BMS amps vs inverter draw; weight | RV sizing attach |

### B. MPPT controllers
| Product | Status | Buyer / why | Tradeoffs | Angle |
|---|---|---|---|---|
| Victron 100/30 (B073ZJ3L13) · 100/20 (B075NPQHQK) | reviews live [S] | reference class / right-sizers | array Isc headroom | keep spec tables dated |
| Renogy Rover 40A (B01MSYGZGI) · EPEver Tracer 4210AN (B01GMUPGZA) | reviews live [S] | 400W-class / budget | BT vs display; warranty terms | "40A vs two smaller" section |
| Victron SmartSolar 150/35 (B073ZHRG9K; BlueSolar non-BT B01BVQT2ZA) | **[V]** new | 24V/48V upgraders | cold-corrected Voc vs 150V ceiling | 48V wiring + expansion pieces |
| EPEver BT-1 dongle | [E] class verified, model [NV] | Tracer owners | adapter economics | Tracer review section |

### C. Wiring hardware (fuses/busbars/cable/tools)
| Product | Status | Buyer / why | Tradeoffs | Angle |
|---|---|---|---|---|
| BougeRV 15A MC4 inline fuse kit (B08L56RDNP) · Blue Sea 2315 busbar (B094QWG3VV) | boxed [S] | string protection / clean distribution | fuse amps vs Isc; stud count | calculator pages attach |
| Blue Sea **5502/5503 Class T** block | **[V]** corrected | inverter-bank protection | AIC rating; interrupt speed (correction: 5025 is the ATO blade block, not Class T) | **Class T vs ANL vs MRBF page** |
| MRBF terminal fuse · ANL kit | [E] class real | compact / budget bank fusing | AIC lower than Class T — say so | same page |
| Klein MM600 (B018CLOSTC) · iCrimp crimper (B017S9EINA) | boxed [S] | every builder | CAT ratings; die coverage | troubleshooting + cable pages |

### D. Monitoring (attach category)
Victron BMV-712 (B075RTSTKS, boxed [S]) + **SmartShunt 300A IP65 (B0DJ2P2XN5) / IP65 (B0CPZ1755Z) [V]**, genuine 500A street ~$100–120 at authorized dealers [V] + budget AiLi-class shunt [E] — the monitoring guide's comparison table (post-purchase cluster).

### E. Winter kit (seasonal, Oct 10)
Self-heating LiFePO4 (above) + thermostat heater pads (Facon CW-T1218 12V class, silicone pads w/ 32°F thermostats) **[V]** + insulated enclosure guidance [E]. Community demand corroborated by live diysolarforum/solar-electric threads [V].

**Products explicitly not added:** anything whose specs can't be verified from a manufacturer source at write time; desulfators (see §10); power-station roundups beyond the two already-boxed models (B0C1SMJTDT, B0D7PPG25F) — stations enter via sizing pages only.

---

## 5. Organic Keyword & Search-Intent Map

Condensed from W4 (full tables + per-row evidence there). Demand/competition are **estimates** with stated basis (SERP composition + site pageviews). Priority formula in W4 §header. Page column = improve existing [path] or NEW.

| Cluster | Intent | Representative keywords | Demand/Comp (est. basis) | Page | Monetization | P |
|---|---|---|---|---|---|---|
| **C1 LiFePO4 buying** | commercial | lifepo4 100ah which brand · best lifepo4 for solar · litime 100ah review · 100ah vs 200ah | High/Med (shopping cards + 4 Reddit + PAA, Brave 09-06) | improve brand-comparison · NEW litime review · NEW 100ah-vs-200ah | B084DB36KW | 8 |
| **C2 Controller buying** | commercial | what size charge controller for 400w · best mppt charge controller · best mppt for 400w array | High/Med (Reddit + vendor blogs + YT, no editorial lock) | improve sizing + roundup · NEW 400w scenario | 4 controller ASINs | 9 |
| **C3 Inverter buying** | commercial | what size inverter · pure sine vs modified · inverter cable size chart | High/Med (forum-heavy) | improve sizing · pure-vs-modified · cable chart | B081CLPDT9 | 8 |
| **C4 Stations per appliance** | commercial | cpap battery backup / jackery cpap · chest freezer battery · oxygen concentrator backup · well pump station · what size power station | High/Med (retailer + Reddit + PAA; poweroutage.us proves entry) | improve cpap/freezer/oxygen · NEW well-pump (T-003) · NEW station calculator | B0D7PPG25F, B0C1SMJTDT | 9 |
| **C5 Wire/fuse/cable sizing** | tool→purchase | battery cable size calculator · solar fuse size calculator · solar wire size calculator · fuse between panel and controller | High/Low (site's own top pages; forums only) | improve + add calculators | Klein, iCrimp, busbar, fuse kits | 9 |
| **C6 Monitoring** | post-purchase | battery monitor shunt · state of charge off-grid · victron bmv-712 | Med/Low-Med (forum-heavy) | NEW monitoring guide (T-010) | B075RTSTKS + SmartShunt | 7 |
| **C7 Winter/cold** | seasonal | lifepo4 charging below freezing · solar panels winter output · winter storm backup power | High/Med (vendor blogs + 6 Reddit + iRV2, active now) | NEW below-freezing · winter-output · improve solar-generator winter section | B084DB36KW + self-heating class | 8 |
| **C8 RV/van** | segment | solar for van conversion · 12v vs 24v for rv · 100w kit expectations | Med/Low-Med (forum-dominated) | NEW van-conversion (T-004) · improve 12v-vs-24v · rv-sizing section | panel + controller + battery | 7–8 |
| **C9 Cabin/off-grid** | segment | cabin solar sizing/cost · 48v off grid wiring | Med/Low-Med (Victron forum ×4) | improve cabin trio · 48v guide | controller + battery | 6–7 |
| **C10 Starter/beginner** | entry | solar kit for shed · off grid solar for beginners | Med/Med | improve shed page (kit-vs-components math) · NEW roadmap start-here | starter kits (late) | 6–7 |

**PAA/question shapes:** question-form H2s already house-standard — keep; "In brief" 40–60-word direct answers target featured snippets [K]. **Excluded as unqualified** (no purchase path): DIY-generation silo, definitional TOFU (how panels work/efficiency), net-metering/policy rows, phone chargers/yard lights, anker-vs-jackery brand wars, "free solar panel" phrasings [W4 exclusions].

---

## 6. Content Cluster Blueprint

Three priority clusters (full per-article fields: title, keyword+intent, funnel stage, value, outline, products, link paths, CTA placement, effort/impact/priority — in `.agency/affiliate-strategy/w5-clusters.md`).

**Cluster A — LiFePO4 batteries** (pillar: best-solar-batteries-2026 → spokes: brand-comparison [verify + PF-8 box], li-ion-vs-lead-acid [monitor], NEW litime review, NEW 100ah-vs-200ah, NEW below-freezing, NEW monitoring guide → link path: every sizing/runtime page funnels to the pillar; review gets ≥3 inbound to fix starvation). CTAs: review pattern on the review; PF-8 mid-page deciders elsewhere.

**Cluster B — MPPT controllers** (pillar: best-mppt roundup → sizing hub + calculator, NEW 400W scenario, 4 reviews, symptom page mesh, Victron 150/35 section in 48V/expansion pieces, BT-1 economics in Tracer review).

**Cluster C — wiring hardware** (pillars: fuse-sizing + battery-cable-size, both gaining calculators → wire-size 100W example, fuses-vs-breakers decision section, NEW Class-T-vs-ANL-vs-MRBF authority page, MC4/combiner accessory mesh).

Cross-cluster paths: calculators (C5) feed every cluster's sizing entry; winter cluster (C7) links batteries (A) + stations (C4); the CRO audit's bridge gaps (12v-vs-24v → roundup, how-many-panels → panel guide) close in phase 1.

---

## 7. 90-Day Roadmap (phases; item = impact / effort / urgency / confidence)

**Days 1–7 (Sep 6–12) — decision layer + measurement.**
- T-002 LiTime review (H/M/H/H) · brand-comparison verify + box (H/S/H/H) · PF-8 handoffs ×3 + mppt-vs-pwm box move (M/S/M/H) — *in-repo, starts immediately.*
- User levers: GSC verify + sitemap submit; Rybbit outbound toggle (R-002) — **the phase-4 data clock starts here. Owner: user, ~30 min.**

**Days 8–30 (Sep 13–Oct 6) — winter window (hard deadline Oct 10) + calculator intents.**
- Winter cluster: below-freezing, winterizing (T-005), well-pump (T-003), van-conversion (T-004), solar-generator winter section (H/M/**H**/M-H).
- Fuse-size calculator, cable-calculator deepening, wire-size 100W example (H/M/M/H) · 100ah-vs-200ah (M/S/M/M-H) · controller-sizing calculator improve (H/M/M/H).

**Days 31–60 (Oct 7–Nov 5) — comparisons, Q4 tier, authority.**
- Jackery-vs-EcoFlow capacity math (M-H/M/M/M-H) · monitoring guide (M/M/M/H) · CPAP/chest-freezer/oxygen PF-8 + early-Nov outage push (M-H/S-M/M/M-H) · Class-T page (M-H/M/L/M) · expansion + Victron 150/35 (M/M/L/M).

**Days 61–90 (Nov 6–Dec 5) — optimize from real data.**
- First Rybbit funnel report + GSC query mining → retitle/expand what earns impressions (defers the 127-page title-trim backlog until data exists — consistent with the tech-SEO addendum) · BLUETTI-vs-Jackery (M/M/L/M) · start-here + complementary-products pages (M/S-M/L/M) · glossary +50 · December quarterly maintenance (R-003: OA re-verify, price bands, tag grep).

**Dependency chain:** everything compounds only after GSC indexing ramps; the Q4 push depends on the winter cluster; phase-4 optimization depends on 30 days of Rybbit outbound data (thus the phase-1 user levers are the schedule's critical path).

---

## 8. First 10 Articles / Page Updates (exact priority order)

| # | Piece | Type | Keyword / intent | Monetization relevance |
|---|---|---|---|---|
| 1 | LiTime 100Ah spec-math review | NEW (T-002) | "litime 100ah review" · decision | anchor ASIN's first destination page; fixes review starvation |
| 2 | LiFePO4 charging below freezing | NEW | winter · informational→commercial | self-heating class + pads [V] |
| 3 | Winterizing your off-grid system checklist | NEW (T-005) | winter · post-purchase | monitor/pads/enclosure attach |
| 4 | Well-pump power-station sizing (240V honesty) | NEW (T-003) | "solar generator for well pump" | 1–2kWh stations via sizing frame |
| 5 | Van-conversion solar use-case | NEW (T-004) | "solar for van conversion" | full RV basket sequence |
| 6 | Fuse-size calculator on fuse-sizing | UPGRADE | "solar fuse size calculator" · tool | sizing answer = purchase spec |
| 7 | Cable-calculator deepening + 100W wire example | UPGRADE | "battery cable size calculator" family | site's #2 page; tools already boxed |
| 8 | Battery monitoring guide (BMV-712 vs SmartShunt) | NEW (T-010) | "battery monitor shunt" | monitor attach category |
| 9 | Brand-comparison verify + PF-8 box | UPGRADE | "lifepo4 100ah which brand" | decision centerpiece stays fresh + monetized mid-page |
| 10 | Jackery vs EcoFlow capacity-class math | NEW | row 30, demand-verified | station class via math frame |

Rationale: #1 was already the PM queue's next item; #2–5 jump the 09-05 calendar because the Oct-10 winter window is hard and the cold-SERP is active now [K]; #6–7 enter on W4's calculator-intent evidence; #8–10 preserve the calendar's relative order.

---

## 9. Compliance & Credibility Checklist

**Program facts verified live 2026-09-06** [V/W3]: OA "Updated: October 15, 2025"; Program Policies "Updated: April 14, 2026" (both re-confirmed). Commission income = fixed % of Qualifying Revenue per the public Standard Commission Income Statement [V — see §1]. 24-hour session cookie (cart adds convert ≤89 days). Qualifying Revenue is net of shipping/tax/fees. Prices/availability displayable only via Amazon-served or PA-API/Creators-API data; star ratings/review counts API-only; no cloaking/shorteners/obscured URLs; disclosure "As an Amazon Associate I earn from qualifying purchases" clearly and prominently; FTC wants it near the recommendation.

**Per-article checklist (run on every new/edited monetized page):**
1. Disclosure present and near the first link (not footer-only).
2. No prices, star ratings, review counts, or availability claims anywhere; "current price on Amazon" framing only.
3. Links: tagged `slrpwp-20` format via the amazon/product-box shortcodes only; buttons honestly describe destination; no redirects that bypass a click.
4. No fabricated experience: no "we tested/measured" outside documented Project Lab builds; spec claims cite manufacturer sources with retrieval dates.
5. No fake urgency/scarcity/testimonials; no copied Amazon content; "best for" always = spec-matched with shown criteria.
6. ≥1 CTA before 60% page depth (PF-8); hub pages carry a link path to the monetized set.
7. US framing for voltage/price-context claims until international setup is verified.
8. Images: Amazon-served or site-owned only; no stale API-cached content (24h rule).
9. Anything policy-dependent labeled "Policy verification required" at draft time.

**Items requiring current verification (user, logged-in Associates Central):** per-ASIN commission categories for the top ~10 ASINs · OneLink/marketplace setup for the ~40% non-US sessions (revenue-only decision) · payment-minimum chart · the email-marketing participation clause (page 400'd on fetch today).

---

## 10. "Do Not Pursue" List

1. Head "best" roundups for big-ticket items — lab-media + retailer lock; would require fabricated testing [K].
2. National/state cost-query expansion — EnergySage-class data lock; unsourceable price claims [K].
3. SKU-framed station queries — brand-blog lock; enter via the math underneath [K].
4. Whole-home install buyer content beyond the existing trust layer — installs aren't Amazon products [K].
5. Any hands-on-testing claim, review-unit story, or implied bench testing — house rule; existential trust risk [S].
6. Price-tracking/deal-alert content — program-prohibited [V].
7. Thin-calculator spam class — quality misalignment; tool SERPs only with NEC-cited worked examples [K].
8. Non-US locale builds — leak until marketplace/OneLink verified [W3].
9. Desulfators/"rejuvenators" — chemistry-honesty conflict, weak evidence [E].
10. Deep-well solar pumping beyond the T-003 honesty page — 240V specialist class, weak catalog [E].
11. DIY-generation silo expansion — physics-curious traffic, no purchase path; keep as trust asset [K].
12. Net-metering/policy-war queries — freshness treadmill vs installers; support sections only [K].
13. Small solar electronics (yard lights, USB chargers) — 4.5/10 overall; low AOV × low intent [W2].

---

## Method & attribution

Fact-pack (Boss) → 5 parallel seats with live-web budgets → Boss verification pass (commission rate card double-fetch; six [NV] product families verified with ASINs; one model-number correction) → this synthesis. Raw seat files + evidence.json tool logs: `.agency/runs/20260906T*` and `.agency/affiliate-strategy/`. Seat failures (two final-write truncations) repaired/completed per incident protocol; notes obs-20260906T173022-*.

## Limitations

No GSC/keyword-tool data exists — all demand/competition figures are labeled estimates from SERP composition and the site's own small traffic base; Brave/DuckDuckGo HTML served as the search proxy (search APIs degraded both days). Commission rates verified from the public statement but per-ASIN category assignment is Amazon-internal. The strategy's traffic-dependent phases assume Google indexing ramps post-fix; if it doesn't, re-run the Q4 priorities against whatever the first GSC data shows.

---

## Independent review outcome

**qwen-judge, 2026-09-06 (reassigned after the original review seat truncated twice): VERDICT PASS, 92/100.** Ten checks: all 10 required sections present and substantive ✓ · ASIN/placement/category counts consistent ✓ · commission math correct ($2,000 ÷ 3–4% = $50k–67k) ✓ · zero invented volumes/KD ✓ · zero testing-implying phrasing ✓ · 5/5 spot-checked content paths exist ✓ · roadmap phases map cleanly to first-10 order ✓ · buyer-intent-plan re-prioritizations all carry reasons ✓. Findings acted on before delivery: **MAJOR** — rate-card [V] label needed its access path documented (legacy URLs 302 to sign-in; the public help node `GRXPHT8U84RAYDXZ` still serves the table; §1 now states this, and the logged-in Commission Income Statement stays flagged as the authoritative per-account view) — **fixed**. **MINOR** — 36→37 monetized-file discrepancy now acknowledged in §4 — **fixed**. **MINOR** — scorecard row 17 traffic-vs-competition tension clarified (traffic = demand size, not entry feasibility) — **fixed**. Full review verbatim: `.agency/affiliate-strategy/review.md`.

---

## Addendum — media layer (2026-09-06, evening)

**Directive:** user authorized dedicated AI-generated article imagery — "3–7 images per article from magica media skill gpt image 2." **Standard:** `reports/media-standard-2026-09-06.md` (binding honesty rules: generated images are illustrations, never product photography — no branded/SKU-accurate renders, no logos, no fake-testing scenes; every alt labels the image as illustration/diagram; diagram labels trace to the article's own numbers). **Engine:** Magica `gpt-image-2-text`, quality `medium`, house style = flat technical illustration on warm paper with orange/charcoal accents (matches the design system and existing field-guide diagrams).

**v1 rollout (this session):** 28 images across 13 pages — 7 heroes + 15 concept figures for the seven pages published today (each article now carries hero + 2–3 decision-math figures), plus 6 dedicated heroes replacing the duplicated themed assets from the morning og-image fix. Per-image Boss vision-verification against §1 before integration; rejects regenerated. ~1.2 credits of the 34.30 balance.

**Standing rule going forward:** every new article ships with hero + inline figures per the standard (3–7), budgeted at ~0.04–0.05 credits/image at medium quality; `high`-tier only for named showcase pieces. The "dedicated hero art" open decision in STATUS is now **resolved** by this standard.
