+++
title = "What Size Solar Generator to Run a Refrigerator?"
slug = "what-size-solar-generator-run-refrigerator"
date = 2026-08-19
draft = false
description = "Measure your fridge's real running watts, surge, and daily Wh, then size a solar generator with honest math — not brand marketing claims."
image = "/images/what-size-solar-generator-run-refrigerator/img-1.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
+++

{{< affiliate-disclosure >}}

## Quick answer

Most full-size refrigerators need a solar generator rated for **at least the fridge's running watts — typically 100–250W for modern efficient models, up to 400W for older or larger units** — with **surge capacity 2–4× that** for the compressor start, and roughly **1–2.4kWh of battery per 24 hours of runtime**. But do not size from averages. Measure *your* fridge in 10 minutes using the method below, then buy for your worst day, not the label.

## The only three numbers that matter

Every fridge spec boils down to three numbers you actually need:

1. **Running watts** — what the compressor and fans draw continuously while operating.
2. **Surge watts** — the brief spike when the compressor starts (locked-rotor amps, or LRA).
3. **Daily watt-hours (Wh)** — total energy consumed over 24 hours, which is what your battery must supply.

The trap is the nameplate. A fridge label might say "115V, 6.5A" — that's 748W if you multiply naively. But the compressor does not run continuously. It cycles on and off to hold temperature, running roughly **30–50% of the time**. So the mental model is *not* "watts × 24h." It's:

**Daily Wh = running watts × duty cycle × 24 hours**

A 150W fridge at a 40% duty cycle uses 150 × 0.40 × 24 = **1,440 Wh/day** — not 3,600 Wh/day as the naive label math would suggest. That's the difference between a 1.5kWh battery and a 4kWh one.

## Measure your actual fridge (10 minutes, no gear or a $20 meter)

### Method A: nameplate + duty-cycle estimate

Read the nameplate inside the fridge door for volts and amps. Multiply for running watts. Then estimate duty cycle from the table below. This is the fastest method and good enough for a first pass.

<table>
<thead>
<tr class="header">
<th>Fridge type</th>
<th>Typical running watts</th>
<th>Typical duty cycle</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Modern efficient 18 cu-ft</td>
<td>100–150W</td>
<td>30–40%</td>
</tr>
<tr class="even">
<td>Older / larger 25 cu-ft</td>
<td>250–400W</td>
<td>40–50%</td>
</tr>
<tr class="odd">
<td>Chest freezer</td>
<td>80–120W</td>
<td>30–40%</td>
</tr>
</tbody>
</table>

### Method B: plug-in wattmeter (the gold standard)

A $20 plug-in wattmeter (Kill A Watt style) between the wall and the fridge gives you the real numbers over 24 hours: running watts, surge on start, and cumulative kWh. This is the only method that captures *your* fridge's actual duty cycle, door openings, and ambient temperature. Leave it in for a full day, ideally including a warm afternoon.

### Method C: EnergyGuide label arithmetic

The yellow EnergyGuide label lists estimated **kWh/year**. Divide by 365 for daily Wh. Worked example: a label says **500 kWh/year**. That's 500 ÷ 365 = **1.37 kWh/day = 1,370 Wh/day**. This is a yearly average, so it already includes duty cycle — but it may understate a hot-summer or frequent-door-opening day. Use it as a floor, not a ceiling.

## Worked examples: three fridge classes

Let's run the math for three realistic fridges and turn each into a minimum generator spec.

**Example 1 — Modern 18 cu-ft efficient fridge.** Running 150W, surge 800W, duty cycle 40%.
- Daily Wh: 150 × 0.40 × 24 = **1,440 Wh/day**
- Minimum inverter: 150W continuous, 800W surge
- Battery: 1,440 Wh/day × 1 day ÷ 0.85 usable (LiFePO4) ≈ **1,700 Wh**

**Example 2 — Older 25 cu-ft fridge.** Running 350W, surge 1,800W, duty cycle 50%.
- Daily Wh: 350 × 0.50 × 24 = **4,200 Wh/day**
- Minimum inverter: 350W continuous, 1,800W surge
- Battery: 4,200 ÷ 0.85 ≈ **4,940 Wh** for one day

**Example 3 — Chest freezer.** Running 100W, surge 500W, duty cycle 35%.
- Daily Wh: 100 × 0.35 × 24 = **840 Wh/day**
- Minimum inverter: 100W continuous, 500W surge
- Battery: 840 ÷ 0.85 ≈ **990 Wh**

<table>
<thead>
<tr class="header">
<th>Fridge</th>
<th>Running W</th>
<th>Surge W</th>
<th>Wh/day</th>
<th>Min inverter</th>
<th>Min battery (1 day)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Modern 18 cu-ft</td>
<td>150</td>
<td>800</td>
<td>1,440</td>
<td>150W cont / 800W surge</td>
<td>~1,700 Wh</td>
</tr>
<tr class="even">
<td>Older 25 cu-ft</td>
<td>350</td>
<td>1,800</td>
<td>4,200</td>
<td>350W cont / 1,800W surge</td>
<td>~4,940 Wh</td>
</tr>
<tr class="odd">
<td>Chest freezer</td>
<td>100</td>
<td>500</td>
<td>840</td>
<td>100W cont / 500W surge</td>
<td>~990 Wh</td>
</tr>
</tbody>
</table>

## Surge: the spec that kills cheap generators

The compressor's start surge is where undersized generators fail. The nameplate's **LRA (locked-rotor amps)** tells you the worst-case start draw. A fridge with 6.5A running might pull 30–40A for a fraction of a second at start — that's 3,450–4,600W at 115V. The common **2–4× running-watts multiplier** is a practical rule because actual start current depends on compressor design, refrigerant pressure, and temperature.

What "2,000W surge for 1 second" really means: the inverter can deliver that peak briefly, then must drop to its continuous rating. If your fridge's start surge exceeds the generator's surge rating — even for a moment — the inverter overloads and shuts down, and the fridge never starts.

**Soft-start kits** are a legitimate fix. They ramp the compressor up gradually, cutting start surge by roughly 50–70%. They cost $100–300 and are worth it when your fridge's surge is just over a generator's rating — far cheaper than buying a bigger generator. They are safe when installed per the manufacturer's instructions and are common on RVs and off-grid builds.

## Runtime math you can reuse

The formula for how many days a battery will run your fridge:

**Days = (battery Wh × usable DoD) ÷ daily Wh**

Usable depth of discharge (DoD): **LiFePO4 ~80–90%, lead-acid ~50%** — see our [lithium-ion vs lead-acid](/pages/li-ion-vs-lead-acid.html) comparison for the chemistry trade-off. See our [how long will a 100Ah battery run](/pages/how-long-will-100ah-battery-run.html) article for the full method — we won't re-derive it here.

**Worked example A:** A 2,000Wh LiFePO4 station at 85% usable = 1,700Wh usable. Running the modern fridge (1,440 Wh/day): 1,700 ÷ 1,440 = **1.18 days**.

**Worked example B:** A 5,000Wh LiFePO4 station at 85% = 4,250Wh usable. Running the older fridge (4,200 Wh/day): 4,250 ÷ 4,200 = **1.01 days** — barely one day. You'd want 2× that for a realistic multi-day outage.

## Keeping it charged: solar input reality check

To offset daily Wh with solar, you need panel watts roughly equal to daily Wh divided by good sun hours, with an efficiency penalty:

**Panel watts ≈ daily Wh ÷ (sun hours × 0.8)**

The 0.8 accounts for panel angle, temperature, charge-controller losses, and cloudy gaps. For the modern fridge at 1,440 Wh/day with 4 good sun hours: 1,440 ÷ (4 × 0.8) = **450W of panels**. That's a substantial array — not a single 100W panel. See our [solar system sizing](/pages/solar-system-sizing.html) guide for the full method.

**Cloudy-day honesty:** solar is intermittent. A 450W array on a fully overcast day might deliver 10–20% of rated output. Your battery is the real buffer; solar just extends it. If you need guaranteed multi-day runtime, size the battery for the worst stretch and treat solar as a recharge bonus, not the primary supply.

**Recharge-rate limits:** small stations cap input at 100–200W. A 450W array on a 100W-input station takes 4.5+ hours of full sun just to replace one day's fridge draw. Check the station's max solar input before buying panels.

## Beyond the fridge: what else is on the circuit

**Resistive loads spike hard.** A 1,000W coffee maker or 1,500W toaster draws its full rating continuously — no duty cycle. Add these to your daily Wh and, critically, to your surge/continuous inverter rating. A fridge-only generator may not run a toaster at the same time.

**Freezer stacking:** running a fridge *and* a chest freezer means adding their daily Wh. From our examples: 1,440 + 840 = **2,280 Wh/day**, needing roughly a 2,700Wh battery at 85% DoD for one day. Surge is the sum of both compressors starting — worst case, both at once.

**Medical devices:** if a CPAP or other medical equipment must stay powered, that's a hard requirement, not a nice-to-have. See our [CPAP battery backup guide](/pages/cpap-battery-backup-guide.html) for the dedicated math. And if you're still deciding between a solar generator and a gas backup, our [solar battery backup vs generator](/pages/solar-battery-backup-vs-generator.html) comparison covers the trade-offs.

## Buying checklist (no brands bought here — specs you verify)

Before you buy, verify these specs on the datasheet — not the marketing page:

- **Continuous watts ≥ measured running watts × 1.5** — headroom for voltage sag and other loads.
- **Surge watts ≥ LRA-implied start draw** — from the nameplate, not the 2× guess.
- **Battery Wh ≥ target days × daily Wh ÷ DoD** — e.g., 3 days × 1,440 ÷ 0.85 ≈ 5,080 Wh.
- **Pure sine output** — modified sine can cause compressor hum, overheating, and premature failure on some motors.
- **Recharge ≥ daily Wh ÷ good sun hours** — so solar can actually keep up.

**Red flags in marketing:** "peak watts" or "max watts" ratings that conflate surge with continuous. A "2,000W peak" station that only delivers 1,000W continuous will not start a fridge needing 1,800W surge. Always read the fine print for continuous rating. For the basics of how these stations work, see our [solar generator explainer](/pages/solar-generator.html).

{{< product-box asin="B0D7PPG25F" name="Jackery Explorer 1000 v2 (1070Wh, 1500W)" label="Mid-size fridge class pick" description="1070Wh LiFePO4 with 1500W continuous / 3000W surge (per manufacturer spec) — covers the modern-fridge class from the worked examples (1,400-1,600Wh/day) for most of a day, and the compressor start spike with margin. 4,000-cycle rated cells. Not for: the older 25-cu-ft class from the table above (~4,940Wh/day) or multi-day outages — by the runtime math that needs a ~5,000Wh battery. The honest tradeoff: a sealed unit with a 1,070Wh ceiling — a one-day buffer, not multi-day autonomy." button="Check price on Amazon" >}}

## FAQ

{{< faq "Can I run a fridge and freezer together?" >}}
Yes, if the generator's continuous watts cover both running draws and its surge covers both compressors starting. Add the daily Wh (1,440 + 840 = 2,280 Wh/day in our examples) and size the battery for that total.
{{< /faq >}}

{{< faq "How long will a 500Wh station run a fridge?" >}}
At 85% usable that's 425Wh. A modern fridge at 1,440 Wh/day runs 425 ÷ 1,440 = **0.30 days — about 7 hours**. A chest freezer at 840 Wh/day runs about 12 hours. 500Wh is a short-term buffer, not an outage solution.
{{< /faq >}}

{{< faq "Can a 100W panel keep up with a fridge?" >}}
Rarely. 100W × 4 sun hours × 0.8 = 320 Wh/day — about 22% of a modern fridge's 1,440 Wh/day. It extends runtime but cannot keep the battery charged. You'd need roughly 450W for the modern fridge in our example.
{{< /faq >}}

{{< faq "Are soft-start kits safe?" >}}
Yes, when installed per the manufacturer's instructions. They reduce compressor start surge by roughly 50–70%, which can let a smaller generator start a larger fridge. They are common in RVs and off-grid systems.
{{< /faq >}}
