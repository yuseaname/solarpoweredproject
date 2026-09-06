# UX, Accessibility & Trust Audit — solarpoweredproject.com

**Date:** 2026-09-05/06 · **Auditor lens:** skeptical first-time visitor researching solar/off-grid products
**Team:** Boss (recon, verification, integration) + 3 agency seats — glm-xo-3 (persona journeys, live fetches), dsv4-wing-1 (WCAG 2.2 AA audit, repaired round 2), glm-xo-2 (trust signals, 10 live fetches) — plus independent review (see verdict at end).
**Method:** repo inspection (layouts, CSS both layers, shortcodes, JS, 153 pages' front matter), live-site fetches (HTTP status, titles, rendered HTML, byte-offset disclosure/link checks), WCAG contrast computation (sRGB), git-date verification. Raw seat deliverables: `.agency/ux-audit/{fact-pack,journeys,accessibility,trust}.md`.
**Ethics screen:** No dark patterns, fake trust signals, or fabricated authority recommended anywhere in this report. Two live defects that violated the site's own honesty standard were removed during the audit (documented below as applied hotfixes, with before/after). Accessibility and clarity ranked above monetization in every severity call.

---

## Executive summary

The site's UX foundation is **unusually strong for an affiliate property**: task-first homepage, zero ads/popups/overlays, disclosure-before-link verified in HTML on every monetized page sampled, a real dated corrections log that matches live content, `rel="sponsored"` on every affiliate link, 48px thumb-friendly CTAs inline with decision content, and 0-click paths from landing to first Amazon button after value. The three persona journeys all end in "trust: high."

The defects that matter are **truth-consistency and legibility**, not manipulation:

1. **CRITICAL (fixed during audit):** a leftover lead-gen pitch on the site's flagship informational page offered a service that doesn't exist ("Contact our team… free, customized solar assessment" + a dead "[Get Your Free Solar Quote Now]" placeholder).
2. **HIGH:** Google Analytics loads sitewide but is undisclosed in the privacy policy (which discloses only Rybbit + hypothetical AdSense) — cookies with no consent mechanism.
3. **HIGH:** two WCAG AA contrast failures on the highest-traffic text classes: `--muted` gray (4.06:1) used for breadcrumbs, bylines, dates, and the commission note *directly under every Amazon button*; and white-on-orange primary CTAs (3.82:1).
4. **HIGH (fixed during audit):** five root pages rendered "Published Jan 1, 0001" — including two trust pages (authors, corrections).
5. **MEDIUM:** the buyer loop has gaps that cost conversion without harming trust — the roundup never links to the site's own standalone reviews, no page puts even an editorial price band in the comparison table, calculators don't announce results to screen readers, and the disclosure page claims display ads run (none do).

One finding from my own recon was **retracted after seat verification**: `/terms.html` is not a soft-404 — it is a correct noindex meta-refresh alias to the real `/pages/terms.html` (see Appendix).

---

## 1. User-journey audit

### 1a. First-time informational visitor ("how many solar panels to power a house")

**Journey:** Google → `/pages/how-many-solar-panels-to-power-a-house.html`. Within one viewport: task-named nav, kicker, H1, dek, and a meta row with Published/Updated dates and reading time — *what the site covers, who it's for, and freshness are answered in ~5 seconds*. Scroll reveals the system brief strip, a 14-link TOC, an "In brief" box, then genuinely useful content: the 12-month kWh method, worked formula (10,000 kWh ÷ 365 ÷ 4.5 → 16×400W panels), three home profiles. Zero ads, zero affiliate links on the page.

**Moment of truth — was:** trust high for 90% of the journey, then **broken at the finish line**: the Conclusion offered a fake team assessment and a dead bracket-placeholder CTA. That single paragraph retroactively poisoned the honesty of every number above it (and contradicted the homepage trust strip "Editorially independent").

**Applied hotfix #1 (this audit):** removed the fabricated pitch + placeholder; replaced with an honest close: *"Next step: run your own numbers in the solar system sizing guide, then use them to sanity-check any installer proposal you receive."* Also fixed two credibility typos in the "Practical Tips" section preceding the Conclusion ("Determarily" → "Determining"; "Return on On Investment" → "return on investment").

**Remaining friction (URL + location):**
- "In brief" box repeats the dek word-for-word (both render `description`) — second touchpoint adds nothing. (U-19)
- End-of-article stack = three competing next-step blocks (related list + "Next decision" chips + related cards). (U-20)
- Breadcrumb/byline/date row at .72rem in 4.06:1 muted — provenance signals are the least legible text on the page. (U-2)
- System brief strip is identical generic copy on all non-lab pages. (U-17)

**Verdict (post-fix): trust high, path visible.** A skeptical first-timer gets the math, the assumptions, and a named next decision.

### 1b. Buyer comparing products (MPPT charge controllers)

**Journey:** roundup (`/pages/best-mppt-charge-controllers.html`) → review → vs page. Disclosure callout appears **before any product content** (byte-verified: ~4.4 KB ahead of the first affiliate link on the roundup; ~9 KB on reviews). Methodology block within 1.5 viewports: "this is a spec-based comparison — we have not bench-tested these controllers… not a ranking." Sizing math taught before picks. Every product box carries "Not for:" and "The honest tradeoff:" *before* its button — a buyer can disqualify a pick in one sentence. Spec tables carry per-row "retrieved 2026-09-05" dates.

**Click/scroll to first Amazon link (value-first check):**
- Roundup: **0 clicks, ~1.5–2 viewport scrolls** (first CTA at ~49% page depth, after methodology + sizing + first full profile).
- Review: **0 clicks, ~3.5–4 scrolls** (single CTA at ~80%, after verdict, sourced spec table, worked math, who-for/not-for, warranty, FAQ — including a flat "No." to "Did you test this?").
- Vs page: 0 clicks, CTA at ~81%.

**Friction (the gap is completeness, not integrity):**
- **Zero links from the roundup to the standalone reviews** (verified 0 occurrences in HTML; the Victron 100/30 review exists and the path is one-way). (U-9)
- **No price signal anywhere in decision content**: table shows "Budget/Mid-range" classes only; bands live in prose elsewhere; the buyer's #1 question ("what does this actually cost?") forces a detour or an Amazon trip. Editorial, dated price *bands* are house-legal and unanswered. (U-10)
- Identical CTA label ×4 boxes with no differentiation; "Common buying mistakes" (strong pick-changing content) sits after all four CTAs. (U-10/U-21)

**Verdict: trust high, convert likely** — a price-band row and roundup→review links would make it "confident."

### 1c. Mobile visitor ready to click to Amazon

*(Reasoned from verified CSS facts + live stylesheet + fetched HTML; seat cannot render a phone — limitation stated.)*

**What works:** sticky 64px header with a 44×44 aria-wired hamburger (focus management, Escape close); menu panel shows item name *and* description; product boxes render full-width 48px-min CTAs exactly where the decision happens; tables pan horizontally without breaking layout; **nothing overlays content** — no popups, cookie banners, sticky bars; the only `position:fixed` element is the hidden skip link. CTA opens Amazon in a new tab with `rel="sponsored nofollow noopener"` and the commission note was already under the button.

**Friction:**
- **TOC wall:** on ≤900px the sticky rail becomes a static 12–14-link list in-flow *before* "In brief" — the answer and first box arrive ~a viewport late. (U-14)
- **The commission note under every CTA is .68rem muted at 4.06:1** — the disclosure line is the hardest-to-read text on the screen at exactly the moment it matters most. (U-2, overlaps accessibility)
- Primary CTA contrast 3.82:1 — a legibility problem in sunlight, not just a WCAG number. (U-3)
- Review page's single deep CTA (≈4+ viewports) means some ready-to-buy users tap out via the related roundup instead; an early compact exit after the Quick verdict would serve the already-convinced without interrupting anyone. (U-15)
- 4-column spec table on ~390px requires panning past the warranty row — the decision-maker column. (U-16)

**Verdict: trust high; converts from roundup boxes; slower on review pages.**

---

## 2. UX/trust scorecard by page type

Scale 0–10 per dimension: **C**larity (5-second comprehension) · **S**cannability · **T**rust signals · **D**ecision support · **M**obile/legibility.

| Page type | C | S | T | D | M | Notes |
|---|---|---|---|---|---|---|
| Homepage | 9 | 9 | 8 | 8 | 8 | "What are you trying to power?" paths are best-in-class; trust strip is claim-only until byline question resolved |
| Hub pages (guides, planner, search) | 8 | 8 | 7 | 7 | 7 | Zero-date artifact fixed; search limited to title+description index |
| Informational guide | 8 | 8 | 8 | 8 | 7 | Post-hotfix; "In brief"=dek duplication; system-strip boilerplate |
| Roundup | 8 | 7 | 9 | 7 | 7 | Methodology + not-for copy strong; no prices, no review links |
| Vs-comparison | 8 | 8 | 8 | 8 | 7 | Table at ~35% depth; takeaways first; table panning on mobile |
| Standalone review | 9 | 8 | 10 | 9 | 7 | "Did you test this? No." is the strongest honesty signal on the site |
| Calculator pages | 8 | 8 | 8 | 9 | 7 | Labeled inputs; results not announced to screen readers; no inputmode |
| Trust pages (about/authors/methodology/corrections/contact/privacy/terms) | 8 | 8 | 8 | n/a | 7 | Real corrections log verified live; privacy/disclosure pages carry the U-4/U-6 truth defects — see Week 1 |
| 404 | 9 | 9 | 8 | 8 | 8 | On-brand, two recovery actions |
| Global (nav/footer/disclosure plumbing) | 9 | 8 | 8 | 8 | 7 | All landmark/aria work verified; footer Terms link works via alias hop |

**Site-wide distinctives (verified, keep):** no overlays of any kind · disclosure-before-link in HTML · on-box commission note · `rel="sponsored nofollow noopener"` sitewide · centralized affiliate tag · skip link + focus-visible ring + reduced-motion · real 404 handling · sticky-nav a11y done right.

---

## 3. Prioritized issue list

### Critical
| ID | Issue | Status |
|---|---|---|
| U-1 | Fabricated installer-service pitch + dead "[Get Your Free Solar Quote Now]" placeholder, `how-many-solar-panels-to-power-a-house.md` Conclusion — contradicts editorial-independence claim; only occurrence sitewide (grep-verified) | **FIXED during audit** (hotfix #1, before/after in §1a) |

### High
| ID | Issue | Evidence |
|---|---|---|
| U-4 | Google Analytics gtag (G-GLZVS6799J) loads sitewide; privacy policy discloses only Rybbit + hypothetical AdSense; GA sets cookies with no consent mechanism | live HTML incl. privacy page itself; `hugo.toml` param + `head.html:24-30` |
| U-2 | `--muted #77766d` = **4.06:1** on paper (4.49:1 on surface) — AA fail on breadcrumbs, byline/date row, product-note (commission disclosure under every CTA), footer-meta, system-strip labels, all at .64–.72rem | computed + `design-system.css` |
| U-3 | `.button-solar` white on `#d65e2b` = **3.82:1** — AA fail on the primary "Check price on Amazon" CTA (~14.4px bold) | computed |
| U-5 | "Published Jan 1, 0001" on 5 root pages (authors, corrections, methodology, system-planner, search) — broken dates on trust pages — **FIXED during audit** (hotfix #2: real git first-commit dates added) | live-verified |

### Medium
| ID | Issue |
|---|---|
| U-6 | Privacy/disclosure truth-alignment: affiliate-disclosure page states "We also run display advertising (Google AdSense)" as present fact; no ads run (no `adsense.client_id`, zero ad markup live) |
| U-7 | Calculators (5): results not announced (`aria-live`/`role=status` absent), numeric inputs lack `inputmode="decimal"`, no error-message pattern |
| U-8 | Rendered tables lack `th scope` (Hugo default); wide tables not keyboard-scrollable (no focusable wrapper) |
| U-9 | Roundup→review link gap: 0 inbound links from `/pages/best-mppt-charge-controllers.html` to the standalone reviews it summarizes |
| U-10 | No editorial price-band row in roundup/review/vs decision tables (prose bands exist elsewhere; house standard permits labeled, dated bands) |
| U-11 | New-tab Amazon links carry no "opens in new tab" indication (visual or SR-only) |
| U-12 | Byline credibility ceiling: entity byline on all 113 pages, no humans named — honest per authors page, but capped vs named-reviewer competitors; truthful remedies only |
| U-13 | Search index covers title+description+section only; body-text queries miss |
| U-14 | Mobile TOC wall: static 12–14-link list precedes "In brief" and first CTA (~1 viewport delay) |
| U-15 | Review pages have no early compact CTA after the Quick verdict for already-convinced buyers (single CTA at ~80% depth) |

### Low
| ID | Issue |
|---|---|
| U-16 | 4-column spec tables on ~390px viewports: warranty row (decision-driver) sits mid-pan |
| U-17 | System brief strip renders identical generic copy on every non-lab page |
| U-18 | Small standalone targets (TOC, breadcrumb, footer links) rely on text height alone (<24px hit area) |
| U-19 | "In brief" box duplicates the dek verbatim (both render `description`) |
| U-20 | Triple end-of-article next-step stack (related list + chips + cards) |
| U-21 | "Common buying mistakes" (pick-changing content) placed after all CTAs on the roundup |
| U-22 | Repeated "Read guide →" link text ×3 (purpose clear from context; polish) |
| U-23 | Footer Terms href goes through the alias hop (works; direct `/pages/terms.html` is cleaner) |
| U-24 | Contact page states no response-time expectation (add only if truthful) |

---

## 4. Recommendations (location · rationale · implementation)

**Applied during this audit (before/after):**
1. **U-1** — removed fabricated quote-service pitch + dead placeholder; honest "Next step" close pointing to the sizing guide; 2 typos fixed. *File: `content/pages/how-many-solar-panels-to-power-a-house.md`.*
2. **U-5** — added `date = 2026-08-10` (git first-commit date) to `authors.md`, `corrections.md`, `methodology.md`, `system-planner.md`, `search.md`.

**Highest-leverage next (all low-risk, reversible):**
3. **U-4 — GA decision (owner gate).** *Rationale:* privacy page is factually wrong today; GA + cookieless Rybbit is redundant measurement. *Preferred implementation:* delete `google_analytics` from `hugo.toml` (removes gtag sitewide, zero content loss). *Alternative if GA stays:* name Google Analytics in the policy (cookies set, purpose), and gate non-essential cookies behind consent for EEA/UK traffic. Either way the policy must match reality.
4. **U-6 — make the disclosure page true.** `content/pages/affiliate-disclosure.md`: change "We also run display advertising (Google AdSense)" to "We do not currently run display advertising" (or future-tense "may"), aligning `privacy-policy.md` wording in the same edit.
5. **U-2 + U-3 — two-token contrast fix (single CSS PR).** `assets/css/design-system.css`: `--muted: #77766d` → `#6b6a62` (verified 4.83:1 paper / 5.35:1 surface); `.button-solar` background → `var(--orange-deep)` (white = 6.02:1), hover can deepen to `#7d301a`. Verify no other rule re-declares these tokens (theme layer check).
6. **U-9 — close the roundup loop.** In `best-mppt-charge-controllers.md`, link each pick's product name to its standalone review (Victron 100/30 now; EPEver/Renogy as they ship), and link the reviews' "Alternatives" back. Zero new content needed.
7. **U-10 — add dated editorial price-band rows.** One table row per roundup/review/vs table: "Typical price band (editorial estimate, Sep 2026): $–$" with the existing as-of-line convention. No live prices (Amazon-served pricing only, per house rule).
8. **U-7 — calculator operability.** `layouts/shortcodes/toolscript.html`: wrap result output in `role="status" aria-live="polite"`; add `inputmode="decimal"` to numeric inputs; define a visible error summary pattern with `aria-describedby`.
9. **U-8 — table render hook.** `layouts/_default/_markup/render-table.html` emitting `scope="col"` (+ `scope="row"` for first-column headers); optionally `tabindex="0"` + label on the scroll wrapper for keyboard panning. Regression-build all 153 pages.
10. **U-14 — mobile answer-first.** At ≤620px collapse the TOC into a `<details><summary>` (or move below "In brief"). Desktop sticky rail unchanged.
11. **U-11 — new-tab indication.** Append visually-hidden "(opens in new tab)" to Amazon CTAs (screen-reader text; no visual clutter).
12. **U-15 — early exit for the convinced.** One compact text CTA ("Check price on Amazon") inside the review's Quick-verdict area, only on review pages with a single pick; the deep box stays canonical.
13. **U-12 — byline ceiling (owner gate, truthful paths only).** Option A: owner attaches a real name + verifiable background to `authors.html` and the meta row. Option B (no name): deepen process proof — a "Last reviewed [date]" line on monetized pages and per-page source counts. **Never** invent personas or credentials; the current honest entity byline is better than a fake expert.
14. **U-13 — search enrichment.** Add a `keywords` field (or body-terms index) to the search JSON build; keep the 12-result cap and empty-state guidance.
15. **U-19 — differentiate or drop.** Either suppress the header dek on article pages or support an `answer` param so "In brief" can say something the dek didn't.
16. **U-16/U-21/U-17/U-20/U-22/U-23/U-24/U-18** — polish batch: reorder "buying mistakes" before the first box or add a jump link; auto-fill system-strip cells from front-matter params instead of generic copy; collapse the end-of-article stack to two blocks; vary "Read guide" with page-specific labels; point footer Terms directly at `/pages/terms.html`; add small-target padding (`.toc a`, `.breadcrumbs a`, footer links: `display:inline-block; padding:.25rem .5rem`); add a truthful reply-window line to contact only if one exists.

---

## 5. Reusable trust-signal checklist (pre-publish, every future page)

**Byline & dates**
1. Meta row shows BOTH "Published" and "Updated" (set `updated`, or confirm GitInfo lastmod will render)?
2. Front matter has a real `date` — no "Jan 1, 0001" anywhere?
3. Every time-sensitive claim (prices, incentives, specs, warranties) carries "retrieved YYYY-MM-DD"?
4. Material revisions reflected in the corrections log or an on-page note?

**Disclosure & links**
5. `{{< affiliate-disclosure >}}` placed ABOVE the first `{{< product-box >}}`/`{{< amazon >}}`?
6. All Amazon links via shortcodes (rel="sponsored nofollow noopener", tag from `hugo.toml`), zero hardcoded tags?
7. Each box includes "Not for:" and an honest-tradeoff line before the button?
8. On-box commission note present and unedited?
9. No quoted prices (labeled editorial bands with as-of dates only)?
10. Funding claims on the page match reality (affiliate yes; display ads only if actually running; analytics only if disclosed)?

**Claims & sourcing**
11. Equipment claims marked "per manufacturer spec" or third-party sourced + dated?
12. Arithmetic shown with stated assumptions so a reader can re-run it?
13. "Best for" framed as spec-and-math scenario match, criteria linked to `/pages/how-we-recommend.html`?
14. No bench-test/hands-on/review-unit claims except documented Project Lab builds?
15. Safety-critical steps flagged as licensed-professional territory?
16. Policy/incentive claims checked against the corrections log's latest rulings?

**Reader recourse**
17. Corrections/contact route reachable (footer + in-text link on material-claim pages)?
18. FAQ answers "Did you test this?" honestly ("No" unless Project Lab)?

**Page anatomy**
19. "In brief", byline row, and disclosure all visible before the first Amazon button on a mobile viewport?
20. Nothing overlays content (no ads, popups, sticky bars, cookie banners)?
21. Privacy policy still matches the page's actual scripts (Rybbit disclosed; GA removed or disclosed+consented)?
22. All links on the page resolve with real content (no soft-404s; sitemap URLs = 200s)?

---

## 6. 30-day UX improvement sprint

**Urgency key:** 🔴 trust/compliance · 🟠 conversion-relevant · 🟢 polish. Effort: S <½ day · M ½–2 days · L >2 days.

### Week 1 — Truth & legibility (close all Critical/High)
| # | Item | IDs | Impact | Effort | Urgency |
|---|---|---|---|---|---|
| 1 | GA: remove from `hugo.toml` **or** disclose+consent (owner gate) | U-4 | High | S (remove) / M (consent) | 🔴 |
| 2 | Affiliate-disclosure + privacy wording matches reality | U-6 | Med | S | 🔴 |
| 3 | Contrast tokens: `--muted`→`#6b6a62`, `.button-solar`→`orange-deep` + font-floor pass (.64–.72rem → ≥.75rem on note/meta/labels) | U-2/U-3 | High | S | 🔴 |
| 4 | Rebuild, verify: contrast script on both CSS layers, spot-render 5 page types | — | — | S | — |

### Week 2 — Close the buyer loop
| 5 | Roundup↔review links (all picks) + review "Alternatives" links | U-9 | High | S | 🟠 |
|---|---|---|---|---|---|
| 6 | Dated editorial price-band rows in roundup/review/vs tables | U-10 | High | S/M | 🟠 |
| 7 | Early compact CTA after review Quick-verdict; "buying mistakes" moved/jump-linked before first box | U-15/U-21 | Med | S | 🟠 |
| 8 | "In brief" vs dek differentiation (`answer` param or dek suppression) | U-19 | Med | S | 🟢 |

### Week 3 — Operability (accessibility engineering)
| 9 | Calculator a11y: aria-live results, inputmode, error pattern | U-7 | Med | M | 🟠 |
|---|---|---|---|---|---|
| 10 | Table render hook (th scope) + keyboard-scrollable wrapper; 153-page regression build | U-8 | Med | M | 🟢 |
| 11 | New-tab SR text on Amazon CTAs; small-target padding batch | U-11/U-18 | Low-Med | S | 🟢 |

### Week 4 — Trust depth & polish
| 12 | Byline decision executed (owner gate): real name+bio OR "Last reviewed" lines on monetized pages | U-12 | High | S/M | 🟠 |
|---|---|---|---|---|---|
| 13 | Mobile TOC collapse (details/summary ≤620px) | U-14 | Med | S/M | 🟠 |
| 14 | Search index enrichment (keywords/body terms) | U-13 | Med | M | 🟢 |
| 15 | Polish batch: system-strip param-fill, end-stack reduction, link-text variety, footer terms href, contact reply-window if truthful | U-16/17/20/22/23/24 | Low | M | 🟢 |
| 16 | Final verification: contrast script, keyboard pass, 320px/200% zoom pass, live URL sweep; corrections-log entry for the GA/disclosure change; re-score §2 | — | — | S | — |

**Standing constraint honored:** no URL changes anywhere; every fix above is in-place content, template, or CSS work.

---

## Appendix — evidence base, corrections, and attribution

**Corrections to the Boss fact-pack (seat-verified, adopted):**
- `/terms.html` is NOT a soft-404: `content/pages/terms.md` exists; the footer's `/terms.html` serves a 337-byte noindex meta-refresh alias with correct canonical to `/pages/terms.html`. (Boss re-verified the alias headers directly.)
- `mppt-vs-pwm.html` live shows "Published May 31, 2026 · Updated Sep 5, 2026" — the trust seat's local-build concern ("no Updated row") does not apply live; retracted.
- Local `public/` is a stale 2026-08-15 build containing old AdSense markup — never treat as deployed state (live pages verified ad-free).

**Verified-pass inventory (don't over-fix):** skip link + focus ring + reduced-motion; 44/48px targets; sticky-nav a11y (aria-expanded, focus mgmt, Escape); labeled calculator inputs; descriptive hero alt text; zero overlays; disclosure-before-link (byte-verified ×4 pages); corrections log matches live content (ITC fix spot-verified on AZ/FL/CA guides); all nav/footer URLs 200 with real titles; proper 404 for bogus URLs; og/twitter meta complete; landmark aria-labels present throughout (re-verified).

**Seat log:** journeys (glm-xo-3, 1 round, clean) · accessibility (dsv4-wing-1, failed round 1 "no deliverable after forced-final prompt" → same-seat repair with ≤3-tool-call correction packet, round 2 PASS with 7 FLAGs, all FLAGs since Boss-resolved) · trust (glm-xo-2, evidence complete, hit tool cap before write — deliverable salvaged verbatim from response, verification log intact).

**Hotfix diff summary (this audit):** `how-many-solar-panels-to-power-a-house.md` (−fake pitch, −2 typos, +honest close) · 5 root pages (+`date = 2026-08-10`).

---

## Addendum — independent review (2026-09-06)

**VERDICT: PASS (93/100)** — reviewer glm-or-1 (uncorrelated provider family; 8 factual spot-checks performed: both hotfixes verified in working tree with git-accurate rationale; contrast ratios independently recomputed to the second decimal from the CSS tokens; live roundup/review/terms-alias claims reproduced; `--muted` confirmed declared exactly once across both CSS layers, validating the single-PR fix; sprint IDs ⊆ issue list; owner gates intact; ethics screen clean).

Three MINOR issues raised, all applied:
1. Trust-pages scorecard row: T 9→8 with explicit "U-4/U-6 — see Week 1" pointer (truth defects live on those pages; a skimming owner could otherwise skip Week 1).
2. §1a typo location corrected to "Practical Tips" section (not the Conclusion).
3. §3 U-5 row restructured so the "FIXED during audit" status renders reliably in both table renderers.

---

## Addendum — execution log (2026-09-06, sprint executed)

All 16 sprint items resolved or explicitly dispositioned. Regression-verified before push: build clean, 153 sitemap URLs unchanged (no URL changes), all new internal links resolve, anchors verified, 10-point rendered-HTML check passed.

**Owner-gate decisions (per standing directive, both reversible):**
- **U-4 GA: REMOVED** from `hugo.toml` (the audit's preferred option). Privacy policy now matches reality (Rybbit only, cookieless). *Revert:* re-add `google_analytics = '…'` under `[params]` — but if re-added, disclose it on the privacy page first (logged in the corrections entry).
- **U-12 byline: Option B** (process proof, no invented people). New `reviewed` front-matter param renders "Reviewed Sep 6, 2026" in the meta row; set on the 6 pages whose facts were verified that day (roundup, 3 reviews, vs page, cost guide). Option A (owner's real name/bio in `authors.html` + meta row) remains available at any time.

**Week 1 — truth & legibility:** GA removed · affiliate-disclosure AdSense claim corrected to "we do not currently run display advertising" · privacy policy rewritten (Rybbit-only, Amazon-third-party-cookie honesty) · `--muted` → `#6b6a62` (4.83:1) · `.button-solar` → `--orange-deep` bg (6.02:1), hover deepened · font floor: all .62–.72rem utility text → ≥.75rem with line-heights (breadcrumbs, meta row, product-note, footer-meta, system-strip, kickers, TOC) · target padding on breadcrumbs/TOC/footer links.

**Week 2 — buyer loop:** roundup now links all three existing standalone reviews ("Full review:" lines) · verified editorial price bands added to roundup, vs-page, and all three review spec tables (as-of Sep 2026, volatility-labeled) · early compact Amazon CTA after each review's honesty block · "common buying mistakes" pointer added to Key takeaways · `answer` param supported in template (In-brief can now differ from dek; no pages set it yet).

**Week 3 — operability (JS enhancements in main.js, no-JS = prior baseline):** calculator results `role=status aria-live=polite` (div/p `[id$=result]`) · `inputmode=decimal` on numeric inputs · `th scope=col` on all rendered tables · `tabindex=0` + scroll hint aria-label on tables (keyboard panning) · "(opens in a new tab)" SR text on every Amazon CTA · related-posts "Read guide" links get page-specific aria-labels.

**Week 4 — trust depth:** `reviewed` dates (above) · mobile TOC now a `<details>` collapsed ≤620px via JS (desktop unchanged) · search index enriched with body text + keywords.

**BONUS defects found and fixed during execution:**
1. **The site search was entirely dead** — `/search.html` rendered an empty article since launch (the search template in `layouts/search/` was never wired: `content/search.md` lacked `type = "search"`). The nav "Search" item led to a blank page. Fixed with one front-matter line; the search UI and enriched index now render. Arguably the largest functional defect on the site, missed by the audit (which only flagged the zero-date and index breadth).
2. **Wrong price class on both Victron reviews** ("bottom of the $250–$600 mid-range band") — Sep 2026 street checks (official EUR price list, authorized distributor, 5 US retailers) put the 100/20 at ~$95–125 and 100/30 at ~$110–140: small class. Cost-guide small-class floor corrected $120 → $95. Logged in corrections.
3. Five root pages' zero dates and the fake installer pitch (audit hotfixes, committed `402d540`).

**Deferred (with reasons):** U-13 search body-index — done (keyword+body); the *render-hook* variant of th-scope (M4) deferred in favor of the JS enhancement (zero regression risk across 153 pages) · U-17 system-strip param-fill deferred (needs per-page editorial params; label sizing fixed) · U-20 next-steps/related dedupe deferred (template coupling outweighs Low-severity polish) · U-24 contact reply-window not added (no truthful value exists to state) · U-16 table panning mitigated by keyboard access + contrast/size fixes; column reduction would need per-table editorial decisions.

**Price-band provenance:** seat research (family floors, honestly withheld at model level due to retailer blocking) + Boss corroboration searches (≥2 model-specific sources each); snapshot archived at `.agency/ux-exec/prices.md`.
