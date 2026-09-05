**Deliverable content below (file write blocked — see status note at end).**

---

# Competitive Analysis: Off-Grid / DIY / Appliance-Runtime Sub-Niche

solarpoweredproject.com — market-research/competitors-diy.md — Session 20260905T185646Z. All web evidence retrieved **2026-09-05**. Labels: FACT (source-cited), INFERENCE (my reasoning), ASSUMPTION (flagged).

## Method & evidence caveats

- The harness `web_search` tool returned unrelated results on every query (tool failure). All SERP evidence below comes from DuckDuckGo Lite (`https://lite.duckduckgo.com/lite/`) fetched via shell; channel data from YouTube `/about` pages. DDG rankings may not mirror Google — treat SERP composition as directional. INFERENCE.
- No traffic estimates are cited anywhere (per rules). YouTube subscriber/view counts are the platform's own public numbers. FACT.
- Reddit blocked every read path (www, old.reddit, api — login wall `reason=lor2` or JS challenge) on 2026-09-05. No claims are made about subreddit content. FACT (block) / ASSUMPTION (that forum pain points mirror Reddit's — flagged, unverified).
- Jackery blog could not be fetched (404s on `/blogs/` paths). Excluded; no claims made.

## 1) YouTube makers

**Will Prowse — "DIY Solar Power with Will Prowse"** (https://www.youtube.com/@WillProwse/about, 2026-09-05): 1.14M subscribers, 526 videos, 163,746,528 views, US, joined Jun 2007. FACT. Trust engine: teardowns/bench tests plus ownership of diysolarforum.com, where his "Approved Products" list and a "Vendor Review Corner" (843 threads) create community accountability (https://diysolarforum.com/, 2026-09-05). FACT. Gap: no structured written guide library, no sizing calculators, no appliance-runtime reference pages; the forum's FAQ board holds just 14 threads/251 messages vs 21.6K threads in Beginners Corner (https://diysolarforum.com/, 2026-09-05). FACT. Knowledge is scattered across 600K+ forum messages — not consumable as a curriculum. INFERENCE.

**Off-Grid Garage (Andy, Australia)** (https://www.youtube.com/@OffGridGarageAustralia/about, 2026-09-05): 125K subscribers, 703 videos, 23,036,846 views, joined Jul 2020. FACT. Trust engine: long-duration real-world tests, cell-level battery data, published BMS comparison spreadsheet ("an ongoing project and more data will be added") (https://off-grid-garage.com/battery-management-systems-bms/, 2026-09-05). FACT. Nuance vs. my brief's assumption: he *does* have written content — but it is component-test notes organized as shopping/reference pages (BMS, cells, inverters, tools), not step-by-step build guides with load math or wiring plans, and the site nav contains no calculators (https://off-grid-garage.com/, 2026-09-05). FACT (structure) + INFERENCE (gap).

**The Solar Lab (Canada)** (https://www.youtube.com/@TheSolarLab/about, 2026-09-05): 152K subscribers, 119 videos, 27,229,107 views, joined Oct 2023 — fastest growth of the set. Self-described "honest product reviews and clear, easy-to-understand education." FACT. Review/education channel, not a written reference library; no calculator/guide site found in SERPs. INFERENCE.

**Nate's DIY Solar (US)** (https://www.youtube.com/@natesdiysolar/about, 2026-09-05): 10.5K subscribers, 1,529,823 views; "product reviews, DIY solar, and off grid solar projects." FACT. Representative of the long tail: video-first, no written curriculum. INFERENCE.

**Pattern:** trust in this niche is earned by visible measurements on video; none of the four offers a searchable written knowledge base with interactive math. Video answers "what does a teardown show," not "what fuse does *my* 24V 2000W system need." INFERENCE.

## 2) Communities

**diysolarforum.com** (https://diysolarforum.com/, 2026-09-05) — verified structure:
- Beginners Corner & Safety Check: 21.6K threads / 223.4K messages — the largest help venue; live threads on fetch day: "Check on 12V solar system for van build," "Am I doing this right? I designed an off-grid system," "PV Array MPPT Voltage minimum." FACT.
- Recurring pain visible in live titles: wire gauge ("Is 10 awg pv wire good for my setup?"), fusing ("class fuse no flat washer"), controller behavior ("ECO-WORTHY 5kW inverter stops charging at 100%, then starts again around 96–97% — normal?"), brand trust ("Goal Zero?" thread; "EG4 abandoned defective warranty batteries in my garage"). FACT.
- "Up in smoke… learn from my mistake!" board: 519 threads of documented failures. FACT.
- Wind/hydro DIY board exists but is small (254 threads) vs battery/inverter boards (7.5K/5.4K threads). FACT.
- Frustration pattern: answers are conversational and scattered; canonical answers don't exist (FAQ board nearly empty). INFERENCE.

**r/SolarDIY, r/Solar, r/OffGrid:** unreadable this session (login wall). Unresolved blocker; recommend a logged-in manual pass later. FACT.

## 3) Appliance-runtime written SERP

DDG Lite, query "how long will a 100ah battery run a refrigerator" (2026-09-05) — organic results: beacar.com, gridwright.com, rackbattery.com, wattsizing.com, backuppowerexplained.com, batteryruntime.com, outbax.com.au, smartenergyedge.com, portablesolarexpert.com. No major brand, no medical/standards body. FACT (DDG composition).

Fetched examples:
- **rackbattery.com** (https://www.rackbattery.com/how-long-will-a-100ah-battery-run-a-refrigerator/, 2026-09-05): Chinese B2B rack-battery factory blog; answer "12–24 hours"; math = 960Wh usable ÷ 50W ≈ 19h; byline "By admin"; no measured duty-cycle data, no model-level numbers. Thin-to-moderate. FACT.
- **backuppowerexplained.com** (https://backuppowerexplained.com/how-long-will-a-100ah-battery-run-a-refrigerator/, 2026-09-05): the quality bar — 8–16h range, duty cycle 30–50%, surge 600–1,200W, worked example (1,200Wh → 800–900Wh usable → 8–9h), plus free tools (Load Calculator, Battery Runtime Estimator, Appliance Wattage Reference). Small site, ~660 words. FACT. Beating this is achievable with measured, methodology-disclosed content. INFERENCE.

DDG Lite, "what size solar generator to run a refrigerator" (2026-09-05): powerstationlab.com, ankersolix.com (2 URLs), bestgeneratorsolar.com, generatorshop.net, ecowised.com, offgridauthority.com, ecoflow.com — affiliate farms mixed with Anker/EcoFlow brand content. FACT.

DDG Lite, "cpap battery backup power outage how long" (2026-09-05): sleepbackuplab.com (2 URLs), dumbo.health, dreamsleep.ca, udpwr.com, easylonger.com (2 URLs), backuppowerreport.com, medicsolar.com, ampverdict.com — all commerce/niche sites; no clinical authority visible. FACT (composition only; pages not fetched — depth unverified).

## 4) Retailer/blog content

- **EcoFlow blog** (https://blog.ecoflow.com/us/, 2026-09-05): high-cadence, product-led (multiple posts dated 2026-09-01: well-pump generator sizing, sump-pump backup, flood kit; state incentive posts); runs an affiliate program and a forum. FACT.
- **EcoFlow fridge article** (https://www.ecoflow.com/us/blog/what-size-solar-generator-to-run-refrigerator, 2026-09-05): claims fridges "use between 300 and 800W to run" (running-watt framing that overstates a modern fridge's average draw), recommends 1,000–2,000Wh (4,000Wh+ all-day), then pivots to "DELTA Pro Ultra + 2×400W" panels. Generic math, no measured runtimes, no per-model table; ends in product pitch. FACT.
- **Goal Zero blog** (https://www.goalzero.com/blogs/, 2026-09-05): story/brand-led ("Why Outdoor Gear Is the Ultimate Emergency Preparedness Gear," photographer profile, "Dad Camps Yeti 1500 Review") plus one useful piece — "What Can the Yeti 1500 Power? A Comprehensive Runtime and Recharge Guide" — scoped to their own product only. FACT.
- **Jackery:** unverified (404s). No assumption made about parity with EcoFlow.

## 5) Five written-form plays nobody executes well

1. **Measured appliance-runtime matrix with disclosed methodology.** Everyone publishes one formula (Wh ÷ W); only backuppowerexplained.com shows duty-cycle nuance, and nobody publishes a per-appliance measured table. Play: runtime matrix built from public EnergyGuide label data + stated compressor duty-cycle ranges, math shown, calculator embedded — no fabricated lab claims. INFERENCE + plan.
2. **Canonical "decision pages" for the forum's biggest recurring threads.** Beginners Corner's 21.6K threads show demand; the 14-thread FAQ board shows nobody wrote the answers. Play: one authoritative page per decision (fuse size, wire gauge, MPPT-not-charging, 12V-vs-24V) with embedded calculator — the format the client's few winners already prove. FACT (counts) + INFERENCE.
3. **CPAP backup planner grounded in machine specs.** The SERP is 100% commerce sites with no clinical grounding; runtime swings hugely with heated humidifier/tube settings. Play: runtime tables by machine class and humidifier setting, citing manufacturer spec sheets; no "best battery" claims. FACT (SERP) + INFERENCE.
4. **"What a 100Ah battery actually runs" — load-by-load reference.** Current results are single-appliance thin posts by anonymous admins or factories. Play: one reference page with realistic runtime ranges for 15–20 common loads, inverter-loss and depth-of-discharge assumptions stated, interlinked to calculators. FACT (SERP) + INFERENCE.
5. **Winter/worst-week reality guides.** The forum's top active thread is "Quit designing solar setups that inherently need a generator in winter!" (https://diysolarforum.com/, 2026-09-05); retailer blogs only publish product/success stories. Play: written worst-week sizing guides (PVWatts-class reasoning) and safe generator-hybridization pages. FACT (thread) + INFERENCE.

**Ethics/compliance:** all plays are original-calculation content; no scraping, fake testing, or unsupported "best" claims. Amazon Associates compliance points (disclosure placement, link density) flagged for direct verification against the Operating Agreement. ASSUMPTION.

---

**Status / completion contract:**
- Acceptance criteria met: every material claim carries URL + retrieved date or is labeled INFERENCE/ASSUMPTION; no fabricated statistics (zero traffic numbers cited; YouTube counts are platform-public); ethics rules respected.
- **Unresolved blocker:** the harness tool limit hit before I could write the file — `market-research/competitors-diy.md` could not be committed. The full deliverable is above, ready to save verbatim to that path. Also blocked: Reddit reads (login wall), Jackery (404), Google/Bing SERPs (bot walls) — none of these blocked the core analysis; Reddit remains the one recommended follow-up.
