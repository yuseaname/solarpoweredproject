+++

title = "How to Calculate Your Solar Load: A Step-by-Step Energy Audit"
slug = "how-to-calculate-solar-load"
date = 2026-08-10
draft = false
description = "Learn how to calculate your daily solar energy needs in watt-hours. Includes a step-by-step load worksheet, common appliance wattages, and sizing mistakes to avoid."
image = "/images/how-to-calculate-solar-load/hero.jpg"
image_alt = "Solar calculator and planning worksheet on a desk — the arithmetic side of a load calculation"
author = "Solar Powered Project"
image_width = 1024
image_height = 576
+++

## Key takeaways

-   A solar load calculation starts with listing every device and finding its wattage and daily run hours.
-   The core formula is simple: **watts × hours = watt-hours per day (Wh/day)** per device.
-   Sum all devices, divide by your local peak sun hours, then derate for system losses (0.75–0.85).
-   Motors and compressors have a surge 2–3× their running watts that must be factored into inverter sizing.
-   Forgetting "phantom" loads is the most common sizing mistake — they add up faster than people expect.
-   Battery bank sizing in amp-hours: **daily Wh ÷ battery voltage ÷ depth of discharge**.

## Why your solar load calculation matters

Every correctly sized solar system on the planet starts with the same boring, unglamorous step: an energy audit. People love to start with panels — how many watts, mono or poly, what brand — but the panels are actually the last thing you size. The math flows in one direction: loads first, then battery bank, then panels to recharge it, then a charge controller and inverter sized to match.

Skip this step or fudge the numbers and you end up with a system that can't keep up, batteries that chronically undercharge, a generator that runs every other weekend, and a lingering feeling that solar "just doesn't work." It does work — you just sized it wrong.

The good news is that the calculation itself is genuinely simple. Middle-school arithmetic. What takes time is the inventory: walking through your home, cabin, or RV with a notepad and being honest about how many hours a day the TV is actually on.

Related: <a href="solar-system-sizing.html" class="text-link">How to size a complete solar system</a> <a href="solar-basics.html" class="text-link">Solar power basics</a>

## The seven-step solar load worksheet

### Step 1: List every device

Grab a spreadsheet, a legal pad, or the back of an envelope. Walk room by room. Open every drawer and cabinet. Anything that plugs in, gets charged, or runs on a thermostat goes on the list. This includes:

-   Lights (count each bulb or fixture)
-   Refrigerator and freezer
-   Phone, tablet, laptop, and tool chargers
-   Water pump (if on a well or tank system)
-   Ventilation fans and ceiling fans
-   Router, modem, and network gear
-   Entertainment: TV, soundbar, streaming stick, game console
-   Kitchen: microwave, coffee maker, toaster, blender, Instant Pot
-   Heating and cooling: space heater, window AC, mini-split, electric blanket
-   Medical devices: CPAP, oxygen concentrator
-   Power tools used regularly

The goal is completeness, not filtering. A device you forget isn't a rounding error — it's a daily deficit you'll feel later. We'll trim and prioritize in a later step.

### Step 2: Find the wattage of each device

There are three ways to get the wattage, in order of accuracy:

1.  **Use a plug-in watt meter (most accurate).** A Kill-A-Watt meter costs about $20–30 and tells you exactly how many watts a device draws in real time, plus total Wh over a day or week. This is the gold standard for anything that plugs into a standard outlet. Run it for 24 hours on a fridge and you'll have a real number, not a guess.
2.  **Read the label (good).** Most devices have a sticker on the back or bottom listing input volts and amps. Multiply them: **V × A = watts**. A laptop brick reading "19V, 3.42A" draws about 65W at full tilt. A phone charger labeled "5V, 2A" draws 10W max.
3.  **Look it up (acceptable estimate).** For hard-to-measure items like well pumps or hardwired furnaces, manufacturer specs or common wattage tables work fine. The table below covers the usual suspects.

For devices that cycle on and off (fridge, freezer, furnace, well pump), you want the **average** wattage over the day, not the momentary running watts. A 150W fridge doesn't run 24 hours — the compressor runs maybe 30–40% of the time, so average consumption is closer to 1,000–1,400 Wh/day for a full-size unit. A Kill-A-Watt over 24 hours captures this automatically.

### Step 3: Estimate daily running hours

This is where most people lie to themselves. Be realistic, not aspirational. The laptop runs 6 hours, not "a couple." The lights are on 4 hours in the evening, not "barely at all."

For cycling loads, use duty cycle × 24 hours. A fridge with a 35% duty cycle: 0.35 × 24 ≈ 8.4 equivalent running hours per day.

For seasonal loads, note both summer and winter usage. A heater that runs 8 hours a day in January runs 0 hours a day in July. An AC does the opposite. Pick the **worse-case season** for sizing — winter is usually the harder one for off-grid solar because you need more energy *and* have less sun.

### Step 4: Multiply — watts × hours = Wh/day per device

Here's where the math happens. For each row on your list:

| Device | Watts | Hours/day | Wh/day |
|---|---|---|---|
| LED light (×4) | 10 W each | 4 h | 40 W × 4 h × 4 bulbs = 640 Wh |
| Phone charger | 5 W | 3 h | 15 Wh |
| Laptop | 50 W | 6 h | 300 Wh |
| Wi-Fi router | 7 W | 24 h | 168 Wh |
| Refrigerator (full-size, cycling) | 150 W | 8 h equiv. | 1,200 Wh |
| LED TV (55") | 90 W | 4 h | 360 Wh |
| Well pump (½ hp) | 750 W | 0.5 h | 375 Wh |
| Bathroom exhaust fan | 30 W | 1 h | 30 Wh |

That's a representative sample — your numbers will differ. The point is the pattern.

### Step 5: Sum everything to get total daily Wh

Add the right-hand column. Using the table above: 640 + 15 + 300 + 168 + 1,200 + 360 + 375 + 30 = **2,888 Wh/day**, or about **2.9 kWh/day**.

That's your **load number**. Everything downstream — battery bank, panel array, charge controller — is sized from this single figure. Write it down. It's the most important number on the whole project.

Don't forget to add a fudge factor for things you'll add later: another light, a second fridge, a fan you forgot. A common practice is to multiply your total by 1.2–1.3 to give yourself 20–30% headroom. For 2.9 kWh/day, plan for about 3.7 kWh/day.

### Step 6: Divide by peak sun hours to size the panel array

Solar panels are rated in watts under standard test conditions, but they never produce rated watts for a full "solar day." Instead, the industry uses **peak sun hours (PSH)** — the equivalent number of hours per day when sunlight is strong enough to produce full rated output. A location with 5 PSH means the panels get 5 hours of full-strength sun, even though the actual daylight may last 12+ hours.

You can find your local PSH on the NREL PVWatts calculator or regional solar maps. As a rough guide: the U.S. Southwest averages 5.5–6.5 PSH, the Southeast 4.5–5.5, the Midwest 4–5, and the Pacific Northwest and Northeast 3–4. Winter numbers run 25–50% lower.

Panel watts needed = daily Wh ÷ peak sun hours. For 3,700 Wh/day at 5 PSH: 3,700 ÷ 5 = **740 W of panels minimum**.

Related: <a href="solar-panel-output.html" class="text-link">How much energy solar panels actually produce</a>

### Step 7: Derate for system losses — multiply by 0.75–0.85

A 740 W array will not produce 740 W into your battery bank. Real-world losses stack up fast:

-   Panel temperature derate (panels lose ~0.4% efficiency per °C above 25°C)
-   Dirt and soiling (5–10% on an unwashed array)
-   Wiring and connector losses (2–5%)
-   Charge controller efficiency (75–98%, depending on MPPT vs PWM)
-   Battery round-trip losses (5–15% for lead-acid, 2–5% for lithium)
-   Inverter efficiency (85–95% for AC loads)

Multiply it all together and you land somewhere around 0.75–0.85 — that is, only 75–85% of rated panel wattage ends up as usable energy in your appliances. So divide your Step 6 number by 0.8 (a reasonable middle value): 740 ÷ 0.8 ≈ **925 W**. Round up to a practical array size — say, four 250 W panels for 1,000 W.

That's how a 2.9 kWh/day load turns into roughly 1 kW of panels. The math is honest, not generous.

Related: <a href="solar-inverter-sizing.html" class="text-link">How to size your solar inverter</a>

## Battery bank sizing in amp-hours

Once you know your daily Wh, sizing the battery bank is a similar process. You want enough stored energy to cover your loads through the night and through a cloudy day or two (days of autonomy, typically 2–3 for off-grid).

Formula: **required Ah = (daily Wh × days of autonomy) ÷ battery voltage ÷ depth of discharge**

-   **Battery voltage**: 12V, 24V, or 48V depending on your system design. Higher voltage = lower current = thinner wire. Most small systems start at 12V; anything over ~1,500 Wh/day should consider 24V or 48V.
-   **Depth of discharge (DoD)**: how far down you can safely drain the bank. Lead-acid: 50% (0.5). Lithium (LiFePO4): 80–90% (0.8–0.9).

Example: 3,700 Wh/day, 2 days autonomy, 48V lithium bank at 80% DoD:

(3,700 × 2) ÷ 48 ÷ 0.8 = 7,400 ÷ 48 ÷ 0.8 ≈ **193 Ah at 48V**

A common 48V lithium server-rack battery is 100 Ah, so you'd wire two in parallel for 200 Ah — right in the zone.

For a 12V lead-acid bank at 50% DoD with the same load: (3,700 × 2) ÷ 12 ÷ 0.5 ≈ **1,233 Ah at 12V**. That's six golf-cart batteries in series-parallel — a lot of lead. This is why higher voltage and lithium chemistry pay for themselves on any non-trivial system.

Related: <a href="battery-capacity.html" class="text-link">Understanding battery capacity and amp-hours</a>

## Surge watts and motors

Resistive loads (lights, chargers, heaters) draw a steady wattage. **Inductive loads** — anything with a motor, compressor, pump, or transformer — have a **surge** (also called inrush or lock-rotor current) that's typically 2–3× their running wattage for the first few seconds of startup; hard-start loads like well pumps can briefly demand 3–7×. A 750 W well pump might briefly pull 1,800–2,200 W as the motor spins up. Refrigerator surge depends heavily on compressor type: traditional compressors can hit 5–6× running watts, while inverter-compressor models barely surge at all — check which type you have.

Surge doesn't affect your Wh/day calculation much (a few seconds is nothing across a full day), but it **directly determines inverter sizing**. If your inverter can't deliver the surge, the motor won't start and may stall or trip. Always size the inverter for the sum of all likely-to-be-on surge loads plus a safety margin.

Common surge ratios:

| Device | Running watts | Surge (approx.) |
|---|---|---|
| Refrigerator (full-size) | 150–250 W | 500–1,500 W (compressor-dependent) |
| Chest freezer | 100–200 W | 800–1,200 W |
| Well pump (½ hp) | 750 W | 1,800–2,200 W |
| Air conditioner (window, 5k BTU) | 500–700 W | 2,000–3,000 W |
| Microwave (1,000 W output) | 1,400–1,600 W (input) | ≈ running (resistive, no motor surge) |
| Coffee maker | 1,000–1,500 W | 1,000–1,500 W (resistive, no surge) |

The microwave is a good reminder: **watts in (from the wall) ≠ watts out (cooking power)**. A "1,000 W" microwave typically draws 1,400–1,600 W from the outlet. Check the label.

## The most common sizing mistakes

### Forgetting phantom loads

Anything with a power brick, a clock, a remote control, or "instant-on" capability draws power 24/7, even when "off." A TV in standby uses 5 W. A cable box can draw 20–30 W constantly. A phone charger left plugged in draws 1–2 W with no phone attached. A coffee maker with a clock pulls 3 W around the clock.

Twenty watts of phantom load × 24 hours = **480 Wh/day**. On a 3,700 Wh/day budget, that's 13% of your energy consumed by things you're not even using. Track them down, unplug them, or put them on switched power strips.

### Using nameplate max instead of actual draw

A laptop brick rated 90W rarely draws 90W — closer to 30–60W in normal use, spiking to 90W only when the battery is low and you're doing heavy compute. Using nameplate max inflates your total. A Kill-A-Watt meter resolves this in minutes.

### Forgetting the inverter's own consumption

Inverters aren't free. A pure-sine inverter draws 10–40 W just sitting there turned on (tare loss or idle draw), plus conversion losses of 5–15% on every watt that passes through. An oversized inverter idling 24/7 on a small system can eat 500+ Wh/day all by itself. Size the inverter to your real loads and turn it off when not needed.

### Underestimating winter loads and overestimating winter sun

Winter means more lighting hours, more heating (if electric), and often less computer use (good) but more oven use (bad for solar). It also means 30–50% less peak sun in most of the U.S. If your system barely squeaks by in July, it will fail in December. Always size for your worst month.

### Ignoring duty cycle on cycling loads

If you assume the fridge runs 24/7, you'll over-size by 2–3×. If you assume it runs 4 hours, you'll under-size by 2×. The truth is somewhere around 8–10 equivalent hours for a modern full-size fridge. Measure it.

## A worked example: small off-grid cabin

Let's put it all together. A weekend cabin for two people, no grid available.

**Loads (daily average during a weekend stay):**

| Device | Watts | Hours | Wh/day |
|---|---|---|---|
| LED lights (×6) | 60 W total | 4 h | 240 |
| Phone chargers (×2) | 10 W | 3 h | 30 |
| Laptop | 50 W | 5 h | 250 |
| Wi-Fi router | 7 W | 12 h | 84 |
| Small fridge | 120 W | 10 h equiv. | 1,200 |
| LED TV | 60 W | 3 h | 180 |
| Water pump (12V) | 100 W | 0.5 h | 50 |
| Ventilation fan | 25 W | 4 h | 100 |
| **Total** | | | **2,134 Wh** |

With 25% headroom: **2,670 Wh/day**.

At 4.5 peak sun hours (Pacific Northwest, shoulder season): 2,670 ÷ 4.5 = 593 W panels. Derated by 0.8: **742 W**. Four 200 W panels = 800 W. Comfortable.

Battery (2 days autonomy, 24V lithium at 80% DoD): (2,670 × 2) ÷ 24 ÷ 0.8 = **278 Ah at 24V**. Two 12V 280Ah LiFePO4 batteries in series.

That's a real, workable system. Not a fantasy, not over-built — just honest math.

## Next logical reads

<a href="solar-system-sizing.html" class="text-link">Complete solar system sizing guide</a> <a href="solar-panel-output.html" class="text-link">How much energy solar panels actually produce</a> <a href="battery-capacity.html" class="text-link">Understanding battery capacity</a> <a href="solar-inverter-sizing.html" class="text-link">How to size your inverter</a> <a href="solar-basics.html" class="text-link">Solar power basics</a>

## FAQ

{{< faq "What is a solar load calculation?" >}}
A solar load calculation is the process of adding up the daily energy (in watt-hours) used by every device you want to run on solar. It's the first step in sizing any solar system, because panel and battery sizes are derived from your daily energy demand.
{{< /faq >}}

{{< faq "How do I find the wattage of an appliance?" >}}
The most accurate method is a plug-in watt meter like a Kill-A-Watt, which shows real-time draw and total daily Wh. Otherwise, read the label on the back of the device and multiply volts × amps to get watts. For devices that cycle on and off, like refrigerators, measure average consumption over 24 hours rather than peak draw.
{{< /faq >}}

{{< faq "How many peak sun hours do I get?" >}}
Peak sun hours vary by location and season. The U.S. ranges from about 3 PSH (Pacific Northwest and Northeast in winter) to 6.5+ PSH (Southwest in summer). Use the free NREL PVWatts calculator with your ZIP code for accurate local numbers.
{{< /faq >}}

{{< faq "Do I need to size for summer or winter?" >}}
Size for your worst month — almost always winter in the U.S., when you need more lighting and heating energy and the panels produce 25–50% less. A system sized only for July will fail in December.
{{< /faq >}}

{{< faq "What is a phantom load?" >}}
A phantom load (or vampire draw) is energy consumed by a device that's plugged in but turned off or in standby — TVs, chargers, cable boxes, anything with a clock or remote. A typical home has 20–60 W of phantom load running 24/7, which can add up to 1,000+ Wh/day.
{{< /faq >}}

{{< faq "How do I convert watt-hours to amp-hours for battery sizing?" >}}
Divide watt-hours by battery voltage to get amp-hours: Ah = Wh ÷ V. Then divide by depth of discharge to account for usable capacity. For a 3,000 Wh daily load on a 48V lithium bank at 80% DoD: 3,000 ÷ 48 ÷ 0.8 ≈ 78 Ah per day of autonomy.
{{< /faq >}}

{{< faq-schema >}}

---

**Related guides:**
- [Multi-Source Hybrid Off-Grid Charge Controller: Combine Solar, Wind & Hydro](/diy-off-grid-energy/multi-source-hybrid-charge-controller.html)
- [DIY Small Wind Turbine for Battery Charging (Wiring + Diversion Load Control)](/diy-off-grid-energy/diy-small-wind-turbine-for-off-grid-battery-charging.html)
- [Gravity Battery DIY: Store Energy with Weights (Physics + Build Guide)](/diy-off-grid-energy/gravity-battery-diy-energy-storage.html)
