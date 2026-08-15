#!/usr/bin/env python3
"""Insert product boxes into solar site pages at exact contextual anchor points."""
import re

BASE = "/mnt/ai-shared/cluster/websites/adsense-portfolio/solarpoweredproject"

# (file, anchor-substring, box-shortcode)
JOBS = [
    ("content/pages/mppt-vs-pwm.md",
     "Many modern MPPT controllers include presets for LiFePO4 and other lithium chemistries.",
     '{{< product-box asin="B073ZJ3L13" name="Victron SmartSolar MPPT 100/30" label="Our MPPT pick" description="The 100V/30A SmartSolar most DIY builds standardize on — Bluetooth monitoring, lithium presets, and the build quality that made Victron the off-grid default." button="Check price on Amazon" >}}'),
    ("content/pages/solar-battery-management-system-explained.md",
     "Cost: $100–200 for a good one (Victron BMV-712, SmartShunt, etc.).",
     '{{< product-box asin="B075RTSTKS" name="Victron BMV-712 Battery Monitor" label="Recommended monitor" description="Shunt-based monitoring with Bluetooth and detailed in-app history — the unit our own wiring diagrams assume. If you run lead-acid, this is the $200 that saves a $1,000 bank." button="Check price on Amazon" >}}'),
    ("content/pages/rv-solar-cost.md",
     "Many beginners skip this and regret it.",
     '{{< product-box asin="B075RTSTKS" name="Victron BMV-712 Battery Monitor" label="Worth-it upgrade" description="Exact state-of-charge at a glance. The component most often skipped and most often regretted." button="Check price on Amazon" >}}'),
    ("content/pages/solar-generator.md",
     "a standalone Pure Sine Wave inverter.",
     '{{< product-box asin="B084DB36KW" name="LiTime 12V 100Ah LiFePO4" label="Budget battery pick" description="The value benchmark in DIY LiFePO4 — built-in 100A BMS, low-temp cutoff, and the track record that made it the default recommendation in budget build guides." button="Check price on Amazon" >}}'),
]

BOX_RE = re.compile(r'\{\{<\s*product-box[^>]*>\}\}', re.S)

def insert_after_paragraph(text, anchor, box):
    idx = text.find(anchor)
    if idx == -1:
        return None, "anchor not found"
    para_end = text.find("\n\n", idx)
    if para_end == -1:
        para_end = len(text)
    return text[:para_end + 2] + box + "\n\n", None

changed = 0
for path, anchor, box in JOBS:
    fp = f"{BASE}/{path}"
    src = open(fp).read()
    if BOX_RE.search(src):
        print(f"SKIP (already has box): {path}")
        continue
    new, err = insert_after_paragraph(src, anchor, box)
    if err:
        print(f"FAIL {path}: {err}")
        continue
    open(fp, "w").write(new)
    changed += 1
    print(f"OK {path}")
print(f"\ninserted: {changed}/{len(JOBS)}")
