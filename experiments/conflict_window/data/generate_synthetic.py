"""Generate synthetic (τ, O, conflict) pairs for testing Equation 1a."""

import json
import math
import random
from pathlib import Path


def generate(n: int = 500, seed: int = 42) -> list[dict]:
    rng = random.Random(seed)
    pairs = []
    for _ in range(n):
        tau = rng.uniform(0, 24)          # 0–24 hours
        overlap = rng.uniform(0, 1)       # 0–1
        p = 1.0 - math.exp(-3.0 * overlap * math.exp(-tau / 4.0))
        conflict = 1 if rng.random() < p else 0
        pairs.append({"tau": tau, "overlap": overlap, "conflict": conflict})
    return pairs


if __name__ == "__main__":
    pairs = generate(500)
    out = Path(__file__).parent / "pairs.json"
    out.write_text(json.dumps(pairs, indent=2))
    print(f"✅ Generated {len(pairs)} synthetic pairs → {out}")
    print("   (Self-consistency test — verifies code correctness)")
