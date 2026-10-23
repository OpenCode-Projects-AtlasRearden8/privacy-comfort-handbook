# STATUS — Privacy Comfort Handbook

Last updated: 2026-10-23. Overall state: **complete and verified**.

## What was built

A beginner-friendly digital privacy manual ("explain it like a friend would")
in two deliverable forms:

1. **Markdown source of truth** in `docs/` (10 pages):

   - `index.md` — welcome, how to use the book, the three high-impact habits
   - `01-what-apps-and-websites-collect.md` — what chat apps and websites actually collect (metadata, cookies, device fingerprinting, why "free" products collect), with calm framing
   - `02-what-never-to-paste.md` — the never-paste list (passwords, 2FA codes, ID numbers, card numbers, document photos, keys/tokens), the postcard analogy, AI-chatbot guidance, calm recovery steps if you already pasted
   - `03-passwords-and-2fa.md` — long passphrases, password managers, a 2FA options table (passkey / authenticator app / SMS), recovery codes
   - `04-phishing-red-flags.md` — seven red flags, annotated example, phone-scam version, calm "if you clicked" drill
   - `05-browser-and-phone-privacy-settings.md` — the five browser moves that matter, the phone permission audit, an honest take on VPNs, a 20-minute tidy routine
   - `06-family-and-kid-accounts.md` — child accounts, shared devices, teens, grandparents, the family emergency folder
   - `07-checking-for-breaches.md` — Have I Been Pwned walkthrough, the calm five-step response, twice-a-year ritual, official-channel boundary
   - `08-privacy-checklist.md` — printable, checkbox-based (15-minute / one-hour / household / twice-a-year / someday / emergency-card sections)
   - `09-glossary.md` — 25 plain-English definitions

2. **A static HTML site** generated from that Markdown by `build.py`
   (Python standard library only, no dependencies). Output in `site/`:
   10 styled HTML pages plus `style.css` and `favicon.svg`. Features: top
   chapter navigation with current-page highlighting, previous/next links,
   warm book-like print-friendly CSS, anchor IDs on headings, internal links
   rewritten from `.md` to `.html`, external links with `rel="noopener"`,
   extra page footer, and a "Print this checklist" button on the checklist
   page only. The site contains no analytics, no cookies, no required
   JavaScript, and works offline.

Supporting files: `README.md`, `LICENSE` (MIT), `assets/`, `tests/`,
`.gitignore`, and this `STATUS.md`.

## How to run it

```bash
# build the static site (no dependencies, stdlib only)
python3 build.py            # -> site/

# build somewhere else
python3 build.py --out /tmp/anywhere

# read it
# open site/index.html in any browser (works offline)

# run the full test suite
python3 -m unittest discover -s tests -v
```

## Verification results

Environment: Python 3.13.5, Linux.

- `python3 build.py` — builds cleanly; 12 files written into `site/`
  (10 HTML pages + style.css + favicon.svg).
- `python3 -m unittest discover -s tests -v` — **32 tests, all passing.**
  Coverage includes:
  - converter units: headings/anchor slugs, paragraphs, bold/italic/code,
    link rewriting (.md -> .html, anchors preserved), external-link
    no-opener, raw-HTML escaping, code-span escaping, horizontal rules,
    fenced code blocks (including unterminated ones), blockquotes,
    unordered/ordered/task/nested lists, tables;
  - end-to-end: every doc produces an HTML page, assets copied, exact
    `Copyright (c) 2026 Asdale Dynamics, LLC` line present in every page
    footer, LLC credited on every page, nav lists all pages, prev/next only
    at the ends, print button only on the checklist, 26 checkboxes render,
    **every internal link and every anchor resolves to a real generated
    page/heading**, no duplicate heading IDs, no secret-shaped strings
    (`sk-`, `AKIA`, `ghp_`, `xoxb-`, `BEGIN PRIVATE KEY`, `api_key`) in any
    source file, LICENSE contains the exact required copyright line,
    README credits Asdale Dynamics, LLC.
- `python3 -m py_compile build.py tests/test_build.py` — passes.
- A repo-wide scan confirmed no CJK/Cyrillic characters (several slipped
  into early drafts and were caught and fixed via this scan).
- The site is intentionally **not committed and not published** anywhere;
  it is generated locally via `build.py` (and `.gitignore`d).

## Commits

Single plain commit on `main` using the existing local git identity
(Dylan Asdale, dylanasdale@users.noreply.github.com). No Co-authored-by
trailers. No pushes, no remotes, nothing published.

## Known gaps

- **Markdown support is a deliberate subset**, matched to what the docs
  use: no images, no setext headings, no footnotes, no HTML passthrough
  (raw HTML is escaped, not rendered). Extending it means writing more
  converter tests first.
- **No site search**, RSS feed, dark mode, or print-PDF generator; the CSS
  covers screen + print only.
- **App menus drift**: chapters describe settings by category rather than
  exact menu paths, so version drift between app settings pages is expected.
- **External sites change**: links such as haveibeenpwned.com and national
  reporting sites are current as of 2026-10; chapters note to search the
  name if a link dies.
- The checklist renders as real HTML checkboxes — an accidental tick (or a
  browser "restore form values") can persist on an individual page reload;
  fresh build or incognito clears it. Considered cosmetic.
- Manual content covers everyday privacy for a general audience; it
  deliberately excludes deep-dive topics (hard drive encryption,
  enterprise MDM, Tor usage) to keep the beginner promise.
