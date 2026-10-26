---
name: design-taste-frontend
description: "Art-direct and implement distinctive landing pages, brand websites, portfolios, editorial pages, and visual redesigns. Use for stronger composition, typography, visual rhythm, and purposeful motion, including 去模板化、官网美化、作品集设计. Complements ui-ux-pro-max for UX guidance; exclude dashboards, data tables, complex forms, and native app workflows."
---

# Taste: product-specific visual design

Adapted from Taste and selected design-engineering guidance. Distinctiveness comes from this product's content, audience and composition, not ornamental copy or a recurring style preset.

## Direction

Inspect the affected page, real assets/content, audience, primary action, project rules, stack and established design. Distinguish new work, preservation and overhaul. Keep a short working direction for substantial changes; small edits need no ceremony or multiple concepts. Clarify only material blockers.

Use Taste for marketing, brand, portfolio and editorial web surfaces. Dashboards, tables, complex forms and native workflows use UI/UX Pro Max or platform guidance. Share brand tokens without copying marketing layout, density or motion into operational UI. Choose hierarchy, type, imagery and spacing from actual content; one meaningful expressive choice can be enough. Familiar fonts, colors, centered layouts, cards and repeated structures remain valid when useful.

## Words and structure

- Titles identify real subjects or specific benefits; action labels name outcomes. Ordinary product screens need no hero slogan. Do not invent “让数据，清晰可见” or pseudo-editorial titles to fill space. Expressive brand headlines need a specific offer and real brief; preserve approved copy and quotations.
- Before adding a subtitle, eyebrow, hint, badge or note, identify its distinct information. If removing it changes no identification, decision, action or recovery, omit it. Avoid habitual small text beneath every heading/control. Keep units, requirements, errors, consequences, legal copy and accessible labels. Use consistent vocabulary, not literary synonyms. The companion's optional [product-copy guide](../ui-ux-pro-max/references/product-copy.md) covers text-heavy work; core rules stand alone if absent.
- Use real assets and authentic claims. Never invent customers, testimonials, endorsements, specifications or metrics; visibly label illustrative mock content. Images and numbers need a purpose, not a slot in a template. A typographic page can be complete without photos.
- Give type roles clear size/weight/spacing contrast and deliberate alignment. Tune actual copy at real widths rather than adding captions, giant headings, excessive tracking, forced breaks or tiny text. Check font coverage, punctuation, clipping and localization; English word quotas do not transfer to Chinese. Read [composition.md](references/composition.md) only for substantial visual work.

## Craft and implementation

- Make ambiguous actions recognizable before hover with coordinated soft backgrounds, segments, rows, underlines or local emphasis. Group related controls; avoid a wall of rectangles, decorative nested frames and filler grids. Keep necessary input boundaries and semantic status colors.
- Use graphical icons from the existing family with needed labels/accessible names; retain meaningful file labels, shortcuts, formatting controls and brand marks. Distinguish momentary press, selection, expansion, focus and disabled states. Modes switch directly; unavailable operations must not look enabled. Avoid unintended harsh black frames while keeping keyboard focus, editing cues and high-contrast support; never suppress all focus or blur after clicks.
- Provide relevant loading/error feedback, useful content retention, separated popup surfaces and contextual help accessible on keyboard/touch. The companion's optional [interaction guide](../ui-ux-pro-max/references/interaction-guide.md) covers detailed scenarios; use only affected sections.
- Reuse the actual framework, tokens, primitives and themes in scope. Do not migrate to React/Next.js or add Tailwind, Motion, GSAP, remote fonts or themes merely for style. Use framework-appropriate browser/client boundaries. Preserve routes, IDs, form/analytics contracts, brand and copy outside the requested change.
- Compose focused components with clear state ownership in appropriate files. Extract cohesive sections, repeated UI and substantial logic; keep page entrypoints concise without arbitrary line quotas, excessive wrappers or many local render helpers hiding an oversized file.
- Motion serves feedback or explanation, respects reduced motion and is optional. Read [motion.md](references/motion.md) only for animation. Variance/motion/density dials describe intent, not quality; do not increase them automatically or impose an `8 / 6 / 4` baseline.

## Efficient completion

Work directly when existing guidance is sufficient. Catalog searches resolve specific gaps and their results are shared, not duplicated. Load only relevant reference sections; no automatic detector, document, critique command, several audits or variant batch. Read the optional [collaboration guide](references/collaboration.md) only for routing/dials. Share one direction, token set, component structure and verification pass.

Inspect the affected render when possible: does it belong to this product, what reads first, and which words/boxes can disappear without losing meaning? Check representative pointer/keyboard states, layouts/themes, relevant loading/help, content without motion and module boundaries, then applicable project checks. Fix concrete defects and recheck affected behavior; no scoring loops or unexplained repeats. Report the implemented result or prioritized findings, actual evidence and material limitations briefly. Do not claim visual/performance/accessibility tests that were not run. No subagent workflow is implied.
