# Discoverable actions and lightweight interaction

Read the affected sections for controls, state, loading, menus, help, or focus work. Apply the project's existing components/tokens and platform equivalents. These are general lessons from UI usage, not a scanning-app preset, mandatory library, or fixed timing configuration.

## Click cues without a wall of boxes

An action that resembles plain static text needs a visible cue before hover. Prefer a consistent soft surface distinguishable from the canvas for ambiguous controls; a segmented group, interactive row, established link underline, icon-plus-label affordance, or local emphasis may fit better. Keep text, boundaries where needed, and meaningful icons readable. Soft must not mean indistinguishable; color alone should not have to communicate an unfamiliar meaning.

Differentiate action hierarchy instead of boxing everything identically: reserve strong treatment for primary actions, use quieter secondary controls, and group related modes or toolbar actions. Whitespace, alignment, tint, and sparse dividers can separate content without an outer frame on every item. Avoid decorative frame-within-frame nesting; retain boundaries that explain an input, popup, grouped choice, or distinct content region. Use native semantic controls rather than styled static text with hidden click handlers. Static labels must not misleadingly resemble enabled buttons.

## States and behavior

| Role | Expected behavior |
|---|---|
| Momentary action | Press feedback ends after release/cancel/capture loss; post-click focus is not a selected state |
| Mutually exclusive mode | Clicking an enabled choice enters that named mode directly and clears the previous selection |
| Toggle | Persistent selected/pressed appearance reflects actual on/off state and appropriate semantics |
| Disclosure | Expanded state follows the content and indicator; it need not retain a dark pressed background |
| Unavailable operation | Accurately disabled or otherwise clearly unavailable, including the handler; explain a non-obvious prerequisite when useful |

Do not use one boolean or visual treatment for press, focus, selection, and expansion. Retain clear selected state and input-editing cues while normal buttons recover after the press. On web use native buttons/links and appropriate state semantics; use native commands/control states on desktop. Do not display an enabled operation that silently does nothing in the current mode.

## Borders and accessible focus

Inspect borders, outlines, rings, and shadows inherited from browser/native defaults and component styles. Replace unintended harsh black frames across rest/hover/press/post-click/selected states with coordinated theme tokens and clear background, color, or elevation feedback. Preserve deliberate outlines requested by the brief.

On web use `:focus-visible` or the existing accessible focus system for keyboard focus, keeping input-editing cues where needed. Replace an unwanted outline with a visible contrasting indicator before removing it. Never globally suppress focus styles, programmatically blur controls to hide a frame, or use low contrast to conceal focus. Retain high-contrast/forced-colors behavior. Do not apply web selectors mechanically to native controls.

## Loading and valid result reuse

Give timely operation feedback; for noticeable waits show an appropriate spinner/progress or short status and a meaningful placeholder. During updates preserve useful previous content when safe; do not show a blank region with no explanation. Prevent duplicate submissions where relevant and handle completion, failure, cancellation, and stale results accurately. Respect reduced motion and announce important status changes without repeatedly moving focus.

When revisiting unchanged content, reuse valid data/previews using the existing architecture where beneficial. Invalidate results when their inputs change, and prevent late responses from replacing the current selection. Do not mandate a cache size, storage backend, animation duration, or full processing rewrite for ordinary UI work.

## Menus, dropdowns, and contextual help

Dropdown/popover surfaces need enough opacity, separation, spacing, and layering to remain distinct from underlying controls. Check selected item, clipping, placement, dismissal, and keyboard operation using the framework's accessible primitives. Test the actual popup rather than only the closed trigger.

Use concise, local explanations for unfamiliar terms rather than permanent paragraphs under every control. A small graphical help icon can reveal assistance on hover and keyboard focus; provide click/touch access as needed. Keep essential instructions visible. Manage related help as one coherent overlay so switching targets replaces stale help; allow reading the content without accidental immediate dismissal. Follow project/platform delay and dismissal conventions rather than hardcoding timings from one project. Keyboard dismissal and focus should remain predictable, including Escape where applicable.

## Focused review scenarios

- **Toolbar:** the action is discoverable before hover without an independent heavy box around every label; the static title does not look actionable.
- **Mode group:** choose A → B → A and repeat the current choice; displayed content and selected indicator agree, with no inert enabled choice.
- **Disclosure/action:** press, release, cancel, and move focus; only real persistent state remains emphasized.
- **Async content:** observe initial wait, update, revisit, failure, and any cancellation relevant to the change; useful content and progress stay understandable and stale results cannot win.
- **Dropdown/help:** open over adjacent controls, move among help targets, dismiss, and use keyboard/touch alternatives; surfaces remain distinct and explanations readable.
- **Focus:** inspect mouse states and Tab/Shift+Tab focus in themes/sizes in scope; no unintended black frame, hidden focus, or loss of editing/selected cues.

Check representative instances of each changed control role. Perform one integrated pass; rerun affected checks only after changes, failures, or unresolved concerns. Describe unavailable rendering or interaction checks honestly; a rule walkthrough is not runtime UI validation.
