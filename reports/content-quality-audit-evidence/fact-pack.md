# Content-Quality / E-E-A-T Audit — Fact Pack (Boss ground truth, 2026-09-05)

READ THIS FIRST. Everything below is verified by the Boss today. Do not re-derive it.

## Site facts
- Hugo static site, theme adsense-base (project layouts override most templates), 140 content files:
  104 flat pages in content/pages/, 11 state-cost guide bundles in content/guides/, 20 Project Lab
  files in content/diy-off-grid-energy/, plus root trust pages (authors, methodology, corrections,
  system-planner, search) and trust pages inside content/pages/ (about, contact, editorial-policy,
  affiliate-disclosure, privacy-policy, how-we-recommend, terms).
- 36 pages carry `{{< product-box asin=... >}}` buyer boxes; 11 pages have interactive calculators
  (`{{< toolscript >}}` + .calc-actions); FAQ schema present on 103 pages; 5 duplicate pages are
  canonicalized (noindex-redirect stubs or canonical front matter) — URLs NEVER change on this site;
  consolidation is canonical-only. Actions may be keep/update/expand/merge-via-canonical. NO removals.
- Rendering (verified in layouts/): product-box shortcode prints its own disclosure line
  ("Price & availability shown on Amazon.com — we may earn a commission.") and rel="sponsored nofollow".
  A separate `{{< affiliate-disclosure >}}` shortcode (reader-supported banner) is used in 67 page bodies.
  Article template shows: kicker, H1, dek (= description), "By {author}" when author param set (8 pages
  lack it), "Published {date}", "Reviewed {updated}" ONLY if `updated` front-matter param exists —
  ZERO pages set it, so no update date is ever visible; reading time; "In brief" answer box (=description);
  TOC rail when >800 words.
- Theme hygiene: themes/adsense-base/layouts still contains dormant text from a sibling site
  ("Utility Explained", "water meter", "sewer") — verified NOT rendered on live homepage (project
  layouts/_default/index.html wins). Note as hygiene, not user-facing.

## KNOWN BOSS FINDINGS (confirm, deepen, or refute — and hunt for more like them)
1. CLAIM CONFLICT between trust pages: content/pages/affiliate-disclosure.md says guides are
   "written from hands-on experience with off-grid systems, DIY builds, and component research".
   But content/authors.md says "We do not run a test lab, and we do not claim hands-on testing we
   have not done" and content/pages/how-we-recommend.md says "We do not run a test lab" +
   "unless an article specifically documents a real build with measurements (our Project Lab
   articles do), assume nothing here has been bench-tested by us". The site DOES have a Project Lab
   section — check whether its articles actually document firsthand builds/measurements, and whether
   that justifies, narrows, or refutes the affiliate-disclosure sentence.
2. Manufacturer-attribution language ("per manufacturer spec", "retrieved 2026-..", "not lab-tested")
   appears on only 3 buyer pages (best-solar-batteries-2026 x10, what-size-solar-generator-run-
   refrigerator x3, solar-generator x1). The other ~33 box pages state specs with no visible claim
   tier. Verify in context: are specs presented as facts without sourcing, and does it matter per page?
3. Zero `updated`/lastmod front matter anywhere — heavily-updated pages (Sept 2026 ITC purge) show
   no review date to users or crawlers ( Hugo .Lastmod falls back to date).
4. Hub/section intros thin: content/pages/_index.md (65 words), diy-off-grid-energy/_index.md (37
   words). Homepage bounce 90.9% on 252 pv (30-90d window).
5. DIY cluster traffic is real but very high bounce: hand-crank 78pv/80%, flywheel 65pv/91%,
   TEG 39pv/95%, pelton 37pv/96%, alternator 33pv/93%. Question: intent mismatch or single-answer
   satisfaction? Read the pages before judging.

## Traffic (Rybbit, ~30-90d, pulled 2026-09-05; bots likely included — Hostinger bot issue unresolved)
Top: / 252pv/90.9% · battery-cable-size-for-inverter 104/86.9 · hand-crank 78/80.4 ·
solar-system-sizing 73/19.8 · 12v-vs-24v-vs-48v 70/80.4 · flywheel 65/91.1 · solar-panel-output 60/79.7 ·
mppt-charge-controller-not-charging 60/87.1 · solar-fuse-and-breaker-sizing 58/90.9 ·
solar-system-costs 47/37.7 · solar-battery-not-charging 45/76.7 · pure-sine-vs-modified 42/81.5 ·
inverter-keeps-shutting-off 41/75.9 · TEG 39/94.8 · pelton 37/95.5 · rv-solar-cost 33/58.6 ·
alternator 33/92.9 · solar-components 30/24.1 · stirling 28/58.3 · diy hub index 28/6.2.
Calculators cluster bounce 6-33% (sticky). Full data: .agency/content-audit/rybbit-pages-30d.json
(empty pull — API route moved; use .agency/seo-audit/rybbit-traffic.json instead, 99 rows).

## Scan outputs (Boss-scripted, today)
- .agency/content-audit/quality-signals.json (+.tsv): per-page words, boxes, calc, faq, h2/h3,
  tables, firsthand-claim-language hits, honest-attribution hits, internal links, caveat words,
  canonical, author, desc length. USE IT to pick and prioritize pages; verify claims in file text.

## Prior work you must not duplicate
- Keyword/SERP audit is DONE: .agency/seo-audit/master-matrix.md (37 rows, priority-scored) — the
  keyword-opportunity layer. Your layer is editorial QUALITY: intent satisfaction, evidence tiers,
  recommendation fairness, trust infrastructure, thin/AI content, topical completeness.
- Recent content history (git log): federal 30% ITC expired Dec 31 2025 — sitewide purge DONE;
  state guides de-templated with EIA June-2026 rates; 8 new pages + 5 calculators added Sept 2026.

## Claim-tier taxonomy (use these labels verbatim in findings)
T1 firsthand-tested (real build/measurement documented on-site) · T2 manufacturer-stated ·
T3 reputable third-party (EIA, NEC, datasheet aggregators — cite source+date) · T4 editorial
judgment/opinion · T5 unknown/unverified. Never present T2-T5 as T1.

## Web method warning
The web_search tool is UNRELIABLE (returns unrelated results; known malfunction). If you need live
SERP/product evidence: web_fetch on https://search.brave.com/search?q=... (URL-encode) or
https://old-search.marginalia.nu/search?query=... (non-commercial bias — floors, not Google).
Manufacturer pages via direct web_fetch are fine. If you cannot verify a spec, say T5 — do not guess.

## Ethics boundaries (hard)
No inventing testing/credentials/feedback/outcomes; no copying Amazon reviews/ratings text; no
fabricated pros/cons; preserve research-vs-hands-on transparency everywhere; recommendations must
be research-framed unless a page documents a real build. Audit only — you change nothing except
your own deliverable file.
