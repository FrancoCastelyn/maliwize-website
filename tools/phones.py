"""The app's screens, drawn in HTML and CSS so the site can show the product without screenshots
(which go stale the week after they are taken) and without JavaScript.

Every size inside a screen is in em. `.phone` sets its font-size from `--s`, so one variable scales
a whole phone, frame and all. The screens are decorative: each phone is `role="img"` with a label
that says what it shows, and the drawn content is hidden from assistive technology.

Values are illustrative sample data in the app's own words (src/i18n/en.ts in Powerstack). They
never state a saving in rands, a price, a retailer or a points rule the scorer does not publish.
Progress bars take a `p05` to `p100` class and counters an `n-…` class, because the site's Content
Security Policy allows no inline styles. Both sets of classes live in assets/site.css.
"""

HF_MARK = (
    '<svg viewBox="41.76 22.59 683.12 620.38" aria-hidden="true" focusable="false">'
    '<path fill="#0076CA" d="M188.85 360.84v84.39c0 40.62-32.94 73.54-73.54 73.54-20.31 0-38.69-8.23-52.01-21.54-13.31-13.31-21.54-31.69-21.54-52.01V287.3c0 40.61 32.92 73.54 73.54 73.54h73.55z"/>'
    '<path fill="#D70027" d="M724.88 96.13c0 20.31-8.23 38.69-21.54 52.01-13.31 13.31-31.69 21.54-52.01 21.54H390.91c-40.62 0-73.54-32.94-73.54-73.54 0-20.31 8.23-38.69 21.54-52.01 13.31-13.31 31.69-21.54 52.01-21.54h260.42c40.62 0 73.54 32.92 73.54 73.54z"/>'
    '<path fill="#00A2E7" d="M471.7 287.3v282.13c0 40.61-32.92 73.54-73.54 73.54-20.31 0-38.69-8.23-52.01-21.54-13.31-13.31-21.54-31.69-21.54-52.01V360.84H115.3c-40.62 0-73.54-32.94-73.54-73.54V96.13c0-40.62 32.92-73.54 73.54-73.54 20.31 0 38.69 8.23 52.01 21.54s21.54 31.69 21.54 52.01v117.62h209.31c20.31 0 38.69 8.23 52.01 21.54 13.31 13.31 21.54 31.69 21.54 52z"/>'
    '<path fill="#FD8514" d="M619.92 287.3c0 20.29-8.23 38.69-21.54 52.01-13.31 13.29-31.69 21.54-52.01 21.54H471.7V287.3c0-20.31-8.23-38.69-21.54-52.01-13.31-13.31-31.69-21.54-52.01-21.54h148.22c40.63 0 73.55 32.92 73.55 73.55z"/>'
    '</svg>'
)

MW_MARK = (
    '<svg viewBox="0 0 140 110" aria-hidden="true" focusable="false">'
    '<path d="M10 98 L32 22 L54 74 L76 16 L95 60 L115.85 27.83" fill="none" stroke="currentColor" stroke-width="13" stroke-linejoin="miter"/>'
    '<path d="M130 6 L128.45 35.99 L103.25 19.67 Z" fill="currentColor"/></svg>'
)

STATUS_ICONS = (
    '<svg viewBox="0 0 46 12" aria-hidden="true"><rect x="0" y="7" width="3" height="5" rx="1"/>'
    '<rect x="4.5" y="5" width="3" height="7" rx="1"/><rect x="9" y="3" width="3" height="9" rx="1"/>'
    '<rect x="13.5" y="1" width="3" height="11" rx="1"/>'
    '<path d="M21 5.2a7 7 0 0 1 9 0l-1.3 1.6a5 5 0 0 0-6.4 0z"/><path d="M23.3 8a3.6 3.6 0 0 1 4.4 0L25.5 10.6z"/>'
    '<rect x="33" y="1.5" width="10" height="9" rx="2" fill="none" stroke="currentColor" stroke-width="1.2"/>'
    '<rect x="34.5" y="3" width="6.5" height="6" rx="1"/><rect x="43.6" y="4.5" width="1.6" height="3" rx=".5"/></svg>'
)

TAB_ICONS = {
    "home": '<svg viewBox="0 0 24 24"><path d="M4 11.5 12 5l8 6.5V19a1 1 0 0 1-1 1h-4.5v-5h-5v5H5a1 1 0 0 1-1-1z"/></svg>',
    "budget": '<svg viewBox="0 0 24 24"><path d="M5 5h14v3H5zm0 5.5h14v3H5zm0 5.5h9v3H5z"/></svg>',
    "activity": '<svg viewBox="0 0 24 24"><path d="M4 16.5h11.2l-2.6 2.6 1.4 1.4 5-5-5-5-1.4 1.4 2.6 2.6H4zm16-9H8.8l2.6-2.6L10 3.5l-5 5 5 5 1.4-1.4L8.8 9.5H20z"/></svg>',
    "rewards": '<svg viewBox="0 0 24 24"><path d="M3.5 4.5h7.6l9.4 9.4-7.6 7.6-9.4-9.4zm4 2.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3z"/></svg>',
    "me": '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 20a8 8 0 0 1 16 0z"/></svg>',
}

TABS = [("home", "Home"), ("budget", "Budget"), ("activity", "Activity"), ("rewards", "Rewards"), ("me", "Me")]


def tabbar(active):
    items = "".join(
        f'<span class="{"on" if key == active else ""}">{TAB_ICONS[key]}{label}</span>' for key, label in TABS
    )
    return f'<div class="tb">{items}</div>'


def status():
    return f'<div class="sb"><span>9:41</span>{STATUS_ICONS}</div>'


def ring(p, cls="ring"):
    """A progress ring. `p` is a pNN class (share of the way to the next tier)."""
    return (
        f'<svg class="{cls} {p}" viewBox="0 0 60 60" aria-hidden="true">'
        '<circle class="track" cx="30" cy="30" r="26"/><circle class="val" cx="30" cy="30" r="26"/></svg>'
    )


def bar(p, tone=""):
    return f'<div class="bar"><i class="{p} {tone}"></i></div>'


def line(name, words, p, tone="", savings=False):
    return (
        f'<div class="ln"><div class="ln-h"><span>{"🐖 " if savings else ""}{name}</span>'
        f'<span class="{tone or ("green" if savings else "")}">{words}</span></div>{bar(p, tone)}</div>'
    )


def phone(screen, label, cls=""):
    return (
        f'<div class="phone {cls}" role="img" aria-label="{label}">'
        f'<div class="screen" aria-hidden="true"><div class="island"></div>{status()}{screen}</div></div>'
    )


# ---- the screens -------------------------------------------------------------------------------

def home():
    return (
        '<div class="app">'
        '<header class="ah"><span class="av">TN</span><div><small>Good morning</small><b>Thabo</b></div>'
        '<span class="bell"><svg viewBox="0 0 24 24"><path d="M12 3a5 5 0 0 0-5 5v3.5L5 15v1h14v-1l-2-3.5V8a5 5 0 0 0-5-5zm-2 15a2 2 0 0 0 4 0z"/></svg><i></i></span></header>'
        '<div class="hc"><small>Left in your budget this month</small>'
        '<div class="amt count n-3420"><span class="static">R 3 420</span></div>'
        '<small>excluding savings · from what you have captured</small>'
        '<div class="hc-stats"><span>Budget<b>R 9 800</b></span><span>Captured<b>R 6 380</b></span></div></div>'
        '<div class="tiles"><div class="tile"><small>Add a transaction</small><b>＋ Capture</b><span>14 this month</span></div>'
        '<div class="tile"><small>Import a statement</small><b>⇪ Upload</b><span>CSV or Excel</span></div></div>'
        f'<div class="card rr">{ring("p58")}<div><b>Your Maliscore</b><small>Builder · 84 pts to Achiever</small>{bar("p58")}</div><span class="chev">›</span></div>'
        f'<div class="hfdoor"><span class="hfm">{HF_MARK}</span><span><b>Switch on Hey Fill Rewards</b><small>Rands off selected groceries</small></span><span class="chev">›</span></div>'
        '<div class="card"><div class="ch"><b>Your budget</b><span>See budget</span></div>'
        + line("Groceries", "R 640 left", "p72")
        + line("Transport", "R 210 left", "p80", "near")
        + line("Savings", "Reached", "p100", savings=True)
        + "</div></div>" + tabbar("home")
    )


def budget():
    return (
        '<div class="app">'
        '<header class="ah2"><b>Budget</b><span class="link">Edit</span></header>'
        '<div class="pb"><div class="seg"><span class="on">Calendar</span><span>Financial</span><span>Custom</span></div><small>September · day 19 of 30</small></div>'
        '<div class="hc"><small>September · day 19 of 30</small><div class="amt">R 3 420</div>'
        '<small>left to spend in your budget lines, excluding savings</small>'
        '<div class="hc-stats"><span>Take-home<b>R 9 800</b></span><span>Planned<b>R 9 300</b></span><span>Left to plan<b>R 500</b></span></div></div>'
        '<div class="card"><div class="ch"><b>Your lines</b></div>'
        + line("Rent", "R 4 500 of R 4 500", "p100", "fixed")
        + line("Groceries", "R 640 left", "p72")
        + line("Transport", "R 210 left", "p80", "near")
        + line("Electricity", "Over by R 20", "p100", "over")
        + line("Airtime and data", "R 70 left", "p70")
        + line("Savings", "Reached", "p100", savings=True)
        + "</div></div>" + tabbar("budget")
    )


def capture():
    return (
        '<div class="app">'
        '<header class="ah2"><span class="back">‹</span><b>Capture</b></header>'
        '<div class="amtin"><small>Amount</small><div class="big">R 86<span>,50</span></div></div>'
        '<div class="field"><small>Where</small><b>Spaza shop</b></div>'
        '<div class="field"><small>Budget line</small><div class="chips"><span class="on">Groceries</span><span>Transport</span><span>Airtime and data</span></div></div>'
        '<div class="seg"><span class="on">Cash</span><span>Card</span></div>'
        '<div class="field split"><span>Split the bill<small>Capture only your share</small></span><span class="tog on"><i></i></span></div>'
        '<div class="field split"><span>Tip<small>Added on top</small></span><b>10%</b></div>'
        '<div class="btn">Save</div>'
        '<div class="card"><div class="ch"><b>Recent</b><span>All</span></div>'
        '<div class="crow"><span>Taxi to work<small>Transport · today</small></span><b class="clay">−R 32</b></div>'
        '<div class="crow"><span>Airtime<small>Airtime and data · yesterday</small></span><b class="clay">−R 55</b></div></div>'
        '</div>' + tabbar("activity")
    )


def maliscore():
    return (
        '<div class="app">'
        '<header class="ah2"><span class="back">‹</span><b>Your Maliscore</b></header>'
        f'<div class="score">{ring("p58", "bigring")}<div class="big count n-216"><span class="static">216</span></div>'
        f'<span class="pill">Builder</span>{bar("p58")}<small>84 points to Achiever</small></div>'
        '<div class="card"><div class="ch"><b>What earns points</b></div>'
        '<div class="rule"><span class="ic">✓</span><span>Capturing what you spend<small>A little each day</small></span></div>'
        '<div class="rule"><span class="ic">◎</span><span>Keeping a line inside its limit<small>Counted when you close the month</small></span></div>'
        '<div class="rule"><span class="ic">▲</span><span>Reaching your savings line<small>Once a month</small></span></div>'
        '<div class="rule"><span class="ic">☀</span><span>Checking in<small>Once a day</small></span></div>'
        '<small class="foot">Never for spending more. The amount spent earns nothing.</small></div>'
        '<div class="card"><div class="ch"><b>Recent points</b></div>'
        '<div class="crow"><span>Kept Groceries inside its limit<small>30 Sep</small></span><b class="green">+</b></div>'
        '<div class="crow"><span>Reached Savings<small>30 Sep</small></span><b class="green">+</b></div>'
        '<div class="crow"><span>Captured a transaction<small>Today</small></span><b class="green">+</b></div></div>'
        '</div>' + tabbar("home")
    )


def shop():
    def tile(pic, off, name, cat, state):
        action = {
            "added": '<div class="add on">✓ Added</div>',
            "add": '<div class="add">Add</div>',
            "locked": '<div class="add off">Locked</div>',
        }[state]
        return (
            f'<div class="ctile {"locked" if state == "locked" else ""}"><div class="pic">{pic}</div><span class="off">{off}</span>'
            f'<b>{name}</b><small>{cat}</small>{action}</div>'
        )

    return (
        '<div class="app hf">'
        f'<header class="hfh"><span class="hfm sm">{HF_MARK}</span><b>Hey Fill Rewards</b></header>'
        '<small class="sub">Builder tier · 9 of 14 coupons open</small>'
        '<div class="chips"><span class="on">All</span><span>Rands off</span><span>Groceries</span><span>Baby</span><span>Home</span></div>'
        '<div class="grid2">'
        + tile("🥛", "R15 off", "Long-life milk, 6 pack", "Groceries", "added")
        + tile("🧴", "R20 off", "Washing powder, 2 kg", "Home", "add")
        + tile("🍞", "R10 off", "Brown bread, 700 g", "Groceries", "added")
        + tile("🧷", "R30 off", "Nappies, jumbo pack", "Reach Achiever in Maliwize to unlock", "locked")
        + '</div></div>'
        '<div class="basket"><span>2 coupons picked</span><span>Get one code ›</span></div>' + tabbar("rewards")
    )


def code():
    return (
        '<div class="app hf">'
        '<header class="ah2"><span class="back">‹</span><b>Your code</b></header>'
        '<div class="codecard"><small>One code for 3 coupons</small><div class="barcode"></div>'
        '<div class="digits">9021 4483 7726</div><div class="ok">● Active · expires in 23:58</div>'
        '<small>Show this at the till. Works even on a slow connection.</small></div>'
        '<div class="card"><div class="ch"><b>In this code</b></div>'
        '<div class="crow"><span class="off">R15 off</span><span>Long-life milk, 6 pack</span></div>'
        '<div class="crow"><span class="off">R10 off</span><span>Brown bread, 700 g</span></div>'
        '<div class="crow"><span class="off">R20 off</span><span>Washing powder, 2 kg</span></div></div>'
        '<small class="foot">Savings depend on what you buy. Grocery coupons only.</small>'
        '</div>' + tabbar("rewards")
    )


def switch_on():
    return (
        '<div class="app hf">'
        '<header class="ah2"><span class="back">‹</span><b>Hey Fill Rewards</b></header>'
        f'<div class="hfhero"><span class="hfm">{HF_MARK}</span><b>Switch on Hey Fill Rewards</b><small>Rands off selected groceries, opened by your Maliscore.</small></div>'
        '<div class="card"><div class="ch"><b>What is shared</b></div>'
        '<div class="rule"><span class="ic">✓</span><span>Your tier</span></div>'
        '<div class="rule"><span class="ic">✓</span><span>Your name and mobile number</span></div>'
        '<div class="rule"><span class="ic">✓</span><span>Your ID number, so coupons can be issued to you</span></div>'
        '<div class="rule"><span class="ic no">✕</span><span>Never your transactions, balances or budget</span></div></div>'
        '<div class="card consent"><span class="box">✓</span><span>I have read the Hey Fill Rewards terms and I agree</span></div>'
        '<div class="btn hfb">Switch on</div><small class="foot center">Switch off any time in Settings</small>'
        '</div>' + tabbar("rewards")
    )


def close_month():
    def row(name, state):
        badge = {"kept": '<span class="badge ok">Kept</span>', "over": '<span class="badge over">Over</span>',
                 "reached": '<span class="badge ok">Reached</span>', "fixed": '<span class="badge">Fixed cost</span>'}[state]
        return f'<div class="crow"><span>{name}</span>{badge}</div>'

    return (
        '<div class="app">'
        '<header class="ah2"><span class="back">‹</span><b>Close September</b></header>'
        '<div class="hc"><small>September</small><div class="amt">4 of 5 lines kept</div>'
        '<small>R 410 unspent can carry forward to October</small></div>'
        '<div class="card"><div class="ch"><b>How the month went</b></div>'
        + row("Rent", "fixed") + row("Groceries", "kept") + row("Transport", "kept") + row("Electricity", "over")
        + row("Airtime and data", "kept") + row("Savings", "reached")
        + '<small class="foot">Lines kept inside their limit and reaching Savings add to your Maliscore. Spending less than you planned earns; the amount you spent never does.</small></div>'
        '<div class="btn">Close the month</div>'
        '</div>' + tabbar("budget")
    )


def first_budget():
    def row(name, amount, savings=False):
        return f'<div class="crow"><span>{"🐖 " if savings else ""}{name}</span><b>{amount}</b></div>'

    return (
        '<div class="app">'
        '<header class="ah2"><span class="back">‹</span><b>Your first budget</b></header>'
        '<small class="sub">Filled in from your answers. Adjust anything, then save.</small>'
        '<div class="hc"><small>Take-home pay this month</small><div class="amt">R 9 800</div>'
        '<div class="hc-stats"><span>Planned<b>R 9 300</b></span><span>Left to plan<b>R 500</b></span></div></div>'
        '<div class="card"><div class="ch"><b>Planned</b></div>'
        + row("Rent", "R 4 500") + row("Groceries", "R 3 000") + row("Transport", "R 1 000") + row("Electricity", "R 600")
        + row("Airtime and data", "R 250") + row("Savings", "R 500", savings=True)
        + '</div><div class="btn">Save my budget</div>'
        '<small class="foot center">Money with no line gets a nudge to find one. Savings is a line of its own.</small>'
        '</div>'
    )


# ---- fragments for feature cards (no frame) ----------------------------------------------------

def mini_budget():
    return (
        '<div class="mini" aria-hidden="true"><div class="ch"><b>Your lines</b><span>September</span></div>'
        + line("Groceries", "R 640 left", "p72") + line("Transport", "R 210 left", "p80", "near")
        + line("Electricity", "Over by R 20", "p100", "over") + line("Savings", "Reached", "p100", savings=True)
        + "</div>"
    )


def mini_score():
    return (
        f'<div class="mini rr" aria-hidden="true">{ring("p58")}<div><b>Your Maliscore</b><small>Builder · 84 pts to Achiever</small>{bar("p58")}</div></div>'
    )


def mini_coupons():
    return (
        '<div class="mini hf" aria-hidden="true"><div class="grid2">'
        '<div class="ctile"><div class="pic">🥛</div><span class="off">R15 off</span><b>Long-life milk, 6 pack</b><div class="add on">✓ Added</div></div>'
        '<div class="ctile locked"><div class="pic">🧷</div><span class="off">R30 off</span><b>Nappies, jumbo pack</b><small>Reach Achiever to unlock</small></div>'
        '</div></div>'
    )


SCREENS = {
    "home": (home, "The Maliwize home screen: what is left in the budget this month, a Maliscore ring, and the Hey Fill Rewards doorway"),
    "budget": (budget, "The Budget screen: take-home pay, planned lines, and each line's progress in words"),
    "capture": (capture, "The Capture screen: an amount, where it was spent, the budget line, cash or card, and a bill split"),
    "maliscore": (maliscore, "The Maliscore screen: the score, the tier, the way to the next tier, and what earns points"),
    "shop": (shop, "Hey Fill Rewards inside Maliwize: grocery coupons as tiles, with a locked one that opens at a higher tier"),
    "code": (code, "One code at the till for the coupons picked, with a barcode and its expiry"),
    "switch_on": (switch_on, "Switching on Hey Fill Rewards: exactly what is shared, and a separate consent"),
    "close": (close_month, "Closing the month: which lines were kept inside their limit, and what carries forward"),
    "first_budget": (first_budget, "Your first budget, filled in from three questions"),
}


def screen(name, cls=""):
    fn, label = SCREENS[name]
    return phone(fn(), label, cls)
