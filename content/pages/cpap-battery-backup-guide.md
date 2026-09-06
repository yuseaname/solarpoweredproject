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

{{< product-box asin="B084DB36KW" name="LiTime 12V 100Ah LiFePO4" label="The deep-cycle CPAP bank" description="100Ah at 12.8V — 1,280Wh nameplate (per manufacturer spec), the 100Ah-lithium class the runtime table above sizes at about 2.7 nights without the humidifier and 1.3 with it. It doubles as the cabin/RV bank the rest of the year. Not for: packed travel — at over 100Wh it can't go in an airline carry-on without approval, per the rules above. The honest tradeoff: pair with a 12V DC cable for your machine to skip inverter losses; on AC the inverter eats 10-15%." button="Check price on Amazon" >}}




<a href="/diy-off-grid-energy/diy-hand-crank-generator-emergency-charging.html" class="text-link">Hand-crank charging: what it can actually power</a>

## How long will a power station run a CPAP? (the honest math)

Any "how long will a [brand] run a CPAP" question — Jackery, EcoFlow, Bluetti, no matter — is answered by one formula:

**Runtime (h) = (usable Wh × efficiency) ÷ machine watts**

Three inputs, and only three:

1. **Usable Wh.** A station's rated Wh isn't all deliverable. Plan on ~85% (use 0.85) for an AC port on a lithium machine — that covers inverter overhead plus chemistry. If your station's datasheet quotes a deeper usable depth-of-discharge, run the formula with that number instead; see our [100Ah runtime guide](/pages/how-long-will-100ah-battery-run.html) for the chemistry details.
2. **Machine watts.** Most CPAPs draw **30–60W without the humidifier** and **60–100W with the heated humidifier**, depending on model and pressure setting. Check *your* machine's label (V × A = W) or manual before buying anything — do not size from a friend's number.
3. **Efficiency.** On the AC port, the inverter eats ~10–15%. If your machine has a **12V DC input**, a manufacturer's DC cable skips that loss entirely, and the same Wh runs roughly 15% longer.

Worked examples, a 300Wh station:

- **40W, no humidifier:** 300 × 0.85 = 255 Wh usable; 255 ÷ 40 ≈ **6.4h** on AC — call it 6.5h, and up to ~7.5h on DC (300 ÷ 40 = 7.5). That's where the "6.5–7 hours" figure you'll see quoted comes from.
- **80W, with humidifier:** 255 ÷ 80 ≈ **3.2h ≈ 3h** — one rough night, not two.

Two nights means 16h of runtime. The honest picture for three common station sizes (0.85 usable, 8h nights):

| Power station | Usable Wh (× 0.85) | No humidifier (40W) | With humidifier (80W) |
| --- | --- | --- | --- |
| 268Wh | ~228Wh | ~5.7h (0.7 nights) | ~2.9h (0.4 nights) |
| 512Wh | ~435Wh | ~10.9h (1.4 nights) | ~5.4h (0.7 nights) |
| 1024Wh | ~870Wh | ~21.8h (2.7 nights) | ~10.9h (1.4 nights) |

Only the 1024Wh class reaches two full nights — and only without the humidifier. On 12V DC each row improves roughly 15%: the 268Wh goes to ~6.7h at 40W, the 512Wh to ~12.8h, the 1024Wh to ~25.6h. Sizing for your worst night with your real draw beats any brand's marketing table: re-run the formula whenever the battery or the machine changes, and treat any quoted runtime with no visible Wh-and-watts arithmetic as an ad.

## Camping and flying with a CPAP battery

The lithium rules that decide your travel battery, straight from TSA/FAA:

- **Up to 100Wh:** generally allowed in carry-on without special approval — no airline sign-off needed for the battery itself. A typical 26,800mAh USB-C power bank works out to ~99.2Wh (26.8Ah × 3.7V), just under the line.
- **101–160Wh:** need airline approval; most airlines allow them, typically at most **two spares** per passenger.
- **Over 160Wh:** forbidden on passenger aircraft — not in carry-on, not in checked luggage.
- **Spares: carry-on only, never checked.** Power banks and spare lithium batteries are prohibited in checked baggage; if your carry-on gets gate-checked, pull the battery out and keep it with you. The CPAP machine itself isn't the regulated item — the battery is.

<!-- Sources verified 2026-09-05: TSA "Power Banks" https://www.tsa.gov/travel/security-screening/whatcanibring/items/power-banks ; TSA "Lithium batteries with more than 100 watt hours" https://www.tsa.gov/travel/security-screening/whatcanibring/items/lithium-batteries-more-100-watt-hours ; FAA PackSafe for Passengers https://www.faa.gov/hazmat/packsafe ; FAA PackSafe – Lithium Batteries https://www.faa.gov/hazmat/packsafe/lithium-batteries -->

That's the flying half. The camping half is three habits:

- **Skip the humidifier.** It's the biggest single saving: it roughly doubles your draw (60–100W → 30–60W), which roughly doubles your nights. Whether that's livable for you is a therapy question for your prescriber; the electrical difference is ours to quote.
- **Use 12V DC if you can.** A manufacturer-approved DC cable runs the machine straight from a 12V source, skipping the inverter's ~10–15% loss — same battery, roughly 15% more runtime.
- **Bank vs station.** A sub-100Wh bank is flyable and cheap, but it only helps if your manual says the machine can run from DC or USB-C. A 300–500Wh-plus station gives one to three nights but stays home or in the car — it can't fly. Choose by your actual travel: flyers shop under 100Wh, campers shop the station.

Airlines may impose stricter limits than TSA/FAA, and the TSA officer has the final word at the checkpoint — confirm with your airline before you fly, and keep battery terminals protected (tape or a case) so they can't short out.

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
