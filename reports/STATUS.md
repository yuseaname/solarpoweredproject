# STATUS — solarpoweredproject.com

**Live index · one page · updated at each milestone · PM: project-manager skill (Boss session)**
**Definition of complete:** [COMPLETION_CONTRACT.md](COMPLETION_CONTRACT.md) — $2,000/mo trailing-3-month affiliate revenue (AC-001). Version 1.0 accepted 2026-09-06.

## Current milestone
**M-A: Traffic engine running** (calendar execution + measurement + indexation). Progress: measurement wired (2026-09-06, `daab276`); winter window open until ~early Oct; first-10 of calendar shipped (prior session).

## Next actions
**User-owned (top levers, in order):**
1. **Googlebot 403 fix** (Hostinger firewall) — gates ALL Google-side returns. Test: `curl -s -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://solarpoweredproject.com/` → must return 200. [R-001]
2. **Rybbit outbound toggle** (dashboard → Settings → "Track clicks to external websites") — starts the CTR data that drives AC-005. [R-002]

**In-repo queue (revenue-first order):**
1. ~~Renogy Rover 40A review~~ — **DONE 2026-09-06** (`dd61903`), 4th review live, roundup link closed.
2. LiTime 100Ah review (verify datasheet claims vs brand-comparison table first) — weeks-2 item.
3. Winter cluster by ~Oct 10: well-pump power-station sizing (240V honesty angle), van-conversion use-case, winterizing off-grid systems. **Time-sensitive** (pre-season publishing window).
4. Remaining weeks-3–13 per [buyer-intent calendar](buyer-intent-content-plan-2026-09-05.md) (authoritative roadmap of record).
5. First monthly Rybbit funnel report — as soon as toggle is on + 30 days of data (AC-002/005).

## Open user decisions (non-blocking)
Byline Option A (real name in authors.html + meta row) · OneLink (revenue-only; re-check cookieless first) · reply-window line on contact (only if truthful) · dedicated hero art for 5 pages currently reusing themed assets.

## Top risks
- **R-001 Googlebot 403** — Certain-until-fixed · Critical · owner: user. Every month unfixed ≈ month added to AC-001.
- **R-002 measurement dark** — High likelihood until toggle · High · owner: user (2 min).
- **R-003 freshness drift** — Medium · Medium · quarterly cycle (AC-007): price bands, OA re-verify, tag grep, glossary +20.
- **R-004 bus factor** — Medium · Medium · mitigated by reports/ layer; no ops runbook yet.

## Authoritative docs (do not duplicate)
Roadmap/calendar + 36-row backlog: `buyer-intent-content-plan-2026-09-05.md` (+ addenda) · Public changelog: `/corrections.html` (content/corrections.md) · Standards: `review-templates/` (templates, CTA library, table fields) · Audits: content-quality, SEO, review-template, UX/trust, affiliate-CRO (each with execution addenda) · Contract: `COMPLETION_CONTRACT.md`.

## Milestone log
- 2026-09-06: Contract v1.0 accepted (revenue outcome). PM layer = thin integration (D-002).
- 2026-09-06: T-001 Renogy Rover 40A review shipped; roundup review-link set complete (4/4).
- *(prior work recorded in git history + reports addenda; log forward from here)*
