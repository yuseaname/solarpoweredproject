+++
title = "Inverter Cable Size Chart: 12V/24V/48V Wire Gauges by Wattage"
slug = "inverter-cable-size-chart"
date = 2026-09-05
draft = false
description = "Inverter cable size chart for 12V, 24V and 48V systems: amps by wattage, minimum wire gauge, 10-foot run upsizing, and DC fuse sizing with honest math."
author = "Solar Powered Project"
related = [
  "/pages/battery-cable-size-for-inverter.html",
  "/pages/solar-fuse-and-breaker-sizing.html",
  "/pages/solar-wire-size.html",
  "/pages/12v-vs-24v-vs-48v-solar.html"
]
+++

{{< affiliate-disclosure >}}

## Quick answer

Find your inverter's continuous watts in the left column and your battery voltage across the top — the cell gives you the minimum copper cable gauge for a short run (under ~5 ft one-way). Longer runs go one size thicker, and every row includes the fuse size that protects it. The full decision math (run length, voltage drop targets, termination checklist) lives in the [battery cable size guide](/pages/battery-cable-size-for-inverter.html), which also has an interactive calculator.

## Key takeaways

-   **Amps = watts ÷ volts.** That single division drives every cell in the chart — a 2,000W inverter pulls ~167A at 12V but only ~42A at 48V.
-   **The gauge ladder:** 10 AWG covers ~25A, 8 AWG ~45A, 4 AWG ~85A, 2/0 ~130A, 4/0 ~175A (short-run planning values; longer runs step up).
-   **The fuse protects the wire, not the inverter** — size it at amps × 1.25, at or below the cable's rating, and use a DC-rated device (Class T or MRBF above ~150A).
-   **Above ~175A, stop upsizing wire:** parallel 2/0 feeds or move the system to 48V.

## How to read this chart

Use the inverter's **continuous** rating, not its surge rating — surge is brief and the inverter's job to ride through. Read the minimum gauge, then adjust: if your one-way run is over 5 ft, go one size thicker; if you want to verify a specific run, the [cable-size calculator](/pages/battery-cable-size-for-inverter.html) computes the exact voltage drop. Cells marked "go 48V" mean amps exceed what a single 4/0 cable should carry — that's a system-voltage decision, not a cable decision ([why](/pages/12v-vs-24v-vs-48v-solar.html)).

## The chart: watts × volts → amps → minimum gauge

Planning values: copper cable, ~85% inverter efficiency headroom ignored on purpose (watts ÷ volts is the conservative planning division the cable guide uses).

| Inverter | 12V amps → gauge | 24V amps → gauge | 48V amps → gauge |
| :-- | :-- | :-- | :-- |
| 300W | 25A → **10 AWG** | 13A → 10 AWG | 7A → 10 AWG |
| 500W | 42A → **8 AWG** | 21A → 10 AWG | 11A → 10 AWG |
| 750W | 63A → **4 AWG** | 31A → 8 AWG | 16A → 10 AWG |
| 1,000W | 83A → **4 AWG** | 42A → **8 AWG** | 21A → 10 AWG |
| 1,500W | 125A → **2/0 AWG** | 63A → **4 AWG** | 31A → 8 AWG |
| 2,000W | 167A → **4/0 AWG** | 83A → **4 AWG** | 42A → **8 AWG** |
| 2,500W | 208A → **go 48V** | 104A → **2/0 AWG** | 52A → **6 AWG** |
| 3,000W | 250A → **go 48V** | 125A → **2/0 AWG** | 63A → **4 AWG** |
| 4,000W | — | 167A → **4/0 AWG** | 83A → **4 AWG** |
| 5,000W | — | 208A → **go 48V** | 104A → **2/0 AWG** |
| 6,000W | — | 250A → **go 48V** | 125A → **2/0 AWG** |

Gauges between the ladder steps (6 AWG, 2 AWG, 1/0) exist — the bold cells are the common "battery cable kit" sizes, which is what most people actually buy.

## Fuse and breaker size for each row

Fuse or breaker = amps × 1.25, rounded up to the next standard size, and never above the cable's ampacity. Standard sizes: 30, 40, 50, 60, 80, 100, 125, 150, 175, 200, 250, 300A.

| Inverter | 12V fuse | 24V fuse | 48V fuse |
| :-- | :-- | :-- | :-- |
| 300W | 40A | 20A | 15A |
| 500W | 60A | 30A | 15A |
| 1,000W | 110A | 60A | 30A |
| 1,500W | 175A | 80A | 40A |
| 2,000W | 250A | 110A | 60A |
| 3,000W | 300A+ (Class T) | 175A | 80A |
| 4,000W | — | 250A (Class T) | 110A |
| 6,000W | — | — | 175A |

Above ~150A, a **Class T fuse or an MRBF** is the right hardware — the interrupt rating at battery fault currents is what matters, not just amps. The full placement and DC-rating rules: [solar fuse and breaker sizing](/pages/solar-fuse-and-breaker-sizing.html).

## Surge: why the chart uses continuous watts

Motor starts can briefly pull 2–4× continuous watts. Cables are sized to **continuous** current (heat builds over minutes, not milliseconds); the inverter's surge rating exists to carry the seconds-long spike. If your load trips the inverter on surge, the fixes are a bigger inverter or a soft-start device on the load — never thinner-safety-margin wiring. Sizing the inverter itself (continuous vs surge math): [inverter sizing guide](/pages/solar-inverter-sizing.html).

## Voltage drop: the one worked example you should run

The chart's gauges assume a short run. Here's why longer runs hurt, in one calculation — a 1,000W/12V inverter (83A) on 10 ft one-way of 4 AWG (0.25 Ω per 1,000 ft):

**Drop = 2 × 10 ft × 83A × 0.25 ÷ 1,000 = 0.42V ≈ 3.5% of 12V**

That's over the 3% planning target — so on that run you'd step up to 2 AWG. Voltage drop is also the hidden cause of many "inverter keeps shutting off" mysteries: the battery reads fine at rest, but under load the inverter sees battery-minus-cable-drop. ([The shutdown checklist](/pages/inverter-keeps-shutting-off-troubleshooting.html) walks that diagnosis.)

## Lugs, heat-shrink, torque, and corrosion

The cable is only half the circuit — lugs and terminations cause more failures than copper:

-   **Lugs:** correctly sized copper ring lugs, crimped with a proper tool (hammer crimps are a last resort), matched to the stud size.
-   **Heat-shrink** over every lug joint: insulation plus corrosion seal.
-   **Torque** terminal bolts to the inverter manual's spec and re-check after the first month — vibration works copper connections loose.
-   **Anti-corrosion paste** on battery terminals; inspect for heat-discolored insulation at every service.

## FAQ

{{< faq "Can I use welding cable for inverter connections?" >}}
Yes — fine-stranded welding cable (pure copper, 2 AWG–4/0) is a popular and appropriate choice for battery-to-inverter runs, as long as lugs are crimped correctly. What matters is copper cross-section and terminations, not the marketing label.
{{< /faq >}}
{{< faq "What happens if my cable is one size too small?" >}}
Under full load the inverter sees lower voltage than the battery supplies: alarms, early low-voltage shutdowns, and reduced surge capacity. The cable also runs warm. One size down rarely fails instantly — it fails as mysterious shutdowns and heat-damaged insulation over months.
{{< /faq >}}
{{< faq "Why does my 2,000W inverter say to use 2/0 when the chart says 4/0?" >}}
Manufacturer tables assume specific insulation temperature ratings and derating factors. When the manual and any chart disagree, follow the manual — it reflects that exact product's testing. Charts like this one are for planning before you've picked the unit.
{{< /faq >}}
{{< faq "Do I fuse both the positive and negative cable?" >}}
Normally one fuse, on the positive, as close to the battery as practical. Fusing the negative is only considered in specific marine/metal-chassis situations — follow your system's wiring standard or an installer's advice.
{{< /faq >}}
{{< faq "Is 4 AWG enough for a 1,000W inverter on a 15-foot run?" >}}
Ampacity-wise yes, but at 83A over 15 ft one-way, 4 AWG drops about 0.62V (5%+) — too much. Step up to 2/0, shorten the run, or (better) reconsider 24V. Run the exact numbers in the [cable-size calculator](/pages/battery-cable-size-for-inverter.html).
{{< /faq >}}

## Next logical reads

<a href="battery-cable-size-for-inverter.html" class="text-link">Battery cable size guide + calculator</a> <a href="solar-fuse-and-breaker-sizing.html" class="text-link">Fuse and breaker sizing</a> <a href="solar-wire-size.html" class="text-link">Solar wire size (PV circuits)</a> <a href="12v-vs-24v-vs-48v-solar.html" class="text-link">12V vs 24V vs 48V systems</a> <a href="/pages/48v-off-grid-wiring-guide.html" class="text-link">48V off-grid wiring guide</a>