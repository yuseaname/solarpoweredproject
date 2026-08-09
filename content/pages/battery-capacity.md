+++

title = "Battery Capacity Calculator for Solar Systems"
slug = "battery-capacity"
date = 2026-05-31
draft = false
description = "Calculate solar battery capacity in Wh and Ah for 12V, 24V, and 48V systems. Enter daily load, days of autonomy, depth of discharge, and inverter efficiency."
image = "/images/battery-capacity/hero.webp"
author = "Solar Powered Project"
updated = 2026-08-09
keywords = ["battery capacity calculator", "solar battery sizing", "ah calculator", "off grid battery bank", "solar battery kwh"]
image_width = 1536
image_height = 1024
+++

## Quick estimate

Use this calculator to find the minimum battery bank size for a given daily load. It converts required watt-hours into amp-hours at your chosen system voltage.

## Battery capacity calculator

<form id="battery-form" class="space-y-4 p-4 bg-gray-50 rounded-lg border border-gray-200">
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
    <div>
      <label class="block text-sm font-medium text-gray-700" for="daily-wh">Daily load (Wh)</label>
      <input type="number" id="daily-wh" value="2000" min="1" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="autonomy">Days of autonomy</label>
      <select id="autonomy" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
        <option value="1">1 day (grid-tied backup)</option>
        <option value="1.5">1.5 days</option>
        <option value="2" selected>2 days (off-grid common)</option>
        <option value="3">3 days (cloudy season buffer)</option>
      </select>
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="dod">Depth of discharge (DoD)</label>
      <select id="dod" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
        <option value="0.5">50% (lead-acid / conservative)</option>
        <option value="0.80" selected>80% (LiFePO4 typical)</option>
        <option value="0.9">90% (Li-ion max usable)</option>
        <option value="1.0">100% (theoretical only)</option>
      </select>
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="inv-eff">Inverter efficiency</label>
      <select id="inv-eff" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
        <option value="0.85">0.85 (older/modified sine)</option>
        <option value="0.90" selected>0.90 (quality pure sine)</option>
        <option value="0.93">0.93 (high-efficiency)</option>
      </select>
    </div>
  </div>
  <button type="button" id="calc-battery" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">Calculate battery size</button>
</form>

<div id="battery-results" class="mt-6 hidden">
  <div class="overflow-x-auto rounded-lg border border-gray-200">
    <table class="min-w-full text-sm">
      <thead class="bg-gray-100">
        <tr><th class="px-4 py-2 text-left font-medium">Metric</th><th class="px-4 py-2 text-left font-medium">Value</th></tr>
      </thead>
      <tbody class="divide-y divide-gray-200">
        <tr><td class="px-4 py-2">Required usable energy</td><td id="res-usable-wh" class="px-4 py-2 font-semibold"></td></tr>
        <tr><td class="px-4 py-2">Required total energy</td><td id="res-total-wh" class="px-4 py-2 font-semibold"></td></tr>
        <tr><td class="px-4 py-2">At 12V</td><td id="res-ah-12" class="px-4 py-2"></td></tr>
        <tr><td class="px-4 py-2">At 24V</td><td id="res-ah-24" class="px-4 py-2"></td></tr>
        <tr><td class="px-4 py-2">At 48V</td><td id="res-ah-48" class="px-4 py-2"></td></tr>
      </tbody>
    </table>
  </div>
</div>

{{< toolscript id="battery-calc" >}}
  function fmt(n){ return n.toLocaleString(undefined, {maximumFractionDigits: 0}); }
  function calculate(){
    var dailyWh = parseFloat(document.getElementById('daily-wh').value) || 0;
    var autonomy = parseFloat(document.getElementById('autonomy').value) || 1;
    var dod = parseFloat(document.getElementById('dod').value) || 0.8;
    var invEff = parseFloat(document.getElementById('inv-eff').value) || 0.9;
    var usableWh = dailyWh * autonomy / invEff;
    var totalWh = usableWh / dod;
    document.getElementById('res-usable-wh').textContent = fmt(usableWh) + ' Wh (' + fmt(usableWh/1000) + ' kWh)';
    document.getElementById('res-total-wh').textContent = fmt(totalWh) + ' Wh (' + fmt(totalWh/1000) + ' kWh)';
    document.getElementById('res-ah-12').textContent = fmt(totalWh / 12) + ' Ah';
    document.getElementById('res-ah-24').textContent = fmt(totalWh / 24) + ' Ah';
    document.getElementById('res-ah-48').textContent = fmt(totalWh / 48) + ' Ah';
    document.getElementById('battery-results').classList.remove('hidden');
  }
  document.getElementById('calc-battery').addEventListener('click', calculate);
  calculate();
{{< /toolscript >}}

## The formula

**Battery Wh = (Daily Wh × Days of autonomy ÷ Inverter efficiency) ÷ Depth of discharge**

Example: 2,000 Wh × 2 days ÷ 0.90 ÷ 0.80 = **5,556 Wh total battery bank**.

- **Usable capacity** is what you can actually draw before recharging.
- **Total capacity** is the nameplate you must buy to keep DoD healthy.
- Higher voltage means lower current for the same power, so less voltage drop and thinner cable. See [12V vs 24V vs 48V solar](12v-vs-24v-vs-48v-solar.html) and [how to choose system voltage](how-to-choose-solar-system-voltage.html).

## Tips

- **Li-ion/LiFePO4** often supports 80–90% DoD with 4,000–6,000 cycles. Lead-acid is usually limited to 50% DoD for longevity.
- **Factor inverter efficiency** for AC loads. DC loads skip that loss.
- **Size for critical loads first**, then add discretionary loads.
- **Cold temperatures reduce usable capacity** and can slow charging. Size for the coldest month if off-grid year-round.
- Match your bank to inverter and [cable sizing](battery-cable-size-for-inverter.html) so protection stays realistic.

## Next logical reads

<a href="solar-system-sizing.html" class="text-link">How to size a solar system</a> <a href="li-ion-vs-lead-acid.html" class="text-link">Li-ion vs lead-acid</a> <a href="solar-system-costs.html" class="text-link">Solar system cost breakdown</a> <a href="how-to-choose-solar-system-voltage.html" class="text-link">How to choose system voltage</a>

## FAQ

{{< faq "Do I size from daily or peak load?" >}}
Daily Wh is the baseline. Add surge headroom at the inverter, not the battery, unless surge is sustained.
{{< /faq >}}

{{< faq "What if I only need backup for 4 hours?" >}}
Set days of autonomy to 0.17 (4 ÷ 24). The calculator will still apply DoD and inverter efficiency.
{{< /faq >}}

{{< faq "Can I use a 12V battery for a whole house?" >}}
Usually no. Whole-home storage runs at 48V or 400V to keep current and cable sizes manageable.
{{< /faq >}}

{{< faq "Why does the calculator show more Ah at lower voltage?" >}}
For the same energy, lower voltage means higher amp-hours (Wh = V × Ah). Higher voltage gives lower Ah and usually easier wiring.
{{< /faq >}}

{{< faq-schema >}}
