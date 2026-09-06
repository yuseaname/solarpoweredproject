+++
title = "LiFePO4 100Ah Battery Brands: A Spec-Math Comparison (No Testing Claims)"
slug = "lifepo4-100ah-brand-comparison"
date = 2026-09-05
draft = false
description = "Compare 100Ah LiFePO4 battery brands by published specs — BMS current, claimed cycles, weight, warranty, cold protection — honest math, no testing."
author = "Solar Powered Project"
related = [
  "/pages/li-ion-vs-lead-acid.html",
  "/pages/how-long-will-100ah-battery-run.html",
  "/pages/solar-battery-cost-per-kwh.html",
  "/pages/solar-battery-management-system-explained.html",
  "/pages/best-solar-batteries-2026.html"
]
+++

{{< affiliate-disclosure >}}

## Quick answer

Before choosing any 100Ah LiFePO4 battery, compare **published manufacturer specs**, not marketing: **rated capacity (Ah), BMS continuous discharge current (A), claimed cycle life, weight, warranty years, and low-temperature charge protection**. This is a spec-math comparison — we do not test batteries and make no testing claims. Every number comes from a brand's own product page or spec sheet fetched for this article; anything unverifiable is marked **verify before buying**.

Across the five brands we checked: **nearly every 12V 100Ah LiFePO4 claims ~1,280Wh (100Ah × 12.8V), a 100A BMS, 4,000+ claimed cycles, and weighs 21–27 lbs**. The differences show up in the details — peak/continuous discharge limits, the fine print under cycle-life claims, warranty terms, and cold protection. Learn those four specs and you can size and compare any battery yourself.

## Key takeaways

- **Energy, not amps, is the honest unit.** 100Ah × 12.8V = 1,280Wh total; at a realistic 90% usable depth of discharge, that's **~1,152Wh usable**.
- **BMS continuous current is the limit that matters.** 1,000W ÷ 12V ≈ 83A — a 100A BMS is at ~83% of its continuous rating, so keep at least 200W of headroom (the "200W headroom rule").
- **"4,000 cycles" is a claim, not a guarantee.** Typically tested at a stated DOD and temperature; real-world cycles depend on how you run the battery.
- **Weight is a sanity check.** A genuine 100Ah LiFePO4 (four prismatic cells) weighs ~19–25 lbs; suspiciously light batteries may use fewer, smaller, or lower-grade cells.
- **Cold protection comes in two flavors:** a BMS that cuts off charging below ~32°F (0°C), or a heated/self-heating version that warms cells so you can keep charging in freezing weather. Know which you're buying.
- **Price is not in this article** (per marketplace rules). We teach the **$/usable-Wh method** so you can compute value with today's listed price.

## The spec table: five brands, published numbers only

The models are the standard "100Ah deep-cycle" offering from each brand: Renogy Core Mini 12.8V 100Ah, LiTime 12V 100Ah (Group 31 footprint), Redodo 12V 100Ah Group 31 Basic, ECO-WORTHY 12V 100Ah (SOC display), ExpertPower EP12100. Numbers come from the brands' own product pages — every row re-verified 2026-09-06 against the manufacturers' current listings; re-verify against the live datasheet before purchase — specs drift. Anything unverifiable is marked **verify before buying**. Cycle life is always labeled **claimed** — it's a manufacturer test claim, not our measurement. The LiTime row now has its own page: our [LiTime 100Ah spec-based review](/pages/litime-100ah-review.html) works the ceiling, charging, and cold-weather math in full.

| Brand / model | Capacity | BMS continuous discharge | Claimed cycles | Weight | Warranty | Cold protection |
|---|---|---|---|---|---|---|
| Renogy Core Mini 12.8V 100Ah | 100Ah (0.5C, 25°C) | 100A; peak 300A @ 5s | Claimed 5,000 cycles (80% DOD, 80% EOL, 0.5C, 25°C) | 21.8 lbs / 9.9 kg | 5-year prorated | Low-temp charge cutoff (built-in; won't charge below 32°F/0°C) |
| LiTime 12V 100Ah (Group 31 footprint) | 100Ah | 100A; 400A @ 1s | Claimed 4,000 cycles @ 100% DOD (also 6,000 @ 80% DOD, 15,000 @ 60% DOD) | ~24.25 lbs | 5 years | None (charge temp 32°F–122°F; FAQ: charge above 32°F/0°C only); heated versions sold separately |
| Redodo 12V 100Ah Group 31 | 100Ah | 100A; 300A @ 5s (500A @ 1s per listings) | Claimed 4,000+ cycles @ 100% DOD (25°C, 0.2C) | ~24.25 lbs | 5 years | Low-temp charge cutoff on current Group 31 listings (e.g., B0CN1BKPH1); self-heating version sold separately |
| ECO-WORTHY 12V 100Ah (SOC display) | 100Ah | 100A (charge/discharge) | Listing-dependent: 4,000–15,000 claimed depending on version — **verify the exact SKU's figure before buying** | ~22.9 lbs (current listing) | 3 years per ECO-WORTHY's official warranty page; 5 years claimed on Amazon listings — **verify before buying** | Cutoff listed at 19.4°F/−7°C — below the 0°C chemistry guidance; treat with caution and verify the actual BMS behavior |
| ExpertPower EP12100 | ≥100Ah (25°C, 0.2C) | 100A continuous; 200A 2-sec | Claimed 2,500 @ 100% DOD / 3,600 @ 80% DOD / 7,000 @ 50% DOD | ~27 lbs (current official page; earlier runs ~22.6 — verify your listing) | 2 years | BMS claims low-temp protection; threshold not published — charge temp 32°F–140°F, discharge −4°F–140°F; **verify before buying** |

**Peak discharge** differs meaningfully: Renogy claims 300A for 5s, LiTime 400A for 1s (re-verified 2026-09-06), Redodo 300A for 5s and 500A for 1s per current listings, ExpertPower 200A for 2s. ECO-WORTHY does not publish a peak number (**verify before buying**). Peaks fund short surge loads (inverter start), not continuous loads.

**How to read "claimed cycles":** Renogy's 5,000 is at 0.5C discharge and 80% DOD; Redodo's 4,000+ at 0.2C and 100% DOD; LiTime states 4,000 at 100% DOD and higher numbers at gentler DOD. None is a promise of what *your* battery will do — they're lab claims under stated conditions, which is why we always write "claimed."

If your build's math already lands on the 100Ah LiTime row — loads under the 100A BMS ceiling, battery kept above freezing — {{< amazon asin="B084DB36KW" text="check its current price on Amazon" placement="mid-page" >}}; the full ceiling, charging, and cold-weather math is in our [LiTime 100Ah review](/pages/litime-100ah-review.html), and the spec-decoder table below is there if you're still comparing.

### What each spec means for your build

| Spec | What it tells you | Trap |
|---|---|---|
| Rated capacity (Ah) | Energy = Ah × 12.8V (100Ah = 1,280Wh; ~1,152Wh usable at 90%) | The C-rate and temp it's rated at change real capacity |
| BMS continuous discharge (A) | Sustained current; compare watts ÷ 12V | Peak amps in big print, continuous in fine print |
| Claimed cycle life | Lab durability at stated DOD and C-rate | Claims at different DODs aren't comparable |
| Weight | Sanity check (~19–25 lbs for 100Ah) | Suspiciously light packs may carry smaller cells |
| Warranty (years) | How long the maker backs it | Prorated vs full replacement; read the terms |
| Cold protection | Charge-cutoff BMS vs heated version | Cutoff temperature often unlisted — verify before buying |

## $/usable-Wh method (no prices, by design)

We're not allowed to print prices here, and prices change weekly anyway. So here's the method to compare any two batteries on value, using *today's* listed price:

**Usable Wh = 100Ah × 12.8V × 0.9 usable = 1,152Wh usable**

That 0.9 is a realistic usable depth of discharge for LiFePO4 (see our [lithium-ion vs lead-acid](/pages/li-ion-vs-lead-acid.html) comparison for why usable DoD is ~80–90%, not 100%). Then:

**$/usable-Wh = today's listed price ÷ 1,152 usable Wh**

**Worked (illustrative) example** — placeholder, not a real price: if a battery is listed at $X where X = 300, then $300 ÷ 1,152Wh ≈ **$0.26 per usable Wh**. Do the same for a competitor at $Y; lower $/usable-Wh wins on pure energy cost. Add warranty years and cold protection on top — a few cents per Wh can buy years of coverage.

For the broader cost-per-kWh picture (including lifespan), see our [solar battery cost per kWh](/pages/solar-battery-cost-per-kwh.html) guide.

## Weight sanity check: suspiciously light = suspect cells

A true 100Ah LiFePO4 contains four prismatic cells plus a BMS, busbars, and a case. Across the five brands we fetched, published weights run **21.8 lbs (Renogy), 21 lbs (LiTime), 22.05 lbs (Redodo), 23.37–25.1 lbs (ECO-WORTHY), 27 lbs (ExpertPower)** — bracketing the ~19–25 lb range you'd expect from real cells.

**The check:** if a "100Ah" battery weighs meaningfully less than ~19 lbs, ask why. Fewer cells means less capacity; lighter cells can mean lower grade. Weight can't prove a battery is good — but a battery far under normal weight for its chemistry and capacity is a red flag.

## BMS current vs inverter draw: the 200W headroom rule

Your inverter sees watts, the battery's BMS sees amps:

**Inverter draw (amps) ≈ inverter watts ÷ 12V**

A 1,000W inverter at full load pulls **1,000W ÷ 12V ≈ 83A**. On a 100A continuous BMS, that's 83% of the limit — one sag, surge, or cold cell away from the BMS tripping mid-load.

**The 200W headroom rule (a rule of thumb, not a spec):** size so continuous load stays at least ~200W under what the battery can feed. For a 100A BMS at ~12.8V nominal that's ~1,280W theoretical but ~1,050–1,100W practical continuous. If you'll run a 1,000W inverter regularly, or any load near the BMS ceiling, step up to a 200Ah battery or add a second 100Ah in parallel. See our [BMS explainer](/pages/solar-battery-management-system-explained.html) for how the protection board behaves, and our [runtime math article](/pages/how-long-will-100ah-battery-run.html) for how long 100Ah lasts under real loads.

## Cycle-life claims: 3,000–4,000+ cycles, but read the conditions

Almost every brand claims 3,000–4,000+ cycles to 80% capacity — sometimes more. That's a lab test under specific conditions; three things change real-world life:

1. **Depth of discharge** — LiTime publishes 4,000 cycles at 100% DOD but 6,000 at 80% DOD and 15,000 at 60%. Shallower cycles last longer.
2. **Discharge rate** — Renogy's 5,000-cycle claim is at 0.5C; Redodo's is at 0.2C. Gentler pulls age cells less.
3. **Temperature** — cold charging and sustained heat shorten life. A battery never charged below freezing will generally outlast one that is.

Treat any cycle number as **"claimed, under stated lab conditions"** and compare claims only apples-to-apples (same DOD and C-rate). For what cost-per-kWh works out to over the battery's life, read our [solar battery cost per kWh](/pages/solar-battery-cost-per-kwh.html) analysis.

## Cold protection: heated versions vs charge-cutoff BMS

This is the spec most people miss. Two different designs:

- **BMS charge cutoff** — the battery refuses to charge below ~32°F (0°C), protecting cells but leaving you with no charging on a freezing morning. Renogy's Core Mini has this built-in ("built-in low-temperature charging cut-off … below 32°F / 0°C"). LiTime's base Group 24 has no low-temp protection; its own FAQ says to charge only above 32°F (0°C) and bring it indoors to charge in freezing weather. ExpertPower lists charge temperature 32°F–140°F with no low-temp protection feature (**verify before buying**).
- **Heated / self-heating version** — a built-in heater warms the pack so you can keep charging in cold (e.g., LiTime's "Cold Weather" models, Redodo's "Heating" 100Ah, Renogy's Pro self-heating series). Heated versions cost more but matter for winter off-grid, RVs, and cabins where the battery lives outdoors — the heater math and warm-up times are worked out in our [LiFePO4 cold-charging guide](/pages/lifepo4-charging-below-freezing.html), and the rest of the seasonal checklist lives in [winterizing your off-grid system](/pages/winterizing-off-grid-system.html).

ECO-WORTHY's page lists "low-temperature protection" on the 100Ah SOC-display model but doesn't publish the exact cutoff temperature — **verify before buying** if you'll charge in cold.

If you live with freezing winters, this one spec should be a deciding factor, not an afterthought.

## What we'd verify before buying (checklist)

Bring this list to the product page and the full spec sheet — not the marketing bullets:

1. **Rated capacity and nominal voltage** — 100Ah at what C-rate and temperature? (e.g., "100Ah @ 0.5C, 25°C" vs "@ 0.2C").
2. **BMS continuous discharge current** — 100A is common; confirm it's *continuous*, not peak. Compare against your inverter's max draw (watts ÷ 12V).
3. **Peak discharge and duration** — 300A @ 5s vs 300A @ 1s differ for surge-heavy loads.
4. **Cycle-life claim and its conditions** — meaningless without the DOD and C-rate attached.
5. **Weight** — should land ~19–25 lbs for a true 100Ah LiFePO4; verify against the published cell count if given.
6. **Warranty years and what's covered** — prorated vs full replacement changes what the warranty is worth. See [best solar batteries 2026](/pages/best-solar-batteries-2026.html).
7. **Cold protection** — charge-cutoff BMS vs heated; and the exact cutoff temperature if published.
8. **Certifications & ratings** — e.g., UN38.3 (transport), UL listings; all brands here list at least some (UN38.3, CE, FCC, RoHS or UL on ExpertPower's cell-level spec).
9. **Usable energy, not raw Ah** — 100Ah × 12.8V × 0.9 = **1,152Wh usable**; divide today's price by that for the $/usable-Wh comparison.
10. **Expansion and terminals** — series/parallel limits and M8 terminal compatibility with your busbar/lugs.

For full runtime, usable-capacity, and chemistry math, start with [how long will a 100Ah battery run](/pages/how-long-will-100ah-battery-run.html) and [lithium-ion vs lead-acid](/pages/li-ion-vs-lead-acid.html). For a broader 2026 look, see [best solar batteries 2026](/pages/best-solar-batteries-2026.html).

## FAQ

{{< faq "Do you test these batteries?" >}}
No. We do not test batteries and make no testing claims. This page compares published manufacturer specifications from each brand's product page or spec sheet, and marks anything unverifiable as "verify before buying." Treat every cycle-life figure as a claimed, lab-condition number.
{{< /faq >}}

{{< faq "What does '100A BMS' actually limit?" >}}
It's the maximum continuous discharge (and often charge) current the protection board allows. A 1,000W inverter at full load pulls about 83A (1,000 ÷ 12), already 83% of a 100A BMS ceiling. Apply the 200W headroom rule and keep continuous loads roughly 200W under the practical limit.
{{< /faq >}}

{{< faq "Is a lighter 100Ah battery automatically bad?" >}}
Not automatically, but it's a sanity flag. Verified weights for genuine 100Ah LiFePO4 across five brands run 21–27 lbs. If a "100Ah" battery is much lighter than roughly 19–25 lbs, question the cells — fewer or lower-grade cells is the usual explanation.
{{< /faq >}}

{{< faq "How do I compare prices without seeing prices here?" >}}
Use the $/usable-Wh method: usable Wh = 100Ah × 12.8V × 0.9 ≈ 1,152Wh. Divide today's listed price by 1,152 to get $/usable-Wh, then compare across brands, and add warranty years and cold protection to the decision.
{{< /faq >}}

{{< faq "Do I need a heated battery for winter?" >}}
Only if you need to *charge* below ~32°F (0°C). A BMS charge-cutoff battery just refuses to charge in the cold; heated/self-heating versions warm the pack so charging continues. If your battery lives indoors or you only discharge in the cold (discharge is fine to −4°F on most), a charge-cutoff BMS may be enough.
{{< /faq >}}

## Next logical reads

- [How long will a 100Ah battery run? The runtime formula, decoded](/pages/how-long-will-100ah-battery-run.html)
- [Lithium-ion vs lead-acid batteries (solar comparison)](/pages/li-ion-vs-lead-acid.html)
- [Solar battery cost per kWh: pricing, lifespan, and value](/pages/solar-battery-cost-per-kwh.html)
- [Solar battery management systems (BMS): what they do and when you need one](/pages/solar-battery-management-system-explained.html)
- [Best solar batteries for home 2026: brand comparison guide](/pages/best-solar-batteries-2026.html)