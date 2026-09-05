+++
title = "CPAP Battery Backup: Sizing and Run Times"
slug = "cpap-battery-backup-guide"
date = 2026-08-19
draft = false
description = "How many nights will a battery run your CPAP? Learn the one formula, read your machine's label, and size a backup for outages and travel — with honest math and zero medical claims."
image = "/images/cpap-battery-backup-guide/img-1.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
+++

{{< affiliate-disclosure >}}

## Quick answer

A CPAP typically draws **30–60W while running**, and a heated humidifier can roughly double that. So one night (8 hours) is about **240–700Wh** — roughly **360Wh at 45W without the humidifier**, **720Wh at 90W with it**. A **100Ah 12V lithium battery** (about 960Wh usable) usually covers **1–3 nights without the humidifier**, fewer with it. The steps: (1) read your machine's label for volts and amps, (2) decide whether you'll use the humidifier each night, (3) apply the runtime formula below. This is purely electrical sizing — we are not giving medical advice, and any therapy questions belong with your prescriber. The goal here is calm, concrete numbers so an outage is a plan, not a panic.

## Find YOUR machine's real draw

The label is the starting point. On most CPAP machines it's on the bottom or back, and it lists **volts (V)** and **amps (A)**. Multiply them: **V × A = watts**. A label reading "24V, 1.5A" means 24 × 1.5 = **36W** — right in the typical range.

But the label is usually a **maximum rating**, not what the machine draws all night. Pressure settings change the blower speed, and a heated tube or humidifier adds real load. The humidifier is the big one: the heating plate can roughly **double total consumption**. If your label only gives max ratings, treat that as an upper bound — your real average is likely lower.

Some machines report average consumption in their companion app or data screen. If yours does, that's the most honest number to size from. If not, the label's V × A is a safe planning figure — plan for the worst night, and you'll be pleasantly surprised on the easy ones.

One more thing to check: whether your machine has a **DC input** in addition to the AC power brick. Many common models do, and that changes your battery options significantly — more on that in the next section. Whatever the label says, write down the volts and amps before you shop; it's the single number that makes every other calculation honest.

## The one-night math

**Wh per night = watts × hours**, plus a **15% inverter margin** if you're using the AC port.

Worked example, no humidifier: 45W × 8h = **360Wh**. On an AC port with 15% margin: 360 ÷ 0.85 ≈ **424Wh** from the battery.

Worked example, with humidifier: 90W × 8h = **720Wh**. On AC: 720 ÷ 0.85 ≈ **847Wh**.

**The DC shortcut:** many common CPAP machines have a **12V DC input**. Using the manufacturer's DC cable skips the inverter entirely — no 15% loss, and often a cleaner power path. If your machine offers a DC cable, it's usually the most efficient way to run from a battery. We cover the full runtime formula in our [how long will a 100Ah battery run](/pages/how-long-will-100ah-battery-run.html) guide — we won't re-derive it here.

## Run-time table: nights per battery

The hero table. Assumes **8-hour nights**, **lithium at 80% depth of discharge**, and **45W without humidifier / 90W with it**. Your machine's real draw changes the numbers — use the formula above.

<table>
<thead>
<tr class="header">
<th>Battery</th>
<th>Usable Wh (lithium)</th>
<th>No humidifier (45W)</th>
<th>With humidifier (90W)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>300Wh power station</td>
<td>~240Wh</td>
<td>0.7 nights</td>
<td>0.3 nights</td>
</tr>
<tr class="even">
<td>500Wh power station</td>
<td>~400Wh</td>
<td>1.1 nights</td>
<td>0.6 nights</td>
</tr>
<tr class="odd">
<td>100Ah 12V lithium</td>
<td>960Wh</td>
<td>2.7 nights</td>
<td>1.3 nights</td>
</tr>
<tr class="even">
<td>200Ah 12V lithium</td>
<td>1,920Wh</td>
<td>5.3 nights</td>
<td>2.7 nights</td>
</tr>
</tbody>
</table>

The math is simple: usable Wh ÷ nightly Wh. 960 ÷ 360 = 2.7 nights; 960 ÷ 720 = 1.3 nights. A 300Wh station is a **single-night emergency buffer**, not an outage solution. A 100Ah lithium battery is the sweet spot for most people — one to three nights without the humidifier. For the full chemistry and DoD reasoning behind these numbers, see our [100Ah runtime guide](/pages/how-long-will-100ah-battery-run.html).

## Outage playbook

The real use case is a storm knocking out power. Here's the calm, concrete sequence:

1. **Charge before the storm.** Top the battery to 100% when the forecast turns. A full battery is the whole point.
2. **Power the CPAP first.** It's the hard requirement. Everything else — phone, lights, router — comes after.
3. **Decide on the humidifier per night.** Running without it roughly doubles your nights. That's a neutral trade-off, not a medical recommendation — if you're unsure, ask your prescriber. Some people pre-heat the bedroom or use a heated tube instead; we're not advising on therapy, just noting the electrical difference.
4. **Know when to stop.** When the battery drops to your DoD limit (about 20% for lithium), stop drawing and preserve it for phone and comms. A dead battery helps no one.

A few practical habits make the playbook smoother. Keep the battery's charging cable and your machine's DC cable (if you have one) in the same drawer as the battery — hunting for cables in the dark is avoidable stress. If your station has a display, learn what the battery percentage and watt draw screens show before you need them. And once a season, do a **test night**: run the CPAP from the battery for one full night so you know the real numbers and the real feel, not just the spec sheet. That rehearsal is worth more than any table.

## Camping and travel sizing

For travel, the same math applies, plus airline rules. **Batteries under 100Wh are generally allowed in carry-on; 101–160Wh typically need airline approval**. A 300Wh station won't fly in carry-on — you'd need a smaller dedicated battery or a checked-bag approach, and rules change, so check with your airline before you fly.

For camping, solar top-up during the day extends your nights. A 100W panel in 4 good sun hours at 80% efficiency delivers about **320Wh** — nearly one no-humidifier night. See our [how long will a 100Ah battery run](/pages/how-long-will-100ah-battery-run.html) guide for the refill math.

## Integration with a solar setup

If you already have solar, the CPAP is just another load. To cover one no-humidifier night (360Wh) with 4 good sun hours: 360 ÷ (4 × 0.8) = **~113W of panels**. With the humidifier (720Wh): 720 ÷ 3.2 = **~225W**. That's a modest addition to most arrays — see our [solar system sizing](/pages/solar-system-sizing.html) guide for the full method, and our [what size solar generator to run a refrigerator](/pages/what-size-solar-generator-run-refrigerator.html) guide for the same sizing approach applied to another critical load.

**Cold nights cut capacity.** Below about 0°C, lithium capacity drops roughly 20%, and lead-acid loses more. If you're camping in winter, size up or keep the battery insulated. The same cold note applies to the runtime formula in our [100Ah guide](/pages/how-long-will-100ah-battery-run.html).

## Safety and machine notes (non-medical)

This is electrical, not medical — but a few practical notes:

- **Use manufacturer-approved DC cables** where offered. Third-party cables can be electrically incompatible with your machine's input.
- **Avoid cheap modified-sine inverters** on sensitive electronics. Pure sine is the safer choice — see our [pure sine vs modified sine inverter](/pages/pure-sine-vs-modified-sine-inverter.html) guide.
- **Don't touch pressure settings or firmware.** Those are therapy settings. Any question about your treatment goes to your prescriber, not a battery guide.
- **Read your machine's manual** for its actual input requirements before buying anything.

{{< product-box asin="B084DB36KW" name="LiTime 12V 100Ah LiFePO4" label="The deep-cycle CPAP bank" description="1,280Wh of usable-capacity chemistry (100Ah at 12.8V, 80-100% DoD) — at 40-60Wh per CPAP night that is over a week of runtime, and it doubles as the cabin/RV bank the rest of the year. Pair with a 12V DC cable for your machine to skip inverter losses." button="Check price on Amazon" >}}




<a href="/diy-off-grid-energy/diy-hand-crank-generator-emergency-charging.html" class="text-link">Hand-crank charging: what it can actually power</a>

## FAQ

{{< faq "Can a 300Wh station run my CPAP for one night?" >}}
Barely, and only without the humidifier. At 45W for 8h you need 360Wh; a 300Wh station at 80% DoD gives ~240Wh usable — about 0.7 nights. It's an emergency buffer, not a full-night solution.
{{< /faq >}}

{{< faq "Can I run my CPAP from a power station?" >}}
Yes, if the station's continuous watts cover your machine's draw and its battery Wh covers the night. A 100Ah lithium station (960Wh usable) runs a 45W CPAP about 2.7 nights without the humidifier. Check your machine's label first.
{{< /faq >}}

{{< faq "Can I use the heated humidifier on battery?" >}}
You can, but it roughly doubles consumption — a 100Ah lithium battery drops from ~2.7 nights to ~1.3. Whether to run it is a therapy question for your prescriber; the electrical cost is what we can tell you.
{{< /faq >}}

{{< faq "Can I fly with my battery?" >}}
Batteries under 100Wh are generally allowed in carry-on; 101–160Wh typically need airline approval. Rules change, so confirm with your airline before flying.
{{< /faq >}}

{{< faq "Should I get a whole-house battery instead?" >}}
If you already have solar or want to power more than the CPAP, a whole-house battery (5kWh+) covers many nights and other loads. But it's a bigger investment. A 100Ah lithium station is a cheaper, portable first step. See our [solar generator](/pages/solar-generator.html) and [battery capacity](/pages/battery-capacity.html) guides for the trade-offs.
{{< /faq >}}

## Image Prompts

1. **Placement: H2-1, beside the label-reading section.** Concept: a close-up of a CPAP machine's spec label with the volts and amps circled in a bright callout ring, and a small "V × A = W" equation badge beside it. Composition: label centered and slightly angled, shallow depth of field, warm neutral background, crisp text readable at thumbnail size, photorealistic, 16:9.

2. **Placement: H2-3, above the nights-per-battery table.** Concept: a vertical ladder graphic with four rungs — 300Wh, 500Wh, 100Ah, 200Ah — each rung labeled with nights without humidifier, and a small moon icon per night. Composition: ladder centered on a clean white background, flat infographic style, warm neutral palette, clear night counts, readable at thumbnail size, 16:9.

3. **Placement: H2-4, in the outage playbook.** Concept: a decision card showing a CPAP icon on a battery, with two branches — "humidifier on" and "humidifier off" — each leading to a night-count badge, and a small "stop at 20%" marker. Composition: card centered, two clean branches, flat illustration style, calm blue and green palette, minimal text, 16:9.
