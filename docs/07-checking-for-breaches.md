# Checking for breaches

*Reading time: about 8 minutes.*

Somewhere along the way, "your data was breached" started sounding like a personal failure. Let's fix that framing before anything else: **a breach is a theft incident at a company — not yours.** A store you shopped at in 2019 got robbed of its customer list. You were simply a customer that year. There is no shame in it, no aura of doom follows it, and the response takes about twenty minutes.

## What a breach actually is, in one paragraph

Companies keep databases: names, emails, passwords (hopefully scrambled), order histories. Sometimes someone steals one — an outside attacker, an insider, a misconfigured cloud folder left open like an unlocked car. That stolen database then floats around the internet. It is called a breach. If your email is in that database, it means *that company* lost data about you; it does not mean your devices are compromised, and it does not mean anyone has "hacked your email" — those are different, rarer events with different fixes.

## How to check: the friendly, five-minute way

The easiest tool for this is a website run by security researcher Troy Hunt, called **Have I Been Pwned** (yes, that is really the name — "pwned" comes from gamer slang for getting soundly beaten). Go to `haveibeenpwned.com` and:

1. Type your email address into the search box on the front page.
2. Read the results list. If your address appears, the page shows *which* breached sites it came from — old forums, stores, services — and the date.
3. Interpret gently. A list of small, old breaches from defunct forums is utterly normal — most people who have been online for a decade have one. What matters is what you *do* about it, which is next.

There is also a "Passwords" page on the same site where you can check whether a specific password ever appears in known leak collections. It is safe by design (the site never sends your actual password anywhere — it checks a scrambled fingerprint of it), though the easiest and most automatic way to get the same protection is simply using a password manager, which does this monitoring in the background (chapter 03).

## If your email shows up: the calm five-step response

Work top to bottom. Three of the five steps usually turn out to be "already done," and that is the point — this drill ends quickly:

1. **Change the password on any account you still use** that appeared in the breach list. (If you followed chapter 03, each account already has its own unique password — meaning a breach of site A cannot open site B. This is exactly why.)
2. **Change any password you reused** anywhere — the breach list tells you which site it leaked *from*, but reuse spreads it elsewhere.
3. **Confirm 2FA is on** for the important accounts: email first, then bank, then the rest.
4. **Watch that mailbox for a week.** Password-reset emails you didn't request, verify-your-account notices, new-device alerts: most are noise, but a burst of them means someone is testing the door — run the "new sign-in drill" from chapter 03 if that happens.
5. **Close the loop and move on.** Make a note of which accounts you checked; consider it done for another six months.

Then — genuinely intended — off you go with your day.

## How breaches relate to everything else in this handbook

The breach check is the "smoke alarm test" step that ties the other chapters together:

- Unique passwords (chapter 03) mean a breach anywhere is a *containable* event for you.
- 2FA (chapter 03) means a leaked password alone still fails at your door.
- The never-paste list (chapter 02) keeps your unfixable identifiers — ID numbers, card numbers — out of databases that leak in the first place.
- And the breach check itself turns vague background anxiety into a concrete, twice-a-year errand with a beginning and an end.

## The twice-a-year habit

Pair the breach check with something you already do twice a year — smoke-alarm batteries, the dentist, the spring closet clean. Ten minutes, once every six months:

1. Run your two most important email addresses through the checker.
2. Glance at your password manager's "security" or "watchtower" page if it has one (it flags weak, reused, or breached passwords for you).
3. Change anything it flags, using the drill above.

That is the entire ritual. It turns "am I safe?" — an unanswerable midnight worry — into "I checked in October and I am handling the list," which is a status you can *see*.

## One important boundary

If a breach ever involves something bigger than passwords — ID numbers, medical records, or you are seeing concrete fraud (accounts opened in your name, tax filings that aren't yours) — that moves past guides and into official channels, and that is *the correct next step*, not an escalation of panic. In the United States, IdentityTheft.gov walks you through a personalized recovery plan; most countries have an equivalent national reporting site (search "identity theft report" plus your country). Where this handbook gets fuzzy, official channels get precise — that is what they are for.

> **Remember:** appearing in a breach list means you were a customer. It does not mean you were careless. The drill is short, the fix is ordinary, and the person running the checker is the calm one at the table.

Next up: [The printable privacy checklist](08-privacy-checklist.md).
