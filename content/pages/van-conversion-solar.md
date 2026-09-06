+++
title = "Solar Power for a Van Conversion: Sizing the Electrical System Before You Drill Anything"
slug = "van-conversion-solar"
date = 2026-09-06
draft = false
description = "Van conversion solar sizing: the honest load list (incl. real Starlink draw), roof-watts reality, battery choice with winter in mind, alternator charging, and the build order."
image = "/images/van-conversion-solar/hero.webp"
image_alt = "White cargo van with a roof rack parked at a campsite — the roof real estate a van solar build has to work with"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
related = [
  "/pages/rv-solar-sizing.html",
  "/pages/how-to-calculate-solar-load.html",
  "/pages/12v-vs-24v-vs-48v-solar.html"
]
+++

{{< affiliate-disclosure >}}

## Quick answer

A van electrical system is three budgets that have to balance: **your daily watt-hours (the load list), your roof's watts (typically 200–400W of panel on a standard van), and your charging sources (solar + alternator + shore)**. Size in that order — most van-build mistakes are buying hardware before finishing the load list. The two decisions that shape everything: **12V-first design** (skip the inverter losses where you can) and **whether your battery needs to charge through freezing nights** (vans get cold inside; that decides heated vs base-model lithium). This page runs a real worked example — including what Starlink actually costs you in watts — with nothing tested by us, just spec math you can re-run with your own numbers.

## Step 1: the honest load list (with Starlink measured, not guessed)

Internet is the load that quietly sizes modern van builds, so use real numbers (Starlink's official specs: Mini averages 20–40W, Standard 75–100W, idle ~15–20W; retrieved 2026-09-06):

| Load | Typical draw | Hours/day | Wh/day |
| :-- | :-- | :-- | :-- |
| 12V compressor fridge | 40–60W avg (cycling) | 24 | 500–800 |
| Roof vent fan (variable) | 15–50W | 8 | 120–300 |
| LED lighting | 10–25W | 5 | 50–125 |
| Water pump (12V diaphragm) | 50–80W (intermittent) | 0.5 | 25–40 |
| Laptop + phone charging | 60–100W | 4 | 240–400 |
| **Starlink Mini** | 20–40W (25W typical real-world) | 6 | **150–240** |
| *Starlink Standard instead* | *75–100W* | *6* | *450–600* |
| Induction/heat* (if 120V life) | 1,200–1,800W | 0.3 | 360–540 |
| **Realistic 12V-first total** | | | **~1,100–1,900Wh/day** |

*Cooking on electricity changes everything: add ~400–600Wh/day and force an inverter into the build. Most considered builds keep a propane/ diesel route for heat and cooking — the [load calculation guide](/pages/how-to-calculate-solar-load.html) has the full worksheet.

**The Starlink decision alone is worth ~300–450Wh/day** (Mini vs Standard, per official specs and owner-measured reports — real-world Mini runs ~20–25W after connection). That's the difference between one 100Ah battery being enough and needing two.

## Step 2: what the roof can actually make

A standard high-roof van fits roughly **200–400W** of panels (2–4 × 100W-class, or ~2 × 175–200W) depending on rack, vent, and AC clearance. What that yields:

- **Good conditions** (sunny, panel flat on roof): ~4–5 sun hours × 300W × ~0.8 system efficiency ≈ **1,000–1,200Wh/day**.
- **Winter or parked-in-forest conditions:** half that or worse — see [peak sun hours](/pages/peak-sun-hours-by-state.html) and be honest about shade; a flat roof panel in December makes a fraction of its summer figure.
- Flat mounting (the van default) loses tilt angle — panels nailed flat sacrifice ~10–15% annually vs tilted, more in winter. Adjustable mounts recover some of it when you're parked.

Compare to the load list: a 1,100–1,900Wh/day build on 1,000–1,200Wh/day of solar **does not close on sunshine alone**. That's not failure — that's what the alternator is for.

## Step 3: the battery (with winter in mind)

Vans are unheated metal boxes overnight — exactly the [cold-charging problem](/pages/lifepo4-charging-below-freezing.html). If you'll camp below freezing and charge from solar mornings:

- **Base 100Ah LiFePO4** (like the one in our [LiTime review](/pages/litime-100ah-review.html)): fine if your charging happens while driving (alternator warmth + cabin heat) or you accept cutoff behavior in cold snaps.
- **Self-heating 100Ah** (LiTime Group 24 self-heating, Redodo self-heating — the [cold-charging guide](/pages/lifepo4-charging-below-freezing.html) has the verified warm-up math): the right call if the van sits outside in winter and relies on solar.
- **Capacity math:** 2 × 100Ah = 2,560Wh at 12.8V nominal; at 80% usable × 90% wire efficiency ≈ **~1,880Wh practical** — one full day of the heavy load list, two of the light one.

Bank voltage: 12V is the van default (every appliance exists in 12V; see [12V vs 24V vs 48V](/pages/12v-vs-24v-vs-48v-solar.html) for when it isn't).

## Step 4: the alternator is a charging source (use it deliberately)

Driving is your most reliable winter charger. A **DC-DC charger** (not a plain isolator — modern vans have smart alternators that isolators can't track) charges the house battery from the alternator at a controlled rate:

- The current reference unit: **Victron Orion XS 12/12V 50A (700W)** — smart-alternator compatible, lithium profiles, Bluetooth configuration, IP65 (per manufacturer documentation and manual, retrieved 2026-09-06). 50A × ~14V ≈ 700W of charging while driving; a 2-hour drive puts ~1.4kWh into the bank.
- Check your alternator's spare capacity before maxing the charger (50A is fine on most vans; verify against your vehicle's specs).
- Shore charging and a small inverter-generator remain the third and fourth options — the [battery vs generator tradeoffs](/pages/solar-battery-backup-vs-generator.html) apply at van scale.

## Step 5: controller, fusing, wiring (the parts that keep it alive)

- **Controller sizing:** array watts ÷ battery volts × 1.25 ≤ controller amps (the [charge controller sizing](/pages/charge-controller-sizing.html) page works it in full). 400W on 12V → ~39A → a 40A MPPT (our [controller guide](/pages/best-mppt-charge-controllers.html) covers the honest picks; MPPT-vs-PWM threshold math is [here](/pages/mppt-vs-pwm.html)).
- **Every segment fused:** panel-to-controller, controller-to-battery, battery-to-distribution, alternator line — the [fuse and breaker sizing](/pages/solar-fuse-and-breaker-sizing.html) page is the worksheet. In a metal box on moving wheels, this is the page you don't skip.
- **Wire for the inverter run:** if you do add 120V, the [inverter cable chart](/pages/inverter-cable-size-chart.html) and [battery cable sizing](/pages/battery-cable-size-for-inverter.html) prevent the classic van fire-starter.
- **Monitor:** a shunt-based battery monitor is the difference between managing and guessing — the math is in the [BMS/monitoring guide](/pages/solar-battery-management-system-explained.html).

## The worked build (one honest example)

Load list lands at **1,400Wh/day** (fridge + fan + lights + laptop + Starlink Mini at 6h). Roof takes **300W flat**. Solar delivers ~1,000–1,100Wh/day in decent weather — the gap closes with **one 2-hour drive per few days** through a 50A DC-DC charger. Bank: **2 × 100Ah LiFePO4** (self-heating if winter-bound). Controller: **40A MPPT**. Total: a system that runs indefinitely with movement, indefinitely in summer sun, and honestly needs a shore/generator top-up in a parked winter week. That's the real answer no component catalog gives you — the arithmetic does.

## Build order (so you don't buy twice)

1. Load list (worksheet in the [calculation guide](/pages/how-to-calculate-solar-load.html))
2. Battery capacity + chemistry-with-winter decision
3. Charging sources: roof watts → controller; alternator → DC-DC
4. Distribution: fusing, busbar, monitor
5. Inverter last, only if the load list demands 120V

## Frequently Asked Questions

{{< faq "How much solar do I need for a van conversion?" >}}
Start from the load list, not the roof: most 12V-first builds land at 1,100–1,900Wh/day, which 200–400W of roof panel covers in good weather but not in winter or shade. Size the battery for a full day, solar for the average day, and let alternator charging cover the gaps — the worked example above shows the balance.
{{< /faq >}}

{{< faq "Can I run Starlink on van solar?" >}}
Yes, and the dish choice matters: Starlink's official specs put the Mini at 20–40W average (owners typically see ~20–25W connected) versus 75–100W for the Standard — roughly a 300–450Wh/day difference at 6 hours of use. The Mini is nearly universal in van builds purely on power economics; the Standard needs double the battery or half the runtime.
{{< /faq >}}

{{< faq "Do I need a DC-DC charger or is a battery isolator enough?" >}}
A DC-DC charger, on any van with a smart alternator (most built in the last decade): it regulates charge current for lithium profiles and works with the alternator's variable output; a plain isolator does neither. The Victron Orion XS 50A class is the common reference (per manufacturer documentation, retrieved 2026-09-06).
{{< /faq >}}

{{< faq "Should my van system be 12V or 24V?" >}}
12V for almost every van build: every major appliance (fridges, fans, pumps, Starlink via DC) exists natively in 12V, which avoids inverter losses. 24V starts making sense for big inverter loads or long cable runs — the threshold math is in our voltage comparison guide.
{{< /faq >}}

{{< faq "Will my lithium battery be OK in the van over winter?" >}}
Discharging is fine to about −4°F; the rule is charging — LiFePO4 must not charge below 32°F. If your van charges from solar on cold mornings, use a self-heating model or keep charging to drive times; the full chemistry and heater math is in our cold-charging guide.
{{< /faq >}}

{{< faq-schema >}}

## Next logical reads

<a href="/pages/rv-solar-sizing.html" class="text-link">RV solar sizing (the sibling system)</a> <a href="/pages/how-to-calculate-solar-load.html" class="text-link">How to calculate your solar load</a> <a href="/pages/12v-vs-24v-vs-48v-solar.html" class="text-link">12V vs 24V vs 48V</a> <a href="/pages/lifepo4-charging-below-freezing.html" class="text-link">LiFePO4 in freezing weather</a> <a href="/pages/solar-fuse-and-breaker-sizing.html" class="text-link">Fuse and breaker sizing</a>

{{< product-box asin="B0CWYWQGBF" name="Victron Energy Orion XS Smart DC-DC Charger 12/12V 50A 700W" label="The alternator-charging standard" description="Charges the house bank from the van's alternator at a controlled 50A (700W) — smart-alternator compatible, lithium profiles, Bluetooth configuration, IP65 (per manufacturer documentation, retrieved 2026-09-06). Not for: vehicles without spare alternator capacity for 50A — verify your van's numbers and consider the smaller Orion if marginal. The honest tradeoff: it's the priciest part of the charging trio, and also the one that makes winter and forest camping work — solar alone doesn't close a 1,400Wh/day gap." button="Check price on Amazon" >}}
