# Keyword Optimization Standard v3.5

## Purpose

Optimize keywords as evidence of intent coverage, not as a word-insertion exercise.

## Required keyword map

For every supplied keyword, record:

- Keyword and normalized form.
- Intent: core topic, solution, comparison, scenario, product, or question.
- Priority: core, secondary, or long-tail.
- Natural target section.
- Target count and actual count.
- Exact sentence/location after editing.
- Optimization role and reader value: why this location answers the query rather than merely containing it.
- Review-markup evidence: exact highlighted span and the paragraph or heading containing it.

Use `templates/keyword_map.md`.

## Canonical source and priority lock

1. Select the worksheet containing both `Keyword` and `Search Volume`; record its exact name and header row. Do not combine briefing tabs, duplicate tabs, or derived tabs into the priority list.
2. Default strict rule: the first 20 workbook-ranked keywords must each receive one natural exact occurrence and one yellow-highlighted exact occurrence in the marked review copy.
3. A phrase that is a typo, duplicate, unsafe request, or demonstrably incompatible with the article may be omitted only through a named exception. The exception must state the phrase, reason, owner decision, and the semantic coverage retained. It cannot silently disappear.
4. Count exact matches separately from semantic variants. Semantic coverage never satisfies an exact-match requirement by itself.
5. Do not satisfy coverage by adding a search-query table, a “people also search” block, or grouped quoted phrases. A passing placement must be a reader-facing sentence, heading, step, scenario, FAQ answer, or product explanation that would remain useful if its highlight were removed.

## Placement rules

1. Core topic keywords should appear naturally across title/H1, introduction or Quick Answer, a central solution section, and FAQ or Verdict when relevant.
2. Each main solution section should contain at least one matching core keyword, semantic variant, or scenario keyword; do not force unrelated exact matches.
3. Long-tail keywords belong in matching H2/H3 headings, `Best for` blocks, scenario examples, or FAQ answers.
4. Product keywords belong in the product's relevant decision point, not in unrelated sections.
5. Use natural variants where grammar requires them. Do not damage readability to preserve an exact string.
6. A useful exact placement is a heading, answer, step, scenario, comparison, FAQ answer, CTA, or explanatory sentence that would remain useful if the keyword were removed. A quoted search phrase, keyword table, label, or isolated insert does not qualify.
7. Map title/H1, metadata, main heading, method/scenario, FAQ, and CTA/conclusion deliberately. Do not make all placements generic body sentences.
8. Maintain a heading-role map. H1 must carry the primary intent naturally; intent-bearing H2s must carry a primary or semantic cluster; FAQ/product H3s should carry relevant long-tail or semantic wording. Procedure-step H3s should use clear verbs and inherit the parent query rather than repeat it.
9. If exact wording makes an English heading unnatural, use the natural heading and record the exact phrase in a nearby useful sentence, question answer, or approved exception. Never write headings such as missing-article or word-order fragments merely to match a workbook string.

## Count guidance

- Core keywords: normally 2–3 natural appearances, adjusted to article length and user intent.
- Secondary keywords: normally 1–2 useful appearances.
- Long-tail keywords: once when the matching search need is genuinely answered.
- Provided keyword lists shorter than 20 should be mapped in full; longer lists should prioritize the user-designated or highest-relevance set.

## Prohibited patterns

- Search-query lists in body copy.
- Keyword-dump sentences.
- Repeating exact phrases in adjacent paragraphs.
- Adding a keyword where it does not answer an intent.
- Inventing FAQ questions solely to place a phrase.
- Search-query tables, quoted phrase blocks, or "Keyword Coverage" paragraphs used as keyword placement.
- A universal exception rationale copied across multiple keywords.
- Treating every H3 as a keyword target, or treating action-step H3s as a coverage dump.

## Keyword-quality exceptions

Flag, normalize, or omit obvious typos, duplicate variants, or semantically broken phrases. Record the unique decision in the keyword report, including alternative reader-facing wording and reviewer approval. Never force a low-quality query into publishable copy or silently waive a relevant term.

## Final keyword audit

Check:

- Whole-document counts.
- Counts and placement by H2/H3 section.
- Coverage of topic, solution, scenario, product, and FAQ intent.
- Naturalness in context.
- No concentrated keyword block or keyword-free central solution section.
- Every Top-20 phrase is either PASS with a location/highlight proof or EXCEPTION with an approved rationale.
- The clean and marked copies have identical normalized text; highlights are the only intentional difference.

If keyword highlighting is requested, create a marked review copy. Remove highlights from the clean publication copy unless the user explicitly asks to retain them.
