+++

title = "Micro vs String Inverters (Solar Comparison)"
slug = "micro-vs-string-inverters"
date = 2026-05-31
draft = false
description = "Compare micro-inverters vs string inverters for solar arrays: shade performance, cost, monitoring, and maintenance tradeoffs."
image = "/images/micro-vs-string-inverters/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
+++

{{< affiliate-disclosure >}}

## Quick answer

**A string inverter is the right default for an unshaded, single-orientation roof; microinverters are worth their premium when shade, a complex roof, or per-panel monitoring enters the picture.** On a clean 4kW array the hardware premium for micros is roughly $500–$1,500, and it buys you almost nothing — both architectures convert DC to AC at 96–98% efficiency. Put two chronically shaded panels on that same array and the math flips: the string inverter drags all ten panels down to the weakest two during shade hours, costing roughly 360–1,120 kWh per year versus micros (worked below). Decide with a shade assessment first, an inverter catalog second.

## Key takeaways

-   **Shade is the deciding factor.** One shaded panel in a series string can pull a 10-panel array's output down 20–40% depending on severity; microinverters confine the damage to the shaded panel itself.
-   **Cost gap:** string inverters run roughly $800–$3,000 for the unit; microinverters run roughly $120–$250 per panel. On a 10-panel array that's a premium of a few hundred to ~$1,500.
-   **Reliability trade:** a string inverter is a single point of failure — when it dies, the whole array stops. A failed micro takes out one panel. But the string unit is easy to swap at ground or wall level; a failed micro means roof work.
-   **Warranty gap:** string inverters carry 10–12 year warranties and typically get replaced once in a 25-year system (~$1,000–$2,500). Leading microinverters carry 25-year warranties.
-   **Rapid shutdown:** module-level electronics (micros, optimizers) satisfy NEC 690.12 rapid-shutdown requirements inherently; bare string systems need listed add-on rapid-shutdown devices.
-   **Power optimizers are the middle path:** per-panel MPPT at $30–$60 per panel plus a central inverter — most of the shade benefit, keeps the single-inverter architecture.

## How each architecture works

### String inverter: one brain for the whole array

Panels are wired in series into one or two "strings" whose voltages add — ten 40V panels make a ~400V DC input — and a single wall- or ground-mounted inverter converts it all to 240V AC. The inverter runs one MPPT (maximum power point tracker) per string, so the entire string operates at the current of its weakest panel. That's fine when every panel sees the same sun, and it's why string inverters dominate simple, unshaded installations: fewer parts, lowest cost, one unit to service.

The weakness is the same series circuit. As our [shading guide](/pages/solar-panel-shading-effects.html) explains, a shaded cell becomes a resistor, bypass diodes sacrifice a third of the module to cope, and the string inverter — tracking the string as a whole — has to settle for whatever current the worst panel can pass. A chimney shadow from 2–5 PM taxes every panel in the string, not just the two it touches.

### Microinverter: one brain per panel

A microinverter mounts under each panel and converts DC to AC right there. Each panel gets its own MPPT and operates independently — a shaded panel simply produces less, and the other nine never notice. There is no string inverter at all; the AC outputs combine at a junction box and run to your main panel. You also get per-panel monitoring out of the box: when production dips, the dashboard tells you which panel, not just "the array is down 15%."

The costs are more hardware dollars, more roof-level components and wiring, and electronics living in the hottest spot on the system — the back of a panel in July. Individual failures are rare and only affect one panel, but fixing one means a roof visit.

## Side-by-side comparison

<table>
<thead>
<tr class="header">
<th>Factor</th>
<th>String inverter</th>
<th>Microinverters</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Hardware cost per watt</td>
<td>~$0.15–$0.40/W ($800–$3,000 per unit, size-dependent)</td>
<td>~$0.30–$0.60/W ($120–$250 per 400W panel)</td>
</tr>
<tr class="even">
<td>Shading response</td>
<td>Whole string drops to the weakest panel during shade hours</td>
<td>Loss confined to the shaded panel(s) only</td>
</tr>
<tr class="odd">
<td>Single point of failure</td>
<td>Yes — one unit, whole array down when it fails</td>
<td>No — one failed unit costs one panel (~10% of a 10-panel array)</td>
</tr>
<tr class="even">
<td>Monitoring granularity</td>
<td>String/array-level production</td>
<td>Per-panel production and fault identification</td>
</tr>
<tr class="odd">
<td>Serviceability</td>
<td>Easy — one accessible unit, swap in an hour or two</td>
<td>Harder — diagnosis is precise, but the swap is roof work</td>
</tr>
<tr class="even">
<td>Roof-work complexity</td>
<td>Low — panels plus DC homerun to one inverter</td>
<td>Higher — a unit, cabling, and connection per panel</td>
</tr>
<tr class="odd">
<td>Rapid-shutdown fit (NEC 690.12)</td>
<td>Needs listed add-on rapid-shutdown devices</td>
<td>Inherently compliant — shutdown happens at the module</td>
</tr>
<tr class="even">
<td>Warranty</td>
<td>10–12 years typical</td>
<td>25 years (leading brand)</td>
</tr>
</tbody>
</table>

## Worked example: 10-panel 4kW array with 2 shaded panels

Same array, two architectures. Here are the assumptions, all stated so you can swap in your own numbers:

-   **Array:** 10 × 400W = 4,000W, wired as a single string (string case) or ten independent panels (micro case).
-   **Unshaded production:** ~1,400 kWh per kW per year — a mid-range US residential figure (most homes land between ~1,200 and ~1,600). That's 4,000 × 1,400 ÷ 1,000 = **5,600 kWh/yr**, or 560 kWh per panel.
-   **The shade:** a chimney or tree limb crosses 2 of the 10 panels for about 3 afternoon hours a day. That window carries roughly a third of daily production: 5,600 ÷ 3 ≈ **1,850 kWh/yr**.
-   **Shaded-panel output during the window:** 33–67% of normal. The low end matches a bypass diode sacrificing one of the module's three cell groups (about a one-third loss); the high end is lighter, partial shade. This range comes straight from how bypass diodes partition a 60-cell module.

### String inverter: the whole string sinks to the shaded level

During the shade window, the string inverter's single MPPT must operate at the current the two shaded panels can pass, so **all ten panels** produce at 33–67% for those hours:

-   Window output: 1,850 × 0.33 to 0.67 ≈ **610–1,240 kWh/yr**
-   Normal window output: 1,850 kWh/yr
-   **String loss: 1,850 − 610 to 1,240 ≈ 610–1,240 kWh/yr** (about 11–22% of the array's total)
-   **String harvest: 5,600 − 610 to 1,240 ≈ 4,360–4,990 kWh/yr**

Heavier shade or a longer window gets worse — our shading guide puts a single badly shaded panel in a series string at a 20–40% whole-array loss, and this model's upper edge sits just under that band.

### Microinverters: only the shaded panels pay

The eight clean panels are untouched. Only the two shaded panels lose output, and only during the window:

-   Each shaded panel's window output: 560 ÷ 3 ≈ 187 kWh/yr
-   Loss per shaded panel: 187 × 0.33 to 0.67 ≈ 62–125 kWh/yr
-   **Two-panel loss: ~125–250 kWh/yr**
-   **Micro harvest: 5,600 − 125 to 250 ≈ 5,350–5,480 kWh/yr**

### The difference

**Micro advantage: roughly 360–1,120 kWh/yr** — about 6–20% more harvest on this array, depending on shade severity. At $0.15–$0.25/kWh (spanning typical US residential rates; high-cost states run higher), that's **$54–$280 per year**, or **$1,350–$7,000 over 25 years** at flat rates — more if rates rise.

<table>
<thead>
<tr class="header">
<th>Result (4kW array, 2 shaded panels)</th>
<th>String inverter</th>
<th>Microinverters</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Annual harvest</td>
<td>~4,360–4,990 kWh</td>
<td>~5,350–5,480 kWh</td>
</tr>
<tr class="even">
<td>Loss vs unshaded baseline (5,600 kWh)</td>
<td>~610–1,240 kWh/yr</td>
<td>~125–250 kWh/yr</td>
</tr>
<tr class="odd">
<td>25-yr energy value difference</td>
<td>—</td>
<td>+$1,350–$7,000 at $0.15–$0.25/kWh</td>
</tr>
</tbody>
</table>

### Does the premium pay for itself?

Micro hardware for ten panels runs 10 × $120–$250 = **$1,200–$2,500**, versus roughly **$800–$2,000** for a right-sized string inverter (a 4kW array needs a ~3.6–4.8kW unit under the standard 90–120% [inverter sizing](/pages/solar-inverter-sizing.html) rule). Call the premium **a few hundred to ~$1,500**. Against $54–$280/yr of recovered production, the payback is anywhere from **~2 years in the worst shade to never in light shade**. Two honest caveats cut both ways:

-   If trimming the branch or relocating two panels eliminates the shade, that beats any inverter architecture — free, permanent.
-   The string inverter will likely need one ~$1,000–$2,500 replacement within 25 years; micros with 25-year warranties usually don't. That narrows the lifetime cost gap in micros' favor even before shade math.

## When a string inverter wins

-   **Unshaded, single-orientation roof.** No shade, no mixed orientations, nothing for per-panel MPPT to fix — the premium buys nothing.
-   **Ground mounts and pole mounts.** You control the layout; rows can be wired and angled uniformly, and the inverter sits at ground level where service is trivial.
-   **Budget-first builds.** Every dollar saved on power electronics goes toward more panels, and more panels usually beat fancier electronics on total harvest.
-   **Simple service philosophy.** One replaceable unit, mounted at eye level, with the longest installer familiarity in the industry.

## When microinverters win

-   **Chronic, unavoidable shade.** Mature trees you won't cut, a neighbor's building, power lines — anything the [shading math](/pages/solar-panel-shading-effects.html) says will chronically tax a series string.
-   **Complex roofs.** Multiple orientations, dormers, east-west splits: each panel does its own MPPT, so mixed orientations stop being a design compromise.
-   **You want per-panel monitoring.** Catching one underperforming panel (a cracked cell, a failed diode, debris) is trivial from the dashboard instead of a guessing game — see our [output troubleshooting guide](/pages/solar-output-troubleshooting.html).
-   **Phased expansion.** Add panels one at a time without recomputing string voltage or buying another inverter.
-   **Code-driven rapid shutdown.** Module-level electronics meet NEC 690.12 without add-on devices, which is a real chunk of why they took over US residential installs.

## The middle path: power optimizers

DC optimizers (SolarEdge, Tigo) mount under each panel like micros but only condition DC — per-panel MPPT, then the conditioned power still flows down a string to a central inverter. Hardware adds **$30–$60 per panel** ($300–$600 on this 10-panel array) on top of the string inverter.

What you get: harvest within a few percent of micros in shaded conditions, per-panel monitoring, and a single inverter to service. What you keep from the string column: the central inverter remains a single point of failure with a 10–12 year warranty, and you still have DC wiring on the roof (optimizers bring string voltage down only when the system is shut down per rapid-shutdown rules — under normal operation the string runs at high DC voltage). For many partially shaded roofs, optimizers hit the best cost-per-recovered-kWh; for chronically shaded or multi-orientation roofs, full micros remain the cleaner answer.

<table>
<thead>
<tr class="header">
<th>25-year view (10-panel, 4kW, partial shade)</th>
<th>String</th>
<th>Optimizers + string</th>
<th>Micros</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Power electronics hardware</td>
<td>$800–$2,000</td>
<td>$1,100–$2,600</td>
<td>$1,200–$2,500</td>
</tr>
<tr class="even">
<td>Likely mid-life replacement</td>
<td>$1,000–$2,500 (inverter, once)</td>
<td>$1,000–$2,500 (inverter, once)</td>
<td>~$0–$500 (occasional single units)</td>
</tr>
<tr class="odd">
<td>Harvest in the shade scenario</td>
<td>~4,360–4,990 kWh/yr</td>
<td>Close to micro (per-panel MPPT)</td>
<td>~5,350–5,480 kWh/yr</td>
</tr>
</tbody>
</table>

One budget note that applies to all three columns: the 30% federal residential solar credit expired December 31, 2025 (P.L. 119-21), so for a 2026 install the sticker price is effectively the price — which makes the string-vs-micro premium decision more concrete, not less.

## Next logical reads

<a href="/pages/how-to-choose-solar-inverter.html" class="text-link">How to choose a solar inverter</a> <a href="/pages/solar-inverter-cost.html" class="text-link">Solar inverter cost by type</a> <a href="/pages/solar-panel-shading-effects.html" class="text-link">How shading affects solar panels</a> <a href="/pages/solar-output-troubleshooting.html" class="text-link">Solar output troubleshooting</a>

## FAQ

{{< faq "Do microinverters produce more power than a string inverter?" >}}
Only when conditions differ between panels — shade, mixed orientations, or soiling. On an unshaded, uniform roof, both architectures convert at 96–98% efficiency and harvest essentially the same energy. The micro advantage in our worked example (360–1,120 kWh/yr on a 4kW array) exists entirely because two panels are shaded; remove the shade and the gap collapses to near zero.
{{< /faq >}}

{{< faq "Are power optimizers a good compromise between string and micro?" >}}
Often, yes. Optimizers give you per-panel MPPT — most of the shading benefit — at $30–$60 per panel on top of a cheaper central inverter. You give up the micro's 25-year warranty on the conversion stage and keep a single inverter that will likely need one replacement. If your shade is moderate and your roof is otherwise simple, optimizers usually recover more kWh per dollar than either extreme.
{{< /faq >}}

{{< faq "Which lasts longer, a string inverter or microinverters?" >}}
Microinverters, on paper. String inverters carry 10–12 year warranties and typically get replaced once in a 25-year system at roughly $1,000–$2,500. Leading microinverters are warranted for 25 years. The honest caveat: micros live on the hot back of panels, and a failure — however rare — requires roof work, while a string inverter swap happens at ground or wall level.
{{< /faq >}}

{{< faq "My roof is completely unshaded. Are microinverters still worth it?" >}}
Usually no. With uniform sun and a single orientation, a string inverter harvests the same energy for several hundred to ~$1,500 less on a typical residential array. The remaining micro arguments — per-panel monitoring and expandability — are conveniences, not production gains. Spend the difference on more panels instead.
{{< /faq >}}

{{< faq "Can I expand a microinverter system later?" >}}
Yes, and it's the architecture's quiet advantage. Each panel is independent, so you add capacity panel by panel without recomputing string voltage or replacing the inverter. Expanding a string system means the new panels must match the existing string's voltage window — or you add a second string or a second inverter, which gets complicated fast.
{{< /faq >}}

---

**Related guides:**
- [Solar Inverter Cost: Typical Prices by Type (String, Hybrid, Off-Grid)](/pages/solar-inverter-cost.html)
- [How to Choose a Solar Inverter: Types, Sizing, and What Matters in 2026](/pages/how-to-choose-solar-inverter.html)
- [MPPT Charge Controller Cost: Typical Prices + How to Budget](/pages/mppt-charge-controller-cost.html)