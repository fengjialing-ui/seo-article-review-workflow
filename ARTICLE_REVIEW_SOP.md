# Article Review SOP v3.8.0

Default visual scope is NAMED_SECTIONS, chosen by reader benefit and frozen in the contract; Sources does not require an image by default. Explicit user requests for ALL_H2 retain all-H2 coverage.

## 0. Delivery Contract and Mode Detection

Before reviewing content, record:

- Required final files and whether the article must be immediately publishable.
- Whether keyword highlighting belongs in a review copy, a publish copy, or both.
- Required image count, asset format, independent image delivery, and visual direction.
- Required product(s), product category, conversion purpose, CTA, internal links, or evidence requirements.
- Optimization Mode or Rewrite Mode.
- Release ID, source article path/version, canonical keyword-sheet name, and required priority-keyword rule.
- The exact list of sections that require visuals. If the request says “every section,” list **every H2 after the final structure is set, including Sources when ALL_H2 is explicitly requested**. An exception must name the heading, reader-value reason, and approver; no implied exception exists.
- The required review-markup behavior. Default: yellow highlights only in the marked copy; clean copy has no yellow highlights; the two copies must have identical normalized text.
- Whether the clean article must include a CMS-ready SEO metadata block: SEO title, meta description, URL slug, primary keyword, and secondary-keyword cluster. Default: yes when the article is delivered as a Word handoff.
- The reader persona, intended device/context, preferred visual style, prohibited visual styles, and the concrete rule for one or two visual uses per required section.

If the user asks for optimization/review, select Optimization Mode. Do not proceed to a full rewrite without explicit authorization.

## 1. Content Preservation Audit (mandatory before editing)

Create an inventory using `templates/content_asset_audit.md`.

Evaluate every substantial source asset:

- Search-answer modules: introduction, Quick Answer, decision guidance, FAQ, Verdict.
- Decision assets: tables, comparison matrices, checklists, workflows, scenarios.
- Authority assets: data, source citations, expert boundaries, verified claims.
- Conversion assets: product explanations, product workflows, use cases, benefits, limitations, CTAs.
- Visual assets: original images, diagrams, captions, Alt text, product screens.

Assign one action only: **Keep**, **Merge**, **Refine**, **Relocate**, **Replace with an equivalent**, or **Delete**.

Deletion is permitted only for true repetition, empty generality, unsupported claims, stale facts, or content with no search, decision, evidence, or conversion value. State the reason and preserve an equivalent asset where required.

## 2. SERP, Topic, Intent, and User Journey Research

Before proposing headings, create `templates/serp_structure_evidence.md` from a dated, topic-specific SERP review. Record the query, location/language, result type, recurring reader questions, solution categories, authority sources, and gaps worth covering. Do not copy a competitor or reference article's heading sequence.

Then create a structure plan that maps each proposed section to one reader decision, the SERP/intent evidence that justifies it, source assets retained there, a keyword cluster, a product role if applicable, and its visual job. A sample article may be used only to set quality expectations such as depth, decision usefulness, tables, figure integration, and CTA clarity.

Identify:

- Primary search intent and secondary intents.
- User scenarios, urgency, pain points, and decision needs.
- Source states or problem states that require different routes.
- The minimum answer a skimming reader needs before deeper detail.

Build the article as a user journey. Example pattern:

`Diagnose state -> Choose solution category -> Follow method -> Validate outcome -> Preserve/share -> FAQ/CTA`

## 3. Structure Review

Check:

- One H1 only.
- A Quick Answer that actually resolves the first decision.
- One structural dimension per heading level.
- Parallel grammar at the same heading level.
- Related solutions grouped under a common category instead of duplicated as flat, competing sections.
- A consistent method pattern such as: `Best for -> Why it fits -> Steps -> What to check -> Product/CTA -> Limits`.

### 3.1 Content-economy and heading-role gate

Before drafting, make two maps:

1. **Decision-owner map.** Each H2 owns one reader decision. If Quick Answer, a chooser, an FAQ, and Verdict repeat the same decision, retain the most useful version and make the others link back, summarize in one sentence, or answer a genuinely new decision.
2. **Heading-role map.** Classify every final H1/H2/H3 as primary keyword, semantic keyword, long-tail question, action step, reference, or structural. H1, intent-bearing H2, and FAQ/product H3 must have a deliberate keyword or semantic-query role. Step H3s may be action-led; they must not become query dumps.

During final regression, remove repeated rights warnings, repeated source-first advice, repeated verification instructions, repeated product boundaries, and duplicated source lists unless the later instance supplies a new scenario, action, or legal constraint. Any final expansion above 110% of source words needs a recorded value reason by section.

Do not keep two sections separate merely because they use different tools if they solve the same stage of the same user journey. Create one category, then distinguish tools/scenarios underneath it.

## 4. Solution Logic Review

Classify each solution before drafting:

1. **Required/source-level solution**: fixes the source state or enables later work.
2. **Direct solution**: solves the reader's central problem at that decision point.
3. **Alternative solution**: solves the same problem in a materially different scenario.
4. **Adjacent solution**: supports a related workflow step.
5. **Boundary-sensitive solution**: useful only after limitations and risks are clear.

Every solution must include a concise `Best for` block with three concrete, recognizable scenarios or long-tail situations. Include one or two boundary cases when relevant.

## 5. Product Portfolio, Placement & Conversion Review

Use `PRODUCT_RECOMMENDATION_STANDARD.md` and `templates/product_portfolio_map.md`.

For each product, verify role, problem fit, placement, evidence, differentiated value, limit, alternative, and CTA. A product should appear only where the reader has enough context to understand why it is recommended.

If a named core conversion product does not support the primary task, classify it as **Boundary-sensitive core conversion (Ultra Tips)** rather than silently downgrading it to an adjacent/exclusion mention. First explain the unsupported primary task. Then build a dedicated `Ultra Tips: [Product] for [truthful authorized supported route]` H2 with three best-for scenarios, not-for/escalation, four to six steps, verified value/status, privacy/rights boundary, a safe CTA, a mapped product visual, and two further lightweight decision touchpoints. This module is a protected conversion asset. A factual limitation improves the recommendation; it never justifies replacing the product path with a one-sentence disclaimer. If no truthful adjacent route exists, stop the product decision and request an approved alternative rather than making a false recommendation.

If the current official evidence shows that a named core conversion product **does** support the primary task, classify it as `direct_supported` and use the direct-solution route. Give it a named direct method/solution heading, current official feature link in Sources, three scenarios, workflow, limitation, and CTA. Do not use or retain an Ultra Tips module, adjacent label, or “not supported” boundary for that product. Recheck this classification immediately before release because new feature launches can invalidate a historic route.

Immediately before release, verify live availability, account requirement, beta/demo/coming-soon status, pricing, region, and material processing limitations on an official source. A product that is unavailable, coming soon, demo-only, or may return an unchanged result must not receive a conventional “try now” CTA.

Keep direct-solution conversion content strong: scenario-specific value, practical workflow, comparison/selection aid, constraints, and a next action. Fact-checking should improve claims, not erase persuasive utility.

## 6. Keyword Review

Use `KEYWORD_OPTIMIZATION_STANDARD.md` and `templates/keyword_map.md`.

Map each keyword to search intent, article section, target count, and natural sentence. Audit distribution by section, not only by whole-document totals.

Before writing, select the canonical workbook sheet and lock the Top 20 priority list. For each listed item, record its intent, planned optimization role (H1, metadata, H2/H3, Quick Answer, method, scenario, FAQ, CTA, or conclusion), exact final location, actual count, and marked-copy highlight evidence. A blank or generic location is a failed gate.

An exception is allowed only for a typo, duplicate, semantically broken query, legal/brand-risk term, or a demonstrably harmful exact phrasing. It must include a unique reason, semantic route, reader-facing substitute, reviewer approval, and proof that it was not used to evade a relevant placement. Never replace keyword coverage with a query table, quoted query block, or a sentence that would not remain useful if the highlight disappeared.

## 7. Visual Asset Review and Production

Use `standards/VISUAL_ASSET_STANDARD.md` and `templates/visual_asset_map.md`.

Plan actual visuals before final composition. Every main content section needs a visual role: problem identification, workflow, scenario comparison, method operation, product experience, or outcome/archiving.

Preserve effective original visuals. New visuals should complement a missing task, not replace useful assets merely for stylistic uniformity. For every visual use, record the user scenario, visual job, exact insertion point, filename, source/rights status, visual-style rationale, true Alt text, caption, and rendered-page QA. Require one or two visual uses per named section when the contract says so.

## 8. EEAT and Evidence Review

Check that claims are proportionate and sourced where needed.

- Retain useful existing evidence, case material, technical boundaries, and authority references.
- Use current primary or official sources for version-sensitive product claims.
- Mark illustrative workflows as examples, not claimed customer outcomes.
- Add sources where a reader needs a factual basis to choose a solution.
- Merge all source material into one deduplicated, reader-readable source system. For each version-sensitive claim, record official URL, verification date, claim scope, and final insertion point. A label-only source list plus a later URL list fails.

## 9. Edit and Regress

Implement approved actions from the source asset audit. After editing, compare the revised article to the source:

- Effective word-count change and explanation for material reduction.
- Preserved/replaced tables, cases, workflows, FAQ, evidence, visuals, and product modules.
- No accidental loss of decision depth or product conversion logic.

If source effective-information retention drops below 80%, stop and require explicit authorization plus an asset-by-asset reduction rationale. A lower threshold may be used only when the user expressly requests a short version.

## 9.5 Marked-copy integrity gate

Create the clean copy first. Build the marked copy from it with a run-safe highlighter. Do not rebuild a whole paragraph from `paragraph.text`, because this can duplicate or destroy hyperlinks, drawings, fields, and formatting. Compare clean text to marked text after stripping highlights; the normalized text and media relationship counts must match exactly.

## 9.6 Final editorial QA gate

Complete `templates/final_human_qa.md` after all automated checks and after rendered-page review. The reviewer must inspect the entire clean and marked article, not a sample page. A PASS requires evidence for:

- retention of source assets and article depth;
- reader-first keyword placement and accurate yellow highlighting;
- product fit, factual boundary, official evidence, and CTA;
- every required visual use: concrete scenario, reader fit, aesthetic quality, caption/Alt accuracy, and no white text-card, generic-arrow, watermark, or invented-branded-UI failure;
- all rendered pages: figure/caption adjacency, no clipping, no blank pages, no broken tables, and no accidental markup in the clean copy;
- actual source/official-link verification and a single-release package.

The reviewer may mark **BLOCKED**, never “PASS with issues.” A render failure automatically produces `Structurally verified - visual QA pending`, not a final release.

## 10. Final QA and Delivery

Run the complete checklist in `standards/DELIVERY_ACCEPTANCE_STANDARD.md`.

Run `scripts/review_preflight.py` against the release manifest and attach its PASS output to the gate ledger. It must validate the evidence files rather than only their existence. A partial pass, a manual promise, or an image-count-only check is not sufficient.

Do not label an output “final” or “publish-ready” if it is an outline, a review memo, a visual plan, a document with placeholders, or an artifact that has not passed the available visual/layout checks.
