# TABLE-FIELDS — Recommended comparison-table fields by niche

*Authored by the Boss 2026-09-05 (seat rt-template's file was truncated before delivery; fields verified against the site's verified fact packs).*

**Source tiers:** **T2** = manufacturer-stated (mark "per manufacturer spec", note retrieval date) · **T3** = reputable third party (cite URL + date; NEC/ABYC code citations go here) · **T4** = editorial estimate/band (must be labeled "band"/"typically"/"class") · **DERIVED** = arithmetic from T2 inputs (show the formula once).

## Never-display fields (all niches, hard rule)

Amazon price or any per-listing price · sale/discount/percent-off · availability or stock · star ratings · review counts or review text · "best seller"/"Amazon's choice" badges · savings claims ("save $X"). Dynamic listing data must come from Amazon-approved mechanisms only — this site uses none, so it displays none. The box's "Check price on Amazon" button and its built-in disclosure are the compliant path.

## 1. Solar panels (roof/installed)

| Field | Tier | Verification note |
|---|---|---|
| Nameplate wattage (W) | T2 | datasheet |
| Module efficiency (%) | T2 | datasheet; state "up to" |
| Temperature coefficient (%/°C) | T2 | datasheet |
| Power density (W/ft²) | DERIVED | W ÷ (L×W in ft); show one worked example |
| Dimensions / weight | T2 | datasheet |
| Product / performance warranty (yr) | T2 | warranty PDF; note capacity-retention floor |
| Cell type / architecture (mono PERC, IBC, TOPCon) | T2 | datasheet; do NOT guess architecture from brand |
| Degradation (first-year + annual %) | T2 | datasheet |
| Availability channel (installer-only vs DIY) | T4 | editorial; e.g., "primarily international post-restructuring" |

Known trap: brand exits (LG 2022, Panasonic 2025-04-28). Any brand-name row must be re-verified at publish time; dead lineups get removed, not remarked upon.

## 2. Charge controllers (MPPT/PWM)

| Field | Tier | Note |
|---|---|---|
| Max PV input voltage (V) | T2 | the decisive field |
| Max charge current (A) | T2 | |
| Rated PV power @12V / @24V | T2 | datasheet |
| Battery voltages supported | T2 | 12/24 auto vs 48V-capable |
| Monitoring (Bluetooth built-in / optional adapter) | T2 | |
| Lithium profiles / presets | T2 | |
| Remote battery-temp sensor input | T2 | |
| Warranty (yr) | T2 | verify on warranty page — do not assume |
| Typical price class (Budget/Mid) | T4 | label "class", never $ |

DERIVED fields that earn their columns: charge current ≈ watts ÷ battery V × 1.25; cold-adjusted Voc (Voc × (1 + 0.003 × °C below 25)) — both with formulas shown.

## 3. Batteries — installed home systems

| Field | Tier | Note |
|---|---|---|
| Usable capacity (kWh) | T2 | insist on usable vs nameplate distinction |
| Continuous AC power (kW) | T2 | off-grid vs grid-tied ratings differ — footnote |
| Chemistry | T2 | caveat when the maker doesn't publish it |
| Warranty: years + retention % + throughput cap | T2 | all three terms |
| Stackability (units per gateway/controller) | T2 | |
| Installed cost ($/kWh band) | T4 | "planning band" label + link to dated cost guide |

## 4. Batteries — DIY/drop-in (LiFePO4)

| Field | Tier | Note |
|---|---|---|
| Nominal voltage (V) | T2 | LiTime-class: 12.8V nominal (site convention: Ah × 12.8 = Wh) |
| Capacity (Ah) and nameplate Wh | T2 / DERIVED | never call nameplate "usable" |
| Usable Wh at stated DoD | DERIVED | show the ×0.8 (or maker's DoD) once |
| BMS continuous rating (A) | T2 | determines load ceiling |
| Cycle life @ DoD | T2 | datasheet condition must match the DoD cited |
| Low-temperature charge cutoff | T2 | safety-relevant |
| Warranty (yr) | T2 | pack-level vs system-level distinction |

## 5. Inverters / inverter-chargers

| Field | Tier | Note |
|---|---|---|
| Continuous output (W) | T2 | |
| Surge/peak (W, duration) | T2 | duration often buried — check |
| Waveform (pure/modified sine) | T2 | |
| DC input voltage (12/24/48V) | T2 | |
| Efficiency (%) | T2 | at what load — footnote if stated |
| Outlets/ports, remote switch | T2 | |
| Warranty (yr) | T2 | |
| Battery-side current at rated load | DERIVED | W ÷ (V × 0.9); drives cable/fuse pages |

## 6. Portable power stations ("solar generators")

| Field | Tier | Note |
|---|---|---|
| Capacity (Wh) | T2 | nameplate |
| Usable estimate | DERIVED | ×0.85 typical unless maker states DoD |
| Continuous / surge AC (W) | T2 | |
| Cell chemistry (LiFePO4 vs NMC) | T2 | safety + cycle-life implications |
| Max solar input (W) + charge time at that input | T2 | the "recharging reality" field |
| Cycle life to 80% | T2 | |
| Weight | T2 | portability decision |
| Airline carry-on legal (≤100Wh)? | DERIVED | from Wh |

## 7. Wiring, fusing, breakers

| Field | Tier | Note |
|---|---|---|
| Conductor ampacity by gauge | T3 | NEC 310.16 (cite table; note 60°C vs 75°C column) |
| Derating conditions | T3 | NEC 310.15 |
| PV max current = Isc × 1.25 | T3 | NEC 690.8(A) |
| Conductor sizing ≥125% | T3 | NEC 690.8(B) |
| OCPD sizing (string fuse ≈ Isc × 1.56) | T3 | NEC 690.9(B) |
| Terminal-fuse distance (≤150 mm) | T3 | ABYC E-11 (marine/DIY bank context) |

Code fields never editorialize: quote the rule, cite the section, and hedge ("verify against the current adopted code edition with your inspector").

## 8. Solar lights / phone chargers (consumer small-solar)

| Field | Tier | Note |
|---|---|---|
| Output (W) / lumens | T2 | treat as CLAIMED — budget makers exaggerate lumens; say "claimed lumens" |
| IP rating | T2 | maps to real use (IPX4 rain vs IP65 jets vs IP67 immersion) |
| Integrated battery mAh / Wh | T2 | note usable derate |
| Port specs (2.1A USB-A, USB-C PD) | T2 | charging-speed decision |
| Cell/coating material (ETFE vs PET) | T2 | longevity field |
| Weight / mount style | T2 | |

**Editorial-band fields** (allowed, must be labeled): "budget tier ($3–$5/W class)", "mid-range tier", runtime bands from the site's own worked math.

---

## General rules

1. A column that can't be filled with T2/T3/DERIVED data for every row doesn't ship — no half-empty comparison tables, no "N/A" walls.
2. Every table carries a source-note footer + as-of line ("specs retrieved [date]; specs drift — verify against the live datasheet").
3. One worked example per table minimum (density, usable Wh, battery amps) so readers can extend the table to products not listed.
4. Rows are scenario-labeled ("Best for: X") not rank-ordered; no row is visually crowned.
