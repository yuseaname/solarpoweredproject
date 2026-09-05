+++

title = "Li-ion vs Lead-acid Batteries (Solar Comparison)"
slug = "li-ion-vs-lead-acid"
date = 2026-05-31
draft = false
description = "Compare lithium-ion vs lead-acid solar batteries for cost, lifespan, depth of discharge, and best use cases."
image = "/images/li-ion-vs-lead-acid/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
+++

{{< affiliate-disclosure >}}

## Quick answer

If your battery bank will cycle most days — an off-grid cabin, a full-time RV, a daily backup routine — buy LiFePO4 and be done with it. Per usable kilowatt-hour actually delivered over its life, lithium beats lead-acid by roughly 5 to 7 times, and the arithmetic below shows exactly where that number comes from. If the battery will sit near full as occasional backup, if your real budget is $150 rather than $300, or if you can source a good used or free lead-acid bank, lead-acid is still the rational choice. Lithium's one hard limitation is cold: a LiFePO4 battery cannot be charged below 0°C (32°F) without a built-in heater or a low-temperature cutoff, which matters in unheated sheds, cabins, and winter RV trips. Lead-acid charges happily in the cold but gives up 20–30% of its capacity there. Everything else in this comparison is detail; those last two sentences are the decision.

## Comparison table

<table>
<thead>
<tr class="header">
<th>Factor</th>
<th>Li-ion (LiFePO4)</th>
<th>Lead-acid</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Upfront cost per usable kWh</td>
<td>~$230–$320 per usable kWh for budget 12V drop-ins (a $300, 100Ah unit at 80% DoD works out to ~$312)</td>
<td>~$330–$400 per usable kWh for small AGM (a $200, 100Ah unit at 50% DoD works out to ~$333); flooded is cheaper per nameplate kWh but the DoD penalty eats the advantage</td>
</tr>
<tr class="even">
<td>Cycle life</td>
<td>4,000–6,000 cycles to ~80% of original capacity</td>
<td>~500 cycles (AGM) to ~1,000–1,500 (flooded) at 50% DoD</td>
</tr>
<tr class="odd">
<td>Usable depth of discharge</td>
<td>80–100% daily with minimal lifespan penalty</td>
<td>50% maximum for longevity; deeper regularly cuts life in half or worse</td>
</tr>
<tr class="even">
<td>Weight (12V 100Ah)</td>
<td>~25–30 lb</td>
<td>~60–70 lb (AGM); flooded similar or heavier</td>
</tr>
<tr class="odd">
<td>Temperature behavior</td>
<td>Cannot charge below 0°C/32°F without a heater or BMS cutoff; discharge is fine cold but capacity drops</td>
<td>Charges at any temperature (with temp-compensated voltage) but delivers 20–30% less capacity near freezing</td>
</tr>
<tr class="even">
<td>Maintenance</td>
<td>Nearly none — no watering, no equalization, no terminal corrosion from vented gas</td>
<td>Flooded: watering every 1–3 months, terminal cleaning, equalization. AGM/gel: monitoring only</td>
</tr>
<tr class="odd">
<td>Safety mechanism</td>
<td>Built-in BMS: per-cell over/under-voltage, over-current, short-circuit, and temperature protection</td>
<td>Gas venting plus an external low-voltage disconnect; tolerance to overcharge is the built-in "feature"</td>
</tr>
<tr class="even">
<td>Monitoring</td>
<td>Many drop-ins report state of charge as a percentage over Bluetooth via the BMS</td>
<td>Voltage and specific gravity (hydrometer) — indirect, and voltage lies under load</td>
</tr>
</tbody>
</table>

## The capacity math that changes the decision

Two batteries can both say "100Ah" on the label and still not be equal, because amp-hours are only half the story. Usable energy is nameplate capacity times the depth of discharge you're willing to cycle at.

**Lead-acid, 12V 100Ah:**

- Nameplate: 12V × 100Ah = 1,200 Wh
- Recommended DoD: 50%
- Usable: 1,200 × 0.50 = **600 Wh per cycle**

**LiFePO4, 12V 100Ah:**

- Nameplate: 12V × 100Ah = 1,200 Wh (real LiFePO4 packs are 12.8V nominal, so 1,280 Wh — the numbers below are slightly conservative)
- Recommended DoD: 80–100%
- Usable: 1,200 × 0.80 = **960 Wh**, up to 1,200 × 1.00 = **1,200 Wh** per cycle

So the "same size" lithium battery delivers 1.6 to 2 times the usable energy every cycle. That's why our maintenance guide says a 100Ah lithium battery effectively replaces a 200Ah lead-acid bank: the lead-acid unit only lets you safely draw 100Ah before recharging, while the lithium gives you 80–100Ah of the same label. If you're sizing a bank from scratch, run your numbers through the <a href="/pages/battery-capacity.html" class="text-link">battery capacity calculator</a> — it applies DoD for you, and the difference between the two chemistries shows up immediately in the amp-hours it tells you to buy.

## Lifetime cost per usable kWh

Upfront price is where lead-acid looks best and where the comparison is most misleading. The honest metric is cost per usable kilowatt-hour delivered over the battery's life: **price ÷ (usable kWh per cycle × cycle life)**.

**The AGM, over 10 years:**

- Street price for a common 12V 100Ah AGM: ~$200
- Usable per cycle: 600 Wh (from the math above)
- Cycle life at 50% DoD: ~600 cycles
- Lifetime energy from one battery: 0.6 kWh × 600 = 360 kWh
- In daily solar service it lasts roughly 3 years, so a decade needs the original plus ~3 replacements: 4 × $200 = **$800 total**
- Lifetime energy delivered: 4 × 360 = 1,440 kWh
- Cost per usable kWh: $800 ÷ 1,440 = **~$0.56 per kWh**

**The LiFePO4, over the same 10 years:**

- Street price for a common 12V 100Ah drop-in: ~$300
- Usable per cycle: 960 Wh at 80% DoD
- Cycle life: 4,000 cycles (conservative end of the 4,000–6,000 range)
- Lifetime energy: 0.96 kWh × 4,000 = 3,840 kWh — more than a decade of daily cycling, so you buy one
- Cost per usable kWh: $300 ÷ 3,840 = **~$0.08 per kWh**

That's roughly 7 times cheaper per kilowatt-hour actually delivered, before counting the other lead-acid costs: watering time, a replacement you'll forget to buy, and the 80–85% round-trip efficiency (versus ~95% for lithium) that quietly wastes 10–15% of every solar harvest you push through an AGM.

One caveat so the numbers stay honest: $200 and $300 are street prices for small 12V drop-in batteries, which land below the $200–$450 (lead-acid) and $400–$900 (lithium) per-kWh ranges on our <a href="/pages/solar-battery-cost-per-kwh.html" class="text-link">solar battery cost per kWh</a> page — those ranges cover larger banks and systems with integrated electronics. The method is identical either way: always divide by usable kWh and multiply out cycle life, never compare nameplate price tags.

## Temperature and environment

This is the section that flips decisions for anyone with an unheated shed, cabin, or RV.

**Lithium's hard floor.** Charging a LiFePO4 battery below 0°C (32°F) causes lithium plating on the anode — permanent capacity loss and, in the worst case, an internal short. Discharging in the cold is fine; only charging is dangerous. Every quality drop-in handles this one of two ways: the BMS simply refuses charge current below freezing (your panels produce, the battery stays empty), or a self-heating pack warms itself first using a bit of that charge current. If your bank lives where winter happens, you need one of those two features or a heated enclosure — a plain lithium battery and an unheated room is a battery that won't charge from November to March.

**Lead-acid's soft penalty.** Lead-acid accepts charge at any temperature (use a controller with temperature compensation so the voltage setpoints adjust), but the cold strips out capacity: expect roughly 20–30% less usable capacity near 0°C (32°F), and about half the rated capacity at -18°C (0°F). A fully charged lead-acid battery is freeze-resistant; a deeply discharged one is not — its weaker electrolyte can freeze, expand, and crack the case. The pattern is the mirror image of lithium: lead-acid always works a little, lithium either works fully or refuses to charge at all.

**Heat hurts both.** Sustained temperatures above about 45°C (113°F) shorten lithium lifespan, and lead-acid ages even faster — as a rough rule, every 8–10°C above 25°C (77°F) cuts lead-acid life roughly in half. Neither chemistry belongs in a hot attic.

## Charging behavior

The two chemistries reach full charge by different routes, and the difference decides how well each one fits solar's short, unpredictable charging window.

Lead-acid needs three stages. Bulk throws maximum current at the bank until it hits the absorption voltage (about 14.4–14.8V for a 12V flooded bank, 14.2–14.4V for AGM). Absorption then holds that voltage while current tapers, for 1–3 hours, and this stage is non-negotiable: a lead-acid battery that never finishes absorption never reaches 100%, and plates that sit partially charged sulfate and lose capacity. Float finishes the day at ~13.5V. The problem for solar is timing — absorption takes hours, and solar gives you an afternoon. Chronic undercharged lead-acid is the single most common off-grid battery death, and flooded banks also want a periodic equalization charge on top of it all.

Lithium uses CC/CV too, but the practical behavior is different in three ways. First, a LiFePO4 battery accepts full charge current almost all the way to full — there's no long taper — so the same panels refill it faster. Second, it has no memory and no sulfation equivalent: a lithium battery that lives at 60% state of charge is completely unharmed, while a lead-acid battery living at 60% is dying. Third, charge efficiency is near 99% versus roughly 70–85% effective for lead-acid once you account for the taper and losses, so more of what your panels make ends up stored. Lithium doesn't even need float — a controller holding 13.4–13.6V does no harm, but the battery is content to sit at partial charge for weeks.

The practical rule: set the controller's profile to match the chemistry (lithium absorption is typically 14.2–14.6V, and never equalize lithium), and if you're converting an RV with a lead-acid setup, the vehicle's alternator feed needs a DC-DC charger — lithium's low internal resistance can overload a plain alternator connection.

## When lead-acid still wins

Lithium wins the 10-year math, but not every system runs 10 years on daily cycles. Lead-acid remains the right call when:

- **The upfront budget is genuinely fixed.** A functional 100Ah AGM costs ~$200 and a LiFePO4 ~$300. If $300 isn't available, a working $200 battery that gets you off the generator now beats waiting a season to afford the better one.
- **The storage space runs hot.** In a hot shed or attic where summer temperatures push past 40°C, both chemistries suffer, but most lithium BMS units refuse charge above roughly 45–50°C (113–122°F) — the system just stops working on hot afternoons — and you're slow-cooking expensive cells and electronics. Cooking a $200 commodity battery hurts less than cooking a $300 smart pack.
- **The battery is free or refurbished.** Used golf-cart and forklift lead-acid shows up cheap or free constantly, and its state of health can be judged with a hydrometer and a load test. Used lithium is a gamble: cell damage doesn't show on a voltage check, and a tired BMS can hide a pack that's one cycle from trouble.
- **The system is grid-topped.** If a generator or shore power does the real charging and the battery floats as occasional backup — cycling a handful of times a year — you never accumulate the thousands of cycles that pay off lithium. A $200 AGM replaced every 5–6 float years is cheaper than any lithium option for that job.

## Safety

The chemistries fail in opposite directions, and that shapes the enclosure.

Flooded lead-acid vents hydrogen gas every time it charges — the same electrolysis that consumes watering water — and hydrogen becomes explosive above 4% concentration in air. A flooded bank needs an enclosure vented to the outside, no sparks or ignition sources nearby, and containment for the acid in case of a cracked case. AGM and gel batteries recombine most of that gas and vent far less, but they still need relief venting under fault conditions. Lead-acid's failure mode is gradual and visible: corrosion, water loss, shrinking capacity.

Lithium vents nothing in normal operation — it's fully sealed — so it has no hydrogen requirement and can live in tighter indoor spaces. Its safety mechanism is the battery management system: per-cell voltage monitoring that disconnects the bank on overcharge, over-discharge, short circuit, or out-of-range temperature. The BMS is not optional equipment; it's the reason drop-in lithium is safe to own, and series-connected lithium banks need an external one because individual built-in BMS units can't coordinate. The failure mode it guards against is abrupt rather than gradual — thermal runaway burns hard and can't be smothered like a fuel fire — though LiFePO4 is the most thermally stable lithium chemistry in common use. For venting layouts, clearances, and thermal management for either chemistry, see the <a href="/pages/solar-battery-enclosure-guide.html" class="text-link">solar battery enclosure guide</a>, and for what the protection circuitry actually does, see <a href="/pages/solar-battery-management-system-explained.html" class="text-link">how a battery management system works</a>.

## FAQ

{{< faq "Can I just swap my lead-acid battery for a lithium one?" >}}
Usually yes, with three checks. Set the charge controller to a lithium profile (absorption ~14.2–14.6V, no equalization). In an RV, put a DC-DC charger between the alternator and the battery. And confirm the lithium pack has a low-temperature cutoff or heater if it can see freezing — a bare BMS cutoff means no charging below 0°C, which changes your winter behavior.
{{< /faq >}}

{{< faq "Can I mix lithium and lead-acid batteries in the same bank?" >}}
No. They have different charge and float voltages, different acceptable charge currents, and the lithium BMS will disconnect at its own moments, forcing the entire charge and discharge current through the remaining lead-acid units. Each chemistry also hides the other's problems. Pick one per bank.
{{< /faq >}}

{{< faq "How many years does each chemistry actually last?" >}}
In real solar service: AGM typically 3–5 years, flooded lead-acid 5–7 years with regular watering and full absorption charges (up to 7–10 with diligent care), and LiFePO4 10–15 years or 4,000–6,000 cycles. Heat, chronic undercharging, and deep discharging below 50% are what shorten the lead-acid numbers.
{{< /faq >}}

{{< faq "Will lithium work with my existing charge controller?" >}}
Almost certainly, if the controller offers a lithium or user-set profile in the 14.2–14.6V absorption range — most MPPT controllers from the last decade do, and even a basic PWM controller with an AGM setting is usually close enough to work, just without lithium-specific protections. The one thing to verify is low-temperature behavior, since a controller without that logic will happily push charge current into a freezing lithium battery unless the battery's own BMS stops it.
{{< /faq >}}

{{< faq "Does the federal tax credit apply to batteries?" >}}
Not anymore. The 30% federal residential clean energy credit expired December 31, 2025 under P.L. 119-21, so battery and solar installations in 2026 get no federal credit. Any payback math you do this year should assume you're paying full price — which makes the lifetime cost-per-usable-kWh comparison above the one that matters.
{{< /faq >}}

## Next logical reads

<a href="/pages/battery-capacity.html" class="text-link">Battery capacity calculator</a> <a href="solar-components.html" class="text-link">Components overview</a> <a href="solar-system-costs.html" class="text-link">Cost breakdown</a> <a href="/pages/solar-battery-cost-per-kwh.html" class="text-link">Solar battery cost per kWh</a> <a href="/pages/solar-battery-maintenance-guide.html" class="text-link">Solar battery maintenance guide</a> <a href="/pages/solar-battery-management-system-explained.html" class="text-link">Battery management systems explained</a> <a href="/pages/solar-battery-enclosure-guide.html" class="text-link">Solar battery enclosure guide</a> <a href="/diy-off-grid-energy/diy-flywheel-energy-storage.html" class="text-link">Flywheel energy storage, honestly assessed</a>

- <a href="/pages/best-solar-batteries-2026.html" class="text-link">Best solar batteries 2026 comparison</a>