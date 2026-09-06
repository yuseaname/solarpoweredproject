+++
title = "Inverter Loading and Derating: Why You Shouldn't Run at 100%"
slug = "inverter-loading-derating-guide"
date = 2026-09-05
draft = false
description = "Inverter derating explained: the 80% loading rule, heat and altitude effects, surge headroom, and the worked math that sizes an inverter honestly."
image = "/images/inverter-loading-derating-guide/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
related = [
  "/pages/solar-inverter-sizing.html",
  "/pages/pure-sine-vs-modified-sine-inverter.html",
  "/pages/solar-inverter-cost.html"
]
+++

{{< affiliate-disclosure >}}

## Quick answer

Run an inverter at **80% or less of its continuous rating** — a 2,000W unit is honestly a 1,600W unit. Above that, three things bite: heat shortens component life, the surge headroom you need for motor starts disappears, and the wiring/fusing around the inverter (sized to its full rating) runs closer to its limits than your loads require. The exceptions are brief peaks — starting a fridge compressor for a second at 1,900W on a 2,000W inverter is what surge ratings are for; running a 1,900W load for an hour is not. The math and the exceptions are below.

**How to read this page:** this is an engineering-practice guide, not a test report — we have not bench-tested any inverter. The 80% rule and the derating factors below are standard practice drawn from how manufacturers rate their units (continuous vs surge) and how installers size systems; where a figure is an editorial planning rule rather than a code requirement, it is labeled as such. Our <a href="/pages/how-we-recommend.html" class="text-link">how we recommend</a> page covers the site's standards.

## Continuous, surge, and the number that lies

An inverter's spec sheet lists two wattages that get confused constantly:

-   **Continuous rating** — what the unit can sustain indefinitely at 25°C ambient. This is the number the box shouts.
-   **Surge/peak rating** (typically 2× continuous for seconds) — what it can deliver while a motor starts.

The rating that *lies* is continuous at what temperature: sustained output drops as the inverter heats up (see below), so the practical continuous number in a hot equipment bay is lower than the brochure. The honest sizing chain: **your simultaneous running load ≤ 80% of continuous; your worst motor start ≤ the surge rating.**

## The worked math: sizing with the 80% rule

**The load list.** A cabin runs: refrigerator 200W (running), LED lights 100W, laptop + phone 100W, and occasionally a microwave at 1,500W input — but the microwave runs alone (nothing else starts simultaneously by house rule).

-   **Simultaneous running load (no microwave):** 400W → any quality 600W+ inverter covers it at 80% (400 ÷ 0.8 = 500W minimum).
-   **With the microwave:** 1,900W → needs a 2,400W-class inverter at the 80% rule (1,900 ÷ 0.8 = 2,375W). A "2,000W" inverter technically fits 1,900W — and that's exactly the sustained-near-max trap this guide exists to prevent.
-   **Surge check:** the refrigerator's compressor start (~600–1,200W for a split second) on top of 300W of lights: ~1,500W — comfortably inside a 2,400W unit's ~4,800W surge rating.

Run your own list through the <a href="/pages/solar-inverter-sizing.html" class="text-link">inverter sizing calculator</a>, then apply the 80% rule to its answer.

## The three derating factors

**1. Heat.** Electronics derate as they warm — a unit that sustains 2,000W at 25°C sustains less at 45°C inside a closed cabinet in July. Editorial planning rule: **keep continuous loads at 80%** and give the inverter ventilation (its manual's clearances are real, not decorative). In hot-climate enclosed installs, be more conservative still.

**2. Altitude.** Thinner air cools worse; manufacturers commonly publish reduced continuous output above roughly 2,000 m / 6,500 ft (check your unit's manual for the specific derate — it varies by maker and is a per-manufacturer spec, not a universal number). Mountain installs should size with that reduced figure.

**3. Battery-side reality.** At 12V, a 2,000W load at 90% inverter efficiency draws ~185A — a current level where cable length, lugs, and fusing start mattering as much as the inverter (the full chart is our <a href="/pages/battery-cable-size-for-inverter.html" class="text-link">battery cable size guide</a>). This is a big part of why bigger loads push systems to 24V/48V: <a href="/pages/12v-vs-24v-vs-48v-solar.html" class="text-link">the voltage comparison</a> halves and quarters that current.

## What actually happens at sustained 100%

Nothing dramatic at first — that's the trap. The unit runs, maybe for months. But its cooling system runs flat-out, components live at their thermal limits, and the surge headroom that would have absorbed a compressor start is spent. Community failure reports pattern-match: inverters that "ran fine at max" die during the July week everything runs at once, or trip offline exactly when the well pump starts. You paid for surge capability; sustained max loading is how you never get to use it.

## Loading quick-reference

| Your simultaneous load | Buy an inverter rated (continuous) | Why |
| :-- | :-- | :-- |
| 400W | 500–600W+ | 80% rule with margin |
| 800W | 1,000–1,200W | plus motor-start headroom |
| 1,600W | 2,000–2,400W | the "2,000W inverter" trap zone — buy 2,400 |
| 2,400W+ | 3,000W+ (and consider 24/48V) | battery-side current becomes the story |

## Frequently Asked Questions

{{< faq "Is the 80% rule a code requirement?" >}}
No — it's an engineering planning rule (labeled as such above). Code governs the wiring and protection around the inverter; the 80% loading practice protects component life and keeps surge headroom available. Some manufacturers implicitly endorse it in their manuals' output-vs-temperature tables; check yours.
{{< /faq >}}

{{< faq "Can I exceed 80% for short periods?" >}}
Yes — that's what the continuous rating is for, briefly, and what surge ratings are for on motor starts. The damage pattern is sustained hours at 95–100%, not a 20-minute cooking session at 85%.
{{< /faq >}}

{{< faq "Does derating apply to power stations too?" >}}
Same physics, same advice: a station's continuous rating has the same thermal reality, and its surge rating (often lower than a standalone inverter's 2×) is the spec that kills cheap units on fridge starts. The capacity-tier table in our solar generator guide bakes this in.
{{< /faq >}}

{{< faq "How do I find my inverter's altitude derating?" >}}
The unit's manual — manufacturers publish output-vs-altitude figures differently (or not at all for small units). If your manual is silent and you're above ~6,500 ft, apply the same 80% conservatism on top of the loading rule.
{{< /faq >}}

{{< faq-schema >}}

## Next logical reads

<a href="/pages/solar-inverter-sizing.html" class="text-link">Inverter sizing calculator</a> <a href="/pages/pure-sine-vs-modified-sine-inverter.html" class="text-link">Pure sine vs modified sine</a> <a href="/pages/battery-cable-size-for-inverter.html" class="text-link">Battery cable size chart</a> <a href="/pages/solar-inverter-cost.html" class="text-link">Inverter cost guide</a>
