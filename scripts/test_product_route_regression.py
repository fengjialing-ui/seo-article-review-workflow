"""Regression tests for core-conversion product routing.

Run with the bundled workflow Python:
    python scripts/test_product_route_regression.py
"""
from review_preflight import BOOTSTRAP_REQUIRED_FILES, core_conversion_ultra_tips_failures, workflow_bootstrap_failures


NAME = "HitPaw FotorPea"
URL = "https://www.hitpaw.com/ai-photo-editing-tips/remove-reflections-in-photoshop.html"
CFG = {"core_conversion_products": [NAME]}
DIRECT_HEADING = "Method 3: Remove Sunlight Glare with HitPaw FotorPea"
DIRECT_STEPS = ["Open a copy", "Make a narrow adjustment", "Preview before export"]
DIRECT_TEXT = f"{DIRECT_HEADING}\n{URL}\n" + "\n".join(DIRECT_STEPS)


def direct_row(**overrides):
    row = {
        "name": NAME,
        "core_conversion_product": True,
        "primary_task_support": "direct_supported",
        "role": "Direct solution",
        "direct_solution_heading": DIRECT_HEADING,
        "direct_workflow_steps": DIRECT_STEPS,
        "official_evidence_url": URL,
    }
    row.update(overrides)
    return row


def adjacent_row():
    heading = "Ultra Tips: HitPaw FotorPea for Authorized Adjacent Cleanup"
    module = {
        "heading": heading,
        "boundary_disclosure": "It does not perform the primary task.",
        "supported_authorized_route": "It supports an authorized adjacent cleanup.",
        "not_for": "Not for the unsupported primary task.",
        "workflow_steps": ["Open a copy", "Choose the adjacent route", "Preview", "Export"],
        "current_status_statement": "Check current availability.",
        "cta_text": "Check the current product details.",
        "touchpoints": [
            {"role": "decision_context", "exact_location": "Decision guide"},
            {"role": "ultra_tips_owner", "exact_location": heading},
            {"role": "reassurance", "exact_location": "FAQ"},
        ],
        "visual_asset_filename": "product.png",
    }
    text = "\n".join(["Decision guide", heading, "FAQ", *[str(v) for v in module.values() if isinstance(v, str)]])
    row = {
        "name": NAME,
        "core_conversion_product": True,
        "primary_task_support": "adjacent_authorized_route",
        "role": "Boundary-sensitive core conversion (Ultra Tips)",
        "ultra_tips": module,
    }
    visuals = [{"asset_filename": "product.png", "required_section": heading}]
    return row, text, visuals


def run():
    assert core_conversion_ultra_tips_failures(CFG, [direct_row()], DIRECT_TEXT, []) == []

    stale = direct_row(ultra_tips={"heading": "Ultra Tips: HitPaw FotorPea"})
    failures = core_conversion_ultra_tips_failures(CFG, [stale], DIRECT_TEXT + "Ultra Tips: HitPaw FotorPea", [])
    assert any("retains an Ultra Tips evidence object" in item for item in failures)
    assert any("routed through Ultra Tips" in item for item in failures)

    failures = core_conversion_ultra_tips_failures(CFG, [direct_row(direct_workflow_steps=[])], DIRECT_TEXT, [])
    assert any("requires three to six direct workflow steps" in item for item in failures)

    adjacent, adjacent_text, visuals = adjacent_row()
    assert core_conversion_ultra_tips_failures(CFG, [adjacent], adjacent_text, visuals) == []

    blocked = direct_row(primary_task_support="no_truthful_route", blocked_decision="No lawful route.", approved_alternative_request="Request an approved alternative.")
    failures = core_conversion_ultra_tips_failures(CFG, [blocked], "", [])
    assert any("route is blocked pending approved alternative" in item for item in failures)

    bootstrap_cfg = {"workflow_version": "v3.7.0"}
    good_bootstrap = {"workflow_bootstrap": {"workflow_version": "v3.7.0", "completed_before_editing": True, "required_files_read": sorted(BOOTSTRAP_REQUIRED_FILES)}}
    assert workflow_bootstrap_failures(bootstrap_cfg, good_bootstrap), "Prefilled legacy bootstrap must not pass"
    assert workflow_bootstrap_failures(bootstrap_cfg, {"workflow_bootstrap": {}})
    print("product-route regression tests: PASS")


if __name__ == "__main__":
    run()
