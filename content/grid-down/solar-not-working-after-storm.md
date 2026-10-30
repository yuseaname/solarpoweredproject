+++
title = "Solar Not Working After a Storm: The Diagnosis Order That Saves the Bank"
slug = "solar-not-working-after-storm"
date = 2026-10-30
pagetype = "informational"
draft = false
description = "After a storm, solar outages are usually boring: a tripped breaker, a faulted controller, water in a connector — in that order. The 6-step multimeter diagnosis sequence, what each reading means, and what never to buy before the meter says so."
image = "/images/solar-not-working-after-storm/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
related = [
  "/pages/solar-output-troubleshooting.html",
  "/pages/solar-grounding-and-lightning-protection.html",
  "/pages/solar-battery-not-charging-troubleshooting.html",
  "/grid-down/salvaged-solar-panels.html",
  "/pages/mc4-connectors-wiring-guide.html"
]
+++

{{< affiliate-disclosure >}}

<p class="jump-links"><a href="#quick-answer" class="text-link">Quick answer</a> <a href="#safety-first-wet-electricity-deserves-respect" class="text-link">Safety first</a> <a href="#the-diagnosis-order" class="text-link">The diagnosis order</a> <a href="#the-six-checks-in-detail" class="text-link">The six checks</a> <a href="#what-lightning-actually-does-to-a-system" class="text-link">What lightning does</a> <a href="#prevention-before-the-next-storm" class="text-link">Prevention</a> <a href="#faq" class="text-link">FAQ</a></p>

## Quick answer

Post-storm solar failures are usually boring, in this order: **a tripped DC breaker or blown fuse**, **a charge controller latched in a fault state** after a surge, **water in a connector or junction box**, then — much further down — **panel damage** and **battery problems**. A multimeter and this six-step order find the overwhelming majority of causes in under an hour. The rule that saves money: **diagnose before buying** — the most expensive post-storm mistake is replacing a controller that just needs its breaker reset, or a panel that just needs its connector dried and re-seated.

## Safety first: wet electricity deserves respect

Before touching anything: if the roof or array is wet and anything smells burnt or is visibly arcing, stop — that is a job for someone qualified. Working assumptions for the rest of this page: you are probing a low-voltage DC system (12–48V bank class) with dry hands, from the ground where possible. Cover panels with an opaque blanket or cardboard before disconnecting anything — a lit panel is always a live panel ([the testing safety framing](/pages/how-to-test-solar-panel-with-multimeter.html)). And never disconnect a battery cable with a load running — spark plus hydrogen is how lead-acid banks become stories.

## The diagnosis order

Work cheapest-first, exactly in this order. Each step either finds the fault or eliminates the cheapest class of causes before you touch anything expensive:

| Order | Check | Tool | What it means |
| :-- | :-- | :-- | :-- |
| 1 | Breakers, fuses, disconnects | eyes | The #1 post-storm cause is a protection device that did its job |
| 2 | Controller state and voltages | multimeter | Surge-faulted or latched controllers mimic dead arrays |
| 3 | Battery voltage and health | multimeter | A bank dragged low makes the whole system misbehave |
| 4 | Panel Voc in daylight | multimeter | Separates panel damage from everything upstream |
| 5 | Connectors and junction boxes | eyes + meter | Water ingress corrodes quietly and kills current |
| 6 | String wiring | multimeter | The deepest check — [the full procedure](/pages/solar-output-troubleshooting.html) |

## The six checks in detail

**1. Breakers, fuses, disconnects.** Every properly built system has a DC disconnect or breaker between array and controller, and fuses on parallel strings ([what belongs where](/pages/solar-fuse-and-breaker-sizing.html)). After a storm, check each one. A tripped breaker after lightning is not a failure — it is the system working. Reset once; if it trips again immediately, stop and go to step 2 with the meter, because something downstream is genuinely faulted.

{{< product-box asin="B0B57L9FNL" name="Klein Tools MM325 Multimeter" label="The storm-aftermath tool" description="Checks 2 through 6 of the diagnosis order: battery resting voltage, controller input and output, panel open-circuit voltage, and continuity through weathered connectors. A 600V CAT III rating covers hobby-scale DC safely (per manufacturer spec). Not for: residential string-system combiner interiors — licensed-electrician territory. The honest tradeoff: no Bluetooth logging — you write the readings down, which in a diagnosis is a feature; the notebook is the record." button="Check price on Amazon" >}}

**2. Controller state.** A nearby strike induces surges that can latch a controller into a fault state without destroying it. Symptoms: error codes, dead display, or input present but no charging. The meter sequence: panel-side voltage present at the controller's PV input? Battery-side voltage present? If both read sane but charging current is zero, power-cycle the controller (disconnect PV first, then battery, wait, reconnect battery then PV — check your manual's order). If it faults again, the controller took the hit protecting the bank — that is what it was designed to do, and [the controller classes are compared here](/pages/best-mppt-charge-controllers.html) when you replace it.

**3. Battery voltage.** A storm usually means a dark day or three; the bank may simply be low, and low-voltage cutoffs make systems look dead. Measure resting voltage (nothing charging, loads off): a 12V lead-acid bank near 12.0V or a lithium bank at its BMS cutoff explains everything. Recharge gently and re-test — and if the bank sat flat through freezing weather, read [the cold-chemistry page](/pages/lifepo4-charging-below-freezing.html) before charging a lithium bank.

**4. Panel Voc.** Daylight, panels disconnected, meter on DC volts: a healthy 12V-nominal panel reads near its label Voc ([the full procedure](/pages/how-to-test-solar-panel-with-multimeter.html)). Hail or debris damage shows as healthy-looking glass but collapsed voltage — and the [salvage triage table](/grid-down/salvaged-solar-panels.html) classifies exactly what's worth keeping.

**5. Connectors and junction boxes.** Driven rain finds every connector that was never properly mated. Signs: green corrosion, water tracks, or a connector that reads voltage but delivers no current. Dry, clean, re-crimp or replace with proper [MC4 tooling and technique](/pages/mc4-connectors-wiring-guide.html), and re-seal the entry. If a string fuse blew here, replace it with the same rating — never higher:

{{< product-box asin="B08L56RDNP" name="BougeRV 15A MC4 Inline Fuse Kit (5-pk)" label="For the fuse that did its job" description="Post-storm string-fuse replacements sized to the common 100W-class parallel string (per manufacturer spec) — same rating as what blew, which is the only correct rating. Not for: the battery-side main fuse; that's a Class-T/ANL conversation. The honest tradeoff: keep the spares with the tools, because the fuse that blows is always the size you didn't pack." button="Check price on Amazon" >}}

**6. String wiring.** Last because it's deepest: the [full diagnostic](/pages/solar-output-troubleshooting.html) walks string voltage and current math per string. A single dead string in a multi-string array often changes nothing you'd notice without the meter — which is exactly why the storm is when you find it.

## What lightning actually does to a system

Direct strikes destroy whatever they hit — no residential protection survives one. What protection *does* handle is the common case: **induced surges** from nearby strikes, which ride long wires into controllers and inverters. That is why [grounding and surge protection](/pages/solar-grounding-and-lightning-protection.html) is the boring page that saves the expensive box: SPDs at the combiner and controller, short straight ground conductors, one bond point. If this storm took out a controller and the system had no surge protection, the replacement budget should include the SPD, not just the controller.

## Prevention before the next storm

In order of value: (1) [Surge protection and grounding audit](/pages/solar-grounding-and-lightning-protection.html) — one afternoon. (2) Connector mating check — every MC4 clicked to its detent, every junction box gasketed. (3) A [winterizing pass](/pages/winterizing-off-grid-system.html) before storm season covers the cold-weather failure modes. (4) Spares: one fuse kit, one spare controller if the system is your only power — the [grid-down spares thinking](/grid-down/faraday-cage-solar-electronics.html) applies to storm kits as much as anything else. And the [complete grid-down guide](/grid-down/rebuilding-power-from-scratch.html) frames all of it in one system view.

## FAQ

{{< faq "My solar stopped working after thunderstorms but nothing looks damaged. What first?" >}}
Breakers and fuses, then controller state — in that order. The majority of invisible post-storm failures are a protection device that tripped or a controller latched by a surge. Both cost nothing to check with your eyes and a multimeter, and both are fixed in minutes if that's the cause.
{{< /faq >}}

{{< faq "Can lightning ruin solar panels themselves?" >}}
Rarely the panels first — panels have no fragile microelectronics, and induced surges do their damage in controllers and inverters, which is where the wiring concentrates. Physical panel damage from storms is usually mechanical: hail, branches, debris. The Voc test in step 4 tells you which you're dealing with.
{{< /faq >}}

{{< faq "Is it safe to check my system while it's still raining?" >}}
Measure from dry ground on the low-voltage bank side if you must, but the honest answer is wait for dry — wet roofs especially. A system that survived the storm will survive the afternoon; a wet inspection mistake won't. If anything is arcing or smells burnt, that's a professional's job, full stop.
{{< /faq >}}

{{< faq "The controller display is dead but the battery reads fine. Controller or panel?" >}}
Meter the controller's PV input terminals in daylight: panel voltage present + dead display = the controller took the surge. No panel voltage = work upstream (disconnects, connectors, the panel itself). That one reading splits the whole diagnosis tree in half.
{{< /faq >}}

{{< faq "Should I just replace the charge controller to be safe after a strike?" >}}
No — test first. A controller that passes the input/output voltage checks and resumes charging after a power cycle is fine; surge damage that matters shows up in the measurements. Diagnosis before replacement is the whole point of the order above — and if it did die, that's the moment to add the surge protection it died without.
{{< /faq >}}
