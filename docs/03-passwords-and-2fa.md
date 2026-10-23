# Passwords and 2FA, simply

*Reading time: about 9 minutes.*

Two facts carry this entire chapter:

1. Almost every real account takeover happens because someone reused a password that leaked from some other site, or fell for a phish. Not because a hacker "guessed" a clever password.
2. Turning on two-factor authentication (2FA) blocks the overwhelming majority of those takeovers — with one setup, done once, per account.

So this chapter is not about becoming a cryptography expert. It is about two small habits: long passwords you barely have to remember, and a second lock where it counts.

## Passwords: length beats drama

The old rules — "change it every 90 days," "add a symbol," "p@ssW0rd!" — were aimed at a threat that barely exists: brute-force guessing. Modern password guessing dies at length. Each extra character multiplies the work enormously.

- `Tr0ub4dor&3` — eleven characters, famously miserable to remember.
- `purple-frog-radiates-tuesday` — twenty-nine characters of ordinary words, far harder to attack, and you can actually hold it in your head.

The friendly modern rule: **pick three or four unrelated words, connect them with dashes or spaces, done.** Smush unrelated things together: `maple-runway-71-brunch`. If a small element feels memorable to you — a childhood street, a favorite dish — that is fine; the *combination* of unrelated words is the security, not the cleverness.

## The password manager: an address book for passwords

Once passwords must be long and unique, no human memorizes them all — and you are not supposed to. That is what a password manager is for: an app that remembers every password behind one master password (or your phone's fingerprint).

A beginner-friendly description: it is a contacts app, except each entry stores a login instead of a phone number. You tap the login field, your password manager offers the right credentials, you confirm. After two weeks it works better and faster than your old system.

Options, all respectable as a starting point:

- **The one built into your browser or phone** (saved passwords, syncs across your devices). Zero setup, does 90% of the job. Fine everyday choice.
- **A dedicated password manager app**, which adds stronger autofill, secure notes, and breach alerts, and can share select entries with family members (handy for chapter 06).

Either way, one habit matters most: **the master password is the only password you keep in your head.** Make it a long four-word passphrase, never type it into any other site, and never paste it into a chat (chapter 02!).

And the honest caveat, so nothing here is oversold: if you forget the master password, most managers cannot recover it for you. Write the master passphrase on paper while you are learning the system, and store the paper somewhere an intruder would not casually wander by — a bookshelf is plenty normal; taping it to the monitor is where we draw the line.

## 2FA: the second lock

Here is a useful reframe for 2FA: your password says "this is my account"; the second factor says "this is my account and I am standing here with my own device." A thief with your password alone now fails at the front door.

**Where to turn it on first:** anything that holds money or the keys to everything else.

1. Your email account — it resets the passwords of everything else.
2. Banking and payment apps.
3. Your phone's account (Apple/Google), and your cloud backups.
4. Social media — someone else posting as you is a mess worth avoiding.

Everything else: welcome bonus, add whenever.

**Which kind of 2FA to pick**, if the app offers the choice:

| Option | How it works | In plain terms |
| --- | --- | --- |
| Authenticator app codes | A six-digit code, refreshed every 30 seconds, on your phone | The sweet spot: works offline, survives a dead SIM, easy setup. |
| Passkeys / signing in with your device's fingerprint or face | Your phone or computer itself proves it is you | Even easier once configured — nothing to type. Great where offered. |
| Text message (SMS) codes | A code texted to your phone | Much better than nothing. Weaker if someone tricks your phone company (a "SIM swap"), still worth having. |
| Nothing | Password only | The one option to avoid on important accounts. |

So the ladder is: **passkey if offered, authenticator app if not, SMS rather than nothing.**

Setting up an authenticator app takes about three minutes:

1. In the account's security settings, find "two-factor authentication" and choose "authenticator app."
2. The service shows a square barcode. On your phone, an authenticator app scans it.
3. The app now shows a six-digit code that rotates every half-minute. Type today's code back into the website to finish pairing.
4. Take the receive-a-code method off your mental pedestal — same six digits, but generated on your phone instead of arriving by text.

## Recovery codes: the spare key under the flowerpot

Right after enabling 2FA, the site shows a list of one-time recovery codes. Screenshot-free zone — this is one of the few genuinely safe things to write down or store:

- Print them, or save them inside your password manager's secure notes.
- They are your spare key: phone in a lake, phone lost, SIM replaced — recovery codes get you back in.
- Store them with roughly the care you would give a spare house key. Not on your desk. Not in an email draft to yourself.

If you have family accounts (chapter 06), tuck recovery codes into the household's emergency folder. One folder, rarely opened, occasionally a lifesaver.

## The "someone has my password" drill (30 seconds)

If you ever see a "new sign-in from elsewhere you don't recognize" alert:

1. In that account's security settings, sign out all other sessions.
2. Change the password.
3. If 2FA was off, turn it on now — this alert is its origin story for most people.

> **Remember:** you are not forgetful for needing help storing dozens of passwords. Humans were never meant to memorize forty keys. Tools exist for exactly this; using one is getting organized, not getting old.

Next up: [Phishing red flags](04-phishing-red-flags.md).
