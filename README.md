# SEO Article Review Workflow v3.8.0

当前执行版本：**3.8.0**。版本以 `workflow.json` 为准；入口见 `START_HERE.md`。本次升级记录见 `RELEASE_NOTES.md`。

GitHub-ready workflow for improving an existing SEO article without destroying its useful content, product-conversion value, evidence, visuals, or publication readiness.

## What changed in v3.7.0

- Adds `START_HERE.md`, a mandatory bootstrap that loads the complete execution contract before every article review.
- Requires a machine-readable `workflow_bootstrap` record; preflight rejects a release if its version, required-rule list, or pre-edit completion status is missing.
- Makes the minimal instruction self-sufficient across computers: the user provides files and the short command, while the workflow owns the fixed standards.

## What changed in v3.6.0

- Adds a fail-closed **direct-support route** for named core conversion products: a product classified `direct_supported` must have a direct-solution heading, current official feature URL visible in the article, three scenarios, workflow, limitation, and CTA.
- Blocks any direct-supported product that retains an `Ultra Tips`, `adjacent`, or “does not support the primary task” route in the article or release evidence.
- Adds product-route regression tests for direct support, adjacent authorized support, and no truthful route. A no-route classification is a release block pending an approved alternative.

## What changed in v3.5

- Adds a content-economy gate: duplicate reader decisions need one primary owner; unexplained expansion above 110% of source length fails.
- Requires a complete H1/H2/H3 heading-role map, keeping core headings keyword-aware while preserving action-led step headings and grammatical English.
- Interprets “every section needs a visual” as every H2, including Sources, unless an explicit approved exception is recorded.
- Requires one deduplicated claim-linked source system and a live product-availability check before any CTA can be approved.
- Extends preflight to reject missing content-economy, heading-role, source-record, product-availability, and all-H2 visual evidence.

## What changed in v3.5.2

- Adds the non-bypassable **Boundary-sensitive core conversion (Ultra Tips)** route for a named conversion product that does not support the article's primary task but does have a verified lawful adjacent use.
- Prevents that product from being silently reduced to an `Adjacent`, `Boundary`, exclusion-only, or one-sentence limitation mention.
- Requires the dedicated Ultra Tips H2, 3 best-for scenarios, not-for route, 4–6 steps, status-safe CTA, 3 touchpoints, and one mapped product visual.
- Extends machine-readable evidence and preflight to fail releases missing the module, required touchpoints, workflow depth, article evidence, or visual mapping.

## What changed in v3.4

- Adds a release lock: no final label until every mandatory gate has a recorded PASS.
- Adds canonical keyword-sheet selection, Top-20/exceptions evidence, and marked-copy text-integrity checks.
- Makes visual coverage section-specific, rather than relying on an overall image count.
- Adds a preflight script and delivery-contract/gate-ledger templates so an incomplete package fails before handoff.

## What changed in v3.1

- Adds a mandatory content-preservation audit before any drafting.
- Treats ordinary "review" and "optimize" requests as **Optimization Mode**, not rewrite requests.
- Replaces single-product logic with product portfolio, placement, and conversion review.
- Defines actual visual-asset delivery, not image plans or placeholders.
- Adds section-level keyword mapping and delivery acceptance gates.
- Blocks final delivery when the output is only an outline, a review memo, an image plan, or an unrendered/unverified artifact.
- Requires dated SERP evidence and a topic-specific structure plan before headings are changed; reference samples define quality, not a reusable outline.
- Raises Optimization Mode retention expectation to 80–90% and turns lower retention into a hard authorization gate.
- Requires per-use visual maps with audience, scene, rights, Alt, caption, exact insertion point, and rendered-page QA; decorative image totals cannot pass.
- Rejects generic keyword exceptions and non-editorial highlighting; each keyword placement must earn its reader value.
- Adds a named final editorial QA gate and an exact release-file manifest; a release cannot be final while visual QA, content QA, or package purity is unresolved.

## Repository map

| File | Purpose |
|---|---|
| `AGENTS.md` | Operating rules and mandatory stage gates. |
| `ARTICLE_REVIEW_SOP.md` | End-to-end article review process. |
| `KEYWORD_OPTIMIZATION_STANDARD.md` | Keyword intent, mapping, and audit rules. |
| `PRODUCT_RECOMMENDATION_STANDARD.md` | Multi-product recommendation, placement, and conversion rules. |
| `standards/CONTENT_PRESERVATION_STANDARD.md` | Protects valuable source content and prevents accidental rewrites. |
| `standards/VISUAL_ASSET_STANDARD.md` | Defines image strategy, asset requirements, and visual QA. |
| `standards/DELIVERY_ACCEPTANCE_STANDARD.md` | Defines publishable deliverables and final QA. |
| `templates/` | Reusable audit and handoff templates. |
| `templates/serp_structure_evidence.md` | Dated SERP findings and an evidence-backed, original structure plan. |
| `templates/release_evidence.json` | Machine-readable evidence contract used by preflight. |
| `templates/release_manifest.example.json` | Exact manifest contract; enumerates every release file and all gate records. |
| `templates/final_human_qa.md` | Named human release lock; every criterion must pass. |
| `templates/review_highlight_map.example.json` | Exact approved locations for yellow review markup. |
| `scripts/targeted_keyword_highlighter.py` | Creates a review copy with only mapped editorial optimizations highlighted. |

## Default operating principle

> Review is not a license to rewrite. Preserve the article's useful information and conversion assets first; remove only duplication, low-value text, and verified inaccuracies; then fill search, keyword, evidence, product, and visual gaps.

## How to use

1. Execute `START_HERE.md` in full.
2. Complete the source asset inventory in `templates/content_asset_audit.md`.
3. Select **Optimization Mode** unless the user explicitly requests a rewrite.
4. Build the keyword and product maps before editing prose.
5. Create or source actual visual assets, then embed and package them.
6. Run `scripts/review_preflight.py` and every acceptance check in `standards/DELIVERY_ACCEPTANCE_STANDARD.md`.
7. Do not label the article final unless `templates/gate_ledger.md` is fully PASS.

Before changing or releasing the workflow itself, run `python scripts/test_product_route_regression.py`. It must pass the direct-supported, adjacent-authorized-route, and no-truthful-route cases.

## Minimal instruction for a new article

For a standard complete review, the user only needs to provide the source article and keyword workbook, then send:

```text
请使用 SEO Article Review Workflow v3.8.0 对附件文章进行完整回审，默认采用 Optimization Mode，保留原文有效信息，不得改写成提纲或缩水稿。
```

The workflow then automatically executes and delivers the full v3.8.0 contract: source-asset and content-economy audits; SERP/intent research; structure and heading-role maps; keyword, product, source, and visual maps; clean and yellow-marked DOCX copies; embedded and standalone images for every required H2; preflight; rendered-page/editorial QA; and final gate records.

If a reference article is attached, it is automatically treated as a **quality benchmark only**, never as a copyable article structure. The new article's structure must be derived from its own SERP and intent research.

Only provide extra instructions if they change scope: required product/brand, audience/locale, output language, legal/compliance limitations, or a deliberate exception to the default delivery contract.

Established project-level core conversion products remain active in later review requests unless the user overrides them. Before source audit, transfer those products (or an explicit `none`) into the delivery contract and `core_conversion_products` manifest field; this activates the fail-closed Ultra Tips route when a product lacks primary-task support.

## Versioning

Use semantic workflow versions. Any change to a hard gate, delivery contract, or asset-preservation rule requires a minor version increase and an entry in `CHANGELOG.md`.
