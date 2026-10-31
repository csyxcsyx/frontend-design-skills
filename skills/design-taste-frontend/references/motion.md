# Purposeful motion

Read only when motion contributes to the brief. Preserve upstream Taste's emphasis on motivated movement, cleanup, and client-side isolation while treating its library choices as optional.

Choose the smallest mechanism already suitable for the project: CSS for simple transitions, the installed UI animation system for component states, and a scroll library only for a justified complex sequence. Before adding an effect, identify its purpose: feedback, hierarchy, explanation, or state continuity. Decorative motion should not block reading or input.

- Use transform/opacity when they express the effect well; avoid layout work in continuous frame loops and update motion values without rerendering the full UI on each frame.
- Restrict transitions to intended properties instead of `transition: all`. Hover fades should be prompt and interruptible; changing targets must not leave stuck highlights or invisible layers intercepting input.
- Keep content surfaces opaque over connectors/decorations; animate a separate highlight or decoration rather than fading the whole node/card. Verify counters, labels, spinners and entry/exit states do not cause layout jumps.
- A requested primary action may use a restrained breathing/attention effect, but it is not a default for every button. Preserve a clear readable hit target, pause irrelevant offscreen motion, and provide a reduced-motion/static state.
- Scope selectors and animation ownership to the component. Different engines can coexist on separate targets; do not let them control the same property on the same element.
- Clean up listeners, observers, timelines, and temporary styles on unmount and when media conditions change. Test repeated navigation and development-mode remounts.
- Honor reduced motion at every intensity. Content remains visible and usable when animation is disabled, unsupported, or fails; essential content must not remain at opacity zero.
- For pinned stacks, provide a normal-flow fallback and check focused content is not hidden by overlays or sticky headers. Avoid gratuitous full-screen pinning on touch devices.
- For horizontal pans, recompute travel from the actual container after resizing or font/image loading; handle non-positive travel. Provide keyboard access and a normal-flow or ordinary scrolling reduced-motion/mobile fallback. Simply skipping the JS while keeping overflow hidden can make content unreachable.
- For image/video reveals, reserve dimensions and prevent layout shift. Provide pause/stop for moving content where needed, and avoid autoplay that competes with reading.
- Use framework-appropriate browser boundaries. Next.js client components are one implementation, not a cross-framework directive.

Upstream snippets are sketches, not a drop-in verified library. Check current official API documentation and installed versions before implementing a requested complex effect. Report performance measurements only when actually collected.
