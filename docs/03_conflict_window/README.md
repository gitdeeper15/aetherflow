# Conflict Window — v1.0.0

**Status:** Defined, version 1.0.0.
**Source:** Section 3.1 and 3.4 of the manuscript.
**Depends on:** Formalization Section (v1.0.0).

---

## Conflict Window

The dynamic conflict window `W(cᵢ, cⱼ)` estimates the probability that two parallel changesets conflict:

```

W(cᵢ, cⱼ) = 1 − exp(−κ·O·e^(−τ/θ))

```

Where:
- `τ(cᵢ, cⱼ)` = temporal distance between injections
- `O ∈ [0, 1]` = overlap score from file-footprint overlap and dependency-graph proximity
- `κ > 0` = sensitivity
- `θ > 0` = decay horizon

### Illustration

| Pair | Overlap O | Temporal Distance τ | W = P(Conflict) | Reading |
|---|---|---|---|---|
| A | 0.5 | 1 | 0.689 | Nearby code, injected almost together: likely mutually unaware |
| B | 0.5 | 10 | 0.116 | Same overlap, injected much later: likely informed by earlier change |
| C | 0.8 | 0.5 | 0.880 | Heavy overlap, near-simultaneous: highest verification priority |

Pairs A and C would be placed at the front of the verification schedule (Section 4.2); pair B would not. Nothing is blocked in any case.

---

## Queue Saturation

A serial merge queue is modeled as a single server with Poisson arrivals at rate `λ` and exponential service time of mean `s` (the CI duration), so utilization is `ρq = λs`. For `ρq < 1`, the M/M/1 mean time in system is:

```

T_queue = s / (1 − ρq)

```

which diverges as `ρq` approaches 1 (Kleinrock, 1975), and for `ρq ≥ 1` the queue is unstable.

In contrast, lock-free entry consists of one atomic append with cost `a` that does not depend on `s` or on the number of pending verifications.

### Illustration

Consider a hypothetical organization in which a fleet of autonomous agents submits 30,000 changesets per day to one monorepo trunk, an arrival rate of `λ = 30,000 / 86,400 = 0.347` changesets per second. Suppose the full CI pipeline for a changeset takes `s = 20` minutes (1,200 s).

For a single serial queue, utilization is `ρq = λs = 0.347 × 1,200 = 417`. Because `ρq` is far above 1, the queue is unstable and its backlog grows without bound.

To be stable, a serial design would need roughly 418 or more parallel verification lanes, plus a way to reconcile them — which is exactly what speculative merge systems attempt.

---

## Document Status

| Field | Value |
|---|---|
| Version | 1.0.0 |
| Status | ✅ Defined |
| Source | Section 3.1 and 3.4 of the manuscript |
| Depends on | Formalization Section (v1.0.0) |
