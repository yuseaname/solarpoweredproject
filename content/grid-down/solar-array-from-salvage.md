+++
title = "From One Panel to a Microgrid: Wiring a Multi-Panel Solar Array From Salvage"
slug = "solar-array-from-salvage"
date = 2026-10-30
pagetype = "informational"
draft = false
description = "The scaling math for multi-panel arrays: series and parallel string arithmetic, controller voltage headroom rules with worked cold-weather examples, per-string fusing, busbars, and a 2/4/8-panel build table."
image = "/images/solar-array-from-salvage/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
related = [
  "/grid-down/rebuilding-power-from-scratch.html",
  "/grid-down/salvaged-solar-panels.html",
  "/pages/solar-panels-series-vs-parallel.html",
  "/pages/solar-combiner-box-and-disconnect-guide.html",
  "/pages/best-mppt-charge-controllers.html"
]
+++

{{< affiliate-disclosure >}}

<p class="jump-links"><a href="#quick-answer" class="text-link">Quick answer</a> <a href="#string-arithmetic" class="text-link">String arithmetic</a> <a href="#the-headroom-rule" class="text-link">The headroom rule</a> <a href="#parallel-strings-fuses-and-the-busbar" class="text-link">Fuses and busbars</a> <a href="#the-2-4-8-panel-table" class="text-link">The 2/4/8 table</a> <a href="#grounding-and-disconnects" class="text-link">Grounding and disconnects</a> <a href="#faq" class="text-link">FAQ</a></p>

## Quick answer

Scaling from one panel to many is two sums and one rule. The sums: **series adds voltage (current stays)**, **parallel adds current (voltage stays)** — [the fundamentals guide](/pages/solar-panels-series-vs-parallel.html) has the diagrams. The rule: **keep the string's cold-day open-circuit voltage at least 15% under your controller's PV input limit** — panels make *more* voltage in cold, and exceeding the limit is one of the few ways to actually destroy a controller. Match panels within strings (salvage: same current class), fuse every parallel string, and land everything on a busbar with a real disconnect. Four matched salvage panels on a 100V/30A-class controller is a ~1.6kWh/day microgrid — the working heart of a [Tier-2 system](/grid-down/rebuilding-power-from-scratch.html).

## String arithmetic

Planning numbers for the common salvage unit — a "12V nominal" 100W panel: Vmp ≈ 18V, Imp ≈ 5.5A, Voc ≈ 21V, Isc ≈ 6A (always use *your* panel's label; [how to read it](/pages/read-solar-panel-specs-sheet.html)).

- **Series string of 3:** voltages add → Vmp 54V, Voc 63V; current stays 5.5A. Power: 54 × 5.5 ≈ 300W. Voltage is high enough to keep wire losses low over a long run — [wire size math](/pages/solar-wire-size.html).
- **Parallel strings of 2:** currents add → Imp 11A at 18V. Power: ~200W at 12V-class voltage, cheaper controller class but thicker copper.
- **Series-parallel (2S2P):** two series strings (36V, 5.5A each) in parallel → 36V, 11A, ~400W. The standard layout for 4-panel builds: comfortable voltage, moderate current, and each string is separately fused.

Mismatch warning carried over from the [salvage guide](/grid-down/salvaged-solar-panels.html): within a series string, panels should share a current class (the weakest panel sets the string's current); between parallel strings, voltage classes should match. Mixed salvage works — but sort it *before* wiring, not after wondering why the harvest is low.

## The headroom rule

Controller PV limits are hard ceilings. A "100V" model means 100V of PV input, ever — not "100V at room temperature." Panel Voc *rises* as temperature falls (the coefficient is on the label, typically a small negative number per °C); a cold clear dawn is when your string hits its maximum.

Worked example, 100V-class controller (e.g., the [Victron 100/30](/pages/best-mppt-charge-controllers.html), 100V input per manufacturer spec):

- **3× in series:** 3 × 21V = 63V nominal Voc. Cold margin: 63 × 1.15 ≈ **72V** — comfortable.
- **4× in series:** 84V nominal. Cold: 84 × 1.15 ≈ **97V** — technically under 100V, but a hard-freeze morning with a worse-than-average coefficient brushes the limit. Verdict: 4S on a 100V controller is *climate-dependent*; the honest build is 2S2P instead, or step to a 150V-class controller.
- **The rule of thumb:** plan string Voc at **+15%** for cold, and stop at ~90% of the controller's limit. If the math is close, change the layout — a controller that dies takes the harvest of every panel behind it.

Current has its own ceiling: the controller's rating (20A, 30A…) applies on the *battery* side for MPPT units, so array current is bounded by array watts ÷ charging voltage — [the sizing guide works the cases](/pages/charge-controller-sizing.html).

## Parallel strings, fuses, and the busbar

Every parallel string gets its own fuse or breaker sized to the string's Isc × ~1.56 (the standard continuous-load factor) rounded to the next common size — [the fuse-sizing guide carries the table](/pages/solar-fuse-and-breaker-sizing.html). Why: in a parallel layout, a short in one string makes the *other strings* feed it — the fault current your fuse interrupts is theirs, not the sky's.

{{< product-box asin="B08L56RDNP" name="BougeRV 15A MC4 Inline Fuse Kit (5-pk)" label="Per-string protection" description="MC4 inline fuses sit at the string junction, sized to each string's short-circuit current class (per manufacturer spec) — for 100W-class parallel strings, the 15A position is the standard fit. Not for: the battery side; that's a Class-T or ANL conversation. The honest tradeoff: they're single-fuse sacrificial parts, which is exactly what a fuse should be." button="Check price on Amazon" >}}

Strings land on a busbar inside an enclosure — not twisted into a chocolate-block. A busbar gives you one labeled, torque-checked junction point per polarity, and a place the [combiner + disconnect](/pages/solar-combiner-box-and-disconnect-guide.html) architecture expects:

{{< product-box asin="B094QWG3VV" name="Blue Sea Systems 2315 100A Mini BusBar (4 Studs)" label="The array's landing zone" description="Four tinned studs rated to 100A (per manufacturer spec) take ring lugs from your strings and one feeder to the controller — labeled, inspectable, and torqueable, which is what splices-for-life are not. Not for: unprotected direct battery connections; fuse first. The honest tradeoff: costs more than a terminal strip and outlives several of them outdoors." button="Check price on Amazon" >}}

The controller itself, chosen by the headroom rule:

{{< product-box asin="B073ZJ3L13" name="Victron Energy SmartSolar MPPT 100V 30A 12/24V Solar Charge Controller with Bluetooth" label="The 4-panel default" description="100V input / 30A charging with Bluetooth harvest monitoring (per manufacturer spec) — sized for ~400W on a 12V bank or ~800W on 24V, which is exactly the 2S2P salvage build. Not for: arrays beyond those ceilings or 48V banks — the 150V line follows. The honest tradeoff: priced above budget brands; the monitoring pays for itself the first time you debug a shaded string from the couch." button="Check price on Amazon" >}}

## The 2/4/8 panel table

Daily harvest planned at 4 peak-sun-hours ([check your region](/pages/solar-panel-output.html)); battery sizing assumes LiFePO4 usable depth:

| Panels | Layout | Array | Controller class | Daily harvest | Bank that balances it |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 2 | 2S | ~200W | 100V/20A | ~800Wh | 100Ah (≈1,280Wh) |
| 4 | 2S2P | ~400W | 100V/30A | ~1.6kWh | 100–200Ah |
| 8 | 2S2P ×2 controllers, or 4S2P on 150V class | ~800W | 150V/50–60A | ~3.2kWh | 200–400Ah ([series/parallel bank math](/pages/batteries-in-series-vs-parallel.html)) |

"Balances" means the bank can absorb a full day's harvest while covering the [load budget](/pages/how-to-calculate-solar-load.html) through the next morning. Undersized bank wastes harvest; oversized bank never fills — both are expensive ways to learn arithmetic.

## Grounding and disconnects

At array scale, do the unglamorous parts properly: [grounding and lightning protection](/pages/solar-grounding-and-lightning-protection.html) (lightning is the surge you will actually meet), a real DC disconnect near the controller, and [MC4 connectors done right](/pages/mc4-connectors-wiring-guide.html). An array that can't be isolated for maintenance is an array that can't be maintained.

## FAQ

{{< faq "Can I add panels of a different wattage to my existing array?" >}}
Yes, in a new string or on a second controller — not mixed into an existing series string. Series strings share current, so a different-current panel throttles the whole string. Parallel strings need matched voltage classes. The clean answer for salvage growth: a second cheap controller for the odd panels.
{{< /faq >}}

{{< faq "Why does my array make more voltage on cold mornings?" >}}
Physics: PV voltage has a negative temperature coefficient — colder silicon holds more voltage. It's why the headroom rule plans +15% on Voc for cold snaps, and why a system that ran fine all summer can trip an over-voltage error on the first hard frost.
{{< /faq >}}

{{< faq "Do I need a combiner box for four panels?" >}}
Two parallel strings can be fused inline at the MC4 level; three or more, or anything on a roof/permanent mount, belongs in a proper combiner with a disconnect — [the guide covers when the step-up pays](/pages/solar-combiner-box-and-disconnect-guide.html). The combiner is where maintenance happens at 8am in the rain; plan for that person.
{{< /faq >}}

{{< faq "Is it better to series or parallel my panels?" >}}
Series for long wire runs (higher voltage = thinner copper) and MPPT efficiency; parallel for shade tolerance (one shaded panel kills its series string's current but only its own share in parallel) and cheap PWM controllers. Most 4-panel salvage builds land on 2S2P — moderate on both axes.
{{< /faq >}}

{{< faq "How many panels before I need 24V or 48V?" >}}
Rule of thumb: past ~400W of array or ~200Ah of bank, stepping the bank voltage doubles the controller's watt ceiling (a 30A unit does ~400W at 12V, ~800W at 24V, per the sizing math) and halves the current in your copper. The [system voltage guide](/pages/how-to-choose-solar-system-voltage.html) works the decision.
{{< /faq >}}
