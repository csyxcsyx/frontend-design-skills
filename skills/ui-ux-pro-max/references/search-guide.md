# Focused catalog search and optional persistence

Read only when a concrete question needs catalog guidance or a design proposal needs saving. Existing project decisions can be sufficient; a small UI fix does not require search or full design-system generation.

## Invocation and modes

Resolve `scripts/search.py` from this skill's directory and use its absolute path from any project. Use Python 3 with no external packages. In the examples, replace `<absolute-skill-dir>` with the actual directory containing this skill's SKILL.md; do not pass the placeholder literally:

```powershell
python -X utf8 "<absolute-skill-dir>/scripts/search.py" "keyboard focus modal" --domain ux -n 3
python -X utf8 "<absolute-skill-dir>/scripts/search.py" "virtualize" --stack react -n 1
python -X utf8 "<absolute-skill-dir>/scripts/search.py" "SaaS analytics dashboard" --design-system -p "Analytics" -f markdown
```

If needed, use `py -3 -X utf8` on Windows or `python3` on Unix. Do not use Claude environment variables or assume the project contains the script.

- **Focused issue:** choose an explicit `--domain` and 1–3 results. For accessibility or wrapping, query the semantic outcome first; use a separate detected-stack query only for distinct implementation details.
- **Known stack:** use its actual `--stack` name; inspect supported names with `--help` if needed. Do not invent a default or assume all frameworks are covered. Design-system mode ignores `--stack`, so run separate queries when both are needed.
- **Genuinely new direction:** `--design-system` aggregates product/style/color/landing/typography suggestions. Reuse an existing design system for new pages in the same product.
- Use `--full` only when truncation hides necessary detail and `--json` when structured results are useful. Avoid printing whole catalogs or irrelevant results.

Domains: `product`, `style`, `color`, `typography`, `google-fonts`, `landing`, `ux`, `chart`, `icons`, `gsap`, `react`, `web`. The historical `web` domain contains native/app guidance; check the platform column. Stacks include web/mobile frameworks and JavaFX/WPF/WinUI/Avalonia/Uno/UWP; use the detected supported target rather than applying web examples to native UI unchanged.

## Relevance and retry contract

Build a query around one intent in 2–5 English terms because the index is primarily English. Translate Chinese design intent for search, not the user's requested UI language. Examples: “后台表格太挤” → `table density responsive`; “报错不清楚” → `error summary validation`.

Inspect domain/platform, top result identity, and applicability before using output. If empty or irrelevant, rewrite once using narrower terms, an explicit domain/stack, or suggested catalog vocabulary (`virtualize` may match when `table virtualization` does not). If still unsuitable, disclose the limitation and label general guidance as a fallback. Reuse successful results within the task; do not repeat queries because a second skill is involved.

Check generated sections independently: dashboard suggestions may include an irrelevant marketing hero/CTA pattern. Keep useful palette/type candidates while discarding unsuitable structure. Catalog entries are recommendations, not overrides of the brief, private-data handling, project rules, or current official version documentation. Do not persist unverified or irrelevant matches.

## Optional persistence

Read the existing project design documentation first. Where this mechanism is used, read `design-system/<project-slug>/MASTER.md` and the relevant `pages/<page>.md`; page overrides take precedence. Saving is useful only if it serves the requested deliverable, not as an automatic extra documentation step.

```powershell
python -X utf8 "<absolute-skill-dir>/scripts/search.py" "SaaS analytics dashboard" --design-system --persist -p "Analytics" --output-dir "<absolute-project-root>"
```

Always pass the explicit project root. This creates `design-system/<project-slug>/MASTER.md`; add `--page "dashboard"` for a page override. Existing files are skipped unless `--force` is used. Read existing content and use force only when replacement is authorized. Review saved proposals and edit them to reflect accepted decisions; generation alone is not approval or authority.

For optional 1–10 `--variance`, `--motion`, and `--density`, read [design-dials.md](design-dials.md) only when tuning those dimensions. They are heuristic intent controls, not quality scores or dependency requirements.
