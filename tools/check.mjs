// The gate: Netlify runs this as the build command, so a page that breaks a rule is never published.
// No dependencies. Run it locally with `node tools/check.mjs`.
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join, relative } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname;
const APP = 'https://app.maliwize.co.za'; // keep in step with APP in tools/pages.py
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
  // Nothing commercial until Franco says it is public (CLAUDE.md): no retailer or partner names,
  // no prices, and no rand figure attached to a saving.
  [/\b(shoprite|checkers|pick n pay|dis-?chem|clicks|woolworths|spar|usave|boxer|makro|berelo|wigroup|wicode)\b/i, 'no retailer or partner names until Franco says they are public'],
  [/\bR\s?\d[\d ]*(?:,\d\d)?\s*(?:pm|p\/m|per month|a month|\/month|once[- ]off|per year|a year)\b/i, 'no prices'],
  [/\bsaves?\b(?: you)?(?: up to)?\s+R\s?\d/i, 'no rand figure for a saving; say that savings depend on what you buy'],
  [/\bR\s?\d[\d ]*(?:,\d\d)?\s*(?:saved|in savings|of savings)\b/i, 'no rand figure for a saving; say that savings depend on what you buy'],
  [/\b(airtime on credit|cashback|cash back)\b/i, 'not offered; do not present it'],
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
  if (/\sstyle="/i.test(html) || /<style\b/i.test(html)) fail(rel, 'no inline styles: the CSP allows only /assets/site.css');
  if (/\son[a-z]+="/i.test(html)) fail(rel, 'no inline event handlers');
  if ((html.match(/<h1\b/g) || []).length !== 1) fail(rel, 'exactly one h1 per page');
  for (const [re, why] of banned) {
    const m = text.match(re);
    if (m && !(re.source.startsWith('financial advice') && /does not give financial advice/.test(text))) fail(rel, `"${m[0]}": ${why}`);
  }
  for (const [, href] of html.matchAll(/href="([^"#]+)/g)) {
    if (href.startsWith('https://maliwize.co.za/') && !href.startsWith(APP + '/auth') && !href.startsWith('https://maliwize.co.za/sitemap')) {
      if (!html.includes('rel="canonical" href="' + href) && !href.includes('og-image')) fail(rel, `absolute link to the site: ${href} (use a path)`);
    }
    if (/^https?:\/\/[^/]*maliwize/.test(href) && href.includes('/auth') && !href.startsWith(APP)) fail(rel, `app link does not use APP (${APP}): ${href}`);
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

// Redirects: the old app paths go on to the app, and no rule may be forced, or it would hide a
// website page (see the header of _redirects).
const redirects = readFileSync(join(ROOT, '_redirects'), 'utf8').split('\n').filter((l) => l.trim() && !l.startsWith('#'));
for (const line of redirects) {
  const [from, to, code] = line.trim().split(/\s+/);
  if (/!$/.test(code || '')) fail('_redirects', `forced rule hides website pages: ${line.trim()}`);
  if (!to.startsWith(APP + '/')) fail('_redirects', `rule does not go to the app (${APP}): ${line.trim()}`);
  if (code !== '301') fail('_redirects', `use a permanent 301: ${line.trim()}`);
  if (['/', '/how-it-works/', '/maliscore/', '/privacy/', '/contact/', '/rewards/'].includes(from)) fail('_redirects', `rule would take over a website page: ${from}`);
}
for (const must of ['/r/*', '/auth/*', '/pay/*', '/login']) if (!redirects.some((l) => l.trim().split(/\s+/)[0] === must)) fail('_redirects', `missing ${must}: links already sent would break`);

if (fails.length) { console.error(`check failed (${fails.length}):\n  ` + fails.join('\n  ')); process.exit(1); }
console.log(`check ok: ${files.length} pages`);
