"""Additional tests to improve coverage to >85%."""

import math
import tempfile
from pathlib import Path

import pytest

from aetherflow import (
    Changeset, Status, conflict_window, overlap_score,
    remediation_bound, minimum_tier_depth,
    verify, verify_dag, AdaptiveScheduler,
    check_guardrails, ViolationType,
)
from aetherflow.admission.log import ChangesetLog
from aetherflow.remediation.guardrails import Patch


# ─── conflict/window.py ───
def test_conflict_window_invalid_inputs():
    with pytest.raises(ValueError, match="tau must be"):
        conflict_window(-1.0, 0.5)
    with pytest.raises(ValueError, match="overlap must be"):
        conflict_window(1.0, 1.5)
    with pytest.raises(ValueError, match="kappa"):
        conflict_window(1.0, 0.5, kappa=0)
    with pytest.raises(ValueError, match="theta"):
        conflict_window(1.0, 0.5, theta=0)


def test_conflict_window_zero_overlap():
    assert conflict_window(1.0, 0.0) == 0.0


def test_conflict_window_monotonic_tau():
    for overlap in (0.2, 0.5, 0.8):
        prev = conflict_window(0.0, overlap)
        for tau in (1.0, 2.0, 5.0, 10.0):
            curr = conflict_window(tau, overlap)
            assert curr < prev
            prev = curr


def test_conflict_window_monotonic_overlap():
    for tau in (0.5, 2.0, 5.0):
        prev = conflict_window(tau, 0.1)
        for overlap in (0.3, 0.5, 0.8):
            curr = conflict_window(tau, overlap)
            assert curr > prev
            prev = curr


def test_overlap_score():
    # O = max(J, exp(-d/L))
    # J=0.5, d=0 → exp(0)=1 → max(0.5, 1) = 1.0
    assert overlap_score(0.5, 0.0) == 1.0
    # J=0.1, d=10, L=1 → max(0.1, exp(-10)) ≈ 0.1
    assert math.isclose(overlap_score(0.1, 10.0, 1.0), 0.1, abs_tol=1e-6)
    # J=0.9, d=0 → max(0.9, 1) = 1.0
    assert overlap_score(0.9, 0.0) == 1.0
    with pytest.raises(ValueError):
        overlap_score(1.5, 0.0)
    with pytest.raises(ValueError):
        overlap_score(0.5, -1.0)
    with pytest.raises(ValueError):
        overlap_score(0.5, 1.0, characteristic_length=0)


# ─── remediation/bound.py ───
def test_remediation_bound_monotonic():
    prev = remediation_bound(0.6, 1.0, 1, 0.15, 8.0)
    for K in (2, 4, 8, 16):
        curr = remediation_bound(0.6, 1.0, K, 0.15, 8.0)
        assert curr > prev
        prev = curr


def test_remediation_bound_invalid():
    with pytest.raises(ValueError):
        remediation_bound(-0.1, 1.0, 8, 0.15, 8.0)
    with pytest.raises(ValueError):
        remediation_bound(0.6, 0.0, 8, 0.15, 8.0)
    with pytest.raises(ValueError):
        remediation_bound(0.6, 1.0, 0, 0.15, 8.0)
    with pytest.raises(ValueError):
        remediation_bound(0.6, 1.0, 8, -0.1, 8.0)
    with pytest.raises(ValueError):
        remediation_bound(0.6, 1.0, 8, 0.15, -1.0)


def test_minimum_tier_depth_no_budget():
    K = minimum_tier_depth(0.008, 0.6, 0.15, 0.0)
    assert K == 10


def test_minimum_tier_depth_invalid():
    with pytest.raises(ValueError):
        minimum_tier_depth(0.0, 0.6, 0.15, 8.0)
    with pytest.raises(ValueError):
        minimum_tier_depth(0.01, 1.0, 0.15, 8.0)


# ─── admission/log.py ───
def test_changeset_log_append_and_iterate():
    with tempfile.TemporaryDirectory() as tmpdir:
        log = ChangesetLog(Path(tmpdir))
        assert log.head is None

        cs1 = Changeset.create("delta1")
        cid1 = log.append(cs1)
        assert cid1 == cs1.cid
        assert log.head == cs1.cid

        cs2 = Changeset.create("delta2", (cs1.cid,))
        log.append(cs2)
        assert log.head == cs2.cid

        changesets = list(log)
        assert len(changesets) == 2
        assert changesets[0].cid == cs1.cid
        assert changesets[1].cid == cs2.cid


def test_changeset_log_reload():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir)
        log1 = ChangesetLog(path)
        cs = Changeset.create("delta1")
        log1.append(cs)

        log2 = ChangesetLog(path)
        assert log2.head == cs.cid


# ─── verification/scheduler.py ───
def test_scheduler_empty():
    scheduler = AdaptiveScheduler()
    assert scheduler.next() is None
    assert len(scheduler) == 0


def test_scheduler_priority_ordering():
    """
    With recent=[], w_conflict=0.
    c3 has out_degree=5 → priority = 0.3 * 0.5 = 0.15 (highest)
    c1, c2 have out_degree=0 → priority = 0.0
    """
    scheduler = AdaptiveScheduler()
    c1 = Changeset("c1", "d1", (), 0.0, "c1")
    c2 = Changeset("c2", "d2", ("c1",), 1.0, "c2")
    c3 = Changeset("c3", "d3", ("c1",), 1.5, "c3")

    scheduler.schedule(c1, recent=[], parent_verified=True)  # priority 0.0
    scheduler.schedule(c2, recent=[], parent_verified=True)  # priority 0.0
    scheduler.schedule(c3, recent=[], parent_verified=True, out_degree=5)  # priority 0.15

    assert len(scheduler) == 3

    # c3 (highest priority) must be first
    first = scheduler.next()
    assert first.cid == "c3", f"Expected c3 first, got {first.cid}"

    # Then c1 and c2 (both priority 0.0, order arbitrary)
    remaining = {scheduler.next().cid, scheduler.next().cid}
    assert remaining == {"c1", "c2"}

    assert scheduler.next() is None


def test_scheduler_unverified_parent():
    """
    With recent=[], w_conflict=0.
    c2 with parent_verified=False → priority = 0.2
    c1 with parent_verified=True → priority = 0.0
    """
    scheduler = AdaptiveScheduler()
    c1 = Changeset("c1", "d1", (), 0.0, "c1")
    c2 = Changeset("c2", "d2", ("c1",), 1.0, "c2")

    scheduler.schedule(c1, recent=[], parent_verified=True)   # priority 0.0
    scheduler.schedule(c2, recent=[], parent_verified=False)  # priority 0.2

    assert len(scheduler) == 2

    first = scheduler.next()
    assert first.cid == "c2", f"Expected c2 first (unverified parent), got {first.cid}"

    second = scheduler.next()
    assert second.cid == "c1"


# ─── guardrails additional ───
def test_guardrails_disabled_tests():
    patch = Patch(
        files_changed={"src/main.py"},
        deleted_tests=set(),
        disabled_tests={"test_foo"},
        widened_assertions=[],
        blast_radius={"src/main.py"},
    )
    violations = check_guardrails(patch)
    assert ViolationType.TEST_DISABLED in violations


def test_guardrails_tolerance():
    patch = Patch(
        files_changed={"src/main.py"},
        deleted_tests=set(),
        disabled_tests=set(),
        widened_assertions=["assertAlmostEqual"],
        blast_radius={"src/main.py"},
    )
    violations = check_guardrails(patch)
    assert ViolationType.TOLERANCE_WIDENED in violations


def test_guardrails_blast_radius():
    patch = Patch(
        files_changed={"src/other.py"},
        deleted_tests=set(),
        disabled_tests=set(),
        widened_assertions=[],
        blast_radius={"src/main.py"},
    )
    violations = check_guardrails(patch)
    assert ViolationType.OUTSIDE_BLAST_RADIUS in violations


# ─── CLI test ───
def test_cli_conflict_window(capsys):
    from aetherflow.cli import main
    exit_code = main(["conflict-window", "--tau", "1.0", "--overlap", "0.5"])
    assert exit_code == 0
    captured = capsys.readouterr()
    assert "0.689" in captured.out


def test_cli_remediation_bound(capsys):
    from aetherflow.cli import main
    exit_code = main([
        "remediation-bound",
        "--lambda-fail", "0.6",
        "--mu-remediate", "1.0",
        "--K", "8",
    ])
    assert exit_code == 0
    captured = capsys.readouterr()
    # Print may contain unicode ≥, extract just the number
    import re
    numbers = re.findall(r"\d+\.\d+", captured.out)
    assert len(numbers) >= 1
    assert abs(float(numbers[0]) - 0.995) < 0.01


def test_cli_min_tier_depth(capsys):
    from aetherflow.cli import main
    exit_code = main([
        "min-tier-depth",
        "--epsilon", "0.008",
        "--rho", "0.6",
    ])
    assert exit_code == 0
    captured = capsys.readouterr()
    assert "8" in captured.out
