# Completion Contract — solarpoweredproject.com

**Version 1.0 · 2026-09-06 · Authority: site owner (user) · Status: Active**

## Desired Outcome
solarpoweredproject.com generates **$2,000/month in net affiliate revenue** (Amazon Associates), measured as the trailing 3-month average, with the site operating on its honesty standards (no dark patterns, disclosure-first, spec-based reviews).

## Revenue Model (planning baseline, not a promise)
- Commission baseline: **3%** (Home/Home Improvement — controllers, batteries, panels, inverters); some items (consumer-electronics-classed power stations) at 4%. Sources: [Standard Commission Income Rates](https://affiliate-program.amazon.com/help/node/topic/GRXPHT8U84RAYDXZ), [Onsite Commission Income](https://affiliate-program.amazon.com/help/node/topic/G4ARBJC7Z2NK48CA), retrieved 2026-09-06. Rates change; re-verify quarterly.
- At 3%: $2,000/mo ≈ **$67k/mo qualifying revenue** ≈ 130–270 orders at a $250–400 blended AOV ≈ **2,000–9,000 affiliate clicks/mo** ≈ roughly 30k–150k visits/mo at 3–10% click-through on commercial pages.
- Honest implication: this is a **12–24 month SEO build** under good conditions (indexation fixed + ~2 publishes/week sustained). Timeline is Unknown by nature; the lever hierarchy below is how it gets shorter.

## Acceptance Criteria
**Revenue gate (defines completion):**
- [ ] AC-001: Trailing 3-month average of Amazon Associates fee earnings ≥ $2,000/month, verified in Associates reports (not estimated from clicks).

**Enabling criteria (leading indicators, all required on the path):**
- [ ] AC-002: Measurement live — Rybbit outbound toggle ON; `affiliate_click`/`reached_end` events populating; monthly funnel reports produced (per affiliate-cro-audit §6).
- [ ] AC-003: Googlebot unblocked — `curl -s -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://solarpoweredproject.com/` returns 200; pages visibly indexed in Google Search Console.
- [ ] AC-004: Buyer-intent calendar fully executed — every weeks-2–13 row shipped or formally dispositioned in the plan's execution log (17 pages incl. winter cluster by mid-Oct).
- [ ] AC-005: Conversion loop operating — at least 3 monthly measurement-driven adjustments made and documented (placement changes, handoff copy, new reviews) with before/after CTR data.
- [ ] AC-006: Revenue checkpoints passed in order — first $100/mo month, first $500/mo month, first $1,000/mo month (each logged in STATUS.md).
- [ ] AC-007: Quarterly maintenance cycle executed at least once — price bands refreshed, OA/policy re-verify, tag-integrity grep, glossary expansion (owner + generated dated list per CRO audit §7 item 5).
- [ ] AC-008: Zero compliance debt — annual re-audit of the OA risk register shows no unresolved non-VERIFY items; P1 disclosure-first holds sitewide.

## Quality Requirements
- **Reliability:** build clean; 0 broken internal links; 153+ URLs all 200.
- **Editorial honesty:** binding — no fabricated testing/prices/ratings; spec-based reviews with retrieval dates; corrections log maintained.
- **Compliance:** Amazon OA + Program Policies; disclosure-first; `rel="sponsored"`; verbatim OA sentence present.
- **Accessibility:** WCAG 2.2 AA on contrast/targets (achieved 2026-09-06); no regressions.
- **Maintainability:** single design-source CSS; single affiliate tag swap point; reports/ as decision record.
- **Documentation:** STATUS.md current at each milestone; corrections log for user-visible changes.

## Launch or Handoff Requirements
- Continuous deploy via git push (existing). No separate launch event.

## Constraints
- **Time:** none fixed; seasonal windows matter (winter content by early-mid Oct; state-incentive pages before summer).
- **Budget:** $0 paid acquisition — organic only. No paid traffic, no paid links.
- **Technology:** Hugo static; URLs never change; consolidation via canonicals only.
- **Permissions:** production changes only via this repo's deploy path; external services (Hostinger panel, Rybbit dashboard, Associates account) are user-owned.
- **Other:** all Amazon-side promotion rules per the CRO audit's risk register; no email/PDF/social link promotion.

## Explicitly Out of Scope
- Paid ads/traffic; black-hat or gray-hat SEO; fabricated trust signals; second affiliate networks on the same links (OneLink may be evaluated separately); redesign/replatforming; non-content engineering projects.

## Acceptance Authority
The site owner (user). Completion is declared only against AC-001 with evidence from Associates reports.

## Completion Evidence
Associates earnings reports (3-month window); Rybbit funnel exports; Google Search Console indexation status; git history; STATUS.md milestone log.

---

## Decisions
**D-001: Completion defined as revenue outcome (not deliverable list)**
- Date: 2026-09-06 · Status: Accepted (user)
- Context: site is post-five-audits with queued content calendar; "complete" was undefined.
- Options: content-plan-executed / traffic milestone / steady-state ops / revenue target / combination.
- Decision: **$2,000/mo trailing-3-month revenue.**
- Rationale: aligns all work with the actual goal; calendar and ops become means, not ends.
- Consequences: measurement and indexation become critical-path; roadmap re-prioritized revenue-first; timeline is demand-dependent (Unknown) — managed via leading indicators AC-002..AC-008.

**D-002: PM system = thin integration layer**
- Date: 2026-09-06 · Status: Accepted (delegated by user)
- Decision: `reports/COMPLETION_CONTRACT.md` (this file) + `reports/STATUS.md` (live index). Existing reports remain authoritative for their domains; content-plan calendar remains the roadmap of record. No `.project-manager/` scaffold (would duplicate).

## Scope Changes
*(none yet — record any as SC-00n here)*
