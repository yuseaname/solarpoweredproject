+++

title = "Peak Sun Hours by State: The Number Behind Every Solar Estimate"
slug = "peak-sun-hours-by-state"
date = 2026-09-05
draft = false
description = "Peak sun hours by US region with the seasonal swing that changes panel counts, plus a calculator that turns your local number into daily watt-hours."
image = "/images/peak-sun-hours-by-state/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
related = [
  "/pages/solar-panel-output.html",
  "/pages/solar-system-sizing.html",
  "/pages/solar-panel-angle-calculator.html"
]
+++

{{< affiliate-disclosure >}}

## Quick answer

A **peak sun hour** is one hour of sunlight at 1,000 W/m² — the industry-standard unit that converts panel watts into daily energy. Most US locations get **3.5–6.5 peak sun hours per day** on an annual average: the Southwest sits at 6+, the Sun Belt around 5–6, the Midwest and Mid-Atlantic around 4.2–4.9, and the Northwest and Northeast around 3.5–4.5. The number that actually decides your panel count is your **worst month** (winter typically runs 50–65% of the annual average), not the brochure average. Use the regional table below, then your exact location's number from NREL's PVWatts tool.

**How to read this page:** regional bands below are drawn from the US Energy Information Administration's solar-resource maps (eia.gov, based on NREL's National Solar Radiation Database — retrieved 2026-09-05) and rounded conservatively into bands; for any specific address, NREL's PVWatts calculator (pvwatts.nrel.gov) is the authoritative source and takes thirty seconds. This site tests nothing and sells nothing on this page — the number is the product.

## Why peak sun hours (not daylight hours)

A panel's rated watts are measured at 1,000 W/m² of irradiance. Morning light, dusk, clouds, and winter angles all deliver less. "Peak sun hours" collapses all of that into one number: **how many hours of full-strength sun your location averages per day**. Daily energy is then simple:

**Panel watts × peak sun hours × ~0.75 system efficiency ≈ daily watt-hours**

Worked: a 400W panel at 4.5 peak sun hours → 400 × 4.5 × 0.75 ≈ **1,350Wh/day** (annual-average conditions). The full method and the efficiency factors live in our <a href="/pages/solar-panel-output.html" class="text-link">panel output guide</a>.

## Regional peak-sun-hour bands (annual average)

| Region (representative states) | Annual avg PSH/day | Winter (worst-month) band | Summer band |
| :-- | :-- | :-- | :-- |
| **Desert Southwest** (AZ, NV, NM, inland CA) | 6.0–7.0 | 4.5–5.5 | 7.0–8.0 |
| **Sun Belt** (TX, OK, southern CA coast, FL south, GA, LA) | 5.0–6.0 | 3.8–4.8 | 6.0–7.0 |
| **Mid-Atlantic / Midwest** (VA, NC north, OH, IN, MO, KS, CO front range) | 4.2–4.9 | 2.7–3.6 | 5.2–6.2 |
| **Northeast** (NY, PA north, New England, MI, WI) | 3.8–4.5 | 2.2–3.0 | 4.8–5.8 |
| **Pacific Northwest / cloud-belt** (WA west, OR west, AK) | 3.3–4.2 | 1.6–2.4 | 4.5–5.8 |
| **Mountain-high** (UT, WY, ID, MT high country) | 4.8–5.8 | 3.0–4.2 | 6.0–7.2 |

Reading notes: bands are annual averages for typical locations in each region — a valley fog pocket or a high south-facing slope moves you within (or past) the band, which is why PVWatts-by-address is the final word. Alaska spans the widest range in the country. Florida's summer monsoon season trims its summer band despite the latitude.

## Peak sun hours calculator (watts → daily Wh, seasonal)

<form id="psh-form" class="space-y-4 p-4 bg-gray-50 rounded-lg border border-gray-200">
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
    <div>
      <label class="block text-sm font-medium text-gray-700" for="psh-hours">Your peak sun hours / day</label>
      <input type="number" id="psh-hours" value="4.5" min="1" max="8" step="0.1" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="psh-watts">Total panel wattage (W)</label>
      <input type="number" id="psh-watts" value="400" min="1" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
    </div>
  </div>
  <button type="submit" class="px-4 py-2 rounded-md bg-blue-600 text-white font-medium hover:bg-blue-700">Estimate daily output</button>
  <div id="psh-result" class="mt-4 p-4 bg-white rounded-md border border-gray-200 text-gray-800 hidden"></div>
</form>

{{< toolscript id="psh-calc" >}}
  function pshFmt(n){ return n.toLocaleString(undefined, {maximumFractionDigits: 0}); }
  function pshCalc(){
    var hours = parseFloat(document.getElementById('psh-hours').value) || 0;
    var watts = parseFloat(document.getElementById('psh-watts').value) || 0;
    var eff = 0.75;
    var daily = watts * hours * eff;
    var winter = watts * (hours * 0.6) * eff;
    var summer = watts * (hours * 1.25) * eff;
    var box = document.getElementById('psh-result');
    if (daily > 0) {
      box.innerHTML = '<p class="font-medium">Estimated daily output (at 0.75 system efficiency):</p>' +
        '<ul class="list-disc pl-5 mt-1 space-y-1">' +
        '<li><strong>Annual average:</strong> ' + pshFmt(daily) + ' Wh/day (' + pshFmt(daily*30/1000) + ' kWh/month)</li>' +
        '<li><strong>Winter band (60% of sun hours):</strong> ' + pshFmt(winter) + ' Wh/day</li>' +
        '<li><strong>Summer band (+25%):</strong> ' + pshFmt(summer) + ' Wh/day</li></ul>' +
        '<p class="text-sm text-gray-600 mt-2">Size year-round arrays on the winter row.</p>';
      box.classList.remove('hidden');
    } else {
      box.classList.add('hidden');
    }
  }
  document.getElementById('psh-form').addEventListener('submit', function(e){ e.preventDefault(); pshCalc(); });
  pshCalc();
{{< /toolscript >}}

The calculator applies the site-standard 0.75 system-efficiency factor (controller, wiring, heat) and shows the winter band at 60% of your entered sun hours — plan array size on the winter row if you need year-round power. The <a href="/pages/solar-panel-output.html" class="text-link">full output calculator</a> adds panel count and climate presets.

## How the number changes your panel count

Two worked examples, same 2,000Wh/day cabin load (0.75 efficiency):

-   **Phoenix-class (5.5 annual, 4.8 winter):** winter needs 2,000 ÷ (4.8 × 0.75) ≈ **556W** of panel.
-   **Seattle-class (3.8 annual, 2.0 winter):** winter needs 2,000 ÷ (2.0 × 0.75) ≈ **1,333W** — more than double the array for the same winter power.

That is the entire argument for knowing your worst-month number before buying anything: it can double your panel budget. The complete load-planning method is our <a href="/pages/solar-system-sizing.html" class="text-link">system sizing guide</a>, and the seasonal-tilt side of the same problem is in the <a href="/pages/solar-panel-angle-calculator.html" class="text-link">panel angle calculator</a>.

## Frequently Asked Questions

{{< faq "What is a peak sun hour exactly?" >}}
One hour of sunlight at 1,000 watts per square meter — the irradiance at which panels are rated. Six hours of weak morning light might add up to only one peak sun hour; that is why the unit exists: it converts any day's mixed conditions into "equivalent full-strength hours."
{{< /faq >}}

{{< faq "Why does my state's number come as a range?" >}}
Because solar resource varies within states — elevation, fog belts, valley haze, lake effect. The regional bands here are planning bands; NREL's PVWatts (pvwatts.nrel.gov) gives a point estimate for any address from the National Solar Radiation Database, and it is the number to use for a real design.
{{< /faq >}}

{{< faq "Should I size my system on annual average or winter sun hours?" >}}
Winter, if you need power year-round — winter typically runs 50–65% of the annual-average figure in most of the US. Size on the annual average only if the system's job is seasonal (an RV used April–October, a cabin used in summer).
{{< /faq >}}

{{< faq "Do solar panels still produce on cloudy days?" >}}
Yes, but roughly 10–25% of rated output under heavy overcast — that is already priced into the sun-hours average. A storm-week plan needs either battery reserve, a generator, or both; the honest version of that tradeoff is in our battery-backup-vs-generator comparison.
{{< /faq >}}

{{< faq-schema >}}

## Next logical reads

<a href="/pages/solar-panel-output.html" class="text-link">Solar panel output calculator</a> <a href="/pages/solar-system-sizing.html" class="text-link">How to size a solar system</a> <a href="/pages/solar-panel-angle-calculator.html" class="text-link">Panel angle calculator</a> <a href="/pages/how-to-calculate-solar-load.html" class="text-link">How to calculate your solar load</a>
