---
name: design-taste-frontend
description: "Art-direct and implement distinctive landing pages, brand websites, portfolios, editorial pages, and visual redesigns. Use for stronger composition, typography, visual rhythm, and purposeful motion, including 去模板化、官网美化、作品集设计. Complements ui-ux-pro-max for UX guidance; exclude dashboards, data tables, complex forms, and native app workflows."
---

# Taste: product-specific visual design

Distinctiveness comes from the actual product, audience and composition, not ornamental copy or a recurring style preset. Adapted from Taste and selected design-engineering guidance.

## Direction and content

Inspect the actual page/content, audience, action, project rules, stack and existing design. Distinguish new work, preservation and overhaul. Substantial work needs a short direction; small edits need no ceremony or concept batch. Clarify blockers only.

Taste serves marketing, brand, portfolio and editorial web surfaces. Dashboards, tables, complex forms and native workflows use UI/UX Pro Max or platform guidance. Share brand tokens without copying marketing navigation, density or motion into operational UI. Choose hierarchy and expression from content; familiar fonts, colors, centered layouts, cards and repetition are valid when useful.

- Titles name actual subjects or specific benefits; buttons name outcomes. Utility screens need no hero slogan. Do not invent “让数据，清晰可见” or pseudo-editorial titles. Expressive brand copy needs a real offer/brief; preserve approved wording and quotations.
- Before adding a subtitle, hint, eyebrow, badge or note, identify its distinct information. Omit it if removal changes no identification, decision, action or recovery. Deduplicate status without removing uncertainty, provenance, units, requirements, error recovery, consequences or legal/accessibility labels. Avoid habitual small text under every control and literary synonyms for established terms. Use the companion's optional [product-copy guide](../ui-ux-pro-max/references/product-copy.md) for text-heavy work; core rules stand alone if absent.
- Use authentic assets/claims; never invent customers, testimonials, endorsements or metrics. Visibly label illustrative mock content. Imagery and numbers need a purpose rather than a slot in a template.

## Layout and interaction

- Give type roles clear scale/weight/spacing contrast and deliberate alignment. Tune real content at actual widths; avoid giant headings, tiny labels, excessive tracking or forced breaks as shortcuts. Check scripts/fonts, punctuation, wrapping, clipping and localization; English word quotas do not transfer to Chinese.
- Match card size and content density; use available space without empty filler or forcing every screen into a single viewport. Keep labels, badges and controls visible. Updates and detail opening should not cause unrelated rows, centered titles or primary actions to jump. Read [composition.md](references/composition.md) for substantial visual work; the companion's optional [dense-surfaces guide](../ui-ux-pro-max/references/dense-surfaces.md) covers dense detail/graph surfaces.
- Make ambiguous actions recognizable before hover using soft surfaces, segments, rows, underlines or local emphasis. Group related controls, retain functional boundaries and avoid decorative nested frames. Hit areas need visible ownership, not surprise full-row activation. Use graphical icons with needed visible/accessibility labels; meaningful shortcuts, file/formatting controls and brand marks remain valid.
- Separate temporary press, persistent selection, expansion, focus and disabled states. Selection survives blur; modes switch directly and unavailable actions do not look usable. Avoid unintended black frames while preserving keyboard focus, editing cues, semantic colors and high-contrast support; do not globally suppress focus or blur after clicks.
- Provide truthful loading/status, separated popup surfaces and accessible contextual help. Routine notices should not require a click or expand the page; important decisions and recovery must remain available. Read only affected companion [interaction-guide](../ui-ux-pro-max/references/interaction-guide.md) sections. Core rules here apply if the companion is absent.

## Implementation and finish

Reuse the framework, primitives, tokens and themes; no migration or new styling/animation/font dependency for Taste alone. Preserve routes, IDs, contracts, brand and copy outside scope; use appropriate client boundaries. Compose focused modules with clear state ownership in suitable files. Extract substantial/repeated UI and logic without arbitrary line quotas, trivial wrappers or local helpers hiding an oversized page.

Decorations must not obscure text, data or controls. Animate emphasis separately from opaque content surfaces, with prompt interruptible feedback and reduced-motion support. Attention effects may suit a requested primary action, not every control. Read [motion.md](references/motion.md) only for animation. Variance/motion/density dials describe intent, not quality; no automatic escalation or mandatory baseline.

Work directly when guidance suffices; searches resolve concrete gaps and are reused. Load only relevant sections, not detectors, full audits, documents or variant batches by default. Use the optional [collaboration guide](references/collaboration.md) for routing/dials; share one direction, component structure and validation pass.

Inspect the affected render: product fit, hierarchy, necessary copy/boxes, content fit, update stability and pointer/keyboard states at in-scope sizes/themes. Check changed feedback/details/graphs, module boundaries and project checks together. Fix defects and recheck affected behavior without scoring loops or unexplained repeats. Briefly report evidence and limitations, not unrun tests. No subagent workflow is implied.
