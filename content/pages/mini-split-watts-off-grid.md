+++
title = "How Many Watts Does a Mini Split Use Off Grid? (Battery Math)"
slug = "mini-split-watts-off-grid"
date = 2026-09-05
draft = false
description = "Mini split watts off grid: measure real running watts, then size the battery bank and solar array with honest math for 9,000-12,000 BTU inverter units."
author = "Solar Powered Project"
related = [
  "/pages/solar-inverter-sizing.html",
  "/pages/12v-vs-24v-vs-48v-solar.html",
  "/pages/solar-system-sizing.html",
  "/pages/battery-capacity.html",
  "/pages/solar-panel-output.html"
]
+++

{{< affiliate-disclosure >}}

## Quick answer

Off grid, a 9,000–12,000 BTU inverter mini split typically draws **about 200–600W at mild load, up to roughly 1,000–1,500W at full output on a hot day** — a 12,000 BTU (1-ton) unit in the SEER 17–22 class averages **about 400–700W** in cooling. That's roughly **4kWh for an 8-hour cooling night**, needing about **4,700Wh of usable battery (~100Ah at 48V or ~400Ah at 12V)** and **about 1,000–1,300W of panels** to refill it on a typical sunny day. Bottom line: a mini split is a big off-grid load — realistic for a large DIY battery bank, not for a small portable power station.

## Key takeaways

- **Inverter mini splits modulate:** ~200–600W at mild load, ~1,000–1,500W only at full output on a hot day.
- **Startup surge is modest (~2× running)** — nothing like the 3–5× spike of old single-speed compressors.
- **A 12,000 BTU unit at SEER 17–22 averages ~400–700W in cooling** — about 3–5.6kWh for an 8-hour night.
- **Measure first:** a 24-hour plug-in wattmeter beats nameplate math; the NEEP cold-climate heat pump list covers published heating watts.
- **Battery: ~4kWh/night ÷ 0.85 usable ≈ 4,700Wh** (~100Ah@48V or ~400Ah@12V) before adding autonomy days. Why 48V: [our explainer](/pages/12v-vs-24v-vs-48v-solar.html).
- **Refill: ~1,000–1,300W of panels** at 4 sun hours with a 0.75 derate — a real array, not a couple of portable panels.
- **Honest verdict:** mini splits suit large DIY banks or generator-fed systems; small portable stations and smaller loads (fans, DC evaporative) are the realistic alternatives.

## Section 1: Measure YOUR draw — meter first

The nameplate figure is the *maximum* rated input at full output — not your typical draw. Inverter mini splits run at partial capacity most of the time, so the average sits far below the maximum.

**Step 1: plug in a wattmeter** (Kill A Watt style) between the wall and a 120V mini split for a full 24 hours, including a warm afternoon and your usual set-point. You get: **running watts** at your set-point, **max watts** on the hot day, and **total kWh over 24h** (divide by run hours for your average draw).

**Step 2 (heating): NEEP cold-climate listings.** For heating, published rated watts at low outdoor temperatures beat guesses. NEEP's Cold Climate Air Source Heat Pumps product list ([ashp.neep.org](https://ashp.neep.org)) lists models with rated input watts at low-temperature conditions — use those at your design outdoor temperature, not cooling watts. The database moved to AHRI reporting in 2025; re-verify before you buy.

| Load condition (9,000–12,000 BTU inverter unit) | Typical draw | What it means |
| --- | --- | --- |
| Running, mild load (set-point mostly met) | ~200–600W | Modulating compressor at partial capacity — most of its runtime |
| Full output, hot day | ~1,000–1,500W | Unit pinned at max cooling |
| Average in cooling, SEER 17–22 (12k BTU / 1 ton) | ~400–700W | The number to use for nightly energy math |
| Startup surge | ~2× running | Inverter ramp, not the 3–5× of old compressors |

## Section 2: Energy budget — 8 hours × 500W ≈ 4kWh

The working case: **0.5kW average × 8h = 4kWh per night**. That's "worst-case-ish" — 500W sits mid-range of a SEER 17–22 unit's 400–700W. A mild night lands closer to 3kWh; a long, hot one can run 5kWh+.

| Scenario (12k BTU cooling) | Average draw | Hours | Nightly energy |
| --- | --- | --- | --- |
| Mild night | ~400W | 8 | ~3.2kWh |
| Hot night (our working case) | ~500W | 8 | **~4.0kWh** |
| Worst-ish continuous | ~700W | 8 | ~5.6kWh |

**Heating changes the budget.** A heat pump at low outdoor temperatures draws more power and delivers less capacity per watt — the SEER averages above are cooling numbers. Budget heating from the unit's published low-temperature input watts (NEEP listing or manufacturer spec) for the coldest night you expect. A common rule of thumb is 1.2–1.5× the cooling budget, but verify with your model's rated watts.

## Section 3: Battery sizing — 4kWh ÷ 0.85 ≈ 4,700Wh usable

Batteries are rated in total (nominal) watt-hours, but you can only use a fraction. For LiFePO4, usable depth-of-discharge is ~80–90%; we use **0.85** — the same factor the site's fridge article uses, so all math stays consistent.

**Worked example:**
- Daily need: 4,000Wh (8h × 500W)
- ÷ 0.85 usable = ~4,706Wh ≈ **4,700Wh usable**
- At 48V: 4,700 ÷ 48 ≈ **98Ah → 100Ah@48V**
- At 12V: 4,700 ÷ 12 ≈ **392Ah → 400Ah@12V**

<table>
<thead>
<tr class="header">
<th>Nightly energy</th>
<th>÷ 0.85 usable =</th>
<th>≈ @48V</th>
<th>≈ @12V</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3.2 kWh (mild)</td>
<td>~3,765 Wh</td>
<td>~80Ah</td>
<td>~315Ah</td>
</tr>
<tr class="even">
<td>4.0 kWh (our case)</td>
<td>~4,700 Wh</td>
<td><strong>~100Ah</strong></td>
<td><strong>~400Ah</strong></td>
</tr>
<tr class="odd">
<td>5.6 kWh (worst-ish)</td>
<td>~6,590 Wh</td>
<td>~138Ah</td>
<td>~550Ah</td>
</tr>
</tbody>
</table>

That's one night for one mini split before any other loads — no fridge, lights, or pump. Add **autonomy days**: 2 days × ~4,700Wh = ~9,400Wh usable (~200Ah@48V). The site's [battery capacity calculator](/pages/battery-capacity.html) does this for you.

**Why 48V and not 12V?** A 4,700Wh battery at 12V means ~390A at full draw — wiring, fuses, and inverter connections get heavy and lossy. At 48V currents drop 4×, which is why large banks practically need 48V. Full trade-off: [12V vs 24V vs 48V](/pages/12v-vs-24v-vs-48v-solar.html); inverter and battery-draw sizing: [solar inverter sizing](/pages/solar-inverter-sizing.html).

## Section 4: Solar array to refill — 4kWh/day ≈ 1,000–1,300W of panels

The panels must put the 4kWh back on a good solar day:

**Panel watts ≈ daily Wh ÷ (sun hours × 0.75)**

Worked:
- 4,000 ÷ (4 × 0.75) = 4,000 ÷ 3 ≈ **1,333W** → ~1,300W
- At 5 sun hours: 4,000 ÷ (5 × 0.75) ≈ ~1,067W → ~1,100W
- At 3 sun hours: 4,000 ÷ (3 × 0.75) ≈ **~1,780W**

So the honest planning range at typical US locations (3–5 good sun hours) is **~1,000–1,300W of panels for a 4kWh/night cooling budget** — push toward the higher end in summer, when nights are cooling-heavy and usable sun shrinks. The 0.75 derate covers panel angle, temperature, controller losses, and cloudy gaps — full method in [solar panel output](/pages/solar-panel-output.html).

| Sun hours | Panel watts for 4kWh/day (0.75 derate) | Notes |
| --- | --- | --- |
| 5 | ~1,100W | Sunny Southwest locations |
| 4 | ~1,300W | Typical US planning day |
| 3 | ~1,780W | Shaded/northern summers |

**Cloudy-day honesty:** an overcast day can deliver 10–20% of rated output (see [solar system sizing](/pages/solar-system-sizing.html)). The battery is the buffer — size for the worst stretch, treat solar as the recharge.

## Section 5: Honest verdict — big load, big bank

A mini split is comfortable, quiet, and *efficient* — but one of the biggest single loads you can put off grid. A modern fridge runs on ~1.4kWh/day; a mini split cooling night runs ~4kWh — nearly 3× the energy, before heating season.

- **Works well:** large DIY battery banks (10kWh+), cabins with real arrays (1.5kW+), whole-house systems sized with the [solar system sizing](/pages/solar-system-sizing.html) planner.
- **Struggles:** a "solar generator" with 1–2kWh of battery runs a mini split for a couple of hours at mild load before draining — not a nightly solution. A 100W panel can't refill what the unit uses; you'd need ~10× that.
- **Alternatives for small systems:** 12V DC fans, DC evaporative coolers in dry climates (point-cooling, not whole-room), and spot-cooling an occupied chair or bed — all happy on modest batteries and small panels.

## Common mistakes

1. **Sizing from the nameplate maximum.** A 12,000 BTU unit labeled ~1,100–1,500W max doesn't run at that all night — it modulates. Nameplate math over-sizes the system 2–3×.
2. **Mixing average and max.** The 400–700W average sets battery kWh; the 1,000–1,500W max sets inverter continuous rating. Confusing the two doubles battery cost or trips the inverter.
3. **Treating surge like an old fridge.** Inverter mini splits start at ~2× running — no 5× surge buffer needed, but check the ramp in [solar inverter sizing](/pages/solar-inverter-sizing.html).
4. **Spending the whole battery budget on cooling.** The fridge, lights, and water pump still eat kWh/day — subtract them first.
5. **Assuming heating obeys the cooling average.** Low outdoor temps mean higher draw and lower capacity; plan from published low-temperature watts, not the SEER cooling figure.
6. **Skipping the meter.** Spec tables are averages across models, seasons, and set-points; 24 hours of your actual unit at your actual set-point beats them all.

## FAQ

{{< faq "How many watts does a 12,000 BTU mini split use?" >}}
Running at mild load, a 12,000 BTU inverter unit typically draws about 200–600W, averaging roughly 400–700W in cooling (SEER 17–22), and up to about 1,000–1,500W at full output on a hot day. Startup surge is modest — around 2× running — because inverter compressors ramp up rather than slam on.
{{< /faq >}}

{{< faq "What size battery do I need for a mini split off grid?" >}}
For an 8-hour cooling night at ~500W average (about 4kWh), you need 4,000 ÷ 0.85 usable ≈ 4,700Wh — roughly a 100Ah battery at 48V or a 400Ah battery at 12V, for one night. Add autonomy days (2 nights ≈ 9,400Wh) and all your other loads before buying.
{{< /faq >}}

{{< faq "Can a 2,000W solar generator run a mini split?" >}}
Partially. It can start and briefly run a 9,000–12,000 BTU unit (inverter surge ~2× is fine), but a 2,000Wh battery at 85% usable only holds ~1,700Wh — under half of a 4kWh cooling night. It's an emergency-cooling buffer, not an off-grid nightly solution.
{{< /faq >}}

{{< faq "How much solar do I need to run a mini split?" >}}
Plan roughly 1,000–1,300W of panels for a 4kWh/day cooling budget at 4 sun hours (4,000 ÷ (4 × 0.75) ≈ 1,330W). Fewer sun hours or heating-season nights push that higher; use the site's [solar panel output](/pages/solar-panel-output.html) method for your location.
{{< /faq >}}

{{< faq "Do inverter mini splits have a big startup surge problem off grid?" >}}
No — that's the good news. Inverter compressors ramp, so startup surge is about 2× running rather than the 3–5× of old single-speed compressors. You still size the inverter for peak draw (see [solar inverter sizing](/pages/solar-inverter-sizing.html)), but you don't need a huge surge buffer on top.
{{< /faq >}}

## Next logical reads

- <a href="/pages/solar-inverter-sizing.html" class="text-link">How to Size an Inverter for Solar (Watts, Surge, Battery Draw)</a>
- <a href="/pages/12v-vs-24v-vs-48v-solar.html" class="text-link">12V vs 24V vs 48V Solar Systems: Key Differences</a>
- <a href="/pages/battery-capacity.html" class="text-link">Battery Capacity Calculator for Solar Systems</a>
- <a href="/pages/solar-system-sizing.html" class="text-link">How to Size a Solar System (Step-by-Step Load Planner)</a>
- <a href="/pages/solar-panel-output.html" class="text-link">Solar Panel Output Calculator (Watts to Watt-hours)</a>