+++
title = "Battery Backup for an Oxygen Concentrator: The Runtime Math, Honestly"
slug = "battery-backup-oxygen-concentrator"
date = 2026-09-05
draft = false
description = "How long a battery or power station runs an oxygen concentrator: the draw classes, the runtime math, and the layered plan that covers multi-day outages."
image = "/images/battery-backup-oxygen-concentrator/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
related = [
  "/pages/cpap-battery-backup-guide.html",
  "/pages/solar-generator.html",
  "/pages/solar-battery-backup-vs-generator.html"
]
+++

{{< affiliate-disclosure >}}

## Quick answer

A home oxygen concentrator is a **continuous 300–600W load** (read the label on YOUR unit — the class, not the brand, decides everything). That makes battery backup honest arithmetic: a 1,000Wh-class power station runs a 300W concentrator about **3 hours**; a 2–3kWh class runs it **about 5.5–8.5 hours** (per the table below). No battery alone covers a multi-day outage — the honest plan is **layered**: battery for short outages, oxygen tanks as the non-electrical fallback, and a generator for the long tail. **This page is electrical math, not medical advice — plan backup with your oxygen supplier, who is also the right source for tank quantities and delivery.**

**How to read this page:** we test nothing and sell nothing on this page. Draw figures are typical classes from machine labels and user communities (sources noted where cited); your unit's nameplate wattage overrides every number here. For medical questions — required flow rates, backup duration your provider recommends, tank handling — your oxygen supplier and prescriber are the authorities; do not let an electrical guide override them.

## The one number that decides everything: your machine's draw

Home concentrators typically draw **300–600W continuous** (flow-rate dependent — higher liters-per-minute pulls more), with a brief startup surge. Portable oxygen concentrators (POCs) are a different animal: **10–75W class** with their own internal batteries — their backup problem is mostly *charging*, not running. Find your number on the machine's label or manual, then use it in the table below. Community experience matches the math: users running home units on ~1,000Wh stations report roughly three hours (r/OxygenConcentrator and r/batteries threads, retrieved 2026-09-05).

## Runtime table: hours by battery size and draw

Usable capacity ≈ nameplate × 0.85 for power stations; hours = usable Wh ÷ draw.

| Battery (nameplate) | Usable Wh | @300W | @450W | @600W |
| :-- | :-- | :-- | :-- | :-- |
| 500Wh | ~425Wh | ~1.4 h | ~0.9 h | ~0.7 h |
| 1,000Wh | ~850Wh | ~2.8 h | ~1.9 h | ~1.4 h |
| 2,000Wh | ~1,700Wh | ~5.7 h | ~3.8 h | ~2.8 h |
| 3,000Wh | ~2,550Wh | ~8.5 h | ~5.7 h | ~4.3 h |
| 10kWh installed-class | ~9,000Wh | ~30 h | ~20 h | ~15 h |

Two catches the table hides: **surge** — a concentrator's compressor start can spike past its running watts, so the station's surge rating must clear it (the same trap as refrigerators; the math is in our <a href="/pages/what-size-solar-generator-run-refrigerator.html" class="text-link">fridge-sizing guide</a>); and **recharge time** — a 2kWh station refilled by one 200W panel takes days, not hours, in winter light (<a href="/pages/peak-sun-hours-by-state.html" class="text-link">peak sun hours by state</a>).

## The layered plan (what actually covers a multi-day outage)

1.  **Battery/power station — the short-outage layer.** Sized for the *common* outage: enough hours to bridge short cuts without anyone touching anything. For a 450W machine wanting 4 hours: ~2kWh usable.
2.  **Oxygen tanks — the non-electrical layer.** Tanks work with no power at all and are the standard emergency backup. Quantity and delivery scheduling come from your oxygen supplier — this is the layer that covers the battery's runtime ceiling, and only your provider can say how much backup you should keep on hand.
3.  **Generator — the long-tail layer.** For multi-day regional outages (hurricane and ice belts), a generator recharges the battery and carries the house; the honest tradeoffs (fuel, CO safety, noise) are in <a href="/pages/solar-battery-backup-vs-generator.html" class="text-link">battery backup vs generator</a>.
4.  **POC owners:** your math is charging, not running — size a station to refill the POC's own batteries several times over (a 300–500Wh station recharges a typical POC battery many times).

## CPAP is the easier cousin

If you're backing up a CPAP rather than a concentrator, the math is far friendlier: 40–60Wh per night on DC without the humidifier — a small battery runs it for a week. The full runtime table and airline rules are in our <a href="/pages/cpap-battery-backup-guide.html" class="text-link">CPAP battery backup guide</a>.

## Frequently Asked Questions

{{< faq "How long will a Jackery/BLUETTI-class 1,000Wh station run my concentrator?" >}}
About 3 hours at a 300W draw, less at higher flow rates (usable ≈ 850Wh ÷ your label's watts). Check the station's surge rating against the compressor start too. If you need overnight coverage at 450W, you're in the 4kWh class — which is installed-battery or generator conversation.
{{< /faq >}}

{{< faq "Can solar panels run a concentrator directly?" >}}
Not reliably without a big buffer battery: a concentrator runs day and night at 300–600W while panels produce only in daylight. Solar's role is recharging the battery bank between outages — and in winter that recharge is slow. Treat solar as the layer that keeps the battery topped, not as the supply.
{{< /faq >}}

{{< faq "Are generators safe to use with oxygen equipment?" >}}
Engine generators and oxygen therapy require real separation and ventilation planning — follow your oxygen supplier's guidance on distance and indoor/outdoor rules, and carbon monoxide alarms are non-negotiable (CPSC: outdoors only, 20+ feet from the home). The generator's *electricity* is fine; the exhaust and the oxygen environment are the issue your provider should advise on.
{{< /faq >}}

{{< faq "What size whole-home battery covers a concentrator overnight?" >}}
A 450W machine for 12 overnight hours needs ~5.4kWh usable — a 10kWh-class installed battery covers it plus essentials with margin. Installed batteries are quote-and-install products; the five questions to ask an installer are in our home battery guide.
{{< /faq >}}

{{< faq "Is a battery backup required for my oxygen setup?" >}}
That is a question for your oxygen supplier and prescriber, not an electrical guide — providers typically specify a backup plan (often tanks) as part of the therapy plan. This page exists to make the *electrical* half of that plan honest and sized right.
{{< /faq >}}

{{< faq-schema >}}

## Next logical reads

<a href="/pages/cpap-battery-backup-guide.html" class="text-link">CPAP battery backup guide</a> <a href="/pages/solar-generator.html" class="text-link">Solar generator (power station) guide</a> <a href="/pages/solar-battery-backup-vs-generator.html" class="text-link">Battery backup vs generator</a> <a href="/pages/peak-sun-hours-by-state.html" class="text-link">Peak sun hours by state</a>
