+++
title = "Faraday Cages for Solar Electronics: What Actually Works (EMP Physics, Audited)"
slug = "faraday-cage-solar-electronics"
date = 2026-10-30
pagetype = "informational"
draft = false
description = "What a Faraday cage can and cannot do for charge controllers, inverters, and radios: cage physics explained honestly, CME versus HEMP threat differences, a falsifiable DIY attenuation test, and how to audit commercial EMP-bag claims."
image = "/images/faraday-cage-solar-electronics/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
related = [
  "/grid-down/rebuilding-power-from-scratch.html",
  "/pages/solar-grounding-and-lightning-protection.html",
  "/pages/how-to-choose-solar-inverter.html",
  "/pages/best-mppt-charge-controllers.html",
  "/grid-down/grid-down-communications-power.html"
]
+++

{{< affiliate-disclosure >}}

<p class="jump-links"><a href="#quick-answer" class="text-link">Quick answer</a> <a href="#what-a-cage-actually-is" class="text-link">What a cage actually is</a> <a href="#know-your-threat-cme-vs-hemp" class="text-link">CME vs HEMP</a> <a href="#what-to-protect-and-why-spares" class="text-link">What to protect</a> <a href="#build-and-test-your-own" class="text-link">Build and test your own</a> <a href="#auditing-commercial-emp-bags" class="text-link">Auditing EMP bags</a> <a href="#faq" class="text-link">FAQ</a></p>

## Quick answer

A Faraday cage — a closed conductive enclosure — really does shield its interior from external electromagnetic fields; that's settled physics, and your microwave's door mesh demonstrates the principle daily. But honest hardening starts with threat triage: for solar electronics, **lightning-induced surges are the documented, routine threat** ([grounding and surge protection](/pages/solar-grounding-and-lightning-protection.html) is the guide that pays off this storm season), while the exotic pulse scenarios are lower-probability and — crucially — a cage only helps if it encloses the *spare* electronics you'll need after the event, not the system you're using. We describe a DIY attenuation test you can run for about the cost of a radio, and we make no performance claims for any specific product — this page audits the claims, it doesn't sell certainty.

## What a cage actually is

The physics, without mystique: place a conductive enclosure in an external electric field and the free charges in the conductor redistribute on its surface until the field inside the conductor is (ideally) zero. This is Faraday's ice-pail result — textbook electromagnetism, reproducible in any classroom.

What that means for a practical cage:

- **Closure matters more than thickness.** A cardboard box wrapped in aluminum foil is a legitimate cage for many purposes; a metal trash can with a loose plastic lid gap is a much worse one. Continuity of the conductive path, not mass, is the design variable.
- **Holes are wavelength-dependent, not forbidden.** A cage with apertures still attenuates strongly when the apertures are small relative to the wavelength. A microwave door's mesh (holes ~1–2mm) contains 2.45GHz radiation (~12cm wavelength) because the holes are a small fraction of it. The same mesh would be far less effective against a 10cm-wavelength-adjacent fast pulse with significant low-frequency content — which is why standards-grade enclosures are solid metal, not mesh.
- **Insulate the contents from the walls.** A device touching the cage wall is on the outside of the shield, electrically. Cardboard or cloth lining inside a metal container is part of the design, not packaging.
- **No through-wires.** A cable entering the cage is an antenna delivering the outside to the inside. A "cage" with a charging cable running through the lid is a decorated box.

<figure>
<img src="/images/faraday-cage-solar-electronics/fig-physics.webp" loading="lazy" width="640" height="427" alt="Physics-diagram illustration: external field lines deflecting around a closed conducting box whose interior stays empty, with induced charge dots on the outer surfaces." />
<figcaption>The physics in one picture: a closed conductor deflects the external field while the interior stays calm — induced charge lives only on the outer surface. (Illustrative)</figcaption>
</figure>

## Know your threat: CME vs HEMP

These get conflated constantly, and the distinction decides what protection even means:

- **Coronal mass ejection (CME)** — solar storm physics. A CME's geomagnetic disturbance induces slow, powerful currents in *long* conductors: transmission lines, pipelines, railways. The historical reference is the 1859 Carrington event; NOAA's geomagnetic storm scale (G1–G5) is the operational yardwatch. The honest engineering summary: CMEs threaten the **grid and its transformers**, and the electronics at risk are those connected to long wires when the grid misbehaves — not free-standing electronics bathed in some field. Your unplugged charge controller is a poor CME target; the grid it depends on is the real one.
- **High-altitude electromagnetic pulse (HEMP, the E1 component)** — nuclear detonation in the upper atmosphere producing a nanosecond-rise electromagnetic pulse that couples into electronics and antennas. This is the threat Faraday enclosures are actually *for*. Public hardening practice for critical infrastructure is codified in military standards (MIL-STD-188-125-1/-2); those documents describe test methods and enclosure classes — a useful anchor when a vendor claims military-grade protection. We will not rate your personal probability of this scenario; we will say the physics is real, the standards exist, and most products marketed around it are unaudited.

The practical asymmetry: you can do useful CME preparation by having **standalone power** (the entire [grid-down project](/grid-down/rebuilding-power-from-scratch.html)) and surge protection at your service entrance. HEMP preparation adds the enclosure layer for *spares*. Neither is served by fear-priced foil bags.

## What to protect, and why spares

A cage around your *operating* system is a contradiction — panels can't charge through solid metal, and the cables that let them would defeat the cage. Hardening is therefore a **spares library**, not a shell over the working hardware:

- One spare charge controller (the component whose sudden death stops all harvest)
- One spare inverter or the means to live without AC
- Spare radios and headlamps ([comms budget](/grid-down/grid-down-communications-power.html))
- Memory sticks with manuals, firmware, wiring diagrams — knowledge is an electronic component too

The logic: after a pulse event, the grid is down and your exposed electronics may be down with it. The caged spares are how the [four-element system](/grid-down/rebuilding-power-from-scratch.html) gets rebuilt on day two. Rotate the spares into service periodically so you're debugging a *known-good* controller, not a five-year-old mystery.

<figure>
<img src="/images/faraday-cage-solar-electronics/fig-spares.webp" loading="lazy" width="640" height="427" alt="Technical-plate illustration: a shelf holding an open cardboard-lined steel can with a controller and radio, a smaller sealed can, and a documents folder with a blank tag." />
<figcaption>The spares library: sealed, lined, labeled — and rotated into service before it becomes a mystery box. (Illustrative)</figcaption>
</figure>

## Build and test your own

A workable home enclosure, materials-first:

1. **Container:** a galvanized steel trash can with a lid (the classic), an ammunition can, or a metal filing cabinet — solid metal, tight-fitting lid, hinges and latch included in the metal path.
2. **Seal the lid gap:** foil tape (conductive adhesive is better) around the lid seam, or lay a fine conductive mesh gasket. The lid-to-body seam is where cheap builds leak.
3. **Insulate:** cardboard or cloth lining so nothing conductive inside touches the walls. Devices in their own bags or boxes first.
4. **No wires through the seal.** Ever.
5. **Label it.** Contents, date sealed, test date.

**The falsifiable test — radio attenuation.** Take a battery-powered AM/weather radio, tune it to a strong local station at full volume, and place it inside the closed cage. A well-sealed enclosure should silence or drastically quiet the reception (AM broadcast wavelengths are huge, making it an easy first test — it is necessary, not sufficient, evidence of good sealing). A microwave oven (unplugged, never activated) does the same demo with a phone's signal. If the radio plays on merrily inside your cage, your seam leaks — fix it before trusting it. This method and its limits are described as engineering practice; we have not laboratory-tested any enclosure, and passing the AM test does not certify performance against a standards-defined pulse. That certification is what MIL-STD-188-125-class testing is for.

## Auditing commercial EMP bags

The marketplace around pulse protection is fear-priced and largely unaudited. A claim ladder, weakest to strongest:

| Claim on the listing | What to demand | Red flags |
| :-- | :-- | :-- |
| "Faraday-style," "signal-blocking" | A demonstration (phone-in-bag loses signal) — meaningful but easy | No testable claim at all |
| "Tested to IEEE 299" (shielding effectiveness) | The actual report: frequency range, dB attenuation, who ran it | Report "available on request" forever |
| "MIL-STD-188-125-1" | Facility test data, enclosure class, and — realistically — this standard applies to *facilities*, and a bag claiming it warrants suspicion | A bag citing a facility standard it wasn't tested to |
| No claims, just vibes | Pass | Price correlates with adjective density |

The meta-principle this whole site runs on applies double here: **an unevidenced claim in a threat-marketed product is the same defect it would be anywhere else.** If a vendor documents real attenuation data, fine. If not, a steel can with a taped seam you tested yourself with a radio is more honest protection than an unaudited bag with a patriot font.

## FAQ

{{< faq "Will a Faraday cage protect my solar panels themselves?" >}}
No — and it can't, because panels must be exposed to light to work. Panels are also among the more robust solar components: no microelectronics in the classic sense. The vulnerable parts are the controller, inverter, and communications gear, which is why hardening means caged *spares*, not shellacked operations.
{{< /faq >}}

{{< faq "Is a solar storm going to fry my off-grid system?" >}}
The physics says CMEs primarily threaten long conductors — the grid — rather than standalone electronics. The realistic CME exposure for an off-grid home is grid-side: if you're truly standalone with proper surge protection, your documented threat ranking remains lightning first, surges second. This page deliberately avoids probability claims about rare events; the mitigation (spares + grounding) is the same either way.
{{< /faq >}}

{{< faq "Does a microwave make a good Faraday cage?" >}}
An unplugged microwave demonstrates cage physics well (try the phone test), and its mesh is engineered for one frequency band. As storage it's awkward and untested across the spectrum that matters — a steel can with a taped seam is the better *and* cheaper container.
{{< /faq >}}

{{< faq "Are EMP bags a scam?" >}}
The honest answer is "mostly unaudited." Some vendors publish real shielding data; many sell adjectives. Use the claim ladder above: demand the report, and treat a steel container you attenuation-tested yourself as the default against which products must beat on evidence, not price.
{{< /faq >}}

{{< faq "What's the first hardening step if I do nothing else?" >}}
Grounding and surge protection — boring, documented, and tested against the threat you will actually face this year. Do that before any enclosure; the [grounding guide](/pages/solar-grounding-and-lightning-protection.html) is the starting point.
{{< /faq >}}
