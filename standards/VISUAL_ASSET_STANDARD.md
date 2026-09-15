# Visual Asset Standard v3.5

Default visual scope is NAMED_SECTIONS, chosen by reader benefit and frozen in the contract; Sources does not require an image by default. Explicit user requests for ALL_H2 retain all-H2 coverage.

## Core rule

Actual visual assets are part of the article deliverable. A placeholder, image plan, filename suggestion, or generic collage is not a delivered image.

## Visual strategy before production

For every main content section, define one primary visual job:

- Problem identification.
- Scenario overview.
- Decision workflow.
- Method operation.
- Before/after or comparison.
- Product experience.
- Outcome, preservation, or sharing.

Create a visual map with `templates/visual_asset_map.md` before making or sourcing images.

## Minimum asset requirements

- Introduction: pain point or outcome visual when it improves comprehension.
- Quick Answer: compact decision/workflow visual.
- Every main solution/method: at least one scenario or method visual.
- A featured direct-product section: a product-experience, workflow, or result-comparison visual.
- Each asset must be embedded in the final document and separately delivered as an image file.

The delivery contract must define whether a summary, FAQ, Verdict, and Sources require a visual. Do not leave “every section” ambiguous. If the user requests every section, the default is **one or two visuals per every H2 heading**, including decision guidance, mistakes, FAQ, Verdict, and Sources; exclusions require an explicit approved exception.

## Best-for and scenario visuals

- Every main solution must have a concise `Best for` block containing three recognizable scenarios.
- Where several scenarios help readers self-identify, use one visual-first scenario overview with only short labels.
- Do not use a white-background text-heavy card or generic arrow graphic when a concrete user scenario, product state, clip state, or before/after visual would serve better.

## Steps: default image pattern

- Default: one method = one compact composite step visual, for example `Find -> Select -> Fix -> Export`.
- Use step-by-step individual images only when the operation is high risk, materially different at each step, or needs precise UI confirmation.
- Do not create multiple large images that repeat the same explanation.
- Preserve useful original visuals; additions should fill a new visual task, not replace them only for style consistency.

## Quality requirements

Each asset needs:

- A unique filename suitable for SEO.
- Accurate, descriptive Alt text; no keyword stuffing.
- A caption that explains the reader benefit.
- A documented insertion point and corresponding section.
- A visual style appropriate to the audience, product type, and article topic.
- The intended reader/persona and specific decision or task the visual helps them complete.
- Source, generation, or licensing status.
- No placeholder text, unreadable dense text, irrelevant scene, watermark, clipped subject, or invented branded UI.

## One-to-two visual-use rule

When the delivery contract requires one or two visuals per section, create a row for every visual **use**, not merely every unique file. Each named section needs one or two appropriate uses with a distinct reader benefit. Reusing a file is permitted only when the map states why the same scene serves that different section; repeated decorative reuse does not count. White-background text cards, generic arrows, and text-heavy diagrams do not satisfy a scenario visual requirement.
- Asset filename must be the actual independently delivered file name, not an aspirational name in a plan.

## Visual QA

Verify:

- Asset count and independent files match the visual map.
- Image actually appears in the intended section.
- Correct inline anchoring, readable size, caption adjacency, and Alt text.
- No crop, stretch, overlap, blank page, or table collision in rendered output.
- Summary and method visuals serve distinct purposes.
- The visual map has one PASS row for every required section, and every row has a matching embedded image and matching independent file.
