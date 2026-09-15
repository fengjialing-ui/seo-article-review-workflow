# SEO Article Review Workflow v3.8.0

Execution authority: `workflow.json` and `EXECUTION.md`. Run `scripts/workflow_state.py` at startup and advance each configured stage with actual evidence. Do not hand-edit generated state.

Default visual scope is NAMED_SECTIONS, chosen by reader benefit and frozen in the contract; Sources does not require an image by default. Explicit user requests for ALL_H2 retain all-H2 coverage.

## Mission

Review and improve existing SEO articles into publication-ready deliverables. Preserve valuable source assets, remove only justified low-value content, and improve intent coverage, structure, evidence, product conversion, visuals, keywords, and final usability.

## Mode detection: mandatory

Use **Optimization Mode** by default when the request says review, optimize, improve SEO, revise, restructure, or update an existing article.

Use **Rewrite Mode** only when the user explicitly asks to rewrite from scratch, replace the article, discard the original, or create a new article.

Optimization Mode sequence: `Preserve -> Improve -> Expand`.

Rewrite Mode sequence: `Research -> Structure -> Draft`.

## Hard rules

1. Do not rewrite blindly. An existing article is an asset, not raw material.
2. Complete a source content asset audit before changing prose.
3. Never delete a table, case, evidence block, detailed workflow, FAQ, CTA, or product module without recording a reason and replacement plan.
4. Do not replace a complete article with an outline, framework, review memo, image plan, or short-form summary.
5. Do not substitute image placeholders, filenames, or design directions for actual image assets.
6. Treat every product as part of a product portfolio. Do not create rules around a single named product.
7. Correct unverified claims, but do not remove legitimate conversion value merely because the wording needs verification.
8. Same-level headings must share the same logic dimension and grammar pattern.
9. Keyword optimization must be section-aware and natural. Never insert keyword-dump sentences or search-query lists.
10. Do not call a deliverable publication-ready until it passes the delivery acceptance gates.
11. Create a machine-readable gate ledger before editing. A missing, failed, or unverified gate is a delivery stop - never a note to resolve later.
12. Treat the supplied keyword workbook's designated `Keyword` + `Search Volume` sheet as authoritative. Record its sheet name, priority order, accepted exceptions, exact locations, and highlighter evidence.
13. A highlighter may split only plain text runs. It must preserve hyperlinks, drawings, fields, comments, and all non-text OOXML; verify that marked and clean copies have identical normalized text after highlights are removed.
14. When a delivery contract says every main section needs visuals, list those sections explicitly. An aggregate image count never proves section coverage.
15. Run and record topic-specific SERP research before fixing the article structure. A reference article can define quality expectations, but never supplies a copyable heading outline.
16. The default retention target in Optimization Mode is 80–90% of effective source information. Any lower result needs explicit user authorization and an asset-by-asset justification.
17. A keyword exception is not a pass-by-default. It needs a unique intent analysis, a reader-quality rationale, an approved alternative coverage route, and named reviewer approval. Reusing one generic exception reason is a failure.
18. A yellow highlight marks an editorially useful optimization in the final text, not a keyword inventory, a quoted query, or an artificial sentence added only to satisfy coverage.
19. For a contract requiring one or two visuals per section, every required section needs one or two mapped visual *uses*. Reused files count only where their visual job and reader benefit are independently justified; a global image total is irrelevant.
20. Do not use white-background text cards, generic arrows, invented branded interfaces, or unreadable embedded text as a substitute for a scenario-appropriate visual.
21. A gate may show PASS only when its required evidence is complete, specific, and internally consistent with the final article. Template headings, generic phrases, and unchecked files are FAIL.
22. A release directory contains one release ID only. Do not mix records, assets, or preflight reports from prior releases.
23. A final release must include a completed editorial QA record. “PASS” is valid only with a named reviewer, date, evidence reference, and an explicit PASS for content integrity, editorial keyword quality, product suitability, visual relevance, visual aesthetics, source/claim review, document hygiene, and release-directory purity.
24. A document with placeholder copy, comments, tracked changes, empty metadata, or review notes inserted into the publish copy is a release failure.
25. The release manifest must list every expected output file. Unexpected historical files, unlisted assets, or prior-version records in the release directory are failures.
26. If a Word document cannot be rendered and visually inspected, the release remains blocked from publication. It may be saved only as `Structurally verified - visual QA pending`; it must not be called a final article.
27. Do not represent a workflow as guaranteeing editorial quality by itself. The guarantee is procedural: no item can be labelled final until the automated checks and named editorial QA both pass.
28. Run a **content-economy audit** before finalizing. Every repeated reader decision has one primary home; later repetitions must add a new action, constraint, or scenario. Remove duplicated summaries, repeated rights warnings, repeated tool limits, and duplicate source lists. If final body length grows by more than 10% over the source, record a section-by-section reason for the expansion.
29. Maintain a heading-role map for every H1, H2, and H3: `primary keyword`, `semantic keyword`, `long-tail question`, `action step`, `reference`, or `structural`. Every intent-bearing H1/H2 and every FAQ/product H3 needs a natural keyword or semantic-query role. Action-step H3s may remain action-led only when their parent H2 owns the query and the map records the reason.
30. Natural language outranks an awkward exact keyword in a heading. Preserve the natural title, then place the exact query in a useful nearby answer, FAQ, or exception route; never damage grammar to satisfy a string match.
31. When the contract says “every section”, visual scope is **all H2 headings, including Sources when ALL_H2 is explicitly requested**, unless the contract lists an explicit approved exception with a reader-value reason. A manually shortened required-section list is not allowed.
32. Sources are a single, deduplicated, claim-linked source system. Do not leave an old label-only list beside a new URL list. Every version-sensitive source must record current verification date, official URL, and the claim or section it supports.
33. Verify the live availability state of every recommended product immediately before release. `Coming soon`, beta/demo-only, waitlist, unavailable region, or degraded service states prohibit a normal “try/use now” CTA; write the limitation prominently and give a live alternative or wait-state action.
34. Build marked copies from `templates/review_highlight_map.example.json` with `scripts/targeted_keyword_highlighter.py`. Do not globally highlight every occurrence of a Top-20 term: yellow must show the approved editorial placement, especially headline-level optimizations, not all inherited source mentions.
35. When a named core conversion product does not support the article's primary task but has a verified lawful adjacent route, it must receive a Boundary-sensitive core conversion `Ultra Tips` H2, not an exclusion-only or adjacent-only mention. The required module contains the truthful boundary, three best-for scenarios, not-for route, four-to-six steps, current status, safe CTA, one mapped product visual, and two further decision touchpoints. A missing module is a release-blocking product failure. If no truthful adjacent route exists, block and escalate; do not invent functionality.
36. Determine core-conversion status from the current brief and the retained project product policy before source audit. A user does not need to repeat an already-established project core product in every request. Record every such product in the delivery contract and `core_conversion_products` manifest field; if no policy or brief identifies one, explicitly record `none` rather than silently assuming a product is non-core.
37. Classify each named core conversion product against the exact primary task using a current official feature URL before drafting. `direct_supported` requires a direct-solution heading, article-visible official URL, scenarios, workflow, limitation, and CTA; it forbids any `Ultra Tips`, adjacent, or “does not support the primary task” route for that product in both article and release evidence. `adjacent_authorized_route` alone permits Ultra Tips. `no_truthful_route` blocks release pending an approved alternative. Re-run this route check immediately before delivery to catch new launches and stale templates.
38. Before opening or editing an article, execute `START_HERE.md` in full and generate `workflow-state.json` with actual loaded-file/input hashes. A release without that record fails preflight. The user does not need to repeat the fixed execution contract in each request.

## Minimum stage gates

`Bootstrap -> Delivery Contract -> Source Audit + Content-Economy Audit -> SERP & Intent Research -> Structure Plan + Heading-Role Map -> Product Portfolio + Core-Conversion Route Check + Availability Check -> Keyword Map -> Visual Map -> Edit -> EEAT + Source De-duplication -> Regression -> Render QA -> Release`

## Release lock

Final delivery is permitted only when `templates/gate_ledger.md` shows **PASS** for all required gates, the preflight report is PASS, and the following artifacts share one release ID:

- clean article, marked review copy (when requested), and source-audit record;
- keyword map, product map, visual map, and independent images;
- rendered QA evidence, or the exact fallback status `Structurally verified - visual QA pending`.

Never call a release final/publication-ready when fallback status is present.

## Delivery default

Unless the user requests otherwise, a final publication package contains:

- A publication-ready article document with full body content, embedded visuals, tables, links, FAQ, and CTA.
- Separate image assets used in the document.
- A concise keyword optimization record.
- A concise visual asset manifest.

Do not substitute review notes for the final article. Provide review notes only when requested or as a separate supporting artifact.

## Minimal user instruction contract

When the user says: `请使用 SEO Article Review Workflow v3.8.0 对附件文章进行完整回审，默认采用 Optimization Mode，保留原文有效信息，不得改写成提纲或缩水稿。` and provides an original DOCX plus a canonical keyword XLSX/sheet, treat this as authorization to execute the complete v3.8.0 process and deliver the complete package above. Do not ask the user to restate stage gates, visual requirements, evidence records, clean/marked-copy behavior, or final acceptance criteria.

If the user also provides a reference article, it is a **quality benchmark only**. Inspect its depth, decision usefulness, visual integration, table/FAQ/CTA quality, and publication finish, but do not copy its heading order, section sequence, wording, or outline. The actual structure must come from the new article's SERP and intent research.

The user only needs to supply additional instructions when they materially change scope: a required product/brand, target audience/locale, a specific output language, a legal/compliance limitation, or an explicit exception to the default delivery contract.
