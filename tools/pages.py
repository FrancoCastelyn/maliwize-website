#!/usr/bin/env python3
"""Writes the site's pages from the content below. Run it after changing copy:

    python3 tools/pages.py

The output is plain HTML that Netlify serves as it is. There is no build step at deploy time,
so what is in the repo is exactly what is live. tools/check.mjs checks the result.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://maliwize.co.za"
# Where the app lives. It moves to app.maliwize.co.za when the site takes the main address
# (scoping board Q-11, AC56). Change it here and re-run; check.mjs fails on any other value.
APP = "https://app.maliwize.co.za"

NAV = [("/", "Home"), ("/how-it-works/", "How it works"), ("/rewards/", "Rewards"),
       ("/privacy/", "Privacy"), ("/contact/", "Contact")]


def page(path, title, description, body, hero):
    current = ' aria-current="page"'
    nav = "\n".join(
        f'        <a href="{href}"{current if href == path else ""}>{label}</a>'
        for href, label in NAV
    )
    canonical = SITE + path
    return f"""<!doctype html>
<html lang="en-ZA">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <meta name="theme-color" content="#0E3A52">
  <link rel="icon" type="image/svg+xml" href="/assets/icon.svg">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Maliwize">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{SITE}/assets/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap">
  <link rel="stylesheet" href="/assets/site.css">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  <header class="top">
    <div class="wrap">
      <a class="brand" href="/"><img src="/assets/icon.svg" alt="" width="34" height="34">Maliwize</a>
      <nav class="nav" aria-label="Main">
{nav}
        <a class="signin" href="{APP}/auth">Sign in</a>
      </nav>
    </div>
  </header>
{hero}
  <main id="main">
{body}
  </main>
  <footer class="foot">
    <div class="wrap">
      <div>
        <a class="brand" href="/"><img src="/assets/icon.svg" alt="" width="34" height="34">Maliwize</a>
        <p>Know where your money goes. Get rewarded for it.</p>
        <p class="legal">Maliwize is a budgeting app. It does not give financial advice, lend money, or hold or move money for anyone.<br>MALIWIZE (PTY) LTD &middot; registration 2026/703098/07</p>
      </div>
      <div>
        <p class="caption">Maliwize</p>
        <ul>
          <li><a href="/how-it-works/">How it works</a></li>
          <li><a href="/rewards/">Rewards</a></li>
          <li><a href="{APP}/auth">Sign in</a></li>
        </ul>
      </div>
      <div>
        <p class="caption">Help</p>
        <ul>
          <li><a href="/privacy/">Privacy</a></li>
          <li><a href="/contact/">Contact</a></li>
        </ul>
      </div>
    </div>
  </footer>
</body>
</html>
"""


def hero(title_html, lead, actions="", mark=False, small=False, status=None):
    s = f'<p class="status">{status}</p>' if status else ""
    m = ('      <svg class="mark" viewBox="0 0 140 110" aria-hidden="true"><path d="M10 98 L32 22 L54 74 L76 16 L95 60 L115.85 27.83" '
         'fill="none" stroke="#fff" stroke-width="13" stroke-linejoin="miter"/><path d="M130 6 L128.45 35.99 L103.25 19.67 Z" fill="#fff"/></svg>\n') if mark else ""
    return f"""  <section class="hero{' small' if small else ''}">
    <div class="wrap">
      <div>
        {s}
        {title_html}
        <p class="lead">{lead}</p>
        {actions}
      </div>
{m}    </div>
  </section>"""


HOME = page(
    "/",
    "Maliwize: know where your money goes, and get rewarded for it",
    "A budget that fills itself in, a Maliscore that grows with good habits, and grocery coupons that open up as it does. A South African budgeting app.",
    """    <section class="block">
      <div class="wrap">
        <p class="label">What Maliwize does</p>
        <h2>Three things, working together</h2>
        <div class="grid">
          <div class="card">
            <div class="icon">R</div>
            <h3>A budget you can keep</h3>
            <p>Plan against your take-home pay, line by line. Capture what you spend in a few taps, including cash and split bills, and see what is left before the month runs out.</p>
          </div>
          <div class="card">
            <div class="icon">&#9650;</div>
            <h3>A Maliscore that grows</h3>
            <p>Your Maliscore goes up when you capture your spending and stay inside your budget. It rewards good habits, never spending.</p>
          </div>
          <div class="card">
            <div class="icon">%</div>
            <h3>Coupons that open up</h3>
            <p>Hey Fill Rewards gives you rands off selected groceries. As your Maliscore grows, more coupons open. Savings depend on what you buy.</p>
          </div>
        </div>
        <div class="promise"><p><b>Rewards come from saving and sticking to your budget, never from spending.</b> Many of our members are working their way out of debt. Nothing in Maliwize rewards spending, and there are no spend targets.</p></div>
      </div>
    </section>
    <section class="block">
      <div class="wrap">
        <div class="cta">
          <div>
            <h2>Maliwize is nearly here</h2>
            <p class="muted" style="margin:6px 0 0">We are opening the doors soon. If your employer, debt counsellor or another partner has invited you, use the link they sent you.</p>
          </div>
          <a class="btn teal" href="/how-it-works/">See how it works</a>
        </div>
      </div>
    </section>""",
    hero('<h1 class="display">Know where your money goes.<br>Get rewarded for it.</h1>',
         "A budget that fills itself in, a Maliscore that grows with good habits, and grocery coupons that open up as it does.",
         f'<div class="actions"><a class="btn primary" href="/how-it-works/">How it works</a><a class="btn ghost" href="{APP}/auth">Member sign in</a></div>',
         mark=True, status="Opening soon"),
)

HOW = page(
    "/how-it-works/",
    "How Maliwize works",
    "Set up a budget in about two minutes, capture what you spend, and watch your Maliscore and your rewards grow with good habits.",
    """    <section class="block">
      <div class="wrap">
        <ol class="steps">
          <li><h3>Sign up and set your budget</h3><p>A few questions about your household and your pay date, then a first budget planned against your take-home pay. Money with no line gets a nudge to find one, and savings is a line of its own.</p></li>
          <li><h3>Capture what you spend</h3><p>Amount, place and budget line, in a few taps. Card or cash, a tip, a bill split with friends: you capture only your share. Nothing needs access to your bank account; bank linking may come later, as a separate choice you make.</p></li>
          <li><h3>See where you stand</h3><p>Your budget shows what is left to spend in each line, excluding savings, and warns you when an everyday line is heading over before it gets there.</p></li>
          <li><h3>Close the month</h3><p>At month end you close the budget. Lines kept inside their limit, and reaching your savings, add to your Maliscore. Unspent money can carry forward.</p></li>
          <li><h3>Switch on rewards when you are ready</h3><p>Rewards are off until you switch them on in the app. Then your Maliscore tier opens grocery coupons, and more open as it grows.</p></li>
        </ol>
      </div>
    </section>
    <section class="block">
      <div class="wrap">
        <p class="label">Pay dates that fit</p>
        <h2>Your month can start on your pay day</h2>
        <p class="lead">Choose calendar months, your pay date, or a custom period. If you are paid on the last day of the month, choose that, and Maliwize handles the months that are shorter.</p>
      </div>
    </section>""",
    hero("<h1>How Maliwize works</h1>", "Five steps, and the first one takes about two minutes.", small=True),
)

REWARDS = page(
    "/rewards/",
    "Hey Fill Rewards in Maliwize",
    "Rands off selected groceries, opened by your Maliscore. Earned by budgeting and saving, never by spending more.",
    """    <section class="block">
      <div class="wrap">
        <p class="label">Your Maliscore tier</p>
        <h2>Four tiers, earned by good habits</h2>
        <p class="lead">Every tier opens coupons. Capturing your spending, staying inside your budget lines and reaching your savings move you up.</p>
        <div class="tiers">
          <div class="tier"><b>Starter</b><span>from 0 points</span></div>
          <div class="tier"><b>Builder</b><span>from 100 points</span></div>
          <div class="tier"><b>Achiever</b><span>from 300 points</span></div>
          <div class="tier"><b>Champion</b><span>from 600 points</span></div>
        </div>
      </div>
    </section>
    <section class="block">
      <div class="wrap">
        <div class="grid two">
          <div class="card">
            <h3>One basket, one code</h3>
            <p>Pick the coupons you want, and take them to the till as one code. Coupons are for rands off selected items; your savings depend on what you buy.</p>
          </div>
          <div class="card">
            <h3>You decide when it is on</h3>
            <p>Switching on shares your tier, name, mobile number and ID number with the rewards layer, so coupons can be issued to you. Never your transactions, balances or budget. Switch it off any time in Settings.</p>
          </div>
        </div>
        <div class="promise"><p><b>No spend targets, ever.</b> Rewards open up because you budget and save, not because you buy more.</p></div>
      </div>
    </section>""",
    hero("<h1>Hey Fill Rewards, inside Maliwize</h1>", "Rands off selected groceries, opened by your Maliscore.", small=True),
)

PRIVACY = page(
    "/privacy/",
    "Privacy at Maliwize",
    "How Maliwize handles your personal information under POPIA: what we collect, why, who it is shared with, and your rights.",
    """    <section class="block">
      <div class="wrap prose">
        <p class="note"><b>Summary, not the policy.</b> This page explains how Maliwize treats your information in plain words. The full privacy policy you agree to is shown in the app when you sign up, and it is the one that applies.</p>
        <h2>What we collect, and why</h2>
        <ul>
          <li><b>Your account details:</b> name, email, mobile number, to run your account and reach you.</li>
          <li><b>Your budget and what you capture:</b> to show you your budget and work out your Maliscore.</li>
          <li><b>Your South African ID number</b>, only where a service needs it. It is stored encrypted and only ever shown to you masked.</li>
        </ul>
        <h2>Consent you can see</h2>
        <p>Each thing you agree to is a separate choice, recorded with the date and the version you saw: the terms, the privacy policy, rewards, and marketing messages. Optional ones can be withdrawn in Settings.</p>
        <h2>What is shared</h2>
        <p>If you switch on rewards, your tier, name, mobile number and ID number go to the rewards layer so coupons can be issued to you. Never your transactions, balances or budget. Nothing is sold, and nothing is used to target you by who you are.</p>
        <h2>Your rights</h2>
        <p>You can ask to see the information we hold about you, have it corrected, or have your account and data deleted. You can also complain to the Information Regulator.</p>
        <h2>Contact our Information Officer</h2>
        <p>Email <a href="mailto:privacy@maliwize.co.za">privacy@maliwize.co.za</a>.</p>
      </div>
    </section>""",
    hero("<h1>Privacy at Maliwize</h1>", "Your money is personal. Here is how we look after the information that goes with it.", small=True),
)

CONTACT = page(
    "/contact/",
    "Contact Maliwize",
    "How to reach Maliwize about your account, privacy, or a partnership.",
    """    <section class="block">
      <div class="wrap">
        <div class="grid">
          <div class="card">
            <h3>Joining through a partner</h3>
            <p>If your employer, debt counsellor or another partner invited you, the fastest way in is the link they sent you. It carries your reference code.</p>
          </div>
          <div class="card">
            <h3>Privacy and your data</h3>
            <p>To see, correct or delete your information, email <a href="mailto:privacy@maliwize.co.za">privacy@maliwize.co.za</a>.</p>
          </div>
          <div class="card">
            <h3>Members</h3>
            <p>Help with your account is inside the app, under Me. <a href="APPURL/auth">Sign in</a>.</p>
          </div>
        </div>
      </div>
    </section>""".replace("APPURL", APP),
    hero("<h1>Contact us</h1>", "We read every message.", small=True),
)

NOT_FOUND = page(
    "/404.html",
    "Page not found | Maliwize",
    "This page does not exist on the Maliwize website. Go to the home page, or sign in to the app.",
    """    <section class="block">
      <div class="wrap">
        <p>The page you asked for is not here. <a href="/">Go to the home page</a>, or <a href="APPURL/auth">sign in to the app</a>.</p>
      </div>
    </section>""".replace("APPURL", APP),
    hero("<h1>Page not found</h1>", "It may have moved, or the link may be old.", small=True),
)

OUT = {
    "index.html": HOME,
    "how-it-works/index.html": HOW,
    "rewards/index.html": REWARDS,
    "privacy/index.html": PRIVACY,
    "contact/index.html": CONTACT,
    "404.html": NOT_FOUND.replace('<link rel="canonical" href="https://maliwize.co.za/404.html">\n  ', '').replace('<head>', '<head>\n  <meta name="robots" content="noindex">', 1),
}

for rel, html in OUT.items():
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")

(ROOT / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE}{href}</loc></url>\n" for href, _ in NAV)
    + "</urlset>\n", encoding="utf-8")
print("wrote", len(OUT), "pages and sitemap.xml")
