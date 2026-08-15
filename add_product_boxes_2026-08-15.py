#!/usr/bin/env python3
"""Add product boxes to 6 high-traffic buyer-intent pages (2026-08-15).

Traffic-ranked targets from RYBBIT_BASELINE top_10_pages. Idempotent: skips
files that already contain the box. Disclosure shortcode added after front
matter where missing.
"""
import re, sys

JOBS = {
    "content/pages/battery-cable-size-for-inverter.md": [
        '{{< product-box asin="B08B7VPWD4" name="IWISS Battery Lug Crimper (10–2/0 AWG)" label="The crimp tool lugs deserve" description="A proper hex/indent crimper for 10 AWG to 2/0 battery lugs — the difference between a connection you trust at 100A and one that heats. If you are building inverter cables, this is the tool." button="Check price on Amazon" >}}'
    ],
    "content/pages/12v-vs-24v-vs-48v-solar.md": [
        '{{< product-box asin="B084DB36KW" name="LiTime 12V 100Ah LiFePO4" label="12V building block" description="The value benchmark for starting a 12V bank — built-in 100A BMS, low-temp protection, and thousands of cycles. (Going 24V/48V? Series/parallel-match these.)" button="Check price on Amazon" >}}',
        '{{< product-box asin="B073ZJ3L13" name="Victron SmartSolar MPPT 100/30" label="Voltage-flexible controller" description="Auto-detects 12V/24V (48V-capable across the range) with Bluetooth monitoring and lithium presets — the controller that grows with a voltage upgrade." button="Check price on Amazon" >}}'
    ],
    "content/pages/solar-fuse-and-breaker-sizing.md": [
        '{{< product-box asin="B08L56RDNP" name="BougeRV 15A MC4 Inline Fuse Kit (5-pk)" label="String-level protection" description="Waterproof IP68 in-line fuse holders for panel strings — the cheapest insurance a DIY array can buy. Match the fuse rating to your string current." button="Check price on Amazon" >}}',
        '{{< product-box asin="B00MYSQM58" name="Blue Sea 100A Mini BusBar" label="Clean distribution point" description="A tinned-copper busbar for battery/inverter distribution — the tidy, inspectable alternative to stacked ring terminals that protection devices can actually guard." button="Check price on Amazon" >}}'
    ],
    "content/pages/mppt-charge-controller-not-charging.md": [
        '{{< product-box asin="B018CLOSTC" name="Klein Tools MM600 Multimeter" label="First diagnostic tool" description="Step one of every MPPT troubleshooting checklist is measuring PV voltage — an auto-ranging 1000V meter like this is the tool that answers it." button="Check price on Amazon" >}}'
    ],
    "content/pages/solar-panel-output.md": [
        '{{< product-box asin="B018CLOSTC" name="Klein Tools MM600 Multimeter" label="Verify real output" description="Estimated output is theory; a meter is truth. A 1000V-rated auto-ranging multimeter lets you confirm panel Voc and string voltage against spec-sheet numbers." button="Check price on Amazon" >}}'
    ],
    "content/pages/pure-sine-vs-modified-sine-inverter.md": [
        '{{< product-box asin="B081CLPDT9" name="Renogy 2000W 12V Pure Sine Inverter" label="Our pure sine pick" description="2000W continuous pure sine with remote switch and cables included — sized for the mid-size off-grid loads where waveform quality actually matters." button="Check price on Amazon" >}}'
    ],
}

ANCHOR = "## Next logical reads"
BOX_RE = re.compile(r"\{\{<\s*product-box", re.S)

changed, skipped = [], []
for path, boxes in JOBS.items():
    src = open(path).read()

    # 1. product boxes before final anchor
    if BOX_RE.search(src):
        skipped.append(path + " (already has box)")
    else:
        idx = src.rfind(ANCHOR)
        if idx == -1:
            skipped.append(path + " (anchor missing!)")
            continue
        block = "\n" + "\n\n".join(boxes) + "\n\n"
        src = src[:idx] + block.lstrip("\n") + "\n" + src[idx:]
        changed.append(path)

    # 2. disclosure after front matter if missing
    if "{{< affiliate-disclosure >}}" not in src:
        m = re.search(r"\A(?:\+\+\+.*?\+\+\+|---.*?---)\s*\n", src, re.S)
        if m:
            src = src[:m.end()] + "\n{{< affiliate-disclosure >}}\n" + src[m.end():]
            if path not in changed:
                changed.append(path + " (+disclosure)")
        else:
            skipped.append(path + " (no front matter found)")

    open(path, "w").write(src)

print("CHANGED:")
for c in changed: print("  " + c)
print("SKIPPED:")
for s in skipped: print("  " + s)
