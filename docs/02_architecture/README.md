# Architectural Pillars — v1.0.0

**Status:** Specified, version 1.0.0.
**Source:** Section 4 of the manuscript.
**Depends on:** Formalization Section (v1.0.0).

---

## Pillar 1 — Lock-Free Merge Entry

Every incoming agentic changeset is appended to the trunk's reference log by an atomic compare-and-swap on the log head, retried on contention. No queue, branch-protection gate, or global lock stands between submission and admission.

### Proposition 1 — Admission Independence

Under lock-free entry, the time from submission to admission to the trunk log is `a`, independent of the CI duration `s` and of the verification backlog.

**Proof:** Admission consists only of the atomic append; verification is dispatched asynchronously after the append returns and no step of admission waits on it. [QED]

**Caveat:** This moves the cost rather than eliminating it — verification still takes time `s`, and a failure is discovered after admission, not before. The architecture's claim is that this reordering is beneficial under the controls of the verified-head discipline, not that the work disappears.

---

## Pillar 2 — Post-Merge Verification Layer

Immediately after admission, verification workers execute builds, tests, and semantic dependency scans against the new state. Work is scheduled in priority order:

1. Changesets with high conflict-window scores against recent neighbours.
2. Changesets touching widely depended-upon code (high out-degree in `G`).
3. Changesets whose parents are not yet verified.

Failing checks trigger attribution (Section 3.2), producing the failed/tainted distinction that the remediation layer consumes.

---

## Pillar 3 — Proactive Remediation Agents

When a changeset is marked failed, a remediation agent is dispatched with the failing changeset, the failing checks, and the last verified state. The policy is graded, with four tiers of compensation plus a final escalation to a human owner.

| Tier | Action | Typical Trigger | Compensation Type |
|---|---|---|---|
| 1 | Automatic revert | Failure is clearly attributable, no dependents yet | Full compensation (saga undo) |
| 2 | Targeted micro-patch | Small, local failure with identifiable cause | Forward correction |
| 3 | Patch with broader context | Failure involves interaction with adjacent changes | Forward correction |
| 4 | Semantic conflict resolution / rewrite | Two intents that cannot both be preserved textually | Forward correction, higher risk |
| Final | Escalation to a human owner | Tiers exhausted or guardrail triggered | Human decision |

### Guardrails

Because the remediating party is an agent, remediation must be constrained so that it cannot satisfy the verifier by weakening it. A corrective patch is rejected if it:

- Deletes or disables the failing test.
- Modifies test infrastructure.
- Widens an assertion's tolerance.
- Changes files outside a declared blast radius derived from the failing changeset and its dependency neighbourhood.

Unless a human approves.

---

## Verified-Head Discipline

The principal risk of lock-free entry is that the trunk head may be temporarily unverified. AetherFlow confines that risk by distinguishing two references:

- **Admission head** — advances on every append.
- **Verified head** — the most recent changeset all of whose ancestors are verified.

Producers branch from, and agents read context from, the admission head so that they see the latest work. Anything that requires a known-good state — releases, deployments, downstream consumers, human review views — reads the verified head.

The invariant the design maintains is therefore not "the trunk is always green" but "the verified head is always green".

---

## Document Status

| Field | Value |
|---|---|
| Version | 1.0.0 |
| Status | ✅ Specified |
| Source | Section 4 of the manuscript |
| Depends on | Formalization Section (v1.0.0) |
