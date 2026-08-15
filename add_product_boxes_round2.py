#!/usr/bin/env python3
"""Solar affiliate round 2: cost/best-of buyer-intent pages (2026-08-15).

'How much does X cost' visitors are pre-purchase researchers — highest
converting affiliate traffic. 1 box per page (2 on cabin cost), all ASINs
verified. Idempotent. Anchors auto-detected per file.
"""
import re

JOBS = {
    "content/pages/how-much-do-solar-panels-cost.md": (
        '{{< product-box asin="B07GF5JY35" name="Renogy 100W 12V Monocrystalline Panel" label="The DIY price benchmark" description="The panel most cost tables are built around. When installer quotes cite $2.50+/Watt installed, a $1/Watt panel like this shows exactly what the labor and overhead line items cost you." button="Check price on Amazon" >}}'),
    "content/pages/solar-battery-cost-2026.md": (
        '{{< product-box asin="B084DB36KW" name="LiTime 12V 100Ah LiFePO4" label="Best cost-per-kWh in the 2026 field" description="The battery that defines the budget tier of every 2026 battery cost comparison — built-in BMS, low-temp protection, and the cycle life that makes its $/usable-kWh number beat lead-acid." button="Check price on Amazon" >}}'),
    "content/pages/solar-battery-cost-per-kwh.md": (
        '{{< product-box asin="B084DB36KW" name="LiTime 12V 100Ah LiFePO4" label="The $/kWh reference point" description="The battery we benchmark cost-per-kWh math against: 1.28 kWh nominal, thousands of cycles, and a built-in BMS — the datasheet numbers behind realistic DIY cost models." button="Check price on Amazon" >}}'),
    "content/pages/how-much-do-solar-batteries-cost.md": (
        '{{< product-box asin="B084DB36KW" name="LiTime 12V 100Ah LiFePO4" label="The budget-tier anchor" description="When sticker shock from turnkey batteries ($15k+) hits, this is the DIY alternative the math points to — the value benchmark for what a kWh of storage should cost." button="Check price on Amazon" >}}'),
    "content/pages/best-solar-panels-for-home-2026.md": (
        '{{< product-box asin="B07GF5JY35" name="Renogy 100W 12V Monocrystalline Panel" label="The expandable starter panel" description="Not a roof replacement — the panel future-proofers start with. Add-by-add scaling without a re-roof contract, and the efficiency tier that makes 2026 shortlists." button="Check price on Amazon" >}}'),
    "content/pages/mppt-charge-controller-cost.md": (
        '{{< product-box asin="B073ZJ3L13" name="Victron SmartSolar MPPT 100/30" label="The price-performance reference" description="The controller every MPPT cost table benchmarks against — where the diminishing-returns curve flattens. Bluetooth monitoring and lithium presets at the mid-tier price point." button="Check price on Amazon" >}}'),
    "content/pages/solar-inverter-cost.md": (
        '{{< product-box asin="B081CLPDT9" name="Renogy 2000W 12V Pure Sine Inverter" label="Mid-size cost anchor" description="2000W pure sine with remote and cables included — the honest mid-size reference point for inverter cost tables: enough for real loads, without paying for surge headroom you will not use." button="Check price on Amazon" >}}'),
    "content/pages/cabin-solar-cost.md": (
        '{{< product-box asin="B084DB36KW" name="LiTime 12V 100Ah LiFePO4" label="Cabin bank building block" description="The cabin-cost math favorite: 1.28 kWh per unit, scale by stacking. Low-temp protection matters more in cabins than anywhere else on the property." button="Check price on Amazon" >}}\n\n{{< product-box asin="B073ZJ3L13" name="Victron SmartSolar MPPT 100/30" label="Right-sized cabin controller" description="The 30A tier covers most weekend-cabin arrays, and Bluetooth lets you check charging from town — the feature cabin owners actually use." button="Check price on Amazon" >}}'),
    "content/pages/best-solar-panels-for-small-homes.md": (
        '{{< product-box asin="B07GF5JY35" name="Renogy 100W 12V Monocrystalline Panel" label="Right-sized for small homes" description="Small-home budgets need panel efficiency per dollar, not maximum wattage — this is the module that wins that math and scales in affordable increments." button="Check price on Amazon" >}}'),
    "content/pages/best-solar-panels-small-roof.md": (
        '{{< product-box asin="B07GF5JY35" name="Renogy 100W 12V Monocrystalline Panel" label="Small-roof friendly footprint" description="Compact monocrystalline footprint with the output density tight roofs need — easier to fit, wire, and expand than full-size 400W monsters when space is the constraint." button="Check price on Amazon" >}}'),
    "content/pages/how-to-choose-solar-inverter.md": (
        '{{< product-box asin="B081CLPDT9" name="Renogy 2000W 12V Pure Sine Inverter" label="A safe default choice" description="If the sizing math in this guide points you at 2000W continuous, this is the honest default: pure sine, remote switch, cables in the box, from a brand that honors warranties." button="Check price on Amazon" >}}'),
}

BOX_RE = re.compile(r"\{\{<\s*product-box", re.S)
ANCHORS = ["## Next logical reads", "## Related guides", "## Frequently Asked Questions", "## FAQ"]

changed, skipped = [], []
for path, (box,) in [(k, (v,)) for k, v in JOBS.items()]:
    src = open(path).read()
    if BOX_RE.search(src):
        skipped.append(path)
        continue
    idx = min((i for i in (src.rfind(a) for a in ANCHORS) if i != -1), default=-1)
    if idx == -1:
        skipped.append(path + " (no anchor)")
        continue
    src = src[:idx] + box + "\n\n" + src[idx:]
    if "{{< affiliate-disclosure >}}" not in src:
        m = re.search(r"\A(?:\+\+\+.*?\+\+\+|---.*?---)\s*\n", src, re.S)
        if m:
            src = src[:m.end()] + "\n{{< affiliate-disclosure >}}\n" + src[m.end():]
    open(path, "w").write(src)
    changed.append(path)

print(f"changed={len(changed)} skipped={len(skipped)}")
for s in skipped: print("  SKIP " + s)
