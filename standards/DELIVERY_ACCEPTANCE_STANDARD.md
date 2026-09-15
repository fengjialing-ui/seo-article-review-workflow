# Delivery Acceptance Standard

Execution version and reviewer policy: workflow.json and EXECUTION.md.

Default visual scope is NAMED_SECTIONS, chosen by reader benefit and frozen in the contract; Sources does not require an image by default. Explicit user requests for ALL_H2 retain all-H2 coverage.

## Publication-ready means all required deliverables exist

A final package must contain, as required by the delivery contract:

- Complete publication-ready article document, not a framework or audit memo, with a CMS-ready metadata block when required by the delivery contract.
- SEO metadata, full body content, table(s), FAQ, sources, and CTA where applicable.
- Embedded actual images with captions and Alt text.
- Independent image asset files.
- Keyword optimization record.
- Visual asset manifest.

Review notes, image plans, and audit documents are supplementary only. They never substitute for the article.

## Hard release stop

Do not hand off a final release when any of the following is missing or failed: source audit, dated SERP/structure evidence, canonical keyword source, Top-20 keyword disposition, marked/clean text-integrity comparison, product map, per-section visual-map PASS rows, independent assets, release-directory purity, preflight report, or render evidence/fallback label. A reviewer must fix the defect or label the release blocked; “draft ready for review” is not a substitute for gate status.

The release must also include a complete final editorial QA record and an exact manifest of every file in the release directory. A named reviewer must mark every required criterion PASS. No criterion may be marked “pass with issues.”

## Content acceptance

- One H1; heading hierarchy and same-level logic are consistent.
- Quick Answer, methods, decision guidance, FAQ, and Verdict answer their intended needs.
- Source asset audit is complete and no protected asset was accidentally lost.
- Effective-information retention is 80–90%, or a lower result has explicit user authorization and asset-level justification.
- The structure plan is backed by current topic-specific SERP/intent evidence, not copied from a reference article.
- No empty sections, placeholder copy, keyword dumps, or duplicated explanations.
- A content-economy audit identifies each repeated decision, its single primary owner, and the disposition of duplicates. Unexplained final expansion above 110% of source words fails.
- A heading-role map covers each H1/H2/H3; core H1/H2 and FAQ/product H3 have natural keyword or semantic-query roles, while action H3s are explicitly justified as action-led.
- Sources are one deduplicated, claim-linked list; version-sensitive entries have an official URL and current verification date.
- Source and final word counts are recorded from the actual documents; a final word-count drop below 80% fails unless explicitly authorized.

## Product acceptance

- Product portfolio map is complete.
- Every product has a role and logical placement.
- Direct solutions retain `Best for`, scenario value, workflow, evidence, limitation, and CTA.
- Competing or adjacent products are grouped and differentiated by scenario.
- Version-sensitive claims are verified or safely generalized.
- Product availability, beta/demo/coming-soon state, and CTA suitability are verified immediately before release.
- A named core conversion product classified `direct_supported` has a direct-solution heading, three scenarios, workflow, limitation, CTA, and current official feature URL visible in the article's source system. It has no Ultra Tips/adjacent/not-supported route in article or release evidence.
- A named core conversion product that does not support the primary task is not downgraded to an exclusion. Where a verified lawful adjacent route exists, a dedicated Ultra Tips H2 contains the truthful boundary, three scenarios, not-for route, four to six steps, status-safe CTA, mapped product visual, and three decision touchpoints. Where no truthful route exists, the product decision is blocked and escalated rather than misrepresented.

## Keyword acceptance

- Keyword map records target and actual locations/counts.
- Core coverage is distributed across the reader journey.
- Main solution sections do not have unexplained keyword gaps.
- Long-tail usage answers the relevant user need.
- Typo/low-quality keyword exceptions are documented.
- Every keyword exception has a unique rationale, an alternative reader-facing route, and reviewer approval; generic exception batches fail.
- Highlighted wording is useful prose in its location; query labels, keyword tables, and artificial coverage sentences fail.
- Marked review copy and clean publication copy are clearly separated when both are requested.
- Removing yellow highlights from the marked copy produces text-identical clean content; no duplicate text, missing hyperlink, altered media, or altered source list is introduced.

## Visual acceptance

- Required visual count and section coverage are met.
- All images are real assets, embedded, and independently packaged.
- Every image has filename, Alt, caption, and insertion point.
- Every required section has one or two mapped visual uses when the contract requires this; when the contract says “every section,” required means every H2, including Sources when ALL_H2 is explicitly requested unless an approved exception is recorded.
- Each visual use has an audience/scenario rationale, style/rights status, and distinct purpose; white text cards, generic arrows, decorative reuse, and invented branded interfaces do not qualify.
- Original useful visuals are preserved or replaced only with documented equivalence.
- Rendered pages show no clipping, overlap, stretch, broken tables, orphaned captions, or blank-page artifacts.

## Technical/document acceptance

- Comments and tracked changes are removed or intentionally retained per contract.
- Links and source citations work.
- Tables have readable geometry and repeat headers where appropriate.
- Document has passed render-to-image review where the environment supports it.
- If rendering is unavailable, mark the result **Structurally verified - visual QA pending**. Do not call it publish-ready.
- `templates/gate_ledger.md` and `scripts/review_preflight.py` report PASS for the same release ID.
- No comments, tracked changes, or review-only content remain in the clean publication copy.
- Every file in the release directory is declared by the manifest; no historic release records or unlisted files are present.

## Revision regression gate

When responding to user feedback:

1. State the exact defects being repaired.
2. Re-run all affected checks, including preservation and delivery gates.
3. Confirm that the repair did not remove original assets, product conversion, images, tables, or keyword coverage.
4. Deliver the final article first; supporting notes are secondary.
