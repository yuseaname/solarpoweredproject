+++
title = "What Size Solar Generator to Run a Well Pump? The 240V Problem, Honestly"
slug = "solar-generator-well-pump-sizing"
date = 2026-09-06
draft = false
description = "Most well pumps are 240V submersibles most power stations can't run. The honest sizing math: surge, runtime per gallon, and which stations actually output 240V."
image = "/images/solar-generator-well-pump-sizing/hero.webp"
image_alt = "Wall-mounted home battery unit installed in a utility room beside a water heater — the water-system backup problem in one picture"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
related = [
  "/pages/what-size-solar-generator-run-refrigerator.html",
  "/pages/solar-generator.html",
  "/pages/solar-battery-backup-vs-generator.html"
]
+++

{{< affiliate-disclosure >}}

## Quick answer

**The size most people ask for and the size they need are different questions, because most deep-well pumps run on 240V — and almost every popular 1–2kWh power station only outputs 120V.** No amount of wattage fixes the voltage mismatch: a ½ HP submersible needs ~900–1,200 running watts and **2,200–3,500W of starting surge at 240V** (typical figures from pump-industry sizing guides and nameplate math; verify your own pump's plate). Your real options: (1) a 120/240V-capable station rated ~4,000W+ (EcoFlow DELTA Pro 3 and Anker SOLIX F3800 are the current single-unit examples — specs below), (2) a 240V generator with a transfer switch — often the honest budget answer, or (3) if your water comes from a shallow well with a 120V jet pump, the ordinary 1–2kWh station class genuinely works. We'll run all three calculations.

This page is sizing arithmetic and manufacturer-published specs — nothing here was bench-tested by us, and surge behavior varies pump to pump. Check your pump's nameplate before buying anything.

## Step 0: identify your pump (this decides everything)

| Pump type | Voltage | Typical running watts | Typical starting surge | Station-friendly? |
| :-- | :-- | :-- | :-- | :-- |
| Deep-well submersible (½–1½ HP, most rural wells) | **240V** | ~900–1,200W (½ HP); ~1,840W (1 HP) | 2–3× running: ~2,200–3,500W (½ HP); ~5,500W+ (1 HP) | Only 240V-capable stations |
| Shallow-well jet pump (½–1 HP, wells to ~25 ft) | 120V (most) | ~600–1,000W | ~1,800–2,700W | **Yes** — 1–2kWh class works |
| 12V/24V DC pressure pumps (RV, cabin, tiny house) | 12/24V DC | 50–300W | 2–3× running | Any station with DC output or small inverter |

*Surge multiplier per pump-industry sizing practice (motor inrush 2–3×); running watts per manufacturer sizing guides and the standard V×A nameplate math. Your pump's nameplate is the authority.*

The label on the pressure tank or the well cap, the breaker size in your panel (a 2-pole breaker = 240V), or the control box tells you which row you're in. If it says 230V or 240V and two hots — you're in row one, and the popular stations are out.

## Why the voltage wall is absolute

A 120V-only inverter cannot produce 240V — there is no adapter, cable, or "surge protector" that changes this. Split-phase 240V is two 120V legs 180° out of phase; the station has to be built to output both. So the BLUETTI AC180 / Jackery Explorer 1000 class — perfectly good hardware, and exactly what our [refrigerator sizing page](/pages/what-size-solar-generator-run-refrigerator.html) recommends for fridges — is simply the wrong tool for a submersible. Anyone telling you otherwise is selling something.

## Option 1: a 240V-capable station (the money answer)

Two current single-unit examples that output both 120V and 240V (specs per manufacturer/retailer listings, retrieved 2026-09-06; both expandable with extra batteries):

| Spec | EcoFlow DELTA Pro 3 | Anker SOLIX F3800 |
| :-- | :-- | :-- |
| Rated AC output | 4,000W | 6,000W |
| Voltage | 120V/240V in one unit | 120V/240V split-phase |
| Capacity (base unit) | 4,096Wh (LFP), expandable | 3,840Wh (LFP), expandable |
| Surge handling | EcoFlow's own well-pump guide sizes it for 1½–2 HP submersibles | 9,000W surge per manufacturer |
| Solar input | up to 2,600W | 2,400W |

BLUETTI's route is different: the AC500 needs **two units bonded** for 240V split phase — workable, more modular, more assembly. (All per manufacturer documentation; we've tested none of it.)

**The sizing math for a ½ HP submersible:** running ~1,000W, starting ~3,000W at 240V → either unit clears the surge (per the manufacturers' own compatibility guides) and runs the pump with the whole rest of its capacity available for fridge/freezer/internet — which is why these are "home backup" class rather than "gadget" class products.

**Runtime per day — the honest good news.** Pumping water is energetically cheap. Lifting 250 gallons (≈946 kg) up a 200-ft (61 m) well is m·g·h ≈ 946 × 9.81 × 61 ≈ **157Wh of hydraulic work**; at a realistic 45–55% wire-to-water efficiency for a small submersible, that's roughly **290–350Wh of electricity per day** for a typical household's water. A 4kWh-class station pumps your household water for the better part of a week. The surge is the hard part, not the energy.

## Option 2: a 240V generator (the budget answer)

A quality 4,000W+ dual-fuel inverter generator with a 240V outlet, a **transfer switch or inlet box installed by an electrician**, and a pressure tank that limits cycles: often **half the cost** of a 4kWh 240V station for unlimited runtime. The tradeoffs are the ones in our [solar battery vs generator](/pages/solar-battery-backup-vs-generator.html) comparison: fuel logistics, noise, maintenance, and the fact that it's backup-only, not solar-rechargeable. For an outage-focused household on a budget, this is frequently the honest recommendation — a site that earns your trust saying so earns it back later.

## Option 3: the 120V path (if your pump cooperates)

Shallow-well jet pumps (120V) and 12V DC pressure pumps are the stations' home turf:

- **½ HP 120V jet pump:** ~600–900W running, ~1,800–2,700W starting → a station with **1,800W+ rated output and ~2,700W+ surge** runs it (the [BLUETTI AC180 class](/pages/what-size-solar-generator-run-refrigerator.html) — 1,152Wh, 1,800W — sits right at this line; check your pump's nameplate surge).
- **12V DC diaphragm pumps (RV/cabin class):** 50–300W — practically any station runs these, and a 100Ah LiFePO4 + small inverter does it without a station at all ([our 100Ah runtime math](/pages/how-long-will-100ah-battery-run.html)).

If you're *designing* an off-grid water system rather than backing up an existing one, choosing a 120V jet pump or a DC pump up front is what makes the affordable station class usable.

## The soft-start wildcard

A soft-start kit (or a VFD pump controller) reduces a submersible's inrush toward its running current — pump-industry practice for generator and inverter sizing. It can shrink the station class you need (and is standard on many modern pumps). It's electrical work on a 240V circuit: licensed-electrician territory, and it changes the surge row of the table above in your favor. Verify your pump model's compatibility before counting on it.

## Safety and wiring notes (non-negotiable)

- **Never backfeed a panel** from any station or generator. A proper transfer switch or interlock, installed to code, is the only connection to household wiring.
- **Grounding and bonding** for a permanently installed station or generator follow your local code — this is inspection-grade work.
- The 240V stations above are heavy, and their solar-input windows assume big arrays; read our [inverter loading guide](/pages/inverter-loading-derating-guide.html) for why running anything at 100% of rated watts is the wrong habit.

## Frequently Asked Questions

{{< faq "Can a Jackery or BLUETTI 1000Wh station run my well pump?" >}}
Not a submersible — those are 240V, and those stations are 120V-only; voltage can't be adapted up. If your pump is a 120V shallow-well jet pump, check its nameplate: roughly 600–1,000W running and up to ~2,700W starting is borderline for the 1,000Wh class and comfortable for the 1,800W-output class.
{{< /faq >}}

{{< faq "How many watts does a well pump use per day?" >}}
For a typical household drawing ~250 gallons/day from ~200 ft, the physics works out to roughly 300Wh/day of electricity (hydraulic lift at realistic pump efficiency). The starting surge — not daily energy — is what sizes the inverter.
{{< /faq >}}

{{< faq "What size solar generator runs a 1 HP submersible?" >}}
Plan for ~1,840W running and ~5,500W starting at 240V (industry inrush multipliers): a 4,000W-class 120/240V station (DELTA Pro 3 per EcoFlow's own pump guide) or the 6,000W Anker F3800, or a 5,000W+ 240V generator. A soft-start kit on the pump can pull those numbers down.
{{< /faq >}}

{{< faq "Is a generator better than a power station for well-pump backup?" >}}
Often yes, on cost: a 4,000W+ 240V inverter generator plus transfer switch typically costs far less than a 4kWh 240V station and runs as long as you feed it. The station wins on silence, indoor safety, and solar recharging. The full tradeoff table is in our battery-vs-generator guide.
{{< /faq >}}

{{< faq "Can I use a pressure tank to reduce the load?" >}}
A pressure tank doesn't change the pump's draw — it changes how often the pump starts. A larger tank means fewer, longer cycles, which reduces total starts per day and surge events. Worth having, but it doesn't shrink the inverter you need for each start.
{{< /faq >}}

{{< faq-schema >}}

## Next logical reads

<a href="/pages/what-size-solar-generator-run-refrigerator.html" class="text-link">What size station runs a refrigerator</a> <a href="/pages/solar-generator.html" class="text-link">Solar generators: the honest guide</a> <a href="/pages/solar-battery-backup-vs-generator.html" class="text-link">Solar battery vs generator</a> <a href="/pages/solar-inverter-sizing.html" class="text-link">Inverter sizing</a> <a href="/pages/how-long-will-100ah-battery-run.html" class="text-link">100Ah battery runtime math</a>

{{< product-box asin="B0D14FMFZD" name="EF ECOFLOW DELTA Pro 3 Portable Power Station, 4096Wh" label="The single-unit 240V answer" description="4,000W rated AC with native 120V/240V output in one unit, 4,096Wh LiFePO4 expandable to 48kWh, up to 2,600W solar input (per manufacturer/retailer listing, retrieved 2026-09-06); EcoFlow's own well-pump guide sizes it for 1½–2 HP submersibles. Not for: budget-first backup where a 240V generator and transfer switch do the same job for less, or 120V-only loads that don't need this class. The honest tradeoff: whole-home-class capability at whole-home-class cost, and the surge headroom only pays off if you actually have a 240V load like a submersible pump." button="Check price on Amazon" >}}
