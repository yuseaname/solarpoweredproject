+++

title = "Solar Fuse and Breaker Sizing: A Simple Planning Guide (By Circuit)"
slug = "solar-fuse-and-breaker-sizing"
date = 2026-05-31
draft = false
description = "Solar fuse sizing and breaker sizing explained with a circuit-by-circuit planning flow: PV array, controller-to-battery, battery-to-inverter, and service disconnects using DC-rated hardware."
image = "/assets/images/field-guide/wiring-protection-diagram.jpg"
image_alt = "Wiring protection diagram showing fuse and disconnect placement between battery and inverter"
author = "Solar Powered Project"
image_width = 1024
image_height = 768
related = [
  "/pages/battery-cable-size-for-inverter.html",
  "/pages/solar-wire-size.html",
  "/pages/solar-fuses-vs-breakers.html"
]
+++

{{< affiliate-disclosure >}}
<a href="#takeaways" class="text-link">Key takeaways</a> <a href="#protecting" class="text-link">What fuses/breakers protect (and what they don’t)</a> <a href="#circuits" class="text-link">The 4 common solar circuits</a> <a href="#labels" class="text-link">Sizing using labels (avoid guesswork)</a> <a href="#placement" class="text-link">Placement rules-of-thumb</a> <a href="#dc-rated" class="text-link">DC-rated checklist</a> <a href="#mistakes" class="text-link">Common mistakes</a> <a href="#faq" class="text-link">FAQ</a> <a href="#next" class="text-link">Next logical reads</a>

## Key takeaways

-   Start by identifying the circuit: PV wiring, controller-to-battery, or battery-to-inverter.
-   Size protection using **real equipment ratings** (labels/specs), not “typical” numbers.
-   Use **DC-rated** devices at the correct voltage rating—AC-only gear is not a substitute.

## Quick sizing reference (planning-level)

Match fuse/breaker size to the **wire ampacity**, not the load. The protection device should be rated at or slightly below the wire's safe current-carrying capacity.

| Circuit | Wire gauge | Typical fuse/breaker | Notes |
| :-- | :-- | :-- | :-- |
| Small PV string (1–2 panels) | 10 AWG | 15–20A | Match to panel Isc × 1.56 |
| Large PV string (3+ parallel) | 8–6 AWG | 20–30A per string | Each parallel string needs its own |
| Controller → battery (30A MPPT) | 8 AWG | 40A | Sized to controller max output |
| Controller → battery (60A MPPT) | 6 AWG | 80A | One size above controller rating |
| Battery → 1000W inverter (12V) | 4 AWG | 100–125A | High-current DC-rated breaker |
| Battery → 2000W inverter (12V) | 4/0 AWG | 200–250A | Class T fuse or MRBF |
| Battery → 2000W inverter (24V) | 4 AWG | 100–125A | Verify inverter specs |
| Battery → 3000W inverter (48V) | 4 AWG | 80–100A | Always DC-rated |

**Golden rule:** the fuse protects the wire. If a fuse keeps blowing, the answer is never "install a bigger fuse" — it means something else is wrong. Check for overloads, shorts, or loose connections.

<a href="solar-fuses-vs-breakers.html" class="text-link">Solar fuses vs breakers (what to use where)</a> <a href="wiring-decisions.html" class="text-link">Solar wiring decisions (pillar hub)</a>


## Fuse and breaker calculator (by circuit)

Pick the circuit you're protecting, enter the number from the equipment label, and get a planning-level fuse size using this guide's rules.

<form id="fuse-form" class="space-y-4 p-4 bg-gray-50 rounded-lg border border-gray-200">
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
    <div>
      <label class="block text-sm font-medium text-gray-700" for="fuse-circuit">Circuit</label>
      <select id="fuse-circuit" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
        <option value="pv" selected>PV string → charge controller</option>
        <option value="controller">Charge controller → battery</option>
        <option value="inverter">Battery → inverter</option>
      </select>
    </div>
    <div id="fuse-input-wrap">
      <label class="block text-sm font-medium text-gray-700" for="fuse-input" id="fuse-input-label">Panel short-circuit current Isc (A)</label>
      <input type="number" id="fuse-input" value="6" min="0.5" max="400" step="0.1" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
    </div>
  </div>
  <div id="fuse-inv-wrap" class="hidden grid grid-cols-1 sm:grid-cols-2 gap-4">
    <div>
      <label class="block text-sm font-medium text-gray-700" for="fuse-watts">Inverter watts (continuous)</label>
      <input type="number" id="fuse-watts" value="1000" min="100" max="6000" step="50" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700" for="fuse-volts">Battery voltage</label>
      <select id="fuse-volts" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500 px-3 py-2 border">
        <option value="12" selected>12V</option>
        <option value="24">24V</option>
        <option value="48">48V</option>
      </select>
    </div>
  </div>
  <button type="button" id="calc-fuse" class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">Calculate fuse size</button>
</form>

<div id="fuse-results" class="mt-6 hidden">
  <h3>Your protection plan (planning-level)</h3>
  <table>
  <thead><tr><th>Result</th><th>Value</th></tr></thead>
  <tbody>
    <tr><td>Continuous current</td><td id="fuse-amps"></td></tr>
    <tr><td>Recommended fuse/breaker</td><td id="fuse-size"></td></tr>
  </tbody>
  </table>
  <p id="fuse-notes"></p>
</div>

<div class="calc-actions hidden mt-3" data-target="fuse-results">
  <button type="button" class="calc-copy px-3 py-1.5 text-sm font-medium rounded-md border border-gray-300 bg-white hover:bg-gray-50">Copy results</button>
  <button type="button" class="calc-print px-3 py-1.5 text-sm font-medium rounded-md border border-gray-300 bg-white hover:bg-gray-50">Print</button>
  <span class="calc-copied hidden text-sm text-green-600 ml-2">Copied!</span>
</div>

{{< toolscript id="calc-actions-fuse-results" >}}
(function(){
  var actions = document.querySelector('.calc-actions[data-target="fuse-results"]');
  var target = document.getElementById('fuse-results');
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
{{< toolscript id="fuse-calc" >}}
  var SIZES = [5,7.5,10,15,20,25,30,35,40,45,50,60,70,80,90,100,110,125,150,175,200,225,250,300,350,400];
  function nextStd(a){
    for (var i=0;i<SIZES.length;i++){ if (SIZES[i] >= a) return SIZES[i]; }
    return null;
  }
  function circuit(){ return document.getElementById('fuse-circuit').value; }
  function syncInputs(){
    var c = circuit();
    document.getElementById('fuse-inv-wrap').classList.toggle('hidden', c !== 'inverter');
    var lbl = document.getElementById('fuse-input-label');
    var inp = document.getElementById('fuse-input');
    if (c === 'pv') { lbl.textContent = 'Panel short-circuit current Isc (A)'; inp.value = 6; }
    if (c === 'controller') { lbl.textContent = 'Controller max output current (A)'; inp.value = 30; }
    if (c === 'inverter') { lbl.textContent = 'Not used for inverter circuit'; }
  }
  function calcFuse(){
    var c = circuit(), notes = [], amps, target, sized;
    if (c === 'pv') {
      amps = parseFloat(document.getElementById('fuse-input').value) || 0;
      target = amps * 1.56;
      sized = nextStd(target);
      notes.push('PV string rule: Isc \u00d7 1.56 (' + amps + ' A \u00d7 1.56 = ' + target.toFixed(1) + ' A).');
      notes.push('Fuse each parallel string individually. A single series string usually needs no string fuse \u2014 check whether one parallel string can back-feed another.');
    } else if (c === 'controller') {
      amps = parseFloat(document.getElementById('fuse-input').value) || 0;
      target = amps * 1.25;
      sized = nextStd(target);
      notes.push('Controller-to-battery rule: max output \u00d7 1.25 (' + amps + ' A \u00d7 1.25 = ' + target.toFixed(1) + ' A).');
      notes.push('Place it close to the battery end so the battery side is protected.');
    } else {
      var w = parseFloat(document.getElementById('fuse-watts').value) || 0;
      var v = parseFloat(document.getElementById('fuse-volts').value) || 12;
      amps = w / v;
      target = amps * 1.25;
      sized = nextStd(target);
      notes.push('Battery-to-inverter rule: (watts \u00f7 volts) \u00d7 1.25 = ' + amps.toFixed(0) + ' A \u00d7 1.25 = ' + target.toFixed(0) + ' A.');
      if (sized >= 150) notes.push('At this size use a Class T fuse or MRBF \u2014 the interrupt rating matters, not just the amp rating.');
      notes.push('The fuse protects the wire: the cable ampacity must be at or above this fuse rating.');
    }
    document.getElementById('fuse-amps').textContent = amps.toFixed(1) + ' A' + (c === 'pv' ? ' (Isc)' : '');
    document.getElementById('fuse-size').textContent = sized ? sized + ' A' : 'beyond 400 A \u2014 redesign the circuit';
    if (!sized) notes.push('This current level needs an engineered solution, not a bigger fuse.');
    notes.push('Planning-level. Follow the equipment manuals and local code; when in doubt, ask a qualified installer.');
    document.getElementById('fuse-notes').textContent = notes.join(' ');
    document.getElementById('fuse-results').classList.remove('hidden');
  }
  document.getElementById('fuse-circuit').addEventListener('change', function(){ syncInputs(); calcFuse(); });
  document.getElementById('calc-fuse').addEventListener('click', calcFuse);
  syncInputs();
  calcFuse();
{{< /toolscript >}}

## What fuses and breakers protect (and what they don’t)

In planning terms, overcurrent protection exists to reduce the chance that a fault turns wiring into a heater. That’s why people often say “fuses protect the wire.”

**Helpful framing:** protect each circuit at the point where a dangerous fault current could start.

Protection also improves serviceability (being able to isolate parts of the system), but it’s not a substitute for correct cable sizing, tight terminations, or DC-rated disconnects.

<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Electrical_fuses%2C_plug-in_type%2C_different_sizes.jpeg" loading="lazy" width="640" height="427" alt="Assorted DC plug-in fuses used for solar circuit protection." />
<figcaption>Image: havarhen, CC BY-SA 3.0 — Source: <a href="https://commons.wikimedia.org/wiki/File:Electrical_fuses,_plug-in_type,_different_sizes.jpeg" class="text-link">Wikimedia Commons</a></figcaption>
</figure>

## The 4 common solar circuits (pick the one you’re sizing)

### 1) PV array → charge controller

This is the panel side. Whether you need string protection depends on how the array is wired (especially parallel strings) and the controller input requirements.

<a href="solar-panels-series-vs-parallel.html" class="text-link">Solar panels: series vs parallel</a> <a href="mppt-vs-pwm.html" class="text-link">MPPT vs PWM (why input voltage/current matters)</a>

### 2) Charge controller → battery

This circuit is driven by the controller’s maximum output current. It’s one of the cleanest places to use the controller label as your “source of truth.”

### 3) Battery → inverter

This is usually the highest current circuit. It’s also the circuit where placement and DC interrupt ratings matter most.

<a href="solar-inverter-sizing.html" class="text-link">Inverter sizing (watts, surge, draw)</a> <a href="battery-cable-size-for-inverter.html" class="text-link">Battery cable size for inverters (new guide)</a>

### 4) Disconnects and service isolation

Even when a disconnect isn’t strictly “required” for a tiny setup, it can be a big quality-of-life improvement for troubleshooting and safe maintenance.

## Sizing using labels (avoid guesswork)

Use equipment specs first. You’re looking for the maximum current the device can output or draw on that circuit.

-   **Charge controller:** max output current (battery side)
-   **Inverter:** DC input current guidance and/or power rating (battery side)
-   **Panels:** short-circuit current (Isc) and wiring configuration (array side)

If your system is a blend of sources (solar + alternator + generator + shore power chargers), the battery-side protection plan gets more nuanced. When in doubt, ask a qualified installer/electrician.

## Placement rules-of-thumb (planning-level)

-   **Protect near the source:** battery circuits are a classic example because the battery can supply very high fault current.
-   **Short unprotected runs:** keep the section of cable between source and protection as short as practical.
-   **Accessibility matters:** place disconnects where you can actually reach them in an emergency.

<a href="solar-wire-size.html" class="text-link">Solar wire size (amps + distance + drop)</a> <a href="solar-wiring-and-protection-cost.html" class="text-link">Wiring &amp; protection cost (budgeting guide)</a>

## DC-rated checklist (quick sanity check before you buy)

-   **Voltage rating:** device is rated for your system voltage (12V/24V/48V and PV string voltage where relevant).
-   **Interrupt rating:** device can safely open under fault current at that DC voltage.
-   **Environment:** outdoor/UV/water ratings for array-side hardware if exposed.
-   **Compatibility:** terminals accept your cable size without adapters that loosen over time.

If a product page doesn’t clearly state DC ratings, treat that as a red flag.

## Common mistakes (and how to avoid them)

-   **Using AC-only breakers on DC:** not interchangeable; DC arc behavior is different.
-   **Oversizing to stop nuisance trips:** fix the cause (loose lug, undersized cable, overload) instead of “bigger fuse.”
-   **Confusing PV current numbers:** Isc vs operating current matters on the array side.
-   **Protection too far from the battery:** long unprotected battery runs raise risk.
-   **Ignoring system growth:** plan for realistic upgrades (bigger inverter, more strings) if they’re likely.

### If your breaker keeps tripping or fuse keeps blowing

This is one of the most common solar troubleshooting questions. Before replacing anything, work through this checklist:

1.  **Is it actually overloaded?** Add up the running watts of everything on that circuit. If you're pulling more amps than the wire is rated for, the protection is doing its job.
2.  **Loose connection?** A loose lug creates resistance → heat → the breaker senses heat and trips. Check torque on all terminals.
3.  **Undersized wire?** If someone installed too-thin wire for the load, it heats up and trips the breaker. The fix is bigger wire, not a bigger breaker.
4.  **Short circuit?** Look for pinched wires, chafed insulation, or water intrusion. A short trips the breaker instantly, not after a delay.
5.  **Wrong breaker type?** DC breakers and AC breakers behave differently. A DC-rated breaker may nuisance-trip if it's actually an AC unit being used on DC.

<a href="solar-fuses-vs-breakers.html" class="text-link">Solar fuses vs breakers (what to use where)</a> <a href="solar-output-troubleshooting.html" class="text-link">Low solar output troubleshooting</a>



### The code basis (and why our numbers are conservative)

The ×1.25 multipliers above trace to the National Electrical Code's PV rules: **NEC 690.8(A)** defines a PV circuit's maximum current as short-circuit current × 125%, and **NEC 690.9(B)** requires overcurrent protection rated at no less than 125% of that maximum current — which is why PV string fusing lands at roughly **Isc × 1.56**. Battery-side and inverter circuits follow the general **NEC 240** overcurrent rules with equipment datasheets setting the floor. Treat this page's outputs as planning values; the datasheet max fuse rating printed on your controller or inverter is a hard limit, and your AHJ has the final word.

## FAQ

{{< faq "Do I need fuses on solar panels wired in parallel?" >}}
Sometimes. Parallel strings can allow backfeed current into a faulted string depending on configuration. The safest approach is to follow panel and controller guidance and use appropriate string protection when required.
{{< /faq >}}

{{< faq "Breaker vs fuse: which is “better”?" >}}
It depends on the circuit and your goals. Breakers can act as a disconnect and reset after troubleshooting; fuses can be simple and robust. Use devices rated for your system’s DC voltage and expected fault current.
{{< /faq >}}

{{< faq "What does “DC-rated” actually mean?" >}}
It means the device is designed and tested to interrupt current safely on DC at a specified voltage. DC arcs behave differently than AC arcs, so ratings are not interchangeable.
{{< /faq >}}

{{< faq "Why does a correctly-sized fuse still blow sometimes?" >}}
A fuse can blow due to true overloads, surges, heat from a loose connection, or a short. Treat repeated failures as a diagnostic clue—not a reason to oversize protection.
{{< /faq >}}

{{< faq "What’s the safest “first upgrade” for a DIY system?" >}}
If your system lacks clear DC-rated disconnects and correctly placed protection, improving isolation and protection can make maintenance and troubleshooting safer.


{{< /faq >}}

{{< product-box asin="B08L56RDNP" name="BougeRV 15A MC4 Inline Fuse Kit (5-pk)" label="String-level protection" description="Waterproof IP68 in-line fuse holders for panel strings — the cheapest insurance a DIY array can buy. Match the fuse rating to your string current." button="Check price on Amazon" >}}
{{< product-box asin="B094QWG3VV" name="Blue Sea Systems 2315 100A Mini BusBar (4 Studs)" label="Clean distribution point" description="Four-stud tinned-copper busbar with cover — the tidy, inspectable alternative to stacked ring terminals that protection devices can actually guard." button="Check price on Amazon" >}}}}

## Next logical reads

<a href="solar-fuses-vs-breakers.html" class="text-link">Solar fuses vs breakers</a> <a href="solar-panels-series-vs-parallel.html" class="text-link">Series vs parallel panels</a> <a href="solar-wire-size.html" class="text-link">Solar wire size</a> <a href="solar-wiring-and-protection-cost.html" class="text-link">Wiring &amp; protection cost</a> <a href="solar-system-sizing.html" class="text-link">Solar system sizing</a>

---

**Related guides:**
- [Multi-Source Hybrid Off-Grid Charge Controller: Combine Solar, Wind & Hydro](/diy-off-grid-energy/multi-source-hybrid-charge-controller.html)
- [12 Common Solar Installation Mistakes (And How to Avoid Each One)](/pages/common-solar-installation-mistakes.html)
- [Battery Cable Size for Solar Inverters (12V/24V/48V): How to Choose Safely](/pages/battery-cable-size-for-inverter.html)
