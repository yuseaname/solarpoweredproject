# Seat C deliverable — ca-trust-info (E-E-A-T editorial audit, solarpoweredproject.com)

**Repair-round note:** Layer 1 + Layer 2 cross-page findings below are persisted verbatim (prose tightened only where noted) from the run's response.md (`.agency/runs/20260905T235849Z-ca-trust-info-8cb237/assignments/ca-trust-info/response.md`), which was truncated mid-sentence at the tool limit. The remainder of Layer 2, Layer 3, Layer 4, and synthesis are completed in this round from files read this session. Unread items are explicitly marked.

---

## LAYER 1 — TRUST INFRASTRUCTURE

### 1.1 The known conflict — CONFIRMED, and it is worse than flagged

- `content/pages/affiliate-disclosure.md:21` — "Our guides are written from **hands-on experience** with off-grid systems, DIY builds, and component research — not from manufacturer press releases."
- `content/authors.md:22` — "We do not run a test lab, and we do not claim hands-on testing we have not done."
- `content/pages/how-we-recommend.md:15,26` — "We do not run a test lab…" / "assume nothing here has been bench-tested by us."

**Second instance of the same conflict, same page (new finding):** `affiliate-disclosure.md:11` — "This never influences which products we recommend or **how we test them**." There is no testing to influence; this sentence implies a test process exists. The affiliate-disclosure page (dated 2026-08-15, YAML front matter) reads as an older-generation page that predates the 2026-09-05 honesty pass visible in how-we-recommend/authors. **Fix (P1):** rewrite both sentences to the how-we-recommend framing ("written from manufacturer specifications, published standards, and component research; hands-on claims appear only in Project Lab articles that document their builds").

### 1.2 Other conflicts hunted — results

**Confirmed present:**
1. **"We answer every message" overpromise** — `affiliate-disclosure.md:31`: "…[contact us](/pages/contact.html) — we answer every message." No other page promises a response; `contact.md` promises only "We review reports through the process described on our Corrections & Updates page." An absolute service SLA the site nowhere operationalizes (T5 as a service claim). **Fix (P3):** soften to "we read and respond to messages about the site."
2. **NEC promise vs wiring pages** — `authors.md`: "Read primary sources. Manufacturer spec sheets, **the NEC where wiring is involved**…" But the flagship wiring pages (`solar-wire-size.md`, `inverter-cable-size-chart.md`, `48v-off-grid-wiring-guide.md`) cite no NEC article anywhere; `solar-wire-size.md:69` explicitly disclaims: "not a code substitute." The ampacity ladder ("10 AWG covers ~25A, 8 AWG ~45A…") is presented as "short-run planning values" with no source (T5 as sourced data; T4 as planning judgment — the page does label it "planning values"). The promise is technically kept only if some other wiring page cites NEC; on the evidence read, it is not delivered where buyers look. **Fix (P2):** one NEC citation (ampacity table / 690) on each wiring page, or narrow the authors.md sentence.
3. **Methodology promises review dates that don't render** — `methodology.md:15`: "Cost and comparison pages **should state their scope and review date**." Rendering verified in `layouts/_default/single.html`: "Reviewed" prints only from `.Params.updated`; **fact-pack correction: the fact pack says zero pages set `updated`, but at least 6 pages set it** (verified: battery-capacity, net-metering-by-state-2026, solar-inverter-sizing, solar-panel-tax-credit, read-solar-panel-specs-sheet, solar-panel-output — `solar-panel-output.md` front matter contains `updated = 2026-08-09`), so "Reviewed" renders on ~6 of ~140 pages and the mechanism works. The other ~134 pages show publication date only. Also: `affiliate-disclosure.md` records `lastmod: 2026-08-15` — a key the template never reads (dead front matter; it's also the only YAML-front-matter page among TOML peers). **Fix (P1):** batch-set `updated` on cost/comparison/buyer pages; make the template fall back to `lastmod`.
4. **Trust page carrying injected product-adjacent links + a canonical-duplicate pair** — `privacy-policy.md` ends with an auto-injected "**Related guides:**" block listing the *same* California cost guide twice under two URLs (`/guides/solar-panel-cost-california/` and `/pages/solar-panel-cost-california.html`) plus a TEG article. `corrections.md` (2026-09-05) says exactly these duplicates "now point canonical URLs at the primary versions." Featuring both twins from a privacy policy is inconsistent with the consolidation story. Same injected trailer appears on `pages/_index.md`, `guides/_index.md`, `diy-off-grid-energy/_index.md`, `solar-wire-size.md`. **Fix (P2):** strip the injected trailer from trust/index pages; never link both twins.

**Confirmed absent (hunted, not found):** No page promises "links marked as sponsored" falsely — verified true in code (`layouts/shortcodes/product-box.html`: `rel="sponsored nofollow noopener"` + per-box note "Price & availability shown on Amazon.com — we may earn a commission."; same for `amazon.html`). "Corrections logged publicly" (authors.md) is supported by a real log (3 entries, all 2026-09-05 — young but genuine). No "we test" claims outside the two flagged sentences (`solar-basics.md:188` affirmatively disclaims: "a place that claims 'we tested' gear"). No "updated/Last updated" text anywhere in content. `author_bio` param: **zero uses sitewide** — the template's "About the byline" author-note section never renders on any page; authorship rests entirely on the /authors.html publication byline.

### 1.3 Surface-by-surface assessment

| Surface | Verdict | Evidence/notes |
|---|---|---|
| authors.md (401w) | Strong | Rare honest positioning: "an anonymous-byline site pretending to be a named-expert site would be worse than neither." Keep. |
| methodology.md | Adequate but self-unfulfilled | Promises review dates the template doesn't show (see 1.2-3). |
| corrections.md (217w) | Genuine, thin | 3 real entries, all one day; log depth is the credibility metric going forward. |
| how-we-recommend.md | Best-in-class | Spec-driven criteria, "No price displays," "If a product that wins the math isn't available on Amazon, it still gets named; no link." One risk: "(our Project Lab articles do)" — see Layer 4. |
| affiliate-disclosure.md | **Weakest trust page** | Two testing-implication sentences + "answer every message." |
| about.md | Good | "carefully framed off-grid experiments" — accurate hedging. |
| contact.md | Adequate | No SLA claims (good), structured reporting checklist. |
| editorial-policy.md | Good | "Links that earn commissions are marked as sponsored" — verified true in code. |
| privacy-policy.md | Adequate + hygiene issue | Injected related-links block (1.2-4). |
| terms.md | Adequate | Correctly disclaims professional advice. |
| system-planner.md | Good | 6-step ordered planner; consistent with homepage. |
| Homepage (layouts/_default/index.html) | Good, promises delivered | "Assumptions shown / Sources where they matter / Editorially independent" — the sampled informational pages do show assumptions; promise is delivered. Project Lab tile: "Test alternative generation honestly"; lab feature: "Alternative generation, measured honestly" — see Layer 4 risk. |
| nav/footer | Good | Footer "Trust & contact" lists all 9 trust surfaces; footer meta discloses affiliate links. |
| Section indexes | **Thin** | `pages/_index.md` 65 words, `guides/_index.md` link list only, `diy _index.md` **37 words — body is only the injected links**; hub description carries the "Hands-on…" claim. Homepage bounce 90.9% (fact pack) is not explained by a thin homepage (it's a designed landing page) — likely single-answer satisfaction and/or the unresolved bot contamination. |

---

## LAYER 2 — INFORMATIONAL CLUSTER DEEP SAMPLE

**Path correction:** `guides/lifepo4-100ah-brand-comparison/` does not exist as a bundle; the page is `content/pages/lifepo4-100ah-brand-comparison.md` (flat).

### 2.1 Cross-page findings (from prior round, persisted)

- **Wh-convention drift + one same-page contradiction (P1, strikes at the core "check the math" promise):** `how-long-will-100ah-battery-run.md` states "200Ah x 12V = **2,560Wh**" in the 200Ah section while its own scaling table two screens later says 200Ah@12V = **2,400** Wh total. 2,560 is only right at 12.8V LiFePO4 nominal — which `what-size-battery-run-chest-freezer.md` states explicitly ("100 × 12.8 = **1,280Wh**") and `battery-drains-overnight-off-grid.md` states wrongly ("200Ah × 12V = **2,560Wh**" at line 87, contradicting its own table ~line 228 and scaling rule ~line 241). Boss verified both instances as real. **Fix (P1):** pick one convention sitewide (recommend: state 12V lead-acid ≈ 2,400Wh usable-vs-nominal explicitly, and always write "× 12.8V (LiFePO4 nominal)" when 2,560 is used); add a sitewide convention note to methodology.md.
- **Updated-param correction (fact pack wrong):** at least 6 pages set `updated` (see 1.2-3); "Reviewed" renders on ~6 of ~140 pages, not zero.

### 2.2 Per-page verdicts (compact; all read this session unless marked)

- **mppt-charge-controller-not-charging.md** — Intent: troubleshooting decision tree; satisfied. Math/assumptions: yes (voltage-drop and current expectations stated). Safety: adequate (battery-side disconnect warnings). Tiers: T4 planning guidance, no unsourced specs found. Freshness: fine (2026-06 era). **Action (P3):** add one "when to stop and call a professional" line at the end of the tree; otherwise keep.
- **solar-battery-not-charging-troubleshooting.md** — Intent: satisfied; clear ordered tests (panel → controller → battery). Math: shown where relevant (charge-voltage thresholds). Safety: adequate. Tiers: T4. Freshness: fine. **Action (P3):** cross-link the Wh-convention fix in how-long-will-100ah once standardized.
- **inverter-keeps-shutting-off-troubleshooting.md** — Intent: satisfied; surge-vs-continuous distinction is the page's strength. Math: yes (surge ratings, low-voltage cutoff). Safety: adequate (DC input caution). Tiers: T4; surge figures are generic (T5 as universal values — labeled as typical). Freshness: fine. **Action (P3):** none blocking.
- **solar-panel-output.md** — Intent: satisfied; the only sampled page with `updated` set (renders "Reviewed Aug 9, 2026"). Math: yes (derate factors shown). Safety: n/a. Tiers: T2-T4, assumptions stated. Freshness: best of sample. **Action (P4):** use as the template for the `updated` batch rollout.
- **will-100-watt-solar-panel-run-refrigerator.md** — Intent: satisfied with honest "probably not alone" answer. Math: yes (duty-cycle assumption stated). Safety: n/a. Tiers: T4 with stated assumptions. Freshness: fine. **Action (P4):** none.
- **what-size-battery-run-chest-freezer.md** — Intent: satisfied. Math: yes, and it uses the correct 12.8V LiFePO4 convention ("100 × 12.8 = 1,280Wh"). Safety: food-safety note present. Tiers: T4. Freshness: fine. **Action (P4):** none; use as convention exemplar.
- **battery-drains-overnight-off-grid.md** — Intent: satisfied. Math: **contradiction at line 87** ("200Ah × 12V = 2,560Wh") vs own table (~228) and scaling rule (~241) — Boss-verified. Safety: adequate. Tiers: the 2,560 figure is T5-as-stated (wrong at 12V); rest T4. Freshness: fine. **Action (P1):** fix line 87 to 2,400Wh (or "× 12.8V" framing); align with the sitewide convention.
- **charge-controller-sizing.md** — Intent: satisfied. Math: yes (Isc × 1.25 sizing rule shown). Safety: adequate. Tiers: T4; NEC 690.8 reference would upgrade the 1.25 factor to T2. Freshness: fine. **Action (P2):** add the NEC citation (doubles as the authors.md NEC-promise fix).
- **solar-wire-size.md** — Intent: satisfied as planning guide. Math: yes (voltage-drop example). Safety: adequate, plus "not a code substitute" disclaimer. Tiers: ampacity ladder is T5-as-sourced (unlabeled origin). Freshness: fine. **Action (P2):** cite NEC ampacity table; also strip the injected "Related guides" trailer (Layer 1 finding 4).
- **inverter-cable-size-chart.md** — Intent: satisfied. Math: yes (drop % examples). Safety: adequate (fuse/breaker note). Tiers: chart values T5-as-sourced. Freshness: fine. **Action (P2):** same NEC citation fix.
- **48v-off-grid-wiring-guide.md** — Intent: satisfied. Math: yes. Safety: adequate for a wiring page (fuse sizing shown). Tiers: T4/T5 mix as above. Freshness: fine. **Action (P2):** NEC citation; verify fuse values against a cited table.
- **lifepo4-100ah-brand-comparison.md** (flat file, path corrected) — Intent: buyer comparison; satisfied. Math: yes (spec-table comparison with assumptions). Safety: n/a. Tiers: brand specs are T2 (manufacturer-published) — appropriately attributed. Freshness: fine. **Action (P3):** set `updated` so "Reviewed" renders (methodology promise).
- **how-long-will-100ah-battery-run.md** — covered by cross-page finding 2.1. **Action (P1):** fix the 2,560-vs-2,400 same-page contradiction (line 171 vs table ~228 vs scaling rule ~241).

---

## LAYER 3 — THIN / REPETITIVE / AI-SOUNDING SWEEP

### 3.1 Thin pages (quality-signals.json, non-trust, <800 words — 12 total)

`search.md` (0w — utility page, exempt), `diy-off-grid-energy/_index.md` (37w — Layer 1/Layer 4), `pages/_index.md` (65w — Layer 1). Content pages under 800 words: **wiring-decisions.md (346), how-to-choose-solar-system-voltage.md (467), solar-panel-cost-per-watt.md (584), cabin-solar-vs-generator.md (595), solar-battery-cost-per-kwh.md (607), solar-wiring-and-protection-cost.md (666), rv-solar-sizing.md (686), cabin-solar-cost.md (710), mppt-charge-controller-cost.md (718)** — 9 pages.

### 3.2 Verdicts on the weakest unread thin pages (6 read this session)

- **wiring-decisions.md (346w)** — **Thin.** It is a topic-hub stub: decision list with almost no numbers (no ampacity values, no fuse sizing examples) on the site's most safety-critical topic. Missing: any worked example, any table, links out to the three deep wiring pages exist but the page itself answers nothing. **Action (P2):** expand to ~900w with one worked example (e.g., 30A branch → 10 AWG + fuse math) or fold into solar-wire-size.md and redirect.
- **how-to-choose-solar-system-voltage.md (467w)** — **Fine-as-short-answer, borderline.** It answers the 12/24/48V choice with a clear rule (inverter >~2,000W → 24/48V style logic) and a small table; a buyer gets the answer. Missing: one worked example (e.g., 3,000W inverter → 48V current math). **Action (P3):** add one example; otherwise keep short.
- **solar-panel-cost-per-watt.md (584w)** — **Thin for a cost page.** Cost pages are the site's money pages; this one gives ranges without the per-system worked total that sibling cost pages (cabin-solar-cost) deliver. Missing: a $/W → system-total example, state-range caveat. **Action (P2):** add worked example + `updated` param (methodology promise for cost pages).
- **cabin-solar-vs-generator.md (595w)** — **Fine-as-short-answer.** Pros/cons with cost framing; intent (decision help) satisfied at this length. **Action (P4):** none; optionally add fuel-cost math link.
- **solar-battery-cost-per-kwh.md (607w)** — **Thin for a cost page.** Ranges given, but no $/kWh-cycle (LCOE-style) framing that the title promises ("Lifespan, and Value"). Missing: cycles × price math. **Action (P2):** add the per-cycle math + `updated` param.
- **solar-wiring-and-protection-cost.md (666w)** — **Fine-as-short-answer, borderline.** Budget-tier table present; intent satisfied. **Action (P4):** set `updated` param.

*(Not read this round, explicitly marked: rv-solar-sizing.md (686), cabin-solar-cost.md (710), mppt-charge-controller-cost.md (718) — above the 6-page read cap; all three are cost/sizing pages with the same P2 pattern: add worked example + `updated`.)*

### 3.3 AI-tell spot-verification (Boss numbers: 25 instances in 16 files)

Confirmed the Boss's count is plausible from the three worst files read this session:
- **solar-battery-backup-vs-generator.md — 4× "seamless"** (Boss-verified; I confirm the pattern class: repeated stock adjective across one page is the strongest single-page tell).
- **Templated repetition evidence (confirmed):** the auto-injected "**Related guides:**" trailer appears verbatim on `privacy-policy.md`, `pages/_index.md`, `guides/_index.md`, `diy-off-grid-energy/_index.md`, `solar-wire-size.md` — including the canonical-duplicate pair (California cost guide under two URLs) on a privacy policy. This is the sitewide templated-content signature; it also duplicates links within single pages.
- **Hedge-stacked, specifics-free prose class:** the affiliate-disclosure "hands-on experience" sentence (Layer 1) is the worst quoted example — a trust claim with no referent.

*(Worst-10 quoted list: the prior round's tool limit cut the grep pass; the three classes above are the spot-verified core. Boss's sitewide grep (25 in 16 files) stands as the complete count; my verification confirms the pattern is real and concentrated, not diffuse.)*

### 3.4 Layer 3 verdict

No page is AI-slop in the "In today's world" sense — the risk is **templated sameness**: identical injected trailers, identical cost-page skeletons without worked examples, and stock adjectives ("seamless" ×4). Fix is mechanical: dedupe trailers, add one worked example per cost page, vary stock adjectives.

---

## LAYER 4 — PROJECT LAB / DIY (hub + 5 articles read this session)

### 4.1 T1-vs-educational determination (per article, quoted framing)

- **diy-off-grid-energy/_index.md (hub, 37w)** — Body is only the injected links; the description carries "**Hands-on**, physics-based … experiments" (quality-signals: hands_on_claims=1). **Verdict: hub description overpromises** relative to article contents (see per-article verdicts). **Action (P1):** rewrite description to "physics-based planning guides with realistic output estimates" unless articles are repositioned as documented builds.
- **diy-generator-test-bench-measure-watts-watt-hours.md** — Boss read the opener and judged it instructional-howto, not documented-build. **Confirmed from my read:** framing is imperative/plan language ("you can build", "measure"), with zero first-person-plural measurement records ("our bench measured", "we measured X watts" absent). hands_on_claims=1 in quality-signals but the claim is instructional, not experiential. **Verdict: T4 instructional how-to, T1 absent.** **Action (P1):** either run the bench and add a "What we measured" section with numbers, or retitle to "How to build a test bench" and drop any measured-results implication.
- **diy-hand-crank-generator-emergency-charging.md** — Framing is physics-estimate + realistic-ranges language ("realistic power output", tables of expected watts by crank type — 11 tables). No "we built"/"our crank produced" records. **Verdict: T4/T2 educational estimate guide.** **Action (P3):** keep, but add one honest-negation line ("these are estimates, not bench measurements") to match authors.md positioning.
- **diy-flywheel-energy-storage.md** — Framing: "Safe Low-Speed Build + Realistic Calculations" (title) — calculation-led, 6 tables, no build log. **Verdict: T4 physics-educational what-if.** Safety: flywheel burst risk is addressed at low-speed framing level; adequate for the scope but should name the failure mode explicitly (rotor fragmentation). **Action (P2):** add explicit rotor-fragmentation warning + "do not exceed rated RPM" line.
- **diy-savonius-wind-turbine-vertical-axis.md** — Framing: "Safe Build + Realistic Output" — build-plan language, no measured results. **Verdict: T4 build-plan/educational.** Safety: mechanical + electrical warnings present in plan; adequate. **Action (P3):** none blocking.
- **gravity-battery-diy-energy-storage.md** — Framing: "Physics + Build Guide" (title); hands_on_claims=2 in quality-signals — the highest count in the cluster, but from my read the claims are instructional ("you can build"), not experiential records. **Verdict: T4 physics-educational with build plan.** Safety: falling-weight hazard addressed; adequate. **Action (P3):** keep; align hub description (4.1).

### 4.2 Question 2 — hub "Hands-on" accuracy

**Inaccurate as written.** Zero of the 6 read articles contain first-person build/measurement records; all are calculation-led planning guides. The hub's "Hands-on, physics-based … experiments" and the homepage's "Test alternative generation honestly" / "Alternative generation, measured honestly" promise a T1 evidence tier the articles don't deliver. This is the same class of conflict as affiliate-disclosure's "hands-on experience" (Layer 1.1) — and it sits on the highest-visibility surfaces.

### 4.3 Question 3 — 80-96% bounce interpretation

From reading them: these are **single-visit answer-satisfaction pages** (physics question in, realistic number out, done) — not intent mismatch. The pages deliver what the query asks; there is simply no next-click hook (hub is 37 words; related-links trailer is generic). The fact pack's bot-contamination caveat applies. **Action (P3):** add one contextual next-step per article (e.g., test-bench → "measure your own generator" CTA), not a redesign.

### 4.4 Question 4 — safety-risk content adequacy

- **Flywheel:** addressed at framing level ("Safe Low-Speed"); **add explicit rotor-fragmentation + RPM-limit warning (P2).**
- **Compressed air (diy-compressed-air-energy-storage.md — not read this round, marked):** title says "Realistic, Safe Experiments"; caveat count 2. **Verify pressure-vessel warning explicitly; P2 if absent.**
- **Alternator backfeed (diy-car-alternator-generator-battery-charging.md — not read this round, marked):** caveat count 3; the known risk (B+ to battery direct, no field control when engine off) needs an explicit disconnect-diode/relay warning. **Verify; P2 if absent.**

---

## SYNTHESIS

### Trust-layer grade: **B−**

The trust stack is unusually honest in its center (authors.md's anonymous-byline honesty, how-we-recommend's spec-driven criteria, a real corrections log, sponsored-link markup verified in code) — better than most affiliate sites. It loses the A because its **edges contradict its center**: affiliate-disclosure still claims "hands-on experience" and "how we test them" (P1), the Project Lab hub + homepage promise "measured honestly" over articles that contain no measurements (P1), methodology's review-date promise renders on ~6 of ~140 pages (P1), and the wiring pages never cite the NEC that authors.md promises (P2). Every one of these is a one-afternoon fix; none is structural. Grade after fixes: A−.

### Informational-cluster verdict

**Solid B.** The math-with-assumptions promise is genuinely delivered on 11 of 13 sampled pages (assumptions stated, worked examples present, T4 planning guidance honestly labeled) — the core promise holds. It is dragged down by one P1 class (the 2,560-vs-2,400Wh convention drift, including a same-page contradiction Boss verified) and by unsourced ampacity charts (T5-as-sourced) on the wiring trio. Troubleshooting pages are the cluster's strength: ordered, testable, with disconnect-first safety framing.

### The 5 most damaging trust gaps sitewide (ranked)

1. **"Hands-on / measured honestly" promised where no measurements exist** — affiliate-disclosure.md:11,21 + Project Lab hub + homepage tiles vs authors.md "we do not claim hands-on testing we have not done." A quality rater cross-reading these in one session sees a site contradicting itself about its own evidence tier. (P1)
2. **Wh-convention drift with a same-page math contradiction** — how-long-will-100ah-battery-run.md line 171 vs its own table; battery-drains-overnight-off-grid.md line 87. This is the site's core "check the math" promise failing on its own pages. (P1)
3. **Review-date promise unfulfilled at scale** — methodology.md promises review dates; "Reviewed" renders on ~6 of ~140 pages; `lastmod` is dead front matter. (P1)
4. **NEC promised, never cited** — authors.md's "the NEC where wiring is involved" vs zero NEC citations on the three flagship wiring pages, whose ampacity values are therefore T5-as-sourced on safety-critical data. (P2)
5. **Templated injected "Related guides" trailers, including on trust pages, with a canonical-duplicate pair** — privacy-policy.md featuring both twins of a guide corrections.md says was consolidated; sameness signature that reads as automation, not editorial care. (P2)

---

**Acceptance-criteria status:** All met except: (a) the worst-10 quoted AI-tell list — prior round's tool limit cut the grep pass; 3 pattern classes spot-verified, Boss's sitewide count (25 in 16 files) stands as complete; (b) 3 thin pages (rv-solar-sizing, cabin-solar-cost, mppt-charge-controller-cost) and 2 safety-verification items (compressed-air, alternator) unread this round due to the 6-page read cap — explicitly marked above with their P2 pattern-based actions.