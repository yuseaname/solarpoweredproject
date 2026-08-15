#!/usr/bin/env python3
"""Convert plain-markdown FAQ sections (#### Q + answer) to faq shortcode blocks.
Usage: python3 faq_convert.py file1.md [file2.md ...]
Only touches the '## FAQ' section. Idempotent (skips files already converted).
"""
import re, sys

FAQ_HEAD = re.compile(r'^## FAQ.*$', re.M)
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
    # split into question chunks: #### always; ### only if line ends with ?
    parts = re.split(r'^(?=#{4} )|(?:^### +.*\?\s*$)', section, flags=re.M)
    # simpler robust pass: collect (q, body) pairs
    pairs = []
    cur_q, cur_body = None, []
    for line in section.split('\n'):
        mq4 = re.match(r'^#### +(.*)$', line)
        mq3 = re.match(r'^### +(.*\?)\s*$', line)
        if mq4:
            if cur_q: pairs.append((cur_q, '\n'.join(cur_body)))
            cur_q, cur_body = mq4.group(1).strip(), []
        elif mq3:
            if cur_q: pairs.append((cur_q, '\n'.join(cur_body)))
            cur_q, cur_body = mq3.group(1).strip(), []
        elif cur_q is not None:
            cur_body.append(line)
    if cur_q: pairs.append((cur_q, '\n'.join(cur_body)))
    head = section.split('\n')[0] if not re.match(r'^(####|###)', section.strip() or '\n') else ''
    # preamble = lines before first question
    first_q_at = None
    for i, line in enumerate(section.split('\n')):
        if re.match(r'^(#### +|### +.*\?\s*$)', line): first_q_at = i; break
    preamble = '\n'.join(section.split('\n')[:first_q_at]).strip('\n') if first_q_at is not None else section.strip('\n')
    if not pairs:
        return f"SKIP (no questions found): {path}"
    out = [preamble, ''] if preamble else []
    for q, body in pairs:
        body = re.sub(r'\n{3,}', '\n\n', body).strip()
        q_esc = q.replace('"', '\\"')
        out.append(f'{{{{< faq "{q_esc}" >}}}}')
        out.append(body)
        out.append('{{< /faq >}}')
        out.append('')
    new_section = '\n'.join(out).rstrip('\n') + '\n\n'
    open(path, 'w').write(src[:start] + new_section + src[end:])
    return f"CONVERTED ({len(pairs)} FAQs): {path}"

if __name__ == '__main__':
    for p in sys.argv[1:]:
        print(convert(p))
