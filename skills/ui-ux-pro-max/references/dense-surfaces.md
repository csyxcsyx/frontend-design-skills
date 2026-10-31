# Dense workspaces, stable detail and relationship views

Load only relevant sections for dense cards, detail expansion or data visualization. Use actual content and platform conventions; do not install a diagram library, force three columns or turn every screen into a graph.

## Content-sized layout without clipping

Use the available workspace and actual text measure, not oversized uniform cards with tiny centered text or empty placeholder cells. Establish suitable min/max widths and heights, readable typography and consistent peer alignment. Wrap long paths/identifiers or offer an accessible full-value detail; do not clip meaningful content to hide layout errors. Include badges, corner controls and hover/focus decorations in padding and overflow checks.

Compact means removing redundant gaps and repeated information, not shrinking text or adding filler. Avoid needless page-level horizontal/vertical scrolling on a desktop workspace while allowing local scrolling for genuinely long details/source or large canvases. On narrow screens permit natural vertical flow; do not force one-screen fit, indiscriminately hide overflow or discard data. Check smaller windows, zoom and representative longest content.

Reserve stable anchors for changing status labels, counters and controls. Independent left/right groups must not pull a centered element sideways as their text changes. Remove a redundant default/configuration label instead of preserving an unstable status strip for decoration.

## Details without disrupting the grid

If expanding one card stretches a whole row or scatters its siblings, use an appropriate drawer, dialog, side pane or dedicated detail view. Inline expansion remains valid where it helps the actual flow. Keep the originating list/grid stable; remember selection, filter, scroll and focus as needed. Use local scrolling for long detail, predictable closing, and restore focus to the trigger. Replace or close stale detail when its underlying result changes. Avoid stacking a second modal to show an item's evidence; navigate within the same detail surface where appropriate.

## Honest overview and full view

Use a compact overview for orientation and a clear action to open a focused full view when the actual visualization is too large. A representative subset or aggregation must not imply exhaustive records; totals, filtering and the route to full data must stay accurate. Do not paginate a small diagram into nearly empty pages just to fit a fixed template.

If the user requests a blurred or symbolic teaser, treat it as illustrative navigation, not a depiction of actual evidence. Avoid fake nodes, relationships or counts presented as data; retain a clear opening action and appropriate accessible description. Never copy this decorative-preview choice to every chart. The full view must use the real data, with readable labels, appropriate search/filter and access to the needed records. A treemap's short label should fit its cell; aggregate tiny categories meaningfully rather than render empty cells or illegible text.

## Graph geometry and interaction

Size nodes from content within practical bounds; preserve graph semantics and enough whitespace to distinguish and target edges. Route connectors through sensible ports, behind opaque node content, without clipping labels or drawing over controls. Meaningful categories may differ in shape/icon/subtle decoration, but legibility and the same semantic style take precedence over novelty. Typographic watermarks requested for categorization are decoration, not icon substitutes or extra state; keep them low contrast and away from readable labels.

Highlight relationships by node/edge identity and intended direction, not merely by matching color. Define and check hovering on each side separately; grouping may deliberately be asymmetric. The hit region can be easier to target than a hairline, but must not activate an unrelated edge or block neighboring nodes. A compact legend can explain categories; do not remove all context or rely on color alone. Show source/uncertainty honestly; an inferred association is not a verified call/dependency.

Provide coherent pan/zoom/full-view behavior for the platform and requested workflow. Do not hijack page scrolling outside the intended canvas. Fit/reset uses the actual full bounds, including labels, padding and controls, rather than stale dimensions or only the initially visible nodes. Preserve relevant filters/selection and focus when entering/leaving the view; provide keyboard/access alternatives as appropriate. Use virtualization, aggregation or another renderer only when scale/performance evidence warrants it; aggregation does not delete underlying records.

## Evidence checks

Use single/empty/dense graphs, long labels, corner badges, changing counters, different windows/zoom and the themes in scope. Inspect connectors behind nodes during motion/hover, edge targeting and directional highlighting, fit/reset, full-view entry/exit and stale-result replacement. Check that a detail action does not disturb sibling cards and that added decoration cannot intercept input. Report actual inspection and measured performance separately from design intent; no universal node count, zoom range, renderer or benchmark is prescribed.
