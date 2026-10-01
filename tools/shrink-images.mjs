// Turns the product originals saved by fetch-catalogue-images.py (assets/products/originals/*.png)
// into the 320px WebP files the pages use (assets/products/*.webp), so a phone on mobile data
// downloads a few kilobytes per picture instead of a few hundred. Uses Playwright's Chromium to
// draw and encode, because the repo has no image library: `node tools/shrink-images.mjs`.
// The originals folder is git-ignored.
import { chromium } from 'playwright';
import { readdirSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const DIR = new URL('../assets/products/', import.meta.url).pathname;
const SRC = join(DIR, 'originals');
if (!existsSync(SRC)) { console.error('nothing to shrink: run tools/fetch-catalogue-images.py first'); process.exit(1); }
const browser = await chromium.launch();
const page = await browser.newPage();
for (const name of readdirSync(SRC).filter((n) => /\.(png|jpe?g)$/i.test(n))) {
  const b64 = readFileSync(join(SRC, name)).toString('base64');
  const type = name.toLowerCase().endsWith('png') ? 'png' : 'jpeg';
  const out = await page.evaluate(async ({ b64, type }) => {
    const img = new Image();
    img.src = `data:image/${type};base64,${b64}`;
    await img.decode();
    const w = 320, h = Math.round((img.height / img.width) * w);
    const c = document.createElement('canvas'); c.width = w; c.height = h;
    const ctx = c.getContext('2d'); ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, w, h); ctx.drawImage(img, 0, 0, w, h);
    return c.toDataURL('image/webp', 0.8).split(',')[1];
  }, { b64, type });
  const dest = join(DIR, name.replace(/\.(png|jpe?g)$/i, '.webp'));
  writeFileSync(dest, Buffer.from(out, 'base64'));
  console.log(`${name} -> ${dest.split('/').pop()} (${Math.round(Buffer.from(out, 'base64').length / 1024)} KB)`);
}
await browser.close();
