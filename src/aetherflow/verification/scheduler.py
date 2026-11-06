"""Adaptive verification scheduling."""

from __future__ import annotations

import heapq
from dataclasses import dataclass, field
from typing import Optional

from aetherflow.conflict.window import conflict_window
from aetherflow.models import Changeset


@dataclass(order=True)
class ScheduledJob:
    """Job with priority (lower = more urgent, heapq is min-heap)."""
    priority: float
    changeset: Changeset = field(compare=False)


class AdaptiveScheduler:
    """
    Schedule verification jobs by priority.

    Priority = -(w_conflict * W + w_outdeg * norm_outdeg + w_parent * parent_unverified)

    We negate the priority because heapq is a min-heap: lower value = higher priority.
    """

    def __init__(
        self,
        kappa: float = 3.0,
        theta: float = 4.0,
        w_conflict: float = 0.5,
        w_outdeg: float = 0.3,
        w_parent: float = 0.2,
    ):
        self.kappa = kappa
        self.theta = theta
        self.w_conflict = w_conflict
        self.w_outdeg = w_outdeg
        self.w_parent = w_parent
        self._queue: list[ScheduledJob] = []

    def _compute_priority(
        self,
        changeset: Changeset,
        recent: list[Changeset],
        out_degree: int,
        parent_verified: bool,
    ) -> float:
        """Compute priority score (higher = more urgent)."""
        if recent:
            w_vals = [
                conflict_window(
                    tau=abs(changeset.timestamp - r.timestamp),
                    overlap=0.5,
                    kappa=self.kappa,
                    theta=self.theta,
                )
                for r in recent[-10:]
            ]
            w_conflict = max(w_vals)
        else:
            w_conflict = 0.0

        norm_outdeg = min(out_degree / 10.0, 1.0)
        parent_unverified = 0.0 if parent_verified else 1.0

        return (
            self.w_conflict * w_conflict
            + self.w_outdeg * norm_outdeg
            + self.w_parent * parent_unverified
        )

    def schedule(
        self,
        changeset: Changeset,
        recent: list[Changeset],
        out_degree: int = 0,
        parent_verified: bool = True,
    ) -> None:
        """Add a changeset to the schedule."""
        priority = self._compute_priority(
            changeset, recent, out_degree, parent_verified
        )
        # Negate: heapq is min-heap, so higher priority = lower value
        heapq.heappush(
            self._queue,
            ScheduledJob(priority=-priority, changeset=changeset),
        )

    def next(self) -> Optional[Changeset]:
        """Pop the highest-priority job."""
        if not self._queue:
            return None
        return heapq.heappop(self._queue).changeset

    def __len__(self) -> int:
        return len(self._queue)
