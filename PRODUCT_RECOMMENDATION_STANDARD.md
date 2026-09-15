# Product Portfolio, Placement & Conversion Standard v3.5

## Purpose

Review all products, services, tools, and product categories in an article as a portfolio. The goal is accurate, useful, scenario-matched recommendation and conversion - not arbitrary mentions and not single-product bias.

## Product roles

Classify every recommended item:

| Role | Definition | Placement rule |
|---|---|---|
| Required/source-level | Enables all later work or resolves the source state. | Explain before downstream software/products. |
| Direct solution | Solves the reader's primary problem at the current decision point. | Recommend prominently after diagnosis and before CTA. |
| Alternative solution | Solves the same problem in a materially different scenario. | Compare under the same solution category. |
| Adjacent solution | Helps an associated step, not the main problem. | Place only at its relevant step. |
| Boundary-sensitive | Useful only when risk, limits, or prerequisites are understood. | State limitation first, then recommend conditionally. |
| Boundary-sensitive core conversion (Ultra Tips) | A required conversion product does not support the article's primary task, but has a verified, lawful, adjacent use that genuinely helps the same reader. | State the primary-task boundary first, then give the product a dedicated `Ultra Tips` H2 with an authorized adjacent workflow. It may never be reduced to an exclusion sentence. |

## Mandatory product portfolio map

For each item, record:

1. Name and product/category type.
2. Role.
3. Specific problem and lifecycle stage solved.
4. Three `Best for` scenarios.
5. One or two `Not best for` or escalation scenarios.
6. Differentiated value versus alternatives.
7. Required evidence or verified official claim.
8. Required placement: diagnosis, method, step, comparison, FAQ, or Verdict.
9. CTA and expected reader action.
10. Limitation, privacy, cost, compatibility, or risk constraint.

When the client identifies a product as a **core conversion product**, also record whether it directly supports the article's primary task: `direct_supported`, `adjacent_authorized_route`, or `no_truthful_route`. A product that does not support the primary task is not automatically optional or removable.

Use `templates/product_portfolio_map.md`.

## Mandatory capability classification before drafting

Before a product route is chosen, record the **exact primary task**, a current official feature URL, the verification date, the supported input/output scope, and the classification. New product launches and current official feature pages override legacy templates, prior article wording, and an earlier capability decision.

- `direct_supported`: the official evidence states that the product performs the article's primary task for the relevant authorized input. Use the direct-solution route.
- `adjacent_authorized_route`: the official evidence supports a lawful, reader-relevant neighboring task but not the primary task. Use Ultra Tips.
- `no_truthful_route`: no current official evidence supports either the primary task or a lawful adjacent route. Block the product decision and request an approved alternative.

Do not infer “adjacent” merely because the product is new, the name of the feature differs from the query, or an older template lacks the feature. Conversely, do not classify a generic editing capability as direct support unless the official evidence covers the actual reader task and input scope.

## Placement rules

- Do not introduce a product until the reader understands the problem it solves.
- Do not place competing products in unrelated standalone sections when they solve the same stage; create one category and split by scenario.
- Do not inject a product merely because it is available or commercial.
- Put a direct solution near the relevant decision point; put adjacent tools near the relevant workflow step.
- Keep CTA after the reader has seen fit, value, workflow, and relevant caveats.
- If an article covers several products, every product needs a distinct scenario, benefit, or role. Otherwise consolidate the discussion.

## Conversion block: direct solutions

Every direct-solution product block must contain:

1. The reader problem and `Best for` scenarios.
2. Why this product/category fits that scenario.
3. A practical workflow or selection aid.
4. A proof point: verified feature, evidence, comparison, case, or observable outcome criterion.
5. A limitation and escalation/alternative path.
6. A specific CTA: test, compare, download, consult, or start a short trial.

The product map must state the exact final heading/paragraph location and a current official evidence URL. A one-sentence product description, a generic “consider” recommendation, or a map with blank scenario, CTA, or evidence fields fails this gate.

Do not weaken conversion into generic “consider this tool” language when the product genuinely fits. Equally, do not use unsupported superlatives, false guarantees, or claims that erase necessary prerequisites.

### Direct-support route lock

For every named core conversion product classified `direct_supported`:

1. Use a dedicated direct-solution H2 or equivalent method heading that names the product and is recorded as `direct_solution_heading` in release evidence, with three to six reader-facing `direct_workflow_steps` evidenced in the article.
2. Put the current official feature URL in the article's claim-linked source system, not only in an internal note.
3. Record three best-for scenarios, not-best-for/escalation, differentiated value, practical workflow, limitation, availability check, and CTA.
4. Omit the `ultra_tips` evidence object entirely. The article and records must not pair that product with `Ultra Tips`, `adjacent`, or wording that says it does not support the primary task.
5. If evidence changes before release, reclassify the product and regenerate all product touchpoints; never patch only the heading or only the evidence record.

Any conflict between `direct_supported` and an Ultra Tips/adjacent route is a release-blocking failure.

## Mandatory Ultra Tips route for a core conversion product that does not support the primary task

This rule applies whenever the brief, delivery contract, or product map marks a named product as a core conversion product and its exact current feature does **not** solve the article's main task.

### Required editorial logic

1. Say clearly and early that the product does not perform the primary task. Never imply it can remove a stock-preview mark, bypass a licence, process an unsupported format, or otherwise perform an unavailable feature.
2. Find the nearest **verified, lawful, reader-relevant** use the product does support: for example, an authorized still image rather than an unsupported video, URL, protected preview, or unlicensed third-party file.
3. Create one dedicated H2 whose heading contains `Ultra Tips`, the product name, and the truthful supported route. It must sit after the reader has understood the primary-task boundary, not as a detached advertorial opener.
4. Give that H2 the same conversion depth as a direct-solution block: three concrete `Best for` scenarios, `Not for`/escalation, four to six ordered workflow steps, differentiated value, official proof/current status, privacy or rights boundary, and a specific next action.
5. Re-enter the product naturally in at least two additional decision points - a chooser/decision guide and an FAQ or Verdict - while keeping the dedicated Ultra Tips H2 as the single detailed owner. Do not repeat the full workflow in each location.
6. Map at least one scenario-appropriate product visual to the Ultra Tips H2. It needs an independent asset file, true Alt text, a caption, and a reader-facing purpose; invented branded UI or a generic text card does not qualify.
7. If the product is coming soon, beta, demo-only, region-limited, or may return no result, keep the conversion module but use a non-promissory action such as checking current eligibility/availability, monitoring release, or preparing a permitted asset. Do not use “try now,” “start now,” or equivalent production-ready language.

### Required evidence fields

For this route, the release evidence must include `core_conversion_product: true`, `primary_task_support: "adjacent_authorized_route"`, and an `ultra_tips` object with the exact H2, boundary disclosure, verified supported route, three best-for scenarios, not-for route, four-to-six steps, status statement, CTA text, three distinct touchpoints, and the mapped product visual filename.

### Fail conditions

The product gate fails when any of the following is true:

- A core conversion product is labelled only `Adjacent`, `Boundary`, `exclusion`, or `not applicable` without the required Ultra Tips evidence.
- The article has only a one-sentence limitation, generic “consider” text, or an exclusion paragraph in place of the module.
- The module claims the unsupported primary feature, omits the authorized supported route, has fewer than four steps, lacks a boundary-safe CTA, lacks the required visual, or appears only once in the article journey.
- No truthful, lawful adjacent route exists. In that case, do **not** invent one or force a promotional module; block the product decision and request an approved product alternative or revised conversion scope.

## Product fact-checking

- Use current primary/official sources for version-sensitive features, format support, pricing, model names, privacy, cloud processing, and compatibility.
- Preserve accurate original benefit framing when updating claims.
- When exact product labels vary by version, use a verified category-level description and instruct the reader to check the current option in their version.
- Do not present illustrative scenarios as customer outcomes.
- Record live availability state and verification date. `Coming soon`, beta/demo-only, waitlist, unavailable-by-region, or materially degraded states require an explicit availability warning and a non-promissory CTA such as “monitor availability”, “use the verified alternative”, or “do not rely on this for production.”

## Product regression QA

Before delivery, confirm:

- No original direct-solution block was removed without an equivalent replacement.
- Product placement is logical in the article journey.
- Every product mention has a defined role.
- Product comparison tables remain decision-useful.
- Direct solutions retain scenario value, workflow, constraints, and CTA.
- Every named core conversion product that lacks primary-task support has either a complete Boundary-sensitive core conversion (Ultra Tips) module or a documented blocked decision because no truthful route exists.
