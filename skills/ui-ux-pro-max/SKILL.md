---
name: ui-ux-pro-max
description: "Design, implement, and review web, mobile, and desktop interfaces using a searchable local UI/UX catalog. Use for page layout, component styling, typography, palettes, interaction, accessibility, responsive behavior, and design systems; includes Chinese requests for 界面设计、页面美化、交互优化. Exclude backend-only tasks."
---

# UI/UX Pro Max

Design for the actual task; assess catalog suggestions against the brief and verify the result.

## Ground and scope

Inspect actual content, project rules, stack/version, tokens and components. Identify the task, needed information and primary action. Preserve brand, platform conventions and functional contracts outside scope. Match the language/platform; utility screens lead with working content. Reuse primitives; no extra framework, dependency, theme, font, image or animation is required. Clarify blockers only; implement requested fixes and report supported review findings.

## Essential decisions

- **Direct, useful copy:** titles name the task/object and buttons name outcomes. State current facts, available functions and next actions directly; omit ornamental slogans, redundant small text and gratuitous “不是……而是……” / “……，不是……” contrasts. Keep meaningful negation for errors, limits, incomplete states, risks and quoted/approved content; preserve uncertainty and provenance. Use consistent terms and retain labels, units, requirements and disclosures. Read [product-copy.md](references/product-copy.md) for copy-heavy work.
- **Visible actions, light grouping:** ambiguous actions need a resting cue, not hover alone: coordinated soft surfaces, segments, rows, underlines or local emphasis. Use spacing/alignment instead of isolated rectangles and decorative nested frames. Keep necessary input boundaries. Hit areas must have clear ownership; unrelated row whitespace must not trigger a nearby control. Respect explicit surface-specific hit-area requests while preserving keyboard names/operation and usable targets.
- **State and focus:** distinguish press, persistent selection, expansion, disabled and focus. Selection survives blur; enabled modes switch directly. Keep resting input boundaries stable: mouse press/focus, dropdown opening and post-click states add no surrounding outline, ring, halo or border strengthening in any color. Use background, label or bottom indicators for editing, selection and visible keyboard focus. Preserve system high contrast; apply scoped replacements with clear cues, retaining focus and keyboard behavior.
- **Stable, readable layout:** size cards and text to actual content; prevent clipped labels, badges and edge controls. Use available workspace without arbitrary empty blocks or forcing everything into one screen. Keep primary anchors stable during updates. Prefer a suitable detail surface over expanding one grid item into a tall empty row. Read relevant [dense-surfaces.md](references/dense-surfaces.md) sections for dense cards, details or graphs.
- **Icons and feedback:** prefer graphical icons, not letters/words posing as icons. Retain meaningful file labels, shortcuts, formatting controls and brand marks; keep needed visible/accessibility labels and hide redundant decorative icons from assistive technology. Loading/status must reflect real work; routine notices should not require dismissal or resize the page, while decisions/errors needing action remain accessible. Read affected [interaction-guide.md](references/interaction-guide.md) sections for feedback, help, popups and state work.
- **Craft and code:** use semantic type/color/spacing/layer roles, readable contrast and task-appropriate density. Check actual scripts/fonts, long labels, zoom and themes in scope. Decorations cannot obscure content; motion is purposeful, interruptible and reduced-motion aware. Compose focused components in suitable files with clear state ownership; extract substantial/repeated UI and logic rather than hiding an oversized page behind local render helpers. No arbitrary line quotas or trivial wrappers.

## Efficient verification

Proceed when project guidance suffices. Search concrete gaps only: read [search-guide.md](references/search-guide.md) when invoking the catalog, start with 1–3 results, rewrite at most once, check relevance and label fallbacks. Full system generation is for a genuinely new direction. Reuse successful searches and already-read guidance.

Read relevant [quick rules](references/quick-reference.md), [native polish](references/pro-rules.md) or [web quality](references/web-quality.md) sections only; reuse evidence and combine checks.

Inspect the affected render: hierarchy, copy, content fit, pointer/keyboard state and layout stability at in-scope sizes/themes/zoom; check changed details/graphs/notices. Review module boundaries and applicable project checks together. Fix defects and recheck their effects without scoring loops, cosmetic variants or unexplained repeats. Report actual evidence/limitations; source review is not a visual test.

Taste is optional for substantial landing/brand/portfolio/editorial web composition. Product dashboards, forms, tables and native workflows use platform/task guidance. Share decisions, searches and validation; read the optional [collaboration guide](../design-taste-frontend/references/collaboration.md) for routing/dials only, and continue independently if absent. No subagent workflow is implied.
