"""
Fit and test Equation 1a on real commit history.

W(cᵢ, cⱼ) = 1 − exp(−κ·O·e^(−τ/θ))
"""

import json
import math
from pathlib import Path

import numpy as np


def conflict_window(tau: float, overlap: float, kappa: float, theta: float) -> float:
    return 1.0 - math.exp(-kappa * overlap * math.exp(-tau / theta))


def fit(pairs: list[dict]) -> tuple[float, float, dict]:
    """Grid search over κ, θ to minimize log-loss."""
    if not pairs:
        return 1.0, 1.0, {"auc": 0.0, "n": 0}

    best = (1.0, 1.0, float("inf"))
    for kappa in np.linspace(0.1, 10.0, 40):
        for theta in np.linspace(0.5, 20.0, 40):
            loss = 0.0
            for p in pairs:
                w = conflict_window(p["tau"], p["overlap"], kappa, theta)
                eps = 1e-9
                y = p["conflict"]
                loss -= y * math.log(w + eps) + (1 - y) * math.log(1 - w + eps)
            if loss < best[2]:
                best = (kappa, theta, loss)

    kappa, theta, _ = best

    # Compute AUC manually (no sklearn required)
    preds = [conflict_window(p["tau"], p["overlap"], kappa, theta) for p in pairs]
    labels = [p["conflict"] for p in pairs]

    # AUC via rank statistic
    pos = [i for i, l in enumerate(labels) if l == 1]
    neg = [i for i, l in enumerate(labels) if l == 0]
    if pos and neg:
        auc = 0.0
        for i in pos:
            for j in neg:
                if preds[i] > preds[j]:
                    auc += 1.0
                elif preds[i] == preds[j]:
                    auc += 0.5
        auc /= (len(pos) * len(neg))
    else:
        auc = 0.0

    return kappa, theta, {"auc": auc, "n": len(pairs)}


if __name__ == "__main__":
    data_file = Path(__file__).parent / "data" / "pairs.json"
    if not data_file.exists():
        print(f"⚠️  {data_file} not found. Run data/collect.py first.")
        raise SystemExit(1)

    pairs = json.loads(data_file.read_text())
    kappa, theta, metrics = fit(pairs)
    print(f"Fitted κ={kappa:.3f}, θ={theta:.3f}")
    print(f"AUC = {metrics['auc']:.3f}, N = {metrics['n']}")

    out = Path(__file__).parent / "results.json"
    out.write_text(json.dumps({"kappa": kappa, "theta": theta, **metrics}, indent=2))
    print(f"✅ Results saved to {out}")
