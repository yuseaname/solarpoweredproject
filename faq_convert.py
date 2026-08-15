#!/usr/bin/env python3
"""Convert plain-markdown FAQ sections (#### Q + answer) to faq shortcode blocks.
Usage: python3 faq_convert.py file1.md [file2.md ...]
Only touches the '## FAQ' section. Idempotent (skips files already converted).
"""
import re, sys

FAQ_HEAD = re.compile(r'^## FAQ\s*$', re.M)
NEXT_SECTION = re.compile(r'^## ', re.M)

def convert(path: str) -> str:
    src = open(path).read()
    if '{{< faq' in src:
        return f"SKIP (already converted): {path}"
    m = FAQ_HEAD.search(src)
    if not m:
        return f"SKIP (no FAQ section): {path}"
    # section boundaries
    start = m.end()
    nxt = NEXT_SECTION.search(src, start)
    end = nxt.start() if nxt else len(src)
    section = src[start:end]
    # split into #### chunks
    parts = re.split(r'^#### +', section, flags=re.M)
    head = parts[0].strip('\n')
    if len(parts) < 2:
        return f"SKIP (no #### questions): {path}"
    out = [head, ''] if head else []
    for chunk in parts[1:]:
        lines = chunk.split('\n')
        q = lines[0].strip()
        body = '\n'.join(lines[1:]).strip('\n')
        # strip trailing separators/blank noise
        body = re.sub(r'\n{3,}', '\n\n', body).strip()
        if not q:
            continue
        q_esc = q.replace('"', '\\"')
        out.append(f'{{{{< faq "{q_esc}" >}}}}')
        out.append(body)
        out.append('{{< /faq >}}')
        out.append('')
    new_section = '\n'.join(out).rstrip('\n') + '\n\n'
    open(path, 'w').write(src[:start] + new_section + src[end:])
    return f"CONVERTED ({len(parts)-1} FAQs): {path}"

if __name__ == '__main__':
    for p in sys.argv[1:]:
        print(convert(p))
