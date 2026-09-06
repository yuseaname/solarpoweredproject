+++
title = "Arc Flash on DC Systems: Why Battery Banks Demand Respect"
slug = "solar-arc-flash-dc-safety"
date = 2026-09-06
draft = false
description = "Why a dropped wrench on a battery bank is an emergency: what a DC arc is and why it sustains, the prevention ladder (fuse at the terminal, insulated tools, one-hand rule), and NEC 690.11 arc-fault protection."
author = "Solar Powered Project"
+++

{{< affiliate-disclosure >}}

## Key takeaways

-   A dropped wrench across a live battery bank is an emergency. That bank can feed an arc at **~35,000°F (~19,400°C)** — hotter than the sun's surface — until the fault clears, the conductor melts, or the energy runs out.
-   DC arcs don't self-extinguish like AC arcs — there's no zero crossing — so a DC fault burns until something actively breaks the circuit.
-   **The fuse within 6 inches of the terminal is the single most important upgrade**: a Class T or MRBF close to the positive terminal clears a dead short before the cable jacket ignites.
-   The rest is behavior: insulated tools, no rings or watches, the one-hand rule, covered terminals, de-energizing first, and never working a big bank alone.
-   On PV wiring, NEC 690.11 requires arc-fault protection above 80V on buildings; NEC 690.12 adds rapid shutdown for firefighters. Those protect panel wiring, not the bank — the ladder below does.

## What a DC arc is, and why it keeps burning

An arc is electricity crossing a gap through ionized air. A wrench touching a positive terminal — or pulled away, or dropped across both terminals — vaporizes metal at the contact, ionizes the air into plasma, and current pours through. The tool becomes a conductor; the junction becomes a blowtorch.

Two properties of the battery make this worse than it sounds:

-   **The source current is enormous.** A 12V lead-acid starter battery can source **more than 1,000 amps** into a dead short. A large LiFePO₄ bank with 4/0 cabling can source **thousands of amps** until something melts. The energy is already in the bank, feet from where you work — nothing upstream limits it or trips.
-   **Anything metal behaves like a resistor.** The wrench is a resistor doing P = I²R. Power scales with the square of the current — double the current, quadruple the heating — so at the currents a real bank can push, even a barely measurable resistance becomes enough heat to weld, vaporize metal, and ignite what's nearby.

Molten metal and a plasma column sit right next to wire insulation and battery casing: a burn-and-fire event that develops faster than anyone can react.

## Why DC arcs are nastier than AC arcs

Household AC flips polarity 50 or 60 times a second. Every zero crossing gives the arc a chance to die — the plasma cools, the gap de-ionizes, and the fault often ends on its own. That's a real self-extinguishing mechanism, and one reason AC fault current is comparatively tame to disconnect.

DC has no zero crossing. Current flows one way, continuously, so an established arc burns until something actively breaks the circuit: a fuse with enough DC interrupt rating, a DC-rated breaker, the conductor melting through, or the stored energy gone.

The standards lag the reality. **NFPA 70E** — the workplace standard for arc-flash analysis and PPE — was built around AC calculation methods; its models and PPE categories are AC-centric, and we'll say that plainly. There's no widely agreed PPE category for a 48V bank the way there is for 480V AC work. That gap is in the standards, not your research — which is why this page gives no PPE category number for DC and leans on the ladder instead.

## The prevention ladder (in order of impact)

Apply all of it, in order: each step catches a failure mode the ones above missed. Step 1 acts in microseconds without human memory — that's why it's first.

1.  **Fuse at the source: Class T or MRBF within ~150 mm (6–8 in) of the battery positive terminal.** This marine practice (ABYC E-11) is the highest-value upgrade on any bank: a short downstream clears before the cable jacket ignites. Keep the unprotected run between terminal and fuse as short as physically possible. At high currents use a Class T (its DC interrupt rating is the point — it has to break a DC arc) or an MRBF that bolts to the terminal for tight builds. Sizing and placement: [solar fuse and breaker sizing](/pages/solar-fuse-and-breaker-sizing.html); worked example in the [48V wiring guide](/pages/48v-off-grid-wiring-guide.html).
2.  **Insulated tools.** Rated insulated wrenches, screwdrivers, and pliers near a bank; tape wrench ends you can't replace as a stopgap, not a substitute.
3.  **No rings, watches, or buckles near the bank.** Jewelry across a terminal is the dropped-wrench scenario attached to your body: a ring across 12V melts into your finger in milliseconds. Metal off before you walk up.
4.  **The one-hand rule.** Near an energized bank, keep one hand in your pocket or behind your back. Hand-to-hand contact runs across your chest — through the heart — so one hand on the work makes the worst shock path impossible.
5.  **Terminal covers and enclosed busbars.** Boot covers on posts, no bare high-current lugs in reach of a dropped tool. The goal is geometry: nowhere for a wrench to land across two potentials.
6.  **De-energize before working — or isolate the string.** Open the main disconnect, cover PV panels (live in any light), and verify 0V with a meter at your work point — don't trust switches or memory.
7.  **Sequence discipline.** Make the last connection and break the first at the fuse holder or disconnect, not at the terminal: the spark stays away from the bank and your hands.
8.  **Never work a big bank alone.** A second person with a phone who can call 911 and open the disconnect without stepping into the hazard. Burn injuries need help in minutes.

Notice what step 1 did: steps 2–8 only work when done every time — the fuse never forgets. "Is my bank fused at the terminal?" is the first question about any battery installation.

## Arc-fault protection on the PV side (NEC 690.11 and friends)

The battery hazard above is handled by fusing and behavior; the PV wiring is handled partly by code.

**NEC 690.11** requires DC arc-fault circuit-interrupter (AFCI) protection for PV circuits above 80V on buildings. Its job: detect **series arcs** — the sneaky failure mode. A series arc hides inside a degraded connection: corroded terminal, loose splice, poor crimp, sloppy connector fit. Current through it looks normal to an overcurrent device, so a fuse or breaker never trips — but the arc burns at thousands of degrees inside a junction box until it ignites what's around it. The AFCI recognizes the noise signature and breaks the circuit.

A **parallel arc** — a short between opposite-polarity conductors — draws fault current that fuses and breakers see and clear anyway. Series arcs slip past ordinary protection; that's why 690.11 exists.

Two notes in its spirit:

-   **MC4 connectors: one brand, one crimp tool, correct die.** Mixed-brand connectors are a documented arc source — dimensional tolerances differ between makers, and a poorly seated pair becomes the series arc the AFCI hunts. Stick to one brand and pull-test every connection before closing a box.
-   **Rapid shutdown (NEC 690.12)** is a separate layer for firefighters: it drops string voltage to a safe level within the array boundary once the inverter shuts down. It doesn't detect arcs — don't confuse the two.

One caveat: planning guidance, not a code substitute. Which NEC edition your jurisdiction adopts, and how your AHJ applies it, is decided locally — see [solar permits and building codes](/pages/solar-permits-and-building-codes.html). And 690.11 protects the PV side, not the bank: the fuse at the terminal stays the battery's protection.

Wiring context: [solar wire size](/pages/solar-wire-size.html), [battery cable size for inverter](/pages/battery-cable-size-for-inverter.html), and [wiring decisions](/pages/wiring-decisions.html).

## If it happens

If an arc flashes on a battery bank, do not fight it: an extinguisher can't stop an electrical arc, it can re-strike, and molten metal is spraying. The sequence:

1.  **Clear people out** — everyone away from the bank and upwind.
2.  **Open the main disconnect only if it's far from the fire and safe to reach.** If getting there means stepping toward the arc or smoke, skip it.
3.  **Evacuate and call the fire department** — say "DC battery bank arc flash / battery fire," so they know what they're walking into.
4.  **Don't re-enter for equipment.** Burns are immediate and severe; the building can wait.

Smoke, swelling, or heat from the batteries themselves — no arc — is thermal runaway: a different emergency with the same preventions, covered in [solar battery fire safety](/pages/solar-battery-fire-safety.html).

## Hazard, prevention, hardware in one table

| Hazard | Prevention | Hardware note |
| :-- | :-- | :-- |
| Dropped tool dead-shorting across terminals | Fuse at the source; terminal covers; insulated tools | Class T or MRBF within ~150 mm (6–8 in) of the positive terminal — it must interrupt DC fault current; AC-rated fuses don't belong here |
| Series arc inside a degraded connection (bank or PV side) | Torqued lugs, one-brand MC4 connectors, correct crimps | Fuses can't see series arcs; NEC 690.11 AFCI covers building PV circuits above 80V |
| Jewelry or metal across a terminal | No rings, watches, or buckles near the bank | Nothing metal on the hands — a ring across 12V melts in milliseconds |
| Sustained DC arc at a connection while working | One-hand rule; de-energize and verify 0V; make/break at the disconnect | DC-rated disconnect, not an AC switch, on the high-current path |
| Someone injured with no help to call | Never work a big bank alone | Second person plus a phone with a signal — response time is the difference-maker for burns |

## FAQ

{{< faq "Is my 12V system dangerous?" >}}
Dangerous is the wrong frame — "unforgiving" is closer. A 12V lead-acid starter battery can source more than 1,000 amps into a dead short, and even a small bank can deliver a flash that burns and ignites what's nearby. The shock hazard at 12V is minor, but the arc hazard isn't about voltage — it's about current through a short gap, and a 35,000°F arc doesn't care that the bus says 12V. So yes: the ladder applies to 12V exactly as it does to 24V and 48V. Sustained arcing gets more likely as voltage climbs, so a 48V bank earns extra respect — but that's not a reason to treat 12V as harmless.
{{< /faq >}}

{{< faq "Where exactly does the Class T fuse go?" >}}
In the positive cable, as close to the battery positive terminal as physically possible — within about 150 mm (6–8 in), the practice codified in marine ABYC E-11. The segment between terminal and fuse is the only cable the battery can feed without a fuse in the way, so keep it as short as possible. An MRBF bolts directly to the terminal itself, which solves placement on tight builds. Size the fuse at or below the cable's ampacity and at or above 125% of your maximum continuous current; the full method is in our [solar fuse and breaker sizing guide](/pages/solar-fuse-and-breaker-sizing.html).
{{< /faq >}}

{{< faq "Are arc-fault detectors required for my system?" >}}
On the PV side, yes for many installations: NEC 690.11 requires DC arc-fault circuit-interrupter protection for PV circuits above 80V on buildings, and most modern inverters include it — which NEC edition your jurisdiction adopts is an AHJ question (see [permits and building codes](/pages/solar-permits-and-building-codes.html)). On the battery side, no: arc-fault detection isn't the standard protection — the fuse at the terminal is. A BMS is a cell-protection layer, not a wiring-layer protection, and no detector replaces a correctly placed Class T or MRBF.
{{< /faq >}}

{{< faq "What's the difference between an arc flash and a battery fire?" >}}
An arc flash is an electrical event: instantaneous, with a blast and molten metal, over in a fraction of a second. A battery fire is thermal: cells heat past their decomposition point and run away over minutes, venting toxic gas and re-igniting hours later. They share the same prevention ladder — fuse at the terminal, covered terminals, insulated discipline — but responses differ: an arc flash means "clear people, isolate if safe, call," while a thermal runaway means "get out, don't breathe the smoke, call and say 'lithium-ion battery fire.'" Our [solar battery fire safety guide](/pages/solar-battery-fire-safety.html) covers the fire side in full.
{{< /faq >}}

{{< faq-schema >}}

## Next logical reads

- [Solar Installation Safety Guide](/pages/solar-installation-safety-guide.html) — the sitewide safety anchor
- [Solar Battery Fire Safety](/pages/solar-battery-fire-safety.html) — the companion page for the thermal side
- [Solar Fuse and Breaker Sizing](/pages/solar-fuse-and-breaker-sizing.html) — prevention ladder step 1, with calculator
- [48V Off-Grid Wiring Guide](/pages/48v-off-grid-wiring-guide.html) — Class T placement on a real bank
- [Solar Combiner Box and Disconnect Guide](/pages/solar-combiner-box-and-disconnect-guide.html) — isolation points and the PV side
- [Off-Grid Solar System Setup Guide](/pages/off-grid-solar-system-setup-guide.html) — where all of this fits in a build