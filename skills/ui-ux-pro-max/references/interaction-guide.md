# Interaction states, hit areas and feedback

Read affected sections only. Reuse project primitives/tokens and native equivalents; these rules do not prescribe a scanning-app layout, fixed timing, library or color palette.

## Visible ownership and state

An action resembling static text needs a resting cue: a distinguishable soft surface, segment, interactive row, underline, icon-plus-label pattern or suitable local emphasis. Hover alone is insufficient. Group related controls and express hierarchy instead of boxing every item. Preserve functional boundaries and semantic contrast.

| Role | State contract |
|---|---|
| Momentary action | Press feedback ends after release, cancel or capture loss; focused is not selected |
| Mutually exclusive mode | Each enabled choice directly enters that mode; actual selection survives blur and clicks elsewhere |
| Toggle | Persistent appearance and accessible state follow on/off data |
| Disclosure | Indicator and content follow expanded state, not sustained press color |
| Unavailable action | Disabled presentation and handler agree; explain a non-obvious prerequisite when useful |

Keep press, focus, selection and expansion separate in state and style. Native buttons/links and platform control states come first; do not leave a clickable control silently inert in a mode.

Hit areas must match the visible control's ownership. Test checkbox, label, adjacent whitespace and neighboring controls separately; an unrelated blank row must not toggle a small control unexpectedly. Preserve normal platform label activation when appropriate. If the user explicitly requests checkbox-only activation on a surface, implement that local contract without a full-row handler or globally disabling labels; preserve accessible naming, Space/keyboard operation and a usable target around the checkbox. Do not shrink targets simply to make them exact pixels.

## Focus and surfaces

Inspect inherited borders, outlines, rings and shadows in rest/hover/press/post-click/selected states. Replace unintended harsh black frames with theme-coordinated feedback while preserving requested intentional styling. On web, use `:focus-visible` or the established accessible mechanism. Keep editing cues, clearly visible keyboard focus and high-contrast/forced-colors behavior. Never suppress focus globally, programmatically blur a clicked control or hide focus with low contrast. Web selectors are not a native-UI implementation.

Hover/selection effects must not make a content card translucent so connectors or decorations show through text. Keep content surfaces opaque; animate a separate highlight, border, decoration or transition layer. Transitions should be brief, interruptible and responsive to a new target; invisible exit layers must not intercept input. No fixed universal duration or breathing effect is required.

## Truthful loading and stable updates

Show the real stage, operation/current item and completed/remaining amounts when known. Display percentages only with a meaningful denominator; use indeterminate progress otherwise. Do not invent progress or repeat the same timer/status in several lines. Preserve the distinction between saved/configured, active, tested, executing and failed; do not promote an AI assessment or unknown result to confirmed fact merely to simplify the wording.

Choose replacement-loading versus background-updating from the actual workflow. When preserving content is safe, keep useful previous results with an updating indicator. When a new run replaces results, use the agreed initial/loading flow and do not silently present stale results as current. Retain valid data for revisits where useful, invalidate changed inputs and isolate late completions. Prevent relevant duplicate submissions; handle completion, failure and cancellation explicitly. No mandated cache capacity or processing rewrite.

Reserve space for changing labels, timers, badges and spinners so they do not shift centered titles or primary actions. Avoid full content-opacity animation that reveals underlying lines. Respect reduced motion; a static progress indicator with accurate text remains useful.

## Notices versus decisions

Routine save/test/success feedback should be non-blocking, appear and dismiss automatically with a gentle transition where appropriate, and not expand a panel or push surrounding content. Use a consistent non-obscuring overlay/status location; centered placement is an explicit context choice, not a global requirement. Deduplicate repeated notices and provide enough reading time, with appropriate hover/focus pause or persistent history where needed. Avoid manual-close-only success dialogs.

Errors requiring recovery, unsaved/destructive decisions and consequential information must remain discoverable and actionable; do not auto-dismiss all messages. Use an inline state, durable notice or confirmation according to the consequence. Do not move focus to a routine toast or interrupt keyboard work.

## Menus and contextual help

Dropdown/popover surfaces need sufficient opacity, separation, spacing and correct stacking. Inspect the open surface for clipping, placement, selection, dismissal and keyboard behavior, not just the trigger.

Use short local help for unfamiliar terms, accessible on focus and touch as well as hover. Essential requirements/errors stay directly available; useless duplicate copy should be removed, not moved into a tooltip. Switching help targets should replace stale help without stacked overlays; allow reading without immediate accidental dismissal. Use project/platform timing and dismissal conventions, including Escape where appropriate, instead of copying one project's millisecond settings.

## Focused checks

Check relevant roles at rest, press/release/cancel, after blur, and by Tab/Shift+Tab/Space. Verify mode A → B → A, persistent selection, hit ownership, loading/revisit/failure, notice lifecycle, menus/help and no hidden focus. For detail panes, crowded cards or graphs, read [dense-surfaces.md](dense-surfaces.md). Batch these with the actual affected render; repeat only after changes or unresolved failures. A rule walkthrough is not runtime UI validation.
