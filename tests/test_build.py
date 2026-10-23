"""Tests for The Privacy Comfort Handbook build.

Covers the markdown-to-HTML converter (unit level) and the whole site build
(end-to-end): page generation, navigation, internal links, anchors, required
attribution, and a scan for secret-shaped strings.
"""

import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

_spec = importlib.util.spec_from_file_location("pch_build", ROOT / "build.py")
build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build)


class ConverterInlineTests(unittest.TestCase):
    def test_headings(self):
        self.assertEqual(build.md_to_html("# Hello"), '<h1 id="hello">Hello</h1>')
        self.assertEqual(build.md_to_html("## Sub part"), '<h2 id="sub-part">Sub part</h2>')

    def test_heading_slug_is_url_safe(self):
        out = build.md_to_html("## What's a 2FA code?")
        self.assertIn('id="whats-a-2fa-code"', out)

    def test_paragraph(self):
        self.assertEqual(build.md_to_html("Just a normal line."), "<p>Just a normal line.</p>")

    def test_bold_italic_inline_code(self):
        out = build.md_to_html("A **bold**, *soft*, and `tick` moment.")
        self.assertEqual(
            out, "<p>A <strong>bold</strong>, <em>soft</em>, and <code>tick</code> moment.</p>"
        )

    def test_link_markdown_to_html(self):
        out = build.md_to_html("See [chapter](03-passwords-and-2fa.md) now.")
        self.assertIn('href="03-passwords-and-2fa.html"', out)
        self.assertNotIn(".md\"", out)

    def test_link_with_anchor(self):
        out = build.md_to_html("See [entry](09-glossary.md#cookie) next.")
        self.assertIn('href="09-glossary.html#cookie"', out)

    def test_external_link_gets_noopener(self):
        out = build.md_to_html("Look at [a site](https://example.com) here.")
        self.assertIn('target="_blank" rel="noopener"', out)

    def test_raw_html_is_escaped(self):
        out = build.md_to_html("<script>alert(1)</script>")
        self.assertNotIn("<script>", out)
        self.assertIn("&lt;script&gt;", out)

    def test_code_span_contents_are_escaped_and_protected(self):
        out = build.md_to_html("Type `<b>x</b>` there.")
        self.assertIn("<code>&lt;b&gt;x&lt;/b&gt;</code>", out)


class ConverterBlockTests(unittest.TestCase):
    def test_horizontal_rule(self):
        self.assertEqual(build.md_to_html("---"), "<hr>")

    def test_fenced_code_block(self):
        md = "```text\nhello <world>\n```"
        out = build.md_to_html(md)
        self.assertIn("<pre><code", out)
        self.assertIn("hello &lt;world&gt;", out)

    def test_blockquote(self):
        out = build.md_to_html("> **Remember:** keep calm.")
        self.assertIn("<blockquote>", out)
        self.assertIn("<strong>Remember:</strong>", out)

    def test_unordered_list(self):
        out = build.md_to_html("- one\n- two\n- three")
        self.assertEqual(out.count("<li>"), 3)
        self.assertTrue(out.startswith("<ul>"))
        self.assertTrue(out.endswith("</ul>"))

    def test_ordered_list(self):
        out = build.md_to_html("1. one\n2. two")
        self.assertTrue(out.startswith("<ol>"))
        self.assertEqual(out.count("<li>"), 2)

    def test_task_list(self):
        out = build.md_to_html("- [ ] not yet\n- [x] done")
        self.assertIn('class="task"', out)
        self.assertIn('<input type="checkbox"> not yet', out)
        self.assertIn('<input type="checkbox" checked> done', out)

    def test_nested_list(self):
        out = build.md_to_html("- parent\n  - child A\n  - child B\n- second parent")
        self.assertIn("<ul>\n<li>parent\n<ul>", out)
        self.assertEqual(out.count("<li>child A</li>"), 1)
        self.assertEqual(out.count("<li>second parent</li>"), 1)

    def test_table(self):
        md = "| A | B |\n|---|---|\n| 1 | two words |"
        out = build.md_to_html(md)
        self.assertIn("<table>", out)
        self.assertIn("<th>A</th>", out)
        self.assertIn("<td>1</td>", out)
        self.assertIn("<td>two words</td>", out)

    def test_unterminated_fence_is_robust(self):
        out = build.md_to_html("```js\nconst x = 1;")
        self.assertIn("const x = 1;", out)


class EndToEndBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name) / "site"
        build.build(cls.out)
        cls.docs = sorted(
            build.DOCS_DIR.glob("*.md"), key=lambda p: (p.name != "index.md", p.name)
        )
        cls.pages = {p.stem for p in cls.docs}

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_every_doc_has_html(self):
        for doc in self.pages:
            self.assertTrue((self.out / f"{doc}.html").is_file(), doc)

    def test_assets_copied(self):
        self.assertTrue((self.out / "style.css").is_file())
        self.assertTrue((self.out / "favicon.svg").is_file())

    def test_footer_copyright_exact(self):
        expected = "Copyright (c) 2026 Asdale Dynamics, LLC"
        for name in self.pages:
            html = (self.out / f"{name}.html").read_text(encoding="utf-8")
            self.assertIn(expected, html, name)

    def test_attribution_credit(self):
        for name in self.pages:
            html = (self.out / f"{name}.html").read_text(encoding="utf-8")
            self.assertIn("Asdale Dynamics, LLC", html, name)

    def test_titles_present(self):
        html = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertIn("<title>Welcome — start here | The Privacy Comfort Handbook</title>", html)
        self.assertIn("The Privacy Comfort Handbook", html)

    def test_nav_lists_all_pages(self):
        html = (self.out / "index.html").read_text(encoding="utf-8")
        for name in self.pages:
            self.assertIn(f'href="{name}.html"', html, name)

    def test_prev_next_only_at_ends(self):
        first = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertNotIn('class="prev"', first)
        self.assertIn('class="next"', first)
        last = (self.out / "09-glossary.html").read_text(encoding="utf-8")
        self.assertIn('class="prev"', last)
        self.assertNotIn('class="next"', last)

    def test_print_button_only_on_checklist(self):
        for name in self.pages:
            html = (self.out / f"{name}.html").read_text(encoding="utf-8")
            if name == "08-privacy-checklist":
                self.assertIn("Print this checklist", html)
            else:
                self.assertNotIn("print-button", html)

    def test_checklist_has_checkboxes(self):
        html = (self.out / "08-privacy-checklist.html").read_text(encoding="utf-8")
        self.assertGreaterEqual(html.count('type="checkbox"'), 10)

    def test_internal_links_resolve(self):
        id_pattern = re.compile(r'id="([^"]+)"')
        link_pattern = re.compile(r'href="([^"]+)"')
        for name in self.pages:
            html = (self.out / f"{name}.html").read_text(encoding="utf-8")
            own_ids = {m.group(1) for m in id_pattern.finditer(html)}
            for href in {m.group(1) for m in link_pattern.finditer(html)}:
                if href.startswith("http") or href.startswith("style.css") or href == "favicon.svg":
                    continue
                target, _, frag = href.partition("#")
                if not target:
                    self.assertIn(frag, own_ids, f"{name} -> {href}")
                else:
                    target_name = target[:-5] if target.endswith(".html") else target
                    self.assertIn(target_name, self.pages, f"{name} -> {href}")
                    if frag:
                        target_html = (self.out / target).read_text(encoding="utf-8")
                        self.assertIn(f'id="{frag}"', target_html, f"{name} -> {href}")

    def test_no_duplicate_heading_ids(self):
        id_pattern = re.compile(r'id="([^"]+)"')
        for name in self.pages:
            html = (self.out / f"{name}.html").read_text(encoding="utf-8")
            ids = [m.group(1) for m in id_pattern.finditer(html)]
            self.assertEqual(len(ids), len(set(ids)), f"duplicate id in {name}")

    def test_no_secret_shaped_strings(self):
        patterns = ["sk-", "AKIA", "ghp_", "xoxb-", "BEGIN PRIVATE KEY", "api_key"]
        sources = [p.read_text(encoding="utf-8") for p in build.DOCS_DIR.glob("*.md")]
        sources.append((ROOT / "build.py").read_text(encoding="utf-8"))
        sources.append((ROOT / "README.md").read_text(encoding="utf-8"))
        for source in sources:
            for pat in patterns:
                self.assertNotIn(pat, source, f"secret-like pattern {pat} found")

    def test_license_exact_line(self):
        license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", license_text)

    def test_readme_credits_llc(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", readme)


if __name__ == "__main__":
    unittest.main()
