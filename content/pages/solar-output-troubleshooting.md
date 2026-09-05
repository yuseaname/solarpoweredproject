+++

title = "Low Solar Output: Troubleshooting Checklist (Common Causes)"
slug = "solar-output-troubleshooting"
date = 2026-05-31
draft = false
description = "Troubleshoot low solar output: weather vs seasonal effects, shading, dirty panels, inverter issues, and simple checks to identify the cause."
image = "/images/solar-output-troubleshooting/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
+++

{{< affiliate-disclosure >}}

## Quick answer

Low output almost always comes down to one of five causes, in this order of likelihood:

1. **Soiling** — dirt, pollen, bird droppings, or snow on the glass.
2. **Shading or season** — new shade from tree growth, or you're comparing December to July.
3. **Wiring and connections** — a loose MC4, corroded lug, or tripped breaker acting like a resistor.
4. **Charge controller or inverter settings** — wrong battery profile, a derating error code, or float mode that just looks like a fault.
5. **Real degradation** — panels lose capacity slowly; sudden drops are almost never this.

The fix sequence is the same order: check what's cheap and visible first, do the voltage/current math second, and only then start disconnecting things. Most "my system got weak" reports end at steps 1 or 2 — and a surprising number aren't a fault at all, just winter.

## Key takeaways

-   **Establish a baseline before diagnosing.** Nameplate watts are lab numbers; a healthy array delivers roughly 70–85% of nameplate in good conditions after real-world losses.
-   **Compare like with like:** this month vs the same month last year, not vs your summer peak.
-   **Shading is disproportionate.** A small shadow on a series string can cut array output 20–40%, far more than the shaded area suggests.
-   **A multimeter plus the spec sheet answers most questions** in 20 minutes — panel voltage and current measurements separate "input problem" from "equipment problem."
-   **Sudden, large drops point to wiring, shading, or an error code.** Slow, gradual decline over years points to soiling habits or normal degradation.

## Establish your baseline first

You can't diagnose "low" without defining "normal." Start with nameplate and derate it honestly.

A panel's rated watts (STC) are measured at 25°C cell temperature under standard lab light. Real installations run hotter and lose a few percent in wiring, connections, and the inverter. A conservative working derate for a well-installed grid-tied array is **0.75–0.85**; dirty or hot rooftop arrays sit at the low end.

**Expected daily Wh ≈ Array watts × Peak sun hours × System derate**

Worked example — 6 × 400W panels (2,400W array), 4.5 peak sun hours, 0.80 derate:

2,400 × 4.5 × 0.80 = **8,640 Wh/day ≈ 8.6 kWh on a clear spring day**

That same array in December at 2.2 sun hours and slightly cooler panels:

2,400 × 2.2 × 0.85 = **4,488 Wh/day ≈ 4.5 kWh — about half, and still normal**

On the instantaneous side: a 400W panel in bright midday sun with a cool cell temperature should read roughly **300–360W**; on a hot afternoon, **250–320W** is common. <a href="solar-panel-output.html" class="text-link">Solar panel output calculator</a>

If your actual production is within about 10–15% of this baseline, you don't have a fault — you have weather, season, or a measurement-timing issue. Below that gap, work the diagnostic in order.

## The diagnostic: cheapest check to deepest

### Step 1: Visual inspection (free, 10 minutes)

Walk the array at the time of day output normally peaks.

-   **Soiling:** look for an even gray film (pollen, dust) versus localized splatter (bird droppings, leaf tannins). Uneven soiling hurts more than a uniform film because shaded spots behave like partial shade. See <a href="solar-panel-cleaning-cost.html" class="text-link">what cleaning actually costs</a> before renting gear.
-   **Shading:** trees grow; vents, satellite dishes, and new construction cast new shadows. A shadow that crosses the array at 2pm but not 10am will hide if you inspect at the wrong time. How badly shade hurts depends on your wiring — see <a href="solar-panel-shading-effects.html" class="text-link">how shading affects panels and what bypass diodes do</a>.
-   **Obvious damage:** cracked glass, burned or melted connector plastic, chewed wiring, panels flush with snow.
-   **Monitoring trend:** if you have panel-level or string-level monitoring, one weak string or module identifies the suspect before you touch a meter.

### Step 2: String voltage and current math (multimeter, 20 minutes)

With a basic multimeter and your panels' spec sheet, you can prove or clear the entire input side.

**Open-circuit voltage (Voc):** disconnect the string (or measure at the controller's PV terminals with PV disconnected) and measure in decent sun.

-   A nominal "12V" panel should read **18–22V** in sun.
-   A typical 60-cell residential panel reads within about **10% of its spec-sheet Voc** (commonly 38–50V depending on model).
-   Series strings add: ten 40V panels ≈ 400V. If your string reads half of what the math predicts, a panel or connection in the string is open or bypassed.

**Short-circuit current (Isc):** briefly measure through the meter's amps jack (or use a DC clamp meter around one conductor — safer, no disconnection). A panel's Isc should land within about 10% of spec. A reading far below spec with clean, unshaded glass points to a failing panel or a resistive connection.

**Voltage at the controller:** for battery-based systems, PV voltage should sit at least **~5V above battery charging voltage** or an MPPT controller has nothing to track. A 12V panel (≈18–22V) feeding a 24V battery bank in parallel wiring can't do that — that's a design problem, not a fault.

| Measurement | Healthy reading | Red flag |
| :-- | :-- | :-- |
| Single 12V-class panel Voc (in sun) | 18–22V | Near 0V, or half the expected string total |
| 60-cell panel Voc | Within ~10% of spec sheet (≈38–50V) | 10V+ below spec |
| Panel/string Isc | Within ~10% of spec sheet | Far below spec with clean, unshaded glass |
| PV voltage at MPPT controller | ≥5V above battery charging voltage | PV volts ≈ battery volts in bright sun |
| Battery resting voltage (12V lead-acid) | 12.1–12.7V | Below 12.0V |
| Battery resting voltage (12V lithium) | 13.2–13.6V | Below 13.0V or 0V (BMS tripped) |
| Charge current in good sun, battery not full | Matches available input | 0A with full sun |

Hot terminals, discoloration, or melted connector insulation at any point: **stop and stop using the circuit** — that's a fire risk, not a performance problem.

### Step 3: Controller and inverter logs (free, 15 minutes)

Input checks out? Look at the electronics' side of the story.

-   **Error and derating codes:** over-temperature derating on hot inverters, grid-voltage faults, and PV overvoltage on cold mornings are common and often self-clearing. Look up codes rather than guessing.
-   **Charging stage:** bulk/absorption taper and float are normal. A full battery showing 2A in the afternoon is the system working correctly. Our <a href="mppt-charge-controller-not-charging.html" class="text-link">MPPT not charging checklist</a> covers the stage-by-stage detail.
-   **Settings:** a lithium battery on a lead-acid profile (or vice versa) chronically undercharges. Verify battery type and charge voltages against the battery manufacturer's sheet.
-   **Timestamps matter:** output that drops every afternoon at the same time is shading; output that's low all day on clear cool days is more likely soiling, wiring, or a hardware fault.

### Step 4: Isolate panels (deepest check)

If a whole string underperforms, find the individual culprit.

1.  With PV disconnected and the meter on DC volts, measure each panel's Voc one at a time. One panel far below its neighbors is your suspect.
2.  Measure Isc on the suspects. Low Voc **and** low Isc on clean glass usually means a failed cell group or a bad bypass diode.
3.  On battery-based systems you can also disconnect panels one at a time (in series strings, removing a shaded or failed panel often lets the rest of the string recover) and watch charge current respond.

Replace or professionally repair the outlier; don't keep running a panel that reads wildly off-spec.

## Winter is not a fault

The single most common false alarm: "my system lost half its output." If the drop began in late fall, do the seasonal math before touching anything.

-   **Shorter days and a lower sun angle cut daily production 40–60% in most of the US between July and December.** A system that made 2,000 Wh/day in July can legitimately make 600–900 Wh/day in December at northern latitudes — same panels, same wiring, nothing broken.
-   **Peak sun hours drop more than people expect.** Use your location's monthly average (NREL's PVWatts is the standard free reference) rather than guessing from summer numbers.
-   **Cold actually helps panel efficiency.** Silicon produces more voltage when cold — a clear, cold January afternoon can beat a hot July one hour-for-hour. Cold hurts output through shorter days and snow, not cell physics.
-   **Snow is a full shutoff, not a derate.** A few inches of cover reads as 0W and is completely normal; it clears without intervention on most tilts.

| Season | What "normal" looks like | Not normal |
| :-- | :-- | :-- |
| Summer | Float by midday on battery systems; high peaks | Midday peaks well below baseline on clear days |
| Fall/Spring | Day-to-day swings with weather | One string or panel far below the others |
| Winter | 40–60% less daily energy; short charge window | Zero output on clear days with no snow |
| Cold snap | Higher panel voltage; possible PV overvoltage error on tight systems | Repeated faults — check controller max PV voltage |

## When it really is the controller or battery

You've confirmed good input, honest wiring, and sane settings, and output is still low. Now the suspicion shifts — but check these two pages before buying anything:

-   <a href="mppt-charge-controller-not-charging.html" class="text-link">MPPT charge controller not charging</a> — PV voltage headroom, cold-weather Voc limits, battery profile settings, and error codes. Most "dead controller" diagnoses turn out to be one of those four.
-   <a href="solar-battery-not-charging-troubleshooting.html" class="text-link">Solar battery not charging</a> — float behavior, BMS low-temperature cutoffs (lithium packs below freezing refuse charge by design), and net-load problems where the system produces fine but loads eat the charge.

And if the array charges the battery fine but household AC output is low, the input side isn't your problem at all — see <a href="inverter-keeps-shutting-off-troubleshooting.html" class="text-link">inverter keeps shutting off</a>.

## Safety first

-   **No roof work in rain, ice, high wind, or on wet panels.** No production figure is worth a fall. Clean from the ground with a pole and deionized water, or hire it out.
-   **DC arcs don't self-extinguish** the way AC arcs do. Never disconnect MC4 connectors or breakers while current is flowing — open the DC disconnect or breakers first, then unplug connectors.
-   Cover the panel with opaque material when measuring Isc to reduce arc risk at the leads, and use a meter rated for your system's DC voltage and current.
-   **Melted insulation, burned smell, or hot connectors = stop.** That's an immediate-call-a-professional situation.
-   When in doubt on anything above your head or inside a combiner box, hand it to a licensed electrician. Solar maintenance has a safe DIY core — see <a href="solar-maintenance.html" class="text-link">the maintenance checklist</a> for what's reasonable to handle yourself.

## FAQ

{{< faq "How much does dirt actually reduce solar output?" >}}
A light, even dust film typically costs a few percent. Heavy or uneven soiling — bird droppings, leaf tannin, pollen buildup — can cut output far more because shaded spots act like partial shade. In dry climates without rain for months, losses of 5–15% from soiling are a reasonable planning range. If your glass looks uniformly hazy from the ground, cleaning is the cheapest test you can run.
{{< /faq >}}

{{< faq "Why is my output lower than my neighbor's identical system?" >}}
Orientation, tilt, and shading. A south-facing array at a good tilt will beat the same panels facing east-west or sitting under a tree line by 10–30%. Compare your system to its own baseline and its own history — not to a neighbor's.
{{< /faq >}}

{{< faq "Can cold weather ever increase output?" >}}
Yes. Panel voltage rises as cells get colder, and most panels' power temperature coefficient is around -0.3% to -0.4% per °C — so a clear 30°F afternoon can outproduce a hot 95°F one hour-for-hour. Winter's production drop comes from short days, low sun angle, and snow cover, not from cold hurting the panels.
{{< /faq >}}

{{< faq "Should I trust my monitoring app or measure with a multimeter?" >}}
Use both. The app gives you the trend (when output dropped, which string, what time of day); the meter gives you ground truth at the panel. If the app says a string is weak, the multimeter's Voc and Isc measurements tell you whether it's shade, a connection, or a failed panel.
{{< /faq >}}

{{< faq "How do I tell degradation apart from a fixable problem?" >}}
Degradation is slow: quality panels typically lose on the order of 0.5% per year, which is why 25-year warranties guarantee around 85–87% of nameplate output. If your decline took years, it's likely degradation plus soiling. A drop of 20%+ over weeks or months is a fault — shading, wiring, or a component — and the checklist above will find it.
{{< /faq >}}

{{< faq "When should I call a professional?" >}}
Anytime you see melted insulation, burned smell, tripping DC breakers, or fault codes you can't clear; anytime the work involves the roof in poor conditions; and anytime you'd be opening a combiner box or working on strings above ~100V DC without experience. Diagnosing from the ground with a meter and an app is DIY territory — repairs inside high-voltage DC circuits are not.
{{< /faq >}}

## Next logical reads

<a href="/pages/solar-panel-output.html" class="text-link">Solar panel output calculator (derating factors)</a> <a href="/pages/solar-panel-shading-effects.html" class="text-link">How shading affects solar panels</a> <a href="/pages/solar-panel-cleaning-cost.html" class="text-link">Solar panel cleaning cost (DIY vs pro)</a> <a href="/pages/solar-maintenance.html" class="text-link">Solar maintenance checklist</a> <a href="/pages/mppt-charge-controller-not-charging.html" class="text-link">MPPT charge controller not charging</a> <a href="/pages/solar-battery-not-charging-troubleshooting.html" class="text-link">Solar battery not charging</a>

---

**Related guides:**
- [MPPT Charge Controller Not Charging: Troubleshooting Checklist (PV Voltage, Settings)](/pages/mppt-charge-controller-not-charging.html)
- [Solar Battery Not Charging: Troubleshooting Checklist (MPPT, Wiring, Loads)](/pages/solar-battery-not-charging-troubleshooting.html)
- [DIY Small Wind Turbine for Battery Charging (Wiring + Diversion Load Control)](/diy-off-grid-energy/diy-small-wind-turbine-for-off-grid-battery-charging.html)
