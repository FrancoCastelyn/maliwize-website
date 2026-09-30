// The gate: Netlify runs this as the build command, so a page that breaks a rule is never published.
// No dependencies. Run it locally with `node tools/check.mjs`.
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join, relative } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname;
const APP = 'https://maliwize.co.za'; // keep in step with APP in tools/pages.py
const fails = [];
const fail = (file, msg) => fails.push(`${file}: ${msg}`);

function pages(dir) {
  return readdirSync(dir).flatMap((name) => {
    const p = join(dir, name);
    if (['tools', 'docs', 'node_modules', '.git'].includes(name)) return [];
    return statSync(p).isDirectory() ? pages(p) : p.endsWith('.html') ? [p] : [];
  });
}

// Copy rules. Rewards come from saving and budgeting, never spending (compliance rail), and
// South African retailers refuse the words "discount" and "voucher" for grocery coupons.
const banned = [
  [/spend more to (earn|get)/i, 'rewards must never be tied to spending more'],
  [/the more you (shop|spend)/i, 'rewards must never be tied to spending more'],
  [/\bdiscounts?\b/i, 'say "coupons" or "rands off selected items", not "discount"'],
  [/\bvouchers?\b/i, 'say "coupons", not "voucher"'],
  [/\b(loan|advance|buy now,? pay later)\b/i, 'Maliwize does not lend or offer credit'],
  [/financial advice(?! ?,? lend)/i, 'only in the "does not give financial advice" line'],
  [/\bwallet\b/i, 'no wallet is live or licensed; do not present one'],
  [/guarantee/i, 'no guarantees of savings'],
];

const files = pages(ROOT);
if (files.length === 0) fail('site', 'no pages found');
let header = null, footer = null;

for (const f of files) {
  const rel = relative(ROOT, f);
  const html = readFileSync(f, 'utf8');
  const text = html.replace(/<[^>]+>/g, ' ');
  if (!/<title>[^<]{10,70}<\/title>/.test(html)) fail(rel, 'title missing or not 10 to 70 characters');
  const d = html.match(/<meta name="description" content="([^"]*)"/);
  if (!d || d[1].length < 50 || d[1].length > 170) fail(rel, 'description missing or not 50 to 170 characters');
  if (!/<html lang="en-ZA">/.test(html)) fail(rel, 'lang must be en-ZA');
  if (/<script\b/i.test(html)) fail(rel, 'no scripts: the site ships no JavaScript (CSP script-src none)');
  if ((html.match(/<h1\b/g) || []).length !== 1) fail(rel, 'exactly one h1 per page');
  for (const [re, why] of banned) {
    const m = text.match(re);
    if (m && !(re.source.startsWith('financial advice') && /does not give financial advice/.test(text))) fail(rel, `"${m[0]}": ${why}`);
  }
  for (const [, href] of html.matchAll(/href="([^"#]+)/g)) {
    if (href.startsWith('https://maliwize.co.za/') && !href.startsWith(APP + '/login') && !href.startsWith('https://maliwize.co.za/sitemap')) {
      if (!html.includes('rel="canonical" href="' + href) && !href.includes('og-image')) fail(rel, `absolute link to the site: ${href} (use a path)`);
    }
    if (/^https?:\/\/[^/]*maliwize/.test(href) && href.includes('/login') && !href.startsWith(APP)) fail(rel, `app link does not use APP (${APP}): ${href}`);
    if (href.startsWith('/') && !href.startsWith('//')) {
      const clean = href.split('?')[0];
      const target = clean.endsWith('/') ? join(ROOT, clean, 'index.html') : join(ROOT, clean);
      if (!existsSync(target)) fail(rel, `broken link ${href}`);
    }
  }
  for (const [, src] of html.matchAll(/src="(\/[^"]+)"/g)) if (!existsSync(join(ROOT, src))) fail(rel, `missing file ${src}`);
  const h = html.match(/<header class="top">[\s\S]*?<\/header>/)?.[0].replace(/ aria-current="page"/g, '');
  const ft = html.match(/<footer class="foot">[\s\S]*?<\/footer>/)?.[0];
  if (header === null) { header = h; footer = ft; }
  else { if (h !== header) fail(rel, 'header differs from the other pages: regenerate with tools/pages.py'); if (ft !== footer) fail(rel, 'footer differs from the other pages'); }
}

const sitemap = readFileSync(join(ROOT, 'sitemap.xml'), 'utf8');
for (const [, loc] of sitemap.matchAll(/<loc>https:\/\/maliwize\.co\.za([^<]*)<\/loc>/g)) {
  if (!existsSync(join(ROOT, loc, loc.endsWith('/') ? 'index.html' : ''))) fail('sitemap.xml', `lists a page that does not exist: ${loc}`);
}

if (fails.length) { console.error(`check failed (${fails.length}):\n  ` + fails.join('\n  ')); process.exit(1); }
console.log(`check ok: ${files.length} pages`);
