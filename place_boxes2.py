#!/usr/bin/env python3
"""Wave 2 product boxes: portable panels + DIY battery sections."""
import re

BASE = "/mnt/ai-shared/cluster/websites/adsense-portfolio/solarpoweredproject"

JOBS = [
    ("content/pages/portable-solar-panels.md",
     "Brands like Renogy or Bougevert. These offer reliable monocrystalline cells and better weather resistance (IP67 ratings).",
     '{{< product-box asin="B07GF5JY35" name="Renogy 100W 12V Monocrystalline Panel" label="Solid mid-range pick" description="The reliable mid-tier standard — monocrystalline cells, IP67 weather rating, and the compatibility footprint (brackets, branch connectors) every RV build already assumes." button="Check price on Amazon" >}}'),
    ("content/pages/best-solar-batteries-2026.md",
     "You can use a high-quality 200W Renogy panel with a cheap LiFePO4 battery and a separate Victron controller.",
     '{{< product-box asin="B00BFCNFRM" name="Renogy 100W Starter Kit (Panel + 30A PWM Controller)" label="DIY starter bundle" description="Panel, controller, brackets, and cables in one box — the classic first step for a DIY bank you expand later. Add a LiFePO4 battery and you have a working system." button="Check price on Amazon" >}}'),
    ("content/pages/best-solar-batteries-2026.md",
     "See our [battery capacity calculator](battery-capacity.html) to size a DIY bank.",
     '{{< product-box asin="B084DB36KW" name="LiTime 12V 100Ah LiFePO4" label="DIY bank building block" description="The value benchmark for DIY banks — built-in 100A BMS, low-temp protection, and thousands of cycles at a fraction of turnkey cost per kWh." button="Check price on Amazon" >}}'),
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
        print(f"SKIP: {path} already has a box")
        continue
    new, err = insert_after_paragraph(src, anchor, box)
    if err:
        print(f"FAIL {path}: {err}")
        continue
    open(fp, "w").write(new)
    changed += 1
    print(f"OK {path}")
print(f"\ninserted: {changed}/{len(JOBS)}")
