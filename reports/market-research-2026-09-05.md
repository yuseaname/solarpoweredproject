# Market Research & Ethical Monetization Strategy — solarpoweredproject.com
**Date:** 2026-09-05 · **Scope:** niche audit, audience/buying-intent, competitive landscape, SERP patterns, content gaps, Amazon-eligible monetization · **Market:** US-primary (Amazon.com program; ~40% US traffic, notable DE/GB/FR/PL/NL/AU/CA share per Rybbit internal analytics, 8.5-month history)
**Method:** 5 parallel research passes (SERP patterns across 18 queries; big-player competitor teardowns; DIY/community sub-niche; Amazon Associates + FTC rules verification; audience evidence from indexed community threads), Boss-verified spot checks on the highest-stakes claims (Amazon pricing policy confirmed verbatim against the live policy page; two SERP classes re-checked via independent search). Full research files with raw citations: `market-research/*.md`.
**Evidence labels:** FACT = cited source; INFERENCE = reasoned; ASSUMPTION = unverified. SERP compositions captured via independent indexes (Brave/DDG Lite) — directional proxies for Google, not identical orderings.

---

## 1. Executive Summary — the 5 strategic findings that matter

**1. The winnable middle is exactly where the site already lives — and almost nobody editorial competes there.** Across 18 captured SERPs, Reddit appeared in 17 and YouTube in 13 (FACT, `market-research/serp-patterns.md`). Troubleshooting queries ("solar battery not charging": 9/10 Reddit; "why is my inverter shutting off": zero dedicated editorial guides in top results) and comparison queries ("MPPT vs PWM": 7/10 Reddit; "Jackery vs EcoFlow": 9/10) show Google surfacing *forums because it has no trusted editorial result*. The only pages on this site that have ever earned traffic sit precisely in those classes. This is the niche's clearest white space and it requires no fabricated expertise — it requires better-organized math than a forum thread.

**2. The unwinnable ends are genuinely locked — stop feeding them.** Head "best" roundups for big-ticket items are owned by lab-testing major media ([OutdoorGearLab — 14 units tested](https://www.outdoorgearlab.com/topics/camping-and-hiking/best-power-station), [Consumer Reports](https://www.consumerreports.org/home-garden/generators/best-portable-power-stations-a4748703075/), [CNET](https://www.cnet.com/home/energy-and-utilities/best-solar-generators/), [CNN Underscored](https://www.cnn.com/cnn-underscored/reviews/best-solar-generator), [OutdoorLife](https://www.outdoorlife.com/gear/best-solar-generator-for-home-backup/); retrieved 2026-09-05). National and state cost queries are owned by marketplace data ([EnergySage](https://www.energysage.com/) appears in every captured cost/local SERP). An anonymous affiliate site cannot and should not fight either — no fake testing, no proprietary pricing. The state-cost guide cluster (11 pages) and the big roundup pages should be repositioned as sizing/incentive math that links out, not price-data competitors.

**3. Component-level commerce is still open — proven by other small sites ranking.** "Best MPPT charge controller" SERPs show four independent small sites in top results; calculator SERPs ("solar wire size calculator") are led by small independent tools (explorist.life, freesunpower.com; FACT, serp-patterns). Big-ticket roundups attract testing-media money; component roundups and tools have no such lock. The site's calculator infrastructure and component guides are its structural edge.

**4. Amazon compliance is a strategic asset, and the site is currently on the right side of the pricing rule — stay there.** Verified against Amazon's live policies page (retrieved 2026-09-05): prices/availability may only be shown via Amazon-served links or PA API/Creators API data with the required disclaimer and timestamp; price-tracking/alerting functionality is prohibited; disclosure must be clear and the FTC wants it adjacent to recommendations. The site's product boxes (no hardcoded price, "Check price on Amazon") are compliant by design. Editorial category price bands ("MPPTs run $120–250") are normal cost guidance — but never attach a specific "$X" to a specific ASIN unless API-served. The 24-hour cookie window also means links belong at the decision moment, not mid-research.

**5. The audience that converts on Amazon is not the whole-home buyer — and 40% of current traffic can't convert at all.** Whole-home installs aren't Amazon products; the Amazon-eligible buyer is the RV/van builder, cabin owner, appliance-runtime/preparedness buyer, and DIY component shopper. The site under-monetizes exactly those (31 of 132 pages carry links; CPAP/fridge/phone-charger/shed pages have none). And with ~40% of sessions from outside the US clicking Amazon.com links, either verify Amazon OneLink/multi-marketplace options or accept the leak (NEEDS VERIFICATION — program rules vary by locale; see compliance notes).

---

## 2. Audience & Buying-Intent Profile

Five evidence-backed segments (quotes captured from indexed community threads, 2026-09-05; full citations in `market-research/audience-evidence.md`; Reddit direct fetches were blocked, so segment 3/5 quotes are inference-level — flagged):

| Segment | Share of intent | Evidence snapshot (FACT unless noted) | Journey stage | Amazon fit |
|---|---|---|---|---|
| **Beginner homeowners (cost research)** | High volume, low Amazon fit | Recurring r/solar threads: "Is this a good quote?" (reddit.com/r/solar/comments/1clm5fc/), "Am I being scammed or is this legit?" (/sn3hwi/), "$0 solar install scam" (/1bd30ol/); community per-watt math $2.50–3.00/W "a pretty good deal," $4–5/W with dealer fees | Research → compare; trust-anxious | Poor (installs aren't Amazon products) — but high trust/authority value; components and monitors are attachable |
| **RV/van/boat builders** | High, urgent, budget-conscious | r/vandwellers: "100w or 200w solar panel for my needs?" (/7s17zu/), sizing-first answers ("calculate watts… THAT determines solar capacity"), Starlink-draw questions (/1bhw953/) | Sizing → component compare → buy | **Excellent** (panels, controllers, LiFePO4, inverters, monitors, wire/fuses) |
| **Cabin/off-grid homesteaders** | Medium, researcher-heavy | INFERENCE (forum captures blocked): sizing obsession, generator-vs-solar debates; diysolarforum Beginners Corner = 21.6K threads/223K messages (FACT) | Long research, phased buying | **Excellent** |
| **Appliance-runtime / preparedness buyers** | High urgency, event-driven | r/CPAP: "For how long would a 1000W battery run a cpap?", "Lost power last night… who uses a battery backup?"; runtime SERPs are brand blogs and thin factories (rackbattery.com "By admin") | Research-then-buy fast | **Excellent** (power stations, LiFePO4, panels) |
| **DIY makers (TEG/pedal/wind)** | Low volume, high loyalty | Project Lab cluster gets the site's only recent organic traffic (Rybbit FACT); forum wind/hydro board exists but small (254 threads, FACT) | Experiment-driven | Good (bench meters, components) |

**Common objections across segments (FACT-cited):** being scammed by installers or door-to-door sales; fire/wiring fear (RV); junk panels and inflated brand pricing; "will it actually run MY thing" uncertainty. **Decision criteria:** verified math over marketing, price-per-watt and $/usable-Wh transparency, safety-code grounding (NEC/fusing), honesty about limits.

---

## 3. Competitor Comparison Table

Established players (all fetched 2026-09-05; details in `market-research/competitors-core.md` and `competitors-diy.md`):

| Competitor | Model | Content depth | Selection methodology | SEO coverage | Trust signals | Review structure | CTA/monetization | Exploitable weakness |
|---|---|---|---|---|---|---|---|---|
| **EnergySage** | Marketplace (DOE-backed claim) | Broad homeowner guides | Not visible; brand/system level (INFERENCE) | Massive; owns cost/local SERPs | Named editorial team, market data | Quote-funnel oriented | Lead-gen (ZIP-code quotes) | Zero DIY/12V/off-grid coverage; every path sells an installer conversation |
| **SolarReviews** | Reviews + lead-gen | Deep; weighted published criteria (20/15/14/10… FACT) | Best in class — weighted scoring + own survey data; not hands-on (INFERENCE) | Broad US | Named experts, 50+ yrs claim | Installer + equipment reviews | Lead-gen + phone | Criteria (company financial strength) meaningless for $150 component decisions; flagship battery list lags (2025 edition, FACT) |
| **Clean Energy Reviews** | Independent technical (AU) | Very deep technical; own calculators + forum | Cites independent lab data (PVEL, FACT) | Strong technical | High technical authority | Analysis-first | Installer referrals (INFERENCE) | Australian lens — thin US pricing/brands/NEC (INFERENCE) |
| **ClimateBiz** | Multi-author affiliate blog | Broad but sprawling (hydroponics, green jobs) | Claims review units, no payment; little visible testing evidence (FACT policy) | Broad | "Experts" page, unverified credentials | Buyer's guides | Affiliate | Topical sprawl dilutes solar authority; testing-story gap |
| **Footprint Hero** (Alex Beale) | Solo creator, closest analog | DIY calculators + tutorials; narrow review catalog (3 lines, FACT) | Buys own gear ("I Bought Every Solar Panel at Harbor Freight", FACT); gifted-product policy | Niche-strong | First-person, transparent | Short review lists | Amazon Associates | One-person bandwidth; no state/code/runtime depth (INFERENCE) |
| **mobile-solarpower.com** (Will Prowse) | "Tested to its limit" curation + 1.14M-sub channel (FACT) | Product shortlists, not education | Genuine destructive/long-term testing (strongest in niche) | YouTube-first | Personality + diysolarforum accountability | Tiered picks | Amazon Associates | It's a curated shop, not a library: no sizing math, no calculators, no code/state content |
| **Off-Grid Garage** (AU, 125K subs, FACT) | Video maker w/ test-note pages | Long-duration cell/BMS tests | Real measured data + public spreadsheets (FACT) | YouTube + reference pages | Measurement-first | Component test notes | Affiliate/unknown | AU focus; test notes ≠ step-by-step guides with load math (FACT structure) |
| **Forum layer** (diysolarforum, r/SolarDIY, r/vandwellers) | Community | 223K+ messages of scattered answers | N/A — experiential | Ranks everywhere (17/18 SERPs) | Peer, anonymous | Thread-shaped | None | Canonical answers don't exist (FAQ board: 14 threads vs 21.6K questions, FACT) — the single biggest structural gap |
| **Brand blogs** (EcoFlow, Jackery, Anker SOLIX, ALLPOWERS) | Manufacturer content | Product-optimized answers | Sell the answer | Own brand-SKU queries | Commercial bias | Product pages | Direct sale | Zero neutrality; no cross-brand math |
| **Tested media** (OutdoorGearLab, Consumer Reports, CNET, CNN, OutdoorLife, PCMag) | Lab-testing publishers | Deep roundups | Real testing programs | Own head "best" terms | Strong | Ranked roundups | Affiliate/direct | Don't cover component math, codes, runtime sizing, or long-tail decision queries |

**Pattern (INFERENCE):** the niche splits into two camps that barely overlap — quote-selling marketplaces and personality-driven testers. **Nobody owns the neutral, written, math-first US decision layer.** That's the position solarpoweredproject.com is already accidentally positioned for.

---

## 4. Content & Positioning Gap Analysis

**Where the site already matches the gap (protect and deepen):** troubleshooting decision pages (only traffic winners), inline calculators, appliance-runtime cluster, wiring/fuse/cable math, honest post-ITC cost framing, corrections/methodology trust layer.

**Gaps the site can own that competitors don't (ranked by evidence strength):**
1. **Canonical decision pages for the forum's biggest recurring questions** — wire gauge, fuse sizing, MPPT-not-charging, 12/24/48V, controller voltage windows. Evidence: 21.6K beginner threads vs 14 FAQ threads on diysolarforum (FACT); forum-dominated SERPs (FACT). The format: symptom→cause→fix + embedded calculator + NEC citations.
2. **Measured-methodology appliance-runtime matrix** — runtime per load built from public EnergyGuide data + stated duty-cycle ranges, math shown. Current SERP: factory blogs ("By admin") and one decent 660-word small site (backuppowerexplained.com, FACT). Nobody publishes per-appliance ranges with disclosed assumptions.
3. **CPAP backup planner grounded in manufacturer spec sheets** — runtime by machine class and humidifier setting. SERP is 100% commerce sites, no clinical grounding (FACT composition). Medical-adjacent care required: no medical claims, cite specs, link clinical authority.
4. **Comparison pages with break-even math instead of "vs" fluff** — MPPT-vs-PWM, LiFePO4-vs-lead-acid (both just upgraded), plus Jackery-vs-EcoFlow class pages done as $/usable-Wh over cycle life. SERPs are 70–90% Reddit (FACT) — Google has no trusted editorial answer.
5. **"Is this quote fair?" homeowner toolkit** — per-watt decoder, dealer-fee explainer, $0-install scam decoder. Directly evidenced by recurring r/solar threads (FACT quotes). Not directly Amazon-monetizable; builds the trust and topical authority that lifts everything else.
6. **Standalone calculator pages** — wire-size, cable-size, tilt-angle as dedicated tool URLs (small tools demonstrably rank #1–2 in their SERPs, FACT). The site has the JS; most pages bury tools inside articles.
7. **Winter/worst-week sizing reality guides** — the forum's top active thread is literally "Quit designing solar setups that inherently need a generator in winter!" (FACT). Nobody writes worst-week math.

**Positioning statement (INFERENCE/synthesis):** *"The written, neutral decision layer between the forums and the testing channels: show the arithmetic, cite the code, admit what we don't know, link to Amazon only where the math ends at a product."*

---

## 5. Prioritized Opportunity List

| # | Opportunity | Impact | Effort | Urgency | Confidence | Basis |
|---|---|---|---|---|---|---|
| 1 | Troubleshooting/decision hub: upgrade existing winners + add inverter-shutting-off, battery-not-charging, low-output canonical pages with embedded calculators | **High** | Low–Med | **High** | **High** | Only proven traffic class; SERPs 80–90% forum with zero editorial (FACT) |
| 2 | Appliance-runtime matrix + runtime calculators; monetize CPAP/fridge/100Ah pages with compliant product boxes | **High** | Med | **High** | **High** | Weak SERP competition verified by fetch (FACT); pure Amazon fit |
| 3 | Standalone calculator pages (wire size, cable size, tilt angle) as tool URLs + worked NEC examples | **High** | Med | Med | **High** | Small tools rank #1–2 in captured SERPs (FACT) |
| 4 | Comparison keystones with break-even math (extend mppt-vs-pwm/li-ion pattern; add Jackery-vs-EcoFlow as math, not roundup) | Med–High | Med | Med | **High** | Forum-dominated SERPs (FACT); pages just proven site-upgradeable |
| 5 | Publish selection & testing methodology page ("what we own, what we don't, how picks are made") + honest authors page | **High** | **Low** | **High** | **High** | SolarReviews-style transparency adapted truthfully; FTC-aligned; differentiates from review-unit blogs |
| 6 | "Quote fairness" homeowner toolkit (per-watt decoder, scam decoder) | Med | Med | Med | Med | Strong thread evidence (FACT); indirect monetization |
| 7 | Reposition state-cost guides: sizing + incentives math, link out to price data; stop competing on price tables | Med | Med | Low | Med | EnergySage data-lock (FACT); avoids unwinnable fight |
| 8 | DIY Project Lab: firsthand build documentation with measured results ("we measured X W at Y head") + build photos | Med | High | Med | **High** | Only honest E-E-A-T moat available; cluster already earns traffic |
| 9 | Verify Amazon OneLink / multi-marketplace for EU traffic (~40% of sessions) | Med | **Low** | Med | Med | Traffic share (FACT, internal); program rules NEEDS VERIFICATION |
| 10 | Component roundup program (controllers, monitors, LiFePO4 100Ah class) with disclosed criteria; never big-ticket "best solar generator" | Med | Med | Low | **High** | Small sites proven ranking in component SERPs (FACT); tested-media lock avoided |

**Explicitly rejected (ethics/compliance):** fabricated "hands-on tested" claims; scraping competitor tables/rankings; fake urgency; price tables with hardcoded Amazon prices (OA-violating, verified); incentivized clicks.

---

## 6. 30-Day Competitive Differentiation Plan

**Week 1 — Trust spine + quick wins (mostly done or cheap):**
- Publish the selection/methodology page: what the site is, what we own vs. don't, how picks are made, how math is checked, correction policy (links to existing corrections log). (Opp. 5; ~1 day)
- Add compliant product boxes to CPAP, fridge-generator, 100Ah, phone-charger, yard-lights pages — after each page's math section, never before it. (Opp. 2 partial; ~1 day)
- Verify OneLink applicability in Associates Central; if eligible, enable. (Opp. 9; ~1 hour + verification)
- Confirm disclosure banner pattern on all monetized pages (site-standard already; spot-check after new boxes).

**Week 2 — Troubleshooting/decision hub (Opp. 1):**
- Upgrade the three existing troubleshooting winners with embedded decision-tree calculators (fuse sizing, voltage-drop, LVD thresholds).
- Publish the missing canonical: "Inverter keeps shutting off — complete diagnostic" as symptom→cause→fix with math (currently 0 editorial competitors in captured SERP, FACT).
- Wire the troubleshooting triangle links (done in part; complete cross-linking).

**Week 3 — Runtime matrix + calculators (Opp. 2+3):**
- Build the appliance-runtime reference: 15–20 loads, EnergyGuide-derived, assumptions stated, runtime calculator embedded.
- Split the wire-size and cable-size calculators into standalone tool pages with worked NEC examples; interlink articles→tools→articles.

**Week 4 — Comparisons + measurement begins (Opp. 4+8):**
- Ship one new math-first comparison (Jackery vs EcoFlow as $/usable-Wh over cycle life — or generator-class vs build-your-own) with zero "best" claims.
- Start the first firsthand build log in Project Lab (any owned equipment; publish real measured numbers and photos; label honestly).
- Measure: Search Console impressions on the new/changed classes; Rybbit (bot-filtered) on the upgraded pages; first Amazon clicks by page from Associates reports.

**KPIs at day 30:** GSC impressions on troubleshooting/tool/runtime queries (leading indicator); associate click-through by page class; 3+ new canonical decision pages indexed.

---

## Compliance notes & verification list
- **Verified 2026-09-05** (live pages): OA pricing rule (Amazon-served or PA API + disclaimer + timestamp; no price tracking/alerting), required Associates statement, no link cloaking/redirect masking, no paid traffic to Amazon links, offline/email link prohibition (opt-in exception), FTC endorsement-guides FAQ (disclosure adjacency; "affiliate link" alone insufficient).
- **Needs verification ( Associates Central, login-walled):** per-page disclosure wording expectations beyond the OA statement; current commission-rate table for the relevant categories (electronics/home/tools); OneLink/multi-marketplace enrollment terms; any 2025–2026 program-change notices.
- **Site-specific rule going forward:** category price bands in cost guides are fine; never a specific "$X" attached to a specific ASIN unless API-served; keep the "check current price" pattern everywhere.

## Assumptions & limitations
- SERP compositions come from independent indexes (Brave/DDG Lite) as Google proxies; validate winnable classes against Search Console impressions after publishing.
- Reddit/Quora direct fetches were bot-walled during research; audience quotes are indexed snippets (cited), and cabin/maker segments rest on inference from forum structure — a logged-in manual pass would upgrade that evidence.
- No competitor traffic/metrics are cited anywhere (not verifiable without paid tools); YouTube/subscriber counts are platform-public.
