#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$REPO_ROOT/out"

echo "=== Building solarpoweredproject.com ==="

# Clean and recreate output directory
rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR/pages"
mkdir -p "$OUT_DIR/assets/images"
mkdir -p "$OUT_DIR/diy-off-grid-energy"
mkdir -p "$OUT_DIR/guides/solar-battery-cost-2026"
mkdir -p "$OUT_DIR/guides/solar-panel-cost-california"

# Copy root files
cp "$REPO_ROOT/index.html" "$OUT_DIR/"
cp "$REPO_ROOT/styles.css" "$OUT_DIR/"
cp "$REPO_ROOT/script.js" "$OUT_DIR/"
cp "$REPO_ROOT/robots.txt" "$OUT_DIR/"

# Copy pages
cp "$REPO_ROOT/pages/"*.html "$OUT_DIR/pages/"

# Copy assets
cp "$REPO_ROOT/assets/images/"* "$OUT_DIR/assets/images/"

# Copy diy-off-grid-energy section
cp "$REPO_ROOT/diy-off-grid-energy/"*.html "$OUT_DIR/diy-off-grid-energy/"

# Copy guides
cp "$REPO_ROOT/guides/solar-battery-cost-2026/index.html" "$OUT_DIR/guides/solar-battery-cost-2026/"
cp "$REPO_ROOT/guides/solar-panel-cost-california/index.html" "$OUT_DIR/guides/solar-panel-cost-california/"

# Generate sitemap.xml
echo '<?xml version="1.0" encoding="UTF-8"?>' > "$OUT_DIR/sitemap.xml"
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' >> "$OUT_DIR/sitemap.xml"

echo '  <url>' >> "$OUT_DIR/sitemap.xml"
echo '    <loc>https://solarpoweredproject.com/</loc>' >> "$OUT_DIR/sitemap.xml"
echo '  </url>' >> "$OUT_DIR/sitemap.xml"

echo '  <url><loc>https://solarpoweredproject.com/diy-off-grid-energy/</loc></url>' >> "$OUT_DIR/sitemap.xml"

for f in "$OUT_DIR/diy-off-grid-energy/"*.html; do
    filename=$(basename "$f")
    echo "  <url><loc>https://solarpoweredproject.com/diy-off-grid-energy/${filename}</loc></url>" >> "$OUT_DIR/sitemap.xml"
done

for f in "$OUT_DIR/pages/"*.html; do
    filename=$(basename "$f")
    echo "  <url><loc>https://solarpoweredproject.com/pages/${filename}</loc></url>" >> "$OUT_DIR/sitemap.xml"
done

echo '  <url><loc>https://solarpoweredproject.com/guides/solar-battery-cost-2026/</loc></url>' >> "$OUT_DIR/sitemap.xml"
echo '  <url><loc>https://solarpoweredproject.com/guides/solar-panel-cost-california/</loc></url>' >> "$OUT_DIR/sitemap.xml"

echo '</urlset>' >> "$OUT_DIR/sitemap.xml"

PAGE_COUNT=$(find "$OUT_DIR/pages" -name "*.html" | wc -l)
echo "=== Build complete: $PAGE_COUNT pages in out/ ==="
