"""Core data models for AetherFlow v2.0.0."""

from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass, field
from enum import Enum


class Status(str, Enum):
    VERIFIED = "verified"
    FAILED = "failed"
    TAINTED = "tainted"


@dataclass(frozen=True)
class Changeset:
    """Immutable changeset record."""
    cid: str
    delta_id: str
    parent_ids: tuple[str, ...]
    timestamp: float
    signature: str

    @classmethod
    def create(cls, delta_id: str, parent_ids: tuple[str, ...] = ()) -> "Changeset":
        ts = time.time()
        payload = f"{delta_id}:{','.join(parent_ids)}:{ts}"
        sig = hashlib.sha256(payload.encode()).hexdigest()[:16]
        return cls(cid=sig, delta_id=delta_id, parent_ids=parent_ids,
                   timestamp=ts, signature=sig)


@dataclass
class VerificationResult:
    """Result of the post-merge verification operator."""
    cid: str
    status: Status
    attributable_failures: list[str] = field(default_factory=list)
    all_failures: list[str] = field(default_factory=list)
