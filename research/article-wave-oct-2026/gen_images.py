#!/usr/bin/env python3
"""Generate 15 images for solar article wave via Magica MCP (execute_tool API)."""
import json, os, re, time, urllib.request, pathlib

OUT = pathlib.Path('/tmp/solar-wave-images'); OUT.mkdir(exist_ok=True)
STATE = OUT/'state.json'
BASE = "https://api.magica.com/api/mcp"

def call(name, args, i=[0]):
    i[0] += 1
    if name == "execute_tool":
        params = {"name":"execute_tool","arguments":{"tool_name":args.pop("tool"),"input":args}}
    else:
        params = {"name":name,"arguments":args}
    body = json.dumps({"jsonrpc":"2.0","method":"tools/call","id":i[0],
                       "params":params}).encode()
    req = urllib.request.Request(BASE, data=body, headers={
        "Authorization": "Bearer "+os.environ["MAGICA_API_KEY"],
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream"})
    resp = urllib.request.urlopen(req, timeout=300).read().decode()
    # strip SSE prefix if present
    if resp.startswith("event:") or "data:" in resp[:200]:
        lines = [l[5:].strip() for l in resp.splitlines() if l.startswith("data:")]
        resp = lines[-1] if lines else resp
    try:
        env = json.loads(resp)
        content = (env.get("result") or {}).get("content") or []
        texts = [c.get("text","") for c in content if c.get("type")=="text"]
        return {"raw": " ".join(texts) or resp[:500], "env": env}
    except Exception:
        return {"raw": resp[:500], "env": None}

A_PHOTO = "Photorealistic documentary field-guide photo, warm cream and kraft-paper surfaces, terracotta and oak tones, soft natural morning light, muted sage-green and rust-orange accents, realistic hands and tools, no text, no logos, no watermarks. "
B_DIAG = "Clean instructional diagram render on paper-cream background, ink-line schematic style with sage-green fills and rust-orange accent highlights, one single concept, absolutely no text, no letters, no numbers, no labels, no logos. "

IMAGES = {
 # Article 1: batteries series vs parallel
 "BSP-HERO": (A_PHOTO + "Two separate groups of 12-volt solar batteries arranged on a wooden workbench: the left group connected in a chain positive-to-negative in a row, the right group connected side by side with short like-to-like links; a pair of hands with a wrench mid-tightening a battery terminal; sunlight from a window.", "2048x1152"),
 "BSP-SERIES": (B_DIAG + "Two battery symbols stacked in a single loop wired positive to negative, connected to one inverter box, with curved arrows showing voltage accumulating around the loop.", "2048x1152"),
 "BSP-PARALLEL": (B_DIAG + "Two battery symbols placed side by side, their like terminals joined by two horizontal bus bars, one single load path leaving the pair.", "2048x1152"),
 "BSP-CABLE": (A_PHOTO + "Close-up of equal-length paired battery cables with copper lugs neatly laid out on kraft paper beside a hex crimping tool.", "2048x1152"),
 "BSP-BALANCE": (B_DIAG + "A row of four battery symbols wired in series where one unit is drawn visibly smaller and highlighted in orange, showing imbalance in the chain.", "2048x1152"),
 # Article 2: testing solar panels
 "TSP-HERO": (A_PHOTO + "A person in a sun hat crouching beside a small ground-mounted solar panel in golden-hour sun, holding a digital multimeter with probes touching the panel's separated connector leads, meter display visible but blurred.", "2048x1152"),
 "TSP-VOC": (B_DIAG + "A meter symbol connected across the positive and negative output leads of a single solar panel symbol, nothing else attached, open-circuit measurement concept.", "2048x1152"),
 "TSP-ISC": (A_PHOTO + "Close-up of two hands briefly holding multimeter probe tips to a solar panel's connector leads, the meter display mid-reading, blurred digits, bright sunlight on the panel surface.", "2048x1152"),
 "TSP-SHADE": (A_PHOTO + "Half of a rooftop solar panel shaded by a leafy tree branch with dappled shade, a small multimeter resting on the panel frame, warm afternoon light.", "2048x1152"),
 "TSP-KIT": (A_PHOTO + "Flat-lay on kraft paper of a solar panel testing kit: a digital multimeter, adapter cables with solar connectors, insulated gloves, and a small notebook with pen.", "2048x1152"),
 # Article 3: LiFePO4 low voltage cutoff
 "LVC-HERO": (A_PHOTO + "A rack-mounted lithium battery module standing beside a wall-mounted power inverter in a tidy garage, morning light coming through an open door, cream walls.", "2048x1152"),
 "LVC-LADDER": (B_DIAG + "A vertical ladder of horizontal bars at descending heights representing voltage thresholds, with a gently falling line descending past the lowest bar marked by an orange highlight.", "2048x1152"),
 "LVC-BMS": (B_DIAG + "A battery pack symbol with an internal circuit board bridging its cells to the output terminals, and a switch symbol drawn on the negative output path.", "2048x1152"),
 "LVC-SAG": (A_PHOTO + "A power inverter's display glowing softly in a dim garage at dusk indicating a warning state with abstract unreadable symbols, battery bank cabinets behind it.", "2048x1152"),
 "LVC-COLD": (A_PHOTO + "A battery bank in a cold garage with frost patterns on the window and faint breath fog in the air, cool blue-grey light mixing with a warm lamp.", "2048x1152"),
}

state = json.loads(STATE.read_text()) if STATE.exists() else {}
for k, v in state.items():
    if v.get("done") and pathlib.Path(v.get("file","")).exists():
        print(f"[skip] {k}"); continue

for key, (prompt, res) in IMAGES.items():
    if state.get(key, {}).get("done"): continue
    try:
        r = call("execute_tool", {"tool":"generate","modelId":"gpt-image-2-text","prompt":prompt,
                                  "size":"2048x1152","quality":"medium"})
        txt = r.get("raw","") if isinstance(r, dict) else str(r)
        m = re.search(r'Run ID: ([a-z0-9]+)', txt) or re.search(r'(cm[a-z0-9]{20,})', txt)
        run = m.group(1) if m else None
        print(f"[submit] {key} run={run}")
        url = None
        for _ in range(60):
            time.sleep(6)
            try:
                s = call("get_run_status", {"runId":run, "runType":"model"})
                stxt = s.get("raw","") if isinstance(s, dict) else str(s)
                m2 = re.search(r'https?://[^"\\\s]+\.png', stxt)
                cand = m2.group(0).replace("\\/","/") if m2 else None
                status = None
            except Exception as e:
                print(f"[poll-err] {key}: {e}"); continue
            if cand:
                url = cand; break
            if status in ("failed","error"):
                print(f"[fail] {key}: {str(s)[:200]}"); break
        if url:
            data = urllib.request.urlopen(url, timeout=120).read()
            f = OUT/f"{key}.png"; f.write_bytes(data)
            state[key] = {"done": True, "file": str(f), "url": url}
            STATE.write_text(json.dumps(state, indent=1))
            print(f"[done] {key} OK ({len(data)//1024}KB)")
        else:
            state[key] = {"done": False, "run": run}; STATE.write_text(json.dumps(state, indent=1))
    except Exception as e:
        print(f"[error] {key}: {e}")
        state[key] = {"done": False, "err": str(e)[:200]}
        STATE.write_text(json.dumps(state, indent=1))
print("ALL DONE")
