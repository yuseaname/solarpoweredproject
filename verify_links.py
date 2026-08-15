#!/usr/bin/env python3
"""Verify built artifact: internal link integrity (quote-less attrs after minify)."""
import re, os, glob

bad, checked = [], 0
for f in glob.glob('public/**/*.html', recursive=True):
    html = open(f, errors='replace').read()
    for m in re.finditer(r'href=(/[^"\'#\s>]+)', html):
        target = m.group(1)
        if target.startswith(('/images', '/css', '/assets')):
            continue
        checked += 1
        path = 'public' + target
        if not (os.path.exists(path) or os.path.exists(os.path.join(path, 'index.html')) or os.path.exists(path.rstrip('/') + '/index.html')):
            bad.append((target, f.replace('public/', '')))

print(f"internal links checked: {checked}")
print(f"broken: {len(bad)}")
for t, src in bad[:15]:
    print(f"  {t}  <-  {src}")
