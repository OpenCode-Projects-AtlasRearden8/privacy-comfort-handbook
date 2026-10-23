# What to never paste

*Reading time: about 8 minutes.*

Paste boxes are everywhere now: DMs, work chats, support forms, and — the newest member of the family — AI chatbots. Pasting feels private. It is just you and a quiet text window, nobody watching.

Here is the analogy that makes it stick: **pasting into anything you don't fully control is like sending a postcard.** A postcard travels fine most of the time, and every postman can read it along the way. You write postcards about the weather. You write the mortgage details in an envelope.

This chapter is your list of what counts as envelope material.

## The never-paste list

None of these go into chat apps, DMs, comment boxes, support forms, or AI chatbot windows:

1. **Passwords and passphrases** — even the "unimportant" ones. Reused passwords turn one leak into five.
2. **2FA codes** — the six-digit codes from your authenticator app or text messages. A live code *is* the key to your account, right now, today. No legitimate company will ever ask for it.
3. **Government ID numbers** — Social Security number, national insurance number, tax ID, driver's license or passport number.
4. **Full payment details** — full card numbers (even partial ones plus the security code), full bank account and routing numbers, login credentials for payment apps.
5. **Medical and insurance identifiers** — insurance member IDs, medical record numbers, claim numbers. Insurance cards are basically a skeleton key to your identity.
6. **The combo that unlocks everything**: full date of birth, full street address, mother's maiden name, first pet, or any "security question" answers — especially not several of them together.
7. **Photos of documents** — a screenshot of your license, passport, insurance card, or a filled-out form is the same data, in a more leak-prone format.
8. **Keys and tokens** (for the developers and tinkerers): API keys, SSH private keys, `.env` files, database connection strings, OAuth tokens. If it looks like a password made of random letters, it is one.

What these share: they are **replayable**. An opinion about a TV show, once leaked, ages harmlessly. A Social Security number, once leaked, can be replayed against bank after bank for years. Replayability is the whole dividing line.

## "But it's just me and an AI, right?"

Gently: no, not exactly. A chat with an AI assistant is a conversation with a service running on a company's computers. Depending on the product and setting you chose, conversations may be stored for days or months, may be reviewed to improve the system, or may be used for training unless you opted out.

This is not a reason to avoid AI tools — they are wonderful for writing, learning, planning, and troubleshooting. It is a reason to paste like it's a postcard:

- **Fine to paste:** an error message, a paragraph you want explained, calendar-agnostic appointment phrasing, imaginary "example 123" data in a spec, code with no credentials in it.
- **Replace and paste:** if the AI needs structure from your data, paste a *disguised twin* instead — "Jane Doe, born 01/01/1970, address of 123 Main Street." The structure is usually all the helper ever needed.

## What if it's already out there?

Do not spiral. Oversharing is a data point, not an identity. In rough order of urgency:

1. **If a password or 2FA code went out:** change that password now, from a device you trust. Then change it anywhere you re-used it. If the code was for an account, sign out all sessions in that account's security settings, then re-check the account.
2. **If a card number went out:** call the number on the back of the card (dial it yourself — never a number from the chat) and ask for a replacement. Card issuers do this politely, all day long, for exactly this reason.
3. **If an ID number went out:** most of the time nothing happens. Watch for the classic signs — unexpected mail, new accounts you didn't open, a tax filing that isn't yours. In several countries you can place a free fraud alert or credit freeze with the credit bureaus; an evening task, fully reversible.
4. **If it went into an AI tool:** check that product's settings for a "delete conversation" option, and revoke any API key immediately (in the provider's dashboard, a "revoke" button does it in seconds). Then carry on.
5. **If someone asked for it in a message:** treat the request itself as the scam — chapter 04 will tell you why, in a way that will save you many future worries.

## The friendly habit, if you want it

Before you paste, ask one question: *"Would I write this on a postcard?"* If the answer is no, the text stays in the envelope — meaning it goes only into your password manager, the official app, or an official page whose address you verified yourself.

That one reflex prevents the majority of privacy disasters that actually happen to normal people. It costs nothing. It works while you're tired. It is the single highest-value habit in this whole handbook.

> **Remember:** you are not paranoid for double-checking. You are a person with a mailbox. Postcards for weather; envelopes for keys.

Next up: [Passwords and 2FA, simply](03-passwords-and-2fa.md).
