+++

title = "Solar Panels in Series vs Parallel: Which Wiring Is Better for Your Setup?"
slug = "solar-panels-series-vs-parallel"
date = 2026-05-31
draft = false
description = "Series vs parallel solar panels explained with a practical decision guide: voltage vs current, shading tradeoffs, controller limits, and common mistakes."
image = "/images/solar-panels-series-vs-parallel/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
+++

{{< affiliate-disclosure >}}

<a href="#key-takeaways" class="text-link">Key takeaways</a> <a href="#quick-decision-guide-choose-this-if" class="text-link">Quick decision guide</a> <a href="#the-one-concept-that-makes-it-click-voltage-up-vs-current-up" class="text-link">The concept that makes it click</a> <a href="#series-voltages-add-current-stays" class="text-link">When series is usually better</a> <a href="#parallel-currents-add-voltage-stays" class="text-link">When parallel is usually better</a> <a href="#how-this-interacts-with-mppt-vs-pwm-plain-language" class="text-link">How this interacts with MPPT vs PWM</a> <a href="#common-mistakes-and-what-they-look-like" class="text-link">Common mistakes</a> <a href="#faq" class="text-link">FAQ</a>

**Short answer:** wire in **series** when you want higher array voltage — longer cable runs, thinner copper, and an MPPT controller that thrives on voltage headroom — and shading is minimal or consistent. Wire in **parallel** when partial shading is common, when your controller or battery bank demands low voltage, or when you want to add panels one at a time without disturbing the existing string. An MPPT controller makes series practical; with PWM, keep the array voltage closely matched to the battery bank instead. The arithmetic is below.

**How to read this page:** this is a physics-based comparison, not a test report — we test nothing on this site. The examples are worked from stated panel inputs (18V Vmp, 22V Voc, 5.56A Imp class) and standard solar electrical relationships, with the code citations named (NEC 690.8 and 690.9) so you can verify them. Ranges describe what actually varies with conditions; where a number is a planning estimate it is labeled as such. The full criteria behind how this site recommends gear are on our <a href="/pages/how-we-recommend.html" class="text-link">how we recommend</a> page.

## Key takeaways

-   **Series** increases array voltage; **parallel** increases array current.
-   Series often helps with longer wire runs; parallel can be more forgiving in partial shading situations.
-   Your charge controller’s voltage/current limits are the hard boundaries—design inside them.

<a href="solar-system-sizing.html" class="text-link">How to size a solar system (start here)</a>

## Quick decision guide (choose this if…)

-   **Choose series** if you have longer cable runs, you’re using an MPPT controller, and shading is minimal/consistent.
-   **Choose parallel** if partial shading is common (trees, vents), or you need to keep voltage low due to controller limits.
-   **Choose series-parallel** (a mix) when you need both: higher voltage than pure parallel, but not as shade-sensitive as a long series string.

The reader is the hero: your job is simply to pick the wiring that prevents the two failures people hate—wasted solar production and wiring that runs too hot.

## Comparison table: series vs parallel at a glance

| Factor | Series | Parallel |
| :-- | :-- | :-- |
| Voltage behavior | Voltages add; current stays the same | Voltages stay the same; currents add |
| Current behavior | String current equals one panel's current | Array current equals the sum of all strings' currents |
| Shading impact | One shaded panel drags the whole string down; group panels with similar sun in the same string | Each string keeps producing independently, so shade hits only the affected string |
| Overcurrent protection needed | One string: usually none beyond controller protection | Each string needs its own fuse at Isc × 1.56 (NEC 690.9(B)); fused per string at the combiner |
| Wire-gauge economics | Same power at lower current — thinner wire and lower voltage drop over long runs | Same power at higher current — thicker wire; check <a href="solar-wire-size.html" class="text-link">wire size</a> before committing |
| Cold-weather Voc risk | Voc adds up fast — check cold-adjusted string Voc against controller limits (see worked math) | Voc stays at one panel's level, so less cold-voltage headroom risk |
| Best for | Long runs, MPPT setups, minimal/consistent shading | Partial shading, low-voltage controller limits, adding panels one at a time |

That said, wiring choice never happens in a vacuum: what your controller can accept decides how far either direction can go.

## The one concept that makes it click: voltage up vs current up

Wiring in **series** adds voltage (like stacking batteries end-to-end). Wiring in **parallel** adds current capacity (like widening the pipe).

**Why it matters:** higher current usually drives thicker wire and higher-rated protection devices.

<figure>
<img src="../assets/images/solar-cells-interconnections.jpg" loading="lazy" width="1535" height="767" alt="Diagram of solar cells wired in series and parallel showing voltage and current changes." />
<figcaption>Image: “Sketch of silicon solar cells interconnections” by Cesardd, CC BY-SA 4.0 — Source: <a href="https://commons.wikimedia.org/wiki/File:Sketch_of_silicon_solar_cells_interconnections.jpg" class="text-link">Wikimedia Commons</a></figcaption>
</figure>

## The worked math: the same three 100W panels, both ways

All arithmetic below uses the same stated inputs so you can re-run it with your own panel's spec sheet. **Stated inputs:** three 100W panels, each rated 18V Vmp and 22V Voc, with a working current in the 5.56A Imp class (100W ÷ 18V = 5.56A). That is the class this site's spec reads use for a typical 100W "12V" panel.

### Series: voltages add, current stays

Three panels in series give you one string with:

-   String Vmp = 18V × 3 = **54V**
-   String Voc = 22V × 3 = **66V**
-   Current stays at one panel's current: **~5.56A**

Total power is unchanged — 54V × 5.56A ≈ 300W, the same 300W as the panels' ratings. What changes is how that power is delivered: at 54V it arrives at one-third the current of a parallel array.

**Why that helps wire loss.** Loss in a cable grows with the square of current: loss = I² × R. Halving current quarters the loss on the same wire. One-line numeric example: two different arrays delivering the same power on the same 25-foot, 10 AWG run (roughly 0.05Ω round trip at ~1 mΩ/ft per conductor), one at 5.56A and one at 16.7A:

-   5.56A² × 0.05Ω ≈ **1.5W** lost
-   16.7A² × 0.05Ω ≈ **13.9W** lost — about nine times more, because 16.7 ÷ 5.56 = 3, and 3² = 9.

That "nine times" gap is the real series advantage on a long run. It is why <a href="solar-wire-size.html" class="text-link">wire size</a> and wiring choice are the same conversation.

**The cold-weather check (series).** Panel Voc rises roughly 0.3% per °C below 25°C. Three panels at 66V STC on a −10°C morning (35°C below STC):

-   66V × (1 + 0.003 × 35) ≈ 66V × 1.105 ≈ **73V**

That is the number your controller's max input voltage must clear. Four panels would give 88V × 1.105 ≈ 97V — under a 100V controller with almost no margin. Run this check for your coldest expected temperature, not the average. Our <a href="solar-fuse-and-breaker-sizing.html" class="text-link">fuse and breaker sizing guide</a> and <a href="solar-wire-size.html" class="text-link">wire size guide</a> cover the wiring side of the same decision.

### Parallel: currents add, voltage stays

The same three panels wired in parallel keep one panel's voltage and add current:

-   Array Vmp = 18V (unchanged); array Voc = 22V (unchanged)
-   Array current ≈ 5.56A × 3 = **~16.7A**

Same ~300W total — 18V × 16.7A ≈ 300W — delivered at three times the current.

**Why each string needs a fuse.** In a parallel array, a faulted string can be backfed by the healthy strings, so each string gets its own overcurrent device. Sized per the National Electrical Code, as this site does elsewhere: **NEC 690.8(A)** sets a PV circuit's maximum current at the panel's short-circuit current Isc × 1.25, and **NEC 690.9(B)** requires the overcurrent device rated at no less than 125% of that — the combined Isc × 1.56 string-fuse rule. Worked, using the ~6A Isc that typically accompanies a 100W panel (with Isc slightly above Imp):

-   Max circuit current = Isc × 1.25 = 6A × 1.25 = **7.5A**
-   String fuse = Isc × 1.56 = 6A × 1.56 ≈ **9.4A**, rounded up to a **15A** string fuse

From here, parallel-string wiring runs on that higher current and dictates thicker conductors — sized to at least 125% of the circuit's maximum current per **NEC 690.8(B)**. Conductor sizing and protection sizing are covered properly in our <a href="solar-fuse-and-breaker-sizing.html" class="text-link">solar fuse and breaker sizing</a> and <a href="solar-wire-size.html" class="text-link">solar wire size</a> guides.

## When series is usually better (and the main tradeoff)

### Longer wire runs (voltage drop advantage)

Higher array voltage often means lower current for the same power, which reduces voltage drop and can simplify wiring—especially when panels are far from the controller.

<a href="solar-wire-size.html" class="text-link">Solar wire size (amps + distance)</a>

### MPPT controllers and higher array voltage

MPPT controllers are often more flexible with higher input voltages (within limits) and can convert that voltage efficiently into battery charging current. This is a common reason people choose series strings.

<a href="mppt-vs-pwm.html" class="text-link">MPPT vs PWM</a>

### The tradeoff: shading and mismatch can hurt more

In a series string, one weaker panel can pull down the string’s output. Good design tries to keep panels in a string seeing similar conditions.

## When parallel is usually better (and the main tradeoff)

### Partial shading and uneven conditions

If you expect frequent partial shading (roof vents, trees, seasonal shadows), parallel wiring can reduce how much one shaded panel affects the rest of the array.

### The tradeoff: more current (often thicker wire + bigger protection)

Parallel wiring typically means higher array current, which can push you toward thicker cable, larger breakers/fuses, or a combiner solution.

<a href="solar-fuses-vs-breakers.html" class="text-link">Solar fuses vs breakers</a> <a href="solar-combiner-box-and-disconnect-guide.html" class="text-link">Combiner boxes and disconnects</a> <a href="solar-wiring-and-protection-cost.html" class="text-link">Wiring &amp; protection cost</a>

## How this interacts with MPPT vs PWM (plain language)

Controller choice can change what “good wiring” means. MPPT often gives you more flexibility to run a higher-voltage array (again: within limits). PWM tends to push people toward keeping array voltage closely matched to the battery bank.

<a href="mppt-vs-pwm.html" class="text-link">MPPT vs PWM: controller comparison</a> <a href="solar-components.html" class="text-link">Charge controllers and batteries (component roles)</a>

## Common mistakes (and what they look like)

-   **Exceeding controller limits:** can cause shutdowns or damage; always design within voltage/current ratings.
-   **Assuming “more panels” fixes shading:** shading is a layout problem first, a panel-count problem second.
-   **Ignoring wire run length:** parallel can punish long distances with higher current and voltage drop.
-   **Mixing mismatched panels:** different specs in the same string often reduce real output.

<a href="solar-output-troubleshooting.html" class="text-link">Low solar output troubleshooting</a>

## FAQ

{{< faq "Is series or parallel “better”?" >}}
Neither is universally better. Series often helps with long runs and MPPT setups; parallel can be more forgiving with partial shading.
{{< /faq >}}

{{< faq "Does series increase watts?" >}}
It increases voltage, not “free power.” Total power depends on sunlight and panel output. Wiring changes how that power is delivered.
{{< /faq >}}

{{< faq "What happens if one panel is shaded?" >}}
Shading can reduce output more in series strings. Design tries to group panels with similar sun exposure in the same string.
{{< /faq >}}

{{< faq "Can I mix series and parallel?" >}}
Yes, many arrays are built as series strings connected in parallel. The safe approach is to keep strings consistent and stay within controller limits.
{{< /faq >}}

{{< faq "Do I need MPPT for series wiring?" >}}
Not always, but MPPT often makes higher-voltage array configurations more practical and efficient (within equipment limits).
{{< /faq >}}

## Next logical reads

<a href="mppt-vs-pwm.html" class="text-link">MPPT vs PWM</a> <a href="solar-wire-size.html" class="text-link">Solar wire size</a> <a href="solar-fuses-vs-breakers.html" class="text-link">Solar fuses vs breakers</a> <a href="solar-panel-output.html" class="text-link">Solar panel output calculator</a> <a href="12v-vs-24v-vs-48v-solar.html" class="text-link">How to choose system voltage</a>

---

**Related guides:**
- [Multi-Source Hybrid Off-Grid Charge Controller: Combine Solar, Wind & Hydro](/diy-off-grid-energy/multi-source-hybrid-charge-controller.html)
- [MPPT Charge Controller Not Charging: Troubleshooting Checklist (PV Voltage, Settings)](/pages/mppt-charge-controller-not-charging.html)
- [Solar Wire Size: How to Choose the Right Gauge (Voltage Drop + Safety)](/pages/solar-wire-size.html)
