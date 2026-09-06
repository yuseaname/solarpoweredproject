+++

title = "Solar Wire Size: How to Choose the Right Gauge (Voltage Drop + Safety)"
slug = "solar-wire-size"
date = 2026-05-31
draft = false
description = "Solar wire size explained with a practical decision flow: identify the circuit, estimate max amps, measure run length, and manage voltage drop safely."
image = "/images/solar-wire-size/hero.webp"
author = "Solar Powered Project"
image_width = 1536
image_height = 1024
+++

<a href="#key-takeaways" class="text-link">Key takeaways</a> <a href="#the-real-goal-safety--performance" class="text-link">The real goal</a> <a href="#two-rules-that-prevent-most-mistakes" class="text-link">Two rules that prevent most mistakes</a> <a href="#a-simple-4-step-decision-flow-what-to-measure-first" class="text-link">A simple 4-step decision flow</a> <a href="#rule-2-distance-drives-voltage-drop" class="text-link">Why higher voltage simplifies wiring</a> <a href="#what-dc-rated-means-a-quick-checklist" class="text-link">A quick “DC-rated” checklist</a> <a href="#two-rules-that-prevent-most-mistakes" class="text-link">Common wire-sizing mistakes</a> <a href="#faq" class="text-link">FAQ</a>

## Key takeaways

-   Start by identifying the circuit: PV wiring, controller-to-battery, or battery-to-inverter.
-   Wire size is driven by **max amps** and **run length**, not “average watts.”
-   Higher system voltage usually reduces current, which often means smaller cable and less voltage drop.

<a href="solar-wiring-and-protection-cost.html" class="text-link">Wiring &amp; protection cost (what’s included)</a>

## The real goal (safety + performance)

The reader is the hero here: you want a solar system that works reliably **without hot wires, nuisance shutdowns, or mystery power loss**. This guide is the “plan” that gets you there.

**Good wire sizing** = low heat + manageable voltage drop + compatible connectors and protection.

<figure>
<img src="../assets/images/copper-wire-comparison.jpg" loading="lazy" width="285" height="297" alt="Copper wire gauges of different thicknesses used for solar wiring." />
<figcaption>Image: “Copper wire comparison” by Chemicalinterest, public domain — Source: <a href="https://commons.wikimedia.org/wiki/File:Copper_wire_comparison.JPG" class="text-link">Wikimedia Commons</a></figcaption>
</figure>

## Two rules that prevent most mistakes

### Rule 1: current (amps) drives heat risk

For a given load, lower voltage means higher current. High current pushes you toward thicker cable and higher-rated lugs, bus bars, fuses, and breakers.

<a href="12v-vs-24v-vs-48v-solar.html" class="text-link">12V vs 24V vs 48V solar systems</a> <a href="12v-vs-24v-vs-48v-solar.html" class="text-link">How to choose solar system voltage</a>

### Rule 2: distance drives voltage drop

The longer the run (especially on high-current battery cables), the more voltage you lose in the wire. Too much drop can look like “the system is underperforming” when the real issue is wiring.

## A simple 4-step decision flow (what to measure first)

### Step 1: identify the circuit

-   **PV wiring:** panels to charge controller (often higher voltage, lower current)
-   **Controller-to-battery:** charging current to the battery bank
-   **Battery-to-inverter:** usually the highest current wiring in the system

<a href="solar-components.html" class="text-link">Solar components explained (what connects to what)</a>

### Step 2: estimate max amps (use labels, not guesses)

Use the equipment specs as your “source of truth.” For example, charge controllers list max output current, and inverters list continuous power and surge behavior.

<a href="solar-inverter-sizing.html" class="text-link">How to size an inverter (watts, surge, draw)</a>

### Step 3: measure one-way run length

Don’t assume a tidy layout. Measure the real path the cable will take (including routing), and remember that long runs are most painful on high-current circuits.

### Step 4: set a conservative voltage-drop target

If you want a simple rule for planning (not a code substitute), aim to keep voltage drop “small enough that it doesn’t change equipment behavior.” The battery-to-inverter run is often where people tighten this target because voltage sag can trigger low-voltage shutdowns.

When in doubt, oversize cable rather than forcing a long, high-current run at a low voltage.


## Wire size calculator (amps, volts, distance)

Enter the circuit numbers from Steps 1–4: the circuit voltage, the max current from the equipment label, and the one-way run length. The calculator picks a gauge that clears both the ampacity ladder and your voltage-drop target.

<form id="wire-form" class="space-y-4 p-4 bg-gray-50 rounded-lg border border-gray-200">
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
    <div>
      <label class="block text-sm font-medium text-gray-700" for="wire-volts">Circuit voltage</label>
      <select id="wire-volts" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
        <option value="12" selected>12V</option>
        <option value="24">24V</option>
        <option value="48">48V</option>
        <option value="36">~36V (PV string)</option>
        <option value="60">~60V (PV string)</option>
      </select>
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="wire-amps">Max amps (from label)</label>
      <input type="number" id="wire-amps" value="6" min="0.5" max="200" step="0.5" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="wire-run">One-way run (feet)</label>
      <input type="number" id="wire-run" value="10" min="1" max="120" step="1" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="wire-drop">Voltage-drop target</label>
      <select id="wire-drop" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
        <option value="2">2% (tight)</option>
        <option value="3" selected>3% (typical)</option>
        <option value="5">5% (relaxed, non-critical)</option>
      </select>
    </div>
  </div>
  <button type="button" id="calc-wire" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">Calculate wire size</button>
</form>

<div id="wire-results" class="mt-6 hidden">
  <h3>Your wire plan (planning-level)</h3>
  <table>
  <thead><tr><th>Result</th><th>Value</th></tr></thead>
  <tbody>
    <tr><td>Recommended gauge</td><td id="wire-rec"></td></tr>
    <tr><td>Expected voltage drop</td><td id="wire-drop-res"></td></tr>
    <tr><td>Ampacity headroom</td><td id="wire-head"></td></tr>
  </tbody>
  </table>
  <p id="wire-notes"></p>
</div>

<div class="calc-actions hidden mt-3" data-target="wire-results">
  <button type="button" class="calc-copy px-3 py-1.5 text-sm font-medium rounded-md border border-gray-300 bg-white hover:bg-gray-50">Copy results</button>
  <button type="button" class="calc-print px-3 py-1.5 text-sm font-medium rounded-md border border-gray-300 bg-white hover:bg-gray-50">Print</button>
  <span class="calc-copied hidden text-sm text-green-600 ml-2">Copied!</span>
</div>

{{< toolscript id="calc-actions-wire-results" >}}
(function(){
  var actions = document.querySelector('.calc-actions[data-target="wire-results"]');
  var target = document.getElementById('wire-results');
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
{{< toolscript id="wire-calc" >}}
  var LADDER = [
    {name:'14 AWG', limit:15, r:2.6},
    {name:'12 AWG', limit:20, r:1.6},
    {name:'10 AWG', limit:30, r:1.0},
    {name:'8 AWG', limit:45, r:0.64},
    {name:'6 AWG', limit:65, r:0.40},
    {name:'4 AWG', limit:85, r:0.25},
    {name:'2 AWG', limit:110, r:0.16},
    {name:'1/0 AWG', limit:125, r:0.10},
    {name:'2/0 AWG', limit:145, r:0.079},
    {name:'4/0 AWG', limit:175, r:0.050}
  ];
  function calcWire(){
    var v = parseFloat(document.getElementById('wire-volts').value) || 12;
    var a = parseFloat(document.getElementById('wire-amps').value) || 0;
    var ft = parseFloat(document.getElementById('wire-run').value) || 1;
    var tgt = parseFloat(document.getElementById('wire-drop').value) || 3;
    var notes = [];
    var idx = LADDER.findIndex(function(g){ return g.limit >= a; });
    if (idx === -1) {
      document.getElementById('wire-rec').textContent = 'beyond 4/0 \u2014 shorten the run or raise voltage';
      document.getElementById('wire-drop-res').textContent = '—';
      document.getElementById('wire-head').textContent = '—';
      document.getElementById('wire-notes').textContent = 'At ' + a + ' A this is battery-cable territory: see the battery cable size guide, parallel feeds, or a higher system voltage.';
      document.getElementById('wire-results').classList.remove('hidden');
      return;
    }
    function dropPct(i){ return (2 * ft * a * LADDER[i].r / 1000) / v * 100; }
    var rec = idx;
    while (dropPct(rec) > tgt && rec < LADDER.length - 1) rec++;
    var dp = dropPct(rec), dv = 2 * ft * a * LADDER[rec].r / 1000;
    if (rec > idx) notes.push('Stepped up from ' + LADDER[idx].name + ' to hold the ' + tgt + '% drop target over ' + ft + ' ft.');
    else notes.push(LADDER[rec].name + ' clears both the ampacity limit and the ' + tgt + '% drop target.');
    if (dp > tgt) notes.push('Even ' + LADDER[rec].name + ' exceeds ' + tgt + '% on this run \u2014 shorten the path, raise circuit voltage, or parallel conductors.');
    notes.push('Planning-level (copper, conservative resistance at temperature). Use equipment labels as the source of truth and confirm with the manuals.');
    document.getElementById('wire-rec').textContent = LADDER[rec].name;
    document.getElementById('wire-drop-res').textContent = dv.toFixed(2) + ' V (' + dp.toFixed(1) + '%)';
    document.getElementById('wire-head').textContent = a + ' A on a ' + LADDER[rec].limit + ' A rating (' + Math.round(a / LADDER[rec].limit * 100) + '% used)';
    document.getElementById('wire-notes').textContent = notes.join(' ');
    document.getElementById('wire-results').classList.remove('hidden');
  }
  document.getElementById('calc-wire').addEventListener('click', calcWire);
  calcWire();
{{< /toolscript >}}

### Worked example: what size wire for a 100W solar panel?

A 100W 12V-nominal panel has an Imp around 5–6 A and an Isc a bit above that — so the wire decision runs on roughly **6 A**, not 100 W. At 6 A, even 14 AWG clears ampacity; voltage drop over distance is what actually decides the gauge:

| One-way run | 12 AWG drop | 10 AWG drop | Verdict |
| :-- | :-- | :-- | :-- |
| 10 ft | ~1.6% | ~1.0% | 12 AWG is fine |
| 20 ft | ~3.2% | ~2.0% | 10 AWG recommended |
| 35 ft | ~5.6% | ~3.5% | 10 AWG minimum; 8 AWG if you want 3% |

Series-string a second panel and the voltage doubles while current stays the same — the same wire suddenly halves its percentage drop, which is one of the quiet advantages of <a href="solar-panels-series-vs-parallel.html" class="text-link">wiring panels in series</a>.

## 12V vs 24V vs 48V: why higher voltage usually simplifies wiring

If you keep power roughly the same, higher voltage means lower current. Lower current typically means thinner wire, less voltage drop, and smaller (and sometimes cheaper) protection hardware. That’s why many systems “graduate” to 24V or 48V as power needs grow.

<a href="12v-vs-24v-vs-48v-solar.html" class="text-link">Choose a system voltage (practical guide)</a> <a href="solar-system-sizing.html" class="text-link">System sizing overview (start here)</a>

## What “DC-rated” means (a quick checklist)

-   **Cable type:** use appropriate PV wire for arrays and appropriate battery cable for high-current battery circuits.
-   **Connectors:** match the cable type and size; avoid “almost fits” lugs.
-   **Protection:** use fuses/breakers/disconnects explicitly rated for your DC voltage and current.
-   **Heat:** cable that runs warm under normal load is a warning sign, not “normal.”

<a href="solar-fuses-vs-breakers.html" class="text-link">Solar fuses vs breakers (where each belongs)</a>

## Common wire-sizing mistakes (and how to avoid them)

-   **Sizing from average watts:** wire is stressed by peak current, not a daily average.
-   **Forgetting inverter surge:** surge can matter on the battery-to-inverter side.
-   **Ignoring distance:** long runs create voltage drop that looks like “low solar output.”
-   **Mixing cable types:** PV wire and battery cable solve different problems.
-   **Using non-DC-rated hardware:** DC interrupt ratings matter for safety.

<a href="solar-output-troubleshooting.html" class="text-link">Low solar output troubleshooting (symptoms vs causes)</a>

## FAQ

{{< faq "Is PV wire the same as battery cable?" >}}
No. PV wire is designed for outdoor array wiring. Battery cable is built for high current and flexible routing on the battery side.
{{< /faq >}}

{{< faq "What voltage drop is “acceptable” for solar?" >}}
It depends on the circuit and equipment behavior. The safest approach is to keep drop low enough that it doesn’t cause shutdowns or lost production.
{{< /faq >}}

{{< faq "Why does 12V require thicker wire than 24V or 48V?" >}}
For the same power, lower voltage means higher current. Higher current drives thicker cable and higher-rated protection.
{{< /faq >}}

{{< faq "Can I oversize wire?" >}}
Often yes, and it’s a common way to reduce voltage drop and improve reliability. The practical limits are cost, routing, and connector compatibility.
{{< /faq >}}

{{< faq "Do I size for continuous watts or surge?" >}}
Use the maximum current that the circuit can realistically see. For inverters, surge can be relevant depending on your loads and design.
{{< /faq >}}



### The code basis (and why our ladder is conservative)

The ampacity ladder above is **planning guidance, not a code table**. For code work, size conductors from **NEC 310.16** using the temperature column your insulation actually carries (THWN-2/USE-2 PV wire is 90°C-rated, but terminals often limit you to the 75°C column), apply the **NEC 310.15** derating factors for bundling and ambient heat, and meet **NEC 690.8(B)**, which requires PV-circuit conductors sized to at least 125% of the circuit's maximum current. Our values sit at or below the 60°C column on the small gauges and slightly below the 75°C column on the large ones — a deliberate planning margin. When your inspector is involved, the NEC table plus your AHJ's amendments win.

## Next logical reads

<a href="solar-wiring-and-protection-cost.html" class="text-link">Solar wiring and protection cost</a> <a href="solar-fuses-vs-breakers.html" class="text-link">Solar fuses vs breakers</a> <a href="solar-panels-series-vs-parallel.html" class="text-link">Series vs parallel solar panels</a> <a href="solar-inverter-sizing.html" class="text-link">How to size an inverter</a> <a href="12v-vs-24v-vs-48v-solar.html" class="text-link">How to choose system voltage</a>

---

## Next logical reads

- [Battery Cable Size for Solar Inverters](/pages/battery-cable-size-for-inverter.html) — the high-current side of the same decision, with its calculator
- [Solar Fuse and Breaker Sizing](/pages/solar-fuse-and-breaker-sizing.html) — every wire you size here needs its fuse sized next
- [Solar Wire Size Calculator](/pages/solar-wire-size.html#wire-size-calculator-amps-volts-distance) and the [worked 100W example](#worked-example-what-size-wire-for-a-100w-solar-panel) on this page
