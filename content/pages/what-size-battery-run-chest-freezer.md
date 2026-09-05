+++
title = "What Size Battery to Run a Chest Freezer? (Sizing Math)"
slug = "what-size-battery-run-chest-freezer"
date = 2026-09-05
draft = false
description = "What size battery runs a chest freezer? Modern units need 0.7–1.1 kWh/day — see the sizing math, worked examples, and how to measure your freezer's draw."
author = "Solar Powered Project"
related = [
  "/pages/what-size-solar-generator-run-refrigerator.html",
  "/pages/how-long-will-100ah-battery-run.html",
  "/pages/battery-capacity.html",
  "/pages/solar-generator.html"
]
+++

{{< affiliate-disclosure >}}

## Quick answer

A modern ENERGY STAR chest freezer (14–20 cu ft) draws roughly **0.7–1.1 kWh per day**, so a **100Ah 12V LiFePO4 battery (~1,280Wh)** runs one for about a day — and a 200Ah-class battery covers two days. Older or manual-defrost units can pull 1.5–2.5 kWh/day, roughly doubling those numbers. The honest method: measure your freezer with a plug-in power meter for 24 hours, then run the formula below — don't buy from an average.

## Key takeaways

- **Modern ENERGY STAR chest freezers (14–20 cu ft) use ~250–400 kWh/year = 0.7–1.1 kWh/day.** Older or manual-defrost units can hit 1.5–2.5 kWh/day.
- **Compressor running draw is ~100–250W**, but it cycles — daily watt-hours, not watts, sizes the battery.
- **Startup surge is typically 2–4× running draw for a few seconds** — the inverter's surge rating makes or breaks the start.
- **Formula: battery Wh = daily Wh × autonomy days ÷ usable DoD, plus ~10% inverter losses.** LiFePO4: 80–90% usable; lead-acid: ~50%.
- **Baseline:** a 15 cu ft ENERGY STAR freezer at 0.9 kWh/day needs ≈1,165Wh → 100Ah@12V LiFePO4 for one day, 200Ah class for two.
- **Measure yours first** — a $20–30 plug-in power meter (Kill A Watt class) over 24 hours beats every table here.
- **A 300W panel in ~4 sun hours replaces ≈900Wh/day** — enough for the 1-day case in decent weather.

## The three numbers that matter

1. **Daily watt-hours (Wh/day)** — total energy consumed over 24 hours. This sizes the battery.
2. **Running watts** — what the compressor draws while on, typically **100–250W** for chest freezers.
3. **Surge watts** — the brief start spike, typically **2–4× running draw for a few seconds**. This sizes the inverter, not the battery.

The trap is the nameplate. A freezer labeled "115V, 1.5A" implies 172W — but the compressor cycles on and off to hold temperature, so the model is *not* watts × 24 hours. It's:

**Daily Wh = running watts × duty cycle × 24h**

A 120W compressor running 30% of the time uses 120 × 0.30 × 24 = **864 Wh/day** — not 2,880 Wh/day as naive nameplate math suggests.

| Freezer | Typical running draw | Typical daily energy |
|---|---|---|
| Modern ENERGY STAR, 14–20 cu ft | ~100–250W | 0.7–1.1 kWh/day (250–400 kWh/yr) |
| Older / manual-defrost unit | ~150–250W | 1.5–2.5 kWh/day |
| Small 5–7 cu ft unit | ~80–150W | ~0.5–0.9 kWh/day |

These are planning ranges, not guarantees — a freezer in a hot garage works harder than one in a 68°F basement. That's why you measure yours.

## Step 1: Measure your freezer before you size anything

Measuring costs about $20–30 and one day of patience. **Get a plug-in power meter** (Kill A Watt class — anything that reads watts and cumulative kWh), plug the freezer into it, and leave it for a **full 24 hours**, ideally a warm day since duty cycle climbs with ambient temperature.

You get two numbers:

- **Cumulative kWh over 24h** — your daily Wh, already including duty cycle, door openings, and ambient temperature. This single number feeds the sizing formula.
- **Instantaneous watts** — watch it when the compressor kicks on; note the running draw and the brief start spike.

Measure in the freezer's real location (a garage freezer in July runs a very different cycle than the same unit in a basement in January), and treat a 24-hour reading as a sample, not a law — if it lands far from the ranges above, run a second day.

No meter? Use the EnergyGuide label's kWh/year ÷ 365 as a fallback. It's a yearly average that already includes cycling, but it may understate a hot-weather or heavy-use day — a floor, not a ceiling.

## The sizing formula

**Battery Wh needed = (daily Wh × days of autonomy ÷ usable DoD) × 1.1**

- **Days of autonomy** — how many days the battery runs the freezer with no recharge. One day covers overnight gaps; two to three is realistic for a storm outage.
- **Usable DoD** — how much of rated capacity you can use without shortening battery life. **LiFePO4: 80–90%. Lead-acid: ~50%** — discharging lead-acid deeper repeatedly kills it early. For the chemistry trade-offs, see our <a href="/pages/li-ion-vs-lead-acid.html" class="text-link">Li-ion vs lead-acid comparison</a>.
- **× 1.1 for inverter losses** — converting 12V DC to 120V AC wastes roughly 10% of stored energy. Skip this term and you'll land ~10% short.

To sanity-check capacity and DoD from a battery you already own, see our <a href="/pages/battery-capacity.html" class="text-link">battery capacity calculator guide</a>.

## Worked examples: from daily Wh to a battery you can buy

**Baseline: 15 cu ft ENERGY STAR freezer, measured 0.9 kWh/day (900 Wh/day), LiFePO4, one day of autonomy.**

- Battery Wh = 900 ÷ 0.85 × 1.1 = **≈1,165 Wh**
- A 100Ah 12V LiFePO4 battery stores 100 × 12.8 = **1,280Wh** — clears 1,165Wh with margin. **Verdict: 100Ah@12V LiFePO4 class covers one day.**

**Same freezer, two days of autonomy:**

- Battery Wh = 900 × 2 ÷ 0.85 × 1.1 = **≈2,330 Wh**
- A 200Ah 12V LiFePO4 battery stores 2,560Wh — clears 2,330Wh. **Verdict: 200Ah class covers two days.**

**Same freezer on lead-acid, one day:**

- Battery Wh = 900 ÷ 0.50 × 1.1 = **≈1,980 Wh** — at 12V that's ≈165Ah, so call it a 200Ah@12V lead-acid bank for margin. Lead-acid needs roughly **double the rated capacity** of LiFePO4 for the same job.

**Worst case: older manual-defrost unit at 2.0 kWh/day, LiFePO4, two days:**

- Battery Wh = 2,000 × 2 ÷ 0.85 × 1.1 = **≈5,180 Wh** — a 400Ah@12V bank (5,120Wh) sits right at the line, so add solar recharge or step up to 500Ah for margin.

| Scenario | Daily Wh | Autonomy | Chemistry | Battery Wh needed | Real-world class |
|---|---|---|---|---|---|
| 15 cu ft ENERGY STAR | 900 | 1 day | LiFePO4 (85% DoD) | ≈1,165 Wh | 100Ah@12V (1,280Wh) |
| 15 cu ft ENERGY STAR | 900 | 2 days | LiFePO4 (85% DoD) | ≈2,330 Wh | 200Ah@12V (2,560Wh) |
| 15 cu ft ENERGY STAR | 900 | 1 day | Lead-acid (50% DoD) | ≈1,980 Wh | ~200Ah@12V lead-acid |
| Older manual-defrost | 2,000 | 2 days | LiFePO4 (85% DoD) | ≈5,180 Wh | 400–500Ah@12V |

For the full runtime method, see our <a href="/pages/how-long-will-100ah-battery-run.html" class="text-link">100Ah battery runtime guide</a>.

## Freezer vs. fridge: why freezers are the easy case

If you've read our <a href="/pages/what-size-solar-generator-run-refrigerator.html" class="text-link">solar generator sizing guide for refrigerators</a>, freezers come out cheaper — and that's not a typo.

**Chest freezers cycle less than fridges.** A fridge gets opened several times a day, spilling cold air with every opening; a chest freezer is opened less often, and its lid-up design keeps the dense cold air from spilling the way it does out of an upright door. Net effect: lower duty cycle, lower daily Wh, smaller battery for the same job — in the model-page examples a modern fridge runs ~1,440 Wh/day versus our freezer's ~900 Wh/day. And a full chest freezer holds temperature a surprisingly long time unpowered with the lid closed, which is why sizing for 1–2 days of autonomy (not 7) is defensible for most people.

## Inverter sizing: surge is the real constraint

The battery stores energy; the inverter delivers power. For a freezer, **surge** matters more than continuous:

- **Continuous rating:** must exceed running draw — with 100–250W compressors, almost any inverter qualifies. Keep ≥1.5× headroom anyway for fans, defrost heaters, and voltage sag.
- **Surge rating:** must cover the start spike, typically **2–4× running draw for a few seconds**. A 150W compressor can pull 300–600W at start; a 250W unit can spike toward 1,000W. If the inverter can't deliver that brief spike, it shuts down — and the freezer never starts, no matter how big the battery is.

Use **pure sine output** — modified sine can make compressor motors hum, run hot, and fail early (see our <a href="/pages/pure-sine-vs-modified-sine-inverter.html" class="text-link">pure sine vs modified sine comparison</a>) — and **check how long the surge rating lasts**. A "2,000W peak" that lasts 20 milliseconds won't necessarily start a compressor that spikes for 2 seconds.

## Solar recharge math: keeping the battery full

A battery alone gives autonomy days; solar makes the system self-sustaining. The question: can your panels replace one day's draw in one day of sun?

**Panel watts needed ≈ daily Wh ÷ (sun hours × 0.75)**

The 0.75 derate covers orientation, heat, controller losses, and imperfect conditions. For the 900 Wh/day freezer with 4 peak sun hours:

| Array | 4 sun hours × 0.75 | vs. 900 Wh/day freezer |
|---|---|---|
| 200W | 600 Wh/day | ~67% of daily draw — battery slowly drains |
| 300W | 900 Wh/day | ≈100% — covers the 1-day case |
| 400W | 1,200 Wh/day | ~133% — margin for cloudy stretches |

**Cloudy-day honesty:** on a fully overcast day, fixed panels might deliver 10–25% of that figure. Solar is the recharge engine; the battery is the buffer. Size the battery for your worst realistic stretch of weather and treat sunny days as the recovery period. For the whole-system picture, see our <a href="/pages/solar-system-sizing.html" class="text-link">solar system sizing guide</a>.

## Battery vs. generator for a freezer

**A battery is silent, fume-free, and runs indoors — but it's finite**: when it's empty you need solar, a charger, or grid power to refill it. **A generator refuels indefinitely but demands fuel logistics and safe outdoor operation** — exhaust CO means it must run outside, away from windows. For a single freezer through a 1–2 day outage, a properly sized battery is usually the cleaner answer. For week-long outages the two pair well: battery for quiet overnight hours, generator for a midday recharge. Our <a href="/pages/solar-battery-backup-vs-generator.html" class="text-link">battery backup vs. generator comparison</a> and <a href="/pages/solar-generator.html" class="text-link">solar generator guide</a> cover both paths in depth.

## Common mistakes

- **Sizing from nameplate amps.** 115V × 1.5A = 172W, and 172W × 24h = 4,128 Wh/day — nearly 5× the real figure for an efficient unit. Use measured daily kWh.
- **Skipping the inverter-loss term.** 900 Wh of freezer draw takes ~1,000 Wh out of the battery once conversion losses are paid.
- **Buying lead-acid by LiFePO4 math.** A "100Ah battery" that's lead-acid delivers ~50Ah usable — half the runtime. Match the chemistry to the DoD in your formula.
- **Ignoring surge.** Days of battery capacity still fail if the inverter can't deliver 2–4× running watts for the compressor start.
- **Sizing for the average day, not the hot day.** A garage freezer in July can draw far more than its annual average. Measure in the worst season, or add margin.
- **Forgetting other loads.** Auto-defrost heaters and ice makers add intermittent draw, and anything else sharing the inverter adds its daily Wh too.

## FAQ

{{< faq "Will a 100Ah battery run a chest freezer?" >}}
A 100Ah 12V LiFePO4 battery (1,280Wh, ~1,090Wh usable after DoD and inverter losses) runs a modern ENERGY STAR freezer using 0.7–1.1 kWh/day for roughly one day. On lead-acid, 100Ah is only ~50Ah usable — about half a day. Measure your freezer's daily kWh first; the answer follows from it.
{{< /faq >}}

{{< faq "How long will a freezer stay cold without power?" >}}
A full chest freezer typically holds safe temperatures for a couple of days unpowered if the lid stays closed; a half-full one warms faster. That's why 1–2 days of battery autonomy is a sensible target. Keep the freezer full (or fill empty space with jugs of water) to maximize thermal mass.
{{< /faq >}}

{{< faq "What size inverter do I need for a chest freezer?" >}}
Continuous: at least 1.5× the compressor's running draw — with 100–250W compressors, a 300–500W continuous inverter covers it. Surge: enough for 2–4× running watts for a second or two — roughly 1,000W surge for smaller units, more for larger or older compressors. Pure sine output, and check how long the surge rating lasts.
{{< /faq >}}

{{< faq "Can a solar generator run a chest freezer?" >}}
Yes, if its battery clears the daily-Wh math and its inverter surge covers the compressor start. A ~1,000Wh-class station runs a 0.9 kWh/day freezer for about a day; a 2,000Wh-class unit covers two days. Verify ratings against your measured numbers — our <a href="/pages/what-size-solar-generator-run-refrigerator.html" class="text-link">refrigerator sizing guide</a> uses the same method.
{{< /faq >}}

{{< faq "How many solar panels to keep a chest freezer running indefinitely?" >}}
For the baseline 900 Wh/day freezer: a 300W panel in ~4 peak sun hours × 0.75 ≈ 900 Wh/day, which breaks even in decent weather. Add 30–50% margin (400–450W) for cloudy stretches, or size the battery for 2+ days of autonomy so overcast days draw it down and sunny days refill it.
{{< /faq >}}

## Next logical reads

- <a href="/pages/what-size-solar-generator-run-refrigerator.html" class="text-link">What size solar generator to run a refrigerator?</a> — the same three-number method applied to fridges.
- <a href="/pages/how-long-will-100ah-battery-run.html" class="text-link">How long will a 100Ah battery run?</a> — the full runtime formula, reusable for any load.
- <a href="/pages/battery-capacity.html" class="text-link">Battery capacity calculator for solar systems</a> — capacity and DoD from a battery you own.
- <a href="/pages/solar-generator.html" class="text-link">Solar generator guide</a> — how these stations work, and what spec-sheet numbers mean.
- <a href="/pages/solar-battery-backup-vs-generator.html" class="text-link">Solar battery backup vs. generator</a> — the full trade-off for outage coverage.