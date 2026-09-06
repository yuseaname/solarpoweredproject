+++

title = "Solar Glossary: Every Term in Plain English"
slug = "solar-glossary"
date = 2026-09-05
draft = false
description = "Look up any solar term before you buy or build: ~50 plain-English definitions, each with the number or rule that decides your design."
image = "/images/solar-glossary/hero.webp"
image_width = 1536
image_height = 1024
author = "Solar Powered Project"
related = [
  "/pages/solar-basics.html",
  "/pages/solar-system-sizing.html",
  "/pages/wiring-decisions.html"
]
+++

{{< affiliate-disclosure >}}

Solar gear is full of abbreviations, and sellers use them loosely. This glossary is version 1 of the plain-English reference for every term that actually matters on this site — each entry is a short definition plus the number or rule that turns the term into a decision. We add and refine entries quarterly as the guides grow. The definitions are standard electrical and solar physics, so what you read here should match the datasheet, the code book, and the other pages on this site — where a term belongs to a deeper guide, the link is right there.

## The five terms that decide your build

-   **Voc** — the highest voltage your array can ever present, so it decides whether your charge controller survives a cold, sunny morning.
-   **Vmp** — the voltage at which panels actually make their rated power, so it decides whether your controller's MPPT window fits.
-   **Isc** — the worst-case current a panel can push, so it decides string fuse size (1.56 x Isc) and wire ampacity.
-   **Usable Wh** — the energy you can actually draw from the battery after depth of discharge, so it decides how long your loads run.
-   **DoD** — the discharge depth you design around, so it decides how big the battery has to be in the first place.

## A–Z glossary

### Amp-hours (Ah)

A measure of battery charge: the current a battery can supply for one hour — a 100Ah battery holds 100 amps for one hour or 10 amps for ten. But it is a unit of charge, not energy: multiply by nominal voltage (100Ah x 12V = 1,200Wh) before comparing batteries honestly. The [battery capacity calculator](/pages/battery-capacity.html) works in this unit.

### Ampacity

The maximum continuous current a wire can safely carry, set by its gauge, insulation, and temperature. Planning rules of thumb for short copper runs: 10 AWG about 30A, 6 AWG about 65A, 4/0 AWG about 175A. The fuse on a circuit must be rated below the wire's ampacity — the fuse protects the wire, never the other way around. See the [solar wire size page](/pages/solar-wire-size.html) and the [wiring decisions hub](/pages/wiring-decisions.html).

### AWG

American Wire Gauge — the sizing system for wire, where a bigger number means a thinner wire. 14 AWG is thinner than 10 AWG, and each step changes cross-section by about 26%. This site plans with a conservative ladder: 10 AWG for ~30A branch runs up to 4/0 AWG for ~175A battery runs. The full ladder lives on the [solar wire size page](/pages/solar-wire-size.html).

### Azimuth

The compass direction your panels face. In the northern hemisphere, due south (180) captures the most annual sun; facing east or west shifts production toward morning or evening instead. Tilting the azimuth 30-45 degrees off south typically costs 5-15% of annual output. The [tilt and orientation guide](/pages/solar-panel-tilt-and-orientation.html) works through the trade-offs.

### Balance of system (BOS)

Everything that is not the panels, inverter, or battery: wire, fuses, breakers, disconnects, racking, and monitoring. On installed quotes, BOS plus labor and soft costs often make up half or more of the total. It is also where most real failures start; the [system cost breakdown](/pages/solar-system-costs.html) shows where the money lands and the [components guide](/pages/solar-components.html) treats it as a job of its own.

### Battery management system (BMS)

The protection circuit inside a lithium battery that guards the cells: it disconnects on overvoltage, undervoltage, overcurrent, and — on good packs — low temperature. Its continuous discharge rating is a hard limit — a 100A BMS will not start a load that surges past it — so check that rating and the low-temp cutoff before buying. The [BMS explainer](/pages/solar-battery-management-system-explained.html) goes deeper.

### Branch fuse

The fuse protecting a single wire run — typically from the array to the controller, or from the battery bus to a load. Its job is to clear before the wire becomes the failure point when a fault dumps current into that run. For PV branch circuits the sizing convention is short-circuit current x 1.56 per NEC 690.8. The [fuse and breaker sizing guide](/pages/solar-fuse-and-breaker-sizing.html) has the decision rule; [fuses vs breakers](/pages/solar-fuses-vs-breakers.html) compares device types.

### Bulk / absorption / float

The three charging stages: bulk pushes maximum current until the bank reaches target voltage, absorption holds that voltage while current tapers, and float keeps a full bank topped up. For a 12V bank, absorption targets run about 14.4-14.8V flooded, 14.2-14.4V AGM, and 14.2-14.6V LiFePO4. The taper in absorption and float can look like "not charging" — see the [not-charging troubleshooting guide](/pages/solar-battery-not-charging-troubleshooting.html) and the [lithium vs lead-acid comparison](/pages/li-ion-vs-lead-acid.html).

### C-rate

How fast a battery is charged or discharged relative to its capacity: 1C means full capacity in one hour, 0.5C means in two. A 100Ah battery at 0.5C delivers 50A. Spec sheets quote capacity "at 0.2C" for a reason — at higher rates the real delivered capacity shrinks — so the [100Ah brand comparison](/pages/lifepo4-100ah-brand-comparison.html) treats the C-rate as part of the spec.

### Charge controller (MPPT/PWM)

The device between panels and battery that manages charging. MPPT converts surplus panel voltage into extra charge current — a meaningful 15-35% gain in cool conditions when panel voltage runs well above battery voltage; PWM just connects the panel to the battery and discards the difference. The number that matters is the controller's max input voltage against your cold-adjusted array Voc — the [MPPT vs PWM comparison](/pages/mppt-vs-pwm.html) shows the worked math, and [controller sizing](/pages/charge-controller-sizing.html) picks the unit.

### Cold-weather Voc rise

Panel voltage rises as cells get cold, and the label Voc is rated at 25C. At about -20C a typical panel's Voc runs roughly 10-12% above its 25C rating — exactly when the array is cold, sunlit, and unloaded. Size the controller for string Voc at your record-low temperature, with margin: the [controller sizing page](/pages/charge-controller-sizing.html) runs this exact check and the [not-charging checklist](/pages/mppt-charge-controller-not-charging.html) treats it as an error source.

### Cycle life

The number of charge/discharge cycles a battery is rated to deliver before capacity falls to a defined floor, usually 80%. LiFePO4 typically rates 4,000-6,000 cycles; lead-acid runs roughly 500-1,500 depending on type. Cycle life only means something at the stated depth of discharge — deeper cycling shortens it. The [lithium vs lead-acid](/pages/li-ion-vs-lead-acid.html) comparison prices batteries on exactly this basis.

### DC-DC charger

A device that charges a house or auxiliary battery from a vehicle alternator or another DC source, at the correct voltage and current profile. In an RV converting to a lithium house bank, it is the required part between the alternator and the lithium battery — a direct connection can push starter current into a bank that does not want it. It also stops the house bank from draining back into a flat starter battery. The [lithium conversion guide](/pages/li-ion-vs-lead-acid.html) calls this out explicitly.

### Depth of discharge (DoD)

How much of a battery's capacity you draw before recharging, expressed as a percentage. Design around ~50% for lead-acid and ~80–90% for LiFePO4 — those bands are what keep each chemistry alive. The rule: usable Wh equals nameplate Wh times usable DoD, so a "100Ah" battery is only as big as the DoD you are willing to cycle at. The [battery capacity calculator](/pages/battery-capacity.html) applies this automatically, and the [lithium vs lead-acid comparison](/pages/li-ion-vs-lead-acid.html) shows why the DoD gap decides the chemistry.

### Derating

Reducing an equipment or wire rating to account for real conditions — heat, altitude, conduit fill, or continuous duty. Solar planning typically derates panel output by 0.75-0.85 to convert nameplate watts into real daily watt-hours. The [panel output guide](/pages/solar-panel-output.html) uses an 0.80 system-efficiency factor, and code work derates wires from NEC 310.15.

### Disconnect

A switch that isolates a circuit so work can be done safely. Every source deserves one: between array and controller, battery and inverter, and (for grid-tied systems) a utility-accessible AC disconnect. The number that matters is the DC-rated voltage and current — AC-rated switches are not safe on PV circuits. The [combiner box and disconnect guide](/pages/solar-combiner-box-and-disconnect-guide.html) covers placement and sizing.

### Efficiency (panel vs system)

Panel efficiency is the percentage of incoming sunlight converted to DC power at standard test conditions — residential panels run about 19-23%. System efficiency is the whole chain: panels, wiring, controller, inverter, and battery, which cuts real output to roughly 75-85% of nameplate. Don't let one number stand in for the other. The [panel efficiency guide](/pages/solar-panel-efficiency.html) explains both and the [panel output page](/pages/solar-panel-output.html) applies the system number.

### Equalization

A deliberate, controlled overcharge of a flooded lead-acid battery that rebalances cells and breaks up sulfate crystals — typically 15.0-15.5V with loads removed and the enclosure ventilated. Flooded batteries need it every 1-3 months in solar service but forbidden on sealed batteries and on lithium: overvoltage vents the case or damages cells. The [battery maintenance guide](/pages/solar-battery-maintenance-guide.html) has the full procedure.

### Grid-tied vs off-grid vs hybrid

The three system architectures: grid-tied exports and imports from the utility (cheapest, but it shuts down in an outage), off-grid supplies everything from panels and battery (most expensive per kWh, fully self-sufficient), hybrid adds battery backup to a grid-tied system for backed-up circuits. The number that separates them is outage behavior, and it drives the design. The [basics guide](/pages/solar-basics.html) compares all three.

### Ground fault

An unintended current path from a live conductor to ground. Solar arrays are vulnerable to it through damaged insulation, water intrusion, or failed connectors (arcing to ground). NEC 690.41 requires ground-fault protection on grounded PV arrays above 50V; a controller throwing a ground-fault error code points at damaged wiring. The [installation safety guide](/pages/solar-installation-safety-guide.html) covers prevention and response.

### Inverter (pure vs modified sine; string vs micro)

The device that converts DC to AC for household use. Pure sine wave matches utility power quality and is required for sensitive electronics, while modified sine is cheaper and adequate for resistive loads — about 20-30% less efficient on some motor loads. "String" means one inverter for the whole array; "micro" means one small inverter per panel, which handles shading and rapid shutdown panel-by-panel. Both choices are compared on the [pure vs modified sine](/pages/pure-sine-vs-modified-sine-inverter.html) and [micro vs string](/pages/micro-vs-string-inverters.html) pages.

### Irradiance

The intensity of sunlight hitting a surface, measured in watts per square meter (W/m2). Panel ratings assume 1,000 W/m2, so irradiance is the input that turns panel watts into output. The practical consequence: morning, dusk, clouds, and winter angles all deliver less than the rating. See the [how do solar panels work](/pages/how-do-solar-panels-work.html) explainer and the [panel output guide](/pages/solar-panel-output.html).

### Isc

Short-circuit current — the maximum current a panel pushes when its terminals are connected directly together, roughly 10-20% above its operating current. It exists to size wire and fuses: the standard for PV circuit protection is 1.56 x Isc per NEC 690.8. You also need it to check the [string fuse sizing](/pages/solar-fuse-and-breaker-sizing.html) math.

### kWh vs Wh

Wh (watt-hours) is energy: power in watts times time in hours. A kilowatt-hour is simply 1,000 watt-hours. The unit matters because panels and batteries are sized in Wh/day and kWh, while loads are rated in watts — mixing them is the classic sizing mistake. The [load calculation guide](/pages/how-to-calculate-solar-load.html) keeps the two straight with worked examples.

### LiFePO4 vs NMC

The two lithium chemistries you will meet. LiFePO4 (LFP) has a flatter voltage curve, longer cycle life (4,000-6,000 cycles), lower energy density, and no thermal runaway in normal abuse — the default for solar banks. NMC packs more energy per kilogram and charges fast, which suits consumer power stations, but ages faster and is less tolerant of deep cycles. The [lithium vs lead-acid](/pages/li-ion-vs-lead-acid.html) page covers LFP in depth.

### Load

Everything that draws power from your system — lights, fridge, pumps, electronics. Loads are measured two ways: watts (peak draw, which sizes the inverter) and watt-hours per day (energy, which sizes panels and battery). Write the load list before buying anything; it is step one of every sizing guide. The [load calculation guide](/pages/how-to-calculate-solar-load.html) walks the full method.

### MC4

The standard locking connector used on solar panel cables. Its job is a weatherproof, tool-free connection — and its failure mode is a slightly loose pair that arcs, corrodes, and sags voltage under load. Two rules: use one brand and one proper crimp tool for all connectors, and never unplug MC4s while current is flowing. The [arc-flash safety guide](/pages/solar-arc-flash-dc-safety.html) explains why.

### Maximum fuse rating

The largest fuse or breaker a device's terminals or internal bus allow, printed on the label. It is a hard limit — exceeding it voids the rating and can turn a fault into a fire. String the fusing chain as: fuse below wire ampacity, and at or below the device's maximum fuse rating. The [fuse and breaker sizing guide](/pages/solar-fuse-and-breaker-sizing.html) orders the whole chain.

### MPPT / PWM

The two charge-controller technologies, tracked from the "charge controller" entry above. MPPT (maximum power point tracking) holds the panel at its best voltage and converts the surplus into charge current; PWM (pulse width modulation) simply switches the panel on and off to hold battery voltage. The rule that matters: MPPT earns its keep when panel voltage runs well above battery voltage (typically 15-35% extra harvest in cool conditions), while PWM is fine for a small 12V system with a "12V" panel. The [MPPT vs PWM comparison](/pages/mppt-vs-pwm.html) shows the worked math.

### MPPT charge controller sizing

The input-voltage window and current rating that decide which controller fits your array — the practical follow-through of the Voc and Vmp checks above. The rule: cold-adjusted string Voc must stay under the controller's max input voltage with margin, while string Vmp should sit above the battery charge voltage. The [controller sizing guide](/pages/charge-controller-sizing.html) picks the unit from your array numbers.

### Net metering

A utility billing arrangement that credits exported solar power against what you draw, usually at or near the retail rate. The credit rate is the number that decides payback: full-retail states keep solar economics simple, while avoided-cost states (California under NEM 3.0) push you toward batteries and self-consumption. See the [net metering explainer](/pages/solar-net-metering-explained.html) and the [state-by-state guide](/pages/net-metering-by-state-2026.html).

### Nominal voltage (12V / 24V / 48V)

The labeled battery-bank voltage class — 12.8V, 25.6V, or 51.2V in practice for lithium — that everything downstream matches: inverters, chargers, and wire. Higher voltage halves or quarters current for the same power, which shrinks wire size and voltage drop; 12V is simplest for small builds, 48V is the norm for whole-home. The [12V vs 24V vs 48V guide](/pages/12v-vs-24v-vs-48v-solar.html) has the selection logic and the [voltage choice page](/pages/how-to-choose-solar-system-voltage.html) as well.

### Overcurrent protection

Fuses and breakers, collectively: devices that open a circuit before current exceeds what the wire or device can take. Every source of fault current gets its own protection, sized to the wire it feeds — the rule the entire [wiring decisions hub](/pages/wiring-decisions.html) hangs on. The [fuses vs breakers](/pages/solar-fuses-vs-breakers.html) page compares the device classes.

### Panel efficiency

The percentage of sunlight a panel converts to DC power at standard test conditions (1,000 W/m2, 25C cell). Residential panels range roughly 19-23%, and the gap translates directly into roof area per watt — a 22% panel needs about 15% less roof than a 19% one. Higher efficiency matters most on small roofs; the [panel efficiency guide](/pages/solar-panel-efficiency.html) explains when it is worth paying for.

### Parallel vs series

The two ways to connect panels. Series adds voltage at the same current (a 2S string of 12V panels makes ~36-44V) — good for MPPT controllers and smaller wire. Parallel adds current at the same voltage. The rule: keep cold-weather string Voc under the controller's max input, and keep parallel string current inside the wire and fuse ratings. The [series vs parallel guide](/pages/solar-panels-series-vs-parallel.html) runs the trade-offs.

### Peak sun hours

The equivalent hours per day of full-strength 1,000 W/m2 sunlight a location receives — not hours of daylight. Most of the continental US sits at 3-6 peak sun hours annually; the Southwest hits 6+, the Pacific Northwest less. Sizing rule: daily Wh divided by (peak sun hours x 0.8 system efficiency) gives needed panel watts. The [state-by-state reference](/pages/peak-sun-hours-by-state.html) has the data.

### Performance ratio

The ratio of a solar system's actual measured output to its nameplate-rated output, usually 0.75-0.85 in the field. It captures all losses at once — heat, wiring, inverter, soiling, angle — and it is the honest way to check whether a new system is performing to plan. Our [output troubleshooting guide](/pages/solar-output-troubleshooting.html) compares measured production against the expected performance ratio.

### Rapid shutdown

A code requirement (NEC 690.12) that drops rooftop DC voltage to safe levels within the array boundary shortly after shutdown, so firefighters are not exposed to live strings. Module-level electronics (microinverters, optimizers) satisfy it inherently; bare string systems need listed add-on devices. The [micro vs string inverters](/pages/micro-vs-string-inverters.html) comparison covers which architecture meets it without extra parts.

### Self-consumption

Using the solar power you generate directly instead of exporting it to the grid. It matters because exported power is often compensated far below the retail rate you pay — in avoided-cost states it can be one-fifth or less. Strategy: shift big loads into sunny hours. The [net metering explainer](/pages/solar-net-metering-explained.html) shows when self-consumption, not export, carries the economics.

### Shunt

A precise low-value resistor placed in series with a battery circuit so a monitor can measure current from the voltage drop across it. It is the only honest way to track state of charge — voltage alone lies, especially with lithium's flat discharge curve. Install a shunt-based monitor on any bank you care about; the [off-grid setup guide](/pages/off-grid-solar-system-setup-guide.html) makes it step one.

### Solar irradiance vs insolation

Irradiance is the instantaneous intensity of sunlight in W/m2; insolation is the accumulated sunlight energy over time, in kWh/m2 per day. Saying "solar insolation" when you mean irradiance (or vice versa) muddles the numbers. In practice: irradiance sets instant panel output, and insolation over a day is what peak sun hours turn into. The [panel output guide](/pages/solar-panel-output.html) uses both correctly.

### State of charge (SoC)

How full a battery is, expressed as a percentage — 100% is full, 20% means 20% of rated capacity left. It matters because lead-acid voltage tracks SoC loosely (12.0V at rest is roughly 50%) while lithium's flat curve makes voltage almost useless for estimating it. Use a shunt-based monitor or the BMS reading instead of guessing from voltage. The [battery drains overnight guide](/pages/battery-drains-overnight-off-grid.html) treats this directly.

### Surge vs continuous watts

Continuous watts is what an inverter can sustain indefinitely; surge watts is what it can deliver for a few seconds — typically 2-3x continuous — to start motors and compressors. If the inverter's continuous rating covers your running load but its surge does not cover the fridge's start spike, it will shut down. The rule is roughly 3-10x running watts on startup for compressors. The [inverter sizing guide](/pages/solar-inverter-sizing.html) checks both numbers.

### Temperature coefficient

The per-degree change in panel output, quoted as %/C, almost always negative: typically -0.30 to -0.45%/C for power. A 400W panel with a -0.35%/C coefficient loses about 10% at 30C above the 25C rating — the hot-roof penalty — so the coefficient matters as much as efficiency in hot climates. The [panel efficiency guide](/pages/solar-panel-efficiency.html) compares panels on this spec. 

### Tilt

The angle of the panels above horizontal relative to true south (see azimuth). For grid-tied systems, tilting to roughly your latitude maximizes annual output; off-grid systems often tilt steeper to favor winter production. Tilting 15 degrees off optimum typically costs only a few percent of annual output. The [tilt and orientation guide](/pages/solar-panel-tilt-and-orientation.html) has the numbers by latitude.

### Transfer switch

A switch that changes a circuit's power source between shore/grid power and inverter/battery power, so the two never feed each other. Automatic transfer switches handle grid-to-backup switching for whole-home or backed-up circuits; they are part of any hybrid installation. The [solar installation safety guide](/pages/solar-installation-safety-guide.html) flags automatic transfer switching as grid-side work for a licensed electrician.

### Usable capacity

The energy a battery can actually deliver within its safe discharge limit — nameplate Wh times usable DoD. A 10kWh battery at 90% DoD is 9kWh usable; the same nameplate at 50% DoD leaves half on the table. Compare batteries by usable kWh and cost per usable kWh per cycle, never by nameplate alone. The [battery capacity calculator](/pages/battery-capacity.html) and the [cost per kWh guide](/pages/solar-battery-cost-per-kwh.html) both run this math.

### Voc

Open-circuit voltage — the panel's voltage with no load attached, measured at standard test conditions. It is the highest number the array ever presents, and it rises in cold weather, so it sizes the charge controller's input limit: string Voc at your record low temperature must stay safely under the controller's maximum. The [controller sizing page](/pages/charge-controller-sizing.html) works this exact check.

### Vmp

Voltage at maximum power — the voltage at which a panel actually delivers its rated wattage under load, typically 15-20% below Voc. Controllers with MPPT track this point to harvest rated power. The rule: the array's Vmp should sit comfortably inside the controller's MPPT window, above the battery charge voltage. The [MPPT vs PWM comparison](/pages/mppt-vs-pwm.html) explains why the gap between Voc and Vmp is where MPPT earns its gain.

### Voltage drop

The voltage lost to wire resistance over a run, which reduces the power delivered to the far end and warms the wire. It scales with length and current (and inversely with thicker wire): plan runs under roughly 3% drop for sensitive circuits, and step up a gauge beyond about 5 feet on high-current runs. The [wire size calculator](/pages/solar-wire-size.html) computes it for any run.

### Watt-hours per day (Wh/day)

The total energy your loads consume in a typical day — the single number everything else in solar sizing flows from. Add each appliance's watts times hours of actual use, then divide by (peak sun hours x 0.8) for panel watts and multiply by days of autonomy for battery size. The [system sizing guide](/pages/solar-system-sizing.html) is built around this number, and the [load calculator](/pages/how-to-calculate-solar-load.html) helps you find it.

## FAQ

{{< faq "What is the difference between a watt and a watt-hour?" >}}
A watt is a rate of power use at this instant; a watt-hour is the energy used over time (watts x hours). A 100W bulb draws 100 watts while on, and 300 watt-hours if it runs for three hours. Solar sizing uses watt-hours per day; ratings and datasheets use watts.
{{< /faq >}}

{{< faq "Why does the glossary list Voc, Vmp, and Isc separately?" >}}
They are three different slices of a panel spec sheet. Voc is the no-load voltage (cold, sunny, unconnected) that sizes your charge controller's input limit; Vmp is the working voltage at which the panel makes rated power; Isc is the short-circuit current that sizes fuses and wire. One panel sells on all three numbers, and each decides a different part of the build.
{{< /faq >}}

{{< faq "What does 'usable' capacity mean on a solar battery?" >}}
Usable capacity is the energy you can safely draw before recharging — nameplate watt-hours times your depth of discharge. A 10kWh lithium battery at 80% DoD is about 8kWh usable; the same lead-acid battery at 50% DoD is only about 5kWh usable. Always size from usable capacity.
{{< /faq >}}

{{< faq "Is a higher voltage system always better?" >}}
No — it is a trade-off. Higher voltage (48V vs 12V) cuts current for the same power, so wire can be thinner and losses lower, which is why larger systems standardize on 48V. But 12V keeps small builds and RV gear simple, since the loads and chargers are already 12V. Choose the voltage class that fits your load size and equipment.
{{< /faq >}}

{{< faq "Why do you explain net metering and rapid shutdown here?" >}}
Because both are policy and code terms that show up on every quote and permit, and both have a number attached: net metering credit rates decide payback, and NEC 690.12 rapid shutdown decides what inverter hardware your roof requires. Their dedicated guides are linked from their entries above.
{{< /faq >}}

{{< faq-schema >}}

## Next logical reads

<a href="/pages/solar-basics.html" class="text-link">Solar basics</a> — the three-piece system picture in one page
<a href="/pages/solar-system-sizing.html" class="text-link">How to size a solar system</a> — the step-by-step that starts from your daily watt-hours
<a href="/pages/wiring-decisions.html" class="text-link">Solar wiring decisions</a> — the fuse-every-source rule and the planning ampacity ladder
<a href="/pages/how-we-recommend.html" class="text-link">How we pick and link products</a> — how product mentions on this site are chosen