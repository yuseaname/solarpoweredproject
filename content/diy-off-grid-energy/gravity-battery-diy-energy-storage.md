+++
title = "Gravity Battery DIY: Store Energy with Weights (Physics + Build Guide)"
slug = "gravity-battery-diy-energy-storage"
date = 2026-05-31
draft = false
description = "A realistic DIY gravity battery guide: potential energy physics (mgh), energy density vs chemical batteries, pulley builds, safety, and when it can supplement solar storage as an educational experiment."
author = "Solar Powered Project"
+++

## Key takeaways

-   Gravity batteries store energy as **gravitational potential energy**: E = mgh (mass × gravity × height).
-   Energy density is extremely low: **1kg lifted 10m stores only 0.027Wh**, vs 50–250Wh for 1kg of lithium battery.
-   Conversion efficiency (mechanical → electrical) is typically **40–70%** depending on gearing, generator, and friction losses.
-   Practical DIY builds range from **desktop demos (1–10Wh)** to garage systems (50–200Wh) to tower setups (500+Wh, advanced).
-   Safety is the biggest concern: **falling weights, structural failure, and crush hazards** require careful design and fail-safes.
-   Best use case: **educational demonstrations** of energy, power, and conversion efficiency — not cost-effective grid replacement.

## Beginner explanation: what a gravity battery is

If you've ever wound up a mechanical watch or a wind-up toy, you've used a gravity-adjacent energy storage mechanism. Those systems use springs, but the principle is the same: store energy mechanically and release it on demand.

A gravity battery skips the spring and uses Earth's gravitational field directly. Lift a weight high, and you've stored potential energy. Let it fall while connected to a generator, and that energy becomes electricity.

### Potential energy basics (mgh)

The amount of energy stored in a lifted weight is given by:

**E = m × g × h**

-   **E**: Energy (joules, J)
-   **m**: Mass (kilograms, kg)
-   **g**: Acceleration due to gravity (≈ 9.8 m/s² on Earth)
-   **h**: Height (meters, m)

This equation is exact — no approximations, no efficiency terms yet. If you lift 100kg by 10m, you store exactly 9,800 joules (about 2.7 watt-hours).

### Why lifting weights stores energy

When you lift a weight, you do work against gravity. That work gets stored in the gravitational field as potential energy.

Release the weight and let it fall, and gravity does work on the weight, accelerating it downward. If you connect the falling weight to a generator through a pulley or gearing system, you can extract that energy as electricity.

### Conversion to electricity (motor/generator, gearing)

The falling weight must do mechanical work on a generator. This usually involves:

-   **Pulley or winch**: Converts linear descent into rotational motion.
-   **Gearing**: Matches the slow speed of descent (maybe 0.1–1 m/s) to the generator's optimal RPM (often 1000+ RPM).
-   **Generator**: Converts mechanical rotation into electricity.

Each conversion step introduces losses: bearing friction, gear friction, electrical resistance in the generator, and voltage regulation losses.

### Energy density reality check (compare to lithium-ion)

This is where gravity batteries hit a wall. Energy density (watt-hours per kilogram) is abysmal:

<table>
<thead>
<tr class="header">
<th>Energy storage type</th>
<th>Energy density (Wh/kg)</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Gravity (1kg, 10m height)</td>
<td>0.027 Wh/kg</td>
<td>1kg weight at 10m = 0.027Wh</td>
</tr>
<tr class="even">
<td>Lead-acid battery</td>
<td>30–50 Wh/kg</td>
<td>1kg lead-acid ≈ 40Wh</td>
</tr>
<tr class="odd">
<td>Lithium-ion battery</td>
<td>150–250 Wh/kg</td>
<td>1kg lithium ≈ 200Wh</td>
</tr>
</tbody>
</table>

To store the same energy as a 1kg lithium battery (200Wh), you'd need to lift about **7,400kg to a height of 10m**.

This is why gravity batteries are educational experiments, not practical grid-scale storage (except in niche cases like pumped hydro at dam scale).

## How a gravity energy storage system works

A complete gravity battery has six key subsystems. Each one needs attention or performance collapses.

### Lifting mechanism (winch, pulley, crank)

Energy input happens during the lift phase. You can power the lift with:

-   **Manual crank**: Simple, zero-cost, and a great workout. Good for educational demos.
-   **Electric winch**: Powered by solar or grid. Makes recharging fast but adds cost and complexity.
-   **Bicycle pedal drive**: Hybrid human-powered approach. See <a href="pedal-power-generator-for-off-grid-battery-charging.html" class="text-link">pedal power guide</a>.

### Stored weight (concrete blocks, water containers, steel)

The mass determines total energy capacity. Common materials:

-   **Concrete blocks or pavers**: Cheap, dense (≈2.4 kg/liter), stackable. Easy to add or remove mass incrementally.
-   **Water containers**: 1 kg per liter. Safer if dropped (won't crush things), but messier if containers leak.
-   **Steel weights or scrap metal**: Denser (≈7.8 kg/liter), but more expensive unless sourced as scrap.

For a garage-scale build, 50–200kg is typical.

### Controlled descent and generator

During discharge, the weight must descend at a controlled, steady speed to drive the generator at optimal RPM.

Uncontrolled freefall produces no useful electricity — it just converts potential energy into kinetic energy (speed), then waste heat when the weight hits the ground.

Speed control mechanisms:

-   **Generator electrical load**: A resistive or battery load creates electromagnetic braking, slowing descent.
-   **Friction brake**: Mechanical brake that limits descent speed regardless of electrical load.
-   **Governor or flywheel**: Advanced mechanical regulation for constant speed under varying load.

### Gearing or speed regulation

A weight descending at 0.5 m/s on a 0.1m-radius pulley yields about 5 RPM at the pulley shaft. Most DC generators need 500–3000 RPM for useful voltage output.

You need a gear ratio of roughly 100:1 to 600:1. Options:

-   **Chain or belt drives with multiple stages**: Simple, but each stage adds friction.
-   **Worm gears**: Compact, high-ratio, but often 50–70% efficient.
-   **Planetary gears**: More expensive, 80–95% efficient, compact.

### Electrical output (DC generator or alternator)

The generator converts mechanical shaft power into electricity. Common choices:

-   **DC motor as generator**: Permanent magnet DC motors work in reverse. Simple wiring, but voltage varies with speed.
-   **Automotive alternator**: Produces AC, then rectified to DC. Needs higher RPM (1000+ RPM). Common in DIY projects.
-   **Bicycle hub dynamo**: Low power (3–6W max) but perfect for small demos.

### Battery charging or direct load use

Generator output is rarely stable enough to run loads directly. Buffer the energy in a battery for stable voltage and load matching:

-   **Battery → inverter → AC loads**
-   **Battery → DC loads** (lights, USB chargers)

Alternatively, run a resistive load directly (like an LED or heating element) for real-time energy measurement without storage.

## Practical DIY build paths

Start small and prove the concept before scaling up. Gravity batteries are mechanically complex and potentially dangerous if built at large scale without engineering rigor.

### Path A — Desktop demonstration (small weights, low energy)

Goal: Understand the physics and measure conversion efficiency without safety risks.

**Design:**

-   Mass: 1–5kg (books, water bottles, hand weights)
-   Height: 1–2 meters
-   Total capacity: 0.003–0.027 Wh (10–100 joules)
-   Generator: Small DC motor (toy motor, 3–12V)
-   Gearing: 3D-printed gears or LEGO Technic
-   Load: LED lights or small capacitor charging

**Pros:** Safe, cheap, fast to build, excellent for learning.

**Cons:** Essentially zero practical energy output.

### Path B — Garage pulley system (moderate scale)

Goal: Store enough energy to charge a phone or run lights for a few minutes.

**Design:**

-   Mass: 50–100kg (concrete blocks, sandbags)
-   Height: 3–5 meters (ceiling height in garage or shed)
-   Total capacity: 40–135 Wh (if 100% efficient; realistically 20–70 Wh delivered)
-   Pulley system: Heavy-duty steel cable and pulleys rated for load
-   Generator: 12V DC motor or automotive alternator
-   Gearing: Bicycle chain drive with 2–3 stages
-   Battery: Small 12V lead-acid or lithium battery for buffering

**Pros:** Enough energy to be "useful" for demos. Teaches system design and instrumentation.

**Cons:** Moderate cost ($100–$300). Safety risks if poorly designed. Still far less practical than a $50 battery.

### Path C — Tower/scaffold larger build (advanced, safety-critical)

Goal: Multi-hundred-watt-hour storage, approaching small battery bank capacity.

**Design:**

-   Mass: 200–1000kg
-   Height: 10–20 meters (scaffolding, tower, or grain silo)
-   Total capacity: 540–5400 Wh theoretical (200–2000 Wh realistic after losses)
-   Structure: Engineered scaffolding or purpose-built tower with load ratings verified
-   Safety: Redundant braking, fall protection, structural engineering review
-   Generator: Industrial-grade alternator or custom-built high-efficiency generator

**Pros:** Approaches "interesting" energy capacity. Can demonstrate grid-scale concepts.

**Cons:** Extremely dangerous if built improperly. High cost ($1,000–$10,000+). Requires engineering expertise. Still worse cost-per-Wh than batteries.

### Choosing weight, height, and drop time

These three variables define your system:

-   **Weight (mass)**: Scales energy linearly. Double the mass = double the energy.
-   **Height**: Also linear. Double the height = double the energy.
-   **Drop time**: Determines power (watts). Slow descent = low power over long time. Fast descent = high power briefly.

Example: 100kg at 10m stores 2.7Wh. If it descends in:

-   **1 minute** → average power ≈ 160W (theoretical)
-   **10 minutes** → average power ≈ 16W
-   **1 hour** → average power ≈ 2.7W

Choose drop time based on the load you want to run and generator efficiency at different speeds.

## Sizing and expected energy output

Calculating theoretical capacity is trivial (E = mgh). Predicting real-world delivered energy requires accounting for every loss mechanism.

### The potential energy equation: E = mgh

This is your starting point. Energy stored (in joules) = mass (kg) × 9.8 (m/s²) × height (m).

To convert joules to watt-hours: **1 Wh = 3600 J**.

So: **Wh = (m × g × h) / 3600**

### Worked examples (10kg at 3m, 100kg at 10m, etc.)

<table>
<thead>
<tr class="header">
<th>Mass (kg)</th>
<th>Height (m)</th>
<th>Energy (J)</th>
<th>Energy (Wh)</th>
<th>Realistic delivered (Wh)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10</td>
<td>3</td>
<td>294</td>
<td>0.08</td>
<td>0.04–0.06</td>
</tr>
<tr class="even">
<td>50</td>
<td>5</td>
<td>2,450</td>
<td>0.68</td>
<td>0.3–0.5</td>
</tr>
<tr class="odd">
<td>100</td>
<td>10</td>
<td>9,800</td>
<td>2.7</td>
<td>1.4–2.0</td>
</tr>
<tr class="even">
<td>200</td>
<td>10</td>
<td>19,600</td>
<td>5.4</td>
<td>2.7–4.0</td>
</tr>
<tr class="odd">
<td>500</td>
<td>20</td>
<td>98,000</td>
<td>27</td>
<td>14–20</td>
</tr>
</tbody>
</table>

### Conversion efficiency (mechanical → electrical losses)

Realistic system efficiency is 40–70%, depending on:

-   **Pulley and bearing friction**: 5–15% loss
-   **Gearing friction**: 10–50% loss (worm gears are worst, planetary gears best)
-   **Generator efficiency**: 50–85% (small DC motors are inefficient; alternators better at higher RPM)
-   **Voltage regulation and battery charging**: 5–15% loss

A well-designed system with quality bearings, planetary gears, and a matched generator might hit 60–70% overall. A crude system with worm gears and a toy motor might deliver 30–40%.

### How long can it power a load? (watt-hours vs watts)

This is where beginners get confused: watts vs watt-hours.

-   **Wh** (watt-hours): Total energy stored.
-   **W** (watts): Rate of energy use or delivery (power).

Runtime = Wh ÷ W.

Example: 100kg at 10m delivers 2Wh (realistic).

-   Running a 2W LED → 1 hour runtime
-   Running a 10W phone charger → 12 minutes
-   Running a 50W laptop → 2.4 minutes

### Comparing to a small lead-acid or lithium battery

Let's compare cost and space for equivalent storage:

<table>
<thead>
<tr class="header">
<th>Storage method</th>
<th>Capacity</th>
<th>Cost</th>
<th>Weight/size</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Gravity (100kg, 10m)</td>
<td>2 Wh</td>
<td>$50–$200 (pulley, gearing, generator)</td>
<td>100kg + 10m vertical space</td>
</tr>
<tr class="even">
<td>Lead-acid (35Ah, 12V)</td>
<td>420 Wh</td>
<td>$80–$150</td>
<td>12kg, shoebox-sized</td>
</tr>
<tr class="odd">
<td>Lithium (100Ah, 12V)</td>
<td>1,200 Wh</td>
<td>$300–$600</td>
<td>12kg, shoebox-sized</td>
</tr>
</tbody>
</table>

To match a cheap 420Wh lead-acid battery with gravity storage, you'd need to lift 15,500kg by 10m. That's not a DIY project — that's civil engineering.

## Costs, efficiency, and maintenance

Gravity batteries are mechanically intensive. The more capacity you want, the more you pay for structure, gearing, and safety.

### Material costs (weights, pulleys, frame, generator)

Desktop demo build (1–10 Wh capacity):

-   Weights: $0 (books, water bottles)
-   Pulley and string: $5–$10
-   Small DC motor: $5–$15
-   Gears/3D-printed parts: $10–$30
-   **Total: $20–$65**

Garage-scale build (20–100 Wh capacity):

-   Weights (concrete, sandbags): $20–$50
-   Heavy-duty pulley and cable: $30–$80
-   Gearing (chain drives, sprockets): $40–$120
-   Generator (alternator or DC motor): $30–$100
-   Frame and mounting: $50–$150
-   Battery and regulation: $50–$150
-   **Total: $220–$650**

Cost per Wh for gravity: $3–$10/Wh. Cost per Wh for lithium battery: $0.25–$0.50/Wh.

Gravity batteries are 10–40× more expensive per watt-hour.

### Efficiency stack (friction, gearing, generator, regulation)

Round-trip efficiency (energy in during lift → energy out during descent) depends on your build quality:

-   **Best case**: Ball-bearing pulleys, planetary gears, high-efficiency generator, MPPT regulation → 60–70% round-trip.
-   **Typical DIY**: Bushings, chain drives, DC motor generator, simple regulation → 40–55%.
-   **Crude build**: Worm gears, friction-heavy pulleys, mismatched generator → 25–40%.

Compare to lithium battery round-trip efficiency: 90–95%.

### Mechanical wear and cable/rope inspection

Gravity batteries have moving parts under load — wear is inevitable:

-   **Cable or rope**: Inspect for fraying, kinks, or corrosion every month. Replace annually or after 1000+ cycles.
-   **Pulleys and bearings**: Lubricate every 3–6 months. Replace bearings if they develop play or noise.
-   **Gears and chains**: Clean and re-lubricate every 6 months. Check for tooth wear.
-   **Generator brushes** (if DC motor): Replace every 500–2000 hours of operation.

### When is it worth building vs just buying a battery?

Build a gravity battery if:

-   Your goal is **education** and you want to understand energy storage physics hands-on.
-   You have free materials and time, and enjoy mechanical projects.
-   You're teaching students or demonstrating concepts at a makerspace.

Don't build one if:

-   You need practical, cost-effective energy storage for off-grid living.
-   You lack fabrication skills or tools for safe structural design.
-   You're hoping to save money vs buying batteries (you won't).

## Electrical design for useful output

The mechanical side is only half the system. You need proper electrical design to extract, regulate, and store the energy usefully.

### Generator selection (DC motor as generator, alternator)

Generators for DIY gravity batteries:

-   **Permanent magnet DC motor (12V–48V)**: Simple wiring, voltage proportional to RPM. Good for variable-speed systems if paired with a boost/buck converter.
-   **Automotive alternator**: Designed for 1000+ RPM. Produces AC, rectified to DC internally (on most units). Needs field excitation but self-regulates voltage once spinning.
-   **Stepper motor as generator**: Can work at very low RPM but produces pulsed DC that needs filtering. Common in low-power demos.
-   **Bicycle dynamo**: 3–6W at typical speeds. Perfect for desktop demos, useless for meaningful power.

### Voltage regulation and battery charging

Generator output voltage varies with descent speed. You need regulation to prevent overcharging the battery or damaging loads:

-   **Charge controller**: Use a 12V solar charge controller (PWM or MPPT) if generator voltage is 15–30V.
-   **DC-DC buck/boost converter**: If generator voltage is unstable or outside battery charging range.
-   **Shunt regulator**: Diverts excess power to a dump load if battery is full, preventing overvoltage.

### Protection and disconnects

-   **Fuse or breaker** near battery positive terminal (sized for max charging current).
-   **Blocking diode** to prevent battery discharging back through the generator when weight is stationary.
-   **Mechanical brake or disconnect** to stop descent instantly in an emergency.

### Instrumentation (measuring stored vs delivered energy)

The best part of a gravity battery project is quantifying efficiency. Install:

-   **Voltmeter and ammeter** at generator output and battery input.
-   **Watt-hour meter** (or log V × A over time) to measure total energy delivered to battery.
-   **Timer or position sensor** to measure descent time and calculate average power.

Compare measured Wh delivered to theoretical Wh from mgh to calculate system efficiency.

## Common mistakes and misconceptions

Most DIY gravity batteries fail due to mechanical design errors or unrealistic expectations, not electrical problems.

### Underestimating mechanical losses

Friction eats efficiency. Every pulley, every gear mesh, every bearing adds loss.

Beginners often assume 90%+ efficiency and are shocked when real systems deliver 40–60%. Design for worst-case losses and be pleasantly surprised if you do better.

### Ignoring safety (falling weights, structural failure)

A 100kg weight falling 10m has the kinetic energy of a small car crash by the time it hits the ground.

If the cable snaps, pulley fails, or structure collapses, people can die. This is not an exaggeration.

Use safety factors of 5:1 or better on all structural components and cables. Add redundant braking and physical barriers.

### Expecting grid-scale storage from backyard builds

A 500kg weight at 20m stores 27Wh theoretical — enough to run a laptop for 30 minutes.

To store 1kWh (one kilowatt-hour, equivalent to a small home battery), you'd need 18,500kg at 20m height. That's 9 full-size cars suspended 6 stories high.

Gravity storage scales at industrial/utility level (pumped hydro, crane-based systems), not backyard DIY.

### Poor speed control causing voltage spikes

If the weight free-falls, the generator spins too fast and produces voltage spikes that can:

-   Damage electronics and batteries
-   Blow fuses
-   Overheat the generator windings

Use electrical load (resistor or battery charging resistance) or mechanical braking to limit descent speed.

### Neglecting braking/emergency stop mechanisms

Once a weight starts descending under load, it has momentum. If something goes wrong, you need to stop it instantly.

Install:

-   Mechanical brake (caliper, band brake, or friction pad on pulley)
-   Emergency disconnect (pull-cord or lever that releases electrical load, allowing brake to engage)
-   End-stop or shock absorber at bottom of travel

## Safety and limitations

Gravity batteries are among the most dangerous DIY energy projects. Treat them with the same respect as a loaded weapon.

### Structural integrity and load ratings

Every component must be rated for at least **5× the maximum load**:

-   **Cable or rope**: Use steel cable rated for lifting, not hardware-store clothesline. Check working load limit (WLL).
-   **Pulleys**: Must be rated for the load. Cheap plastic pulleys will fail.
-   **Mounting structure**: Anchor to structural beams (not drywall). Use lag bolts into studs or concrete anchors rated for 10× the load.
-   **Weight attachment**: Use secure shackles, bolts, or welded connections. Rope tied around a block is not sufficient.

### Fall hazards and crush risk

If the weight falls unexpectedly:

-   Anyone below is at risk of being crushed or struck.
-   The impact can damage floors, break through ceilings, or destabilize structures.

Mitigation:

-   Install physical barriers (fencing, cages) around the drop zone.
-   Use guide rails or tracks to prevent lateral swing.
-   Never allow people below a suspended weight.
-   Test with sandbags before using solid weights.

### Cable/rope failure modes

Cables fail when:

-   **Overloaded** beyond working load limit.
-   **Frayed or corroded** from wear or moisture.
-   **Kinked or bent** over sharp edges (weakens internal strands).
-   **Improperly terminated** (loops, knots, or clamps installed incorrectly).

Inspect cables before every use and replace if any damage is visible.

### Electrical safety during descent/generation

While 12V is generally safe, high current (10A+) can still cause:

-   **Arc flash** if connections are opened under load.
-   **Fire** from overheated wires or poor connections.
-   **Battery damage** from overvoltage or overcurrent.

Use properly rated fuses, connectors, and wire. See <a href="../pages/solar-wire-size.html" class="text-link">wire sizing guide</a> and <a href="../pages/solar-fuse-and-breaker-sizing.html" class="text-link">fuse/breaker sizing</a>.

### When to keep it purely educational

Build for learning if:

-   You're demonstrating physics concepts in a classroom or workshop.
-   You're teaching kids about energy and power.
-   You enjoy mechanical builds and want a conversation piece.

Avoid large-scale builds unless:

-   You have formal engineering training or work with a structural engineer.
-   You can afford to over-build by 5–10× for safety.
-   You accept that cost-per-Wh will be terrible vs batteries.

## How gravity storage pairs with solar

In theory, gravity batteries could store excess solar energy mechanically instead of chemically. In practice, chemical batteries are so much better that this makes sense only as an educational hybrid.

### Lifting weights with solar during the day

Charge phase: solar panels → charge controller → battery → electric winch → lift weight.

This adds two conversion steps vs direct battery charging:

-   Battery → winch motor (70–85% efficient)
-   Weight descent → generator → battery (40–70% efficient)

Round-trip efficiency: 28–60%, vs 90–95% for battery-only.

### Discharging at night or during cloudy periods

Discharge phase: weight descends → generator → battery → loads.

The gravity battery acts as a "mechanical buffer" between solar input and battery storage. But it's less efficient and more complex than just sizing your battery bank larger.

### Battery vs gravity hybrid architecture

Hybrid approach:

-   **Primary storage**: Chemical battery (lithium or lead-acid) for efficiency and energy density.
-   **Backup/demo storage**: Gravity battery for educational value or extremely long-term storage (weeks/months) without self-discharge.

Gravity storage has zero self-discharge. A suspended weight will hold potential energy indefinitely (ignoring cable creep and material fatigue). Batteries self-discharge 1–20% per month.

This makes gravity attractive for ultra-long-term seasonal storage in niche scenarios, but not typical off-grid use.

### Shared inverter and load management

If both battery and gravity system charge the same battery bank:

-   **Solar → charge controller → battery**
-   **Gravity generator → regulator → battery**
-   **Battery → inverter → AC loads**

The inverter doesn't care where the battery charge came from. This is the simplest integration path.

## FAQ: Gravity battery energy storage

{{< faq "Is a DIY gravity battery practical for off-grid power?" >}}
No, not at any realistic scale. Chemical batteries are 10–40× cheaper per watt-hour and 100× more energy-dense.

Gravity batteries are best for **education** and demonstrating physics, not replacing lithium or lead-acid batteries.
{{< /faq >}}

{{< faq "How much weight do I need to power a house for one day?" >}}
A modest off-grid home might use 5–10 kWh/day (5,000–10,000 Wh).

To store 5,000Wh at 10m height: you'd need to lift **184,000 kg** (184 metric tons, or about 90 cars).

This is why pumped hydro (industrial-scale gravity storage) uses millions of liters of water and dam-scale infrastructure.
{{< /faq >}}

{{< faq "What's the best height for a DIY gravity battery?" >}}
For safety and practicality: **3–5 meters** (garage ceiling height).

Higher is better for energy density (more Wh per kg), but:

-   Structural requirements increase (stronger cable, pulleys, mounting).
-   Fall hazards increase exponentially.
-   Building codes and permitting may apply for tall structures.

Unless you have engineering expertise, don't exceed 5m height.
{{< /faq >}}

{{< faq "Can I use water instead of weights?" >}}
Yes. Water is 1 kg per liter, so it's easy to calculate and adjust mass.

Pros: Safer if spilled (vs crushing hazard of concrete). Easy to add/remove mass. Free if you have a water source.

Cons: Containers can leak. Freezing is a problem in winter. Lower density than concrete or steel, so larger volume needed.
{{< /faq >}}

{{< faq "How long do gravity batteries last?" >}}
Theoretically, indefinitely — there's no chemical degradation like in batteries.

Practically, mechanical components wear out:

-   **Cables**: 1,000–10,000 cycles depending on quality and inspection.
-   **Bearings**: 5,000–50,000 hours depending on load and lubrication.
-   **Gears**: 10,000–100,000+ cycles if well-maintained.

With good maintenance, a gravity battery could last 10–30 years mechanically.
{{< /faq >}}

{{< faq "What's the round-trip efficiency of a gravity battery?" >}}
Realistic DIY builds: **40–60%** (energy in to lift → energy out during descent).

High-quality engineered systems: **60–80%**.

Compare to lithium batteries: 90–95% round-trip efficiency.
{{< /faq >}}

{{< faq "Can I build a gravity battery for emergency backup power?" >}}
Technically yes, but it's not practical.

A simple 100Ah lithium battery (1,200Wh) costs $300–$600 and weighs 12kg. To match that with gravity at 50% efficiency, you'd need to lift 890kg to 10m height.

The infrastructure cost and safety risk far exceed just buying a second battery.
{{< /faq >}}

{{< faq "Are gravity batteries used commercially?" >}}
Yes, at utility scale:

-   **Pumped hydro storage**: Water is pumped uphill to a reservoir, then released through turbines. This is the most common grid-scale energy storage worldwide (95%+ of all grid storage).
-   **Crane-based systems**: Companies like Energy Vault are developing systems that lift concrete blocks with cranes to store grid energy.

But these are megawatt-scale installations with millions in capital investment — not DIY projects.
{{< /faq >}}

{{< faq "What can I learn from building a gravity battery?" >}}
Hands-on understanding of:

-   **Energy vs power**: Total capacity (Wh) vs rate of delivery (W).
-   **Conversion efficiency losses**: How friction, gearing, and regulation eat into theoretical capacity.
-   **Mechanical design trade-offs**: Safety, cost, efficiency, complexity.
-   **Energy density reality**: Why chemical batteries dominate despite being "worse" in some ways (degradation, safety, recycling).

It's one of the best educational energy projects precisely because the limitations are so obvious and measurable.
{{< /faq >}}

{{< faq "Should I build a gravity battery if I'm new to off-grid systems?" >}}
Start with a desktop demo (under 10kg, under 2m height) to learn the physics safely.

Don't attempt garage-scale or larger builds until you've successfully built and instrumented smaller projects.

If your goal is practical energy storage, buy batteries and solar panels instead. If your goal is learning, gravity batteries are fantastic — just keep safety paramount.
{{< /faq >}}

---

## Next logical reads

<a href="../diy-off-grid-energy.html" class="text-link">DIY off-grid energy experiments (pillar) →</a> <a href="pedal-power-generator-for-off-grid-battery-charging.html" class="text-link">Pedal power generator guide →</a> <a href="micro-hydro-basics-for-off-grid-power.html" class="text-link">Micro-hydro basics guide →</a> <a href="diy-small-wind-turbine-for-off-grid-battery-charging.html" class="text-link">Small wind turbine guide →</a> <a href="../pages/battery-capacity.html" class="text-link">Battery capacity calculator →</a> <a href="../pages/solar-wire-size.html" class="text-link">Wire sizing guide →</a> <a href="../pages/solar-fuse-and-breaker-sizing.html" class="text-link">Fuse and breaker sizing →</a> <a href="../pages/solar-system-sizing.html" class="text-link">System sizing guide →</a>

---

**Related guides:**
- [DIY Stirling Engine Generator: Turn Heat Into Electricity (Educational Build)](/diy-off-grid-energy/diy-stirling-engine-generator-off-grid.html)
- [DIY Thermoelectric Generator (TEG): Turn Waste Heat Into Battery Power](/diy-off-grid-energy/diy-thermoelectric-generator-teg-battery-charging.html)
- [Multi-Source Hybrid Off-Grid Charge Controller: Combine Solar, Wind & Hydro](/diy-off-grid-energy/multi-source-hybrid-charge-controller.html)
