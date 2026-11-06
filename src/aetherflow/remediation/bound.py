"""Definition 3 + Proposition 3 — Auto-Remediation Bound."""

from __future__ import annotations

import math


def remediation_bound(lambda_fail, mu_remediate, K, gamma, T_react):
    if lambda_fail < 0 or mu_remediate <= 0:
        raise ValueError("invalid rates")
    if K < 1 or gamma < 0 or T_react < 0:
        raise ValueError("invalid parameters")
    rho = lambda_fail / mu_remediate
    return 1.0 - (rho ** K) * math.exp(-gamma * T_react)


def minimum_tier_depth(epsilon, rho, gamma, T_react):
    if not 0 < epsilon < 1:
        raise ValueError("epsilon must be in (0, 1)")
    if not 0 < rho < 1:
        raise ValueError("rho must be in (0, 1)")
    if gamma < 0 or T_react < 0:
        raise ValueError("invalid parameters")
    return max(1, math.ceil((math.log(1.0 / epsilon) - gamma * T_react) / math.log(1.0 / rho)))
