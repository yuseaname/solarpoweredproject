+++

title = "How to Size an Inverter for Solar (Watts, Surge, Battery Draw)"
slug = "solar-inverter-sizing"
date = 2026-05-31
draft = false
description = "Inverter sizing for solar systems: calculate peak watts, surge watts, and how inverter choice affects battery capacity and solar panel sizing. Interactive calculator included."
image = "/assets/images/field-guide/system-planner-architecture.jpg"
image_alt = "Architecture diagram showing inverter placement in a solar battery system"
author = "Solar Powered Project"
image_width = 1024
image_height = 576
updated = 2026-08-15
+++

{{< affiliate-disclosure >}}
## Key takeaways

-   Size for **continuous watts** and **surge watts**.
-   A practical rule of thumb: add **25% headroom** above your simultaneous running watts.
-   Motors and compressors need roughly **2–3× their running watts** to start; hard-start loads like well pumps can briefly demand **3–7×**.
-   Oversizing can increase idle losses and cost.
-   Inverter choice affects battery draw and wiring requirements.

## The quick answer

Add up the running watts of everything you'll power at the same time, multiply by 1.25, and pick the next size up. Then check surge: the worst case is your biggest motor **starting while everything else runs**, so the inverter's surge rating must cover that moment. Use the calculator below — it does both checks plus battery-side amps.

## Inverter sizing calculator

Check the loads you plan to run at the same time. Defaults come from our [solar load calculation table](how-to-calculate-solar-load.html) — edit any value to match your actual equipment.

<form id="invcalc-form" class="space-y-4 p-4 bg-gray-50 rounded-lg border border-gray-200">
  <div class="overflow-x-auto">
    <table class="w-full text-sm">
      <thead>
        <tr class="text-left text-gray-600 border-b border-gray-200">
          <th class="py-2 pr-2">Run together?</th>
          <th class="py-2 pr-2">Load</th>
          <th class="py-2 pr-2">Running W</th>
          <th class="py-2">Surge W</th>
        </tr>
      </thead>
      <tbody id="invcalc-loads">
        <tr class="border-b border-gray-100"><td class="py-1.5 pr-2"><input type="checkbox" class="invcalc-chk rounded" data-name="Refrigerator (full-size)" checked></td><td class="py-1.5 pr-2">Refrigerator (full-size)</td><td class="py-1.5 pr-2"><input type="number" class="invcalc-run w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="200" min="1"></td><td class="py-1.5"><input type="number" class="invcalc-surge w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="1200" min="0"></td></tr>
        <tr class="border-b border-gray-100"><td class="py-1.5 pr-2"><input type="checkbox" class="invcalc-chk rounded" data-name="Chest freezer"></td><td class="py-1.5 pr-2">Chest freezer</td><td class="py-1.5 pr-2"><input type="number" class="invcalc-run w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="150" min="1"></td><td class="py-1.5"><input type="number" class="invcalc-surge w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="800" min="0"></td></tr>
        <tr class="border-b border-gray-100"><td class="py-1.5 pr-2"><input type="checkbox" class="invcalc-chk rounded" data-name="Well pump (1/2 hp)"></td><td class="py-1.5 pr-2">Well pump (½ hp)</td><td class="py-1.5 pr-2"><input type="number" class="invcalc-run w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="750" min="1"></td><td class="py-1.5"><input type="number" class="invcalc-surge w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="2000" min="0"></td></tr>
        <tr class="border-b border-gray-100"><td class="py-1.5 pr-2"><input type="checkbox" class="invcalc-chk rounded" data-name="Window AC (5,000 BTU)"></td><td class="py-1.5 pr-2">Window AC (5,000 BTU)</td><td class="py-1.5 pr-2"><input type="number" class="invcalc-run w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="600" min="1"></td><td class="py-1.5"><input type="number" class="invcalc-surge w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="2200" min="0"></td></tr>
        <tr class="border-b border-gray-100"><td class="py-1.5 pr-2"><input type="checkbox" class="invcalc-chk rounded" data-name="Microwave (1,000W output)"></td><td class="py-1.5 pr-2">Microwave (1,000W output)</td><td class="py-1.5 pr-2"><input type="number" class="invcalc-run w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="1500" min="1"></td><td class="py-1.5"><input type="number" class="invcalc-surge w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="1500" min="0"></td></tr>
        <tr class="border-b border-gray-100"><td class="py-1.5 pr-2"><input type="checkbox" class="invcalc-chk rounded" data-name="Coffee maker"></td><td class="py-1.5 pr-2">Coffee maker</td><td class="py-1.5 pr-2"><input type="number" class="invcalc-run w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="1200" min="1"></td><td class="py-1.5"><input type="number" class="invcalc-surge w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="1200" min="0"></td></tr>
        <tr class="border-b border-gray-100"><td class="py-1.5 pr-2"><input type="checkbox" class="invcalc-chk rounded" data-name="LED lighting"></td><td class="py-1.5 pr-2">LED lighting</td><td class="py-1.5 pr-2"><input type="number" class="invcalc-run w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="300" min="1"></td><td class="py-1.5"><input type="number" class="invcalc-surge w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="300" min="0"></td></tr>
        <tr class="border-b border-gray-100"><td class="py-1.5 pr-2"><input type="checkbox" class="invcalc-chk rounded" data-name="Laptops + phone charging"></td><td class="py-1.5 pr-2">Laptops + phone charging</td><td class="py-1.5 pr-2"><input type="number" class="invcalc-run w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="100" min="1"></td><td class="py-1.5"><input type="number" class="invcalc-surge w-24 rounded-md border-gray-300 shadow-sm px-2 py-1 border" value="100" min="0"></td></tr>
      </tbody>
    </table>
  </div>
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
    <div>
      <label class="block text-sm font-medium text-gray-700" for="invcalc-volts">Battery bank voltage</label>
      <select id="invcalc-volts" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm px-3 py-2 border">
        <option value="12">12V</option>
        <option value="24">24V</option>
        <option value="48">48V</option>
      </select>
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="invcalc-eff">Inverter efficiency (%)</label>
      <input type="number" id="invcalc-eff" value="90" min="50" max="99" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm px-3 py-2 border">
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="invcalc-margin">Continuous headroom (%)</label>
      <input type="number" id="invcalc-margin" value="25" min="0" max="100" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm px-3 py-2 border">
    </div>
  </div>
  <button type="button" id="invcalc-btn" class="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 font-medium">Size my inverter</button>
</form>

<div id="invcalc-results" class="hidden mt-4 p-4 bg-white rounded-lg border border-gray-200 space-y-2"></div>
<div class="calc-actions hidden mt-3" data-target="invcalc-results">
  <button type="button" class="calc-copy px-3 py-1.5 text-sm font-medium rounded-md border border-gray-300 bg-white hover:bg-gray-50">Copy results</button>
  <button type="button" class="calc-print px-3 py-1.5 text-sm font-medium rounded-md border border-gray-300 bg-white hover:bg-gray-50">Print</button>
  <span class="calc-copied hidden text-sm text-green-600 ml-2">Copied!</span>
</div>

{{< toolscript id="calc-actions-invcalc-results" >}}
(function(){
  var actions = document.querySelector('.calc-actions[data-target="invcalc-results"]');
  var target = document.getElementById('invcalc-results');
  if (!actions || !target) return;
  function show(){ if (target.innerHTML.trim() !== '') actions.classList.remove('hidden'); }
  new MutationObserver(show).observe(target, {childList: true, subtree: true, characterData: true});
  show();
  actions.querySelector('.calc-copy').addEventListener('click', function(){
    var text = target.innerText.trim();
    function done(){
      var ok = actions.querySelector('.calc-copied');
      ok.classList.remove('hidden');
      setTimeout(function(){ ok.classList.add('hidden'); }, 2000);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done).catch(function(){
        var ta = document.createElement('textarea');
        ta.value = text; document.body.appendChild(ta); ta.select();
        try { document.execCommand('copy'); done(); } catch(e){}
        document.body.removeChild(ta);
      });
    }
  });
  actions.querySelector('.calc-print').addEventListener('click', function(){ window.print(); });
})();
{{< /toolscript >}}

{{< toolscript id="invcalc" >}}
function fmtW(n) { return Math.round(n).toLocaleString() + 'W'; }
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.getElementById('invcalc-btn');
  var box = document.getElementById('invcalc-results');
  var commonSizes = [300, 500, 800, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 8000, 10000, 12000];
  function calc() {
    var rows = document.querySelectorAll('#invcalc-loads tr');
    var loads = [];
    rows.forEach(function(r) {
      var chk = r.querySelector('.invcalc-chk');
      if (!chk || !chk.checked) return;
      var run = parseFloat(r.querySelector('.invcalc-run').value) || 0;
      var surge = parseFloat(r.querySelector('.invcalc-surge').value) || 0;
      if (run <= 0) return;
      loads.push({ name: chk.getAttribute('data-name'), run: run, surge: Math.max(surge, run) });
    });
    var volts = parseFloat(document.getElementById('invcalc-volts').value) || 12;
    var eff = (parseFloat(document.getElementById('invcalc-eff').value) || 90) / 100;
    var margin = (parseFloat(document.getElementById('invcalc-margin').value) || 0) / 100;
    if (loads.length === 0) {
      box.classList.remove('hidden');
      box.innerHTML = '<p class="text-gray-600">Check at least one load to size your inverter.</p>';
      return;
    }
    var totalRun = loads.reduce(function(s, l) { return s + l.run; }, 0);
    var needCont = totalRun * (1 + margin);
    var size = null;
    for (var i = 0; i < commonSizes.length; i++) {
      if (commonSizes[i] >= needCont) { size = commonSizes[i]; break; }
    }
    if (size === null) size = Math.ceil(needCont / 1000) * 1000;
    var worst = null;
    loads.forEach(function(l) {
      var startW = (totalRun - l.run) + l.surge;
      if (!worst || startW > worst.watts) worst = { name: l.name, watts: startW, isSurge: l.surge > l.run };
    });
    if (!worst) worst = { name: '', watts: totalRun, isSurge: false };
    var ampsCont = totalRun / (volts * eff);
    var ampsSurge = worst.watts / (volts * eff);
    var surgeRatioOk = worst.watts <= size * 2;
    var html = '';
    html += '<p class="text-gray-800"><strong>Simultaneous running load:</strong> ' + fmtW(totalRun) + '</p>';
    html += '<p class="text-gray-800"><strong>Recommended inverter (continuous):</strong> ' + fmtW(size) + ' <span class="text-gray-500">(' + fmtW(totalRun) + ' + ' + Math.round(margin * 100) + '% headroom, rounded up to a common size)</span></p>';
    html += '<p class="text-gray-800"><strong>Worst-case startup moment:</strong> ' + fmtW(worst.watts) + (worst.isSurge ? ' <span class="text-gray-500">(starting the ' + worst.name + ' while everything else runs)</span>' : ' <span class="text-gray-500">(no significant motor surge in your selection — resistive loads only)</span>') + '</p>';
    html += '<p class="text-gray-800"><strong>Required inverter surge rating:</strong> at least ' + fmtW(worst.watts) + (surgeRatioOk
      ? ' — many inverters surge around 2× continuous at this size, but verify the specific model\'s surge rating before buying.'
      : ' — <span class="text-red-600 font-medium">exceeds 2× the recommended size; prioritize models with a higher surge rating (often 2.5–3×) or move the ' + worst.name + ' to its own circuit.</span>') + '</p>';
    html += '<p class="text-gray-800"><strong>Battery-side draw at ' + volts + 'V:</strong> ≈' + Math.round(ampsCont) + 'A continuous, ≈' + Math.round(ampsSurge) + 'A during startup <span class="text-gray-500">(at ' + Math.round(eff * 100) + '% efficiency)</span></p>';
    if (ampsCont > 100) {
      html += '<p class="text-amber-700">At ' + volts + 'V, that continuous current is high. A higher bank voltage cuts amps proportionally — see <a href="/pages/12v-vs-24v-vs-48v-solar.html" class="text-link">12V vs 24V vs 48V systems</a>, then check <a href="/pages/battery-cable-size-for-inverter.html" class="text-link">battery cable sizing</a>.</p>';
    } else {
      html += '<p class="text-gray-600 text-sm">Next: verify <a href="/pages/battery-cable-size-for-inverter.html" class="text-link">battery cable size</a> for ' + Math.round(ampsCont) + 'A continuous.</p>';
    }
    box.classList.remove('hidden');
    box.innerHTML = html;
  }
  btn.addEventListener('click', calc);
});
{{< /toolscript >}}

{{< callout "tip" "Surge defaults are conservative" >}}
Motor surge varies by compressor and starting method. The defaults above use conservative values from our [load table](how-to-calculate-solar-load.html); if your equipment lists a specific LRA or startup rating, use that instead.
{{< /callout >}}

## Step 1: List your AC loads and peak watts

Add up the AC devices you may run at the same time. For each device, use nameplate watts or a measured value (many appliances vary during operation).

**Peak watts** ≈ sum of simultaneous AC watts

Related: <a href="solar-system-sizing.html" class="text-link">How to size a solar system</a>

## Step 2: Account for surge (starting) power

Some loads require a high startup surge (motors, compressors). Inverter specs typically list a surge rating for a short time window.

**Surge headroom** = inverter surge rating − expected surge load

If you're near the limit, the system may trip or fail to start the device reliably. A soft-start kit on a well pump or compressor can cut its startup demand by 50–70%, often removing the surge bottleneck entirely.

## Step 3: Check battery-side current draw

Inverters draw significant current from the battery, especially at lower system voltages. A rough estimate:

**Battery amps** ≈ AC watts ÷ (battery volts × efficiency)

Example: 1,000W ÷ (12V × 0.9) ≈ 93A. High currents impact wiring size, fusing, and heat.

<a href="/pages/battery-capacity.html" class="text-link">Battery capacity calculator</a> <a href="solar-components.html" class="text-link">Components overview</a>

## Step 4: Choose inverter type and waveform

For many off-grid and RV use cases, waveform matters for compatibility.

<a href="pure-sine-vs-modified-sine-inverter.html" class="text-link">Pure sine vs modified sine wave</a> <a href="micro-vs-string-inverters.html" class="text-link">Micro vs string inverters (grid-tied)</a>

## Worked example: small off-grid cabin

Loads running together: refrigerator (200W), LED lighting (300W), laptop + phone charging (100W), microwave (1,500W input — a "1,000W output" microwave draws ~1,400–1,600W from the bank).

-   **Simultaneous running load:** 200 + 300 + 100 + 1,500 = **2,100W**
-   **With 25% headroom:** 2,100 × 1.25 = 2,625W → pick a **3,000W** inverter (next common size)
-   **Worst-case startup:** microwave starting while the rest runs = 600 + 1,500 = 2,100W; refrigerator starting while the rest runs = 1,900 + 1,200 = **3,100W** ← the binding case. A 3,000W inverter with a typical 2× surge rating (6,000W) covers it.
-   **Battery-side at 12V (90% efficiency):** 2,100 ÷ 10.8 ≈ **194A continuous**, 3,100 ÷ 10.8 ≈ **287A during startup** — heavy. At 24V both numbers halve; at 48V they quarter. This is why bigger inverter loads push systems toward higher bank voltage (see <a href="/pages/12v-vs-24v-vs-48v-solar.html" class="text-link">12V vs 24V vs 48V</a>).

{{< product-box asin="B081CLPDT9" name="Renogy 2000W 12V Pure Sine Inverter" label="When the math says 2000W" description="If your load list lands in the 1500–2000W continuous range, this is the honest default: pure sine for electronics and motors, remote switch, and cables in the box (per manufacturer spec) — no surge-headroom upsell. Not for: the worked example above — 2,100W running with a ~3,100W worst-case startup needs a 3,000W class unit, not 2,000W. The honest tradeoff: at 12V the battery draw reaches ~194A continuous, which pushes toward 24V/48V cabling." button="Check price on Amazon" >}}

## Common sizing examples (quick ranges)

<table>
<thead>
<tr class="header">
<th>Use case</th>
<th>Typical inverter size</th>
<th>Common notes</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Charging + small appliances</td>
<td>300–800W</td>
<td>Lower surge needs</td>
</tr>
<tr class="even">
<td>Microwave / mixed RV loads</td>
<td>1,000–2,000W</td>
<td>Surge and wiring matter</td>
</tr>
<tr class="odd">
<td>Heavy loads</td>
<td>2,000–4,000W+</td>
<td>Battery bank and voltage become critical</td>
</tr>
</tbody>
</table>

## FAQ

{{< faq "What happens if my inverter is too small?" >}}
It may trip under load, fail to start surge devices, or run hot near its limit.
{{< /faq >}}

{{< faq "Is a bigger inverter always better?" >}}
No. Bigger units cost more and can waste energy at idle. Size to realistic peak and surge needs.
{{< /faq >}}

{{< faq "Does inverter size change battery size?" >}}
Indirectly. Higher AC loads require more battery energy, and inverter losses add to demand.
{{< /faq >}}

{{< faq "Should I choose pure sine wave for solar?" >}}
If you run a mix of electronics and appliances, pure sine wave is usually the safest default.
{{< /faq >}}

{{< faq "How much inverter surge rating do I need?" >}}
Cover your worst-case startup moment: the surge watts of your biggest motor load starting while everything else runs. Motors and compressors typically need 2–3× their running watts to start; hard-start loads like well pumps can briefly demand 3–7×.
{{< /faq >}}

## Next logical reads

<a href="pure-sine-vs-modified-sine-inverter.html" class="text-link">Pure sine vs modified sine wave</a> <a href="inverter-keeps-shutting-off-troubleshooting.html" class="text-link">Inverter keeps shutting off (troubleshooting)</a> <a href="rv-solar-sizing.html" class="text-link">RV solar sizing guide</a> <a href="solar-system-sizing.html" class="text-link">How to size a solar system</a> <a href="solar-system-costs.html" class="text-link">Solar system cost breakdown</a> <a href="inverter-keeps-shutting-off-troubleshooting.html" class="text-link">Inverter shutdown troubleshooting</a>
