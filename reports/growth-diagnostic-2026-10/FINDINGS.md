# SolarPoweredProject — Full Diagnostic (2026-10-03)

Method: live-site verification (curl), repo inspection, Rybbit 9/30 snapshot (`.audit/rybbit_pages_all.json`), ASIN liveness checks. Live Rybbit API returned 403 from this box at diagnostic time (key valid earlier today — likely rate limit; recheck before next pull).

## Traffic reality (30d to 9/30)
- 510 sessions / 561 pv / 1.10 pv-per-session / 92.4% bounce / 13.5s avg session
- Engagement events: scroll_depth 64, engagement 49, reached_end 13
- Monetization events: **1 affiliate click in 30 days**
- Last 7d of window: 91 sessions — traffic is real and steady but shallow

## WHAT'S WORKING
1. **Infrastructure solid**: home 200, www→apex 301, robots.txt clean w/ sitemap ref, 404 handling correct, LiteSpeed cache-clear step in CI.
2. **Deploy pipeline healthy**: push→Actions→Hugo 0.141 build→rsync (+cache purge). Last commit 85a7543 (9/28) is what's live.
3. **Phase 2+2b monetization IS live and correct**: pick-rail cards + in-feed slots verified live on sampled pages (battery-cable, fuse-sizing, system-sizing); `affiliate_click` events carry destination/format/position props (verified in page JS).
4. **All 24 unique ASINs return 200 on Amazon** — zero dead product links.
5. **Schema complete on sampled pages**: Article + FAQPage + BreadcrumbList + Person + Organization.
6. **Sitemap clean**: 160 URLs, zero dupes, matches 160 content sources exactly.
7. **Bot treatment fixed**: Googlebot-UA 200, GPTBot-UA 200 (the prior Googlebot-403 issue is not reproducing).
8. **Site architecture**: 56/160 pages monetized; of the top-20 traffic pages only ONE is unmonetized (see gaps).

## WHAT'S BROKEN / GAPS (ranked)
- **B1 — Discovery is dead (biggest issue, same disease as ARG).** Bing shows ~1 indexed result; DDG ~1. No GSC verification meta or file found on the site — GSC was never enrolled. 160 quality pages, essentially zero search-engine distribution. Traffic is coming despite indexation (likely direct/AI-referral), not because of search. **Fix: owner enrolls GSC, verifies, submits sitemap. This is the single highest-leverage action for this site.**
- **B2 — Monetization is live but earning ~nothing: 1 click/30d.** With 510 sessions the math is brutal: even a 2% CTR would be ~10 clicks. Root causes: (a) only 56/160 pages carry any monetization; (b) 92% bounce / 1.1 pv/session means most visitors see one page briefly and leave — the rail/slots never get scrolled into view (scroll_depth fired only 64 times vs 561 pageviews).
- **B3 — Engagement anomaly: `solar-battery-not-charging-troubleshooting` shows ToP 0s / 97% bounce** on 31 views — every other top-10 page shows 28–72s. Page renders correctly (200, correct title, FAQ schema). Suspect: search-snippet answers the query fully (it's a checklist page), or a mobile render issue. Needs a live mobile-screenshot look before touching content.
- **B4 — Top-5 page `diy-flywheel-energy-storage` (45 views, 45s ToP) has ZERO monetization** — the only unmonetized top-20 page. It's a "Project Lab" experimental piece, but a flywheel-storage reader is a battery/beginner-kit buyer. One contextual pick (LiFePO4 starter or power meter) fits the page honestly.
- **B5 — Freshness stalling**: last content change 9/12; only 7/160 pages carry an `updated` param; sitemap lastmods cluster at 9/5–9/6. Fine for maintenance-only mode per PM, but zero freshness signals works against re-crawl once GSC lands.
- **B6 — Home page (162 views, #1 page) has no monetization or featured-product surface.** 29% of all pageviews hit a page that sells nothing. Even a single "start here kit" strip would put a money surface on the most-seen page.
- **B7 — Rybbit API 403 from workstation** (blocker for the Monday ritual, not for the site). Likely rate-limit or key rotation; retest before next scheduled pull.

## Not reproducible / cleared
- Googlebot 403 (prior issue): both Googlebot and GPTBot UAs get 200 now.
- Dead Amazon listings (3 fixed in bd9f63c): current sweep shows 0/24 dead.

## Recommended order
1. Owner: GSC enroll + verify + submit sitemap (unblocks everything).
2. Add 1 contextual pick to flywheel page; consider home-page starter-kit strip.
3. Investigate battery-not-charging 0s-ToP anomaly (mobile QA).
4. Retest Rybbit API; resume Monday ritual.
5. After GSC: 2–4 week indexation watch, then freshness pass on top-20 pages.
