# Sitewide SEO & Keyword-Opportunity Audit — solarpoweredproject.com

**Date:** 2026-09-05 · **Prepared by:** Agency (Boss-integrated) · **Scope:** all 141 built pages (134 in sitemap), US/English, solar + off-grid/DIY niche, Amazon Associates monetization (tag `slrpwp-20`)

---

## Method, data sources & limitations

**Evidence used:** a scripted full crawl of the current build (commit `07b7e87`: titles, meta descriptions, H1/H2s, word counts, affiliate-link counts, internal-link graph for every page); Rybbit analytics Jan 1 – Sep 5, 2026 (1,915 pageviews across 99 URLs); live SERP research on 37 keywords by three parallel research seats (every observation dated and engine-labeled, full row-level evidence in `reports/seo-audit-evidence/kw-problem-solution.md`, `kw-tools-wiring.md`, `kw-buyer-seasonal.md`, page inventory in `inventory-factsheet.tsv`); the prior market-research SERP captures (`market-research/serp-patterns.md`, same date).

**Limitations, stated plainly:**
- **No Google Search Console, no GA query data, no commercial keyword tools.** Therefore no numeric search volumes or KD scores appear anywhere in this report — nothing is invented. Demand is inferred from our own DDG-proven pageviews and from SERP composition (forum activity, PAA boxes); difficulty is a qualitative Low/Med/High judged from actually-fetched SERPs.
- **Search-engine access was degraded this date.** The seats' `web_search` tool and Bing HTML returned unrelated/navigational results on most queries (documented per-row in the evidence files). Working channels: **Brave HTML** and **Marginalia** (non-commercial index — ratings marked `Low*` are floor estimates that may be Medium in Google). Two of the seats' headline claims were independently re-verified by the Boss with direct Brave fetches and matched domain-for-domain.
- **Traffic is DuckDuckGo-skewed and bot-noisy.** Google sent ~9 visits all year (vs DDG ~209) because Hostinger's firewall serves 403 challenge pages to Googlebot/bingbot — content-audit issue **C1**, still the site's #1 blocker. ~75.7% of analytics events are bots; pageviews with ~100% bounce + ~0s engagement may be bot-inflated.
- Google-native features (AI Overviews, Google shopping carousels, PAA in Google) are not directly observable from Brave/Marginalia; feature notes reflect what the captured engines actually showed.

**Priority-score formula (used in the matrix):** `Priority = 1 + Winnability + Demand + Monetization-fit + Effort-bonus`, where Winnability Low=4 / Low* =3 / Med=2 / High=0; Demand = 2 if the target page/family already earns ≥8 pv YTD, 1 if SERP shows forum/UGC demand blocks, else 0; Monetization-fit = 2 direct component/accessory path, 1 hub/indirect, 0 informational; Effort-bonus = 1 for improving an existing URL, 0 for a new page. Max 10.

---

## 1. SEO health summary

**Verdict: technically clean, structurally sound, with one external blocker and a handful of precise on-page defects. The site's problem is not health — it's distribution and Google access.**

### 1.1 Site structure & topical clusters (analysis area 1 & 8)

126 content pages across four sections, already forming six working clusters plus two under-built ones:

| Cluster | Pages | Anchor assets | State |
|---|---|---|---|
| Sizing & calculators | ~10 | system-sizing (73 pv, 20% bounce), panel-output, battery-capacity (7.5% bounce), inverter-sizing, payback, angle | **Strongest cluster.** Calculators bounce 6–33% vs ~80% sitewide |
| Wiring & protection | ~8 | battery-cable-size (**104 pv, #2 page**), fuse-sizing (58 pv), wire-size, fuses-vs-breakers, comber box | Proven demand, zero interactive tools on any of them |
| Troubleshooting | 5 | mppt-not-charging (60 pv), battery-not-charging (45), inverter-shutting-off (41), output-troubleshooting | Proven demand; SERPs have near-zero editorial competition |
| DIY generation (18 pages) | 18 | hand-crank (78 pv), flywheel (65), TEG, pelton, stirling… | **Near-closed silo** — links almost only within itself |
| Costs & state guides | ~18 | system-costs (47 pv), 10 state guides, battery-cost, cost-per-watt | 4 of 10 state guides still thin-templated |
| Buyer/comparison | ~15 | pure-sine-vs-modified (42 pv), best-mppt, best-batteries, generator hub | Weakest distribution: several 0-pv monetized pages |
| **Appliance runtime (emerging)** | 3 | fridge-generator page, 100Ah page, CPAP guide (76 inlinks) | The clearest white space (matrix rows 5, 9, 21, 28) |
| **Seasonal/outage (emerging)** | ~2 | battery-backup-vs-generator, generator hub | Unbuilt; two winnable seasonal windows (matrix rows 14–15) |

### 1.2 Page-type inventory (analysis area 2)

- **Buying guides / roundups:** ~6 ("best MPPT controllers", "best batteries 2026"…) — honest spec-table style, but 0–8 pv each; distribution-starved, and head "best" SERPs are locked (per market research + this audit's rows 29–34).
- **Product roundups vs individual reviews:** no individual product review pages exist — correctly so for a no-testing site; the honest substitute is the spec/math comparison (rows 22, 26–27).
- **Comparisons:** strong suit (pure-sine 42 pv; 12v/24v/48v 70 pv; mppt-vs-pwm 14% bounce) and the comparison SERPs are forum-dominated with no trusted editorial — the site's format advantage.
- **Informational/how-to:** the bulk of /pages/; healthy, answer-first house style.
- **Calculators/tools:** 6 interactive — the stickiest pages on the site; the roadmap adds 4 more (cable, fuse, controller, wire).
- **Hubs:** /pages.html, /guides.html, DIY index + topic hubs (solar-basics, components, use-cases, wiring-decisions). Two hubs (use-cases: 1 inlink; components: 3) are effectively unreachable.

### 1.3 Technical & on-page findings

**Solid (verified in build):** unique meta descriptions on all content pages; self-canonicals everywhere plus two deliberate consolidation canonicals (working); 134-URL sitemap; clean robots.txt; FAQPage schema sitewide; noindex'd alias stubs for legacy URLs; mobile table overflow handled; no orphaned content pages; home properly linked from nav.

**Defects found this pass:**

| # | Finding | Scope | Fix effort |
|---|---|---|---|
| H1 | 29 pages render **two "Table of contents" H2s** (body heading collides with the sidebar TOC partial, which fires >800 words) | DIY section + 9 /pages/ | 1 template tweak + strip body headings |
| H2 | `solar-panel-angle-calculator`: vague title, jargon-first description, 100% bounce on 10 pv despite a working calculator | 1 page | Title/desc/intent rewrite |
| H3 | 4 thin templated state guides (AZ 869w, FL 837w, NY 851w, TX 1,109w vs de-templated CO/NJ at 1,800–2,400w) | 4 pages | De-template (as done for CO/IL/MA/NV/NJ) |
| H4 | Three-page "best solar panels" family, 0–1 pv each, same intent (cannibalization §3) | 3 pages | Canonicals |
| H5 | 13 traffic-winning pages have ≤2 internal inlinks; DIY silo barely links to /pages/ money cluster | ~30 pages | §4 link sweep |
| H6 | ~10 DIY core titles run 75–84 chars (mid-phrase truncation risk); keyword-first otherwise | 10 pages | Low priority |
| H7 | Four monetized pages at literally 0 pv (best-panels-for-small-homes, best-panels-for-home-2026, yard-lights, BMS-explained) | 4 pages | Distribution, not content |

**External blocker (unchanged, still #0):** Hostinger firewall 403-challenges Googlebot/bingbot. Every Google-side projection below assumes it's fixed (hPanel rule or support ticket), then sitemap resubmitted in Search Console.

### 1.4 SERP features & CTR considerations (analysis area 7)

From 37 fetched SERPs + the prior captures, consistent patterns:

- **People-Also-Ask boxes appear on nearly every troubleshooting and sizing query** → the site's answer-first "In brief" blocks and FAQ shortcodes are already snippet/PAA-shaped; keep question-form H2s.
- **Reddit/forum "Discussions" blocks appear on almost everything** — Google is using UGC as its trust proxy in this niche. Implication: our pages should cite/engage the real-world numbers forums provide (honest "here's what owners report") without scraping.
- **Video carousels dominate physical how-to's** (MC4 crimping, panel testing) → text-first pages can't win those; that's why row 25 (MC4) is deferred.
- **Shopping carousels lock transactional "best/kit" queries** (rows 29–33) → never build roundup/kit-list pages against them; the winnable layer is always the math/sizing question underneath.
- **Featured-snippet shapes worth targeting:** the chart/table formats (rows 20, 12) and the yes/no decision questions (row 18) — concise 40–60-word direct answers under question H2s.

---

## 2. Keyword opportunity matrix

37 keywords researched live on 2026-09-05, merged and scored (formula above). Full SERP evidence per row lives in the three seat files under `reports/seo-audit-evidence/`. `Low*` = Marginalia floor estimate, may be Medium in Google.

| # | Keyword / topic | Intent | Funnel | Difficulty | Business relevance | Recommended page type | Existing URL to improve / new page | Priority |
|---|---|---|---|---|---|---|---|---|
| 1 | mppt charge controller no output | problem-solving | MOFU→BOFU | Low | High — repair-or-replace ends in a purchase | Troubleshooting decision-tree expansion | improve /pages/mppt-charge-controller-not-charging.html | **10** |
| 2 | battery cable size calculator | problem-solving (tool) | MOFU | Low* | High — exact component purchase follows the sizing | Guide + embedded calculator | improve /pages/battery-cable-size-for-inverter.html | **9** |
| 3 | solar fuse size calculator | problem-solving (tool) | MOFU | Low* | High — fuses/breakers sized then bought | Guide + embedded calculator | improve /pages/solar-fuse-and-breaker-sizing.html | **9** |
| 4 | inverter low voltage alarm keeps beeping | problem-solving | MOFU→BOFU | Low | Med-High — precursor symptom, cable/upgrade path | Troubleshooting section | improve /pages/inverter-keeps-shutting-off-troubleshooting.html | **9** |
| 5 | how long will a 200ah battery run a refrigerator | runtime math | MOFU | Low | Med — formula content, battery-path indirect | Worked example | improve /pages/how-long-will-100ah-battery-run.html | **9** |
| 6 | 12v vs 24v solar system (pick-your-voltage) | comparison | MOFU | Low* | High — voltage choice drives whole parts list | Comparison + mini-calculator | improve /pages/12v-vs-24v-vs-48v-solar.html | **9** |
| 7 | solar panel not charging battery | problem-solving | MOFU→BOFU | Low | Med-High — panel-side diagnosis | Troubleshooting expansion | improve /pages/solar-battery-not-charging-troubleshooting.html | **9** |
| 8 | jackery cpap how long | runtime math (brand) | MOFU | Low | High — power-station runtime decision | Runtime section | improve /pages/cpap-battery-backup-guide.html | **9** |
| 9 | what size battery to run a chest freezer | problem-solving→commercial | MOFU | Low | High — battery sizing → battery purchase | Runtime/sizing guide | NEW /pages/what-size-battery-run-chest-freezer.html | **8** |
| 10 | solar wire size calculator | problem-solving (tool) | MOFU | Low* | Med-High — wire purchase follows gauge answer | Guide + embedded calculator | improve /pages/solar-wire-size.html | **8** |
| 11 | what size wire for 100w solar panel | problem-solving | TOFU→MOFU | Low* | High — first-array wire purchase | Worked example block | improve /pages/solar-wire-size.html | **8** |
| 12 | charge controller sizing calculator (+100/200/400W examples) | problem-solving (tool) | MOFU→BOFU | Low* | High — controllers are a core Amazon component | Guide + embedded calculator | NEW /pages/charge-controller-sizing.html | **7** |
| 13 | battery drains overnight off grid | problem-solving | MOFU | Low | Med — diagnosis page, replacement path indirect | Symptom→diagnosis guide | NEW /pages/battery-drains-overnight-off-grid.html | **7** |
| 14 | solar generator for hurricane season | seasonal commercial | MOFU→BOFU | Med | High — power-station buyers pre-season | Hub seasonal section | improve /pages/solar-generator.html | **7** |
| 15 | winter storm backup power | seasonal commercial | MOFU→BOFU | Med | High — same buyer pool, opposite season | Hub seasonal section (winter) | improve /pages/solar-generator.html | **7** |
| 16 | solar kit for shed | commercial | MOFU | Med | High — kit vs components purchase decision | Buyer guide refresh | improve /pages/solar-panels-for-sheds.html | **7** |
| 17 | solar panel series vs parallel which is better | comparison | MOFU | Low* | Med — wiring decision, components indirect | Decision-first rewrite | improve /pages/solar-panels-series-vs-parallel.html | **7** |
| 18 | do i need a fuse between solar panel and charge controller | problem-solving (yes/no) | MOFU | Low* | Med — fuse purchase if yes | Decision section | improve /pages/solar-fuses-vs-breakers.html | **7** |
| 19 | 48v off grid system wiring | problem-solving build guide | MOFU→BOFU | Low* | High — committed builder, big parts list | Wiring guide | NEW /pages/48v-off-grid-wiring-guide.html | **7** |
| 20 | inverter cable size chart | problem-solving (reference) | MOFU | Low* | High — chart + cable purchase | Chart page + mini-calc | NEW /pages/inverter-cable-size-chart.html | **7** |
| 21 | mini split watts off grid (battery runtime) | runtime math | MOFU | Low | Med — inverter/battery sizing follows | Runtime math guide | NEW /pages/mini-split-watts-off-grid.html | **7** |
| 22 | lifepo4 100ah battery which brand | comparison | MOFU→BOFU | Med | High — direct battery brand decision | Spec/math comparison (no testing claims) | NEW /guides/lifepo4-100ah-brand-comparison.html | **6** |
| 23 | solar panel stopped working troubleshooting | problem-solving | MOFU | Med | Med — dead-panel diagnosis branch | Troubleshooting expansion | improve /pages/solar-output-troubleshooting.html | **6** |
| 24 | battery backup for oxygen concentrator | safety-critical sizing | MOFU→BOFU | Med | High monetization; medical-safety caveats required | Sizing/safety guide | NEW /pages/battery-backup-oxygen-concentrator.html | **6** |
| 25 | mc4 connectors wiring guide | informational how-to | TOFU→MOFU | Med | High — crimpers/connectors/PV wire | Step-by-step guide (needs photos) | NEW /pages/mc4-connectors-wiring-guide.html | **6** |
| 26 | jackery vs ecoflow | comparison | MOFU | Med | High — but "which is better" needs testing we can't claim | Spec/math comparison | NEW /guides/jackery-vs-ecoflow-spec-math.html | **6** |
| 27 | bluetti vs jackery 2000 | comparison | MOFU | Med | High — same constraint | Capacity-class math | NEW /guides/bluetti-vs-jackery-2000-wh-class.html | **6** |
| 28 | will a 100 watt solar panel run a refrigerator | runtime math | MOFU | Med | Med — panel+battery sizing | Runtime math guide | NEW /pages/will-100-watt-solar-panel-run-refrigerator.html | **5** |
| 29 | cpap battery for camping | commercial | BOFU | High | High — but shopping-carousel locked | Info section (never a roundup) | improve /pages/cpap-battery-backup-guide.html | **5** |
| 30 | best power station for cpap | commercial roundup | BOFU | High | High — roundup format dishonest for us | (skip roundup; deepen sizing) | improve /pages/cpap-battery-backup-guide.html | **5** |
| 31 | solar generator for well pump | commercial sizing | MOFU→BOFU | High | High — but brand-blog + shopping lock | Sizing guide (later, surge-math depth) | NEW /pages/solar-generator-well-pump-sizing.html | **4** |
| 32 | power outage preparedness solar | seasonal informational | TOFU→MOFU | High | Low-Med — manufacturer-dominated | Checklist section | improve /pages/solar-battery-backup-vs-generator.html | **4** |
| 33 | 100w solar panel kit for rv | transactional | BOFU | High | Med — "what 100W actually runs" math | Expectation-math section | improve /pages/rv-solar-sizing.html | **4** |
| 34 | anker solix vs jackery | comparison | MOFU | High | High — pure brand lock in both engines | (skip) | — | **4** |
| 35 | is solar worth it in arizona | local commercial | MOFU | High | Med — via existing guide only | Payback/decision section | improve /guides/solar-panel-cost-arizona.html | **3** |
| 36 | solar panels texas worth it | local commercial | MOFU | High | Med — via existing guide only | ERCOT buyback framing | improve /guides/solar-panel-cost-texas.html | **3** |
| 37 | net metering california 2026 | local policy | MOFU | High | Low — freshness war we can't responsibly win | CA support section only | improve /pages/net-metering-by-state-2026.html | **2** |

### 2.1 Low-competition, high-intent keywords (analysis area 9)

The realistic shortlist for a growing no-testing affiliate site — every one is a **Low/Low\*** difficulty row whose SERP is forums + small tools with **no editorial authority**, and every one sits a step away from a component purchase:

1. mppt controller no output / battery not charging / inverter alarm (rows 1, 4, 7) — symptom pages that end in a replacement purchase
2. cable/fuse/wire **calculator** intents (rows 2, 3, 10, 11, 12) — the sizing answer IS the purchase spec
3. appliance runtime math (rows 5, 9, 21) — "will it run X" Wh-math nobody does honestly
4. battery-drains-overnight (row 13) — zero editorial competition at all

---

## 3. Keyword cannibalization & consolidation report

**Already consolidated (verified in the live build — listed for completeness):** `/pages/solar-panel-cost-california` → canonical → `/guides/solar-panel-cost-california`; `/guides/solar-battery-cost-2026` → canonical → `/pages/solar-battery-cost-2026`.

| Risk | Pages | Evidence | Action |
|---|---|---|---|
| **CRITICAL — "best solar panels" 3-way split** | best-solar-panels-for-home-2026 (1,329w) · for-small-homes (1,273w) · small-roof (2,142w) | Same intent (limited-space high-efficiency panels); **0–1 pv each**; all three monetized; head "best panels" SERPs locked by tested media | Keep **small-roof** (deepest); set canonicals on the other two → small-roof; retitle keeper "Best Solar Panels for Small Roofs & Small Homes (2026 Specs Compared)"; merge tiny-house angles in. URLs unchanged |
| **HIGH — system-voltage pair** | how-to-choose-solar-system-voltage (660w) · 12v-vs-24v-vs-48v (1,721w, 70 pv) | Titles both contain "(12V vs 24V vs 48V)"; thin page adds only a cable-run rule | Merge unique bits into the 70-pv winner; **canonical thin → winner**. Seat B independently reached the same conclusion |
| **MEDIUM — tilt/angle pair** | solar-panel-tilt-and-orientation (2,961w) · solar-panel-angle-calculator (2,006w + tool) | Both walk the same latitude-formula content | Keep both, **divide the intent**: calculator owns "what angle/calculator" (fix title/desc, H2 issue); explainer owns azimuth/orientation/roof-pitch; strip duplicated formula section; prominent two-way links |
| **MEDIUM — context-sizing trios (benign, keep)** | system/rv/cabin sizing; system/rv/cabin costs | Same method, different searcher context; each context-anchored | Keep all; funnel each to the shared calculator; cross-link as siblings |
| **BENIGN — 10-state cost series** | guides/solar-panel-cost-{10 states} | Intra-series title overlap is the geography modifier working as designed | No consolidation. Real risk = the 4 thin templated members (H3) reading as mass-produced → de-template |
| **WATCH (distinct today — keep separated + cross-link)** | battery-not-charging vs mppt-not-charging; fuse-sizing vs fuses-vs-breakers; cable-size vs wire-size; inverter-sizing vs choose-inverter | Different failure layers / how-to-size vs which-type / different circuits / math vs selection | Monitor in Search Console impressions post-C1-fix; merge only if one consistently outranks the other for its sibling's query |

---

## 4. Internal-linking recommendations

Principles: feed DDG-proven winners (they're verified demand), open the DIY silo, and route equity to monetized pages from adjacent winners. All in-body contextual links (the house "Next logical reads" pattern), never footer link farms.

**A. Feed the traffic winners** (13 pages at ≤2 inlinks — highest-leverage link targets on the site):

| Source pages | Target (pv · current inlinks) | Anchor-text theme | User value |
|---|---|---|---|
| solar-generator hub, cpap guide, backup-vs-generator | hand-crank (78 · 2) | "realistic hand-crank charging math" | emergency-charging sizing |
| battery-capacity, supercapacitor, li-ion-vs-lead-acid | flywheel (65 · 1) | "flywheel storage physics" | storage alternatives |
| battery-not-charging, mppt-not-charging, inverter-sizing | inverter-shutting-off (41 · 2) | "inverter shutdown causes" | symptom→symptom path |
| micro-hydro-basics, water-wheel, use-cases | pelton (37 · 2) | "pelton runner build" | hydro how-to |
| rv-solar-sizing, cabin-solar-cost, use-cases | rv-solar-cost (33 · 2) | "RV solar price breakdown" | cost research |
| small-wind, panels-vs-wind | savonius (24 · 1) | "VAWT realistic output" | wind DIY |
| wind + hydro pages | dump-load (24 · 1) | "diversion load protection" | safety |
| battery pages | supercapacitor (15 · 1) | "supercap buffer" | experiments |
| solar-output, angle-calculator | panels-vs-wind (11 · 2) | "solar vs wind for off-grid" | generation choice |

**B. Route equity to monetized pages:**

| Source (winner) | Target (monetized, starved) | Anchor-text theme | User value |
|---|---|---|---|
| mppt-not-charging (60 pv) | best-mppt-charge-controllers (8 pv, 1 inlink) | "controllers without this failure mode — spec table" | repair-or-replace decision |
| inverter-shutting-off (41) + pure-sine (42) | how-to-choose-solar-inverter (3 pv) | "inverter selection by surge & waveform" | replacement shopping |
| system-costs (47) + payback-calculator | all 10 state guides | "your state's cost picture" | local cost check |
| solar-basics + components hubs | yard-lights, phone-charger, portable-panels | "small-solar buying guides" | entry purchases |
| battery-not-charging (45) | best-solar-batteries-2026 | "if the battery is the failure" | replacement path |
| li-ion-vs-lead-acid, battery-capacity | BMS-explained (0 pv) | "when you need an external BMS" | battery-build safety |
| 12v-vs-24v (70) | battery-cable-size + fuse-sizing | "parts that match your voltage" | build shopping list |

**C. Open the DIY silo:** each top DIY page adds 1–2 contextual links into the /pages/ cluster (hand-crank/pedal/treadmill/alternator → 100Ah-runtime + battery-capacity; TEG/stirling → panel-output; flywheel/supercap/gravity → battery-capacity + li-ion-vs-lead-acid; pelton/water-wheel/micro-hydro → system-sizing calculator; wind pages → dump-load + fuse-sizing) — and the target pages link back where relevant.

**D. Make hubs reachable:** solar-use-cases (45 outlinks, 1 inlink) and solar-components (52 outlinks, 3 inlinks) get linked from solar-basics' next-steps block and from the top calculators.

**E. Mesh the state cluster:** net-metering-by-state ↔ each state guide; state guides ↔ payback-calculator; each state guide → the two nearest states.

---

## 5. Prioritized 90-day SEO roadmap

**Days 0–15 — unblock + on-page hygiene (no new content)**
1. C1 firewall fix (user-side, hPanel) → verify with a Googlebot-UA curl → resubmit sitemap in Search Console. *Everything below compounds only after this.*
2. Canonicals: best-panels ×2 → small-roof; system-voltage → 12v-vs-24v (§3). Retitle small-roof.
3. Angle-calculator title/desc/intent rewrite (H2); TOC double-H2 fix (H1, template + 29 files).
4. Internal-link sweep A + D (winners + hubs) — pure additions, ~1 day.

**Days 15–45 — upgrade proven winners (improve-only, highest ROI)**
5. Embed calculators: cable-size (row 2), fuse-sizing (row 3), wire-size + 100W example (rows 10–11) — reuse the house `toolscript` pattern.
6. Troubleshooting expansions: mppt no-output branches (row 1), panel-side causes on battery-not-charging (row 7), inverter-alarm section (row 4), dead-panel branch (row 23).
7. 12v-vs-24v decision rewrite + mini-calculator (row 6); CPAP runtime/camping sections (rows 8–9 of seat file: runtime math, TSA limits).
8. 200Ah fridge worked example on the 100Ah page (row 5).

**Days 45–75 — build the white space (new pages, one cluster at a time)**
9. Appliance-runtime cluster: chest-freezer battery (row 9), then mini-split off-grid (row 21), then 100W-fridge (row 28) — cross-linked with the fridge/100Ah/CPAP trio.
10. Charge-controller sizing page + calculator (row 12) with 100/200/400W worked examples.
11. battery-drains-overnight (row 13).
12. Seasonal: hurricane section on the generator hub (row 14 — if within season); schedule winter section (row 15) for an Oct refresh.

**Days 75–90 — second wave + authority**
13. De-template the 4 thin state guides (H3) with EIA-cited rates (pattern already proven on CO/NJ).
14. LiFePO4 100Ah brand spec-comparison (row 22) — strict no-testing-claims format.
15. Second-wave tools: 48V wiring guide (row 19), inverter cable chart (row 20); internal-link sweep B/C/E.
16. Re-pull Rybbit + (once C1 fixed) Search Console impressions; re-validate the `Low*` difficulty rows; adjust the deferred list (rows 26–27) accordingly.

Throughout: every new/edited page ships the disclosure banner, FAQ schema where it has real FAQs, and 2–4 internal links in/out. No page publishes without a genuinely useful answer in the first 100 words.

---

## 6. The 10 highest-leverage SEO actions, in order

1. **Fix the Hostinger bot firewall (C1) and resubmit the sitemap** — the entire Google side of this audit is gated on it (user action, then everything else compounds).
2. **Canonical the "best solar panels" trio and the system-voltage pair** (4 front-matter lines + 1 retitle) — ends the site's only real cannibalization.
3. **Embed a cable-size calculator in battery-cable-size-for-inverter** — the #2 traffic page (104 pv), static today, and calculators are the site's stickiest format (7.5–33% bounce).
4. **Embed the fuse-sizing calculator** (58 pv, 91% bounce) — same pattern, same payoff.
5. **Expand mppt-not-charging with the "no output" decision tree** — Priority-10 row; the SERP has zero editorial competition.
6. **Run the internal-link sweep A+D** (feed the 13 starved winners + 2 hubs) — a day of work, pure equity routing to DDG-proven pages.
7. **Build the chest-freezer battery-sizing page** — the flagship of the appliance-runtime white space; forum-only SERP; direct battery-purchase path.
8. **Add the 200Ah fridge worked example + CPAP runtime sections** — improves two high-inlink pages for an hour each.
9. **Ship the charge-controller sizing calculator page** — wins a whole "what size controller for X watts" family with one URL.
10. **Rewrite the angle-calculator title/description and fix the double-TOC headings** — cleans the two sitewide on-page defects found this pass.

---

*Ethics & compliance: no fabricated metrics anywhere (no volumes/KD invented — all difficulty is SERP-evidenced and dated); no keyword stuffing, doorway pages, or spun content recommended; no "best/testing" claims a no-testing site can't substantiate; shopping-carousel-locked roundup queries are explicitly skip-listed; all Amazon-related recommendations are link-only with existing disclosure banners — prices/availability stay on Amazon. Two medical-adjacent topics (oxygen concentrator) carry verification caveats before monetization.*
