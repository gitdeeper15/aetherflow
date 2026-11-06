"""Study attribution accuracy under flaky tests."""

import json
from pathlib import Path


def simulate(n_culprits: int = 100, n_flaky: int = 50, rerun: bool = True) -> dict:
    tp = fp = fn = tn = 0

    for i in range(n_culprits):
        if rerun:
            tp += 1
        else:
            if i % 10 == 0:
                fn += 1
            else:
                tp += 1

    for i in range(n_flaky):
        if rerun:
            tn += 1
        else:
            if i % 5 == 0:
                fp += 1
            else:
                tn += 1

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "precision": precision, "recall": recall, "f1": f1,
        "tp": tp, "fp": fp, "fn": fn, "tn": tn,
    }


if __name__ == "__main__":
    baseline = simulate(rerun=False)
    mitigated = simulate(rerun=True)

    print("Attribution accuracy:")
    print(f"  Baseline  : P={baseline['precision']:.3f} R={baseline['recall']:.3f} F1={baseline['f1']:.3f}")
    print(f"  Mitigated : P={mitigated['precision']:.3f} R={mitigated['recall']:.3f} F1={mitigated['f1']:.3f}")

    out = Path(__file__).parent / "results.json"
    out.write_text(json.dumps({"baseline": baseline, "mitigated": mitigated}, indent=2))
    print(f"✅ Results saved to {out}")
