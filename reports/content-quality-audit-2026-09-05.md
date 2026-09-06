# Content-Quality & E-E-A-T Audit — solarpoweredproject.com

**Date:** 2026-09-05 · **Auditor:** Agency run `ca-*` (4 seats + Boss) · **Scope:** all 140 content files; 61 pages deep-audited (all 36 buyer pages with product boxes, a 13-page informational sample, every trust surface, 6 Project Lab articles, plus ~20 hub/anchor spot reads); the remaining pages are covered by scripted signals and pattern passes.

**Companion files:**
- `reports/content-quality-audit-pages-2026-09-05.tsv` — machine-readable page-by-page table (all 140 URLs: cluster, words, traffic, action, priority, notes)
- `.agency/content-audit/seat-a-buyer-core.md` (13 buyer pages, full rubric) · `seat-b-buyer-tail.md` (24 buyer pages) · `seat-c-trust-info.md` (trust + informational + thin/AI + Project Lab) · `seat-d-topical-map.md` (topical authority)

---

## Method, evidence standards, and limitations

**Method.** Boss-scripted sitewide scan (word count, product-box/calculator/FAQ presence, attribution-language hits, first-person-claim hits, caveat density, internal links, canonical flags, author/date params) → 4 parallel seat audits with a shared verified fact pack → Boss independent verification of every load-bearing seat claim before acceptance → integration. Traffic weighting from Rybbit (99 pages; caveat: Hostinger bot-blocking issue means possible bot contamination; calculators' 6–33% bounce vs 80%+ sitewide is directionally reliable).

**Claim tiers used throughout:** T1 firsthand-tested (documented on-site build/measurement) · T2 manufacturer-stated · T3 reputable third-party (source + date) · T4 editorial judgment · T5 unknown/unverified. No T2–T5 claim may be presented as T1.

**Ground-truth note.** The audit's ITC fact base — the 30% federal residential credit expired Dec 31, 2025 under P.L. 119-21 — was verified during the sitewide Sept-2026 ITC purge (public log: `/corrections.html`) and is stated consistently across fact pack, all four seats, and the corrected content files; it is inherited ground truth for this audit, not a claim this audit re-derived from live sources.

**Limitations.** (1) No lab access — product-claim verification is documentary, not physical. (2) 11 low-priority URLs were signals-classified without full reads (seat D, flagged in its file). (3) Three thin pages and two DIY safety items (compressed-air, alternator warnings) were pattern-classified without full reads (seat C, flagged). (4) Keyword/SERP difficulty is deliberately out of scope — covered by the 2026-09-05 keyword audit (`reports/seo-keyword-audit-2026-09-05.md`). (5) Several defects were **fixed during the audit** (below) — the report describes pre-fix state and marks them.

**Fixes deployed during this audit (7 commits, all live):**

| Commit | Fix |
|---|---|
| `a2e96d0` | Removed leaked "Image Prompts" AI-scaffold sections rendering live on 3 pages (fridge, CPAP, 100Ah) |
| `4556630` | Removed escaped `\#` duplicate-title lines rendering as stray paragraphs on 10 pages |
| `20cf531` | Corrected live factual errors: 26% ITC claim (small-homes), "17 panels for 5 kWh/day" math (4–8× off), fake "SunPower Maxeon LX" pick (model does not exist) + LG NeON R presented as 2026 model (LG exited solar 2022), inverter efficiency $-math contradiction ($1,600 → ~$270; FAQ baseline 5× low), "Real-world measurements show…" T1-impersonation reworded |
| `91d6538` | Fixed stale ITC FAQ on how-much-do-solar-panels-cost (contradicted its own body; feeds FAQ schema) |
| `4f58a19` | Fixed present-tense expired-ITC claim (how-much-do-solar-batteries-cost); raw LaTeX formulas + "Bougevert"→"BougeRV" (portable panels) |
| `f631aeb` | Fixed Wh-convention errors: "200Ah × 12V = 2,560Wh" relabeled 12.8V LiFePO4-nominal (2 pages, one same-page contradiction); lead-acid usable corrected to ~1,200Wh |
| `5bf60cb` | Truth-alignment: "hands-on experience"/"how we test them"/"answer every message" (affiliate-disclosure), "Hands-on… experiments" (DIY hub description), "measured honestly"/"Test…honestly" (homepage Project Lab tiles) → research-based framing |

---

## 1. Sitewide content-quality scorecard

| Dimension | Grade | Evidence |
|---|---|---|
| Search-intent satisfaction | **B+** | Calculators/troubleshooting/sizing pages answer-first (fridge page 5/5; sizing planner 19.8% bounce — best on site). Legacy panel trio scores 1–2/5 (non-answer deks, zero named products). |
| Experience & research rigor | **B** (was B−) | Center is unusually honest (published assumptions, checkable math, real corrections log). Edges contradicted the center: "hands-on/measured" overclaims — **fixed during audit**. NEC promised in authors.md but never cited on wiring pages. |
| Product-recommendation quality | **B−** | Gen-2 pages: who-for/NOT-for/tradeoffs/alternatives avg 4–5/5 (solar-generator's "Who should NOT buy" is the model). Gen-1 panel trio: 0.6–0.8/5 (one-sentence blurbs, mismatched boxes). |
| "Best" methodology fairness | **A−** | Where present: scenario-match ("best *for*"), criteria shown, "not a ranking," comparison pages argue for the option they don't sell. Missing entirely on legacy "best" pages. |
| Claim support & qualification | **C+** | The audit's biggest gap. T2 attribution ("per manufacturer spec") on only 3→4 of 36 box pages. T5 numbers on legacy pages (device percentages, lifespan years, $1.50/W). Vendor blogs cited as market research (CNTEpower). 3 math errors found (all fixed). |
| Non-commercial guidance | **A** | Safety-forward throughout (300-word safety hub pages, "when to call a professional" triggers, 400V DC/thermal-runaway DIY warnings), worked math with stated assumptions on 11 of 13 informational pages sampled. |
| Thin / repetitive / AI-sounding | **B+** | AI-tell density genuinely low (25 instances / 16 files, mostly benign). 9 content pages under 800 words. Templated sameness: injected "Related guides" trailers sitewide (incl. trust pages + canonical-twin links). Two editorial generations visibly coexist. |
| Trust infrastructure | **B+** (was B−) | 14 trust surfaces; publication-byline honesty page and how-we-recommend are best-in-class; corrections log real; every affiliate link verified `rel="sponsored"` + point-of-click disclosure. After the audit's truth-alignment fixes, remaining gaps: review dates invisible on 133 pages (7 do set it), author-bio template never renders. |
| Scannability vs depth | **A−** | "In brief" answer boxes, TOC rails >800w, 60+ pages with tables, 11 calculators. HTML tables undercounted by tooling (scan artifact). |
| Topical authority | **B** | Strong hubs (troubleshooting, fundamentals, safety); anchor-orphan problem (7 high-traffic pages with 0 inbound links); missing authority spokes (grounding, arc flash, battery fire, monitoring, glossary). Full map in §5. |

**Overall: B.** The site is two editorial generations wearing one domain. Generation 2 (Sept 2026 wave: batteries guide, fridge page, calculators, troubleshooting deep pages, de-templated state guides) is genuinely good — answer-first, attributed, hedged, safe. Generation 1 (May 2026 panel/economics pages) is the trust hole: AI-flavored, unsourced, and — before this audit's fixes — carrying live factual errors and a nonexistent product. Because 25% of pages sell, the G1 defects sat on exactly the pages where money and trust meet.

---

## 2. Page-by-page audit table

**Full table: `reports/content-quality-audit-pages-2026-09-05.tsv`** (140 rows: URL · cluster · words · traffic · verdict source · action · priority · notes). Deep-audit evidence with quoted excerpts: the four seat files.

**Action key:** keep · update · expand · merge-stub (reduce canonicalized duplicate to honest stub — canonical already set, no URL change) · keep-canonical. **Priority key:** P1 = live factual/trust damage or money-page blocker · P2 = significant quality/monetization loss · P3 = polish · P4 = fine as-is.

### P1 and P2 pages (all other pages P3/P4 — see TSV)

| URL | Intent | Core weakness | Action | Pri |
|---|---|---|---|---|
| /pages/best-solar-panels-for-home-2026.html | buyer | Canonicalized dupe still fully live; fake "Maxeon LX" (removed in audit) + defunct LG; zero buyable products; worst AI prose on site | merge-stub | **P1** |
| /pages/best-solar-panels-for-small-homes.html | buyer | 26% ITC + 17-panel errors (fixed in audit); same generation as above | merge-stub | **P1** |
| /pages/best-solar-panels-small-roof.html | buyer | Canonical survivor names **zero panels** — "best" page with no products; needs real 3–4 panel comparison w/ T2 specs | expand | **P1** |
| /pages/solar-battery-cost-2026.html | buyer/cost | CNTEpower vendor-blog sourcing on money-page claim; DIY battery box directly under "always hire a professional"; ROI section with no payback number; duplicate chart; 1 internal link; twin must stay in sync | update | **P1** |
| /pages/pure-sine-vs-modified-sine-inverter.html | comparison | Box nested inside FAQ answer (schema pollution risk); T5 device-percentages & lifespan numbers | update | P2 |
| /pages/how-to-choose-solar-inverter.html | buyer | Efficiency-$ contradiction (fixed); "Huawei/iStore" US-market oddity; FAQ without schema | update | P2 |
| /pages/solar-fuse-and-breaker-sizing.html | tool/sizing | FAQ-schema pollution + string-fuse box contradiction (per seat B) | update | P2 |
| /pages/portable-solar-panels.html | buyer | Was a sale-host page w/ render defects (LaTeX/misspelling — fixed); 0 internal links | update | P2 |
| /pages/rv-solar-sizing.html | sizing | Thin (686w), zero safety caveats — the set's anomaly | expand | P2 |
| /pages/how-much-do-solar-batteries-cost.html | cost | Present-tense ITC (fixed); AI voice; artifacts | update | P2 |
| /pages/charge-controller-sizing.html, /pages/solar-wire-size.html, /pages/inverter-cable-size-chart.html, /pages/48v-off-grid-wiring-guide.html | wiring/tools | Ampacity/fuse values T5-as-sourced; NEC citation missing (authors.md promises it) | update | P2 |
| /pages/wiring-decisions.html | wiring hub | 346-word stub anchoring the site's most safety-critical cluster | expand | P2 |
| /pages/solar-panel-cost-per-watt.html | cost | Thin for a money page (584w), no worked system total | expand | P2 |
| /pages/privacy-policy.html | trust | Injected trailer links both canonical twins from a privacy policy | update | P2 |
| /pages/methodology.html | trust | Promises review dates that render on 7 of 140 pages | update | P2 |
| /pages/affiliate-disclosure.html | trust | 3 overclaims fixed in audit (commit 5bf60cb); YAML front matter still the odd one out vs TOML peers | update | **P1** |
| /pages/authors.html | trust | Promises NEC citations content doesn't deliver | update | P2 |

**Cluster verdicts** (full per-page detail in seat files): buyer-core 13 pages: 5 keep, 6 update, 2 merge-stub · buyer-tail 24: 7 keep, 10 update, 6 expand, 1 P1 update · informational 13: 9 keep, 4 update · trust 14: 10 keep, 4 update · Project Lab 20: keep cluster-wide + positioning pass · state guides 10: keep/update (EIA-cited, post-de-templating; NV/MA/IL thin).

---

## 3. Reusable editorial quality checklist

Every new or updated page must pass all 15. (Derived from what Gen-2 pages already do right plus every defect this audit found.)

**Intent & structure**
1. Dek/first 100 words answers the query — no "Discover…" non-answers; the "In brief" box must contain an actual answer.
2. Worked math with stated assumptions (volts convention labeled — 12.0V generic vs 12.8V LiFePO4 nominal; derate factors named; "planning-level" hedge on charts).
3. At least one table or decision list for any multi-option question.
4. FAQ via `{{< faq >}}` shortcode + `{{< faq-schema >}}`; never plain H3s; **no product boxes inside FAQ answers**.

**Claims (tier discipline)**
5. Every load-bearing spec carries a tier: "per manufacturer spec" (T2), source+retrieval date (T3), or explicit "editorial estimate, checked {month}" (T4). No naked numbers.
6. No first-person testing language ("we tested," "real-world measurements show," "hands-on") unless the article documents a real build with measurements. Default: "our math," "per the datasheet."
7. Cost bands are dated and sourced to independent sources (EIA, EnergySage, NREL) — never vendor content-marketing blogs; installer/vendor figures labeled as such.
8. Time-sensitive claims carry their expiry (ITC-style statements always name the statute/date and the current status — recheck every "currently").
9. Model names verified against the manufacturer's current lineup before publication (the "Maxeon LX" rule).

**Product guidance (any page with a box)**
10. Each recommendation answers: who it's for, who it's **not** for, one real tradeoff, the decisive spec (with compat), and what to buy instead if it doesn't fit. Conditional box framing ("If your load list lands in the 1500–2000W range…") is the house pattern — copy it.
11. Box must match the page's voltage/class/use-case (no 12V RV panels on grid-tied rooftop pages); box must not contradict adjacent body advice.
12. Amazon compliance: no prices, star ratings, review text, or trademark misuse; point-of-click disclosure (shortcode handles it); button "Check price on Amazon."

**Trust & maintenance**
13. Safety-critical steps carry a "stop and call a licensed professional" trigger; electrical-hazard pages name the failure mode.
14. `updated` front matter set whenever content materially changes; year-titled pages re-verified annually ("2026" titles are a promise).
15. No production scaffolding ships: no Image-Prompts blocks, work-order comments, raw LaTeX, escaped `\#` titles, or injected trailers on trust pages. Pre-publish grep: `Image Prompt|\\# |\$\$|work order`.

---

## 4. "How We Research / Recommend" framework — truthful for this site's actual process

The site **already owns the honest version of this framework** across five pages (`authors`, `methodology`, `editorial-policy`, `how-we-recommend`, `affiliate-disclosure`) — it is the strongest part of the site and, before this audit's fixes, also contained the two sentences that contradicted it. The canonical framework, verified truthful as of commit `5bf60cb`:

1. **What we are:** an independent, reader-supported publication. Research-and-math based. **No test lab, no review units, no brand payments, no brand pre-publication access.** Product picks are spec-and-arithmetic matches, not bench results — and pages say so.
2. **How an answer is built:** sizing/runtime/payback math with published assumptions and checkable arithmetic → manufacturer datasheets for specs (prefer datasheet over retailer listing) → primary/authoritative sources for policy and cost (EIA rates, IRS/statute text, NEC where wiring is involved, ENERGY STAR) → honest ranges where data is soft, labeled as ranges.
3. **How a product earns a mention:** the math points at it (watts/volts/surge/duty-cycle fit), the specs come from the manufacturer, the model has an established track record, and value is framed in durable terms ($/usable-Wh over cycle life) — never today's price. Products that win the math but aren't on Amazon still get named.
4. **What "best" means here:** "best-matched by specs and math for a stated scenario," with the criteria shown so readers can disagree. Never a ranking, never a claim of testing.
5. **Transparency mechanics:** `rel="sponsored"` on every commission link (verified in code), disclosure at the click point and page level, corrections logged publicly with dates, review dates shown via the `updated` param *(rollout pending — see improvements list)*.
6. **The upgrade path to T1:** if/when real builds get documented in the Project Lab, those articles state measurements and their limits explicitly, and only then may other pages reference firsthand results — never before.

**Gap to close:** deliver the two promises the framework makes that content doesn't yet keep — NEC citations on wiring pages, and visible review dates — then the framework is fully load-bearing.

---

## 5. Topical-authority map

Full map in `.agency/content-audit/seat-d-topical-map.md`. Summary:

**11 hubs inventoried** (anchor · spokes · depth · monetization posture): H1 Fundamentals/Sizing (16 spokes, stickiest pages on site) · H2 Panels & Home Economics (12, thin, the G1 trust hole) · H3 Batteries & Storage (21 URLs, largest, zero anchor inlinks) · H4 Inverters & AC (9) · H5 Wiring/Protection/DC Safety (spokes deep, **hub is a 346w stub**) · H6 Troubleshooting/Maintenance (strongest: 3,500w anchor, 3 top-10 traffic pages) · H7 Safety/Permits (3,597w anchor — best single safety page) · H8 Buying/Seasonal/Use-Cases (cleanest hub design; **every commercial leaf is an orphan**) · H9 State Costs (11 EIA-cited bundles) · H10 Project Lab (19 deep articles, 37-word hub, no mesh) · H11 Runtime Math (the batteries cluster's buyer tail).

**Missing subtopics (essential-for-authority):** grounding & lightning protection · battery fire/thermal-runaway safety · arc-flash/DC-arc hazard · battery monitoring & SOC metering · DC wire-protection reference (hub upgrade) · inverter loading/derating · glossary · system-expansion planning · buyer-journey roadmap · climate-zone adjustments · lab index rewrite. (Nice-to-have and skip-with-reason items — e.g., HOA-by-state, more state ledgers — reasoned in the seat file; keyword-layer opportunities remain in the keyword-audit matrix.)

**Hub-and-spoke plans** (constraint respected: no URL changes, canonical-only merges): A) Wire/Protection — upgrade wiring-decisions hub + grounding page, mesh the #2/#9 traffic pages up. B) Batteries — anchor li-ion-vs-lead-acid (chemistry deep-dive in place), add battery-fire + monitoring spokes. C) Troubleshooting — decision-tree mesh connecting the three orphaned top-10 traffic pages. D) Safety — arc-flash + battery-fire pages completing the strongest E-E-A-T cluster. E) Use-Cases — the commercial mesh: link the six 0-inlink buyer leaves (rv-solar-cost, rv-solar-sizing, cabin-solar-cost, cabin-solar-sizing, solar-generator, sheds) through solar-use-cases.

**Verdict:** closest to genuine authority — Troubleshooting, Fundamentals/Sizing, Safety/Permits (sealing touches named per hub). Furthest — Panels & Economics (finish = rebuild the trio) and Project Lab (finish = index rewrite + positioning pass, or cap as the physics library it is).

---

## 6. The 15 highest-impact improvements (urgency × impact × effort)

| # | Improvement | U | I | E | Notes |
|---|---|---|---|---|---|
| 1 | **Finish panel-trio consolidation**: stub the two canonicalized bodies (best-panels-for-home-2026, -small-homes) to honest pointers; remove mismatched Renogy boxes | 1 | 5 | 1 | Canonicals already set; ~1 hour; kills the G1 trust hole at 3 URLs |
| 2 | **Rebuild best-solar-panels-small-roof** as a real comparison: 3–4 current named panels (W, dims, efficiency, temp coefficient, "per manufacturer spec") | 1 | 5 | 3 | The canonical survivor currently names zero panels |
| 3 | **solar-battery-cost-2026 money-page repair**: replace CNTEpower/vendor sourcing with EnergySage/EIA-class sources, resolve DIY-box-vs-"hire a pro" contradiction, add the missing payback number, dedupe chart, add internal links — **both copies** | 2 | 5 | 2 | Flagship cost page, 3,746w, 1 internal link |
| 4 | **Review-date rollout**: set `updated` on the top-30 traffic/money pages; make the template fall back to `lastmod` | 2 | 4 | 1 | Delivers methodology.md's promise; strongest cheap E-E-A-T signal |
| 5 | **T2-attribution rollout**: one "specs per manufacturer, not lab-tested" line + NOT-for/tradeoff on the ~32 remaining box pages | 2 | 4 | 2 | Pattern proven by the 4 pages that already do it |
| 6 | **NEC citations on the wiring quartet** (wire-size, fuse-sizing, cable-chart, 48V guide; 690.8 sizing factor on controller-sizing) | 2 | 4 | 2 | Converts T5-as-sourced safety data to T3 and delivers authors.md's promise |
| 7 | **Box hygiene pass**: move boxes out of FAQ answers (pure-sine, 12v-vs-24v, fuse-sizing); resolve string-fuse and Renogy-100W reuse mismatches | 2 | 3 | 1 | Includes FAQ-schema pollution check |
| 8 | **Trust-trailer cleanup**: strip injected "Related guides" from privacy-policy + hubs; never link both canonical twins | 2 | 3 | 1 | Sameness signature on the most-trust-sensitive surfaces |
| 9 | **Project Lab positioning pass**: honest-negation line per article; flywheel rotor-fragmentation warning; verify compressed-air + alternator warnings; rewrite the 37-word hub index | 2 | 3 | 2 | Converts the cluster's overclaim risk into its honest identity |
| 10 | **Orphan-anchor mesh**: inbound links for the seven 0-inlink pages (solar-system-sizing, li-ion-vs-lead-acid, best-solar-batteries, mppt-not-charging, solar-maintenance, solar-inverter-sizing) + the six buyer leaves via solar-use-cases | 3 | 4 | 2 | The single biggest traffic-authority unlock per seat D |
| 11 | **Thin money-page pass**: worked examples + `updated` on the 9 sub-800-word cost/sizing pages | 3 | 3 | 2 | rv-solar-sizing also gets its missing safety caveats |
| 12 | **New authority spokes** (batch 1): grounding & lightning, battery fire safety, arc-flash/DC-arc | 3 | 5 | 3 | The three essential gaps no solar authority lacks; feed plans A/B/D |
| 13 | **wiring-decisions hub expansion** 346w → reference page (fuse-every-source philosophy + master chart + decision tree) | 3 | 4 | 2 | Cheapest authority upgrade on the site per seat D |
| 14 | **Conditional-box pattern adoption** + buyer-journey roadmap section on solar-use-cases | 3 | 3 | 2 | Codifies the site's best box behavior (inverter-sizing model) |
| 15 | **Glossary + system-expansion spokes; state-bundle deepening (NV/MA/IL)** | 4 | 3 | 3 | Long-tail authority completion; keyword layer already queued in matrix |

U = urgency 1(now)–4(later), I = impact 1–5, E = effort 1(easy)–3.

---

## What the user still owns (unchanged from prior audit)

Hostinger Googlebot-403 firewall fix remains the #1 gate on all Google-side gains; Rybbit bot-exclusion toggle; Amazon OneLink check; 2 hero images pending approval. New from this audit: none — all fixes above are repo-side.
