+++
title = "DIY Thermoelectric Generator (TEG): Turn Waste Heat Into Battery Power"
slug = "diy-thermoelectric-generator-teg-battery-charging"
date = 2026-05-31
draft = false
description = "A realistic DIY thermoelectric generator guide: Seebeck basics, temperature requirements, realistic wattage, module selection, boost converter wiring, and safe battery charging as a supplemental off-grid solar backup."
author = "Solar Powered Project"
image = "/images/diy-thermoelectric-generator-teg-battery-charging/hero.webp"
image_alt = "Thermoelectric generator technical plate: TEG module between stove top and heat sink, with Seebeck-effect cross-section detail"
image_width = 1024
image_height = 1536
+++

<figure class="article-image article-image--hero">
<img src="/images/diy-thermoelectric-generator-teg-battery-charging/hero.webp" loading="eager" data-fetchpriority="high" decoding="async" alt="Thermoelectric generator technical plate: TEG module between stove top and heat sink, with Seebeck-effect cross-section detail" width="1024" height="1536" />
</figure>

## Key takeaways

-   Thermoelectric generators work via the **Seebeck effect**: a temperature difference across a semiconductor module creates voltage.
-   Typical efficiency is **3–8%** at best; most waste heat becomes more waste heat, not electricity.
-   Realistic output from a single consumer module: **milliwatts to a few watts**, depending on temperature difference (ΔT).
-   The hot side and cold side must be managed: poor thermal contact or inadequate cooling kills performance instantly.
-   Most TEG systems need a **DC-DC boost converter** to match low module voltage (often &lt;5V) to battery charging voltage (12V+).
-   Best use case: continuous low-power charging as a **supplement** to solar, not a replacement.

## Beginner explanation: how thermoelectric generators work

If you've ever used a Peltier cooler in a mini-fridge or CPU chiller, you've seen the reverse of a thermoelectric generator. Feed electricity to a Peltier module and one side gets hot while the other gets cold.

Flip that around: apply heat to one side and cold to the other, and the module produces electricity. That's the Seebeck effect in action.

### The Seebeck effect (temperature difference → voltage)

Inside a TEG module are many pairs of p-type and n-type semiconductor elements connected electrically in series and thermally in parallel. When you create a temperature gradient across these junctions, charge carriers (electrons and holes) diffuse from hot to cold, creating a voltage.

The bigger the temperature difference (ΔT), the more voltage. But voltage alone doesn't mean power — you need current, too, and that depends on thermal conductivity, electrical resistance, and load matching.

### Why TEGs are inefficient (and why that's okay for learning)

Most of the heat flowing through a TEG doesn't become electricity. It just conducts straight through the ceramic plates and semiconductors to the cold side.

Typical efficiency for consumer modules is 3–8%, and that's under ideal lab conditions. In the real world, thermal contact resistance, air gaps, and mismatched load impedance push real efficiency even lower.

But if the heat is "free" (woodstove, compost, exhaust), low efficiency is acceptable. You're harvesting energy that would otherwise be wasted.

### Typical output expectations (milliwatts to a few watts)

A single 40×40mm consumer TEG module in a moderate setup (like a woodstove side panel) might produce:

-   **50mW to 500mW** with 20–50°C temperature difference
-   **1–3W** with 100–150°C temperature difference and good cooling
-   **5–10W** if you stack multiple modules, manage thermal contact perfectly, and use high ΔT

Compare that to a single 100W solar panel. TEGs are not a solar replacement — they're a niche supplement for specific scenarios.

## How a TEG battery charging system works

A practical thermoelectric charging system has six core pieces. Miss any one of them and performance drops or the system becomes unsafe.

### Heat source (woodstove, compost, engine exhaust)

The hot side needs a steady, controllable heat source. Common DIY options:

-   **Woodstove or rocket stove**: Mount TEG modules on the stove body or flue pipe. Surface temps of 150–300°C are common.
-   **Compost pile**: Active compost can maintain 50–70°C for weeks. Output is low but continuous.
-   **Engine exhaust**: Vehicle or generator exhaust pipes can reach 200–400°C, but vibration and thermal cycling are challenges.
-   **Solar thermal collector**: A black absorber plate under glass can reach 80–120°C, creating a hybrid solar-thermal + TEG system.

### Cold side cooling (heatsink, water, airflow)

The cold side must stay cool to maintain ΔT. If both sides reach the same temperature, voltage and power drop to zero.

-   **Passive heatsink**: Large aluminum or copper fins with natural convection. Simple but limited cooling.
-   **Active fan cooling**: A 12V fan (possibly powered by the TEG itself once started) dramatically improves cold-side performance.
-   **Water cooling**: Flowing water through a cold plate offers excellent cooling but adds complexity and pumping power.

### TEG module specifications and electrical behavior

Consumer TEG modules (often sold as TEC1-12706 or similar Peltier modules used in reverse) are rated by:

-   **Maximum temperature**: Typically 150–200°C on the hot side. Exceeding this damages the module permanently.
-   **Open-circuit voltage (Voc)**: Increases roughly linearly with ΔT. Might be 2–8V depending on ΔT and module design.
-   **Maximum power point**: Like solar panels, TEGs have an optimal load resistance for maximum power transfer. Too high or too low and power drops.
-   **Internal resistance**: Typically 1–5Ω. Matching load impedance matters for efficiency.

### DC-DC boost converter or charge regulation

A TEG producing 2–5V can't charge a 12V battery directly. You need a boost converter that steps voltage up while stepping current down (minus conversion losses).

Look for boost converters with:

-   **Wide input voltage range** (e.g., 0.8–5V input)
-   **Adjustable output voltage** (12V, 14.4V for charging, etc.)
-   **Maximum Power Point Tracking (MPPT)** if available, though this is rare in cheap modules

### Battery and protection

The battery acts as an energy buffer. TEG output is continuous but low-power, so you accumulate charge over hours or days.

Protection essentials:

-   **Fuse or breaker** near the battery positive terminal
-   **Blocking diode or MOSFET** to prevent reverse current if the boost converter fails
-   **Overvoltage clamp** if using an unregulated boost converter
-   **Temperature monitoring** on the hot side to avoid module damage

## Practical DIY build options

Choose a build path based on your heat source, target power, and fabrication skills. Starting small is almost always the right move.

### Path A — Woodstove/rocket stove TEG mount

This is the most popular DIY thermoelectric project. The stove provides high temperatures, and the system can charge batteries while heating your space.

**Design considerations:**

-   Mount TEG modules on a flat section of stove body or flue pipe where surface temp is 150–250°C.
-   Use thermal paste or graphite sheets for good hot-side contact.
-   Attach a large heatsink with fins on the cold side, ideally with a 12V fan powered by the TEG output (self-sustaining once started).
-   Use high-temp wire and connectors near the stove.
-   Install a temperature sensor to avoid exceeding module limits.

**Typical output:** 2–10W depending on ΔT and number of modules.

### Path B — Compost pile heat harvesting (slow, long-term)

Active compost piles generate heat continuously for weeks or months. Temperatures are lower (50–70°C), so output is minimal, but the system is passive and educational.

**Design considerations:**

-   Bury a heat exchanger (copper pipe or aluminum plate) in the center of an active compost pile.
-   Mount TEG modules between the exchanger and an external heatsink.
-   Insulate around the TEG to maximize ΔT.
-   Use waterproof enclosures and corrosion-resistant materials.

**Typical output:** 50–500mW per module, depending on compost activity.

### Path C — Engine exhaust recovery (vehicles, generators)

Exhaust pipes on vehicles or generators can reach 200–400°C, making them attractive for TEG mounting. But vibration, thermal cycling, and safety concerns make this a more advanced build.

**Design considerations:**

-   Use high-temp TEG modules rated for 200°C+ hot side.
-   Design spring-loaded or flexible mounting to handle vibration and thermal expansion.
-   Water-cool the cold side for maximum ΔT.
-   Monitor exhaust backpressure — don't restrict flow.
-   Use automotive-grade wiring and connections.

**Typical output:** 10–50W possible with multiple modules and good engineering, but this is not a beginner project.

### Path D — Desktop/benchtop learning experiment

If your goal is to understand the physics rather than harvest meaningful power, build a low-stakes tabletop demo.

**Design considerations:**

-   Use a single TEG module, a candle or hot plate as heat source, and a CPU heatsink on the cold side.
-   Measure open-circuit voltage, short-circuit current, and power at various loads.
-   Experiment with thermal paste quality, heatsink size, and airflow.
-   Plot ΔT vs power to see the relationship firsthand.

**Typical output:** 10–200mW, but the learning value is high.

## Sizing and expected output (reality check)

TEG performance is dominated by one variable: temperature difference (ΔT). Everything else — module quality, thermal contact, cooling — just modulates how well you can achieve and maintain that ΔT.

### Temperature difference is everything (ΔT)

TEG power output scales roughly with (ΔT)² in the ideal case, though real-world behavior is closer to linear-to-quadratic depending on heat flow and load matching.

If you double ΔT, you might triple or quadruple power output. If you halve ΔT, power drops dramatically.

This is why good thermal contact and active cold-side cooling are non-negotiable for anything beyond a demo.

### Module power rating vs real-world performance

Manufacturer datasheets often show power output at ΔT = 200°C or similar lab conditions. Real-world installations rarely achieve this.

A module rated for "12W at ΔT=200°C" might deliver:

-   **100–300mW** at ΔT = 30°C (compost pile)
-   **1–2W** at ΔT = 100°C (woodstove with passive cooling)
-   **4–8W** at ΔT = 150°C (woodstove with active fan cooling)

Always design for 50–70% of datasheet claims unless you have lab-grade thermal management.

### Example: 5°C, 50°C, 150°C ΔT scenarios

Let's walk through three realistic scenarios using a typical 40mm square TEG module:

<table>
<thead>
<tr class="header">
<th>Scenario</th>
<th>ΔT</th>
<th>Hot side</th>
<th>Cold side</th>
<th>Expected power</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Barely warm surface</td>
<td>5°C</td>
<td>30°C</td>
<td>25°C</td>
<td>5–20mW</td>
</tr>
<tr class="even">
<td>Compost or low-temp waste heat</td>
<td>50°C</td>
<td>70°C</td>
<td>20°C</td>
<td>200–800mW</td>
</tr>
<tr class="odd">
<td>Woodstove with good cooling</td>
<td>150°C</td>
<td>200°C</td>
<td>50°C</td>
<td>3–7W</td>
</tr>
</tbody>
</table>

### How many modules do you need?

If one module produces 2W at your operating ΔT, and you want 10W, you need 5 modules in parallel (assuming thermal and electrical matching).

But diminishing returns kick in fast:

-   Each module adds thermal resistance, making it harder to maintain ΔT unless you scale cooling proportionally.
-   Electrical mismatches between modules (manufacturing tolerances) reduce combined output.
-   Cost and complexity rise linearly while output rises sub-linearly.

For most DIY builds, 2–4 modules is the practical sweet spot.

### Efficiency losses (thermal contact, electrical conversion)

Losses stack up everywhere:

-   **Thermal contact resistance**: Air gaps, poor paste application, or uneven surfaces can cut ΔT by 30–50%.
-   **TEG internal efficiency**: 3–8% is typical, meaning 92–97% of heat becomes waste.
-   **Boost converter losses**: 10–25% depending on quality and load matching.
-   **Wiring and connection losses**: Minimal at low current, but poorly sized wire at low voltage adds up.

Overall system efficiency (heat in → battery charge out) is often 2–5%. But if the heat is free, that's still useful.

## Costs, efficiency, and maintenance

TEG systems are not cheap per watt of output, but they offer unique capabilities that solar can't match (like 24/7 generation from a woodstove).

### TEG module costs per watt

Consumer TEG modules typically cost $5–$30 each, depending on size and quality. At 2–5W realistic output per module, that's $2–$10 per watt of capacity.

Compare that to solar panels at $0.30–$1 per watt. TEGs are 5–30× more expensive per watt of capacity.

But the comparison isn't entirely fair: TEGs work at night, in winter, and anywhere you have waste heat.

### Balance of system costs (heatsinks, mounting, regulation)

The modules are just the start:

-   **Heatsinks**: $10–$50 depending on size and material (aluminum is cheaper, copper conducts better).
-   **Fans** (if active cooling): $5–$15 for 12V PC fans.
-   **Boost converter**: $3–$20 for basic modules; MPPT-capable units cost more.
-   **Mounting hardware**: Depends on heat source; budget $10–$100 for brackets, clamps, and high-temp fasteners.
-   **Thermal paste and insulation**: $5–$20.
-   **Wiring and protection**: $10–$30 for fuses, disconnects, wire.

Total system cost for a 5–10W woodstove TEG setup: $100–$300.

### Maintenance needs (cleaning contacts, thermal paste degradation)

TEG modules have no moving parts, so mechanical maintenance is minimal. But thermal interfaces degrade over time:

-   **Thermal paste drying**: Reapply every 1–2 years for high-temp applications.
-   **Oxidation on metal surfaces**: Clean and re-grease contact surfaces periodically.
-   **Heatsink fouling**: Dust and debris reduce cooling efficiency; clean fins annually.
-   **Fan wear**: Replace cooling fans as bearings wear out (typically 2–5 years).

## Electrical design for battery charging

Getting from a 3V TEG module to a safely charged 12V battery requires careful voltage regulation and protection.

### System voltage choice (12V most common for low power)

Most DIY TEG systems target 12V battery charging because:

-   Readily available batteries, chargers, and loads
-   Boost converters are optimized for 12V output
-   Lower current at 12V vs 6V reduces wiring losses

Higher voltages (24V, 48V) are possible but require more expensive boost converters and offer little benefit at low power levels.

### Boost converter selection (input voltage range matters)

The boost converter is the heart of a TEG charging system. It must handle:

-   **Low input voltage**: Many TEG modules produce 1–5V, so the converter must start and operate in this range.
-   **Variable input**: As ΔT changes (stove heating up or cooling down), voltage and current vary.
-   **Correct output voltage**: 13.8–14.4V for lead-acid float/bulk charging, or 13.3V for LiFePO4.
-   **Current limiting**: Prevents overloading the TEG or overcharging the battery.

Look for converters rated for at least 2× your expected TEG output power to avoid running them at max stress.

### Protection: fuses, disconnects, overvoltage clamps

Even low-power systems need protection:

-   **Fuse near battery positive**: Sized for maximum charging current (e.g., 1A fuse for a 10W system).
-   **Blocking diode or ideal diode controller**: Prevents battery from discharging back through the boost converter at night or when ΔT drops.
-   **Overvoltage protection**: Zener diode or clamp circuit protects battery if boost converter fails in over-voltage mode.
-   **Temperature shutdown**: Optional but recommended for woodstove mounts to disconnect if hot side exceeds safe limits.

### Wire sizing for low-voltage DC

At low voltages (3–5V from the TEG), even small wire resistance causes significant voltage drop.

Use short, heavy-gauge wire between TEG and boost converter:

-   **16–18 AWG for runs under 1 foot**
-   **14 AWG for runs 1–3 feet**
-   **12 AWG for runs over 3 feet**

On the 12V side (boost converter to battery), standard sizing applies: see <a href="../pages/solar-wire-size.html" class="text-link">wire sizing guide</a>.

### Monitoring and instrumentation

TEG systems benefit from measurement because output is so temperature-dependent:

-   **Hot-side temperature sensor**: K-type thermocouple or infrared thermometer spot-check.
-   **Voltage and current meters**: Monitor TEG output and battery charging current.
-   **Watt-hour counter**: Track cumulative energy over days/weeks to see if the system is worth maintaining.

## Common mistakes and misconceptions

TEG projects fail most often from preventable errors in thermal design, not electrical engineering.

### Assuming catalog specs apply to moderate ΔT

A module rated "15W at ΔT=200°C" will produce maybe 1W at ΔT=50°C. Don't design around peak datasheet numbers unless you can prove you'll achieve the required temperature difference.

### Poor thermal contact (air gaps kill performance)

Even a thin air gap adds massive thermal resistance. Use thermal paste, graphite pads, or liquid metal (for advanced builds) to eliminate gaps.

Flat, smooth mating surfaces matter. Sand or mill rough surfaces before assembly.

### Overheating the hot side beyond module rating

Exceeding the module's maximum hot-side temperature (usually 150–200°C for consumer units) causes permanent damage. Solder joints melt, semiconductors degrade, and internal resistance increases.

Always monitor hot-side temperature and use a thermal cutoff or insulating spacer if needed.

### Expecting grid-scale watts from a single module

TEG modules are low-power devices. A single module on a woodstove is not going to run a refrigerator or power tools.

Set realistic expectations: aim for trickle-charging batteries, running low-power sensors, or supplementing solar, not replacing it.

### Ignoring cold-side thermal management

If the cold side heats up to match the hot side, ΔT collapses and power drops to zero. Active cooling (fans) or large passive heatsinks are mandatory for anything beyond milliwatt demos.

## Safety and limitations

Thermoelectric systems are generally safer than wind turbines or micro-hydro (no moving parts, low voltage), but high-temperature heat sources introduce fire and burn risks.

### Fire risk from high-temperature mounting

Mounting TEG modules on woodstoves or exhaust pipes requires:

-   **High-temperature materials**: Stainless steel brackets, ceramic insulators, high-temp wire insulation (silicone, fiberglass).
-   **Clearance from combustibles**: Follow local fire codes for stove installations.
-   **Secure mounting**: Modules must not vibrate loose or fall onto flammable materials.

### Material degradation and thermal cycling stress

Repeated heating and cooling cycles cause:

-   **Thermal expansion mismatches**: Different materials expand at different rates, stressing joints and connections.
-   **Solder joint fatigue**: Internal connections in cheap modules can crack over time.
-   **Ceramic cracking**: Overtightening mounting clamps or rapid thermal shocks can crack module faces.

Design for thermal expansion and avoid rigid, over-constrained mounts.

### Electrical safety on low-voltage high-current systems

While 3–12V is generally safe to touch, poor connections at high current can:

-   **Arc and spark**: Especially on the battery side if disconnected under load.
-   **Overheat and melt insulation**: Undersized wire or corroded connections create hot spots.
-   **Create fire hazards**: Use properly rated wire, connectors, and fuses.

### When TEG is educational vs practical

Thermoelectric generation is practical when:

-   You have reliable, continuous waste heat (woodstove used daily, engine running hours per day).
-   You need low-power charging (under 50W) and solar isn't viable or sufficient.
-   You value the learning experience and enjoy experimental builds.

It's purely educational when:

-   You're trying to replace solar panels or generators with TEG modules (cost and output don't scale).
-   Your heat source is intermittent or low-temperature (under 30°C ΔT).
-   The effort and cost exceed just buying more solar panels or battery capacity.

## How thermoelectric pairs with solar and batteries

TEG and solar are complementary, not competitive. Solar dominates during the day; TEG can charge at night or during winter when a woodstove runs continuously.

### TEG as winter/nighttime supplement to solar

In climates where winter heating is essential, a woodstove TEG can provide continuous low-power charging when solar is minimal.

Example scenario:

-   **Summer**: Solar provides 300Wh/day; woodstove is off; TEG contributes 0Wh/day.
-   **Winter**: Solar provides 50Wh/day; woodstove runs 12 hours/day; TEG contributes 50–100Wh/day.

The TEG doesn't replace solar capacity, but it softens the winter energy deficit.

### Shared battery bank architecture

The simplest integration is parallel charging:

-   **Solar charge controller** → battery positive/negative
-   **TEG boost converter** → battery positive/negative (with blocking diode)
-   **Loads and inverter** → battery bus

Each charge source operates independently. The battery voltage is the common reference point.

### Using solar charge controller for TEG (limitations)

Some people try to feed TEG output into a solar charge controller's input. This rarely works well because:

-   Solar MPPT controllers expect 15–60V+ input; TEG modules produce 3–8V.
-   PWM controllers expect current to flow only during daylight; TEG is continuous.
-   Voltage and impedance mismatches confuse the controller's tracking algorithm.

Use a dedicated boost converter for TEG, and let the solar controller handle solar only.

### Combined wiring and protection strategy

Design the system with independent disconnects:

-   **Main battery disconnect**: Isolates entire system for maintenance.
-   **Solar disconnect**: Allows solar array servicing without affecting TEG.
-   **TEG disconnect**: Allows stove work or TEG maintenance without affecting solar.

Fuse each charging source separately. See <a href="../pages/solar-fuse-and-breaker-sizing.html" class="text-link">fuse and breaker sizing guide</a> for details.

## FAQ: Thermoelectric generators for off-grid power

{{< faq "Can a thermoelectric generator replace solar panels?" >}}
No, not at any realistic scale. TEG modules cost 5–30× more per watt than solar panels and require continuous heat input.

Use TEG to **supplement** solar during winter or at night when a woodstove runs, not as a replacement.
{{< /faq >}}

{{< faq "How much power can I get from a woodstove TEG?" >}}
A typical DIY woodstove TEG with 2–4 modules and good cooling produces **5–15W** while the stove is hot.

If the stove runs 8 hours/day, that's 40–120Wh/day — useful for charging small batteries or running low-power DC loads, but not enough to replace solar or grid power.
{{< /faq >}}

{{< faq "What's the best heat source for DIY thermoelectric generation?" >}}
Woodstoves and rocket stoves are the most practical because they provide high temperatures (150–300°C) for extended periods and are already part of off-grid heating systems.

Compost piles work but produce very low power. Engine exhaust is promising but mechanically complex.
{{< /faq >}}

{{< faq "Do TEG modules wear out?" >}}
High-quality modules can last years if operated within thermal limits. Cheap modules degrade faster, especially if subjected to:

-   Excessive hot-side temperature (over 200°C)
-   Thermal cycling stress (rapid heating/cooling)
-   Poor mounting causing mechanical stress

Expect 3–10 years of useful life for consumer modules in residential woodstove applications.
{{< /faq >}}

{{< faq "Can I use Peltier coolers as generators?" >}}
Yes — Peltier coolers and TEG modules are the same device, just used in reverse. However, Peltier modules optimized for cooling may not be optimized for power generation efficiency.

Dedicated TEG modules (often labeled "TEG" or "thermoelectric generator") typically have better internal resistance matching for power output.
{{< /faq >}}

{{< faq "What temperature difference do I need for useful power?" >}}
For useful battery charging (over 1W per module), aim for **ΔT ≥ 80°C**.

Below 50°C ΔT, most modules produce under 500mW, which is educational but marginal for practical off-grid use.
{{< /faq >}}

{{< faq "Is active cooling (fans) worth it for TEG systems?" >}}
Absolutely. A 12V fan pulling 2–5W can increase cold-side cooling enough to boost ΔT by 30–60°C, which can double or triple TEG output.

Once the TEG produces enough power to self-sustain the fan, the system becomes self-regulating.
{{< /faq >}}

{{< faq "How do I measure TEG performance?" >}}
Install:

-   **Thermocouples or IR thermometer** on hot and cold sides to measure ΔT.
-   **Voltage and current meters** (or a watt meter) at the TEG output and boost converter output.
-   **Watt-hour counter** to log cumulative energy delivered to the battery.

Compare delivered energy over a week to the effort and cost to decide if the system is worthwhile.
{{< /faq >}}

{{< faq "Can TEG modules be stacked in series or parallel?" >}}
Yes, with caution:

-   **Series**: Increases voltage but requires all modules to experience identical ΔT. Thermal mismatches reduce output.
-   **Parallel**: Increases current and is more forgiving of thermal variation. Recommended for most DIY builds.

Match modules by model and test performance before permanent installation.
{{< /faq >}}

{{< faq "What's the biggest mistake beginners make with TEG systems?" >}}
Underestimating the importance of thermal contact and cold-side cooling.

A $20 TEG module with poor thermal paste and no heatsink will produce 10× less power than the same module with proper thermal management. Spend time on mechanical and thermal design, not just electrical wiring.
{{< /faq >}}

---

## Next logical reads

<a href="../diy-off-grid-energy.html" class="text-link">DIY off-grid energy experiments (pillar) →</a> <a href="pedal-power-generator-for-off-grid-battery-charging.html" class="text-link">Pedal power generator guide →</a> <a href="micro-hydro-basics-for-off-grid-power.html" class="text-link">Micro-hydro basics guide →</a> <a href="diy-small-wind-turbine-for-off-grid-battery-charging.html" class="text-link">Small wind turbine guide →</a> <a href="../pages/battery-capacity.html" class="text-link">Battery capacity calculator →</a> <a href="../pages/solar-wire-size.html" class="text-link">Wire sizing guide →</a> <a href="../pages/solar-fuse-and-breaker-sizing.html" class="text-link">Fuse and breaker sizing →</a> <a href="../pages/solar-system-sizing.html" class="text-link">System sizing guide →</a>

---

**Related guides:**
- [DIY Stirling Engine Generator: Turn Heat Into Electricity (Educational Build)](/diy-off-grid-energy/diy-stirling-engine-generator-off-grid.html)
- [Multi-Source Hybrid Off-Grid Charge Controller: Combine Solar, Wind & Hydro](/diy-off-grid-energy/multi-source-hybrid-charge-controller.html)
- [Gravity Battery DIY: Store Energy with Weights (Physics + Build Guide)](/diy-off-grid-energy/gravity-battery-diy-energy-storage.html)
