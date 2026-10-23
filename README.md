# The Privacy Comfort Handbook

Everyday digital privacy, explained like a friend would. A calm, plain-English
beginner's manual covering:

- what chat apps and websites actually collect,
- what never to paste into a chat, a form, or an AI chatbot,
- passwords and 2FA, without the drama,
- phishing red flags that fit on a sticky note,
- browser and phone privacy settings that actually matter,
- family and kid accounts,
- checking if you're in a data breach (and the calm response).

The tone throughout is warm and non-scary: privacy is a dial, not a switch.
The handbook distills into a **printable privacy checklist** and a full
**glossary** of plain-English definitions.

Written and maintained by **Asdale Dynamics, LLC** as part of its
beginner-friendly guide series (the same spirit behind the book
*The Massive AI Manual*: explain technology like a friend would — never
condescending, never alarmist).

## Read it

The Markdown "source of truth" lives in [`docs/`](docs/). Build the static
site and open it in any browser:

```bash
python3 build.py
```

That generates `site/`, a self-contained static HTML site with no external
dependencies, no analytics, no cookies, and no JavaScript requirements (one
optional print button). Open `site/index.html` to start reading. Everything
works offline.

## Test it

```bash
python3 -m unittest discover -s tests -v
```

The suite covers the Markdown-to-HTML converter (headings, lists, tables,
task lists, quotes, code fences, inline formatting, link rewriting) and an
end-to-end build check: every page renders, every internal link and anchor
resolves, the required copyright line appears in the footer, and no secret
or API-key-shaped strings appear anywhere.

## Where things live

```
docs/                 10 Markdown chapters (the source of truth)
assets/               stylesheet and favicon, copied into the site
build.py              stdlib-only static site generator (docs/ -> site/)
tests/                converter unit tests + end-to-end build tests
site/                 generated output (not committed; run build.py)
```

## Project principles

- **Local-first:** plain files, one stdlib Python script, no accounts.
- **Tested:** the build is verified by an automated test suite.
- **Privacy-respecting by construction:** the site ships zero trackers.
- **No secrets:** no API keys, credentials, or personal data in the repo.
- **Beginner-first:** every technical term is defined like a friend would.

## License

MIT — see [`LICENSE`](LICENSE). Copyright (c) 2026 Asdale Dynamics, LLC.

This is educational material about general digital safety, not legal,
medical, or professional security advice. For serious situations (fraud,
identity theft, stalking) the chapters point to official channels.
