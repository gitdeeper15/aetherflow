# Formalization Section — v1.0.0

**Status:** Defined, version 1.0.0.
**Source:** Section 3 of the manuscript.
**Depends on:** Nothing prior — establishes the mathematical vocabulary.

---

## Definition 1 — Dynamic Conflict Window

```

W(cᵢ, cⱼ) = 1 − exp(−κ·O·e^(−τ/θ))

```

Where:
- `τ(cᵢ, cⱼ)` = temporal distance between changeset injections
- `O ∈ [0, 1]` = overlap score from file-footprint overlap and dependency-graph proximity
- `κ > 0` = sensitivity
- `θ > 0` = decay horizon

### Proposition 2 — Monotonicity

Under Equation 1a, `W` is strictly decreasing in `τ` for `O > 0`, and strictly increasing in `O` for finite `τ`.

**Proof:** Write `u = κ·O·e^(−τ/θ) > 0`. Since `W = 1 − e^(−u)` is strictly increasing in `u`, and `u` is strictly decreasing in `τ` and strictly increasing in `O`, the claims follow. [QED]

---

## Definition 2 — Post-Merge Verification Operator

```

V(c) = ⊕_V(δ_i, {V(p) | p ∈ P(c_i)}, CI(c_i))

```

Three-valued: **verified**, **failed**, or **tainted**.

The three-valued range is the key design decision. A two-valued operator that ANDs parent results would mark every descendant of a failed change as failed, making a single defect appear to be hundreds.

---

## Definition 3 — Auto-Remediation Bound

```

P(Remediation) ≥ 1 − (λ_fail/μ_remediate)^K · e^(−γ·T_react)

```

Where:
- `λ_fail` = rate of post-merge integration failures
- `μ_remediate` = aggregate processing capacity of remediation agents
- `K` = remediation capacity tier depth
- `T_react` = remediation time budget
- `γ` = decay coefficient

### Proposition 3 — Monotonicity and Minimum Tier Depth

If `ρ < 1`, the right-hand side of Equation 3 is non-decreasing in `K` and in `T_react`, and tends to 1 as `K` grows without bound. For a target residual risk `ε ∈ (0, 1)`, the bound is at least `1 − ε` whenever:

```

K ≥ (ln(1/ε) − γ·T_react) / ln(1/ρ)

```

**Proof:** The subtracted term `ρ^K · e^(−γT)` is positive, decreasing in `K` when `0 < ρ < 1`, decreasing in `T`, and tends to 0 as `K` grows. Setting `ρ^K · e^(−γT) ≤ ε`, taking logarithms, and dividing by `ln(1/ρ) > 0` yields Equation 4. [QED]

---

## Document Status

| Field | Value |
|---|---|
| Version | 1.0.0 |
| Status | ✅ Defined |
| Source | Section 3 of the manuscript |
| Depends on | Nothing prior |
