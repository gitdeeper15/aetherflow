"""Definition 2 — Post-Merge Verification Operator."""

from __future__ import annotations

from typing import Callable

from aetherflow.models import Changeset, Status, VerificationResult


def verify(changeset, parent_results, ci_failures, attributable):
    attr = attributable & ci_failures
    if attr:
        return VerificationResult(
            cid=changeset.cid, status=Status.FAILED,
            attributable_failures=sorted(attr),
            all_failures=sorted(ci_failures),
        )
    any_parent_bad = any(
        r.status in (Status.FAILED, Status.TAINTED) for r in parent_results
    )
    if ci_failures and (any_parent_bad or not attr):
        return VerificationResult(
            cid=changeset.cid, status=Status.TAINTED,
            all_failures=sorted(ci_failures),
        )
    return VerificationResult(cid=changeset.cid, status=Status.VERIFIED)


def verify_dag(changesets, ci_failures, attribution_fn):
    results = {}

    def _visit(cid):
        if cid in results:
            return results[cid]
        cs = changesets[cid]
        parent_res = [_visit(pid) for pid in cs.parent_ids]
        attr = attribution_fn(cid, [r.status for r in parent_res])
        result = verify(cs, parent_res, ci_failures.get(cid, set()), attr)
        results[cid] = result
        return result

    for cid in changesets:
        _visit(cid)
    return results
