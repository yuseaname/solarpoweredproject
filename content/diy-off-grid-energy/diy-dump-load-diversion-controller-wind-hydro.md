+++
title = "DIY Dump Load (Diversion Control) for Wind + Hydro: Protect Batteries Safely"
slug = "diy-dump-load-diversion-controller-wind-hydro"
date = 2026-05-31
draft = false
description = "A practical DIY diversion (dump load) guide for wind and hydro experiments: why batteries need protection when full, how diversion control works, sizing a dump load, safe wiring with fuses and disconnects, heat management, common mistakes, and how diversion fits into a multi-source solar battery system."
author = "Solar Powered Project"
+++

## Key takeaways

-   A dump load is a **controlled heat sink** for excess generator energy.
-   Wind and hydro can require diversion because the source can keep producing power when the battery is full.
-   Sizing is about **maximum plausible watts** plus margin, and **heat management**.
-   Safety depends on **fusing near energy sources**, a **disconnect**, and wiring sized for current.

## Beginner explanation: diversion is “somewhere safe for power to go”

A dump load is intentionally wasteful. That’s the point. When your generator produces more power than the battery can safely accept, the system diverts the extra power into a load that converts it to heat.

Think of it like a pressure relief valve in plumbing: you don’t want to “use” that water — you want to avoid bursting pipes.

If you’re new to watts vs watt-hours, read <a href="../pages/solar-basics.html" class="text-link">solar basics</a>. Diversion control is about managing watts in real time to keep voltage stable and components safe.

## Why “battery full” is a problem for wind and hydro experiments

Batteries are not bottomless. When a battery is full, it should not keep absorbing charging power at the same rate. In a well-designed system, charging current tapers or is stopped.

### What turbines do when the battery can’t accept power

If a turbine keeps producing energy but the electrical system can’t absorb it, one of three things tends to happen:

-   **Voltage rises** (danger to electronics and batteries).
-   **Mechanical overspeed** (danger to blades, bearings, and couplers).
-   **Uncontrolled heating** (diodes, wiring, regulators, and connectors can overheat).

Diversion is a controlled way to prevent the “nowhere to go” condition.

### Why solar often feels easier

Solar panels can be “turned down” by a controller because they are current-limited sources that respond predictably. Turbines can behave differently: changes in electrical load can change RPM and can create unstable behavior if not managed.

## How diversion control works

A diversion controller monitors battery (or DC bus) voltage. When voltage rises above a threshold (indicating “battery full” or “charging should be limited”), the controller routes current to a dump load.

### Diversion vs series regulation (high-level)

-   **Series regulation:** reduces or interrupts current flowing into the battery.
-   **Diversion regulation:** keeps the generator loaded by sending excess current to another load.

In many wind/hydro situations, keeping the generator loaded is desirable because it helps prevent overspeed.

### PWM diversion (the common pattern)

Many diversion systems pulse current to the dump load (PWM) to control average power smoothly. The dump load still gets hot — but now it’s controllably hot.

## What a dump load actually is

A dump load is simply a device that can safely convert electrical power into heat continuously. For DIY builds, that often means resistors or heating elements.

### Common dump load types

-   **Resistor bank** (wirewound resistors mounted to a heat sink or metal enclosure).
-   **Heating element** (air heater or water heater element) sized for your voltage.
-   **Automotive bulbs** (useful for low-power demos, not for higher power continuous dumping).

The “best” choice depends on power level and how you want to handle heat.

## Sizing a dump load (watts and resistance)

A dump load must handle the maximum power your turbine could plausibly produce in your conditions (or at least the portion you want to divert), plus a safety margin.

### Step 1: estimate maximum plausible watts

Use measured reality, not optimistic ratings. If your wind turbine has produced 120W peaks on a meter, assume the dump load should handle at least that, and preferably more. For hydro, you can estimate water power from head and flow (then apply a conservative efficiency).

If you want a measurement-first method, use a generator test bench approach.

### Step 2: choose a voltage basis (12V / 24V / 48V)

Dump load sizing depends strongly on voltage because for resistive loads:

**P = V² / R**

At higher voltage, the same resistance dissipates more power. At lower voltage, current rises for the same power, which increases wiring demands.

### Step 3: choose resistance and power rating

Suppose you want to dump about 200W on a 12V system. The effective resistance needed is roughly:

**R ≈ V² / P = 12² / 200 ≈ 0.72Ω**

That’s a low resistance, which means high current (about 16–17A at 12V). That current must be handled by wiring, switches, and connectors.

Also, resistors must be rated for the heat. A “200W dump load” is literally a 200W heater. If you build a 200W resistor bank with no airflow or heat sinking, it will overheat.

### Build in margin

A good DIY rule is to oversize thermal handling. If you think you need 200W, aim for a dump load that can safely dissipate more under your mounting conditions.

## Safe wiring patterns

Diversion systems involve high current, and they are often installed in environments where wind/hydro is already stressing hardware. Build for safety and serviceability.

### Minimum protection concepts

-   **Fuse near the battery** and near other energy sources as appropriate.
-   **Disconnect** so you can stop the experiment quickly.
-   **Wire sized for current** and run length to reduce voltage drop and heating.

Use: <a href="../pages/solar-fuse-and-breaker-sizing.html" class="text-link">fuse/breaker sizing</a>, <a href="../pages/solar-wire-size.html" class="text-link">wire size guidance</a>, and <a href="../pages/wiring-decisions.html" class="text-link">wiring decisions</a>.

### Where diversion fits in a simple system

The conceptual model is:

-   **Generator charges battery** (through appropriate rectification/regulation).
-   **Diversion controller monitors battery voltage.**
-   **Dump load absorbs excess power** when voltage rises beyond a threshold.

A clean multi-source layout is described in <a href="multi-source-hybrid-charge-controller.html" class="text-link">the hybrid charge controller guide</a>.

## Heat management and mounting

A dump load is a heater. Treat it like one. You need:

-   **Non-combustible mounting** (metal enclosure or heat sink).
-   **Airflow** (vents, spacing, or forced air if needed).
-   **Physical clearance** from plastic, wood, and insulation.

### Thermal failure is a predictable failure

If your dump load is undersized or enclosed without airflow, it will overheat. If it fails open-circuit, the system may lose its safety valve at the worst time (high wind, full battery). That’s why oversizing and conservative mounting matter.

## How it pairs with solar

In a hybrid system, solar usually charges the battery through a solar charge controller. Wind/hydro sources can also charge the same battery system, but they may need diversion control as their “safety path.”

-   Solar controller handles solar charging behavior.
-   Diversion handles “what happens when the turbine has power but the battery shouldn’t take it.”
-   A clear wiring plan and measurement points keep the system debuggable.

<a href="../pages/solar-components.html" class="text-link">Solar components →</a> <a href="../pages/solar-system-sizing.html" class="text-link">Solar system sizing →</a>

## Common mistakes

-   **Undersizing the dump load** so it overheats.
-   **No ventilation** (a heater in a sealed box fails quickly).
-   **No fuse near the battery** (high current fault risk).
-   **Assuming solar controller behavior applies** to wind/hydro dynamics.
-   **Building without a stop plan** (no disconnect, no safe shutdown).

## Safety and limitations

### Burn and fire hazards

Dump loads can reach high temperatures. Treat them like a space heater: keep them away from combustible materials and plan airflow.

### High current hazards

Low-voltage systems can still produce dangerous current. Use proper fusing, wire sizing, and quality connections.

### Mechanical overspeed still matters

Diversion helps keep a turbine loaded, but you should still design a mechanical safety strategy appropriate to your turbine type. Don’t rely on any one component to prevent all failures.

## Troubleshooting

### My battery voltage rises too high in wind even with a dump load

-   The dump load may be undersized for peak conditions.
-   There may be wiring resistance between controller and dump load.
-   Confirm the controller’s setpoint and that it is actually switching current to the load.

### My dump load gets dangerously hot

-   Improve airflow and mounting to a metal heat sink or enclosure.
-   Oversize resistor bank wattage rating.
-   Verify that the controller isn’t stuck “on” due to wiring or configuration issues.

### My turbine overspeeds when the battery fills

-   That’s a sign the turbine is being unloaded; diversion should help if wired correctly.
-   Confirm diversion activation under high voltage.
-   Consider additional mechanical safety for your turbine type.

<a href="../pages/solar-output-troubleshooting.html" class="text-link">Troubleshooting mindset →</a>

## FAQ

{{< faq "Do I need a dump load for a small wind turbine?" >}}
Often, yes — especially if you plan to charge a battery and the turbine can continue producing power when the battery is full. The need depends on your turbine type, controller behavior, and how your system handles “excess power” scenarios.
{{< /faq >}}

{{< faq "Can I use a water heater element as a dump load?" >}}
Sometimes. Heating elements can handle heat by design, but you must choose an element appropriate for your system voltage and mounting. Wire and protect it as a high-power device, not as an accessory.
{{< /faq >}}

{{< faq "How do I size a dump load for 12V or 24V?" >}}
Estimate maximum plausible watts to dump, then use P = V² / R to select an effective resistance and wattage rating. Oversize thermal handling and pay attention to current (especially at 12V).
{{< /faq >}}

{{< faq "Is diversion the same as braking?" >}}
Diversion loads the generator electrically, which can slow the turbine and reduce overspeed risk. It is not always a full mechanical brake, and it’s not a substitute for safe turbine design and mounting.
{{< /faq >}}

{{< faq "What’s the safest way to start?" >}}
Start with measurement-first experiments and conservative power levels. Confirm your dump load can dissipate heat safely before relying on it as a protection device.

---

**Related guides:**
- [Multi-Source Hybrid Off-Grid Charge Controller: Combine Solar, Wind & Hydro](/diy-off-grid-energy/multi-source-hybrid-charge-controller.html)
- [DIY Small Wind Turbine for Battery Charging (Wiring + Diversion Load Control)](/diy-off-grid-energy/diy-small-wind-turbine-for-off-grid-battery-charging.html)
- [DIY Micro-Hydro Generator: Build a Run-of-River System (Sizing + Safety)](/diy-off-grid-energy/micro-hydro-basics-for-off-grid-power.html)
{{< /faq >}}

