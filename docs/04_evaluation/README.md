# Evaluation — v1.0.0

**Status:** Specified, version 1.0.0.
**Source:** Section 7 of the manuscript.
**Depends on:** Formalization Section (v1.0.0).

---

## Proposed Evaluation Protocol

The source draft stated expected improvements as a comparison table. Those values — an integration latency of 30–120 minutes for merge queues versus 0.5–2.0 seconds for AetherFlow (≈100x), zero queue starvation, and a remediation success rate of at least 99.2% — are retained here only as design targets, not as results.

### Workloads

1. Replay of a real repository's commit history at accelerated arrival rates.
2. Synthetic agent-generated changesets with controlled footprint overlap.
3. Injected-fault workloads with known culprits for attribution accuracy.

### Baselines

- A Git-based merge queue.
- A speculative-gating configuration.
- A pre-submit-plus-post-submit configuration.

### Primary Metrics

- Admission latency.
- Verified latency.
- Fraction of time the admission head is unverified.
- Attribution precision/recall.
- Remediation success rate per tier.
- Count of guardrail violations attempted by remediation agents.

### Ablations

- Two-valued versus three-valued verification.
- With and without conflict-window prioritization.
- `K = 1 … K_max` tiers.
- Guardrails off (to measure how often agents weaken tests).

---

## Validating Equations 1a and 3

**Equation 1a:** The parameters `κ`, `θ`, `L` can be fit by logistic-style regression on observed conflicts versus `(τ, O)`; the quality of fit is then a direct test of the functional form.

**Equation 3:** Tested by estimating `λ_fail`, `μ_remediate`, and the per-tier success probabilities from logs and comparing the predicted bound to the observed remediation success rate across load levels; a bound that is violated falsifies the independence assumption behind it.

---

## Design Targets (Not Results)

| Metric | Merge-Queue Baseline | AetherFlow | Status |
|---|---|---|---|
| Submission-to-admission latency | Grows with queue depth | Atomic append cost `a`; independent of `s` | Structural (Prop. 1); magnitude untested |
| Submission-to-verified latency | Queue wait + CI | CI duration `s`, plus remediation if failed | Untested; may be comparable |
| Queue starvation | Possible near `ρq = 1` | No queue | Structural |
| Hypothesized speed-up | 30–120 min | 0.5–2.0 s | Design target; unvalidated |
| Remediation success | Human review dependent | Eq. 3 bound | Design target; `K = 8` suffices in the stated example |

**Note on the two latency measures:** Admission latency and verified latency are different quantities. The headline benefit of lock-free entry concerns the first; an evaluation that reports only admission latency would overstate the benefit if verified latency is not also reported.

---

## Document Status

| Field | Value |
|---|---|
| Version | 1.0.0 |
| Status | ✅ Specified |
| Source | Section 7 of the manuscript |
| Depends on | Formalization Section (v1.0.0) |
