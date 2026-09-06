+++
title = "How Long Will a 100Ah Battery Run? The Runtime Formula, Decoded"
slug = "how-long-will-100ah-battery-run"
date = 2026-08-19
draft = false
description = "A 100Ah 12V battery holds ~1,200Wh. Learn the one formula that answers how long it runs any device — fridge, TV, CPAP, lights — with honest chemistry and inverter math."
image = "/images/how-long-will-100ah-battery-run/img-1.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
+++

{{< affiliate-disclosure >}}

## Quick answer

A **100Ah 12V battery holds about 1,200Wh** (100Ah × 12V). Runtime is simply **usable Wh ÷ device watts**, where usable Wh = 1,200 × your depth-of-discharge limit — roughly **960Wh at 80% for lithium**, **600Wh at 50% for lead-acid**. So a 60W device runs about **16 hours on lithium, 10 hours on lead-acid**. A fridge, which cycles on and off, lasts far longer than the raw math suggests — see the duty-cycle section below. The formula is the same for every battery and every device; once you learn it, you never need a lookup table again.

## The formula (once, clearly)

There is exactly one runtime formula, and it has three steps:

**Step 1 — Amp-hours to watt-hours:**

**Ah × V = Wh**

A 100Ah battery at 12V: 100 × 12 = **1,200Wh**. This is the total energy stored. Amp-hours alone tell you nothing until you multiply by voltage — that's the first mistake everyone makes.

**Step 2 — Apply your depth of discharge (DoD):**

**Wh × DoD = usable Wh**

You cannot drain a battery to zero without damaging it. Lithium is safe to about 80–90%, lead-acid to about 50%. So usable energy is 1,200 × 0.80 = **960Wh** (lithium) or 1,200 × 0.50 = **600Wh** (lead-acid).

**Step 3 — Divide by your device's watts:**

**usable Wh ÷ W = hours**

A 60W device on lithium: 960 ÷ 60 = **16 hours**. On lead-acid: 600 ÷ 60 = **10 hours**.

That's the whole method. The three mistakes that wreck the answer:

1. **Forgetting voltage.** Ah ≠ Wh. A 100Ah 12V battery (1,200Wh) is not the same as a 100Ah 24V battery (2,400Wh) — see the scaling section.
2. **Ignoring DoD chemistry.** Draining lead-acid to 80% kills it fast. The chemistry table below is not optional.
3. **Ignoring inverter losses.** If your device runs on AC (wall plug), the inverter burns 10–15% of the energy as heat — and often draws power even when idle. That's the next section.

## Why chemistry changes everything

"100Ah" means different real energy depending on what the battery is made of. The chemistry sets your safe DoD, which sets your usable Wh, which sets your runtime.

<table>
<thead>
<tr class="header">
<th>Chemistry</th>
<th>Safe DoD</th>
<th>Usable Wh (100Ah @ 12V)</th>
<th>Typical cycle life</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LiFePO4 (lithium)</td>
<td>80–90%</td>
<td>960–1,080Wh</td>
<td>2,000–5,000 cycles</td>
</tr>
<tr class="even">
<td>AGM / sealed lead-acid</td>
<td>50%</td>
<td>~600Wh</td>
<td>500–1,000 cycles</td>
</tr>
<tr class="odd">
<td>Flooded lead-acid</td>
<td>50%</td>
<td>~600Wh</td>
<td>300–700 cycles</td>
</tr>
</tbody>
</table>

Two batteries both labeled "100Ah" can deliver very different usable energy — a lithium one gives you up to 1,080Wh usable, a lead-acid one only 600Wh. That's a 44% difference in runtime for the same label. It's also why lithium costs more: you pay for usable energy and cycle life, not just amp-hours. For the full trade-off, see our [lithium-ion vs lead-acid](/pages/li-ion-vs-lead-acid.html) comparison.

## AC devices: the inverter tax

If your device plugs into a wall outlet, it runs on AC. Your battery outputs DC. The inverter that converts between them is not free — it costs you **10–15%** of the energy as heat, and it draws a small idle current even with nothing plugged in.

**Worked example, before and after the inverter:**

A 100W AC device, no inverter math: 960 ÷ 100 = **9.6 hours**.

With a realistic 85% efficient inverter: the battery must supply 100 ÷ 0.85 ≈ **118W**. Runtime: 960 ÷ 118 ≈ **8.1 hours**.

That's 1.5 hours lost to the inverter — about 15%. For a small device like a 10W router, the inverter's idle draw can matter more than the device itself, so a DC-powered router is often the smarter choice. When sizing an inverter, also check our [battery cable size for inverter](/pages/battery-cable-size-for-inverter.html) guide — undersized cable is a common hidden loss.

## The lookup table

Here's the runtime for a **100Ah 12V battery** across common draws, using 80% DoD for lithium (960Wh usable) and 50% for lead-acid (600Wh usable). Every number is the formula — usable Wh ÷ watts — nothing else.

<table>
<thead>
<tr class="header">
<th>Device (typical draw)</th>
<th>Watts</th>
<th>Lithium runtime</th>
<th>Lead-acid runtime</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Wi-Fi router</td>
<td>10W</td>
<td>96h</td>
<td>60h</td>
</tr>
<tr class="even">
<td>CPAP (no humidifier)</td>
<td>30W</td>
<td>32h</td>
<td>20h</td>
</tr>
<tr class="odd">
<td>LED TV</td>
<td>60W</td>
<td>16h</td>
<td>10h</td>
</tr>
<tr class="even">
<td>Laptop + monitor</td>
<td>100W</td>
<td>9.6h</td>
<td>6h</td>
</tr>
<tr class="odd">
<td>Fridge (average running watts)*</td>
<td>150W</td>
<td>6.4h</td>
<td>4h</td>
</tr>
<tr class="even">
<td>Power tool / space heater</td>
<td>300W</td>
<td>3.2h</td>
<td>2h</td>
</tr>
<tr class="odd">
<td>Microwave / kettle</td>
<td>600W</td>
<td>1.6h</td>
<td>1h</td>
</tr>
</tbody>
</table>

*The fridge row is the trap. A 150W fridge does **not** run at 150W continuously — it cycles. The 6.4h figure is what you'd get if it ran flat-out, which it never does. The real answer is in the next section.

## The fridge asterisk: duty cycle decoded

A fridge's compressor runs in cycles, not continuously. Typical duty cycle is **30–50%** — the compressor is on only a third to half of the time. That changes everything.

**Effective watts = running watts × duty cycle**

A 150W fridge at 40% duty cycle draws an average of 150 × 0.40 = **60W**. On lithium: 960 ÷ 60 = **16 hours** — not 6.4. On lead-acid: 600 ÷ 60 = **10 hours**.

So a 100Ah lithium battery can realistically run a modern fridge for about **16 hours**, and a lead-acid one for about **10 hours** — roughly 2.5× the naive table number. Duty cycle varies with ambient temperature, door openings, and fridge age, so treat these as estimates. For the full method of measuring *your* fridge's real running watts, surge, and daily Wh, see our [what size solar generator to run a refrigerator](/pages/what-size-solar-generator-run-refrigerator.html) guide — we won't duplicate its measuring steps here. And if the load is a medical device like a CPAP, our [CPAP battery backup guide](/pages/cpap-battery-backup-guide.html) applies the same formula to that specific case.

## 200Ah worked example: running a refrigerator

The most common real-world version of this question is "how long will a 200Ah battery run my fridge?" — so here is the full arithmetic at 200Ah, using the same duty-cycle logic from the section above.

**Nameplate energy:** 200Ah × 12.8V (LiFePO4 nominal) = **2,560Wh**. A generic 12V-nominal rating of the same amp-hours holds 2,400Wh — that is the convention the scaling table further down uses. What you can actually use depends on chemistry:

| Chemistry | Usable fraction | Usable Wh | Est. fridge-days |
| :-- | :-- | :-- | :-- |
| LiFePO4 (lithium) | 80-90% | ~2,050-2,300Wh | **~1-2 days** |
| Lead-acid (AGM/gel, 12V nominal) | 50% | ~1,200Wh | **~0.75-1 day** |

**The demand side:** an efficient modern full-size fridge averages 1-1.5kWh/day; older or larger units can hit 2kWh+. Add roughly 10% for inverter conversion losses when the fridge runs on AC. A modest 60W average draw (the 150W-at-40%-duty example from above) works out to ~1.44kWh/day.

**Putting it together (LiFePO4):** 2,300Wh usable / (1,440Wh/day x 1.1 inverter tax) = **~1.4 days** of fridge runtime from a 200Ah lithium bank. With a hungrier 2kWh/day fridge, that falls to ~1 day; with a small efficient unit (~1kWh/day), closer to 2. The lead-acid bank delivers roughly half those numbers for the same nameplate — the chemistry difference is worth more than the brand sticker.

For sizing the whole backup around a fridge — surge watts, solar refill rates, and generator trade-offs — see the [what size solar generator to run a refrigerator](/pages/what-size-solar-generator-run-refrigerator.html) guide, and to convert any runtime into a bank size, the [battery capacity calculator](/pages/battery-capacity.html) does the reverse math.

## Devices with surges and cycles

Three device types bend the formula, and each bends it differently:

**Anything with a motor** (fridge, freezer, pump, fan) has a **surge** — a brief start spike of 2–4× running watts. Surge matters for inverter sizing more than runtime: a 150W fridge might need 600W of surge capacity for a fraction of a second. The battery's Wh math is unchanged — the surge is too brief to drain meaningful energy — but the inverter must be able to deliver it or the device never starts.

**Anything with a thermostat** (fridge, freezer, water heater) has a **duty cycle** — it cycles on and off to hold a setpoint. Use effective watts (running watts × duty cycle), not nameplate watts, for runtime.

**Anything that charges** (phone, laptop, power tool battery) draws a **taper current** — high at first, then dropping as the battery fills. A laptop might pull 60W for the first hour and 20W after. The formula still works, but your runtime is longer than the peak-watt math suggests because the average draw is lower.

## From runtime to system: how fast will solar refill it?

Runtime tells you how long the battery lasts; solar tells you how fast it comes back. The full sizing method lives in our [solar system sizing](/pages/solar-system-sizing.html) guide — here's the one-paragraph version. If you drained 960Wh usable from a lithium battery, a 200W panel in 4 good sun hours at ~80% efficiency delivers about 200 × 4 × 0.8 = **640Wh** — roughly two-thirds of a full recharge in one good day. A 100W panel delivers about half that, so it extends runtime but won't keep up with heavy use.

One charging note: don't slam a battery from zero at maximum current. Lithium batteries typically charge at **0.2–0.5C** — for a 100Ah battery, that's 20–50A — and lead-acid prefers gentler rates. Your charge controller or solar generator handles this automatically; just know that "from zero to full in one sunny afternoon" is usually optimistic.

## Bigger/smaller batteries: scale the same math

The formula doesn't change — only the Wh does. Here's the quick scaling table at 12V, plus one 24V row to show why voltage matters.

<table>
<thead>
<tr class="header">
<th>Battery</th>
<th>Total Wh</th>
<th>Usable Wh (lithium 80%)</th>
<th>Usable Wh (lead-acid 50%)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>50Ah @ 12V</td>
<td>600</td>
<td>480</td>
<td>300</td>
</tr>
<tr class="even">
<td>100Ah @ 12V</td>
<td>1,200</td>
<td>960</td>
<td>600</td>
</tr>
<tr class="odd">
<td>200Ah @ 12V</td>
<td>2,400</td>
<td>1,920</td>
<td>1,200</td>
</tr>
<tr class="even">
<td>100Ah @ 24V</td>
<td>2,400</td>
<td>1,920</td>
<td>1,200</td>
</tr>
</tbody>
</table>

**The 10-second scaling rule:** double the amp-hours, double the runtime. Double the voltage, double the runtime. A 100Ah 24V battery holds the same energy as a 200Ah 12V battery — 2,400Wh — because 100 × 24 = 200 × 12. That's why higher-voltage systems use thinner cable and smaller batteries for the same energy. For the full trade-off, see our [12V vs 24V vs 48V solar](/pages/12v-vs-24v-vs-48v-solar.html) guide, and for how battery capacity fits into a whole system, our [battery capacity](/pages/battery-capacity.html) explainer.

## FAQ

{{< faq "Can a 100Ah battery run a TV overnight?" >}}
Yes, easily. A 60W LED TV on a lithium 100Ah battery runs 960 ÷ 60 = **16 hours** — a full night with hours to spare. On lead-acid it's 10 hours, still enough for a typical night.
{{< /faq >}}

{{< faq "What do two 100Ah batteries in parallel give me?" >}}
Double the amp-hours at the same voltage: 200Ah @ 12V = 2,400Wh, or 1,920Wh usable on lithium. Runtime doubles — a 60W TV runs about 32 hours. Wire them in parallel for 12V, in series for 24V (which doubles Wh without doubling Ah).
{{< /faq >}}

{{< faq "How low can I drain a 100Ah battery?" >}}
It depends on chemistry. Lithium (LiFePO4) is safe to 80–90% DoD — down to about 10–20% remaining. Lead-acid should stop at 50% DoD — 50% remaining — or you sharply shorten its cycle life. Draining lead-acid to 20% repeatedly can cut its life to a fraction of rated cycles.
{{< /faq >}}

{{< faq "Does cold reduce battery capacity?" >}}
Yes. Cold slows the chemical reactions inside the battery. Below about 0°C, lithium capacity drops by roughly 20%, and lead-acid loses even more — up to 30–40% at -20°C. Runtime in winter is shorter than the table suggests, and charging a frozen lithium battery can damage it. Keep batteries above freezing when possible.
{{< /faq >}}
