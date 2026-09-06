# Seat D — Topical-Authority Map (ca-topical-map)

**Role:** content-strategist · **Date:** 2026-09-05 · **Scope:** editorial-completeness layer over the DONE keyword matrix (`.agency/seo-audit/master-matrix.md`); keyword priorities are not re-litigated.
**Method:** `quality-signals.json/.tsv` (140 URLs), `rybbit-traffic.json` (99 rows), fact-pack.md, master-matrix.md, spot-reads of hub anchors + trust pages + Project Lab files + buyer pages. Every judgment is tied to a quoted signal or file excerpt; claim tiers T1–T5 per fact pack.
**Status:** COMPLETE (file created early, appended per section; this is the final pass).

---

## 0. Inventory facts used (evidence base)

- 140 content files (fact pack): 104 `pages/`, 11 `guides/` bundles, 20 `diy-off-grid-energy/`, root trust pages (authors, corrections, methodology, system-planner, search) + 7 trust pages inside `pages/`.
- 36 pages carry product boxes (fact pack); grep confirms 48 `{{< product-box → }}` refs across 36 files (some pages carry 2+). 11 pages carry calculators (`calc`=1: solar-system-sizing, solar-panel-output, solar-panel-angle-calculator, battery-capacity, solar-payback-calculator, battery-cable-size-for-inverter, solar-wire-size, solar-fuse-and-breaker-sizing, solar-inverter-sizing, charge-controller-sizing, 12v-vs-24v-vs-48v-solar).
- 5 canonicalized duplicates (`canonical`=1 in signals): `guides/solar-battery-cost-2026/`, `pages/best-solar-panels-for-home-2026.html`, `pages/best-solar-panels-for-small-homes.html`, `pages/how-to-choose-solar-system-voltage.html`, `pages/solar-panel-cost-california.html`. Constraint honored: URLs never change; consolidation is canonical-only.
- **Matrix-vs-disk check (editorial layer must not re-spec built pages):** 8 master-matrix rows marked "NEW" already exist on disk (Sept 2026 wave) — rows 9 (chest-freezer), 12 (charge-controller-sizing), 13 (battery-drains-overnight), 19 (48v-off-grid-wiring-guide), 20 (inverter-cable-size-chart), 21 (mini-split), 22 (lifepo4-100ah-brand-comparison), 28 (will-100-watt). Still unbuilt/queued: rows 24 (oxygen concentrator), 25 (MC4), 31 (well-pump sizing).
- Sticky hubs (traffic): solar-system-sizing 73pv/19.8% · solar-components 30pv/24.1% · battery-capacity 26pv/7.5% · diy index 28pv/6.2% · mppt-vs-pwm 7pv/14.3%. High-bounce answer/tool pages (79–96%) dominate top-20 — single-answer intent, not thinness (e.g., battery-cable-size-for-inverter 104pv/86.9%; solar-fuse-and-breaker-sizing 58pv/90.9%).
- `updated` front matter exists on exactly 7 pages (solar-system-sizing, battery-capacity, net-metering-by-state-2026, solar-panel-tax-credit, read-solar-panel-specs-sheet, solar-panel-output, solar-inverter-sizing; plus affiliate-disclosure has `lastmod`). 133 content pages render no review date. Template check (`layouts/_default/single.html`): "Reviewed {date}" renders only `{{ with .Params.updated }}` — confirmed fact-pack finding 3.

---

## 1. CLUSTER INVENTORY (11 hubs)

Posture legend: **none** (0 product boxes) · **light** (1 box) · **heavy** (≥2 boxes, or buyer roundups).

### H1 — Fundamentals, Sizing & Array Design
- **Anchor:** `/pages/solar-system-sizing.html` (1,362w, calc, 3 boxes; 73pv/19.8% bounce — stickiest high-traffic page; **0 inbound internal links**).
- **Spokes (16):** solar-basics · how-do-solar-panels-work · solar-components (41 inlinks — site max) · how-to-calculate-solar-load · solar-panel-output (calc) · solar-panel-output-per-square-foot · solar-panel-efficiency · solar-panel-degradation-rate · solar-panel-shading-effects · solar-panel-tilt-and-orientation · solar-panel-angle-calculator (calc) · read-solar-panel-specs-sheet · solar-system-costs · solar-payback-calculator (calc) · solar-panel-cost-per-watt · 12v-vs-24v-vs-48v-solar (2 boxes, calc) (+ canonical how-to-choose-solar-system-voltage).
- **Depth:** adequate–strong (most 1,300–3,300w; solar-components 2,397w/2 tables; how-to-calculate-solar-load 2,952w/14 tables). Anchor is thin-ish (1,362w) for a pillar.
- **Internal links:** solar-components 41 (excellent); solar-system-sizing **0**, solar-panel-output **0**, solar-system-costs **0** — sizing funnel disconnected inbound.
- **Posture:** light (5 boxes across 16 pages; science pages clean).

### H2 — Panels & Home Solar Economics
- **Anchor:** `/pages/how-much-do-solar-panels-cost.html` (1,492w, 1 box).
- **Spokes (12):** best-solar-panels-for-home-2026 (canon, 1,106w) · best-solar-panels-for-small-homes (canon, 1,052w) · best-solar-panels-small-roof (1,860w) · solar-lease-vs-buy-2026 · solar-financing-options · solar-panel-tax-credit · ground-mount-solar-panels · ground-mount-vs-roof-mount-solar · how-many-solar-panels-to-power-a-house · how-long-do-solar-panels-last · install-solar-panels-yourself · diy-vs-installer (11 inlinks).
- **Depth:** thin-to-adequate; several 1,000–1,900w pages, some without FAQ (best-solar-panels-small-roof, ground-mount-vs-roof-mount, solar-lease-vs-buy all `faq`=0).
- **Internal links:** ground-mount-vs-roof-mount 1, solar-lease-vs-buy 3, install-solar-panels-yourself 3, how-many-solar-panels 1 — spokes weakly linked to anchor and to each other.
- **Posture:** light (4 boxes: anchor, 3 "best panels" pages ≤1 each).
- **Freshness risk found:** `how-much-do-solar-panels-cost.md` FAQ (lines ~127–131) still answers "Does the 30% Federal Tax Credit apply to the whole cost?" with "Yes, the Federal Investment Tax Credit (ITC) applies to the total cost…" — contradicts the page's own body ("The 30% ITC expired December 31, 2025") and the sitewide Sept-2026 purge. T5 freshness defect; E-E-A-T poison on a hub. NOTE: any-flavor guide page `/guides/solar-panel-cost-*` pages carry honest_neg=1–6 and cite EIA June-2026 rates (per fact pack) — that posture is fine.

### H3 — Batteries, Chemistry & Energy Storage (largest hub, 21 URLs)
- **Anchor:** `/pages/li-ion-vs-lead-acid.html` (2,445w, no box) — the chemistry decision page, 0 inlinks.
- **Spokes (20):** best-solar-batteries-2026 (buyer, 1 box, honest_neg=10) · lifepo4-100ah-brand-comparison (spec table, 1,200w) · solar-battery-maintenance-guide (2,822w/11 tables) · solar-battery-enclosure-guide (3,027w) · solar-battery-management-system-explained (1,519w) · solar-battery-cost-2026 (canon bundle + flat page) · how-much-do-solar-batteries-cost · solar-battery-cost-per-kwh · battery-capacity (calc, 26pv/7.5%) · how-long-will-100ah-battery-run (9 inlinks) · battery-drains-overnight-off-grid · what-size-battery-run-chest-freezer · solar-battery-not-charging-troubleshooting · solar-battery-backup-vs-generator · 12v…48v (voltage) · mini-split-watts-off-grid (10 inlinks) · will-100-watt-solar-panel-run-refrigerator (11 inlinks) · cpap-battery-backup-guide (10 inlinks) + 5 DIY storage experiment spokes (gravity, flywheel, supercapacitor, compressed-air, TEG) — better anchored under H11; counted here as chemistry-adjacent.
- **Depth:** strong overall (6 pages >2,200w; 2,822w maintenance guide); buyer pages thin (lifepo4 1,200w body, cost-per-kwh 607w).
- **Internal links:** spread 0–14; anchor li-ion-vs-lead-acid has **0** inlinks; best-solar-batteries-2026 **0**.
- **Posture:** light overall but WIRED for heavy: 5 buyer boxes + BMS page carries 1 box on a forklift (BMS parts) — expansion ready.

### H4 — Inverters & AC Power
- **Anchor:** `/pages/solar-inverter-sizing.html` (2,015w, 1 box, calc, `updated` set).
- **Spokes (9):** micro-vs-string-inverters (6 inlinks) · pure-sine-vs-modified-sine-inverter · how-to-choose-solar-inverter (1,565w) · solar-inverter-cost · inverter-keeps-shutting-off-troubleshooting (2 boxes) · inverter-cable-size-chart (new, 1,308w, 7 inlinks) · ac-vs-dc-coupled-solar-systems · what-size-solar-generator-run-refrigerator · pure-sine… (counted once).
- **Depth:** adequate (1,274–2,270w); inverter-keeps-shutting-off 1,786w and inverter-cable-size-chart 11 tables = strong troubleshooting/reference.
- **Internal links:** solar-inverter-sizing **0** inlinks (top-6 traffic page orbiting alone); micro-vs-string 6, inverter-cable-size-chart 7.
- **Posture:** light (4 boxes across 9 pages).

### H5 — Wiring, Protection & DC Safety (the "wire-protection reference")
- **Anchor:** `/pages/wiring-decisions.html` (346w only — pillar in name, stub in content; no boxes; 3 inlinks).
- **Spokes (9):** solar-wire-size (calc, 1,806w) · battery-cable-size-for-inverter (calc, 2,343w, 104pv #2 traffic) · solar-fuse-and-breaker-sizing (calc, 2 boxes, 58pv/90.9%) · solar-fuses-vs-breakers · solar-combiner-box-and-disconnect-guide (918w) · inverter-cable-size-chart (also H4) · solar-wiring-and-protection-cost (666w) · solar-panels-series-vs-parallel (874w) · battery-cable-size… (counted once).
- **Depth:** spokes deep (2,000–2,600w with calc), **hub is 346w** — the cheapest authority upgrade on the site (expand anchor + add missing wire-protection spokes below).
- **Internal links:** solar-wire-size 3, fuse-and-breaker-sizing 3, combiner 3 — hub links out to spokes well; spokes link back weakly.
- **Posture:** light (2 boxes on fuse-and-breaker-sizing; other pages clean).

### H6 — Troubleshooting & Maintenance
- **Anchor:** `/pages/solar-output-troubleshooting.html` (3,511w/10 tables) — the natural "start here for anything wrong" page.
- **Spokes (10):** solar-battery-not-charging-troubleshooting · mppt-charge-controller-not-charging (3,031w, buyer box, 60pv) · solar-maintenance (2,681w) · solar-battery-maintenance-guide (also H3) · solar-panel-cleaning-cost · battery-drains-overnight-off-grid (also H3) · inverter-keeps-shutting-off-troubleshooting (also H4) · common-solar-installation-mistakes · solar-panel-degradation-rate (also H1) · solar-generation… (outlier: DIY-era page "solar-panel-not-charging" not present; closest is solar-battery-not-charging).
- **Depth:** strong (5 pages >2,000w; troubleshooting trio 1,800–3,500w with 8–10 tables each).
- **Internal links:** anchor has 2 inlinks only; mppt-not-charging **0** inlinks despite 60pv; solar-maintenance **0**.
- **Posture:** none–light (1 box on mppt-not-charging).

### H7 — Safety, Permits & Installation
- **Anchor:** `/pages/solar-installation-safety-guide.html` (3,597w/3 tables; best single safety page on site).
- **Spokes (8):** solar-permits-and-building-codes (1,573w) · common-solar-installation-mistakes (2,196w) · install-solar-panels-yourself · diy-vs-installer (also H2) · off-grid-solar-system-setup-guide (2,652w) · solar-battery-enclosure-guide (also H3) · ground-mount-vs-roof-mount (also H2) · solar-combiner-box-and-disconnect-guide (also H5).
- **Depth:** strong at anchor (3,597w), adequate elsewhere; permits page is a credible NEC/AHJ overview but shallow on specific provisions.
- **Internal links:** anchor 10 inlinks (healthy); permits 3; off-grid-setup **0**.
- **Posture:** none (safety pages clean — correct posture).
- **Note:** safety-guide sentence "None of this is theoretical. Every item here maps to a real failure mode that has sent real people to the ER." is editorial framing (T4) — acceptable but flag: it implies incident reports the site does not cite.

### H8 — Buying, Seasonal & Use Cases
- **Anchor:** `/pages/solar-use-cases.html` (2,400w hub — genuinely the site's cleanest hub; 14 H2s mapping scenarios to spokes; 4 inlinks; 0 boxes).
- **Spokes (16):** rv-solar-sizing · rv-solar-cost · cabin-solar-sizing · cabin-solar-cost · cabin-solar-vs-generator · solar-panels-for-sheds (buyer, thin, 1,543w) · solar-power-mobile-homes (2,856w) · cpap-battery-backup-guide (buyer, 10 inlinks) · solar-generator (2 boxes; 6pv/100% bounce) · what-size-solar-generator-run-refrigerator · solar-battery-backup-vs-generator · portable-solar-panels · solar-phone-charger · solar-lights-for-yard · solar-water-heater · solar-panels-vs-wind-turbines (+ mini-split-watts-off-grid and will-100-watt under H3 math).
- **Depth:** adequate at anchor; spokes uneven — rv-solar-cost 1,303w/19 tables but rv-solar-sizing 686w (thin); solar-phone-charger 1,464w.
- **Internal links:** rv-solar-cost **0**, rv-solar-sizing **0**, cabin-solar-cost **0**, cabin-solar-sizing **0**, solar-generator **0** — every commercial leaf is an orphan.
- **Posture:** light–heavy: rv-solar-cost 1, solar-generator 2, cabin-solar-cost 2, sheds 1, cpap 1, phone-charger 1, lights 1.

### H9 — State Costs, Incentives & Metering (regional)
- **Anchor:** `/guides/solar-panel-cost-california/` (bundle, 3,301w; flat canonical twin exists; grants `_index` variant).
- **Spokes (12):** 11 state bundles (arizona, texas, florida, new-york, new-jersey, colorado, illinois, massachusetts, nevada + california + battery-cost-2026) + net-metering-by-state-2026 (29 tables, `updated` set) + solar-net-metering-explained.
- **Depth:** adequate (900–3,300w; 6 bundles >2,000w with honest_neg=1–6, EIA June-2026 rates per fact pack); nevada/massachusetts/illinois thin (900–1,500w).
- **Internal links:** bundles 0–6; net-metering-by-state-2026 **0**.
- **Posture:** none (no product boxes — correct).
- **Freshness:** depends on the visibility gap in §0; `updated` set only on net-metering pages. State-guide surface: headers say "in 2026" (titles) so datedness is at least declared.

### H10 — DIY Off-Grid Experiments (Project Lab)
- **Anchor:** `/diy-off-grid-energy/_index.html` (37 words — the thinnest hub on the site; "hub" by URL convention only; 28pv/6.2% bounce).
- **Spokes (19):** 18 experiment articles (wind ×3, hydro ×3, human-power ×2, storage ×5, generators ×4, hybrid controller, dump-load, test-bench) + related root pages.
- **Depth:** strong per article (1,679–4,390w; 7 articles >3,000w), none monetized, all FAQ.
- **Internal links:** 3 per article, mostly self-referential (test-bench links); no spoke links to solar hubs except a few ("solar components", "system costs", "maintenance" links in diy-small-wind / micro-hydro). Index 37w links to only 3 articles — 15 of 20 lab files are one click from a dead end.
- **Posture:** none (correct).
- **T1 status (decided from repo evidence):** the lab is a research-and-math library, NOT a documented-firsthand-test section. Authors page: "When we do document a real build or measurement in the Project Lab, the measurements and their limits are stated in that article" — no lab article contains a specific measurement ("it delivers 45W at 600 RPM" is illustrative, line 27 of test-bench; gravity-battery rounds efficiency ranges, 40–70%, no measured value) and zero "we built/we measured" first-person instrument records appear in any of the 20 files. Verdict: no T1 firsthand evidence exists in the lab; its honest_tone is T4/T2 with T5 boundaries clearly labeled. The affiliate-disclosure sentence "our guides are written from hands-on experience with off-grid systems, DIY builds, and component research — not from manufacturer press releases" is therefore **overbroad vs how-we-recommend/authors** ("We do not run a test lab… assume nothing here has been bench-tested by us") — the disclosure should be narrowed to match research-framing. **This is a T1-claim conflict that an authoritative site must fix.** (Detail: the DIY index itself carries a hands_on_claim=1 flag in signals.)

### H11 — Battery Chemistry & Runtime Math (part of H3 spokes; anchor listed here for the map's completeness)
- **Anchor:** `/pages/battery-capacity.html` (909w, calc, 1 box; 26pv/7.5% bounce — a sticky calculator).
- **Spokes:** how-long-will-100ah-battery-run · will-100-watt-solar-panel-run-refrigerator · what-size-battery-run-chest-freezer · mini-split-watts-off-grid · cpap-battery-backup-guide · 48v-off-grid-wiring-guide · battery-drains-overnight-off-grid · what-size-solar-generator-run-refrigerator.
- **Depth/pose/internal:** merged with H3 above (runtime math = the chemistry cluster's buyer tail).
- **Posture:** light (boxes on battery-capacity, cpap, what-size-solar-generator).

**Coverage note:** `search.html`, `system-planner.html`, `methodology.html`, `corrections.html` are trust/infra, not topic hubs — excluded from clustering (they ARE 4 of the 140 URLs).

---

## 2. GAPS (per hub; essential-for-authority / nice-to-have / skip-with-reason)

Cross-referenced with master-matrix.md rows. **Matrix already queued (do not re-spec):** rows 24 oxygen concentrator, 25 MC4 guide, 31 well-pump sizing → "queued (matrix row N)".

### H1 (Fundamentals/Sizing)
- G1.1 **Glossary of solar terms** (beginner landing on site has no definitions hub; solar-basics defines ~6 terms inline). **essential-for-authority.** Not in matrix.
- G1.2 **System expansion planning** ("how to grow a 12V system later: voltage upgrade, adding batteries, inverter upsizing") — found only as stray "expand" context in 12v-vs-24v/48v-wiring; no dedicated planning guide. **essential-for-authority** (commits buyers to compatible components). Not in matrix (adjacent to row 19 wiring guide — distinct intent, keep as own).
- G1.3 **Peak sun hours by location** (solar-basics cites 3–6h but no map/table; dozens of pages depend on it). **nice-to-have** (anchor upgrade could fold a table in, avoiding a new URL). Not in matrix.
- G1.4 **Seasonal/regional yield adjustment** (snow loss, monsoon overcast, latitudes) — **nice-to-have**; partial support via tilt/angle calculator. Not in matrix.

### H2 (Panels/Economics)
- G2.1 **Fix the stale ITC FAQ** in how-much-do-solar-panels-cost.md — **essential-for-authority** (freshness blocker, T5). Not a content gap; a repair.
- G2.2 **NEC 2023 rapid shutdown / module-level power electronics for roof arrays** — mentioned under H7 only. **nice-to-have** (grid-tied buyers hit RSD questions; DIY site can cover the rule (T3) without endorsing products).
- G2.3 **Panels: warranties & UL listing explained** (how to verify a panel is UL 1703/61730 listed — buyers can't verify without it). **nice-to-have.** Not in matrix.
- G2.4 **HOA solar rights by state** — **skip-with-reason**: solar-permits-and-building-codes covers HOAs+access laws at adequate depth; state-by-state is a freshness war the site can't responsibly win (same logic as matrix row 37).

### H3/H11 (Batteries)
- G3.1 **Battery fire / thermal runaway safety** (LiFePO4 venting, Class D extinguisher, spacing from structures, off-gassing; the safety guide mentions Class D + "never water" only). **essential-for-authority** — the single most important battery page a solar site can own after chemistry. Not in matrix (matrix row 13 drains-overnight is diagnosis, not fire).
- G3.2 **Battery chemistry deep-dive hub** (NMC vs LiFePO4 vs lead-acid lifecycle/cost curve beyond 1-page li-ion-vs-lead-acid — owns max continuous discharge, C-rate, cycle definitions). **essential-for-authority.** Not in matrix (row 22 brand-comparison is purchase-layer, not chemistry).
- G3.3 **Battery monitoring & state-of-charge metering** (shunts, smart battery monitors, what "100%" means) — grep shows only BMS-explained (protection) + related "shunt" mentions in 48v/off-grid setups; no metering guide. **essential-for-authority.** Not in matrix.
- G3.4 **Inverter battery-draw / 12V amp draw math** — covered inside solar-inverter-sizing; **skip-with-reason** (already covered; inbound links fix suffices).
- G3.5 **LiFePO4 cold-weather charging (heated batteries, low-temp cutoff)** — exists inside maintenance/enclosure pages; **nice-to-have** as a dedicated page folded into H7 winterization (below).

### H4 (Inverters)
- G4.1 **Inverter loading / derating & continuous-vs-peak** (ambient derating curves, "2× rule", duty limits of surge) — solar-inverter-sizing touches continuous-vs-surge; no derating reference. **essential-for-authority** (prevents the #1 buyer mistake = buying on peak watts). Not in matrix.
- G4.2 **Inverter wiring for standby/transfer (ATS, interlock)** — **nice-to-have** (grid-interactive DIY is a permit/licensed-electrician boundary; a "when to call a pro" framing fits the site's honesty posture). Not in matrix.
- G4.3 **Inverter idle draw (no-load power) explained** — runtime math pages cite it; **nice-to-have** worked-example block inside solar-inverter-sizing (no new URL).

### H5 (Wiring/Protection)
- G5.1 **DC wire-protection reference: ampacity chart + fuse-at-every-source philosophy** (a single wire/fuse/breaker reference the rest of the site links to) — wiring-decisions pillar is 346w; existing tools are per-task. **essential-for-authority.** Overlaps matrix rows 2/3/10/20 (tools) — do NOT re-spec those; this gap = the REFERENCE/hub upgrade, distinct.
- G5.2 **Grounding & lightning protection** (equipment grounding vs system bonding vs ground rods; lightning/transient surge on off-grid; NEC 250/690.43) — grep: grounding only in 6 pages as passing mention; no dedicated page. **essential-for-authority.** Not in matrix.
- G5.3 **Fusing philosophy: "fuse every source of fault current" plus battery terminal fusing** — partially in fuses-vs-breakers (938w); the safety guide says "every battery bank needs proper fusing"; **nice-to-have** fold into G5.1 reference (no new URL).
- G5.4 **Wire protection against rodents/UV/abrasion (conduit, wire management)** — **nice-to-have** (mentioned in maintenance inspection list; a short section in G5.1 suffices).

### H6 (Troubleshooting/Maintenance)
- G6.1 **Seasonal/inspection checklist as a printable reference** — exists as solar-maintenance seasonal table; **skip-with-reason** (already covered, adequate).
- G6.2 **Outage-season readiness (hurricane/winter storm prep)** — matrix rows 14/15 already queued (hub improve solar-generator); **queued (matrix rows 14–15)**; H8 seasonal section is the deliverable.
- G6.3 **Troubleshooting flowcharts / decision-tree format** for the three top pages — **nice-to-have** (rows 1/4/7 matrix already deepen these same pages; do not re-spec content, but note format need is covered by those rows).
- G6.4 **"Why is my battery draining overnight / phantom load hunting with a multimeter"** — **queued (matrix row 13)** — page already exists on disk; treat as built.

### H7 (Safety/Permits)
- G7.1 **Permits/code/inspection workflow** (what an inspector checks, permit docs one-lines, off-grid vs grid-tied) — solar-permits-and-building-codes exists (1,573w) **but lacks the specific inspection checklist and NEC §690.46/§705 interconnection details**; expand in place. **essential-for-authority.** Not in matrix (row 19 wiring guide is close but distinct).
- G7.2 **Arc-flash / DC arc hazard** (battery-bank short = arc flash covered in safety guide qualitatively; no dedicated arc-flash math or arc-fault protection discussion). **essential-for-authority** (the site already teaches 2,000–4,000A short-circuit thinking; a companion page seals it). Not in matrix.
- G7.3 **Battery fire response** (see G3.1) — cross-listed.
- G7.4 **Grounding & lightning** (G5.2) — cross-listed.
- G7.5 **Fall protection / roof work** — **skip-with-reason**: safety guide covers harness/anchor/OSHA 6-ft rule thoroughly; no gap.

### H8 (Buying/Seasonal)
- G8.1 **Buyer-journey stages** (how to buy solar: load audit → component list → budget → where to spend/not spend → DIY vs installer) — pieces exist but no consolidated roadmap; **essential-for-authority** (deduplicates intent and reduces orphan leaves). Not in matrix (rows are per-product).
- G8.2 **Winterization section** (cold-weather battery rules, snow handling, short-day recharge math) — matrix row 15 queued for solar-generator (winter section); **queued (matrix row 15)**; plus G3.5/G6.2 supporting spokes.
- G8.3 **RV/cabin/camping seasonal hooks** — **nice-to-have**; rv-solar-* pages are orphans with 0 inlinks; linking fixes matter more than new URLs.

### H9 (Regional)
- G9.1 **Climate-zone adjustments for off-grid systems** (hurricane tie-downs, desert heat derating, northern short-winter days) — **essential-for-authority** for a site whose calculator math assumes generic sun hours. Not in matrix (rows 35–37 are state-cost only).
- G9.2 **State-by-state incentive ledger beyond the 11 bundles** — **skip-with-reason** (freshness war; matrix row 37 already caps this: CA-only support layer).

### H10 (Project Lab)
- G10.1 **Lab index rewrite** (37-word hub; cut to 15 pages of spokes; classify "educational experiments" vs "practical builds") — **essential-for-authority** (topical coherence; also preserves the honesty posture by labeling experiment vs build). Not in matrix.
- G10.2 **"What actually works" meta-finding page** (lab conclusions as a single reference: human power 5–150W, flywheel storage limits, TEG reality) — **nice-to-have**; seals the research-library identity. Not in matrix.
- G10.3 **Firsthand build log with measurements (T1)** — **skip-with-reason for now**: would be the ONLY legitimate T1 page and requires a real build; recommend as a long-term trust play, gated on actually doing it (ethics boundary: no invented measurements).

### Cross-cutting
- GX.1 **Glossary** (G1.1) + **decisions tree hub** overlap — implement one `solar-glossary` page; **essential**.
- GX.2 **Review-date visibility** across all hubs — **essential-for-authority** (133 pages w/o `updated` or lastmod; template falls back to `.Lastmod` → `date`). Recommend LATER as ops fix: touch-date rollouts; not a content URL.

---

## 3. HUB-AND-SPOKE PLAN (5 strongest-opportunity hubs)

Constraint respected everywhere: existing URLs never change; additions are new slugs; merges are canonical-only; no removals.

### Plan A — H5 Wiring/Protection (highest leverage: anchor is 346w, spokes already deep, tools already rank)
1. **Upgrade anchor:** `wiring-decisions.html` — expand from 346w to a genuine reference hub: the "fuse every source of fault current" philosophy section, a master ampacity/fuse chart pulled from the existing tools, and a decision tree (wire size → fuses vs breakers → series/parallel → battery cable → combiner/disconnect). URL unchanged.
2. **New spokes (2):** `solar-grounding-and-lightning-guide.html` (G5.2 — grounding vs bonding vs ground rod, DI/ground-electrode, NEC 690.43 context, lightning transient basics) and fold G5.3/G5.4 into the hub itself (reference, no URL).
3. **Mesh:** battery-cable-size-for-inverter (104pv, 6 inlinks) → link UP to wiring-decisions in its intro; solar-fuse-and-breaker-sizing → link UP; solar-wire-size → link UP. wiring-decisions → add link OUT to 48v-off-grid-wiring-guide (48V wire math) and take one link from each of the 3 DIY wind/hydro pages that already link solar-maintenance (swap one of their 3 links to wiring-decisions).
4. **Why:** the two #2/#9 traffic pages on the site (battery-cable 104pv, fuse-and-breaker 58pv) flow through this hub; a 346w pillar is the cheapest authority upgrade available, and G5.1/G5.2 are the two gaps a solar authority must own.

### Plan B — H3/H11 Batteries + Runtime Math (largest hub, wired for monetization, zero anchor inlinks)
1. **Upgrade anchor:** `li-ion-vs-lead-acid.html` — add chemistry deep-dive section (C-rate, cycle definitions, NMC-vs-LFP differences) to satisfy G3.2 in place; add inbound links from best-solar-batteries-2026, solar-battery-cost-per-kwh, battery-capacity, cpap guide, and the DIY TEG/flywheel pages (who discuss battery charging). Add `updated` front matter (page has none).
2. **New spokes (3):** `solar-battery-safety-and-fire.html` (G3.1 — thermal runaway, venting, Class D, spacing, what to do) · `solar-battery-monitoring-guide.html` (G3.3 — shunts, smart monitors, SOC metering) · keep G3.5 inside enclosure/maintenance (no URL).
3. **Mesh:** battery-capacity (36pv/7.5% bounce) → link to li-ion-vs-lead-acid + new monitoring spoke; 48v-off-grid-wiring-guide → link to battery-monitoring; solar-battery-enclosure-guide → link both ways to fire-safety.
4. **Why:** 21 URLs = the largest body of work; anchoring it properly converts the deepest content into the site's authority spine and creates the monetization path (battery purchases) without changing posture.

### Plan C — H6 Troubleshooting & Maintenance (traffic hub: 3 of the site's top-10 pages; zero hub linkage)
1. **Upgrade anchor:** `solar-output-troubleshooting.html` — add a decision-tree intro linking each symptom to its branch page (panel dead → output-troubleshooting; controller no output → mppt-not-charging; battery not charging → battery-not-charging; drains overnight → drains-overnight; inverter shutoff → inverter-keeps-shutting-off). Add `updated`.
2. **New spokes (1):** `solar-inverter-troubleshooting-guide.html` — NO: row 4 already targets inverter-keeeps-shutting-off deepening; skip new URL, fold G6.3 flowchart into that page (queued matrix row 4).
3. **Mesh:** mppt-charge-controller-not-charging (60pv, **0 inlinks**) → add inbound from solar-output-troubleshooting and from mppt-vs-pwm; solar-maintenance (**0 inlinks**) → inbound from solar-components and off-grid-setup; battery-cable-size-for-inverter → inbound already strong, add cross-link to battery-not-charging (symptom+fix pairing).
4. **Why:** this is the site's live-traffic cluster (60+45+41+58pv in top-10) — the fastest way to make search engines see a coherent troubleshooting hub rather than orphan answer pages.

### Plan D — H7 Safety/Permits (already strong anchor; missing the two authority-defining pages)
1. **Upgrade anchor:** `solar-installation-safety-guide.html` — add an "arc flash at battery current" numeric section (existing 2,000–4,000A short-circuit passage seeds it) and link OUT to the two new pages below; fix the "None of this is theoretical… sent real people to the ER" framing (T4) to cite sources or soften.
2. **New spokes (2):** `solar-arc-flash-and-dc-arc-safety.html` (G7.2) · `solar-battery-safety-and-fire.html` (G3.1, shared with Plan B — the safety hub and battery hub cross-link).
3. **Mesh:** solar-permits-and-building-codes → expand inspection-checklist section in place (G7.1) and link to arc-flash page; common-solar-installation-mistakes → link OUT to arc-flash on the "protection" mistake; off-grid-setup → link to safety-guide (currently 0 inlinks on the setup page either way).
4. **Why:** safety is the highest-E-E-A-T signal for a DIY solar site; two missing pages (arc flash, battery fire) are the exact topics the site already hints at, and no competitor with this site's honesty framing covers them in DIY depth.

### Plan E — H8 Buying/Seasonal/Use-Cases (the commercial hub; every leaf is an orphan)
1. **Upgrade anchor:** `solar-use-cases.html` — add a buyer-journey road-map section (G8.1: audit first, then component list, then budget, then buy) linking to the H1 sizing tools; add `updated`.
2. **New spokes (0 required):** rows 14/15 (hurricane/winter seasonal) queue new sections on solar-generator (matrix) — do not build new URLs here; the hub's job is linking, not more leaves.
3. **Mesh (highest-impact fix on the site):** rv-solar-cost, rv-solar-sizing, cabin-solar-cost, cabin-solar-sizing, solar-generator, solar-panels-for-sheds are ALL at 0 inbound links — solar-use-cases (2,400w hub designed to map scenarios) goes FIRST in the mesh: add per-scenario links to all six; then have each leaf link back to use-cases. solar-generator (2 boxes; 6pv/100% bounce) also gets inbound from cpap guide, battery-backup-vs-generator.
4. **Why:** ~$ of the site's affiliate revenue sits on orphan pages; the use-cases hub is already built to carry them — finishing the mesh converts isolated commercial pages into a journey.

---

## 4. AUTHORITY VERDICT

**Closest to genuine authority (finish them):**

1. **H6 Troubleshooting & Maintenance.** Evidence: 3,511w anchor with 10 tables (`solar-output-troubleshooting`), 3,031w MPPT checklist, 2,822w battery-maintenance with 11 tables, 1,999w battery-not-charging; the three top-10 traffic pages (60/45/41pv) sit here; tone is honest and caveated (battery-maintenance honest_neg=1, caveat hits on 3 pages). Nothing on a competitor site out-works a 3,000-word decision checklist that ends in a repair-or-replace call. **Sealing touch:** the decision-tree mesh (Plan C) + `updated` dates on the three troubleshooting pages — without them the freshness gap (fact-pack finding 3) undercuts exactly the pages people trust for diagnostics.
2. **H1 Fundamentals/Sizing.** Evidence: strongest stickiness on site (solar-system-sizing 19.8% bounce, solar-components 24.1%, battery-capacity 7.5%), 41-inlink solar-components hub, 14-table load-audit page, 11 calculators across the cluster; ITC-fresh writing throughout the top pages. This cluster behaves like a reference library. **Sealing touch:** the glossary (G1.1) + expansion-planning (G1.2) + connect solar-system-sizing's 0 inbound links (feed it from solar-basics, use-cases, and every 48v/runtime spoke).
3. **H7 Safety/Permits.** Evidence: 3,597w anchored safety guide with real PPE tables, NEC/AHJ-aware permits page covering Dillon's vs Home Rule, off-grid-vs-grid-tied and HOA section; the site already teaches 2,000–4,000A battery short-circuit math and "never water" on lithium fires — that is expert-level framing. **Sealing touch:** add the arc-flash + battery-fire pages (G7.2/G3.1) and soften/scale the "has sent real people to the ER" claim (T4 without citation).

**Furthest from authority (finish or cap, with recommendation):**

1. **H10 Project Lab (cap, don't expand).** Evidence: index is 37 words; 20 articles are thick (1,679–4,390w) but traffic is 12–78pv at 83–96% bounce (hand-crank 78pv/80%, flywheel 65pv/91%, TEG 39pv/95%, pelton 37pv/96%); articles overlap heavily (wind ×3, hydro ×3, human-power ×2 all chase the same "measurement-first" thesis) and none contains a firsthand measurement that would justify T1. **Recommendation:** CAP — rewrite the index into a classification hub (educational experiment vs practical build; G10.1), canonical-merge the two weakest wind spokes into the strongest (canonical-only, URLs preserved), stop adding Experiment-of-the-Month pages. The lab's value is honest research tone, not traffic; expanding it multiplies high-bounce inventory.
2. **H9 State Costs/Incentives (cap at current 11+2).** Evidence: 6 bundles >2,000w with EIA June-2026 rates and honest_neg=1–6 (good), but nevada/massachusetts/illinois are 900–1,500w, net-metering-by-state-2026 has 0 inlinks, and matrix rows 35–37 already flag installer/marketplace locks and a "freshness war we can't responsibly win". **Recommendation:** FINISH the thin bundles' tables + link metering pages from the cost hub; do NOT add more states; cap the cluster and let rows 35–37's support-layer decisions stand.
3. **H2 Panels/Economics (finish repairs, then cap).** Evidence: the stale ITC FAQ (how-much-do-solar-panels-cost.md "Yes, the Federal Investment Tax Credit applies to the total cost" versus the same page's "The 30% ITC expired December 31, 2025") is a T5 freshness break on a hub page; best-panels pages have no FAQ schema (faq=0), and matrix row 26/34 flags brand-comparison locks. **Recommendation:** fix the FAQ (essential), add `updated` to the hub, link ground-mount pages — then cap new "best panels 2026" pages; the site's authority is research, not roundups, and roundups here would be dishonest without testing (per how-we-recommend).

---

## 5. Cross-cutting recommendations (evidence-backed)

- **Fix the T1 claim conflict** (fact-pack finding 1, confirmed): `affiliate-disclosure.md` "our guides are written from hands-on experience with off-grid systems, DIY builds, and component research" overstates vs `authors.md` "We do not run a test lab, and we do not claim hands-on testing we have not done" and `how-we-recommend.md` "assume nothing here has been bench-tested by us". One sentence of the disclosure is fixable copy (narrow to "engineering and component research, plus documented Project Lab builds where noted").
- **Attribution hygiene is mostly done:** best-solar-batteries-2026 carries honest_neg=10, "per manufacturer spec", and dated retrieval ("retrieved 2026-09-05"); lifepo4-100ah-brand-comparison writes "Claimed" before every cycle figure. But the other ~31 box pages (e.g., solar-panels-for-sheds) state specs with no claim tier — for the plan, add a standard "specs per manufacturer, not lab-tested" line to box pages during the H8 mesh pass (T2 attribution, no new pages).
- **Update-date rollout (ops):** set `updated` on the highest-traffic 30 pages first (battery-cable-size-for-inverter, mppt-not-charging, fuse-and-breaker, solar-maintenance, 12v-vs-24v…) — the "Reviewed" date is the site's strongest E-E-A-T signal and it is currently invisible on 133 pages.
- **Homepage:** `pages/_index.html` is 65 words listing 4 links — the 90.9% bounce on 252pv is partly a navigation problem; the topical map above gives it the 11-hub nav it needs (not this seat's file to change).

---

## 6. Checks performed & unresolved blockers

**Checks performed:** read fact-pack fully; read quality-signals.json + .tsv (140 rows) and rybbit-traffic.json (99 rows); read master-matrix.md (37 rows); spot-read 20+ files including every hub anchor candidate (solar-components, solar-system-sizing, solar-use-cases, wiring-decisions, li-ion-vs-lead-acid, battery-capacity, solar-inverter-sizing, solar-output-troubleshooting, solar-installation-safety-guide, solar-permits-and-building-codes, solar-maintenance, solar-battery-maintenance-guide, solar-generator, solar-basics, best-solar-batteries-2026, best-mppt-charge-controllers, solar-panels-for-sheds, how-much-do-solar-panels-cost), all trust pages (authors, affiliate-disclosure, how-we-recommend, methodology), 8 Project Lab files, and the 9-matrix-row disk check; ran ~12 grep sweeps for gap topics (grounding, arc flash, winter, derating, thermal runaway, shunt/monitoring, glossary, expansion, rapid shutdown); verified the 7-page `updated` reality against the template's "Reviewed" conditional; confirmed the 36-page/48-shortcode box count and 5 canonical flags.
**Claims not verified (no lab on-site, no live SERP needed for the map's core):** no web_search used per fact pack; the map stands on repo evidence alone as required.
**Unresolved blocker (1):** none blocking this deliverable. One risk to flag for the Boss: 11 of 140 URLs were NOT individually spot-read (low-priority spokes — e.g., solar-water-heater, solar-phone-charger, solar-lights-for-yard, solar-power-mobile-homes, portable-solar-panels, 3 of the thin state bundles, search/system-planner/methodology) — cluster membership for those is from signals columns (words/boxes/tables), not full-content read; each is low-risk for the verdicts given, but a W3-style per-page pass on the 3 thin state bundles (nevada/massachusetts/illinois) is recommended before any finishing-touch work on H9.