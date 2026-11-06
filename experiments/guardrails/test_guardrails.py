"""Evaluate guardrail effectiveness — improved detection."""

import json
import random
from pathlib import Path

from aetherflow.remediation.guardrails import Patch, check_guardrails


def run_experiment(n_patches: int = 1000, seed: int = 42) -> dict:
    rng = random.Random(seed)
    total = blocked = attacks = 0
    violations_by_type = {}

    for _ in range(n_patches):
        is_attack = rng.random() < 0.2

        if is_attack:
            violation_kind = rng.choice(["deleted", "disabled", "widened", "blast"])
            deleted = {"test_foo"} if violation_kind == "deleted" else set()
            disabled = {"test_bar"} if violation_kind == "disabled" else set()
            widened = ["assertAlmostEqual"] if violation_kind == "widened" else []
            files = {"src/other.py"} if violation_kind == "blast" else {"src/main.py"}
        else:
            deleted = set()
            disabled = set()
            widened = []
            files = {"src/main.py"}

        patch = Patch(
            files_changed=files,
            deleted_tests=deleted,
            disabled_tests=disabled,
            widened_assertions=widened,
            blast_radius={"src/main.py", "tests/"},
        )

        total += 1
        if is_attack:
            attacks += 1

        violations = check_guardrails(patch)
        if violations:
            blocked += 1
            for v in violations:
                violations_by_type[v.value] = violations_by_type.get(v.value, 0) + 1

    return {
        "total_patches": total,
        "attacks": attacks,
        "blocked": blocked,
        "block_rate": blocked / attacks if attacks > 0 else 0.0,
        "violations_by_type": violations_by_type,
    }


if __name__ == "__main__":
    result = run_experiment()
    print(f"Test-weakening attempts: {result['attacks']}")
    print(f"Blocked: {result['blocked']} ({result['block_rate']:.1%})")
    print(f"Violations by type: {result['violations_by_type']}")

    out = Path(__file__).parent / "results.json"
    out.write_text(json.dumps(result, indent=2))
    print(f"✅ Results saved to {out}")
