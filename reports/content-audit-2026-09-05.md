# Solar Powered Project — Full Content Audit
**Date:** 2026-09-05 · **Scope:** all 132 content pages + theme/UX/trust layer · **Method:** 5 parallel agency audit passes (A: electrical/battery, B: money/MPPT/safety, C: panels/costs/use-cases, D: DIY cluster + state guides, E: trust/UX) merged and independently re-verified against a fresh Hugo build, live-site probes, and the Rybbit API.
**Constraints honored:** no URL/slug changes, no page removals. Additions and in-place improvements only.
**Full page-by-page table:** [page-audit-table.md](page-audit-table.md)

---

## 1. Executive Summary

**Strongest assets.**
1. **A genuine two-tier quality split with a strong top tier.** The August 2026 content wave (solar-installation-safety-guide, battery-enclosure/maintenance guides, solar-panel-shading-effects, inverter-sizing, the four new appliance articles) is legitimately good: real numbers, NEC references, inline photos, honest math, working inline calculators. 21 pages rate KEEP (Q≥7).
2. **Working interactive tools** — inline calculators on sizing/output/payback/battery-capacity pages, functional in the current build. This matches where the site's real traffic lives (symptom/decision queries).
3. **A clean technical base** — canonicals, OG/Twitter cards, FAQPage JSON-LD (64 pages), breadcrumbs, webp heroes, lazy-loading, an honest corrections/methodology layer, and a centralized affiliate tag (now `slrpwp-20`, swapped and deployed during this audit).
4. **The DIY "Project Lab" cluster** — evergreen physics content (P=9.81·H·Q etc.) and the only cluster showing fresh organic life (Bing/DDG): pelton 24pv, pedal 19, TEG 18, hand-crank 53 all-time.

**Biggest content-quality risks.**
1. **~40% of the library is a May-2026 machine-generated cohort with visible defects**: 12 pages render a literal `FAQHAHAHUGOSHORTCODE…` garbage TOC anchor, 4 pages render their core comparison table as inline-code (backtick-wrapped markdown), one page ships a Chinese character mid-sentence (`solar-generator.md:19` "Wh需求"), several ship truncated headings ("Key Take", "ical considerations", "able Strategies") and corrupted economics text ("1ne 15% to 17%", "$able $3.00 per watt"). This is the exact "unedited AI output" pattern Google's helpful-content systems and readers punish.
2. **Factually wrong money claims still live on 3 pages** (federal ITC "remains 30% through 2032", "remains at 30% in 2026", payback 6–8yr) contradicting the site's own corrected pages — on its highest-commercial-intent URLs.
3. **Two near-duplicate page pairs** (battery-cost-99%, california-89%) both live, both self-canonical, both in the sitemap.
4. **Anonymous authorship** ("Solar Powered Project" everywhere, authors.md is 80 words and admits no bylines) capping trust for electrical-safety-adjacent, money-decision content.

**Most likely search-visibility blockers (in order).**
1. **Hostinger's browser-verification firewall returned HTTP 403 "Checking your browser… Just a moment" to `Googlebot/2.1`, `bingbot/2.0`, and plain Firefox UAs** during live probes. Google sent **9 visits in 8.5 months** while Bing/DDG (which did index the site) sent 330+. If crawlers are being challenged, nothing else in this report matters until it's fixed.
2. **75.7% of all tracked events last 30 days were bots** (Rybbit bot filter); the June–Aug "traffic collapse" (95–97% bounce, ~0s dwell) is largely bot noise, not readers leaving.
3. Thin/templated cohort dragging sitewide quality signals (see §4).
4. Zero-link and hub-only pages (11 pages reachable only through the /pages hub) plus a recency-based "related posts" module that surfaces arbitrary articles.

**The 5 improvements most likely to create meaningful results.**
1. Fix the crawler 403 challenge in Hostinger (whitelist Googlebot/Bingbot, or disable browser verification) — then request indexing in Search Console.
2. Ship the "mechanical defect sweep" (one afternoon of grep-driven fixes): 12 garbage TOC anchors, 4 broken tables, CJK artifact, truncated headings, corrupted text, 11 missing disclosure banners, 3 stale-ITC pages.
3. Canonicalize the two duplicate pairs via front matter (no URL changes needed).
4. De-thin the 15 EXPAND pages that sit on proven or high-volume intents (li-ion-vs-lead-acid, diy-vs-installer, mppt-vs-pwm, solar-system-costs, solar-maintenance…).
5. Give the DIY cluster a face: build photos/diagrams on the 6 pages with real traffic, generated via magica-media (they are currently 100% imageless).

---

## 2. Critical Issues (severity order)

| # | Severity | Issue | Evidence | Fix |
|---|---|---|---|---|
| C1 | **Blocker** | Hostinger anti-bot serves 403 browser-verification to search crawlers | Live probe: Googlebot & bingbot & Firefox UA → HTTP 403 "Just a moment…" (2,482 bytes, `noindex,nofollow` meta on challenge page); Google=9 visits/8.5mo vs DDG=209 | hPanel → security/DDoS protection: disable browser verification or verified-bot-whitelist Googlebot/Bingbot; re-probe with `curl -A Googlebot`; resubmit sitemap |
| C2 | **Critical** | Factually wrong ITC/payback claims on money pages | `solar-lease-vs-buy-2026.md:139` "ITC remains 30% through 2032 under IRA" contradicts lines 59/64 of same file; savings table subtracts $7,500 credit; `solar-battery-cost-2026.md` FAQ "ensure you qualify for the 30% ITC"; `solar-panel-cost-california.md:14,177,237,336` "credit remains 30%" + 6–8yr payback vs corrected twin's 10–13yr | Rewrite the 3 passages + recompute tables without the credit; matches commit 60666c8 doctrine (P.L. 119-21 expiry) |
| C3 | **Critical** | Duplicate content pairs, both indexed | `/pages/solar-battery-cost-2026.html` ≡ `/guides/solar-battery-cost-2026.html` at 99.1% (5-gram Jaccard .985); California pair 88.9%; both self-canonical, both in sitemap (133 URLs) | Front matter `canonical` on the weaker twin (guides battery → pages; pages california → guides) + differentiate content; zero URL changes |
| C4 | **High** | Visible machine-generation defects on 20+ pages | 12 pages render `FAQHAHAHUGOSHORTCODE…` TOC anchor (built-HTML grep, e.g. `solar-panel-shading-effects.html`, all 6 DIY FAQ pages); backtick tables render as `<code>\|` in backup-vs-generator (9 rows), financing-options (8), lease-vs-buy (12), ground-mount-vs-roof; `solar-generator.md:19` "Wh需求"; `solar-panel-efficiency` "1ne 15%", "$able $3.00"; `solar-panel-angle-calculator.md:16` "## Key Take"; `solar-power-mobile-homes.md:44,114` truncated H2s; `solar-lights-for-yard` "Lithates"; `solar-panel-output-per-square-foot` "100-square-tfoot" | Mechanical sweep (see §7 Fix Immediately); harden the TOC partial to strip shortcode placeholders defensively |
| C5 | **High** | Amazon Associates disclosure inconsistency | 11 pages carry `product-box`/`amazon` links without the top-of-page `{{< affiliate-disclosure >}}` banner (battery-capacity, inverter-keeps-shutting-off, portable-solar-panels, rv-solar-cost, rv-solar-sizing, solar-battery-management-system, solar-components, solar-generator, solar-inverter-sizing, solar-system-costs, solar-system-sizing). Per-box note exists but the site's own standard banner is absent | Add shortcode to all 11, or auto-inject banner in `single.html` when page contains affiliate shortcodes |
| C6 | **High** | Analytics polluted by bots → decisions misinformed | Rybbit last-30d: 2,059 bot events of 2,719 (75.7%); "sessions" 611 @ 93.8% bounce/10.8s are mostly bots; real reader base is ~10 pages ever visited | Enable Rybbit bot filtering as default view; judge pages on the human segment only |
| C7 | **Medium** | `about.md` claims "ad-supported" — AdSense was removed Aug 24 | `about.md` "Advertising and independence" section vs remote commit db31371 (ADR-006 affiliate pivot) | Rewrite section around Associates + honest independence statement |
| C8 | **Medium** | Mobile table overflow | Rendered tables are bare `<table>` (no overflow wrapper in CSS or templates); site is ~40% mobile; cost/state tables are 4–7 columns | Add `overflow-x:auto` wrapper via render hook or small JS; verify on phone |
| C9 | **Medium** | Related-posts module shows 3 most-recent same-section pages — not related content | `layouts/partials/related-posts.html:1` (`first 3 $same`) | Score by shared front-matter keywords or curate per-page "related" lists |
| C10 | **Medium** | `authors.md` is a dead 80-word page, linked from nowhere | Link-graph: 0 inlinks; "bylines shown where available" = none exist | Link from footer globally; make it real (named editor or honest first-person shop voice) |
| C11 | **Low** | 3 dead `[Internal link…](#)` placeholders in `/pages/solar-panel-cost-california.md` | grep | Resolve or remove during C2 rewrite |
| C12 | **Low** | ~10 one-inlink pages (hub-only) | ac-vs-dc-coupled, best-solar-panels-for-home, how-long-do-panels-last, how-much-do-batteries-cost, install-yourself, read-spec-sheet, net-metering-explained, panels-vs-wind, mobile-homes, water-heater | Add 2–3 contextual inlinks each from sibling articles (list in §6) |

**Resolved during this audit:** Amazon tag swapped sitewide `litwd-20` → `slrpwp-20` (hugo.toml + shortcode defaults), verified in a clean build (31 pages carry the tag) and deployed via the standard push→Actions→rsync pipeline (commit `88784aa`). The affiliate machinery is fully centralized — future swaps are a one-line change.

---

## 3. Page-by-Page Audit

Full merged table for all 132 pages: **[reports/page-audit-table.md](page-audit-table.md)** (grouped by cluster, sorted weakest-first within cluster).

**Distribution:** KEEP 21 · IMPROVE 75 · EXPAND 15 · REWRITE 10 · MERGE-CANONICALIZE 3 · NOINDEX 1. Mean quality 6.1/10, mean search-readiness 5.4/10.

**Cluster verdicts:**
- **Core solar library (90 pages)** — the site's spine; bimodal: August-wave pages score 7–9, May-cohort stubs score 1–4. The 15 EXPAND + 10 REWRITE candidates are almost all May cohort. Traffic-winners (battery-cable-size 90pv, 12v-vs-24v-vs-48v 60pv, fuse-sizing 54pv, system-sizing 67pv) are all KEEP/IMPROVE — protect them, link to them harder.
- **State cost guides (11)** — NY/AZ/FL/TX are differentiated (city tables, heroes); **CO/IL/NV/MA/NJ are one skeleton with state names swapped (doorway risk)**. All need state-specific data texture (utility rates by city, local installer market notes, one original data point per state) and cross-links to /pages cost pages instead of duplicating them.
- **DIY / Project Lab (19)** — the site's most original cluster and only source of fresh organic traffic; 100% imageless (no heroes, no body images, zero photos anywhere in 19 build-guides). Highest visual-ROI target on the site.
- **Trust & utility (12)** — mechanism (methodology, corrections, editorial policy) is above-average for an affiliate site; identity (authors, about) is the weak flank; `search.md` (23 words) should be noindexed.

---

## 4. Thin Content & AI-Slop Findings

**Confirmed thin/doorway stubs (EXPAND or REWRITE):**
| Page | Words | Problem |
|---|---|---|
| li-ion-vs-lead-acid | 124 | 3-row "Higher/Lower" table; zero numbers; textbook doorway page |
| solar-use-cases | 154 | five-bullet hub pretending to be an article |
| diy-vs-installer | 154 | same template as above |
| micro-vs-string-inverters | 109 body | 3-row table + links |
| solar-components | 235 | 2 product boxes outweigh 235 words of prose |
| solar-system-costs | 273–502 | thin but 43 all-time pv — proven demand, weakest supply |
| solar-maintenance | 292 | bullet stub |
| mppt-vs-pwm | 336 | symmetric generic table; the site's own cost page duplicates it |
| solar-basics / how-to-choose-system-voltage / wiring-decisions | 417–650 | shells with heroes and descriptions but no substance |
| off-grid-solar-system-setup-guide | 1,283 wc but | "kilowatt-hot (kWh)", "trade-tuffs" typos; templated "imagine the freedom" opener |

**AI-slop patterns found (with the pages that exemplify them):**
1. **Machine-generation debris** — the C4 list; the single most damaging pattern because it's *visible*.
2. **Symmetric Higher/Lower comparison tables** — li-ion-vs-lead-acid, diy-vs-installer, mppt-vs-pwm, micro-vs-string (all May cohort).
3. **Persona/meta leakage** — "the reader is the hero" sentences surviving in solar-fuses-vs-breakers, solar-wire-size, series-vs-parallel; "You're the hero here" in battery-not-charging.
4. **Templated openers/closers** — "Imagine if your meter…", "Pivotal decision", "Harnessing the Sun" H1, "sun is shining" closer, "Welcome to SolarPoweredProject.com" greeting in solar-water-heater.
5. **Unsourced precision** — "90% of cases" (mppt-not-charging), "~60–70% of devices work" (pure-sine), fabricated $/W bands contradicting sibling pages (efficiency vs cost-per-watt).
6. **Empty conclusion + bolt-on product box** — portable-solar-panels and solar-generator end mid-thought at a product box.
7. **State-guide assembly line** — CO/IL/NV/MA/NJ share an 87–103-line skeleton.

**Pages that are genuinely clean (preserve as quality bar):** solar-panel-shading-effects (Q9), solar-installation-safety-guide (9), solar-battery-enclosure-guide (9), solar-battery-maintenance-guide (9), solar-inverter-sizing (9), battery-cable-size-for-inverter (9), what-size-solar-generator-run-refrigerator (8), solar-payback-calculator (8), pure-sine-vs-modified-sine (8), mppt-charge-controller-not-charging (8).

---

## 5. Visual Content Opportunities

Guiding rule: **the site's traffic winners are decision/troubleshooting queries and build guides — both are visual-intent.** 96/128 pages have zero in-body images; the DIY cluster has zero images of any kind. Produce with magica-media; prefer diagrams over photos for electrical content (schematics can be generated accurately; fake product photos cannot — never fake product shots for affiliate pages).

**Priority 1 — DIY cluster (traffic exists, zero visuals):**
- Pelton: nozzle-jet-to-runner diagram + bucket close-up (annotated head/flow) — at the sizing section.
- Hand-crank: photo series of a real crank charger powering a phone + watt-meter reading — at "what to expect" (89.6% bounce page).
- Pedal-power: human-on-bike generator wiring diagram (generator→charge controller→battery) — at the build section.
- TEG: heat-gradient diagram (stove top / TEG module / heatsink) — at the physics section.
- Every DIY page: hero image + one build-progress visual; add `image =` to front matter (theme renders it automatically).

**Priority 2 — electrical decision pages (top traffic):**
- battery-cable-size: voltage-drop bar chart (amps × length → % drop by gauge) near Step 3.
- 12v-vs-24v-vs-48v: current-vs-voltage ampacity chart at the "why higher voltage" section.
- fuse-and-breaker-sizing: one-line electrical diagram with fuse placements per circuit.
- mppt-not-charging + battery-not-charging: symptom→cause decision flowcharts (both pages are checklist-shaped already — a flowchart is the natural medium).
- inverter-keeps-shutting-off: fault-tree flowchart.

**Priority 3 — money pages:**
- lease-vs-buy (after rewrite): 20-year cash-flow chart **recomputed without the ITC**.
- financing-options: monthly cash-flow comparison graphic.
- net-metering-by-state: US map colored by export-rate regime.
- state guides: per-state cost ranges chart + city table (NY/AZ/FL/TX already have heroes; CO/IL/NV/MA/NJ need them).
- battery-cost-2026: price-per-kWh by brand chart (replacing the repeated chart image).

**Priority 4 — concept explainers:** system one-line diagram (solar-basics, solar-components — one asset reused), series-vs-parallel string diagram under shading, bypass-diode schematic (shading page), AC-vs-DC coupling one-liner, sun-path/azimuth diagram (tilt page), degradation curves (how-long / degradation pages).

**Alt-text direction:** describe the electrical relationship, not the picture ("Voltage-drop curve for 3 m cable run at 100 A across 2/0 to 4 AWG"), state units in-image for charts, and keep the site's field-guide voice.

---

## 6. Internal Linking & Topic-Cluster Plan

Current state (from a fresh-build crawl): healthy footer/nav mesh (133-page sitewide links), 1 true orphan (`authors.md`), 10 hub-only pages, recency-based related-posts. The appliance cluster (fridge/100Ah/CPAP) is already promoted sitewide via the system strip.

**Cluster structure to enforce (no URL changes needed):**
1. **Wiring/electrical cluster** — hub: `wiring-decisions`; make `battery-cable-size ↔ 12v-vs-24v-vs-48v ↔ fuse-and-breaker-sizing` a tight triangle (all three already have traffic).
2. **Battery cluster** — hub: `battery-capacity`; ring: li-ion-vs-lead-acid (after expansion), cost-per-kwh, enclosure, maintenance, BMS, not-charging, backup-vs-generator, battery-cost-2026 (canonical survivor).
3. **Troubleshooting cluster** — cross-link the three not-charging/low-output/shutting-off pages as "step 2/step 3" of one diagnostic journey; each links to the specific cause page (cable size, shading, MPPT).
4. **Money cluster** — tax-credit (accurate) → payback-calculator → lease-vs-buy → financing-options → state guides; state guides link OUT to cost-per-watt/system-costs instead of repeating national data.
5. **DIY cluster** — hub: `diy-off-grid-energy/_index`; each build page links its 2–3 nearest neighbors (pelton↔micro-hydro↔water-wheel; small-wind↔savonius; alternator↔treadmill-motor), all roads through `diy-generator-test-bench` (the measurement doctrine page).

**Specific missing links (highest value):** output-troubleshooting→shading-effects; system-costs→payback-calculator; solar-maintenance→degradation-rate; panels-for-sheds→fuse-sizing + wiring-decisions; efficiency→cost-per-watt (resolves a data contradiction); phone-charger↔yard-lights↔portable-panels (same buyer); mobile-homes→permits; net-metering-explained→net-metering-by-state; spec-sheet→degradation-rate; DIY hub inbound links from system-sizing and solar-panel-output (currently almost nothing in /pages reaches the DIY cluster); authors.html from global footer.

---

## 7. Priority Action Plan

### Fix Immediately (this week — mechanical, hours not days)
| Task | Effort | Expected impact |
|---|---|---|
| 1. Hostinger crawler 403 (C1) — whitelist/disable challenge, re-verify with `curl -A "Googlebot/2.1..."`, resubmit sitemap | 30 min | Unblocks everything; site is currently invisible to Google |
| 2. Mechanical defect sweep (C4): 12 fused-FAQ headings (newline before `{{< faq`), 4 backtick tables (strip per-line backticks), `solar-generator.md:19` 需求, "Key Take"/"ical considerations"/"able Strategies" headings, "1ne 15%"/"$able"/"Lithates"/"100-square-tfoot" text, 3 dead `[…](#)` links in CA page | 2–3 h | Removes visible unedited-AI signals from 20+ pages incl. traffic winners |
| 3. Stale-ITC fixes (C2): lease-vs-buy:139 + savings table; battery-cost-2026 FAQ; pages/solar-panel-cost-california 4 passages + payback numbers | 2 h | Kills factually wrong money advice; trust + accuracy |
| 4. Duplicate canonicals (C3): `canonical` front matter on /guides/solar-battery-cost-2026 and /pages/solar-panel-cost-california (+ differentiating edits) | 30 min | Ends self-cannibalization on two money queries |
| 5. Disclosure banners on the 11 pages (C5) | 30 min | Associates compliance consistency |
| 6. TOC partial hardening: strip/escape shortcode placeholders in headings so the garbage can't recur | 30 min | Prevents recurrence |
| 7. Rybbit: default to bot-filtered view; note GA4 unaffected | 15 min | Restores decision-quality analytics |

### Improve Next (weeks 2–6)
1. **De-thin the proven-demand pages:** solar-system-costs (43pv, 273wc), mppt-vs-pwm, li-ion-vs-lead-acid, diy-vs-installer, solar-maintenance, solar-output-troubleshooting, solar-panel-cleaning-cost — EXPAND to the depth of the August cohort (numbers, worked examples, FAQ schema).
2. **State-guide de-templating (CO/IL/NV/MA/NJ):** one original data point per state (utility rate table, city cost rows, local incentive status), link out to /pages cost pages.
3. **DIY cluster visuals** (§5 Priority 1) — 6 pages with existing traffic first.
4. **Rewrite the 10 REWRITE pages** (best list: li-ion-vs-lead-acid, diy-vs-installer, solar-use-cases as real hub, off-grid-setup-guide, solar-generator, financing-options, solar-basics, solar-panel-efficiency, solar-power-mobile-homes, best-solar-batteries-2026 with actual selection criteria).
5. **Trust layer:** authors.md rebuild (named editor or honest shop voice), about.md revenue wording, corrections.md seeded with the ITC corrections already made, editorial-policy review cadence. Link authors from footer.
6. **UX:** mobile table wrappers; related-posts relevance (curated lists per top-20 pages); noindex search.md.
7. **Monetization coverage:** product boxes on pure-buyer pages that have none (phone-charger, yard-lights, shed-kits, fridge-generator page, CPAP batteries, 100Ah LiFePO4) — always after the content earns it, never instead of it.

### Build Over Time (months)
1. **Toolify decision pages** (the site's proven vein): cable-size calculator, wire-gauge calculator, voltage-decision quiz; angle-calculator page needs its actual calculator (currently a formula page under a tool title — pogo-stick risk).
2. **Appliance-runtime cluster expansion** (fridge/100Ah/CPAP template works): CPAP-through-the-night sizing, chest-freezer, well-pump, mini-split pages.
3. **Firsthand build documentation** in Project Lab: measured results with photos ("we measured X watts at Y head") — the only E-E-A-T moat an anonymous site can actually build honestly.
4. **State guide program:** complete the remaining high-volume states (GA, NC, OH, PA, MI…) using the de-templated format.
5. **Digital PR-lite:** the honest post-ITC payback math and the net-metering-by-state table are citable assets — pitch them to solar communities/forums for real referring links (the site has essentially none today).

---

## 8. Rewrite Briefs — five highest-priority weak pages

**1. `/pages/solar-lease-vs-buy-2026.html`** (currently Q4, REWRITE; money decision)
- Audience: homeowner comparing cash/loan/lease/PPA in the post-ITC era. Intent: transactional research.
- Missing value: internally contradictory ITC claims; comparison table renders as code; no state-variation; no "when leasing actually wins" honesty.
- Structure: Quick answer (post-credit reality) → corrected 20-yr math table → lease red flags → loan mechanics → state-by-state nuance → decision checklist → FAQ (schema).
- Evidence to add: recomputed savings without the $7,500 credit; two worked examples (cash vs loan); Escalating PPA rate trap with real 2.9%/yr example.
- Visual: 20-yr cumulative cash-flow chart. Links: financing-options, tax-credit, payback-calculator, net-metering-by-state.
- Outcome: the site's most trustworthy money-decision page; target for "solar lease vs buy 2026".

**2. `/pages/li-ion-vs-lead-acid.html`** (Q1, EXPAND/REWRITE; chemistry comparison, feeds battery cluster)
- Audience: DIY/RV/cabin builder choosing chemistry. Intent: comparison + price.
- Missing: everything — cycles, DoD, usable capacity math, temperature behavior, $/usable-kWh over life, charging profile differences, safety (venting vs BMS).
- Evidence: LiFePO4 3,000–6,000 cycles @80% DoD vs FLA 500–1,200 @50%; $/usable-kWh-lifetime worked math; cold-charging cutoff behavior.
- Visual: cycle-life vs DoD chart; cost-per-usable-kWh bar chart. Links: battery-capacity, cost-per-kwh, battery-cost-2026 (canonical), BMS page, not-charging.
- Outcome: replace the worst page on the site with a cluster keystone.

**3. `/pages/solar-system-costs.html`** (Q5, EXPAND; 43 all-time pv on 273 words)
- Audience: budget-stage buyer. Intent: commercial cost research.
- Missing: itemized budgets (the title promises a breakdown), 2026 post-ITC pricing, DIY vs installed deltas, financing cost of money.
- Evidence: three worked budgets (2kW DIY cabin / 6kW financed home / 10kW+ battery hybrid); component-share table (panels 34%, inverter 10%, BOS/labor…); range sources.
- Visual: stacked cost-share bars. Links: cost-per-watt, wiring-and-protection-cost, inverter-cost, payback-calculator, lease-vs-buy, state guides.
- Outcome: convert proven traffic into the money-cluster hub.

**4. `/pages/solar-generator.html`** (Q5, REWRITE; "solar generator" is a huge commercial term)
- Audience: buyer choosing a portable power station. Intent: buying research.
- Missing: the CJK artifact and escaped debris; capacity tiers with runtimes; LiFePO4 chemistry guidance; why-you-might-not-need-one honesty; zero internal links.
- Structure: what it is/isn't → capacity tiers table → how to size (link what-size-generator-run-refrigerator) → chemistry → tier picks with criteria → FAQ.
- Visual: runtime-vs-capacity chart by tier. Links: fridge article, 100Ah article, pure-sine, battery-cost-per-kwh, portable-solar-panels.
- Outcome: claim the site's biggest head commercial term with a page that currently embarrasses it.

**5. `/pages/mppt-vs-pwm.html`** (Q4, EXPAND; feeds the site's best-performing product category)
- Audience: component shopper with a controller decision. Intent: comparison + immediate purchase.
- Missing: voltage-window math where MPPT actually wins (cold-day Voc, 12V/24V arrays), when PWM is the right cheap answer, real model names/prices, harvest-difference percentages by scenario.
- Evidence: worked example — 100W panel, Vmp 18V: PWM clips to ~13V (≈28% loss) vs MPPT conversion; model table (Victron 75|15, Renogy Rover, EPEver Tracer with prices).
- Visual: MPPT gain vs array-voltage chart. Links: mppt-charge-controller-cost, best-mppt-charge-controllers, not-charging, system-voltage.
- Outcome: comparison keystone + natural funnel into the site's MPPT buyer guide (already affiliate-linked).

---

## 9. Prioritized Checklist (do in this order)

1. ☐ Hostinger: fix 403 browser-verification for crawlers (C1) — everything else depends on it
2. ☐ Sweep 12 fused-FAQ headings; harden TOC partial
3. ☐ Fix 4 backtick tables + 需求 + truncated headings + corrupted text (C4 list)
4. ☐ Correct 3 stale-ITC pages (lease-vs-buy, battery-cost-2026 FAQ, pages/CA)
5. ☐ Set canonicals on the two duplicate pairs (C3)
6. ☐ Add disclosure banners to 11 pages (C5)
7. ☐ Rebuild + deploy; request reindexing in Search Console (submit sitemap + key pages)
8. ☐ Rybbit: enable bot filtering as default view
9. ☐ De-thin solar-system-costs, mppt-vs-pwm, li-ion-vs-lead-acid, diy-vs-installer, solar-maintenance
10. ☐ DIY cluster: heroes + one build visual each on the 6 traffic pages (magica-media)
11. ☐ De-template CO/IL/NV/MA/NJ state guides
12. ☐ Trust layer: authors/about/corrections rebuild; link authors in footer
13. ☐ Mobile table wrappers + related-posts relevance
14. ☐ Product boxes on unmonetized buyer pages (fridge, CPAP, phone-charger, yard-lights, sheds)
15. ☐ Then: rewrite briefs 1–5, toolify angle-calculator + cable-size, expand appliance cluster

---

### Audit scope & confidence notes
- Every content page was read in full by a dedicated audit pass; all headline defects were re-verified by the Boss against a fresh `hugo --minify` build of the current tree and, where relevant, live-site responses.
- Analytics: full-history Rybbit API pull (2025-12-20 → 2026-09-05) + last-30d bot/referrer breakdown. **Search Console data was not available** — verifying C1's exact effect on Googlebot (vs. only UA-string probes) and getting per-query impressions requires GSC access; export it when possible.
- The Googlebot 403 finding is evidenced from this network/IP; Hostinger's protection is rate- and reputation-triggered, so severity could vary — but with Google at 9 visits in 8.5 months, treat it as the primary suspect until disproven in GSC's crawl-stats report.
