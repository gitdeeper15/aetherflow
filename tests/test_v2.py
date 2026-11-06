"""Tests for AetherFlow v2.0.0."""

import math
import pytest

from aetherflow import (
    Changeset, Status, conflict_window, remediation_bound,
    minimum_tier_depth, verify_dag, check_guardrails, ViolationType,
)
from aetherflow.remediation.guardrails import Patch


def test_conflict_window():
    assert math.isclose(conflict_window(1.0, 0.5), 0.689, abs_tol=0.001)
    assert math.isclose(conflict_window(10.0, 0.5), 0.116, abs_tol=0.001)


def test_remediation_bound():
    assert math.isclose(remediation_bound(0.6, 1.0, 8, 0.15, 8.0), 0.995, abs_tol=0.001)
    assert minimum_tier_depth(0.008, 0.6, 0.15, 8.0) == 8


def test_verification_figure_4():
    changesets = {
        "c0": Changeset("c0", "d0", (), 0.0, "c0"),
        "c1": Changeset("c1", "d1", ("c0",), 1.0, "c1"),
        "c2": Changeset("c2", "d2", ("c1",), 2.0, "c2"),
        "c3": Changeset("c3", "d3", ("c1",), 3.0, "c3"),
        "c4": Changeset("c4", "d4", ("c2",), 4.0, "c4"),
        "c5": Changeset("c5", "d5", ("c4", "c3"), 5.0, "c5"),
    }
    ci_failures = {"c2": {"t1"}, "c4": {"t1"}, "c5": {"t1"}}

    def attr(cid, _):
        return {"t1"} if cid == "c2" else set()

    results = verify_dag(changesets, ci_failures, attr)
    assert results["c2"].status == Status.FAILED
    assert results["c4"].status == Status.TAINTED
    assert results["c5"].status == Status.TAINTED
    assert results["c3"].status == Status.VERIFIED


def test_guardrails():
    patch = Patch(
        files_changed={"src/main.py"},
        deleted_tests={"test_foo"},
        disabled_tests=set(),
        widened_assertions=[],
        blast_radius={"src/main.py", "tests/"},
    )
    violations = check_guardrails(patch)
    assert ViolationType.TEST_DELETED in violations
