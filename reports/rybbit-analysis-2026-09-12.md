# Rybbit Analytics Analysis — solarpoweredproject.com (site id 4969)

**Window analyzed:** 2026-06-14 → 2026-09-12 (pulled live from Rybbit API 2026-09-12)
**Author:** Boss session (direct API pulls; agency seats not needed for data collection)

## Headline numbers

| Window | Sessions | Pageviews | Users | Pages/sess | Bounce | Avg dur |
|---|---|---|---|---|---|---|
| 6/14–7/13 | 29 | 29 | 23 | 1.00 | 100% | 0s |
| 7/14–8/13 | 224 | 236 | 174 | 1.05 | 96% | 7s |
| 8/14–9/12 | 637 | 699 | 394 | 1.10 | 92% | 11s |

- Growth is real and steep (~3× month over month), but from a tiny base: current run-rate ≈ **20–35 pageviews/day, ~700 pv/month**.
- All-time: 1,592 sessions / 2,290 pv / 1,204 users.

## Traffic quality — the most important finding

**90% of sessions are "Direct" and 60% of visitors are CN**, with US at only ~14% (89 sessions/30d).
Browser mix confirms this: Chrome WebView (260) + Mobile Chrome (252) dominate; WeChat (5), and CN-heavy patterns. Much of the "CN Direct" traffic has single-page, ~0s sessions — it resembles traffic-farm/invalid traffic that slips past Rybbit's bot filters.

**Channels (30d):** Direct 572 (89.8%) · AI 50 (7.8%) · Organic Search **12 (1.9%)** · Social 2 · Referral 1.
Referrers: google.com 11 · chatgpt.com 9 · bing 1.

Bot layer (Rybbit, separate): 2,223 bot requests vs 2,929 total events = 75.9% bot rate; 496 AI-crawler requests. Googlebot/Bingbot verified receiving real content since 2026-09-06 fix.

**Interpretation:**
1. The **real buyer base is ~89 US sessions/30d**, not 637.
2. **Organic search is nearly dark** (12 sessions/30d despite 160 indexed-quality pages + Googlebot fix on 9/6). The fix was recent; ranking lift hasn't arrived yet. GSC verify+submit remains the biggest un-pulled measurement lever (user-owned, 10 min).
3. **AI referrals (50 sessions, chatgpt.com) are already ~40% of genuine discovery** — the site is becoming an AI-citation source. Quality bar matters for that channel.

## What's actually getting traffic (30d entry sessions)

Two clusters own the traffic:

**A. DIY off-grid energy cluster (unmonetized):** Pelton turbine (33) · solar-battery-not-charging (30) · Savonius wind (25) · Stirling engine (24) · hand-crank (23) · pedal power (22) · TEG (21) · micro-hydro (18) · gravity battery (16) · supercapacitor (14) · treadmill motor (14). Bounce 87–100%, ~3 internal links each, **0 product boxes on 12 of 14**.

**B. Troubleshooting/calculator cluster (partially monetized):** mppt-not-charging (23, 1 box) · solar-panel-output calc (18, 1 box) · 12v-vs-24v-vs-48v (14, 2 boxes) · pure-sine-vs-modified-sine (15).

## Revenue reality

- **Outbound affiliate clicks in 30d: 2** (both 2026-08-26, old litwd-20 URLs; current tag is slrpwp-20 via hugo.toml swap-point).
- AC-001 contract: $2k/mo ≈ $50–67k referred sales at verified fixed category rates (3–4%). At current volume that needs roughly a 20–30× traffic increase with maintained intent quality. **Traffic is the binding constraint, not conversion yet** — but the DIY cluster getting the majority of traffic with zero monetization is free upside.

## Improvement plan (priority order)

**P1 — Monetize + interlink the DIY cluster (free upside on existing traffic).**
12 top-traffic pages have 0 product boxes and ~3 internal links. Add 1–2 honest product boxes per page (multimeter, MC4/fuse gear, small charge controllers, LiFePO4 batteries, hand-crank/TEG-adjacent products only where genuinely relevant — no forced fit) + a "next step" block linking each DIY page to its monetized cousin (e.g., TEG→battery-charging pages, Pelton→charge-controller sizing, hand-crank→solar-phone-charger). Also give solar-battery-not-charging (30 sessions, the #2 page) internal links + a diagnostic-tools box. Target: pages/session 1.1 → 1.4+, first recurring affiliate clicks.

**P2 — Pull the search levers (user-owned, highest leverage).**
GSC verify + submit sitemap (160 URLs); Bing Webmaster same. Without it we're blind on queries and indexation. Then first GSC-driven retitle pass (strategy phase 4 pull-forward).

**P3 — Clean the analytics signal.**
Add CN (+ any non-buyer geos) to Rybbit excluded-countries so dashboards reflect the buyer base; keep AI channel visible. Optional: enable outbound-click tracking toggle verification (R-002 — appears ON now since outbound events are flowing; confirm and close).

**P4 — Feed the winners.**
The DIY cluster is what AI engines and readers cite. Ship 3–5 adjacent pages (DIY cluster is the proven demand): e.g., "DIY solar generator from scratch", "how many watts does a well pump need" style — cross-linked per P1. Keep the winter/Q4 outage calendar from the affiliate strategy running (BLUETTI-vs-Jackery, CPAP/freezer/oxygen PF-8 passes).

**Not recommended:** chasing the CN/direct traffic (invalid-traffic risk, no buyer intent, pollutes CTR math).

## Data-quality notes (Rybbit API quirks, for future pulls)

- `range=30d/90d/180d` params are unreliable (returned identical all-time numbers); use explicit `start_date`/`end_date`.
- `filters` param 500s server-side ("Cannot set property errors"); US-only slices currently impossible via API.
- `parameter=page` 500s; use `/page-titles` (pathname included) or `parameter=entry_page`.
- time-series `interval=day` returns ~hourly mislabeled buckets; aggregate in Python by date prefix.
