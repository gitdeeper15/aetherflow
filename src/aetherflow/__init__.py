"""AetherFlow v2.0.0 — Empirical implementation of the formal architecture."""

from aetherflow.__version__ import __version__

from aetherflow.models import Changeset, Status, VerificationResult
from aetherflow.conflict.window import conflict_window, overlap_score
from aetherflow.verification.operator import verify, verify_dag
from aetherflow.verification.scheduler import AdaptiveScheduler
from aetherflow.remediation.bound import remediation_bound, minimum_tier_depth
from aetherflow.remediation.guardrails import check_guardrails, ViolationType

__all__ = [
    "__version__",
    "Changeset", "Status", "VerificationResult",
    "conflict_window", "overlap_score",
    "verify", "verify_dag",
    "AdaptiveScheduler",
    "remediation_bound", "minimum_tier_depth",
    "check_guardrails", "ViolationType",
]
