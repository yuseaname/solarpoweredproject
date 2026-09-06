+++

title = "How to Size a Solar System (Step-by-Step Load Planner)"
slug = "solar-system-sizing"
date = 2026-05-31
draft = false
description = "Size a solar system from daily load to panels, battery, inverter, and charge controller. Use the interactive load planner, formulas, and next-step links."
image = "/assets/images/field-guide/system-sizing-concept.jpg"
image_alt = "Infographic showing solar system sizing flow from appliance loads through watt-hours to panels, battery, and inverter"
author = "Solar Powered Project"
updated = 2026-08-09
keywords = ["solar system sizing", "how to size solar system", "solar load calculator", "off grid solar sizing", "solar panel sizing"]
image_width = 1024
image_height = 768
related = [
  "/pages/how-to-calculate-solar-load.html",
  "/pages/solar-inverter-sizing.html",
  "/pages/battery-capacity.html"
]
+++

{{< affiliate-disclosure >}}
## Key takeaways

- Start with **daily watt-hours used** — everything else flows from that number.
- Panel size depends on **peak sun hours** at your location.
- Battery size depends on **backup time** and **depth of discharge**.
- Inverter size must handle **continuous load + surge**.
- Use the interactive load planner below to build your own numbers.

## Step 1: List every load

Add up appliance wattage and daily hours of use. Multiply watts by hours to get watt-hours (Wh).

**Example:** 100 W × 5 hours = 500 Wh.

Use the planner below to estimate your total daily load. It will suggest panel, battery, inverter, and charge-controller sizes.

## Interactive solar load planner

<form id="sizing-form" class="space-y-4 p-4 bg-gray-50 rounded-lg border border-gray-200">
  <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
    <div class="sm:col-span-3">
      <label class="block text-sm font-medium text-gray-700" for="load-list">Loads (watts, hours/day per item, one per line)</label>
      <textarea id="load-list" rows="6" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border font-mono text-sm">LED lights, 10, 6
Fridge, 150, 8
Laptop charger, 60, 4
Water pump, 200, 0.5
Fan, 40, 6</textarea>
      <p class="text-xs text-gray-500 mt-1">Format: name, watts, hours/day. Use peak/running watts, not surge.</p>
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="peak-sun">Peak sun hours / day</label>
      <input type="number" id="peak-sun" value="4.5" min="0" step="0.1" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="sys-voltage">System voltage</label>
      <select id="sys-voltage" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
        <option value="12">12V (small cabin/RV)</option>
        <option value="24">24V (mid-size cabin)</option>
        <option value="48" selected>48V (home/off-grid)</option>
      </select>
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="backup-days">Days of autonomy</label>
      <select id="backup-days" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
        <option value="1">1 day</option>
        <option value="2" selected>2 days</option>
        <option value="3">3 days</option>
      </select>
    </div>
  </div>
  <button type="button" id="calc-sizing" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">Size my system</button>
</form>

<div id="sizing-results" class="mt-6 hidden">
<div class="calc-actions hidden mt-3" data-target="sizing-results">
  <button type="button" class="calc-copy px-3 py-1.5 text-sm font-medium rounded-md border border-gray-300 bg-white hover:bg-gray-50">Copy results</button>
  <button type="button" class="calc-print px-3 py-1.5 text-sm font-medium rounded-md border border-gray-300 bg-white hover:bg-gray-50">Print</button>
  <span class="calc-copied hidden text-sm text-green-600 ml-2">Copied!</span>
</div>

{{< toolscript id="calc-actions-sizing-results" >}}
(function(){
  var actions = document.querySelector('.calc-actions[data-target="sizing-results"]');
  var target = document.getElementById('sizing-results');
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
  <div class="overflow-x-auto rounded-lg border border-gray-200">
    <table class="min-w-full text-sm">
      <thead class="bg-gray-100">
        <tr><th class="px-4 py-2 text-left font-medium">Component</th><th class="px-4 py-2 text-left font-medium">Recommended size</th><th class="px-4 py-2 text-left font-medium">Notes</th></tr>
      </thead>
      <tbody class="divide-y divide-gray-200">
        <tr><td class="px-4 py-2">Daily load</td><td id="res-daily-load" class="px-4 py-2 font-semibold"></td><td class="px-4 py-2 text-gray-600">Base for all sizing</td></tr>
        <tr><td class="px-4 py-2">Solar array</td><td id="res-panel-watts" class="px-4 py-2 font-semibold"></td><td class="px-4 py-2 text-gray-600">Sized for daily load + 20% losses</td></tr>
        <tr><td class="px-4 py-2">Battery bank (usable)</td><td id="res-battery-usable" class="px-4 py-2 font-semibold"></td><td class="px-4 py-2 text-gray-600">80% DoD LiFePO4 assumed</td></tr>
        <tr><td class="px-4 py-2">Battery bank (total Ah)</td><td id="res-battery-ah" class="px-4 py-2 font-semibold"></td><td class="px-4 py-2 text-gray-600">At selected voltage</td></tr>
        <tr><td class="px-4 py-2">Inverter</td><td id="res-inverter" class="px-4 py-2 font-semibold"></td><td class="px-4 py-2 text-gray-600">2× peak running load + surge headroom</td></tr>
        <tr><td class="px-4 py-2">Charge controller</td><td id="res-controller" class="px-4 py-2 font-semibold"></td><td class="px-4 py-2 text-gray-600">MPPT rated for array amps at battery voltage</td></tr>
      </tbody>
    </table>
  </div>
</div>

{{< toolscript id="sizing-calc" >}}
  function fmt(n){ return n.toLocaleString(undefined, {maximumFractionDigits: 0}); }
  function parseLoads(text){
    var lines = text.split(/\r?\n/);
    var total = 0, peak = 0;
    for(var i=0;i<lines.length;i++){
      var parts = lines[i].split(',').map(function(s){ return s.trim(); });
      if(parts.length < 2) continue;
      var watts = parseFloat(parts[1]) || 0;
      var hours = parts.length >= 3 ? parseFloat(parts[2]) || 0 : 1;
      total += watts * hours;
      if(watts > peak) peak = watts;
    }
    return {daily: total, peak: peak};
  }
  function calculate(){
    var loads = parseLoads(document.getElementById('load-list').value);
    var sun = parseFloat(document.getElementById('peak-sun').value) || 4.5;
    var voltage = parseInt(document.getElementById('sys-voltage').value, 10) || 48;
    var autonomy = parseFloat(document.getElementById('backup-days').value) || 2;
    var panelWatts = Math.ceil((loads.daily / sun / 0.8) / 50) * 50;
    var usableWh = loads.daily * autonomy / 0.9;
    var totalWh = usableWh / 0.8;
    var ah = totalWh / voltage;
    var inverterW = Math.max(loads.peak * 2, 300);
    var controllerA = Math.ceil((panelWatts / voltage) * 1.25);
    document.getElementById('res-daily-load').textContent = fmt(loads.daily) + ' Wh';
    document.getElementById('res-panel-watts').textContent = fmt(panelWatts) + ' W';
    document.getElementById('res-battery-usable').textContent = fmt(usableWh) + ' Wh (' + fmt(usableWh/1000) + ' kWh)';
    document.getElementById('res-battery-ah').textContent = fmt(ah) + ' Ah at ' + voltage + 'V';
    document.getElementById('res-inverter').textContent = fmt(inverterW) + ' W minimum';
    document.getElementById('res-controller').textContent = fmt(controllerA) + ' A MPPT minimum';
    document.getElementById('sizing-results').classList.remove('hidden');
  }
  document.getElementById('calc-sizing').addEventListener('click', calculate);
  calculate();
{{< /toolscript >}}

## Step 2: Size solar panels

Divide daily Wh by average peak sun hours to estimate needed panel watts.

<a href="solar-panel-output.html" class="text-link">Use the solar panel output calculator →</a>

{{< product-box asin="B07GF5JY35" name="Renogy 100W 12V Monocrystalline Panel" label="The sizing math, made real" description="Once your watt-hour math says how many watts of panel you need, this is the module to check the number against (per manufacturer spec) — the $1/Watt benchmark that turns a sizing worksheet into a shopping list. Not for: whole-home or grid-tied arrays — by the Step 2 math, a 2,000Wh/day cabin needs ~625W, and whole-home loads run well past that in multiples of 100W modules. The honest tradeoff: 100W per module means you buy and mount many units for bigger arrays." button="Check price on Amazon" >}}

## Step 3: Size batteries

Choose a battery bank to cover the number of hours or days you want in reserve.

<a href="/pages/battery-capacity.html" class="text-link">Use the battery capacity calculator →</a>

{{< product-box asin="B084DB36KW" name="LiTime 12V 100Ah LiFePO4" label="The 1.28 kWh building block" description="Battery-bank sizing is usable-kWh multiplication — and this is the unit most DIY banks multiply by. Built-in 100A BMS and low-temp protection come standard in the arithmetic (per manufacturer spec). Not for: 48V banks or whole-home loads without series/parallel-matched wiring — this is a 12V unit, and the bank math here sizes to the system voltage you pick. The honest tradeoff: usable kWh per unit is small, so big banks mean many units and more wiring." button="Check price on Amazon" >}}

## Step 4: Size the inverter

The inverter must handle the sum of all loads that can run at once, plus motor surge. A practical rule: add **~25% headroom** to your simultaneous running watts, then verify the worst startup moment — motors typically need 2–3× running watts to start, hard-start loads like well pumps 3–7×. Run the numbers with the [inverter sizing calculator](solar-inverter-sizing.html).

## Step 5: Size the charge controller

MPPT controllers are rated by output amps at battery voltage. A conservative rule:

**Controller amps ≈ (Panel watts ÷ Battery voltage) × 1.25**

Example: 4,000 W array ÷ 48 V × 1.25 ≈ **104 A**. Round up to the next standard size.

Compare MPPT and PWM in [MPPT vs PWM](mppt-vs-pwm.html) and see [charge controller cost](mppt-charge-controller-cost.html).

{{< product-box asin="B073ZJ3L13" name="Victron SmartSolar MPPT 100/30" label="The controller that fits the math" description="If your controller sizing lands in the 20–30A range, this is the default answer: 100V open-circuit ceiling, lithium presets, and Bluetooth so you can verify the sizing against real charge data (per manufacturer spec). Not for: the Step 5 example — a 4,000W / 48V array needs ~104A, and this is a 20–30A-class 12/24V controller. The honest tradeoff: the 100V input rail caps string voltage; bigger arrays need the 150V line." button="Check price on Amazon" >}}

## Common sizing mistakes

- **Undersizing winter production:** summer sun is not a year-round baseline.
- **Forgetting inverter efficiency:** AC loads need ~10% more battery than the raw Wh.
- **Ignoring surge:** pumps and compressors can need 3–7× running watts for a few seconds.
- **String voltage too low:** a 12 V system for a 3,000 W house creates huge currents and thick cabling.

## Next logical reads

<a href="12v-vs-24v-vs-48v-solar.html" class="text-link">12V vs 24V vs 48V solar systems</a> <a href="12v-vs-24v-vs-48v-solar.html" class="text-link">How to choose solar system voltage</a> <a href="solar-system-costs.html" class="text-link">Solar system cost breakdown</a> <a href="solar-components.html" class="text-link">Solar components guide</a> <a href="mppt-vs-pwm.html" class="text-link">MPPT vs PWM</a> <a href="solar-panel-angle-calculator.html" class="text-link">Solar panel angle calculator</a>

<a href="best-mppt-charge-controllers.html" class="text-link">Best MPPT charge controllers (2026 buyer guide)</a>

## FAQ

{{< faq "Should I size for average or maximum daily use?" >}}
Size for your highest-usage season, then check if it still works in winter. Off-grid systems usually size for winter if year-round use is required.
{{< /faq >}}

{{< faq "Can I add panels later?" >}}
Yes, but design the charge controller and battery voltage to handle the final array size so you don’t replace major components.
{{< /faq >}}

{{< faq "How does a grid-tied system differ?" >}}
Grid-tied systems size to offset annual kWh and meet utility/net metering rules. Battery backup is optional. Off-grid systems must cover every load themselves.
{{< /faq >}}

{{< faq "What if my roof is small?" >}}
Use higher-efficiency panels, prioritize consumption reduction, and consider a ground mount. See [best solar panels for small roofs and small homes](best-solar-panels-small-roof.html). - <a href="solar-payback-calculator.html" class="text-link">Solar payback calculator</a>
{{< /faq >}}

{{< faq-schema >}}
