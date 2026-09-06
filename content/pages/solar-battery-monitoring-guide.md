+++
title = "Solar Battery Monitoring: State of Charge Without Guesswork (Shunts Explained)"
slug = "solar-battery-monitoring-guide"
date = 2026-09-06
draft = false
description = "Voltage lies about lithium state of charge. How shunt-based monitors count amp-hours, the BMV-712 vs SmartShunt vs budget class compared, and the one install rule that makes them accurate."
image = "/images/solar-battery-monitoring-guide/hero.webp"
image_alt = "Two deep-cycle batteries with cables installed inside a wooden shed — the bank a shunt-based monitor watches"
author = "Solar Powered Project"
image_width = 1536
image_height = 864
related = [
  "/pages/solar-battery-management-system-explained.html",
  "/pages/battery-capacity.html",
  "/pages/lifepo4-100ah-brand-comparison.html"
]
+++

{{< affiliate-disclosure >}}

## Quick answer

**A shunt-based battery monitor is the only honest way to know your bank's state of charge on a live solar system** — voltage readings can't do it, especially with LiFePO4, whose voltage curve is nearly flat across the middle of its range. A shunt (a precision resistor in the battery's negative line) measures every amp in and out and counts the balance; the monitor turns that into state of charge, amps, and time-to-go. The practical choice: a **Bluetooth app-first unit** (Victron SmartShunt class) for most builds, a **display unit** (BMV-712 class) if you want SOC readable on the wall without opening an app, or a **budget shunt meter** for a shed system where ~±5% is acceptable. The install rule that makes any of them accurate: *everything* — every load, every charge source — connects on the shunt's far side, with only the shunt itself touching battery negative.

This page is spec math and manufacturer documentation; we test nothing. Prices stay on the retailer's page, not ours.

## Why voltage lies (especially with LiFePO4)

Reading state of charge from a battery's voltage requires a *resting* battery — no charge, no load, for hours. On a live system that condition never happens, so voltage bounces with every cloud and fridge cycle:

- **LiFePO4's flat curve:** roughly 13.2V to 13.0V covers a huge share of the usable range on a 12V lithium bank. A reading of 13.1V could be 40% or 80% — the chemistry simply doesn't announce its level in volts the way lead-acid sort-of does (this is the flat discharge curve that also makes lithium's delivered voltage so stable — the same property read from the other side).
- **Under load, voltage sags;** under charge, it rises. Both lie about the underlying charge.
- **Temperature shifts resting voltage** on top of everything else.

Lead-acid banks have the same problem with a steeper curve. The universal fix is the same: stop inferring, start counting.

## How a shunt counts (and why it needs one honest sync)

A shunt is a resistor of precisely known value (the standard is **50mV drop at rated current** — e.g., 500A/50mV). The monitor measures the tiny voltage across it, converts to amps via Ohm's law, and integrates amps over time — coulomb counting. Three consequences worth knowing:

1. **It counts everything that crosses it.** Loads, solar charge, alternator charge, the inverter — all of it becomes one honest ledger.
2. **It drifts without a reference.** Counting has small errors (measurement noise, charge-efficiency assumptions), so the monitor resynchronizes its "full" zero-point whenever the bank reaches a confirmed full charge (charge current tapering to a threshold at absorption voltage — the standard sync condition). A system that never reaches full keeps drifting; that's a usage fact to know, not a flaw.
3. **LiFePO4 makes counting mandatory.** Because the voltage curve is flat, lithium banks are effectively unmonitorable by voltage; every serious lithium build uses a shunt. Lead-acid can be checked with a hydrometer (flooded) as a cross-check — lithium has no equivalent.

## The units compared (verified against manufacturer pages, 2026-09-06)

| Spec | Victron BMV-712 Smart | Victron SmartShunt | Budget shunt meters (AiLi class) |
| :-- | :-- | :-- | :-- |
| Type | Display head + 500A/50mV shunt, Bluetooth built-in | Shunt-only, Bluetooth (app is the display); 300A–500A classes sold | Shunt + small LED display head |
| Readout | Wall display + VictronConnect app | VictronConnect app only | On-device display only |
| Mid-charge status | At a glance | Phone in hand | At a glance |
| Temp sensor | Optional accessory (BMV-712) | Not applicable/sold separately per listing — verify | Typically no |
| Extras | Relay for generator start-stop (per product documentation) | Same app ecosystem as Victron controllers | None |
| Warranty | 5-year standard (per victronenergy.com) | 5-year standard (per victronenergy.com) | Varies — check before buying |
| Typical street | Premium display class (~$150–$190 street, editorial band) | ~$100–$120 genuine street (authorized dealers; beware far-cheaper counterfeits — a documented marketplace problem) | ~$25–$40 (editorial band) |

*BMV-712 shunt rating, Bluetooth, optional temperature sensor, and 5-year warranty per victronenergy.com product page, retrieved 2026-09-06; the overview page does not list supply range, draw, or accuracy — verify in the datasheet if those matter to your build. SmartShunt pricing per authorized-dealer listings retrieved 2026-09-06.*

**Choosing in one line:** if you check charge status from the couch, get the SmartShunt class (app); if the system lives in a cabin you walk past, the display BMV-712 class; if it's a shed battery and close-enough is fine, the budget class — with eyes open that a ±5% drift between syncs is normal at that tier (editorial judgment from the spec class, not a test claim).

## The install rule that decides your accuracy

**The shunt is the only thing connected to battery negative.** Every load and every charge source lands on the shunt's other side (the "load side" busbar). Wire anything directly to the battery minus post — a fuse block, an inverter case ground, a fridge — and the monitor never sees it, and your SOC quietly becomes fiction.

The rest of the install arithmetic:

- **Cable size to the monitor** is trivial (milliamp draw), but the **main negative cable now routes through the shunt** — size that cable for the full bank current per our [battery cable guide](/pages/battery-cable-size-for-inverter.html), and fuse the positive side per [fuse sizing](/pages/solar-fuse-and-breaker-sizing.html).
- **Placement:** shunt close to the battery (clean, dry, away from the inverter's heat); display or phone range as you like — the electronics don't care.
- **Settings you must enter:** bank capacity (Ah), battery chemistry, charge efficiency (LiFePO4 ≈ 99%; flooded lead-acid ≈ 85–90% typical), and the charged/sync parameters (absorption voltage + tail current). Defaults are sane; wrong capacity entries are the #1 accuracy killer.

## Worked example: what the numbers buy you

A 200Ah LiFePO4 bank (2 × 100Ah in parallel — the [bank-building math](/pages/litime-100ah-review.html) scales), average overnight draw 5A from dusk to midnight and 3A after: 6h × 5A + 6h × 3A = 48Ah out. Morning SOC reads **76%** (152Ah remaining) — not "13.0V, could be anything." At the 8am solar ramp delivering 25A net, the monitor's time-to-go says the bank returns to full in roughly **1.9 hours** — you learn the recharge finished at 10am instead of guessing at noon. Multiply that visibility across every day of the system's life and the monitor pays for itself in avoided guesswork and gentler [depth-of-discharge management](/pages/solar-battery-maintenance-guide.html) — the single biggest lifespan lever.

## Frequently Asked Questions

{{< faq "Can I just use a voltmeter to check my battery?" >}}
You can read voltage, but on a live system it isn't state of charge — load and charge move it constantly, and LiFePO4's flat curve hides most of the usable range between roughly 13.0V and 13.2V. A multimeter (like the one in our troubleshooting guides) is for diagnostics; a shunt is for state of charge.
{{< /faq >}}

{{< faq "What's the difference between the BMV-712 and the SmartShunt?" >}}
Functionally the same measurement: shunt + counting + Bluetooth app. The BMV-712 adds a physical display head (and optional temperature sensor); the SmartShunt is app-only and costs less. Choose by where you read your numbers — wall or phone (per manufacturer product pages, retrieved 2026-09-06).
{{< /faq >}}

{{< faq "Do I need a monitor if my battery has Bluetooth built in?" >}}
Some lithium batteries report their own BMS data over Bluetooth, and for simple single-battery systems that can be enough. A shunt still wins for multi-battery banks (it measures the whole bank as one), for systems with mixed charge sources, and for the time-to-go math a BMS app may not do.
{{< /faq >}}

{{< faq "Why does my monitor's state of charge drift over time?" >}}
Coulomb counting accumulates small errors and only truly resets at a confirmed full charge (absorption voltage with tail current). If your system never quite reaches full, the drift grows. The fix is usage, not hardware: let the bank reach full occasionally, and set the sync parameters to your charger's real absorption behavior.
{{< /faq >}}

{{< faq "Are cheap shunt meters any good?" >}}
For shed-class systems, yes, with expectations set: same working principle, roughly ±5% between syncs, no app ecosystem, and fit/finish to the price. The accuracy ladder is: budget shunt > voltage guessing, and Victron-class > budget — the same ladder our [brand-comparison approach](/pages/lifepo4-100ah-brand-comparison.html) applies to batteries.
{{< /faq >}}

{{< faq-schema >}}

## Next logical reads

<a href="/pages/solar-battery-management-system-explained.html" class="text-link">Battery management systems explained</a> <a href="/pages/battery-capacity.html" class="text-link">Battery capacity explained</a> <a href="/pages/solar-battery-maintenance-guide.html" class="text-link">Battery maintenance guide</a> <a href="/pages/battery-cable-size-for-inverter.html" class="text-link">Battery cable sizing</a> <a href="/pages/litime-100ah-review.html" class="text-link">LiTime 100Ah review (bank-building math)</a>

{{< product-box asin="B0DJ2P2XN5" name="Victron Energy SmartShunt Bluetooth Battery Monitor" label="The app-first counter" description="Shunt-based coulomb counting with Bluetooth as the display — the same measurement as the BMV line without the wall head (per manufacturer product pages, retrieved 2026-09-06). Not for: builds that need SOC readable without a phone (the BMV-712 class) or shed systems where a budget shunt is honest enough. The honest tradeoff: buy from authorized dealers — genuine street runs ~$100–$120, and far-cheaper listings are a documented counterfeit risk." button="Check price on Amazon" >}}
