+++
title = "Powering Communications When the Grid Is Down: Phones, Radios, and the Watt Budget That Keeps You Connected"
slug = "grid-down-communications-power"
date = 2026-10-30
pagetype = "informational"
draft = false
description = "A realistic ~40Wh/day communications budget covering phones, radios, weather alerts, and lighting — with the charging hierarchy (power bank → panel → muscle backup) and worked runtime math for each layer."
image = "/images/grid-down-communications-power/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
related = [
  "/grid-down/rebuilding-power-from-scratch.html",
  "/diy-off-grid-energy/diy-hand-crank-generator-emergency-charging.html",
  "/diy-off-grid-energy/pedal-power-generator-for-off-grid-battery-charging.html",
  "/pages/jackery-vs-ecoflow-power-stations.html",
  "/pages/cpap-battery-backup-guide.html"
]
+++

{{< affiliate-disclosure >}}

<p class="jump-links"><a href="#quick-answer" class="text-link">Quick answer</a> <a href="#the-communications-watt-budget" class="text-link">The watt budget</a> <a href="#the-charging-hierarchy" class="text-link">The charging hierarchy</a> <a href="#muscle-backup-the-honest-numbers" class="text-link">Muscle backup</a> <a href="#radios-what-to-standardize" class="text-link">Radio choices</a> <a href="#faq" class="text-link">FAQ</a></p>

## Quick answer

Keeping a household connected — phones, a handheld radio, weather alerts, and lighting — costs about **40Wh per day**, which is one-fifth of what a single 100W panel harvests on an average day. The plan is a hierarchy, not a product: a charged power bank for day one, a small panel for day two onward, and a muscle backup ([hand-crank 5–30W, pedal 50–150W](/diy-off-grid-energy/diy-hand-crank-generator-emergency-charging.html)) for the stretch when both are gone. Communications should be the *last* thing you ever ration — it is the cheapest line on the entire [grid-down budget](/grid-down/rebuilding-power-from-scratch.html).

## The communications watt budget

Every figure below is label math or physics — volts × amps × hours — rounded to planning precision:

| Device | Draw | Daily use | Daily energy |
| :-- | :-- | :-- | :-- |
| LED headlamp or lantern | 3–5W | 4–6 h | ~15–25Wh |
| Phone charge (typical battery ~4,000–5,000mAh at 3.7V) | ~15–18Wh per full charge | 1 charge | ~15Wh |
| Handheld radio (GMRS/ham), receive ~0.5W, transmit 5W | mostly receive | 8 h RX + 30 min TX | ~6Wh |
| Weather/alert radio | ~1W | 4 h | ~4Wh |
| **Total — the connected household** | | | **≈40Wh/day** |

Two honest notes. First, charging inefficiency is real: expect to spend ~20–25% more than the table (cable and conversion losses), so plan **50Wh/day harvested** to bank 40. Second, the loads that *look* like communications — laptops, TVs for news — are not in this budget. A laptop adapter draws 45–65W; one hour of that is a full day of radio. In an outage, the phone is the computer.

Medical devices jump the queue entirely: [a CPAP night is 240–700Wh](/pages/cpap-battery-backup-guide.html) — bigger than the whole comms budget by an order of magnitude. If one is in the household, size for it first and read its guide, not this one.

## The charging hierarchy

**Layer 1 — The power bank (day one).** A 20,000mAh bank at 3.7V holds ~74Wh — roughly 1.5 days of the full budget, or a week if you're phone-only. Everyone already owns Layer 1; the plan is keeping it charged and knowing where it is.

<figure>
<img src="/images/grid-down-communications-power/fig-hierarchy.webp" loading="lazy" width="640" height="427" alt="Technical-plate illustration of a three-level energy pyramid: pedal charger, folding solar panel, battery — feeding a phone and radio at the apex." />
<figcaption>The hierarchy in one picture: buffer on top, panel in the middle, muscle at the base — each layer backs the one above it. (Illustrative)</figcaption>
</figure>

**Layer 2 — The panel (day two onward).** This is where the outage stops being countdown and becomes routine:

{{< product-box asin="B071G4CQSR" name="BigBlue 28W Solar Panel Charger with Digital Ammeter" label="Layer 2: the folding panel" description="A folding 28W panel with a built-in ammeter — you watch real harvest instead of guessing (per manufacturer spec), which matters most in marginal weather. Not for: running appliances; this is a comms-and-lighting tool. The honest tradeoff: it charges USB devices directly, so it skips your 12V bank — pair it with the power bank it keeps alive." button="Check price on Amazon" >}}

A 28W folder in average sun delivers maybe 15–20W real — the full 40Wh budget in 2–3 hours of daylight. For the household version, a 100W panel into a proper bank makes comms effectively inexhaustible.

**Layer 3 — The station (the household backbone).** A 1kWh-class power station turns the comms budget trivial: [1,024–1,152Wh units](/pages/jackery-vs-ecoflow-power-stations.html) run 40Wh/day for weeks, and the same station is simultaneously covering refrigeration math elsewhere in the plan. Charging it is why the [array guide](/grid-down/solar-array-from-salvage.html) exists.

{{< product-box asin="B0D7PPG25F" name="Jackery Explorer 1000 v2 Portable Power Station, 1070Wh" label="Layer 3: the comms backbone" description="1,070Wh of storage and 1,500W continuous AC (per manufacturer spec) — roughly 25 days of the comms budget on one charge, while also covering lights and a freezer's daytime cycle. Not for: 240V well pumps or whole-house loads. The honest tradeoff: ~400W solar input means full recharges take good sun days; it is a buffer, not a generator." button="Check price on Amazon" >}}

## Muscle backup: the honest numbers

When the panel is shaded, stolen, or broken, you are the power plant — and the physics is unforgiving but usable:

- **Hand-crank: 5–30W sustained.** Thirty minutes of honest cranking at ~15W banks **7.5Wh — about half a phone charge**. This is the [hand-crank guide's](/diy-off-grid-energy/diy-hand-crank-generator-emergency-charging.html) reality check: emergency watts, not house watts. Its role: the radio-and-one-phone floor that never runs out.
- **Pedal power: 50–150W sustained.** An hour of pedaling at a realistic 75W banks **75Wh — the entire day's budget, twice.** [The pedal guide](/diy-off-grid-energy/pedal-power-generator-for-off-grid-battery-charging.html) covers the generator-to-battery chain; the economics are simple: legs beat arms by 5–10×.
- **Heat-to-power (TEG): a few watts.** A stove-top [TEG module](/diy-off-grid-energy/diy-thermoelectric-generator-teg-battery-charging.html) at 3–8% efficiency trickles single-digit watts — enough to keep a weather radio alive off a woodstove you'd run anyway.

The discipline that makes muscle power work: charge a *buffer* (power bank), never pedal to feed a device directly. Batteries forgive your rest breaks; radios don't.

<figure>
<img src="/images/grid-down-communications-power/fig-muscle.webp" loading="lazy" width="640" height="427" alt="Technical-plate illustration: an arm cranking a small generator feeding a thin stream into a small battery, beside legs pedaling a larger generator feeding a wide stream into a larger battery." />
<figcaption>Arms versus legs, same hour of effort: the width of the stream is what lands in the battery. (Illustrative)</figcaption>
</figure>

## Radios: what to standardize

Keep it to three tiers, lowest-power-first:

1. **Receive-only (weather/alert).** Sub-watt draw, runs on AA cells a solar charger can refresh. The cheapest line on the budget — and the one that tells you when the outage ends.
2. **Handheld two-way (FRS/GMRS/ham).** ~5W transmit, negligible receive draw. Standardize one radio type per group so batteries, antennas, and chargers interchange; label channel plans on paper.
3. **The phone.** Highest-value, highest-draw device. Airplane mode + periodic check-ins can cut its budget by more than half — a behavioral 20Wh/day savings no hardware purchase matches.

A note on satellite messengers: genuinely useful in extended regional outages, but they add a subscription and their own charging budget — evaluate against your real risk, not your reading list.

## FAQ

{{< faq "How do I keep my phone alive the longest during an outage?" >}}
Airplane mode with scheduled check-ins is the single biggest saver — the radio searching for weak signal is a phone's hungriest state. Add screen brightness down, background apps off, and charge in the 20–80% band when the source is muscle power (less charging loss per useful percent). Behavioral discipline beats any gadget.
{{< /faq >}}

{{< faq "Is a hand-crank radio worth it?" >}}
The receiver, yes — sub-watt draw and a crank that tops it up in minutes is a genuinely good match. The crank-as-phone-charger is the part to distrust: at 5–30W sustained, a full phone charge is an hour-plus of grinding. Crank for the radio, panel or pedal for the phone.
{{< /faq >}}

{{< faq "How big a power bank do I need?" >}}
Bank size = days × daily budget ÷ 0.8 (charging losses). For the full 40Wh/day budget over three days: ~150Wh, which is roughly a 40,000mAh unit — or two 20,000mAh banks, which lets you charge one while using the other. For phone-only: a 20,000mAh bank covers a week.
{{< /faq >}}

{{< faq "What about charging from a car?" >}}
A idling car is a 100A+ alternator wasting fuel to deliver 20 phone watts — but as a *battery*, the car is excellent: most vehicles can top up power banks for days without starting issues. Use the car as a buffer, run the engine sparingly and in open air, and put a meter on the 12V outlet so you know what you pulled.
{{< /faq >}}

{{< faq "GMRS, FRS, or ham — which should a household standardize?" >}}
FRS/GMRS handhelds cover the neighborhood with zero exam friction; ham covers the region but requires a license you should earn *before* the emergency, not during. For most households: one shared GMRS type for the group, plus the receive-only weather tier. The radio you've practiced with beats the one still in its box.
{{< /faq >}}
