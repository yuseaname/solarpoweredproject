# CTA-COPY-LIBRARY — Compliant CTA text and handoff patterns

*Boss-authored 2026-09-05 (seat rt-ux's Part C was truncated in delivery; findings from its completed Part A live-site audit are incorporated). Governing rules: no urgency, no savings claims, no prices, no superlatives, no pressure; the affiliate nature is disclosed by the product-box's built-in line, not obscured.*

## Current state (verified live, 2026-09-05)

- One uniform button string sitewide: **"Check price on Amazon"** — 32 pages, 44 boxes at audit close (33/45 at start; one mismatched box removed during the audit).
- Every box renders its own disclosure ("Price & availability shown on Amazon.com — we may earn a commission.") and `rel="sponsored nofollow noopener"`.
- CTA-after-value holds across the reviewed surface: almost all boxes sit 60–95% into the body; zero CTAs above the fold on the six live pages checked.

## Recommendation

**Keep the single uniform button string.** Consistency is a trust feature here: it never promises savings, never goes stale, and reads as process rather than persuasion. Variation belongs in the *handoff sentence* that precedes a box — that is where context, honesty, and scenario-matching live.

## Approved button strings (only if a context genuinely needs one)

| String | Context | Note |
|---|---|---|
| `Check price on Amazon` | DEFAULT — all boxes | the standard; use unless a below case clearly fits |
| `See specs on Amazon` | informational/diagnostic boxes (e.g., a multimeter on an output-verification page) | honest when the click is for the datasheet, not a deal |
| `Check current price on Amazon` | acceptable synonym | no advantage over the default — prefer default |

All: verb-first, ≤5 words, no "now/best/save/deal". Never more than one string in rotation per page.

## Handoff sentence patterns (the sentence right before a box)

**Roundup pick:**
- "If your sizing math lands at 20–30 A on a 100 V rail, this is the model to price first."
- "If you're building the ecosystem end-to-end, the installed row above is your quote to request — the box below is the DIY path."

**Vs-page decision point:**
- "If the table put you in the MPPT column, the sizing checks above — not the label — decide which model."
- "If PWM won your scenario, a basic 10 A unit from the cost guide's budget band is all the controller you need."

**Informational page box:**
- "If your load math landed in the lights-and-tool-charging band rather than the workshop scenarios, this is the baseline kit that fits."
- "Once your watt-hour math says how many watts of panel you need, this is the module to check the number against."

**Not-on-Amazon path (installed products):**
- "You can't order a Powerwall or an IQ Battery on Amazon — get three installer quotes and ask the five questions above."
- "Installed systems ship through certified installers; the box below is the DIY building block, not the turnkey unit."

## Non-examples (would violate the ethics frame / Associates norms — with reasons)

| Copy | Why it fails |
|---|---|
| "Buy now — best price today!" | urgency + manual price implication |
| "Save 40% on Amazon right now" | savings claim + urgency; savings are dynamic and not the site's to claim |
| "Our #1 pick — grab yours before it's gone" | deceptive winner label + false scarcity |
| "Limited stock — check Amazon" | availability is dynamic; asserting it is fabrication |
| "Customers love this one" | review-derived claim; review content is off-limits |
| "The last controller you'll ever buy" | unsupported superlative |

## Placement rules (from the structural scan + rt-ux live checks)

1. No box before the decision logic it serves; house norm ≥60% into the body; vs pages ~90%+.
2. A box must never reference content the reader hasn't reached ("the worked example below" → move the box, don't shortcut the argument).
3. Never place a box after a forked link block (the reader has already left the page's decision).
4. One box per distinct purchase decision; a page with no purchasable answer gets no box.
5. The closing CTA for quote-based paths is advice, not lead-gen: "get three quotes and ask for a written load analysis" — never "see how much you could save!"
