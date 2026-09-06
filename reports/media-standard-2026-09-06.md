# House Media Standard — AI-generated article imagery (v1.0, 2026-09-06)

**Authorization:** user directive 2026-09-06 — "generate product images and other media to make my articles outstanding, 3–7 images per article from magica media skill gpt image 2." Engine: Magica `gpt-image-2-text`, `quality: "medium"` (heroes requested at `2048x1152`, inline at `1536x1024`; **practice note:** the engine returns 3:2-family sizes (1536×1024 and 1536×842) regardless — final assets are resized to ≤1536 wide), converted to `.webp` (~q72) on integration, front-matter dims always set from the actual file, matching the existing asset pipeline.

## 1. Honesty rules (binding — same weight as the no-fabricated-testing rule)

1. **Generated images are illustrations, never product photography.** No photorealistic depiction of a specific branded product or SKU (no "LiTime battery", no "Victron controller" renders). Generic, unbranded components only. This is the visual arm of the house rule that we own nothing and test nothing — a fake product photo is a fake test.
2. **No brand names, logos, trademarks, or Amazon marks in any image**, and no in-image text that mimics a product label or rating.
3. **No fabricated testing/measurement scenes** — no bench rigs "measuring" a product, no multimeter readouts implying our measurements, no fake review/testimonial imagery.
4. **Every generated image is labeled in its alt text** as an illustration/diagram ("Illustration of…", "Diagram of…"). Captions, where present, say the same.
5. **Diagrams must be technically consistent with the article's published math** (directions, values, labels verified against the article before publishing; wrong-arrow or wrong-value diagrams are corrections-page material, same as text errors).
6. **No identifiable faces**; scenes and objects over people.
7. Numbers in diagrams only where the article states them; schematic-style otherwise (labels like "PV array", "shunt", "100 A" fine; invented specifics not).

## 2. House visual style (matches the design system)

Flat technical/editorial illustration. Warm paper background (#f7f1e5), deep-orange accents (#a94220 / #d65e2b), charcoal linework (#241c15), occasional muted teal for contrast. Generous whitespace, short legible labels, schematic clarity — the visual language of the existing field-guide diagrams. **No photorealism, no glossy 3D product-render look, no neon-AI gradients, no fake UI screenshots.**

Prompt template: `Flat technical illustration, [SUBJECT], warm paper background, deep orange and charcoal accents, short readable labels ([labels]), generous whitespace, editorial diagram style, no photorealism` (+ size).

## 3. Per-article scope (v1 rollout set, 2026-09-06)

3–5 images per article (hero + 2–4 inline concept figures — 2 inline is compliant, 3–4 for concept-heavy pages), up to 7 where the article's concepts justify. **Count = total including hero**; the article floor is 3. v1 set = the 7 pages published today (which currently reuse themed assets) + dedicated heroes for the 6 pages whose og-fix copied another page's asset (dedupe). ~31 images ≈ 1.3 credits.

| Page | Gets |
|---|---|
| litime-100ah-review | hero + inline: BMS-ceiling gate diagram, 4P4S bank diagram, cold-cutoff timeline |
| lifepo4-charging-below-freezing | hero + inline: plating-vs-intercalation diagram, self-heating flow, heater-energy budget infographic |
| winterizing-off-grid-system | hero + inline: five-job checklist infographic, winter harvest math chart, battery-box cross-section |
| solar-generator-well-pump-sizing | hero + inline: 240V split-phase diagram, pump surge/watts chart, options decision tree |
| van-conversion-solar | hero + inline: van electrical one-line diagram, load-list bar chart, roof-watts reality graphic |
| solar-battery-monitoring-guide | hero + inline: shunt placement diagram, flat-voltage-curve chart, install-rule do/don't |
| jackery-vs-ecoflow-power-stations | hero + inline: gate-math diagram, recharge-time comparison chart, capacity-class scale |
| BMS-explained, enclosure, safety, shading, tilt, load-calc | 1 dedicated hero each (dedupe from copied assets) |

## 4. Pipeline

Brief (concept + prompt + alt + placement) → generate (magica, medium) → **Boss vision-verifies each image against the brief and §1** → convert webp → integrate (front-matter hero or `<figure>` with width/height + lazy loading + honest alt) → build + og-image check → commit. Rejected images are regenerated, never patched in post beyond simple crop/resize.
