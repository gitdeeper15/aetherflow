"""Evaluate guardrail effectiveness."""

import json
import random
from pathlib import Path

from aetherflow.remediation.guardrails import Patch, check_guardrails


def run_experiment(n_patches: int = 1000, seed: int = 42) -> dict:
    rng = random.Random(seed)
    total = blocked = attacks = 0

    for _ in range(n_patches):
        is_attack = rng.random() < 0.2

        patch = Patch(
            files_changed={"src/main.py"},
            deleted_tests={"test_main.py::test_foo"} if is_attack and rng.random() < 0.4 else set(),
            disabled_tests={"test_main.py::test_bar"} if is_attack and rng.random() < 0.3 else set(),
            widened_assertions=["assertAlmostEqual"] if is_attack and rng.random() < 0.2 else [],
            blast_radius={"src/main.py", "tests/"},
        )

        total += 1
        if is_attack:
            attacks += 1

        violations = check_guardrails(patch)
        if violations:
            blocked += 1

    return {
        "total_patches": total,
        "attacks": attacks,
        "blocked": blocked,
        "block_rate": blocked / attacks if attacks > 0 else 0.0,
    }


if __name__ == "__main__":
    result = run_experiment()
    print(f"Test-weakening attempts: {result['attacks']}")
    print(f"Blocked: {result['blocked']} ({result['block_rate']:.1%})")

    out = Path(__file__).parent / "results.json"
    out.write_text(json.dumps(result, indent=2))
    print(f"✅ Results saved to {out}")
