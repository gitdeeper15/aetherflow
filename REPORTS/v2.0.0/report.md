# AetherFlow v2.0.0 — Empirical Evaluation Report

**Date:** 2026-11-06
**Version:** 2.0.0
**Stage:** Empirical Implementation

---

## 1. Implementation Summary

| Component | Status | Coverage |
|-----------|--------|----------|
| `admission/log.py` | ✅ | 100% |
| `verification/operator.py` | ✅ | 100% |
| `verification/scheduler.py` | ✅ | 100% |
| `conflict/window.py` | ✅ | 100% |
| `remediation/bound.py` | ✅ | 100% |
| `remediation/guardrails.py` | ✅ | 88% |
| `cli.py` | ✅ | 100% |
| **Total** | **✅ 24 tests** | **98%** |

---

## 2. Experiment Results

### 2.1 Conflict Window (Equation 1a)

- **Type:** Self-consistency test (synthetic data, N=500)
- **Fitted:** κ = 2.892, θ = 4.000
- **AUC:** 0.894
- **Status:** ✅ Verifies implementation correctness (recovered κ≈3, θ≈4)

### 2.2 Remediation Bound (Equation 3)

- **λ_fail = 0.0370, μ_remediate = 0.1852**
- **T_react = 5.40, γ = 0.15**
- **K=8 → P(Remediation) ≥ 1.0000**
- **Status:** ✅

### 2.3 Attribution Accuracy

- **Baseline:** P=0.900, R=0.900, F1=0.900
- **Mitigated:** P=1.000, R=1.000, F1=1.000
- **Status:** ✅

### 2.4 Guardrail Effectiveness

- **Block rate:** 100.0% (192/192)
- **Violations by type:**
  - `tolerance_widened`: 51
  - `test_deleted`: 49
  - `outside_blast_radius`: 46
  - `test_disabled`: 46
- **Status:** ✅

### 2.5 Scheduler Simulation

- **FIFO mean urgent position:** 497.5
- **Adaptive mean urgent position:** 199.5
- **Speedup:** 2.5x
- **Status:** ✅

---

## 3. Status Note

This report presents **preliminary empirical results** from the v2.0.0
reference implementation. The implementation is a reference, not a
production system. All results should be interpreted with the
limitations stated in the manuscript (Section 9).

No real-world deployment has been evaluated. Data from
`experiments/conflict_window/` is synthetic (self-consistency test).
