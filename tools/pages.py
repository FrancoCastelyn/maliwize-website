#!/usr/bin/env python3
"""Writes the site's pages from the content below. Run it after changing copy:

    python3 tools/pages.py

The output is plain HTML that Netlify serves as it is. There is no build step at deploy time,
so what is in the repo is exactly what is live. tools/check.mjs checks the result. The phone
mockups come from tools/phones.py.
"""
from pathlib import Path

from phones import HF_MARK, MW_MARK, mini_budget, mini_coupons, mini_score, screen

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://maliwize.co.za"
# Where the app lives (scoping board Q-11, AC56). Change it here and re-run; check.mjs fails on
# any other value.
APP = "https://app.maliwize.co.za"

NAV = [("/", "Home"), ("/how-it-works/", "How it works"), ("/maliscore/", "Maliscore"),
       ("/rewards/", "Rewards"), ("/privacy/", "Privacy"), ("/contact/", "Contact")]

ICONS = {
    "lock": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="10" width="14" height="10" rx="2.5"/><path d="M8 10V7.5a4 4 0 0 1 8 0V10" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="2.5" width="12" height="19" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="17.5" r="1.1"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5 4.5 5.5v6c0 4.8 3.2 8.4 7.5 10 4.3-1.6 7.5-5.2 7.5-10v-6z" fill="none" stroke="currentColor" stroke-width="2"/><path d="m8.5 12 2.4 2.4 4.6-4.8" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
    "check": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.5"/></svg>',
    "eye": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2.5 12s3.5-6.5 9.5-6.5 9.5 6.5 9.5 6.5-3.5 6.5-9.5 6.5S2.5 12 2.5 12z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="2.8"/></svg>',
    "bin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 7h14M9 7V4.5h6V7M7 7l1 13h8l1-13" fill="none" stroke="currentColor" stroke-width="2"/></svg>',
    "bank": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9.5 12 4l9 5.5H3zM5 10v7M9.7 10v7M14.3 10v7M19 10v7M3 19.5h18" fill="none" stroke="currentColor" stroke-width="2"/><path d="m4 4 16 16" fill="none" stroke="currentColor" stroke-width="2.4"/></svg>',
    "signal": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V14M9 20V9M14 20V5M19 20v-3" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h14m-5-6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2"/></svg>',
}


def page(path, title, description, body, hero, theme="#0E3A52"):
    current = ' aria-current="page"'
    nav = "\n".join(
        f'          <a href="{href}"{current if href == path else ""}>{label}</a>'
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
  <meta name="theme-color" content="{theme}">
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
      <input type="checkbox" id="menu" class="menu-box" aria-label="Open the menu">
      <label for="menu" class="menu-btn" aria-hidden="true"><span></span><span></span><span></span></label>
      <nav class="nav" aria-label="Main">
        <div class="nav-links">
{nav}
        </div>
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
      <div class="foot-brand">
        <a class="brand" href="/"><img src="/assets/icon.svg" alt="" width="34" height="34">Maliwize</a>
        <p>Know where your money goes. Get rewarded for it.</p>
        <p class="legal">Maliwize is a budgeting app. It does not give financial advice, lend money, or hold or move money for anyone. Rewards come from budgeting and saving, never from spending.</p>
        <p class="legal">MALIWIZE (PTY) LTD &middot; registration 2026/703098/07 &middot; Cape Town, South Africa</p>
      </div>
      <div>
        <p class="caption">Maliwize</p>
        <ul>
          <li><a href="/how-it-works/">How it works</a></li>
          <li><a href="/maliscore/">Maliscore</a></li>
          <li><a href="/rewards/">Hey Fill Rewards</a></li>
          <li><a href="{APP}/auth">Member sign in</a></li>
        </ul>
      </div>
      <div>
        <p class="caption">Help</p>
        <ul>
          <li><a href="/privacy/">Privacy</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/contact/#partners">For partners</a></li>
        </ul>
      </div>
    </div>
  </footer>
</body>
</html>
"""


def hero(title_html, lead, actions="", visual="", small=False, status=None, cls=""):
    s = f'<p class="status">{status}</p>' if status else ""
    v = f'\n      <div class="hero-visual">{visual}</div>' if visual else ""
    return f"""  <section class="hero{' small' if small else ''}{' ' + cls if cls else ''}">
    <div class="wrap">
      <div class="hero-copy">
        {s}
        {title_html}
        <p class="lead">{lead}</p>
        {actions}
      </div>{v}
    </div>
  </section>"""


def section(inner, cls="", id_=""):
    i = f' id="{id_}"' if id_ else ""
    return f'    <section class="block{" " + cls if cls else ""}"{i}>\n      <div class="wrap">\n{inner}\n      </div>\n    </section>'


LOOP = f"""        <ol class="loop" aria-label="How the parts connect">
          <li class="reveal"><span class="loop-k">1</span><b>Budget and capture</b><span>Plan against your take-home pay and write down what you spend.</span></li>
          <li class="reveal"><span class="loop-k">2</span><b>Your Maliscore grows</b><span>Kept lines, reached savings and daily check-ins earn points.</span></li>
          <li class="reveal"><span class="loop-k">3</span><b>Coupons open</b><span>Your tier opens rands off selected groceries. Nothing opens because you spend.</span></li>
        </ol>"""


HOME = page(
    "/",
    "Maliwize: know where your money goes, and get rewarded for it",
    "A budget you can keep, a Maliscore that grows with good habits, and grocery coupons that open as it does. A South African budgeting app, built for any phone.",
    section(
        f"""        <p class="label reveal">One app, one loop</p>
        <h2 class="reveal">Good habits move you up. Moving up opens coupons.</h2>
        <p class="lead reveal">Maliwize is a budget you can actually keep, a score that notices when you keep it, and grocery coupons that open as the score grows. Each part feeds the next, and none of it rewards spending.</p>
{LOOP}""",
        "loop-block",
    )
    + section(
        f"""        <p class="label reveal">What Maliwize does</p>
        <h2 class="reveal">Three things, working together</h2>
        <div class="features">
          <article class="feature reveal">
            {mini_budget()}
            <h3>A budget you can keep</h3>
            <p>Plan against your take-home pay, line by line. Capture what you spend in a few taps, cash included, and see what is left before the month runs out. Each line is judged in words, not percentages.</p>
            <a class="more" href="/how-it-works/">How it works {ICONS['arrow']}</a>
          </article>
          <article class="feature reveal">
            {mini_score()}
            <h3>A Maliscore that grows</h3>
            <p>Capturing your spending, keeping a line inside its limit and reaching your savings all earn points. Four tiers, from Starter to Champion. The amount you spend earns nothing, ever.</p>
            <a class="more" href="/maliscore/">About the Maliscore {ICONS['arrow']}</a>
          </article>
          <article class="feature reveal">
            {mini_coupons()}
            <h3>Coupons that open up</h3>
            <p>Hey Fill Rewards gives you rands off selected groceries. Pick the coupons you want and take one code to the till. As your tier climbs, more coupons open. Savings depend on what you buy.</p>
            <a class="more" href="/rewards/">About Hey Fill Rewards {ICONS['arrow']}</a>
          </article>
        </div>""",
    )
    + section(
        f"""        <div class="steps-grid">
          <div class="steps-copy">
            <p class="label reveal">How it works</p>
            <h2 class="reveal">Two minutes to a first budget. A few taps a day after that.</h2>
            <ol class="steps compact">
              <li class="reveal"><h3>Three quick questions</h3><p>Your household and your pay date, and a first budget is filled in from your answers. Adjust anything, then save.</p></li>
              <li class="reveal"><h3>Capture what you spend</h3><p>Amount, place and budget line. Card or cash, a tip, a bill split with friends. No bank login is needed.</p></li>
              <li class="reveal"><h3>Close the month</h3><p>Lines kept inside their limit and reaching your savings add to your Maliscore. Unspent money can carry forward.</p></li>
            </ol>
            <a class="btn teal reveal" href="/how-it-works/">See all five steps</a>
          </div>
          <div class="steps-visual crop reveal">
            {screen("capture", "tilt-l mid")}
          </div>
        </div>""",
        "steps-block",
    )
    + f"""    <section class="band score-band">
      <div class="wrap score-grid">
        <div class="score-visual reveal">
          <div class="bigring-wrap">
            <svg class="bigring p58" viewBox="0 0 60 60" aria-hidden="true"><circle class="track" cx="30" cy="30" r="26"/><circle class="val" cx="30" cy="30" r="26"/></svg>
            <div class="bigring-num"><span class="count n-216" aria-hidden="true"><span class="static">216</span></span><span class="bigring-tier">Builder</span></div>
          </div>
          <p class="bigring-cap">A sample score. 84 points to Achiever.</p>
        </div>
        <div class="score-copy">
          <p class="label reveal">Your Maliscore</p>
          <h2 class="reveal">A score for how you handle money, never for how much you spend.</h2>
          <p class="lead reveal">It goes up when you capture your spending, keep a line inside its limit, reach your savings and check in. It never looks at who you are, and the amount spent earns nothing.</p>
          <ol class="tiers reveal" aria-label="The four tiers">
            <li><b>Starter</b><span>from 0 points</span></li>
            <li><b>Builder</b><span>from 100 points</span></li>
            <li><b>Achiever</b><span>from 300 points</span></li>
            <li><b>Champion</b><span>from 600 points</span></li>
          </ol>
          <a class="btn light reveal" href="/maliscore/">What earns points</a>
        </div>
      </div>
    </section>
    <section class="band hf-band" id="hey-fill">
      <div class="wrap hf-grid">
        <div class="hf-copy">
          <p class="hf-logo reveal"><img src="/assets/heyfill-lockup-white.svg" alt="Hey Fill" width="172" height="54"><span>Rewards, inside Maliwize</span></p>
          <h2 class="hf-head reveal"><span class="blk red">Rands off</span> <span class="blk white">selected groceries.</span><br>Opened by your Maliscore.</h2>
          <p class="lead reveal">Pick the coupons you want in the Rewards tab and take one code to the till. Every tier opens coupons, and more open as your tier climbs. Nothing opens because you spend more.</p>
          <ul class="hf-pills reveal">
            <li>One basket, one code</li>
            <li>More open as you climb</li>
            <li>Off until you switch it on</li>
          </ul>
          <div class="actions reveal">
            <a class="btn white" href="/rewards/">How rewards work</a>
          </div>
          <p class="hf-caveat reveal">Savings depend on what you buy. Grocery coupons only.</p>
        </div>
        <div class="hf-visual reveal">
          <span class="hf-blob" aria-hidden="true"></span>
          {screen("shop", "tilt-r mid")}
        </div>
      </div>
    </section>
"""
    + section(
        f"""        <p class="label reveal">Your money is personal</p>
        <h2 class="reveal">Built to earn your trust, not to assume it</h2>
        <div class="trust">
          <div class="trust-card reveal"><span class="ic">{ICONS['eye']}</span><h3>Consent you can see</h3><p>Each thing you agree to is a separate choice, recorded with the date and the version you saw. Optional ones can be withdrawn in Settings.</p></div>
          <div class="trust-card reveal"><span class="ic">{ICONS['lock']}</span><h3>ID numbers encrypted</h3><p>Where a service needs your ID number, it is stored encrypted and only ever shown to you masked.</p></div>
          <div class="trust-card reveal"><span class="ic">{ICONS['bank']}</span><h3>No bank login</h3><p>You capture what you spend, or import a statement you downloaded yourself. Nothing asks for your banking password.</p></div>
          <div class="trust-card reveal"><span class="ic">{ICONS['bin']}</span><h3>Your data, your call</h3><p>See what we hold, have it corrected, or delete your account and its data. You can also complain to the Information Regulator.</p></div>
        </div>
        <p class="reveal"><a class="more" href="/privacy/">How Maliwize handles your information {ICONS['arrow']}</a></p>""",
        "trust-block",
    )
    + section(
        f"""        <div class="cta reveal">
          <div>
            <p class="status dark">Opening soon</p>
            <h2>Maliwize is nearly here</h2>
            <p class="muted">We are opening the doors soon. If your employer, debt counsellor or another partner has invited you, use the link they sent you. It carries your reference code.</p>
          </div>
          <div class="actions">
            <a class="btn teal" href="{APP}/auth">Member sign in</a>
            <a class="btn outline" href="/contact/#partners">For partners</a>
          </div>
        </div>""",
    ),
    hero(
        '<h1 class="display">Know where your money goes.<br>Get rewarded for it.</h1>',
        "A budget you can keep, a Maliscore that grows with good habits, and grocery coupons that open up as it does. Built for South Africa, for any phone.",
        f"""<div class="actions"><a class="btn primary" href="/how-it-works/">How it works</a><a class="btn ghost" href="{APP}/auth">Member sign in</a></div>
        <ul class="proof" aria-label="In short">
          <li>{ICONS['bank']}No bank login needed</li>
          <li>{ICONS['phone']}Works on any phone</li>
          <li>{ICONS['shield']}Privacy under POPIA</li>
        </ul>""",
        visual=f"""
        <div class="device-stack">
          <div class="device back">{screen("shop", "tilt-r")}</div>
          <div class="device front"><div class="float">{screen("home", "tilt-l hero-phone")}</div></div>
        </div>""",
        status="Opening soon",
        cls="home",
    ),
)

HOW = page(
    "/how-it-works/",
    "How Maliwize works",
    "Set up a budget in about two minutes, capture what you spend, see where you stand, close the month and switch on rewards when you are ready.",
    section(
        f"""        <ol class="walk">
          <li class="walk-step">
            <div class="walk-copy reveal">
              <span class="walk-k">1</span>
              <h2>Three quick questions</h2>
              <p>Your household, your pay date and roughly what comes in. A first budget is filled in from your answers, planned against your take-home pay, with savings as a line of its own. Every answer is an estimate you can change.</p>
            </div>
            <div class="walk-visual crop reveal">{screen("first_budget", "tilt-r")}</div>
          </li>
          <li class="walk-step">
            <div class="walk-copy reveal">
              <span class="walk-k">2</span>
              <h2>Capture what you spend</h2>
              <p>Amount, place and budget line, in a few taps. Card or cash, a tip, a bill split with friends: you capture only your share. Nothing asks for your bank login. If you prefer, import the statement you download from your banking app, as CSV or Excel.</p>
            </div>
            <div class="walk-visual crop reveal">{screen("capture", "tilt-l")}</div>
          </li>
          <li class="walk-step">
            <div class="walk-copy reveal">
              <span class="walk-k">3</span>
              <h2>See where you stand</h2>
              <p>Each line says what is left in plain words, and warns you when an everyday line is heading over before it gets there. Fixed costs such as rent are counted once. Your month can start on your pay day, not the first.</p>
            </div>
            <div class="walk-visual crop reveal">{screen("budget", "tilt-r")}</div>
          </li>
          <li class="walk-step">
            <div class="walk-copy reveal">
              <span class="walk-k">4</span>
              <h2>Close the month</h2>
              <p>At month end you close the budget. Lines kept inside their limit, and reaching your savings, add to your Maliscore. Unspent money can carry forward. Spending less than you planned earns; the amount you spent never does.</p>
            </div>
            <div class="walk-visual crop reveal">{screen("close", "tilt-l")}</div>
          </li>
          <li class="walk-step">
            <div class="walk-copy reveal">
              <span class="walk-k">5</span>
              <h2>Switch on rewards when you are ready</h2>
              <p>Rewards are off until you switch them on in the app, with their own consent that says exactly what is shared. Then your tier opens grocery coupons, and more open as it grows. Switch off any time in Settings.</p>
              <a class="more" href="/rewards/">About Hey Fill Rewards {ICONS['arrow']}</a>
            </div>
            <div class="walk-visual crop reveal">{screen("switch_on", "tilt-r")}</div>
          </li>
        </ol>""",
        "walk-block",
    )
    + section(
        """        <div class="split">
          <div>
            <p class="label reveal">Pay dates that fit</p>
            <h2 class="reveal">Your month can start on your pay day</h2>
            <p class="lead reveal">Choose calendar months, your pay date, or a custom period. If you are paid on the last day of the month, choose that, and Maliwize handles the months that are shorter.</p>
          </div>
          <div class="period-demo reveal" aria-hidden="true">
            <div class="seg big"><span>Calendar</span><span class="on">Financial</span><span>Custom</span></div>
            <p class="period-line">25 Sep to 24 Oct · paid on the 25th</p>
          </div>
        </div>""",
    )
    + section(
        f"""        <div class="cta reveal">
          <div>
            <h2>Invited by a partner?</h2>
            <p class="muted">Use the link your employer, debt counsellor or another partner sent you. It carries your reference code and takes you straight to sign-up.</p>
          </div>
          <div class="actions"><a class="btn teal" href="{APP}/auth">Member sign in</a><a class="btn outline" href="/maliscore/">About the Maliscore</a></div>
        </div>""",
    ),
    hero("<h1>How Maliwize works</h1>", "Five steps, and the first one takes about two minutes.", small=True),
)

MALISCORE = page(
    "/maliscore/",
    "The Maliscore: a score for good money habits",
    "The Maliscore grows when you capture your spending, keep budget lines inside their limit and reach your savings. Four tiers, from Starter to Champion. Never for spending.",
    section(
        f"""        <div class="split">
          <div>
            <p class="label reveal">Four tiers</p>
            <h2 class="reveal">Earned by good habits, one month at a time</h2>
            <p class="lead reveal">Everyone starts as a Starter. Every tier opens coupons in Hey Fill Rewards, and each tier up opens more. Your tier is worked out from your points, and your points come only from what you do in the app.</p>
            <ol class="tiers dark reveal" aria-label="The four tiers">
              <li><b>Starter</b><span>from 0 points</span></li>
              <li><b>Builder</b><span>from 100 points</span></li>
              <li><b>Achiever</b><span>from 300 points</span></li>
              <li><b>Champion</b><span>from 600 points</span></li>
            </ol>
          </div>
          <div class="split-visual crop reveal">{screen("maliscore", "tilt-l")}</div>
        </div>""",
    )
    + section(
        f"""        <p class="label reveal">What earns points</p>
        <h2 class="reveal">Small things, done often</h2>
        <div class="rules">
          <div class="rule-card reveal"><span class="ic">{ICONS['check']}</span><h3>Capturing what you spend</h3><p>Each transaction you write down earns a little, up to a daily limit, so a few taps a day is all it takes.</p></div>
          <div class="rule-card reveal"><span class="ic">{ICONS['shield']}</span><h3>Keeping a line inside its limit</h3><p>Counted when you close the month, for everyday lines such as groceries and transport. Fixed costs such as rent are not a spending choice, so they earn nothing either way.</p></div>
          <div class="rule-card reveal"><span class="ic">{ICONS['signal']}</span><h3>Reaching your savings</h3><p>Putting away what you planned to save earns once a month. Savings is a line of its own, and the only one where reaching the limit is the goal.</p></div>
          <div class="rule-card reveal"><span class="ic">{ICONS['eye']}</span><h3>Checking in and setting up</h3><p>Opening the app each day, setting your first budget and importing a statement each earn too. The exact points for every rule are shown in the app, under What earns points.</p></div>
        </div>
        <div class="promise reveal"><p><b>Never for spending more.</b> The amount you spend earns nothing. Spending less than you planned earns, because you kept the line. Many of our members are working their way out of debt, and nothing in Maliwize nudges anyone to buy more.</p></div>
        <div class="promise reveal"><p><b>Never for who you are.</b> The Maliscore looks at behaviour only: what you capture, what you keep, what you save. It does not look at your age, your gender, where you live or anything about you other than how you handle your money in the app.</p></div>""",
    )
    + section(
        f"""        <div class="cta reveal">
          <div>
            <h2>What your tier opens</h2>
            <p class="muted">Every tier opens grocery coupons in Hey Fill Rewards, and a higher tier opens more of them.</p>
          </div>
          <div class="actions"><a class="btn teal" href="/rewards/">About Hey Fill Rewards</a><a class="btn outline" href="/how-it-works/">How it works</a></div>
        </div>""",
    ),
    hero(
        "<h1>Your Maliscore</h1>",
        "A score for how you handle money, built from what you do in the app. Never for how much you spend, and never for who you are.",
        small=True,
    ),
)

REWARDS = page(
    "/rewards/",
    "Hey Fill Rewards in Maliwize",
    "Rands off selected groceries, opened by your Maliscore. Pick coupons, take one code to the till. Earned by budgeting and saving, never by spending more.",
    f"""    <section class="band hf-band hf-page">
      <div class="wrap">
        <ol class="hf-steps">
          <li class="hf-step reveal">
            <span class="hf-k">1</span>
            <div><h2>Switch it on</h2><p>Rewards are off until you switch them on in the Rewards tab, with a consent of their own that says exactly what is shared. Switch off any time in Settings.</p></div>
            {screen("switch_on", "tilt-r small")}
          </li>
          <li class="hf-step reveal">
            <span class="hf-k">2</span>
            <div><h2>Pick your coupons</h2><p>Rands off selected grocery items, as tiles or a list. Your tier shows which are open. A locked coupon says which tier opens it, and that is all it ever asks of you.</p></div>
            {screen("shop", "tilt-l small")}
          </li>
          <li class="hf-step reveal">
            <span class="hf-k">3</span>
            <div><h2>One code at the till</h2><p>Your basket becomes one code with a barcode. Show it to the cashier and the rands come off before you pay. It works on a slow connection too.</p></div>
            {screen("code", "tilt-r small")}
          </li>
        </ol>
      </div>
    </section>
"""
    + section(
        """        <p class="label reveal">Your tier opens coupons</p>
        <h2 class="reveal">Four tiers, earned by good habits</h2>
        <p class="lead reveal">Every tier opens coupons. Capturing your spending, staying inside your budget lines and reaching your savings move you up. The amount you spend never does.</p>
        <ol class="tiers dark reveal" aria-label="The four tiers">
          <li><b>Starter</b><span>from 0 points</span></li>
          <li><b>Builder</b><span>from 100 points</span></li>
          <li><b>Achiever</b><span>from 300 points</span></li>
          <li><b>Champion</b><span>from 600 points</span></li>
        </ol>
        <div class="promise hfp reveal"><p><b>No spend targets, ever.</b> Coupons open because you budget and save, not because you buy more. A locked coupon never asks you to spend to unlock it.</p></div>""",
    )
    + section(
        f"""        <div class="grid two">
          <div class="card reveal">
            <h3>You decide when it is on</h3>
            <p>Switching on shares your tier, name, mobile number and ID number with the rewards layer, so coupons can be issued to you. Never your transactions, balances or budget. Switch it off any time in Settings.</p>
          </div>
          <div class="card reveal">
            <h3>Two products that recognise each other</h3>
            <p>Hey Fill is its own product, with its own account and its own privacy terms. Inside Maliwize it is the rewards layer: your Maliwize account stays yours, your Hey Fill account stays yours, and your tier is what travels between them.</p>
          </div>
        </div>
        <p class="hf-caveat dark reveal">Savings depend on what you buy. Grocery coupons only. A coupon is rands off a selected item at a participating store, never cash.</p>
        <p class="reveal"><a class="more" href="/privacy/">What is shared, in full {ICONS['arrow']}</a></p>""",
    ),
    hero(
        '<p class="hf-logo"><img src="/assets/heyfill-lockup-white.svg" alt="Hey Fill" width="172" height="54"><span>Rewards, inside Maliwize</span></p>\n        <h1 class="hf-head"><span class="blk red">Rands off</span> <span class="blk white">selected groceries.</span><br>Opened by your Maliscore.</h1>',
        "Pick coupons, take one code to the till. Earned by budgeting and saving, never by spending more.",
        '<ul class="hf-pills"><li>One basket, one code</li><li>More open as you climb</li><li>Off until you switch it on</li></ul>',
        small=True,
        cls="hf-hero",
    ),
    theme="#0076CA",
)

PRIVACY = page(
    "/privacy/",
    "Privacy at Maliwize",
    "How Maliwize handles your personal information under POPIA: what we collect, why, who it is shared with, and your rights.",
    section(
        """        <div class="prose">
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
        <h2>No bank login</h2>
        <p>Maliwize does not ask for your banking password. You capture what you spend, or import a statement you downloaded yourself.</p>
        <h2>Your rights</h2>
        <p>You can ask to see the information we hold about you, have it corrected, or have your account and data deleted. You can also complain to the Information Regulator.</p>
        <h2>Contact our Information Officer</h2>
        <p>Email <a href="mailto:privacy@maliwize.co.za">privacy@maliwize.co.za</a>.</p>
        </div>""",
    ),
    hero("<h1>Privacy at Maliwize</h1>", "Your money is personal. Here is how we look after the information that goes with it.", small=True),
)

CONTACT = page(
    "/contact/",
    "Contact Maliwize",
    "How to reach Maliwize about your account, privacy, or a partnership for your staff or clients.",
    section(
        f"""        <div class="grid">
          <div class="card reveal">
            <h3>Joining through a partner</h3>
            <p>If your employer, debt counsellor or another partner invited you, the fastest way in is the link they sent you. It carries your reference code.</p>
          </div>
          <div class="card reveal">
            <h3>Privacy and your data</h3>
            <p>To see, correct or delete your information, email <a href="mailto:privacy@maliwize.co.za">privacy@maliwize.co.za</a>.</p>
          </div>
          <div class="card reveal">
            <h3>Members</h3>
            <p>Help with your account is inside the app, under Me. <a href="{APP}/auth">Sign in</a>.</p>
          </div>
        </div>""",
    )
    + section(
        """        <p class="label reveal">For partners</p>
        <h2 class="reveal">Maliwize for your staff or your clients</h2>
        <p class="lead reveal">Employers, debt counsellors and other organisations bring members to Maliwize with an invitation that carries a reference code, so a member's first budget is not a blank page. If that sounds like your organisation, we would like to hear from you.</p>
        <p class="reveal"><a class="btn teal" href="mailto:hello@maliwize.co.za">Email hello@maliwize.co.za</a></p>""",
        id_="partners",
    ),
    hero("<h1>Contact us</h1>", "We read every message.", small=True),
)

NOT_FOUND = page(
    "/404.html",
    "Page not found | Maliwize",
    "This page does not exist on the Maliwize website. Go to the home page, or sign in to the app.",
    section(
        f"""        <p>The page you asked for is not here. <a href="/">Go to the home page</a>, or <a href="{APP}/auth">sign in to the app</a>.</p>""",
    ),
    hero("<h1>Page not found</h1>", "It may have moved, or the link may be old.", small=True),
)

OUT = {
    "index.html": HOME,
    "how-it-works/index.html": HOW,
    "maliscore/index.html": MALISCORE,
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
