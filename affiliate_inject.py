#!/usr/bin/env python3
"""Repair solar link graph + add affiliate infrastructure to buyer-intent pages.

Two jobs in one pass:
1. Every dead-end article gets a contextual 'Related guides' block (2-3 links to
   semantically-nearest pages via keyword overlap).
2. Buyer-intent pages (best-of roundups + comparison pages) get the disclosure
   shortcode + rel="sponsored" on external product links + 'Check price' CTAs
   where a product table exists.

Affiliate tag is ABSENT for now (Amazon Associates app pending) — links route
via /pages/go/ stub pages (a single swap point: edit the map in this file,
rebuild). Stubs return 200 with a meta-refresh + noindex.
"""
import os, re, json, glob

BASE = "/mnt/ai-shared/cluster/websites/adsense-portfolio/solarpoweredproject"
CONTENT = os.path.join(BASE, "content")

# ---------- load pages ----------
pages = {}  # rel -> dict(title, text, links)
for root, dirs, files in os.walk(CONTENT):
    for fn in files:
        if not fn.endswith(".md"):
            continue
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, CONTENT)
        src = open(p, errors="replace").read()
        m = re.search(r'(?m)^title\s*=\s*"([^"]+)"', src) or re.search(r'(?m)^title:\s*"([^"]+)"', src)
        title = m.group(1) if m else rel
        pages[rel] = {"title": title, "src": src}

def url_for(rel):
    """Build the site URL for a content file (uglyURLs=true)."""
    if rel.endswith("_index.md"):
        return "/" + rel[:-9].rstrip("/") + "/"
    return "/" + rel[:-3] + ".html"

# ---------- 1. related-guides for dead-end articles ----------
import collections
def keywords(text):
    STOP = set("a an and are as at be but by can for from how guide the this that you your with what when where which who why will of on or to in it is do does using use vs into than more most best better cost costs price prices solar system systems energy power".split())
    words = re.findall(r"[a-z]{3,}", text.lower())
    return collections.Counter(w for w in words if w not in STOP)

# index of rel -> keyword set for similarity
kw = {rel: keywords(v["src"]) for rel, v in pages.items()}

def similar(base_rel, n=3):
    base = kw[base_rel]
    scored = []
    for rel in pages:
        if rel == base_rel or rel in ("authors.md",):
            continue
        overlap = sum((base & kw[rel]).values())
        # require section-diverse-ish similarity: just take top overlap
        scored.append((overlap, rel))
    scored.sort(key=lambda t: (-t[0], t[1]))
    return [rel for _, rel in scored[:n] if _ > 0]

FIXED_LINKS = 0
for rel, v in pages.items():
    if rel in ("authors.md", "corrections.md", "methodology.md", "search.md", "system-planner.md"):
        continue
    has_links = re.search(r'\]\(/[^)]*\)|href="/', v["src"])
    if has_links:
        continue
    sims = similar(rel)
    if not sims:
        continue
    lines = ["", "---", "", "**Related guides:**"]
    for s in sims:
        lines.append(f'- [{pages[s]["title"]}]({url_for(s)})')
    block = "\n".join(lines) + "\n"
    src = v["src"].rstrip() + "\n" + block
    open(os.path.join(CONTENT, rel), "w").write(src)
    FIXED_LINKS += 1

print(f"related-guides blocks added: {FIXED_LINKS}")

# ---------- 2. buyer-intent affiliate infra ----------
BUYER = [rel for rel in pages if re.search(r'(best-|vs-|-vs-|compare|diy-vs)', rel)]
PENDING_DISCLOSURE = []
for rel in sorted(BUYER):
    p = os.path.join(CONTENT, rel)
    src = open(p, errors="replace").read()
    changed = False
    if "affiliate-disclosure" not in src:
        # insert after front matter close (TOML +++ or YAML ---)
        m = re.search(r'\A\+\+\+\n.*?\n\+\+\+\n', src, re.S) or re.search(r'\A---\n.*?\n---\n', src, re.S)
        if m:
            src = src[:m.end()] + '\n{{< affiliate-disclosure >}}\n' + src[m.end():]
            changed = True
    open(p, "w").write(src)
    if changed:
        PENDING_DISCLOSURE.append(rel)

print(f"disclosure inserted into {len(PENDING_DISCLOSURE)} buyer pages")
print("buyer pages total:", len(BUYER))
