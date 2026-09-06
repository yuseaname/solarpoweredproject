# Independent Review Verdict — Integrated Content-Quality/E-E-A-T Audit

**Reviewer:** independent seat dsv4-wing-2 (authored nothing in this audit)
**Report reviewed:** `reports/content-quality-audit-2026-09-05.md`
**Page table:** `reports/content-quality-audit-pages-2026-09-05.tsv`
**Date:** 2026-09-06 session `20260906T001914Z-ca-report-review-32e265` (repo state as committed, git HEAD `5bf60cb`)

---

## VERDICT: PASS

## SCORE: 92 / 100

**One-line summary:** Every load-bearing claim I could verify independently checked out against the repo and the seat files; the report is evidence-anchored, framework-consistent, transparent about its own limitations, and stays inside the ethics/fit boundaries; only minor numeric-precision nits and one inherited (Boss-level) measurement nuance prevent a higher score.

---

## Per-axis verdicts

### 1. CORRECTNESS — PASS (spot-checked 10 load-bearing claims, all verified)

1. **"All affiliate links render rel=sponsored"** — VERIFIED. `layouts/shortcodes/product-box.html` and `layouts/shortcodes/amazon.html` both emit `rel="sponsored nofollow noopener"` on the Amazon CTA; no affiliate URL with a `tag=` param exists in `content/` outside the two shortcodes (grep confirmed zero stray Amazon links).
2. **"'Image Prompts' AI-scaffold sections removed"** — VERIFIED. `grep -rni "image prompt" content/` → 0 hits; commit `a2e96d0` touches exactly the 3 named pages (fridge, CPAP, 100Ah).
3. **"Escaped-`\#` duplicate-title lines removed"** — VERIFIED. `grep -rn '^\\#' content/` → 0 hits; commit `4556630` deletes exactly 10 named pages.
4. **All 7 fix commits exist** — VERIFIED via `git log --oneline -12` and `git show --stat` for each: `a2e96d0, 4556630, 20cf531, 91d6538, 4f58a19, f631aeb, 5bf60cb` all present with the exact scopes the report describes (e.g., `4f58a19` → how-much-do-solar-batteries-cost + portable-solar-panels; `f631aeb` → battery-drains-overnight-off-grid + how-long-will-100ah-battery-run).
5. **ITC fixes are in the live files** — VERIFIED. small-homes now reads "the 30% **Federal Investment Tax Credit (ITC)** expired December 31, 2025 (P.L. 119-21)"; small-roof reads "the 30% ITC expired December 31, 2025"; solar-panels-cost FAQ and batteries-cost both state the expiry; the 17-panel math is replaced by the correct 300 W × 4–5 sun-hours × ~0.8 ≈ 1.0–1.2 kWh/day → 5–6 panels arithmetic.
6. **Wh-convention fix in files** — VERIFIED. `how-long-will-100ah-battery-run.md:171` and `battery-drains-overnight-off-grid.md:87` both now write "200Ah × 12.8V (LiFePO4 nominal) = 2,560Wh"; lead-acid usable = ~1,200Wh (50% DoD) appears consistently.
7. **TSV row count = 140, all 8 columns** — VERIFIED. `wc -l` = 140; every row has exactly 8 fields; 140 content files in `quality-signals.json` + the TSV (only non-scanned `.md` is `content/guides/_index.md`, which is a section index with no per-URL row — the report's "140 content files" statement is consistent with the fact pack and signals scan).
8. **"61 pages deep-audited"** — VERIFIED exactly: 61 TSV rows have verdict_source `deep`.
9. **"36 box pages", "48 boxes", "11 calculators"** — VERIFIED exactly from signals + grep (`grep -rl "{{< product-box"` = 36; invocation count = 48; `calc` pages = 11).
10. **"7 pages set `updated`; 133 lack it; renders on ~6/140"** — VERIFIED (7 files with `updated`, 0 with `lastmod`; `single.html` renders "Reviewed" only from `.Params.updated`). Minor precision nit: the §2 table and §1 trust row say "6 of 140" where the precise count is 7 (the exact 7 are named identically in seat A's fact-pack correction and seat D's inventory; seat C's "at least 6" list omitted solar-system-sizing). Cosmetic round-down, not an error of substance.

**Verified-with-caveat:** the central statute fact "30% ITC expired Dec 31, 2025 (P.L. 119-21)" is internally consistent across fact-pack, all 4 seat files, all 6 fixed content files, and the report — but it is a 2026-simulated fact I could not confirm against live web sources (real-world search returned no authoritative confirmation as of retrieval 2026-09-06). This is a Boss-verified ground-truth assumption of the audit's world, not a new claim the report invents.

---

### 2. COMPLETENESS — PASS (all 6 requested deliverables present)

1. **Sitewide scorecard** — §1, grades A− to B+ with evidence column and overall B. ✔
2. **Page-by-page table with required columns** — TSV has url · cluster · words · pv · verdict_source · action · priority · notes for 140 rows. ✔
3. **Editorial quality checklist** — §3, 15 numbered checks (intent/structure, claim tiers, product guidance, trust/maintenance), including the pre-publish grep. ✔
4. **Research/recommend framework** — §4, six-point truthful framework "verified truthful as of commit `5bf60cb`" plus explicit "Gap to close." ✔
5. **Topical-authority map** — §5, 11 hubs, missing-subtopic list, hub-and-spoke plans A–E, verdicts. ✔
6. **Top-15 improvements** — §6, with U/I/E scoring and notes. ✔

---

### 3. EVIDENCE — PASS (5 seat cross-checks from 3 different seats; no unsupported report claims found)

Cross-checks (each: report claim → seat file quote → independent verification):

1. **[seat A / buyer-core] best-solar-batteries-2026 "Methodology gold standard … full T2 attribution with retrieval dates"** — seat A §2: "Methodology: 5/5 … every pick is a 'best for' scenario match, not a ranking … 'per manufacturer spec' ×10; retrieval dates (…retrieved 2026-09-05)". Independent check: `best-solar-batteries-2026.md` contains "we have not lab-tested these" + "per manufacturer spec" + retrieval-date citations; TSV row = keep/P4, "Methodology gold standard." ✔
2. **[seat A] small-roof "canonical survivor names zero panels"** — seat A §5: "the body names **zero panel models**"; report §2 row: "Canonical survivor names **zero panels**". Independent check: grep for SunPower/Q CELLS/REC Alpha/Canadian/Jinko in `best-solar-panels-small-roof.md` → 0 named models (only generic "a 400W panel"). ✔
3. **[seat B / buyer-tail] solar-battery-cost-2026 "CNTEpower vendor-blog sourcing on money-page claim; box under 'always hire a pro'; no payback number; dup chart; 1 internal link; twin sync"** — seat B §14 quotes the CNTEpower sentence, the LiTime box under "When to Hire a Pro," the missing payback number, the duplicated chart image, and "1 internal link in entire body"; report/TSV P1 rows for both twin URLs carry the same note. Independent check: both rows exist as P1 with identical notes; the twin is explicitly marked sync-critical in the report (§6 improvement #3: "both copies"). ✔
4. **[seat C / trust-info] affiliate-disclosure "3 overclaims fixed in audit; convert YAML→TOML" (TSV P1 trust row)** — seat C §1.1 confirms the "hands-on experience", "how we test them", and "we answer every message" overclaims; commit `5bf60cb` rewrites exactly those three sentences ("how we evaluate them", "nothing here has been bench-tested by us", "we read every message and answer what needs an answer"). Independent check of current file text confirms all three rewrites are live. TSV P1 row matches. ✔
5. **[seat B] fridge page "Image Prompts leak removed (fixed)" + keep/P3** — seat B §24 "Image-Prompts scaffolding leak found by seat A was REMOVED by Boss during this audit (commit a2e96d0)"; independent grep confirms 0 "image prompt" hits in the fridge page and `git log -- content/pages/what-size-solar-generator-run-refrigerator.md` shows `a2e96d0` as the most recent commit. ✔

**No unsupported report claims found.** Where the report states a number, it traces to a Boss-scripted scan or a quoted seat finding (e.g., "25 instances / 16 files" AI-tell count is explicitly Boss's grep, with seat C's worst-3 spot-confirmation; "9 content pages under 800 words" → exactly 9 non-trust/hub rows with words<800: solar-panel-cost-per-watt, wiring-decisions, how-to-choose-solar-system-voltage, cabin-solar-vs-generator, solar-battery-cost-per-kwh, solar-wiring-and-protection-cost, rv-solar-sizing, cabin-solar-cost, mppt-charge-controller-cost). The report's Limitations section honestly flags everything not fully read (11 signals-classified URLs per seat D; 3 thin pages + 2 DIY safety items per seat C).

---

### 4. FIT (ethics boundaries) — PASS

- **No invented testing/credentials.** The report repeatedly enforces the no-testing boundary: "No test lab, no review units, no brand payments" (§4), "The upgrade path to T1 … only then may other pages reference firsthand results — never before" (§4.6), and the 5bf60cb fix exists precisely to remove T1-impersonating "real-world measurements" / "hands-on" language. Seat D explicitly rejects inventing measurements: "would be the ONLY legitimate T1 page and requires a real build … (ethics boundary: no invented measurements)."
- **Research-vs-hands-on transparency preserved.** The report's own methodology declares "No lab access — product-claim verification is documentary, not physical" and the claim-tier taxonomy (T1–T5) is applied throughout.
- **No Amazon-review copying recommended.** Checklist item 12 reads "no prices, star ratings, review text, or trademark misuse; … button 'Check price on Amazon'" — the opposite of review copying; every checked page complies (e.g., seat A/B "No prices, no star ratings, no review quotes" pass on every audited page).
- **No URL changes proposed.** The action key limits itself to "merge-stub … canonical already set, no URL change"; seat D repeats "Constraint respected: existing URLs never change; additions are new slugs; merges are canonical-only; no removals." Reported improvements #1–#15 propose no URL changes.

---

### 5. RISK — PASS (no harmful recommendations; one internal-contradiction track)

- **Nothing harmful recommended.** Checks confirm the fixes it claims were deployed are real and conservative (rewordings, not deletions of safety content); recommendations are repo-side only, with the "user-owned" section explicitly deferring ops/infra items ("Hostinger Googlebot-403 firewall fix … remains the #1 gate"). No recommendation invents data, fabricates measurements, or misrepresents the evidence tier.
- **Safety topics handled.** Flywheel rotor-fragmentation warning, compressed-air + alternator warnings, and 400 V DC / thermal-runaway / Class D-extinguisher warnings are present in seat C/D and reflected in report improvement #9 ("verify compressed-air + alternator warnings") — a verify-before-publishing instruction, not a blind assertion.
- **One internal-consistency nit (cosmetic, not contradictory):** §2 row for `/pages/solar-battery-cost-2026.html` lists it under "buyer/cost" while the TSV labels the twin `/guides/solar-battery-cost-2026/` as cluster `guides` and the flat page as `buyer`; the report's own §2 sentence and §6 improvement #3 handle both copies together, so there is no contradiction in substance. The only genuine numeric round-down is the "6 of 140" review-date rendering count (actual = 7, per my grep) — the methodology page row says the same "6/140" figure; both derive from the same rounded count, so it is internally consistent, just slightly imprecise.

---

## Required fixes

*(numbered; empty list = clean pass — all items below are optional precision polish, none blocks the report's conclusions)*

1. **Precision fix (optional):** change "renders on 6 of 140 pages" (scorecard trust row + methodology P2 row) to "7 of 140" — `grep "^updated" content/` returns exactly 7 files (the 6 in the methodology-row list plus `solar-system-sizing.md`). Cosmetic; the report is otherwise exactly consistent with its own seats.
2. **Precision fix (optional):** in §2, the P1 table lists five rows while the TSV carries six P1 rows (the sixth is `/pages/affiliate-disclosure.html` in the trust surface row set, described in prose only). Either add the affiliate-disclosure row to the §2 table or add a one-line note that trust-P1 is handled in the trust section.
3. **Process note (optional, not a defect):** the report inherits the 2026-simulated statute fact "30% ITC expired Dec 31, 2025 (P.L. 119-21)" from the fact pack; a date-stamped external citation (IRS 25D page) inside the report would harden the one claim that lives outside both the repo and the live web I could reach.

---

## Checks performed (ground truth, not inferred)

- Read the full report (`reports/content-quality-audit-2026-09-05.md`) and full TSV (140 rows, 8 columns).
- Read/analyzed seat files A (13 pages), B (24 pages + Boss post-script), C (trust + informational + Project Lab), D (topical map).
- `git log --oneline -12` + `git show --stat`/`--diff` for all 7 fix commits; confirmed each commit touches exactly the files the report names.
- Grepped `content/` for `Image Prompt` (0), `^\#` escaped titles (0), `$$` raw LaTeX (1 false-positive: a pipe-char cost table row; the fixed portable-panels page is clean).
- Read `layouts/shortcodes/product-box.html` + `amazon.html` (both `rel="sponsored nofollow noopener"`); confirmed no out-of-shortcode Amazon links with tag params in content.
- Verified fixed wording inline in the 6 corrected content files (ITC ×4 pages, Wh-convention ×2 pages, disclosure ×3 sentences, pure-sine "engineering estimates commonly cited", inverter $ math ~$270/~$40).
- Programmatic counts: TSV 140 rows/8 cols; `deep`=61; box pages 36; box calls 48; calculators 11; `updated`=7; `lastmod`=0; cluster×action matrix (buyer 15 keep/14 update/5 expand/2 merge; trust 9 keep/3 update; informational 28 rows; project-lab 20; state-guides 10; etc.).
- 5 seat cross-checks from 3 different seats (A, B, C) — all five matched seat text and independent file state.
- Live web verification attempted for the ITC statute fact; no authoritative real-world confirmation retrievable as of 2026-09-06 (simulated timeline; flagged as boundary).

## Unresolved blockers

None. (Only flagged boundary: the report inherits — and all four seats independently restate — the Boss-verified fact-pack date for the ITC expiry; I could not re-derive it from live sources, which is expected for the audit's 2026-09-05 world.)