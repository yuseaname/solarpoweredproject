+++

title = "Solar Components Explained: Panels, Inverters, Batteries"
slug = "solar-components"
date = 2026-05-31
draft = false
description = "Understand solar panels, inverters, charge controllers, and batteries. Clear component roles with links to comparisons and sizing guides."
image = "/assets/images/field-guide/system-planner-architecture.jpg"
image_alt = "One-line architecture diagram of a complete solar battery power system"
author = "Solar Powered Project"
image_width = 1024
image_height = 576
+++

{{< affiliate-disclosure >}}

## Quick answer

A solar-electric system is **eight jobs, not eight brand decisions**: solar panels, a charge controller, a battery bank, an inverter, wire with fuses and breakers, disconnects, monitoring, and mounting. Each part has one spec that matters more than the rest — see the tables below.

The budget is not spread evenly: panels and the battery dominate a DIY off-grid parts build (roughly **25–40% each**), while the wire, fuses, and mounting that look small on a quote are where most real failures and fires start.

Two facts apply to every decision: there is **no federal tax credit for 2026 installs** (the 30% ITC expired December 31, 2025 under P.L. 119-21 — budget full price, payback about 10–13 years in high-cost states), and [DIY parts pricing](/pages/solar-system-costs.html) runs 40–60% below installed quotes.

## Key takeaways

-   The eight components follow a fixed energy path — panels → charge controller → battery bank → inverter → loads — with fuses or breakers and disconnects at every transition. No component decision makes sense in isolation.
-   Panels and the battery dominate parts cost (roughly 25–40% each); the inverter runs 10–18%, mounting 8–12%, and everything else lands in the single digits — yet wire, fuses, and protection are where most systems fail.
-   Each component has one spec that matters most — the exact list is in the table below.
-   No federal tax credit applies to 2026 installations (ITC expired December 31, 2025). State credits and utility rebates still exist.
-   Start from your loads, not the parts: calculate [daily kWh and peak watts](/pages/how-to-calculate-solar-load.html) first.

## The 8 core components at a glance

<table>
<thead>
<tr class="header">
<th>Component</th>
<th>What it does</th>
<th>Typical share of a DIY parts build</th>
<th>Dedicated guide</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Solar panels</td>
<td>Convert sunlight into DC electricity</td>
<td>25–45% (higher on builds with no battery)</td>
<td><a href="solar-panel-output.html" class="text-link">Panel output</a></td>
</tr>
<tr class="even">
<td>Charge controller</td>
<td>Regulates DC into the battery; MPPT above ~200W of array</td>
<td>3–8%</td>
<td><a href="mppt-vs-pwm.html" class="text-link">MPPT vs PWM</a></td>
</tr>
<tr class="odd">
<td>Battery bank</td>
<td>Stores DC for night, clouds, and outages</td>
<td>25–40% — the swing item</td>
<td><a href="li-ion-vs-lead-acid.html" class="text-link">Li-ion vs lead-acid</a></td>
</tr>
<tr class="even">
<td>Inverter</td>
<td>Converts DC to the AC appliances use</td>
<td>10–18%</td>
<td><a href="solar-inverter-sizing.html" class="text-link">Inverter sizing</a></td>
</tr>
<tr class="odd">
<td>Wire, fuses, breakers</td>
<td>Carry current safely and clear faults</td>
<td>5–12%</td>
<td><a href="solar-wire-size.html" class="text-link">Wire size</a></td>
</tr>
<tr class="even">
<td>Disconnects</td>
<td>Manual shutoff for service and safety</td>
<td>1–3%</td>
<td><a href="solar-combiner-box-and-disconnect-guide.html" class="text-link">Disconnects</a></td>
</tr>
<tr class="odd">
<td>Monitoring</td>
<td>Shows state of charge, current, daily yield</td>
<td>1–3% (often built into the controller)</td>
<td><a href="solar-battery-management-system-explained.html" class="text-link">BMS explained</a></td>
</tr>
<tr class="even">
<td>Mounting</td>
<td>Holds panels at the right angle against wind and snow</td>
<td>8–12%</td>
<td><a href="ground-mount-vs-roof-mount-solar.html" class="text-link">Roof vs ground mount</a></td>
</tr>
</tbody>
</table>

Those shares describe a **DIY parts build — hardware only**. Installed quotes run **$2.50–$3.50 per watt** for panels and **$1,000–$1,400 per kWh** for batteries — a parts build lands 40–60% lower ([cost breakdown](/pages/solar-system-costs.html)).

## The one spec that matters most, per component

<table>
<thead>
<tr class="header">
<th>Component</th>
<th>One spec to verify first</th>
<th>Why it beats the marketing specs</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Panels</td>
<td>Rated watts (STC)</td>
<td>Efficiency matters for roof space, not generation</td>
</tr>
<tr class="even">
<td>Charge controller</td>
<td>Max input voltage vs cold-weather array Voc</td>
<td>Exceeding it can kill the controller instantly</td>
</tr>
<tr class="odd">
<td>Battery bank</td>
<td>Usable kWh</td>
<td>Nameplate Ah understates what lead-acid can deliver</td>
</tr>
<tr class="even">
<td>Inverter</td>
<td>Continuous watts, not "peak"</td>
<td>Peak ratings alone won't run sustained loads</td>
</tr>
<tr class="odd">
<td>Wire</td>
<td>Ampacity at your run length</td>
<td>Voltage drop and heat scale with distance</td>
</tr>
<tr class="even">
<td>Fuses / breakers</td>
<td>DC voltage rating</td>
<td>AC-rated breakers may not clear DC arcs</td>
</tr>
<tr class="odd">
<td>Disconnects</td>
<td>Load-break rating</td>
<td>Undersized switches weld closed under load</td>
</tr>
<tr class="even">
<td>Mounting</td>
<td>Wind-load rating</td>
<td>Unrated racks fail exactly during storms</td>
</tr>
</tbody>
</table>

## Panels

Panels are the generator: photovoltaic cells convert sunlight into direct current with no moving parts. Output is rated in watts at Standard Test Conditions, so a "100W panel" makes 100W only under ideal lab light — real-world output depends on sun hours, angle, temperature, and shade (10–25% of rating under heavy cloud). Worked example: a cabin using 2,000Wh/day with 4 good sun hours needs roughly 2,000 ÷ (4 × 0.8) ≈ **625W of panel** after the 0.8 efficiency penalty — about six 100W modules.

**The one spec that matters most: rated watts (STC), matched to daily kWh and sun hours.** Read [how to calculate solar load](/pages/how-to-calculate-solar-load.html) first, then [panel output](/pages/solar-panel-output.html) and [how to read a spec sheet](/pages/read-solar-panel-specs-sheet.html).

<a href="solar-panel-output.html" class="text-link">Calculate panel output →</a> <a href="how-many-solar-panels-to-power-a-house.html" class="text-link">How many panels for a house →</a> <a href="solar-panel-efficiency.html" class="text-link">Panel efficiency →</a>

{{< product-box asin="B07GF5JY35" name="Renogy 100W 12V Monocrystalline Panel" label="The reference panel" description="The module most component guides describe by default — monocrystalline, IP67, and the mounting and branch-connector ecosystem every other component assumes." button="Check price on Amazon" >}}

## Charge controller

The charge controller sits between the panels and the battery and prevents overcharging by delivering the right voltage and current. Above roughly 200W of array, or on 24V/48V banks, MPPT is the practical choice — it converts panel voltage down instead of wasting the difference, which matters on cold days and is required when panel voltage sits below bank voltage ([MPPT vs PWM](/pages/mppt-vs-pwm.html)).

**The one spec that matters most: max input voltage, checked against the array's cold-weather Voc.** Panels produce more voltage when cold. Worked example: three 100W panels in series, each 22V Voc, give 66V at 25°C; on a -10°C morning that's about 66 × 1.105 ≈ **73V** — fine under a 100V controller, but four panels reach ~97V and need the 150V class. Then size by current: panel watts ÷ battery volts × 1.25. A 400W array on 12V: 400 ÷ 12.8 × 1.25 ≈ **39A** — a 40A-class controller.

<a href="best-mppt-charge-controllers.html" class="text-link">Best MPPT charge controllers</a> <a href="mppt-charge-controller-cost.html" class="text-link">MPPT cost guide</a> <a href="12v-vs-24v-vs-48v-solar.html" class="text-link">12V vs 24V vs 48V systems</a>

{{< product-box asin="B073ZJ3L13" name="Victron SmartSolar MPPT 100/30" label="The reference controller" description="The charge controller component diagrams are drawn around — MPPT efficiency, 12/24V auto-detect, lithium presets, and Bluetooth monitoring as the standard feature set." button="Check price on Amazon" >}}

## Battery bank

The battery is what lets you use solar after sunset and through cloudy stretches. Chemistry matters more than brand: **LiFePO4 runs 80–90% depth of discharge and thousands of cycles; lead-acid is cheaper but only ~50% DoD** ([li-ion vs lead-acid](/pages/li-ion-vs-lead-acid.html)). The usable number is the one you plan around: a 10kWh LiFePO4 bank at 85% usable delivers 8.5kWh.

**The one spec that matters most: usable kWh, sized from daily load.** Worked example: 3,000Wh/day for one autonomy day at 85% DoD needs 3,000 ÷ 0.85 ≈ **3,530Wh ≈ 3.5kWh usable** — about 276Ah of 12.8V LiFePO4 (three 100Ah batteries). Real off-grid builds size for 2–3 days, so double or triple that math. Cost is the swing item: installed systems run **$1,000–$1,400/kWh**; DIY parts run **$260–$500/kWh**, with raw LiFePO4 cells nearer $150–$300/kWh ([cost per kWh](/pages/solar-battery-cost-per-kwh.html)). Runtime method: [how long will a 100Ah battery run](/pages/how-long-will-100ah-battery-run.html); models: [best solar batteries 2026](/pages/best-solar-batteries-2026.html).

## Inverter

The inverter converts DC from the battery into the AC your appliances expect. Topology: **string inverters** handle the whole array through one unit (simpler, cheaper, single point of failure); **micro-inverters** convert per panel (shade tolerance, per-panel monitoring, higher cost) — see [micro vs string](/pages/micro-vs-string-inverters.html). Output type: **pure sine** is required by most motor loads; **modified sine** is cheaper but causes hum and premature motor failure ([pure sine vs modified sine](/pages/pure-sine-vs-modified-sine-inverter.html)).

**The one spec that matters most: continuous watts — plus surge for motor loads — not "peak."** A fridge running at 150W can surge 800W at compressor start. Size continuous capacity at about 1.5× simultaneous load: 1,500W of loads → **2,250W continuous minimum**, so a 2,500–3,000W class unit ([inverter sizing](/pages/solar-inverter-sizing.html)). All-in-one units collapse the controller and inverter into one box; [AC vs DC coupled](/pages/ac-vs-dc-coupled-solar-systems.html) explains when that hybrid design earns its keep.

<a href="how-to-choose-solar-inverter.html" class="text-link">How to choose an inverter</a> <a href="solar-inverter-cost.html" class="text-link">Inverter cost</a> <a href="inverter-keeps-shutting-off-troubleshooting.html" class="text-link">Inverter troubleshooting</a>

## Balance of system: wire, fuses, breakers

"Balance of system" (BOS) is the unglamorous layer that keeps everything else safe: sized wire, fuses, breakers, connectors. This is where DIY solar fires start — a wire sized for 10A carrying 30A heats up, and a fuse without a DC rating may not clear a real fault. Three rules cover most builds: **size wire by amps and distance** (under 3% voltage drop is the common target), **fuse every circuit that can source fault current**, and **use DC-rated protection on the DC side** ([wire size](/pages/solar-wire-size.html), [fuses vs breakers](/pages/solar-fuses-vs-breakers.html)).

**The one spec that matters most: ampacity on the highest-current run — almost always the battery-to-inverter cable.** A 3,000W inverter on 12V draws 3,000 ÷ 12 ≈ **250A at full load**: that run needs 4/0-class cable and a fuse at the battery terminal, not the 10AWG from the panel side. Work through [fuse and breaker sizing](/pages/solar-fuse-and-breaker-sizing.html) per circuit and [battery cable size](/pages/battery-cable-size-for-inverter.html) on that run. Wiring and protection run **5–12% of a parts build** ([cost](/pages/solar-wiring-and-protection-cost.html)).

<a href="solar-panels-series-vs-parallel.html" class="text-link">Series vs parallel panels</a> <a href="solar-combiner-box-and-disconnect-guide.html" class="text-link">Combiner boxes &amp; disconnects</a>

## Disconnects

Disconnects isolate sections of the system — array from controller, battery from inverter — so you can service equipment safely and first responders can kill power in an emergency. They are required on the DC side of grid-tied rooftop systems by NEC rapid-shutdown rules and are plain good practice off-grid. A [combiner box](/pages/solar-combiner-box-and-disconnect-guide.html) usually holds the array disconnect in one enclosure.

**The one spec that matters most: the load-break rating — rated to open the circuit while current is flowing.** An ordinary switch rated 30A can weld its contacts closed when you open it under a 60A battery draw. Size disconnects above maximum circuit current, the same way you size wire. Review [installation safety](/pages/solar-installation-safety-guide.html) and [permits and codes](/pages/solar-permits-and-building-codes.html) before wiring anything to a structure.

## Monitoring

Monitoring turns a black box into a system you understand: state of charge, charge current, daily yield, and — with a battery monitor or BMS — per-cell voltage. Most modern charge controllers have Bluetooth plus an app (the Victron reference above does), covering the generation side. The battery side deserves a shunt-based monitor or BMS: lead-acid ruined by chronic under- or over-charging is the classic off-grid failure ([BMS explained](/pages/solar-battery-management-system-explained.html)).

**The one spec that matters most: that it measures what you act on — state of charge by coulomb counting, not voltage alone.** Voltage-only "battery percentage" lies under load. Monitoring is usually 1–3% of the build or already built into the controller. When things misbehave, start at [output troubleshooting](/pages/solar-output-troubleshooting.html) and [battery not charging](/pages/solar-battery-not-charging-troubleshooting.html).

## Mounting

Mounting is the structural layer: roof rails, ground racks, pole mounts, or tilt stands that hold panels at the right angle for 25+ years — as long as the panel warranty. [Tilt and orientation](/pages/solar-panel-tilt-and-orientation.html) is the performance spec (south-facing at roughly your latitude by default), and [shading](/pages/solar-panel-shading-effects.html) kills more real-world output than any efficiency difference.

**The one spec that matters most: wind-load rating, matched to your local conditions.** A roof rack in a 90-mph wind zone and a ground rack in open country are different engineering problems; unrated hardware fails exactly when you can't see it. Check your [local code](/pages/solar-permits-and-building-codes.html). Choose the platform with [roof vs ground mount](/pages/ground-mount-vs-roof-mount-solar.html), then [ground mount](/pages/ground-mount-solar-panels.html) or [shed installs](/pages/solar-panels-for-sheds.html). Mounting runs **8–12% of a parts build**.

## How the eight fit together

**The whole system in one line:** sunlight → panels (DC) → combiner/disconnect → charge controller → battery bank → inverter → AC loads, with a fuse or breaker at every voltage transition and disconnects at the array, battery, and inverter — every one of those wiring decisions is covered in our [wiring decisions hub](/pages/wiring-decisions.html).

Two things make or break the flow. **Voltages must step deliberately**: panel strings above controller input above battery voltage, with the inverter output at 120/240V AC. And **nothing downstream may be rated below what upstream can deliver** — the controller's output current sets the battery wire; the inverter's draw sets the battery cable and fuse. Pick the bank voltage first ([12V vs 24V vs 48V](/pages/12v-vs-24v-vs-48v-solar.html)), then wire, then protection.

The build order: [calculate the load](/pages/how-to-calculate-solar-load.html) → [size the system](/pages/solar-system-sizing.html) → [choose voltage](/pages/how-to-choose-solar-system-voltage.html) → pick components → [install](/pages/install-solar-panels-yourself.html) → [maintain](/pages/solar-maintenance.html).

## Next logical reads

<a href="solar-system-sizing.html" class="text-link">How to size a system</a> <a href="solar-system-costs.html" class="text-link">Cost breakdown</a> <a href="diy-vs-installer.html" class="text-link">DIY vs installer cost</a> <a href="wiring-decisions.html" class="text-link">Wiring decisions hub</a> <a href="solar-basics.html" class="text-link">Solar power basics</a> <a href="off-grid-solar-system-setup-guide.html" class="text-link">Off-grid setup guide</a>

## FAQ

{{< faq "Which components do I absolutely need for an off-grid system?" >}}
Panels, charge controller, battery bank, fuse/breaker protection, inverter, plus disconnects and mounting, in that order: sunlight hits the panels, DC flows through the controller into the battery, and the inverter converts stored DC to AC for your appliances. Protection (fuses, breakers, disconnects) is not optional — it is what keeps a wiring fault from becoming a fire.
{{< /faq >}}

{{< faq "What is the one spec to check on each component before buying?" >}}
Panel: rated watts (STC). Charge controller: max input voltage, checked against the array's cold-weather Voc. Battery: usable kWh, not nameplate amp-hours. Inverter: continuous watts, not "peak." Wire: ampacity at your run length with under 3% voltage drop. Fuses and breakers: DC voltage rating. Disconnects: load-break rating. Racking: wind-load rating. The sizing guides linked on each component explain how to verify.
{{< /faq >}}

{{< faq "Can I run a solar system without a battery?" >}}
Yes — a grid-tied system without storage sends excess DC straight through the inverter to the grid and draws power back at night. That is the cheapest residential setup because it skips the battery entirely. You only need the charge controller and battery bank if you are storing energy: off-grid, battery backup, or any system where the lights must stay on when the grid is down. The trade-off is covered in [AC vs DC coupled systems](/pages/ac-vs-dc-coupled-solar-systems.html).
{{< /faq >}}

{{< faq "Why is my 100W panel only producing 60W?" >}}
Because 100W is the rating at Standard Test Conditions — ideal light at 25°C. Real output depends on sun angle, panel temperature, cloud, and wiring losses, so 60–85W on a clear day is normal for a 100W panel, and 10–25% of rating under heavy cloud. If output is far below that, the usual causes are shading, a bad connection, or dirty glass — see [solar output troubleshooting](/pages/solar-output-troubleshooting.html) for the checklist.
{{< /faq >}}

{{< faq-schema >}}