"""Definition 1 — Dynamic Conflict Window."""

from __future__ import annotations

import math


def conflict_window(tau, overlap, kappa=3.0, theta=4.0):
    if tau < 0:
        raise ValueError("tau must be ≥ 0")
    if not 0 <= overlap <= 1:
        raise ValueError("overlap must be in [0, 1]")
    if kappa <= 0 or theta <= 0:
        raise ValueError("kappa and theta must be > 0")
    return 1.0 - math.exp(-kappa * overlap * math.exp(-tau / theta))


def overlap_score(jaccard_files, graph_distance, characteristic_length=1.0):
    if not 0 <= jaccard_files <= 1:
        raise ValueError("jaccard_files must be in [0, 1]")
    if graph_distance < 0:
        raise ValueError("graph_distance must be ≥ 0")
    if characteristic_length <= 0:
        raise ValueError("characteristic_length must be > 0")
    return max(jaccard_files, math.exp(-graph_distance / characteristic_length))
