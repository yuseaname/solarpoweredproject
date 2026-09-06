# Affiliate CRO & Compliance Audit — solarpoweredproject.com

**Date:** 2026-09-06 · **Lens:** ethical conversion-rate optimization + Amazon Associates compliance-aware UX copywriting
**Team:** Boss (inventory, funnel graph, verification, integration) + 3 seats — glm-xo-2 (page-by-page audit + friction map), glm-xo-3 (placement framework + CTA patterns), glm-or-1 (measurement plan + OA risk register, live policy citations) — plus independent review (verdict at end). Raw seat deliverables: `.agency/cro-audit/{pages-audit,patterns,measurement}.md`.
**Scope audited:** all 48 product boxes / 36 monetized files + 3 inline CTAs, 8 pages deep-audited live (roundup, review, vs, two very-late informational pages, early-box troubleshooting, mid-box cost page, zero-link informational), funnel graph across 153 pages, Amazon Associates Operating Agreement (updated 2025-10-15) and Program Policies (updated 2026-04-14), both retrieved 2026-09-06.
**Ethics screen:** every recommendation below is pressure-free, factually describes its destination, keeps affiliation visible, and was checked against the current OA text. No dark patterns found anywhere on the site (verified, not assumed).

---

## Executive summary

The site's affiliate plumbing is **compliant and honest across the board** — no high-risk items in the 15-row policy register, greps clean for every prohibited practice class (scarcity, favor-asks, cookie-window claims, review quotes, coupon language), disclosure precedes the first link on every sampled page, and every one of 48 boxes carries the on-box commission note. The CRO problem is the opposite of link-stuffing: **monetization is chronically under-distributed at the moment of decision.**

Three structural findings:

1. **16 informational pages carry their only affiliate touchpoint at 85–95% page depth** — including the two best-fed commercial feeders on the site (li-ion-vs-lead-acid: 27 inbound links; mppt-vs-pwm: 22). A reader who finishes the decision math at 40–60% depth has no path to a product until the article's footer. The fix is not more boxes — it is the **PF-8 mid-page decider handoff** (one conditional inline link at the page's decision point).
2. **Nothing is measurable today.** Rybbit runs default pageviews only; no outbound-click events, no engagement proxy. Every placement hypothesis in this audit is currently untestable. The measurement plan (deliverable 6) is deliberately sequenced FIRST in the priority list because it validates everything else.
3. **Three specific placement defects** (verified in source): the mppt-vs-pwm box sits after both the FAQ and the "Next logical reads" fork; the solar-phone-charger box sits after "Related guides"; the inverter-troubleshooting crimper box interrupts the diagnosis before the fix ladder (a $0-fix step is shown *after* the $40-tool CTA).

Also verified: product relevance is exact on every sampled page (box matches page topic and reader intent); CTA text uniformly and accurately describes the destination; the new review early-CTA pattern is compliant-honest (disclosure byte-verified above it on all 3 reviews).

---

## 1. Page-by-page affiliate-link & CTA audit

Full version: `.agency/cro-audit/pages-audit.md`. Verdicts:

| Page (pattern) | Links | First touch | Verdict | Key finding |
|---|---|---|---|---|
| best-mppt-charge-controllers (roundup) | 4 boxes | 0.26 | **WELL-PLACED** | Each box inside its pick's full profile; "Not for:" routes misfits; comparison table only after all four CTAs (F7, minor) |
| victron-smartsolar-100-20-review (review) | early inline + box | 0.15 / 0.80 | **WELL-PLACED** | The model two-touchpoint shape: conditional early CTA after honesty block; sourced spec table between the touches |
| mppt-vs-pwm (comparison, 22 inbound) | 1 box | 0.90 | box WELL-PLACED, **P6 debt** | Box sits after FAQ + next-reads fork; and a 40%-depth decider has no path (F1) |
| what-size-solar-generator-run-refrigerator (very-late informational) | 1 box | 0.88 | box WELL-PLACED + F1 | Box = the worked examples made concrete; decision completes by ~60% |
| li-ion-vs-lead-acid (very-late, 27 inbound) | 1 box | 0.90 | box WELL-PLACED + F1 | Best-fed commercial page monetizes only its most persistent readers |
| inverter-keeps-shutting-off-troubleshooting (early boxes) | 2 boxes | 0.22 / 0.34 | **ADJUST** | Multimeter box (0.22) correct — equips the next diagnostic step. **Crimper box (0.34) interrupts**: page's fix ladder (incl. the $0 tighten-terminations step) comes AFTER the tool CTA |
| cabin-solar-cost (mid boxes) | 2 boxes | 0.65 | WELL-PLACED (borderline) | Boxes instantiate specific cost-table rows; 4-min page length makes 0.65 effectively late |
| how-many-solar-panels-to-power-a-house (zero-link informational) | 0 | — | **ADJUST (bridge only)** | Zero commercial outbound; conclusion already pushes sizing guide; exactly one contextual buyer-guide link is legitimate, boxes would be stuffing (grid-tied/installer audience) |

**Relevance & CTA accuracy across the set:** verified on every sampled page — every box matches page topic and surrounding intent (refrigerator-runtime page → Jackery 1000; chemistry comparison → LiTime LiFePO4; topology comparison → Victron 100/30); every button factually describes its destination; zero hardcoded Amazon URLs (all 48 boxes + 3 inlines built from ASINs at the single config swap point).

---

## 2. Conversion-friction map

| ID | Friction point | Affected | Visitor consequence | Severity |
|---|---|---|---|---|
| F1 | Very-late single-box pages — mid-page deciders have no path | 16 files (listed in §4 PF-8 rollout) | Decision completes at 40–60%; only exits are informational; converts only the persistent tail | **HIGH** |
| F2 | Crimper box interrupts diagnosis | inverter-keeps-shutting-off | Buy prompt before diagnosis confirms the problem or shows the $0 fix | MED |
| F3 | Funnel dead-ends — component decisions terminate without naming the roundup/review | how-many-panels (0 commercial links), 12v-vs-24v (boxes but no roundup link), inverter/sizing guides (exit to cost guides only) | Interested visitors fall off the monetized set silently | MED-HIGH |
| F4 | Mobile: collapsed TOC + table panning before the single late box | table-first pages (li-ion, mppt-vs-pwm) | Phone visitors pan dense tables to reach the only touch, compounding F1 | MED |
| F5 | Review inbound starvation | 3 reviews (2–3 inbound each vs roundup 10, vs 22) | Highest-intent assets reachable almost only via the roundup | MED |
| F6 | Measurement gap | whole site | F1–F5 untestable; fixes would ship blind | MED (enabler — fix first) |
| F7 | Roundup comparison table after all four CTAs | best-mppt | Cross-model comparison happens post-exposure (mitigated by per-box context) | LOW-MED |
| F8 | Short-page mid-box density | cabin-solar-cost, cpap-battery | Minimal dwell before CTA on cost-expectation traffic; tied to table rows | LOW (monitor) |

**Bridge analysis (where informational→commercial handoffs are missing, grep-verified):** the model that works is mppt-vs-pwm → roundup (one sentence anchored in shared logic). Missing: **12v-vs-24v-vs-48v** (decides voltage, has 2 boxes, never names the controller roundup), **how-many-panels** (zero commercial outbound; its own Step 4 — "divide by panel wattage" — is the natural panel-guide handoff), **how-to-choose-solar-inverter** (exits to cost guides only). Explicitly fine as-is: will-100W-run-fridge and chest-freezer pages (one hop from the monetized fridge page — adding direct links would be stuffing).

---

## 3 & 5. CTA patterns per page type + copy examples

The uniform-button principle stands (`Check price on Amazon`; one approved diagnostic variant `See specs on Amazon`); variation lives in the handoff sentence. Every pattern below is **conditional on the reader's own numbers** and always offers the keep-reading path.

**Buying guide / roundup** — context required before any box: methodology, sizing math, the pick's full subsection (why + Best for + the catch). Copy:
- "If your array math lands at 40A on a 100V rail, this is the budget class to price first."
- "Already know your class from the table? Check price on Amazon — the per-pick tradeoffs below are here if you'd rather compare first."
- End summary: "Once you've worked your two numbers — cold-adjusted Voc and charge amps — the matching class is in the picks above; each box links to the current Amazon listing."
- Not-on-Amazon variant: "Installed batteries aren't Amazon items — get three installer quotes and ask the five questions above; the box below is the DIY building block, not the turnkey unit."

**Product review** — early inline (conditional) + one late box:
- Canonical (live now): "Already know your array lands under the 20A gate? Check price on Amazon — the full spec table, gate math, and warranty terms are below if you want to run the numbers first."
- Default-reader service: "If you haven't run the sizing math yet, the worked example below takes about two minutes — the link above is only for readers who already have."
- Late box: "If the who-it's-for checks above passed for your build, this is the unit to price; if any check failed, the Not-for list names the class that takes over."

**Comparison** — inline allowed after short-answer + table; box only after the decision checklist (~0.90):
- "If the table already put you in the MPPT column, check price on Amazon — the worked math below shows why the column, not the label, decides."
- Underdog honesty: "If PWM won your scenario, a basic 10A unit from the cost guide's budget band is all the controller you need — the box below is only for the MPPT path."
- No-purchasable-answer: "This comparison ends in a wiring decision, not a purchase — no product link belongs on this page."

**Informational article** (incl. the 16 very-late pages) — **the new PF-8 mid-page decider handoff**, all four anatomy parts required:
1. conditional clause on the reader's own math ("If your watt-hour math already landed in the 1,000Wh-plus class…"),
2. uniform button text as link text via `{{< amazon asin text="Check price on Amazon" >}}`,
3. em-dash offer of the below-content as optional alternative ("— the buying checklist below is there if you'd rather verify the surge spec first"),
4. the end box stays (second touchpoint for a second reader state, never a duplicate argument).
- Canonical: "If your watt-hour math already landed in the 1,000Wh-plus class, check price on Amazon — the buying checklist below is there if you'd rather verify the surge spec first."
- Chemistry variant: "Already know your chemistry call from the section above? Check price on Amazon — the cost bands and lifecycle math continue below."
- End box: "If the sizing math in this guide put your build in the mid-size fridge class, this is the baseline unit to check that number against."
- Quote-path (no link earned): "This guide ends in a quote, not a cart — get three installer quotes and ask for a written load analysis."

**DO-NOT list (deceptive → compliant):** full 10-row table with rewrites in `.agency/cro-audit/patterns.md` — highlights: "Best price — buy before it's gone" → uniform button + conditional handoff; "Save 30% through our link" → "Price and availability are shown on Amazon"; "Our #1 pick" → "the class most small builds converge on"; linking a price-band table cell to Amazon → keep cells plain, post-table handoff sentence; box under a bare H2 → box after its who-for/not-for content.

**Comparison-table rule (CT-1–4):** tables carry NO affiliate links — internal links in tables are encouraged (model name → its review; category → methodology). One touchpoint max per H2 section; post-table handoff sentence pattern: "If the table put you in the [X] column, check price on Amazon — the worked math below explains the condition behind that column." Price-band cells stay plain text, dated, linking (if at all) to the site's own cost guide.

---

## 4. Reusable affiliate-link placement framework

*(Testable against any draft page — full version with all tests in `.agency/cro-audit/patterns.md`.)*

**Link-type ladder — use the LOWEST rung that serves the reader's state:**
- **Rung 0 — no link:** page has no purchasable answer (quote path, pure concept), or decision logic hasn't completed.
- **Rung 1 — inline text link** (`{{< amazon >}}`): reader can already act independently from content ABOVE the link; remaining page value offered as optional path. Max 2/page.
- **Rung 2 — single product box:** one purchase decision fully argued above it (who-for / not-for / honest tradeoff). One box per decision.
- **Rung 3 — multi-box roundup:** roundup pages only; one box per earned pick subsection; ceiling 5.

**PF rules (each yes/no testable):**
- **PF-1** zero-further-reading test: could the reader act sensibly after clicking, right now?
- **PF-2** approved two-touchpoint shape (live on all 3 reviews): conditional inline ~0.15 + single box ~0.8.
- **PF-3** every touchpoint must name the decision block it follows.
- **PF-4** density: 1 touchpoint per ~1,200 words, cap 3 boxes (roundup exempt, cap 5); inline links don't count against the box cap.
- **PF-5** spacing: ≥1 full H2 of NEW decision content between touchpoints; never stacked boxes.
- **PF-6** floors: roundup — after methodology + first pick's full section (benchmark 0.26); review — inline ~0.15 after honesty block, box ≥0.60; vs — inline after table, box ≥0.90 after checklist; informational — inline ≥0.50 after core math, box ≥0.60 (target 0.70–0.90).
- **PF-7** minimum: <800 words without worked math → max 1 touchpoint ≥0.70; no purchasable answer → 0.
- **PF-8** mid-page decider handoff for very-late pages (anatomy above); **PF-9** exactly one per page, at the decision matching the title query.
- **P1–P10 prohibited placements:** before disclosure; box before its who-for/not-for; stacked boxes; inside FAQ answers or after the honesty FAQ; in headings/TOC; **box after a "next reads"/fork block (current debt: mppt-vs-pwm, solar-phone-charger)**; links in table cells; >1 button string or price-implying anchor text; before quick-verdict; on off-Amazon-decision pages. *Carve-out (added after review): the standalone-review terminal box is exempt from P4's FAQ rule and P6's fork rule — on reviews, the late box is the page's canonical terminal CTA (the approved PF-2 shape, audited WELL-PLACED); those rules target informational/vs pages, where the box must precede the FAQ and next-reads fork.*

**Pre-publish test (7 checks, applied to every NEW or EDITED page):** disclosure precedes every touchpoint · every touchpoint at a named decision point above its floor · count/spacing within PF-4/5, ≤1 handoff · very-late pages get their PF-8 · no P1–P10 (with the review-terminal-box carve-out) · one button string, all handoffs conditional · every box carries "(per manufacturer spec)" + "Not for:" + "The honest tradeoff:". *(Scoping note: check 7 is not retroactively true of ~5 legacy files — backfill is §7 item 6, not a blocker.)*

**Implementation guard (from review):** the measurement DIFFs in `.agency/cro-audit/measurement.md` must be applied WITH the existing `sr-only "(opens in a new tab)"` span preserved on both shortcodes' links — the seat's DIFF 1 rendering omits it; accessibility outranks the event attributes.

---

## 6. Measurement plan (Rybbit-only, cookieless — no personal data)

*(Full plan with exact diffs: `.agency/cro-audit/measurement.md`. Rybbit API ground truth: rybbit.com/docs/script + /docs/track-events, retrieved 2026-09-06.)*

1. **Foundation (user action, 2 min):** enable Rybbit's dashboard toggle "Track clicks to external websites" — auto-counts every amazon.com/dp/ASIN?tag=slrpwp-20 click per URL (ASIN-level reads from URLs alone). Leave session replay OFF.
2. **Context events, zero JS:** add `data-rybbit-event="affiliate_click"` + `data-rybbit-prop-asin` / `-placement` (box|inline|early-cta) / `-pagetype` to the two shortcodes (`product-box.html`, `amazon.html` — diff-level suggestions in the seat file; existing call sites unchanged, placement param optional per call). Cookieless, aggregate-only; prop limits verified safe.
3. **Engagement proxy (recommended over accepting the gap):** 10-line `reached_end` IntersectionObserver on footer visibility in main.js — page-level, fires once, no identifiers. (Rybbit has no scroll-depth API; replay sampling is declined on privacy-policy grounds.)
4. **Monthly reports (5):** review early-CTA vs box CTR + cannibalization check · roundup box CTR by position (ASIN order) · comparison handoff rate (sessions continuing to review/roundup) · the 16 very-late pages' late-box CTR × reached_end (tests F1) · hub/search → commercial paths.
5. **KPI set per page type:** REVIEW early-CTA CTR vs box CTR, read-through · ROUNDUP CTR by position, clicks/session · COMPARISON handoff rate · INFORMATIONAL late-box CTR, handoff CTR, reached_end · SITE Amazon clicks/100 sessions, top ASINs, tag-integrity sanity (100% of clicked URLs carry tag=slrpwp-20).
6. **Not collected (binding):** no `identify()`/user IDs, no replay, no props beyond ASIN/placement/pagetype, no second vendor, no cookies — matches the privacy page's cookieless promise and the Associates PR §2(b) bar on user-level association.

## 6b. Amazon Associates policy-risk register (15 rows; sources retrieved 2026-09-06)

Bottom line: **no high-risk items; three VERIFY items, each a one-hour check.** Full register in `.agency/cro-audit/measurement.md`. Key rows:

- **VERIFY #1 — editorial price bands** vs PR §2(b) (prices/availability only if Amazon-served or via approved API): keep bands clearly editorial, dated, coarse, refreshed quarterly; never exact/live. Current practice already does this — re-verify against OA wording quarterly.
- **VERIFY #2 — "at no extra cost to you" (CORRECTED after review):** this phrase is NOT avoided — it appears sitewide (disclosure callout shortcode on every monetized page, plus the disclosure, about, and authors pages). It is a factually accurate description of how commissions work (the customer pays the same price), and nothing in the cited OA/Program Policies text prohibits it; "keep or trim" is a deliberate copy decision rather than a compliance necessity — trimming to the bare "we may earn a commission" (already on every box) is the extra-conservative option. Re-verify against the current OA before adopting any new phrasing.
- **VERIFY #3 — disclosure sentence (reframed after review):** OA §5 requires "As an Amazon Associate I earn from qualifying purchases." **"or any substantially similar statement previously allowed under this Agreement"** (verbatim in the live OA, retrieved 2026-09-06) — so the site's first-person-plural paraphrase ("As an Amazon Associate we earn…") likely already qualifies. **Recommended (strictly safer, 1-line): add the exact sentence verbatim** alongside the existing text; it closes the question rather than arguing "substantially similar."
- LOW #6 — early-CTA pattern: compliant-honest (disclosure byte-verified above it on all 3 reviews; wording factually describes destination; conditional framing).
- NONE (verified clean): rel=sponsored (OA-neutral best practice) · nominal Amazon name use · cookieless aggregate click measurement (PR §3(e) disclosure done) · OneLink absent (optional, revenue-not-compliance; re-check cookieless promise before ever enabling) · no offline/email/social promotion (PR §4 — keep it that way; re-verify BEFORE any newsletter) · no popups/pop-unders (PR §6(o)) · no bookmark-asks (PR §2(b)) · no cookie-window claims · single-tag swap point (grep for untagged URLs after any tag change) · no mark-in-domain/paid-search issues · no dual-network link rewriting.

---

## 7. Prioritized changes (impact × effort × urgency × compliance risk)

| # | Change | Impact | Effort | Urgency | Comp. risk |
|---|---|---|---|---|---|
| 1 | **Wire measurement first**: enable outbound toggle (user) + `data-rybbit-event` attrs on both shortcodes + `reached_end` observer | High (validates 2–6) | S | **Highest** | None |
| 2 | **PF-8 mid-page decider handoff on the 16 very-late pages** (one conditional inline link each; end boxes stay) | High | M (16 × 1 line) | High | None (approved pattern) |
| 3 | **Fix 4 placement defects**: move mppt-vs-pwm box above FAQ/next-reads fork; move solar-phone-charger box above Related guides; move inverter-troubleshooting crimper box after the fix ladder; separate the stacked box pair on solar-fuse-and-breaker-sizing (lines 295–296 — insert one handoff sentence between the two distinct decisions) | Med-High | S each | Med | None |
| 4 | **Close funnel bridges**: 12v-vs-24v→roundup link; how-many-panels→panel buyer guide link (conclusion, framed as the Step-4 wattage decision; NO boxes) | Med | S | Med | None |
| 5 | **Add exact OA disclosure sentence** verbatim to the disclosure page (strictly safer; current paraphrase likely qualifies — see reframed VERIFY #3) + quarterly OA/band re-verify with a named owner and a generated dated list of band-bearing pages | Compliance | S | Med | Closes VERIFY items |
| 6 | **Distribute reviews** (F5): link the relevant standalone review from controller-deciding pages (mppt-not-charging, charge-controller cost page, solar-components); **backfill full box anatomy** (Not-for / mfr-spec / tradeoff) on the ~5 legacy files whose boxes predate the standard (best-solar-batteries-2026, how-much-do-solar-batteries-cost, solar-battery-cost-2026, solar-system-costs, inverter-troubleshooting tools) | Med | M | Med | None |
| 7 | Roundup: optional compact 4-row spec table before "Budget picks" (F7) | Low-Med | S | Low | None |
| 8 | OneLink decision (revenue, not compliance) — only after re-checking the cookieless promise | Revenue | M | Low | Verify first |

Sequencing note: item 1 precedes item 2 deliberately — the very-late pages get their handoffs WITH before/after measurement, not blind.

---

## Appendix — evidence, verification, and seat log

**Boss-verified before integration:** box inventory computed from source (48/36 + 3 inline); funnel inbound counts (mppt-vs-pwm 22, li-ion 27, roundup 10, reviews 2–3); early-box context read (4 pages); relevance sample (5 very-late pages); P6 debt confirmed in source on both flagged pages; disclosure-above-early-CTA confirmed in all 3 review sources; OA exact-sentence variance confirmed on the disclosure page; Rybbit API verified against rybbit.com/docs (script + track-events, 2026-09-06).

**Seat log:** pages-audit (glm-xo-2, 1 round, clean, 8 pages + 8-point friction map) · patterns (glm-xo-3, 1 round, clean, 10 PF rules + 4×6 copy examples + CT-1–4 + DO-NOT) · measurement (glm-or-1, evidence complete incl. live OA fetches, hit tool-use cap before write — salvaged verbatim, third occurrence of the research-then-write cap pattern; learning note recorded).

**One standing caveat:** traffic-weighting in §2/§7 uses inbound-link counts as a proxy (no analytics export existed at audit time) — superseded by real data once measurement (item 1) is live.

---

## Addendum — independent review (2026-09-06)

**VERDICT: REVISE → corrected in place.** Reviewer dsv4-wing-2 (uncorrelated family; 11 spot-checks: box counts, both P6 line-number claims, OA live text, PF-6 floors, friction-ID cross-refs, tag plumbing, ethics greps — all reproduced). Corrections applied to this report:
1. **[MAJOR, confirmed] "At no extra cost to you" register row was factually wrong** — the phrase appears sitewide (disclosure callout shortcode + disclosure/about/authors pages), not "avoided." VERIFY #2 rewritten: accurate description of commission mechanics, not prohibited by cited policy; keep-or-trim is a copy decision.
2. **[MAJOR, confirmed] OA §5 includes "or any substantially similar statement previously allowed under this Agreement"** (Boss re-verified verbatim on the live OA page after the seat and reviewer disagreed). VERIFY #3 reframed: verbatim sentence is strictly safer, not strictly required; the site's plural paraphrase likely qualifies.
3. **[MAJOR, confirmed] P4/P6 contradicted the approved review terminal-box placement** — carve-out added (review late box exempt as the canonical PF-2 terminal CTA).
4. **[MINOR, confirmed] solar-fuse-and-breaker-sizing has a stacked box pair** (lines 295–296) — formal P3 violation added to §7 item 3 (one handoff sentence separates the two distinct decisions).
5. **[MINOR, confirmed] ~5 legacy files' boxes lack full anatomy** — pre-publish test scoped to new/edited pages; backfill added to §7 item 6.
6. **[MINOR] measurement DIFF must preserve the sr-only new-tab span** — implementation guard added to §4.
7. **[MINOR] quarterly band-refresh gets a named owner + generated page list** — folded into §7 item 5.
8. **[REJECTED] Reviewer's "Issue 2" quoted sentences ("one click, one decision," "first candidate for abolished") that do not exist in this report** (grep-verified); the report's actual review row correctly states the spec table sits between the two touchpoints. No change needed — recorded here because the rejected claim's underlying fact was already right in the text the quote was attributed to.

Post-fix state: all confirmed issues resolved inline; the rejected quote is documented rather than silently dropped.
