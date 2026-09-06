# Technical SEO & Performance Audit — solarpoweredproject.com

**Date:** 2026-09-06 · **Method:** Agency audit (5 specialist seats + independent review) + Boss verification of every load-bearing claim · **Evidence base:** local Hugo builds (`hugo --minify --gc`, v0.141.0, 161 HTML files), repo source, live production curl tests (2026-09-06 ~14:55 PT), Amazon OA/policies knowledge base from prior audits.
**Seat deliverables (full detail, evidence, and scripts):** `.agency/tech-seo/` — w1-crawl-index.md, w2-performance.md, w3-schema-security.md, w4-links.md, w5-a11y-mobile.md.
**Ethics constraints honored:** no cloaking, no misleading schema, no hidden content, no fake reviews, no doorway pages, no affiliate-link masking. House honesty rule applied throughout (never fabricate ratings/testing).

---

## 1. Executive summary

**Overall: the technical foundation is strong; the rot is content-level link/image hygiene and one template bug — highly fixable, mostly in minutes-to-hours.** No CRITICAL indexation threat exists: Googlebot and Bingbot receive real content (the previous Hostinger 403 block is verified fixed), robots.txt and the 154-URL sitemap are clean and exactly match the build, every page carries a correct canonical, there are no orphan pages, crawl depth maxes at 3 clicks, zero mixed content, and all 69 Amazon affiliate links are 100% format-compliant (tag `slrpwp-20` on every `/dp/` URL, correct `rel`, no off-pattern shapes).

The audit found **one systemic template bug, one hosting-side duplicate risk, and a cluster of content-hygiene defects concentrated in a handful of files**:

1. **FAQ structured data is double-encoded sitewide** (113 pages): every Question/Answer value is wrapped in extra literal quotes and contains `\u0026rsquo;`-style mojibake. Valid JSON, semantically corrupted. Root cause isolated (per-value `jsonify` inside a `<script>` context → Go's contextual auto-escaper encodes it a second time). Fix is a two-line template change.
2. **31 broken internal link occurrences across 12 targets** (10 `.hml`-extension typos in one file, one of them the `califormia` misspelling; 14 trailing-slash guide URLs; 7 bare `/guides/` links) plus **116 dead in-page anchors** across 18 pages whose "quick links" fragments don't match Hugo's generated heading ids. *(Count reconciled by independent review — W1's initial 21 under-counted; reviewer's exact scan and W4 agree on 31/12.)*
3. **12 broken images**: a typo'd hero (`/assts/`) on the Florida cost guide and 11 referenced-but-missing inline webp files on 6 pages (empty image directories in the repo).
4. **The designed 404 page has never been live**: the template sits at `layouts/_default/404.html`, but Hugo's 404 lookup path is `layouts/404.html` — it never renders, so production serves Hostinger's default error page (real 404 status, unbranded). *(This corrects the prior session's belief that the helpful 404 was deployed — Boss erratum; verified by fresh builds + absence from `public/`.)*
5. **Hosting-side**: `www.solarpoweredproject.com` serves a 200 duplicate instead of 301-redirecting to the apex (canonicals are the only dedupe); HTML is served `no-cache, no-store` with CDN status DYNAMIC (nothing cached at the edge); no HSTS/X-Content-Type-Options/Referrer-Policy/X-Frame-Options headers.
6. **Performance**: two render-blocking stylesheets (40.4 KB raw) of which `tailwind.css` (14.9 KB) is used almost only by the TOC partial; unfingerprinted `main.js`/`tailwind.css` create a 7-day stale-asset window after deploys; 4 DIY hero images weigh 260–370 KB (target ≤100 KB); Google-Fonts swap without metric-compatible fallbacks is the main CLS source. INP risk is LOW (tiny deferred JS, no long tasks).

**Prioritized bottom line:** Week 1 of content-hygiene fixes (mostly `minutes` effort, content editor + developer) removes every user-visible defect; Week 2 fixes the schema bug and 404; Week 3 is hosting-panel work (www 301, headers, caching) plus asset fingerprinting; Week 4 is image/font performance polish. Nothing found requires URL changes, and nothing conflicts with the Amazon Associates compliance posture (which this audit re-verified as clean).

---

## 2. Prioritized technical issue table

Severity: CRITICAL (indexation/revenue threat) · HIGH · MEDIUM · LOW. Effort: minutes / hours / day+. Owner: DEV (developer) / EDITOR (content editor) / DESIGN (designer) / ADMIN (site administrator — Hostinger panel).

| # | Issue | Evidence / affected URLs | SEO/user impact | Severity | Fix | Effort | Owner |
|---|---|---|---|---|---|---|---|
| TS-01 | FAQ JSON-LD double-encoded: values carry extra `"` wrapping + `\u0026rsquo;` mojibake | 113 pages with FAQPage; decoded sample: `"name"` = `"Did you test this charge controller?"` (quotes included); Boss-reproduced on renogy-rover-40a-review.html. Cause: `faq-schema-render.html` pipes each value through `jsonify`, then Go's contextual escaper re-encodes inside `<script>` | Rich-results markup semantically wrong; crawl-trust/quality signal damage; Rich Results Test will flag | HIGH | In `faq-schema-render.html` drop per-value `jsonify` (let contextual escaping quote once) or `jsonify | safeJS`; in `faq.html` store answers `plainify | htmlUnescape` so entities become real characters; rebuild + decode-verify | hours (incl. verify) | DEV |
| TS-02 | Broken images: Florida hero `/assts/...` (404) + 11 missing inline webp on 6 pages | `content/guides/solar-panel-cost-florida/_index.md:20` (typo); empty dirs `static/images/{how-to-calculate-solar-load, solar-battery-enclosure-guide, solar-battery-management-system-explained, solar-installation-safety-guide, solar-panel-shading-effects, solar-panel-tilt-and-orientation}` (Boss-verified 0 files each) | Broken hero on a money page; 11 broken inline images; CLS + trust | HIGH | Fix typo; restore/re-export the 11 webp files (or remove the dead `<img>` refs) | minutes (typo) + hours (files) | EDITOR |
| TS-03 | 31 broken internal links / 12 targets: 10 `.hml` typos incl. `califormia` (all in the Florida guide), 14 trailing-slash guide URLs, 7 `/guides/` | `content/guides/solar-panel-cost-florida/_index.md:46,94,124–131`; trailing-slash sources incl. `solar-system-costs.md:386`, `how-much-do-solar-panels-cost.md:145`, `solar-lease-vs-buy-2026.md:197`, 5 state guides `_index.md`, `solar-basics.md:186,233` | Crawl waste, leaked link equity to 404s, poor UX on 15+ pages | HIGH | Correct hrefs to `.html` forms | minutes | EDITOR |
| TS-04 | 116 dead in-page anchors: quick-links fragments ≠ Hugo heading ids | 115 fragment-only (e.g. `#mistakes`×14, `#takeaways`×9, `#next`×7) across 18 pages + 1 cross-file (`solar-wire-size.md:277` → `#calculator`) | Silent no-op clicks; UX + internal-link signal waste | HIGH (UX) / MEDIUM (SEO) | Align fragments with rendered ids or add explicit `{#id}` anchors | hours | EDITOR+DEV |
| TS-05 | Designed 404 page never built → Hostinger default 404 live | `layouts/_default/404.html` exists but Hugo looks up `layouts/404.html`; no 404.html in any build or `public/` (Boss-verified, 3 build modes); production 404 = host default (status 404 real, unbranded) | Lost recovery UX on 404s; no SEO harm (status correct) | HIGH (UX) / MEDIUM | `git mv layouts/_default/404.html layouts/404.html`; rebuild; verify 404.html in output + deploy | minutes | DEV |
| TS-06 | www host serves 200 duplicate (no 301) | `www.solarpoweredproject.com` → 200 same content (live-verified 2026-09-06); absolute apex canonicals are the only dedupe | Signal-splitting risk if canonicals ever regress; external links to www dilute | MEDIUM | 301 www→apex in hPanel (domain redirect); keep canonicals as backstop | minutes | ADMIN |
| TS-07 | Heading violations on 18 pages: 10 double-h1 (7 state guides + affiliate-disclosure, best-solar-batteries, payback-calculator), 7 alias stubs 0-h1, 1 h1→h3 skip | Content files begin with `<h1>` under a template that already emits one (`layouts/_default/single.html:3-4`); e.g. `guides/solar-panel-cost-florida/_index.md` body | a11y + heading-signaling | MEDIUM | Strip leading `<h1>` from 10 files; stubs are noindex refresh aliases (low priority) | hours | EDITOR |
| TS-08 | Render-blocking CSS 40.4 KB; `tailwind.css` (14.9 KB) used ~only by TOC partial | `head.html:8` links `/css/tailwind.css` (14,859 B); utilities consumed: toc.html classes only (`.my-6 .p-4 .bg-gray-50 …`); also FAQ shortcode div classes | Slower FCP/LCP on every page; one extra RTT | MEDIUM | Merge the ~14 used utilities into design-system.css, delete tailwind.css link + file (full selector scan before deletion — flagged partial in W2 §7) | hours | DEV |
| TS-09 | `main.js` + `tailwind.css` unfingerprinted with `max-age=604800` | Live headers (verified); `baseof.html:8`, `head.html:8` | Up to 7-day stale JS/CSS after deploys (broken half-deploys for users) | MEDIUM | `resources.Fingerprint` both (pattern already used for design-system.css); immutable cache for hashed files | hours | DEV |
| TS-10 | HTML served `no-cache, no-store` + `x-hcdn-cache-status: DYNAMIC` | Live headers on / and article pages; origin RTT ~65 ms | Every pageview hits origin; TTFB ceiling on repeat visits; wastes CDN | MEDIUM | LiteSpeed/hPanel HTML cache TTL 300 s (deploy already purges lscache — compatible); verify DYNAMIC→HIT | minutes | ADMIN |
| TS-11 | 4 DIY hero images 260–370 KB webp | pelton 370 KB, lease-vs-buy 332 KB (meta-only), TEG 322 KB, pedal 289 KB, hand-crank 288 KB; of these, pelton/TEG/pedal/hand-crank ARE rendered LCP heroes | LCP on 4 experiment pages; mobile data cost | MEDIUM | Re-encode ≤100 KB / ≤1600px (cwebp -q 70-75) | hours | DESIGN |
| TS-12 | Font swap CLS: Google Fonts (Fraunces+Space Grotesk, 6 weights — all used) with no metric-compatible fallback | `head.html:6-7` preload/swap pattern; no `size-adjust`/fallback metrics in CSS | Text reflow at swap on every page (main CLS source) | MEDIUM | Option A (recommended): self-host woff2 + `size-adjust` fallbacks — also removes third-party font flow (privacy, TS-27). Option B: keep Google, add fallback metrics | hours / day+ | DEV |
| TS-13 | Publisher logo missing from all 139 Article schemas + home Organization | `hugo.toml [params]` has no `logo`; `head.schema.html` `{{ with .Site.Params.logo }}` never fires; real 250×250 PNG exists at `static/assets/images/solarpoweredproject-logo.png` (verified) | Incomplete Organization entity; weaker E-E-A-T signal | MEDIUM | Add `logo = '/assets/images/solarpoweredproject-logo.png'` to `[params]` (one line fixes 140 pages); delete space-named duplicate file | minutes | DEV |
| TS-14 | Security headers absent (only `content-security-policy: upgrade-insecure-requests`) | Live headers 2026-09-06: no HSTS, XCTO, Referrer-Policy, XFO | Browser-trust basics; minor SEO-trust signal | MEDIUM | `.htaccess` block ready in W3 §5 (HSTS without preload; CSP allowing fonts+rybbit+unsafe-inline; verify edge doesn't strip after deploy) | minutes (apply) + verify | ADMIN |
| TS-15 | CA-cost-guide cluster: hero missing width/height + 6 template-generated alts; battery-cost 3 imgs missing dims | `guides/solar-panel-cost-california.html` (Boss-verified tag); alts like "Main image solar panel cost california" | CLS on eager hero; weak alts | MEDIUM | Add dims; rewrite alts descriptively | minutes | EDITOR |
| TS-16 | Mobile nav dead without JS | `nav.html:14` ships `hidden`; only main.js reveals; CSS hides desktop nav ≤900px | JS-off/disabled mobile users lose main nav | MEDIUM | `<noscript><style>` unhiding panel (pattern in W5 §8) | minutes | DEV |
| TS-17 | hero-proof labels contrast FAIL 3.40:1 (12px bold orange on paper; need 4.5) | design-system.css:59; recomputed 2026-09-06 (all other 20 pairs PASS) | a11y fail on homepage proof strip | MEDIUM | `color: var(--orange-deep)` (5.35:1) | minutes | DESIGN |
| TS-18 | Titles >60 chars on 127/161 pages (worst 103–110 chars, mostly DIY) | Build scan (W5 §1) | SERP truncation; brand suffix consumes 24 chars | LOW-MED | Shorten head terms or trim suffix on long titles (rolling) | hours | EDITOR |
| TS-19 | 95 pages declare front-matter `image` never rendered in body (og/schema only) | Build scan (W2 §2.4) | Missed visual opportunity; images exist but unused in-page | LOW (decision) | Render heroes in body for top traffic pages (after compression) or accept text-LCP | hours | EDITOR |
| TS-20 | `dateModified` date-only on 7 pages (unformatted `updated` param branch) | head.schema.html passes raw `updated` string; 7 pages verified | Inconsistent (spec-legal) date formats | LOW | `time.AsTime` + format in that branch | minutes | DEV |
| TS-21 | search.html (noindex) included in sitemap | Sitemap 154/154 includes it; only noindex page | Contradictory signal; harm ≈ 0 | LOW | Sitemap template filter excluding noindex pages | minutes | DEV |
| TS-22 | EIA citation typo + id variants | `solar-panel-cost-florida/_index.md:25` `epm_table_rapher.php` (soft-404, live-verified); `epmt_5_6_a` vs `epmt_5_06_a` both resolve | Broken source citation on a money page | LOW | Fix to `grapher`; unify id | minutes | EDITOR |
| TS-23 | Alias-stub cosmetics: URL-as-title, 0-h1, `lang=en-us` ×7 | about/contact/editorial-policy/privacy-policy/privacy/terms-of-service/terms.html (noindex meta-refresh stubs) | Invisible to users (instant refresh); noindex'd | LOW | Normalize `languageCode='en'`; optionally title the stubs | minutes | DEV |
| TS-24 | Font-floor remnants: .6/.64/.65rem on 3 homepage micro-labels | design-system.css:60,90 | Sub-12px text | LOW | Raise to .7rem | minutes | DESIGN |
| TS-25 | No `overflow-wrap` on `.prose` | design-system.css:73 | Long URLs/ASINs can overflow 360px | LOW | `.prose{overflow-wrap:anywhere}` | minutes | DEV |
| TS-26 | Calculators silent without JS | Inline toolscript; no noscript note | Confusing degradation | LOW | `<noscript>` hint on calculator pages | minutes | EDITOR |
| TS-27 | Google-Fonts flow not mentioned in privacy policy (page discloses Rybbit only) | privacy-policy.md vs build third-party census (fonts.googleapis/gstatic + app.rybbit.io) | Privacy-claim accuracy (house standard) | LOW | Disclosure sentence, or self-host fonts (TS-12 Option A) and drop the issue | minutes | EDITOR |
| TS-28 | Wikimedia hotlinks ×6 on battery/inverter pages | 6 pages reference upload.wikimedia.org images directly (static census) | Third-party dependency + etiquette; CSP implication | LOW | Download, credit license, self-host | hours | EDITOR |
| TS-29 | Dead code: GA conditional in head.html, unused adsense.html partial, space-named logo duplicate | head.html tail; layouts/partials/adsense.html; `static/assets/images/solarpoweredproject logo.png` | Repo hygiene/confusion risk | LOW | Delete | minutes | DEV |
| TS-30 | Stray `/` inside payback-calculator hero img tag | Built `pages/solar-payback-calculator.html` (Boss-verified `alt="…" / width=`) | Invalid-ish HTML (tolerated) | LOW | Remove | minutes | EDITOR |

**Explicitly verified clean (no action):** sitemap↔build parity exact (154=154) · canonical coverage 100% with exactly the 5 intended consolidation pages · noindex only on search (by design) · robots.txt clean · no orphans, max depth 3 · zero query-string/faceted/pagination URL space · no duplicate meta descriptions (1 known canonicalized title pair) · Amazon links 69/69 compliant (18 ASINs, 100% tag coverage, no `/gp/` `/s?k=` `amzn.to` shapes, all with sponsored/nofollow/noopener + sr-only spans) · 0 http:// externals · http→https single-hop 301 · no Product/Review/AggregateRating/ItemList schema (and none should be added — see §4) · JSON-LD 0 parse errors, BreadcrumbList 153/153 valid · INP low risk · all requested font weights used · JS-off article content fully readable.

---

## 3. Core Web Vitals & performance improvement plan

*(Full analysis: `.agency/tech-seo/w2-performance.md`; all sizes measured from local build; transfer estimates labeled as such.)*

**Current rendering stack (identical across templates):** render-blocking = `tailwind.css` (14,859 B) + `design-system.min.<hash>.css` (25,511 B) + Google Fonts CSS2 (external, ~1–2 KB); deferred = `main.js` (4,173 B) + Rybbit script. Homepage HTML ≈ 11.5 KB.

**LCP per template:** Home and most articles → **H1 text** (only 9 pages render a body hero image; 95 front-matter images are meta-only). Calculator + 4 DIY pages → hero `<img>` (eager + fetchpriority=high + decoding=async on 8 of 11; home hero uses non-standard `fetchpriority` attr form; best-solar-batteries hero lacks fetchpriority). Heaviest rendered LCP heroes: pelton 370 KB, TEG 322 KB, pedal 289 KB, hand-crank 288 KB.

**CLS:** primary source = font swap without metric-compatible fallbacks (TS-12); secondary = CA-guide hero without width/height (TS-15). TOC collapse and calculator-results injection are minor/below-fold. INP: **LOW risk** — handler inventory (menu toggle, Escape, passive scroll class, search filter over ≤154 items, footer IntersectionObserver, inline calculator scripts) contains no long tasks.

**Ordered fix plan (impact desc):**
1. **Kill the tailwind.css request** (TS-08): merge ~14 used utilities into design-system.css → −37% render-blocking CSS on every page. *(Run the full selector-vs-build scan before deleting — W2's scan was partial.)*
2. **Compress the 9 rendered heroes to ≤100 KB** (TS-11): −270 KB on the worst page; `cwebp -q 70-75 -resize 1600 0`.
3. **Self-host fonts** (TS-12 Option A): removes 2 preconnects + external CSS + the swap CLS source + the Google data flow (closes TS-27). Subset later if needed (Option B).
4. **Fingerprint main.js + tailwind.css** (TS-09) with immutable cache-control for hashed assets.
5. **Enable LiteSpeed HTML caching TTL 300 s** (TS-10) — deploy-time lscache purge already exists in the GitHub Action, so short TTL is safe; confirm `x-hcdn-cache-status` flips DYNAMIC→HIT.
6. **Fix hero attribute details**: standard `fetchpriority=high` on home hero; add fetchpriority to best-solar-batteries hero; width/height on CA hero (TS-15).
7. *(Post-fix measurement)* PSI/Lighthouse on home + 2 DIY pages; target LCP <2.5 s mobile on 4G, CLS <0.1, INP <200 ms. No field CWV data exists yet (Rybbit has no CWV; CrUX needs traffic) — establish PSI lab baseline and re-test after each step.

**Page-weight budget (worst affected page, estimates):** DIY article ≈449 KB raw today → ≈165 KB after hero compression + CSS merge + self-hosted cached fonts.

---

## 4. Schema audit with safe implementation recommendations

*(Full analysis + machine-readable inventory: `.agency/tech-seo/w3-schema-security.md`, `w3-inventory.json`, `w3-validate.json`.)*

**Inventory (local build, 267 JSON-LD blocks, 0 parse errors):** Article ×139 · BreadcrumbList ×153 · FAQPage ×113 · WebPage ×14 (list/section nodes) · WebSite+Organization ×1 (home). Seven root alias stubs intentionally carry none.

| Type | Verdict | Notes / safe actions |
|---|---|---|
| Article (139) | Valid, incomplete | Headlines fine; dates present & sane (7 date-only `dateModified` — TS-20); author Person present except 6 utility pages (acceptable); **image missing on 16+** (utility + DIY singles — add front-matter images as they're created, TS-19); **publisher logo missing everywhere → one-line fix (TS-13)** |
| BreadcrumbList (153) | Clean | Sequential positions, absolute URLs, consistent home-item form. No action |
| FAQPage (113) | **Corrupted encoding (TS-01)**; pairing correct | Question counts match visible FAQs exactly on all 10 sampled pages (incl. 4 product reviews); no schema-only FAQs; after the encoding fix, re-verify 10-page sample + Rich Results Test |
| WebPage (14) | Valid | name+url+description complete |
| WebSite/Organization (home) | Valid, minimal | Add `logo` (TS-13). **Do NOT add `sameAs`** — no verified owned social profiles exist (house rule: never invent authority signals) |

**Review/rating markup policy (explicit):** zero Product/Review/AggregateRating/ItemList schema exists — **confirmed by grep across the entire build**. Recommendation: **keep it that way permanently.** The site publishes spec-based reviews with explicit "we did not test this" disclosures; ratings markup would fabricate evidence the site does not have. The honest ceiling would be a factual, rating-free `Product` node on the 4 review pages — but even that is not recommended (merchant-oriented feature, negligible value, drift risk toward ratings later). Current state is the correct end-state.

**Accuracy of schema vs visible content:** Article headlines/dates match pages; canonicals cross-checked; FAQ text matches visible text word-for-word once the double-encoding artifacts are normalized (15/31 exact matches in the strict comparison; all 16 remaining diffs are purely the encoding artifact class — no wording fabrication found).

**Security/trust findings:** mixed content **zero** (100% https everywhere incl. externals); `.htaccess` header block drafted (W3 §5) with per-header risk notes — HSTS without `preload` (near-irreversible — avoid until certain), CSP pragmatically allowing the three real origins (fonts.googleapis/gstatic, app.rybbit.io) + `unsafe-inline` (inline calculator/search scripts exist; long-term hash them), `img-src` should stay `'self' data:` (no Amazon imagery is loaded today — the drafted `m.media-amazon.com` allowance is unnecessary unless product images are added later). One caveat: hcdn edge must be checked not to strip origin headers after applying.

---

## 5. Crawl & indexation action plan

**State:** healthy. robots.txt (allow-all + sitemap) · sitemap 154 URLs, exact build parity, lastmod populated (git-based; distribution currently 144×2026-09-05 from one genuine mass-edit day — keep avoiding no-op mass edits so lastmod stays trustworthy) · canonicals 100% correct incl. 5 consolidation pages · no orphans · depth ≤3 · no query/facet/pagination space · Googlebot + Bingbot verified receiving real content · alias stubs correctly noindex'd.

**Actions:**
1. **Fix the broken-link graph** (TS-03/TS-04) — currently ~30 hrefs leak into 404s and 116 anchors no-op; this is the only crawl-quality defect.
2. **www→apex 301** (TS-06) to make canonicals a backstop rather than the sole dedupe.
3. **Search Console** (user, ~30 min): `google_site_verification` is unset in hugo.toml — verify a GSC property (HTML-tag method: add the meta via hugo.toml param, which head.html already supports), submit sitemap.xml, and check Coverage/Enhancements (FAQ report will show the TS-01 corruption until fixed). Bing Webmaster Tools equivalent (bingbot passes the bot-gate).
4. **Bot-gate policy** (decision, ADMIN): Hostinger's challenge still gates generic agents (GPTBot 429; third-party SEO crawlers see interstitials). Treat GSC/BWT as the only authoritative crawl sources. Decide deliberately whether AI crawlers should be blocked (currently incidental) — robots.txt is allow-all, so the block is hosting-side only. Keep the interstitial noindex'd.
5. **Sitemap hygiene (optional):** exclude noindex'd search.html (TS-21); uniform changefreq/priority are ignored by Google — harmless to keep.
6. **After fixes:** re-run the sitemap-parity + link-graph scripts from W1/W4 (they are reusable: `.agency/tech-seo/` + toolspool) and confirm zero broken targets/anchors.

---

## 6. Post-fix QA checklist

Run after each deploy batch (all checks scripted or single-command):

**Build-level (local, pre-deploy):**
- [ ] `hugo --minify --gc` exit 0; page count matches expectation (154 + new content)
- [ ] `grep -R "\.hml" content/ | wc -l` → 0; `grep -rn "assts" content/` → 0; `grep -rn "califormia" content/` → 0
- [ ] `grep -o 'href="/guides/"' public/**/*.html` → 0; no trailing-slash guide hrefs
- [ ] Anchor script (W4 method): missing fragment count → 0
- [ ] `ls public/404.html` → exists (after TS-05 move)
- [ ] FAQ decode check: python json.loads every FAQPage block → no value starts with `"` and no `\u0026` substring (after TS-01)
- [ ] JSON-LD spot: publisher.logo present on 3 articles + home (after TS-13); 0 parse errors
- [ ] Heading script (W5 method): double-h1 count → 0 on the 10 fixed files
- [ ] Image refs: every `<img src>` resolves in build (script from W5 §3)
- [ ] `grep -c "tailwind.css" public/index.html` → 0 (after TS-08); hashed main.js URL present (after TS-09)

**Live (production, Googlebot UA, spaced requests):**
- [ ] `/`, one article, one guide → 200 with real `<title>` (not challenge page)
- [ ] A 404 URL → 404 status **and** branded "Lost in the wiring?" page (after TS-05 deploy)
- [ ] `www.` → 301 to apex (after TS-06)
- [ ] `curl -sI` shows HSTS/XCTO/Referrer-Policy/XFO (after TS-14); `x-hcdn-cache-status: HIT` on second fetch (after TS-10)
- [ ] Rich Results Test (search.google.com/test/rich-results) on home + 1 review + 1 guide: Article/Breadcrumb/FAQ detected, no encoding warnings
- [ ] PageSpeed Insights mobile: home + pelton page — record LCP/CLS/INP as the post-fix baseline

---

## 7. 30-day technical roadmap

Ordered by urgency → impact → effort. Items marked **[ADMIN]** need the Hostinger panel (site administrator); everything else is repo work.

**Week 1 — Content-hygiene sprint (kills every user-visible defect; EDITOR + DEV, ~1 day total)**
- TS-02 Florida `/assts/` typo; TS-03 all `.hml`/`califormia`/trailing-slash/`/guides/` hrefs; TS-22 EIA URL
- TS-04 anchor alignment (18 pages; scripted where possible)
- TS-02b restore or remove the 11 missing inline webps
- TS-07 strip double-h1 from 10 files; TS-15 CA dims+alts (+ battery-cost dims); TS-30 stray `/`
- TS-16 noscript mobile nav; TS-25 overflow-wrap; TS-26 calculator noscript notes; TS-17 hero-proof color; TS-24 font floors
- Deploy + run QA checklist

**Week 2 — Schema & 404 correctness (DEV, ~half day)**
- TS-01 FAQ encoding fix + decode verification + Rich Results Test
- TS-05 move 404 layout; verify build emits + deploy + live check
- TS-13 logo param (+ delete space-named duplicate); TS-20 dateModified formatting; TS-21 sitemap noindex filter; TS-23 languageCode normalize; TS-29 dead-code removal

**Week 3 — Hosting & caching (ADMIN + DEV, ~1 day)**
- **[ADMIN]** TS-06 www 301; TS-10 LiteSpeed HTML cache TTL 300 s (verify HIT); TS-14 `.htaccess` headers (verify edge passes them)
- DEV: TS-09 fingerprint main.js/tailwind.css + immutable cache rules; TS-08 tailwind merge + delete (after full selector scan)

**Week 4 — Performance polish & measurement (DESIGN + DEV + user)**
- TS-11 hero compression (9 rendered heroes ≤100 KB); re-run PSI baseline
- TS-12 fonts decision + self-host implementation (closes TS-27 privacy note or add disclosure sentence)
- TS-18 title shortening (rolling, top-traffic pages first); TS-19 render-decision for front-matter heroes
- User: GSC property verification + sitemap submission (§5.3); 30-day check of Coverage + Enhancements
- Fold residuals into the quarterly maintenance cycle (AC-007, ~December: re-run W1/W4 link+sitemap scripts, PSI spot-check, OA/tag re-verify)

---

## 8. Independent review outcome (post-draft gate)

The five seat deliverables were challenged by an independent cross-provider reviewer (dsv4-wing-3; qwen-judge was rate-limited upstream) performing 34 spot-checks with its own commands and a fresh build — full log in `.agency/tech-seo/review.md`. Verdicts and dispositions:

- **W3 (schema/security): PASS.** FAQ double-encoding independently reproduced byte-for-byte on a second page; severity calibration upheld.
- **W1 (crawl/index): REVISE — corrected.** Broken-link count 21→**31** (reviewer + W4 exact scans agree; applied to §1/TS-03). The 404 root cause the seat left open was confirmed by the reviewer's minimal Hugo repro (template must live at `layouts/404.html`) — matches the Boss diagnosis already in TS-05.
- **W2 (performance): REVISE — condition applied.** The "tailwind used only by TOC" claim is a partial scan, so TS-08 stays MEDIUM (not HIGH) and the roadmap gates deletion on a full selector-vs-build scan (already stated in §3/TS-08). Florida broken-hero CLS wording softened (image has width/height, so the box is reserved — defect is the 404'd LCP image itself).
- **W4 (links): REVISE — corrected.** Summary count 9→10 `.hml` occurrences (applied); its §7 "404 page good, no change needed" rested on the layout, not the build — superseded by TS-05 (designed 404 never deployed).
- **W5 (a11y/mobile): REVISE — repaired.** All Boss-computed contrast ratios and CSS citations verified **exactly** (16/16 recomputation match); one real Boss error caught: the splice that appended §4–8 had deleted the seat-authored §1–3 — restored verbatim from the pre-splice read (seat content intact; two Boss integration notes added inline where the seat's severity was recalibrated for the noindex-stub context).
- Reviewer items it could not re-verify within budget (Amazon-link compliance scan, EIA live soft-404, http→https trace, hero byte sizes) stand on the producing seats' evidence logs plus direct Boss verification earlier in this session (typos, empty image dirs, sizes via `du`, live headers) — recorded as accepted, not independently re-derived.

**Net effect on this report:** no finding withdrawn; one count corrected upward, one root cause confirmed, one severity held down pending a scan, one file repaired. Integration proceeded after corrections.


---

*Audit artifacts: fact-pack, five seat deliverables with raw evidence, and the independent review in `.agency/tech-seo/`. Seat-failure incidents logged (2× glm-xo-3, 1× dsv4-wing-3 final-write failures — deliverables salvaged verbatim from run logs or Boss-completed where noted; qwen-judge unavailable 2026-09-06, review reassigned within the DeepSeek family). This report is the authoritative integrated record.*
