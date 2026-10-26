---
name: ui-ux-pro-max
description: "Design, implement, and review web, mobile, and desktop interfaces using a searchable local UI/UX catalog. Use for page layout, component styling, typography, palettes, interaction, accessibility, responsive behavior, and design systems; includes Chinese requests for 界面设计、页面美化、交互优化. Exclude backend-only tasks."
---

# UI/UX Pro Max

Design around the actual product and task. Catalog entries are recommendations, not authority over the brief or proof of compliance.

## Ground and scope

Inspect the affected screen, actual content, project rules, stack/version, tokens and components. Identify the user's immediate job, needed information and primary contextual action. Preserve brand, platform conventions and functional contracts unless their change is requested. Match the requested language; do not assume Chinese copy or a website. Utility screens lead with working content, not a decorative hero.

Reuse established decisions/primitives; no framework, dependency, font, theme, image or animation is required by this skill. Ask only about material blockers. Implement when asked to build/fix; report evidence-based findings when asked to review.

## Essential decisions

- **Useful words:** titles name the screen/object/task; buttons name outcomes. Avoid invented poetic slogans such as “让数据，清晰可见” on ordinary product screens. Omit a subtitle, eyebrow, helper line, badge or footer note unless it adds information for identification, a decision, action or recovery. Keep labels, units, requirements, errors, consequences and required disclosures. Use consistent terms through the flow. Read [product-copy.md](references/product-copy.md) only for copy-heavy work.
- **Discoverable actions, light grouping:** ambiguous actions need a resting-state cue, not hover alone. Prefer coordinated soft surfaces with sufficient separation, segments, interactive rows, underlines or local emphasis. Group related controls using alignment/spacing instead of independent rectangles or decorative frames inside frames. Retain necessary input boundaries and meaningful containers.
- **Accurate states:** distinguish temporary press, selection, expansion, disabled and focus. Modes switch directly; unavailable operations must not look enabled. Avoid unintended harsh black borders/rings/shadows with theme-coordinated feedback. Keep keyboard focus, editing cues and high-contrast behavior; never suppress focus globally or blur controls to hide it.
- **Icons and feedback:** use recognizable graphical icons, not letter/word badges pretending to be icons. Keep meaningful file labels, shortcuts, formatting controls and brand marks. Preserve needed visible labels and accessible names; hide redundant decorative icons from assistive technology. Provide timely loading/empty/error feedback, reuse valid content when useful, separate popup surfaces and make contextual help keyboard/touch accessible. Read affected [interaction-guide.md](references/interaction-guide.md) sections only when needed.
- **Visual hierarchy:** use semantic type/color/spacing/layer roles, task-appropriate density and readable contrast; preserve status/chart colors. Check actual language, glyphs, wrapping, long labels and platform sizing. Do not add whitespace, cards, metrics or decorative text just to fill a template. Respect reduced motion and themes in scope.
- **Components:** page/window entrypoints compose cohesive modules with clear state ownership. Extract repeated UI, complex interactions and substantial business/data logic into appropriate files. Avoid oversized files disguised by many local render helpers, arbitrary line quotas and trivial wrappers.

## Context and verification budget

Proceed directly when project guidance suffices. Search only for a concrete gap: read [search-guide.md](references/search-guide.md) when invoking the catalog, start with 1–3 results, rewrite at most once, check relevance and label fallbacks honestly. Full system generation is for a genuinely new direction. Reuse successful searches and already-read guidance.

Load only applicable sections: [quick-reference.md](references/quick-reference.md) for a rule, [pro-rules.md](references/pro-rules.md) for native/mobile polish, [web-quality.md](references/web-quality.md) for affected web forms/layout/state. No automatic full-reference reads, network refreshes, detectors or stacked audits.

Inspect the affected render when available: what reads first, whether actions/titles are concrete, which small text is necessary, and representative states, wrapping, sizes/themes. Review module boundaries and run applicable project checks in one coordinated pass. Fix concrete defects and recheck their effects; no scoring loops, cosmetic variant batches or unexplained repeats of passed checks. Source inspection is not a visual test. Briefly report changes, actual checks and limitations.

Taste is optional for substantial landing/brand/portfolio/editorial web composition. Dashboards, tables, complex forms and native workflows use product/platform guidance. Share decisions, searches and verification; read the optional [collaboration guide](../design-taste-frontend/references/collaboration.md) only for routing/dials, and continue independently if absent. No subagent workflow is implied.
