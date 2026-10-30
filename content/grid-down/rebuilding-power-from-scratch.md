+++
title = "Rebuilding Power From Scratch: The Complete Grid-Down Guide"
slug = "rebuilding-power-from-scratch"
date = 2026-10-30
pagetype = "informational"
draft = false
description = "The complete framework for rebuilding electrical power when the grid is gone: the four elements every system needs, a watt-budget triage ladder for what to electrify first, and three build tiers with worked math from a $100 kit to household scale."
image = "/images/rebuilding-power-from-scratch/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
related = [
  "/grid-down/salvaged-solar-panels.html",
  "/grid-down/grid-down-communications-power.html",
  "/grid-down/solar-array-from-salvage.html",
  "/pages/solar-system-sizing.html",
  "/pages/winterizing-off-grid-system.html"
]
+++

{{< affiliate-disclosure >}}

<p class="jump-links"><a href="#quick-answer" class="text-link">Quick answer</a> <a href="#the-four-elements-every-power-system-needs" class="text-link">The four elements</a> <a href="#triage-what-to-electrify-first" class="text-link">Triage: what to electrify first</a> <a href="#the-three-build-tiers" class="text-link">The three build tiers</a> <a href="#salvage-versus-buy" class="text-link">Salvage versus buy</a> <a href="#skills-beat-stuff" class="text-link">Skills beat stuff</a> <a href="#faq" class="text-link">FAQ</a></p>

## Quick answer

Every working power system — grid-tied mansion or shoebox of salvage — needs the same four elements: a **source** (sun, wind, water, muscle), a **converter** (panel, alternator, motor-as-generator), **control** (charge controller, diversion load), and **protected storage** (a battery with fuses between it and everything else). Skip control or protection and you don't have a rugged system, you have a slow fire. Before buying anything, run the triage math below: a realistic first system is ~100W of panel, a 100Ah-class battery, one controller, and a multimeter — about **400Wh/day** of harvest at typical sun, which keeps lights, phones, and radios alive indefinitely.

## The four elements every power system needs

Attaching random wires to random components is not improvisation; it is an efficient way to destroy scarce equipment. The framework:

1. **Source.** Sun is the highest-reliability watts-per-effort after a disaster: a panel has no moving parts and typical degradation is well under 1% per year. Wind needs site quality most backyards lack; water needs head and flow; muscle is the universal fallback ([hand-crank sustains 5–30W](/diy-off-grid-energy/diy-hand-crank-generator-emergency-charging.html), [pedal power 50–150W](/diy-off-grid-energy/pedal-power-generator-for-off-grid-battery-charging.html) — figures from our Project Lab physics guides).
2. **Conversion.** Photovoltaic panels convert directly. Mechanical sources need a generator: car alternators, treadmill motors, and wheel-driven alternators all work with honest tradeoffs — see the [Project Lab](/diy-off-grid-energy.html) reality checks before believing any nameplate number.
3. **Control.** A charge controller is not optional. A "12V" panel has an open-circuit voltage near 21V; connected straight to a 12V battery it will push the battery far past safe charging voltage — boiling a lead-acid bank or plating a lithium one. The [MPPT controller guide](/pages/best-mppt-charge-controllers.html) covers the classes; wind and hydro additionally need a [diversion (dump) load](/diy-off-grid-energy/diy-dump-load-diversion-controller-wind-hydro.html) so the generator always has an electrical load.
4. **Protected storage.** Battery, fuse, disconnect, correctly sized wire — in that order of importance. Our [fuse and breaker sizing](/pages/solar-fuse-and-breaker-sizing.html) and [wire size](/pages/solar-wire-size.html) guides carry the tables. An unfused battery bank is the single most dangerous object in an improvised system.

## Triage: what to electrify first

Scarce watt-hours force an order of operations. Work down this ladder — each rung must be sustainable before the next matters:

| Priority | Load | Honest daily budget | The math that decides it |
| :-- | :-- | :-- | :-- |
| 1 | Lighting (LED) | 15–25Wh | 3–5W per headlamp × 4–6 hours |
| 2 | Communications | ~40Wh | Phones, radios, weather alerts — [full budget here](/grid-down/grid-down-communications-power.html) |
| 3 | Medical devices | 240–700Wh/night | [CPAP runs 30–60W; a humidifier doubles it](/pages/cpap-battery-backup-guide.html) — this jumps the queue if it applies to you |
| 4 | Refrigeration | 700–1,100Wh | [An ENERGY STAR chest freezer draws 0.7–1.1kWh/day](/pages/what-size-battery-run-chest-freezer.html); a 100Ah 12V LiFePO4 (~1,280Wh) runs one about a day |
| 5 | Water | varies | Most deep-well pumps need 240V — [the voltage problem explained](/pages/solar-generator-well-pump-sizing.html); plan a 120V jet-pump alternative or stored water first |

The pattern: **the ladder is cheap at the top and expensive at the bottom.** Tiers 1–2 together cost about 60Wh/day — one 100W panel harvests 6–8× that on an average day. Tier 4 is where budgets get serious.

<figure>
<img src="/images/rebuilding-power-from-scratch/fig-triage.webp" loading="lazy" width="640" height="427" alt="Technical-plate illustration: a five-shelf priority ladder from lantern to water pump, each shelf tied to a progressively larger battery." />
<figcaption>The triage ladder: each rung down costs roughly an order of magnitude more energy than the one above — plan top-down, never bottom-up. (Illustrative)</figcaption>
</figure>

## The three build tiers

Planning math: harvest/day ≈ panel watts × peak-sun-hours (4 is a common planning figure; [check your region's real number](/pages/solar-panel-output.html)). Every figure below is arithmetic, not a promise — sun varies.

**Tier 1 — The essentials kit (~US$100–180).** One 100W panel, a small 20–30A controller, a modest battery (even a 35–50Ah AGM), and a multimeter. Harvest: ~400Wh/day. Runs the entire top of the triage ladder forever. Bundled 100W starter kits (panel + controller) usually cost less than the parts separately — and [choosing your system voltage](/pages/how-to-choose-solar-system-voltage.html) first keeps later expansion cheap.

{{< product-box asin="B0B57L9FNL" name="Klein Tools MM325 Multimeter" label="The first tool of grid-down work" description="Rebuilding power is measuring power: battery voltage before you connect, panel open-circuit voltage before you trust it, and current draw before you commit storage. A 600V CAT III rating covers hobby-scale DC safely (per manufacturer spec). Not for: mains or high-voltage string work. The honest tradeoff: manual ranging means you set the scale — which is also why it survives a tool bag that nothing digital should." button="Check price on Amazon" >}}

**Tier 2 — The household essentials (~US$900–1,300).** 400W of panel, a 100V/30A-class MPPT controller (~400W array ceiling on a 12V bank, per manufacturer spec), a [12V 100Ah LiFePO4 bank (~1,280Wh)](/pages/how-long-will-100ah-battery-run.html), and a small pure-sine inverter sized to your single biggest load — [sizing method here](/pages/how-to-choose-solar-inverter.html). Harvest: ~1.6kWh/day. Covers lights, comms, refrigeration-by-day, and tool charging with margin. Wire it per the [array guide](/grid-down/solar-array-from-salvage.html).

{{< product-box asin="B073ZJ3L13" name="Victron Energy SmartSolar MPPT 100V 30A 12/24V Solar Charge Controller with Bluetooth" label="The Tier-2 control element" description="The 100V/30A model most 300–400W builds converge on (per manufacturer spec): Bluetooth monitoring, lithium profiles, temperature compensation. Not for: arrays above ~400W on 12V — that's 150V-class territory. The honest tradeoff: you pay for the brand floor; the budget class does the same chemistry of charging for less, with a weaker track record." button="Check price on Amazon" >}}

**Tier 3 — The household system (~US$3,500–5,000+).** 800W+ of array, 200Ah+ of storage or an [expandable power station class](/pages/jackery-vs-ecoflow-power-stations.html) (1,024–1,152Wh units that accept extra batteries, per manufacturer specs), 240V capability if a well pump is in scope (the [DELTA Pro 3 class](/pages/solar-generator-well-pump-sizing.html)), and proper [combiner + disconnect](/pages/solar-combiner-box-and-disconnect-guide.html). At this scale the [full system-sizing guide](/pages/solar-system-sizing.html) takes over — the grid-down version of Tier 3 is just a well-engineered off-grid system with a hardening pass.

<figure>
<img src="/images/rebuilding-power-from-scratch/fig-tiers.webp" loading="lazy" width="640" height="427" alt="Technical-plate illustration: three workbenches with progressively larger solar systems from one panel to a large array with battery bank and power station." />
<figcaption>Three build tiers, one bench apart: from a single panel and a meter to an array, bank, and station — all sized by the same arithmetic. (Illustrative)</figcaption>
</figure>

{{< product-box asin="B084DB36KW" name="LiTime 12V 100Ah LiFePO4 Battery, 100A BMS, Group 31" label="The storage element, sized honestly" description="1,280Wh of nameplate storage, ~960Wh+ usable depth on lithium chemistry, 100A BMS. Not for: charging below freezing without the self-heating variant — [the cold-chemistry physics here](/pages/lifepo4-charging-below-freezing.html). The honest tradeoff: LiFePO4 costs more than AGM upfront and repays it in cycle life and usable depth." button="Check price on Amazon" >}}

## Salvage versus buy

After a real disaster, new supply chains are the first thing to break and the last thing to return. The decision rule:

- **Salvage first** for: panels (they outlive the buildings under them), copper wire, connectors, breakers, enclosures, and structural steel. The [salvage testing guide](/grid-down/salvaged-solar-panels.html) shows the two measurements that separate keepers from boat anchors.
- **Buy new** for: charge controllers, inverters, and battery chemistry you can't verify. A controller that fails short takes the bank with it; a salvaged lithium battery with unknown history is a fire you haven't met yet.
- **Never improvise**: the controller (unregulated charging) and the fuse (unprotected storage). Those two are where "resourceful" becomes "statistics."

## Skills beat stuff

A settlement can possess panels, batteries, and kilometers of wire and still produce nothing safe. The skills layer, in learning order: (1) [measure a panel](/pages/how-to-test-solar-panel-with-multimeter.html), (2) [size a fuse and wire](/pages/solar-wire-size.html), (3) [calculate a daily load budget](/pages/how-to-calculate-solar-load.html), (4) [diagnose a silent system](/pages/solar-battery-not-charging-troubleshooting.html), (5) [keep a bank alive through winter](/pages/winterizing-off-grid-system.html). At least two people should know every critical system — knowledge concentrated in one person is a single point of failure. Learn now, while replacement parts and patient instructors still exist. Build small, measure everything, and scale what the numbers approve.

## FAQ

{{< faq "How much solar do I actually need to 'survive'?" >}}
Far less than instinct says and more than marketing says. The top of the triage ladder — lights, phones, radios, a weather radio — is roughly 60Wh/day. One 100W panel averages 300–500Wh/day depending on season and latitude. "Surviving" on solar is cheap; recreating a normal household (refrigeration, well pump, laundry) is Tier 3 money. Run the load math before buying anything.
{{< /faq >}}

{{< faq "Can I just connect a solar panel straight to a battery in an emergency?" >}}
As a truly temporary measure with constant supervision it can charge a battery — but panel voltage far exceeds safe charging voltage, and unattended it will overcharge, damaging lead-acid by gassing and lithium more permanently. The controller exists precisely to prevent this. Treat controller-less charging like open-flame cooking indoors: possible, watched, and never the plan.
{{< /faq >}}

{{< faq "Are power stations a substitute for building a system?" >}}
They are Tier 1–2 storage with the control element built in, at a price premium per watt-hour. A 1kWh-class station plus a folding panel is a legitimate essentials kit — our [Jackery vs EcoFlow comparison](/pages/jackery-vs-ecoflow-power-stations.html) covers the spec differences. For Tier 3 scale, component systems win on cost per Wh and repairability.
{{< /faq >}}

{{< faq "What about wind or pedal power instead of solar?" >}}
Muscle and wind are real but small: hand-crank sustains 5–30W, pedal 50–150W, and backyard wind usually underperforms its rating because of turbulence. They're the backup layers, not the base — the physics is in the Project Lab guides linked above.
{{< /faq >}}

{{< faq "Should I harden electronics against EMP?" >}}
Understand the threat physics first: everyday lightning and surges damage far more solar electronics than exotic pulses. Start with [grounding and surge protection](/pages/solar-grounding-and-lightning-protection.html); the [Faraday cage guide](/grid-down/faraday-cage-solar-electronics.html) covers what a cage actually does and how to test one honestly.
{{< /faq >}}
