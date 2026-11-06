"""Test Equation 3 on real remediation logs."""

import json
import math
from pathlib import Path


def remediation_bound(lambda_fail, mu_remediate, K, gamma, T_react):
    rho = lambda_fail / mu_remediate
    return 1.0 - (rho ** K) * math.exp(-gamma * T_react)


def minimum_tier_depth(epsilon, rho, gamma, T_react):
    return max(1, math.ceil((math.log(1.0 / epsilon) - gamma * T_react) / math.log(1.0 / rho)))


if __name__ == "__main__":
    # Simulated log data (replace with real CI/CD logs)
    logs = [
        {"tier": 1, "time": 2.5, "success": True},
        {"tier": 1, "time": 3.0, "success": False},
        {"tier": 2, "time": 5.0, "success": True},
        {"tier": 2, "time": 6.5, "success": True},
        {"tier": 3, "time": 10.0, "success": True},
    ]

    total_time = sum(l["time"] for l in logs)
    failures = sum(1 for l in logs if not l["success"])
    lambda_fail = failures / total_time
    mu_remediate = len(logs) / total_time
    gamma = 0.15
    T_react = total_time / len(logs)

    print(f"λ_fail = {lambda_fail:.4f}")
    print(f"μ_remediate = {mu_remediate:.4f}")
    print(f"T_react = {T_react:.2f}")
    print(f"γ = {gamma}")

    for K in [1, 2, 4, 8]:
        bound = remediation_bound(lambda_fail, mu_remediate, K, gamma, T_react)
        print(f"  K={K}: P(Remediation) ≥ {bound:.4f}")

    out = Path(__file__).parent / "results.json"
    out.write_text(json.dumps({
        "lambda_fail": lambda_fail,
        "mu_remediate": mu_remediate,
        "gamma": gamma,
        "T_react": T_react,
    }, indent=2))
    print(f"✅ Results saved to {out}")
