"""Regenerates the static site from docs/privacy-policy.md. Run from the sinew folder: python3 website/build.py
Then upload the changed files to the GitHub repo abelshelby95-lang/Abel-Shelby-Developments."""
import re, html, os
ROOT = os.path.join(os.path.dirname(__file__))
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500&family=Barlow+Condensed:wght@600&display=swap" rel="stylesheet">'

def page(title, desc, depth, body):
    up = '../' * depth
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="icon" href="{up}favicon.png">{FONTS}<link rel="stylesheet" href="{up}styles.css"></head>
<body><header><div class="wrap"><a class="brand" href="{up}">Abel Shelby Developments</a>
<nav><a href="{up}sinew/">Sinew</a><a href="{up}sinew/support/">Support</a></nav></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap"><a href="{up}sinew/privacy/">Sinew privacy policy</a><a href="mailto:abelshelby95@gmail.com">abelshelby95@gmail.com</a><br>© 2026 Abel Shelby Developments</div></footer>
</body></html>
'''

def inline(t):
    t = html.escape(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(https?://[^\s)]+?)([.,]?)(?=\s|$|\))', r'<a href="\1">\1</a>\2', t)
    t = re.sub(r'([\w.+-]+@[\w-]+\.[\w.]+)', r'<a href="mailto:\1">\1</a>', t)
    return t

def md(src):
    out, inlist = [], False
    for line in src.split('\n'):
        if line.startswith('- '):
            if not inlist: out.append('<ul>'); inlist = True
            out.append(f'<li>{inline(line[2:])}</li>'); continue
        if inlist: out.append('</ul>'); inlist = False
        if line.startswith('# '): out.append(f'<h1>{inline(line[2:])}</h1>')
        elif line.startswith('## '): out.append(f'<h2>{inline(line[3:])}</h2>')
        elif line.strip(): out.append(f'<p>{inline(line)}</p>')
    if inlist: out.append('</ul>')
    return '\n'.join(out)

def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(text)

policy = open(os.path.join(ROOT, '..', 'docs', 'privacy-policy.md')).read()
write('sinew/privacy/index.html', page('Sinew Privacy Policy', 'How Sinew handles your data.', 2, '<div class="policy">' + md(policy) + '</div>'))

write('index.html', page('Abel Shelby Developments', 'Simple, private apps for everyday life.', 0, '''
<p class="kicker">Abel Shelby Developments</p>
<h1>Apps that do<br>one thing well.</h1>
<p class="lede">Simple, private tools for everyday life.</p>
<a class="card" href="sinew/"><img src="sinew/icon.png" alt="Sinew app icon"><div><strong>Sinew</strong><span>An AI strength coach built around your recovery.</span></div></a>
'''))

write('sinew/index.html', page('Sinew: AI Strength Coach', 'Workouts built around how you slept.', 1, '''
<p class="kicker">Sinew for iPhone</p>
<h1>A coach that knows<br>how you slept.</h1>
<p class="lede">Sinew reads your HRV, resting heart rate and sleep from Apple Health, then builds a workout that fits your recovery and the weights you actually lifted last time.</p>
<h2>Built around your recovery</h2>
<ul><li>Daily readiness from Apple Health, including Oura and Apple Watch data</li><li>Workouts sized to your time, equipment and focus</li><li>Loads that progress from your logged sets</li><li>Tap any exercise for form cues and form videos</li></ul>
<h2>Log what you really did</h2>
<ul><li>Adjust weight and reps for every set in a couple of taps</li><li>A rest timer that alerts you even when you switch apps</li><li>Runs, rides and other cardio — logged by hand or pulled in from Apple Health</li><li>Personal records, weekly volume and cardio totals</li></ul>
<h2>Recover on purpose</h2>
<ul><li>Sauna, cold plunge, stretching and steam timers with temperature</li><li>Weekly goals, like three sauna sessions a week</li><li>Private progress photos with side-by-side comparisons</li></ul>
<h2>Fuel that keeps up</h2>
<ul><li>Scan a barcode to log packaged food</li><li>Snap a photo or describe a meal for a calorie and protein estimate</li><li>Recipe ideas that fit your goal and what's left of today's targets</li><li>Reminders you control for meals, water, weigh-ins and training</li></ul>
<h2>Private by design</h2>
<ul><li>Sinew only reads from Apple Health and never uses health data for ads</li><li>Progress photos never leave your phone</li><li>AI coaching is opt-in, and Sinew shows exactly what it shares</li><li>Delete your account and data from Settings anytime</li></ul>
<p>Coming soon to the App Store. Sinew Pro: 7-day free trial, then $12.99/month or $79.99/year.</p>
<p><a href="privacy/">Privacy policy</a> · <a href="support/">Support</a></p>
'''))

write('sinew/support/index.html', page('Sinew Support', 'Get help with Sinew.', 2, '''
<p class="kicker">Sinew support</p>
<h1>How can<br>we help?</h1>
<p class="lede">Email <a href="mailto:abelshelby95@gmail.com">abelshelby95@gmail.com</a> and we'll get back to you, usually within two business days.</p>
<h2>Readiness shows a dash</h2>
<p>Sinew needs HRV, resting heart rate or sleep in Apple Health. Check the Health app → Profile → Apps → Sinew and make sure reading is allowed. Oura users: turn on Apple Health sync in the Oura app. Readiness gets more accurate after about five days of data.</p>
<h2>My runs aren't showing up</h2>
<p>Sinew imports runs, walks and rides from Apple Health for the last 30 days. Make sure the app that recorded them (Apple Watch, Strava, etc.) writes workouts to Apple Health, and that Sinew is allowed to read Workouts. Then open Cardio and tap Import from Apple Health.</p>
<h2>Reminders aren't appearing</h2>
<p>Check iPhone Settings → Notifications → Sinew and make sure notifications are allowed. Focus modes can also silence them.</p>
<h2>Coach isn't answering</h2>
<p>AI coaching needs Sinew Pro and your permission. Check Settings → AI coaching in Sinew, and make sure you're online. Each account has a daily Coach limit that resets the next day.</p>
<h2>A barcode isn't found</h2>
<p>Sinew looks products up in Open Food Facts, a free public database. If an item is missing, describe the meal or snap a photo instead.</p>
<h2>Where are my progress photos stored?</h2>
<p>Only on your phone. They aren't backed up by Sinew, so deleting the app deletes them. Save copies to your Photos library if you want to keep them.</p>
<h2>Manage or cancel your subscription</h2>
<p>Subscriptions are handled by Apple. On your iPhone, open Settings → your name → Subscriptions → Sinew. To cancel a free trial without being charged, cancel at least 24 hours before it ends.</p>
<h2>Delete your data</h2>
<p>In Sinew, open Settings → Your data → Delete my data. This removes your account, your cloud backup and everything stored on your phone, including progress photos. Apple Health data isn't touched. You can also email us to request deletion.</p>
<p><a href="../privacy/">Read the privacy policy</a></p>
'''))
print('built')
