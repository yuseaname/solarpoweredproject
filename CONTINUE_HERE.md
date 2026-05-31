# Solar Powered Project — Current State

## Site
- **URL:** https://solarpoweredproject.com
- **Type:** Static HTML content site (solar energy guides)
- **Monetization:** Google AdSense
- **Audience:** US homeowners interested in solar

## Structure
- `pages/` — 76 article HTML pages
- `diy-off-grid-energy/` — 18 DIY energy guides + index
- `guides/` — 2 state-specific guide sections (solar-battery-cost-2026, solar-panel-cost-california)
- `assets/images/` — 11 images
- `index.html` — Homepage
- `styles.css` / `script.js` — Site-wide assets

## Deployment
- **Method:** GitHub Actions → rsync to Hostinger (SSH, port 65002)
- **Target:** `~/domains/solarpoweredproject.com/public_html/`
- **Trigger:** Push to `main` or manual dispatch
- **Build:** `bash scripts/build.sh` → populates `out/`
- **Config:** `deployment-node.yml` (deployment node standard)

## Content Pipeline
- Articles written as markdown, converted via `~/.openclaw/workspace/scripts/md-to-solar-page.py`
- Output HTML placed in `pages/` directory
- Build script copies everything to `out/` and regenerates sitemap.xml

## Last Updated: 2026-05-30
