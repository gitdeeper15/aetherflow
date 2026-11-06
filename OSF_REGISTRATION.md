# AetherFlow: Automated Post-Merge Verification and Dynamic Conflict Resolution in Multi-Agent Programming Environments

---

**Registration DOI:** [10.17605/OSF.IO/92Y3W](https://doi.org/10.17605/OSF.IO/92Y3W)
**Registration Type:** OSF Preregistration
**Registry:** OSF Registries
**Date Created:** Nov 6, 2026, 9:58 AM
**Date Registered:** Nov 6, 2026, 9:58 AM
**Associated Project:** [https://osf.io/8k5gx](https://osf.io/8k5gx)
**Internet Archive:** [https://archive.org/details/osf-registrations-92y3w-v1](https://archive.org/details/osf-registrations-92y3w-v1)
**License:** CC-By Attribution 4.0 International
**Contributor:** Samir Baladi

---

## Data / Analytic Code / Materials / Papers / Supplements

The following files were attached to this registration:

- `README.md`
- `AetherFlow_Research_Paper.pdf`

---

## Overview

### Research questions or hypotheses

This is a formal architecture paper. No empirical hypotheses are tested. The paper formalizes three definitions and derives three propositions.

The central research question is:

What architectural and formal changes become necessary — and which remain optional design choices — when merge queues must be replaced by post-merge verification and auto-remediation in multi-agent programming environments?

The paper decomposes this question into three formal claims, each stated as a definition or theorem:

1. Dynamic Conflict Window (Definition 1): W(cᵢ, cⱼ) = 1 − exp(−κ·O·e^(−τ/θ)). A probabilistic estimate of semantic/structural conflict between parallel changesets.
2. Post-Merge Verification Operator (Definition 2): V(c) = ⊕_V(δ_i, {V(p)}, CI(c_i)). A recursive, three-valued verification status (verified, failed, tainted).
3. Auto-Remediation Bound (Definition 3): P(Remediation) ≥ 1 − (λ_fail/μ_remediate)^K · e^(−γ·T_react). A lower bound on remediation success probability.

Three propositions are proven:
- Proposition 1: Admission Independence.
- Proposition 2: Monotonicity of Conflict Window.
- Proposition 3: Minimum Tier Depth.

These are formal structural claims, not empirical hypotheses. No hypothesis is tested in this paper. The paper does not report an implementation, a benchmark, or empirically measured performance.

### Foreknowledge of data or evidence

Data does not yet exist. No part of the data that will be used for this analysis plan exists, and no part will be generated until after this plan is registered.

### Explanation of foreknowledge and managing unintended influences

Not applicable. No data has been collected, observed, or generated. This is a formal architecture paper, not an empirical study.

The paper does not report:
- An implementation of AetherFlow.
- A simulation or benchmark of AetherFlow.
- Empirically measured performance figures.

The illustrative worked example in Section 5 applies the formulas under stated hypothetical parameters. It is explicitly labeled as an illustration, not a measurement.

All operational figures cited for Git and Scion throughout the paper are drawn from the cited published sources, not independently measured by this author.

No pilot analysis has been conducted. No data will be generated until after registration.

---

## Research Design

### Study type

Other: Formal architecture paper. The paper specifies a source-control architecture (AetherFlow) built on three pillars and formalizes three definitions with three propositions. No empirical data is collected, no experiment is run, and no simulation is performed.

### Intention for causal interpretation

No causal relationship inferred: This study is not intended to inform a causal relationship.

### Blinding of experimental treatments

No blinding is involved.

### Additional blinding during research or analysis

Not applicable. No experimental treatments, no human subjects, no blinding procedures.

### Study design

This is a formal architecture paper. The study design is conceptual and mathematical, not empirical.

Structure:

1. Architecture specification (Section 3): Three pillars are specified —
   (a) Lock-Free Merge Entry,
   (b) Post-Merge Verification Layer,
   (c) Proactive Remediation Agents.

2. Formal specification (Section 3): Three definitions are stated —
   (a) Dynamic Conflict Window: W(cᵢ, cⱼ) = 1 − exp(−κ·O·e^(−τ/θ))
   (b) Post-Merge Verification Operator: V(c) = ⊕_V(δ_i, {V(p)}, CI(c_i))
   (c) Auto-Remediation Bound: P(Remediation) ≥ 1 − (λ_fail/μ_remediate)^K · e^(−γ·T_react)

3. Three propositions are proven:
   - Proposition 1: Admission Independence.
   - Proposition 2: Monotonicity of Conflict Window.
   - Proposition 3: Minimum Tier Depth.

4. Illustrative worked example (Section 5): The formulas are applied under stated hypothetical parameters (ρ = 0.6, γ = 0.15, T_react = 8). This is an illustration of the formulas, not a benchmark or simulation of a real system.

5. Comparative positioning (Section 6): AetherFlow's specified properties are positioned against Git's merge queues, speculative gating, and pre-submit + post-submit CI.

No randomization. No experimental manipulation. No human subjects. No data collection. No implementation. No benchmark.

Units of analysis:
- Formal definition (primary unit).
- Architectural pillar (secondary unit).
- Structural proposition (tertiary unit).

No between-subject or within-subject design. No counterbalancing.

### Randomization

No data

---

## Sampling

### Data collection procedures

This is a formal architecture paper. No new data is collected. No human subjects are involved. No recruiting occurs.

Data sources are published documents only:

1. Anthropic. (2026). Redesigning Source Control at Anthropic. Anthropic Research. https://www.anthropic.com/research/redesigning-source-control — the sole source for all Scion-specific architectural claims.

2. Baladi, S. (2026a). Rethinking Source Control for Agentic Software Engineering. Zenodo. https://doi.org/10.5281/zenodo.23934465 — the author's own directly preceding paper.

3. Baladi, S. (2026b). AetherGit: Scalable Source Control for Autonomous AI Agents. Zenodo. https://doi.org/10.5281/zenodo.23966896 — the companion storage-layer paper.

4. Ananthanarayanan, S., Ardekani, M. S., Haenikel, D., et al. (2019). Keeping Master Green at Scale. Proceedings of EuroSys 2019. https://doi.org/10.1145/3302424.3303970 — speculative merge systems.

5. Brun, Y., Holmes, R., Ernst, M. D., & Notkin, D. (2011). Proactive Detection of Collaboration Conflicts. Proceedings of ESEC/FSE 2011. https://doi.org/10.1145/2025113.2025139 — semantic conflicts.

6. Corbett, J. C., Dean, J., Epstein, M., et al. (2013). Spanner: Google's Globally-Distributed Database. ACM TOCS, 31(3). https://doi.org/10.1145/2491245 — background on the authoritative server tier.

7. Fowler, M. (2006). Continuous Integration. https://martinfowler.com/articles/continuousIntegration.html — CI background.

8. Garcia-Molina, H., & Salem, K. (1987). Sagas. Proceedings of the 1987 ACM SIGMOD Conference. https://doi.org/10.1145/38713.38742 — compensating actions.

9. Herlihy, M. (1991). Wait-Free Synchronization. ACM TOPLAS, 13(1), 124–149. https://doi.org/10.1145/114005.102808 — lock-free progress.

10. Kung, H. T., & Robinson, J. T. (1981). On Optimistic Methods for Concurrency Control. ACM TODS, 6(2), 213–226. https://doi.org/10.1145/319566.319567 — optimistic concurrency.

11. Little, J. D. C. (1961). A Proof for the Queuing Formula: L = λW. Operations Research, 9(3), 383–387. https://doi.org/10.1287/opre.9.3.383 — Little's law.

12. Luo, Q., Hariri, F., Eloussi, L., & Marinov, D. (2014). An Empirical Analysis of Flaky Tests. Proceedings of FSE 2014. https://doi.org/10.1145/2635868.2635920 — flaky tests.

13. Potvin, R., & Levenberg, J. (2016). Why Google Stores Billions of Lines of Code in a Single Repository. CACM, 59(7), 78–87. https://doi.org/10.1145/2854146 — comparator system (Piper).

14. Sapling SCM. (n.d.). Sapling: A Scalable, User-Friendly Source Control System. Meta Platforms. https://sapling-scm.com/ — comparator system.

15. Chacon, S., & Straub, B. (2014). Pro Git (2nd ed.). Apress. https://git-scm.com/book — baseline system (Git).

16. Kleinrock, L. (1975). Queueing Systems, Volume 1: Theory. Wiley-Interscience. — queueing theory.

Inclusion criteria:
- Publicly accessible architectural descriptions and documentation.
- Peer-reviewed or officially published sources.
- Sources directly relevant to the three pillars or three formal definitions.

Exclusion criteria:
- Internal design documents or source code not publicly available.
- Independent benchmark data (none is available for AetherFlow).
- Any claim that cannot be traced to a published source.

No data will be generated before registration. The documents themselves exist publicly, but they have not been collected, coded, or analyzed for this protocol.

Expected duration: not applicable (document analysis only).

### Sample size

Sample size is not defined in the conventional sense because this is a formal architecture paper, not an empirical study.

Units of analysis and planned sample sizes:

1. Comparator systems: 4 (Git + merge queues, speculative gating, pre-submit + post-submit CI, AetherFlow).

2. Published sources: 16 primary references (see Data collection procedures).

3. Formal definitions: 3 (Dynamic Conflict Window, Post-Merge Verification Operator, Auto-Remediation Bound).

4. Propositions: 3 (Admission Independence, Monotonicity, Minimum Tier Depth).

5. Architectural pillars: 3 (Lock-Free Merge Entry, Post-Merge Verification Layer, Proactive Remediation Agents).

6. Illustrative worked example: 1 (Section 5, hypothetical parameters).

7. Comparative table: 1 (Section 6, AetherFlow vs. existing models).

Expected total sample:
- Comparator systems: 4
- Published sources: 16
- Formal definitions: 3
- Propositions: 3
- Architectural pillars: 3
- Illustrative example: 1
- Comparative table: 1

No conditions, treatments, or clusters. No multi-level or mixed design.

### Sample size rationale

The sample size is determined by the scope of the published material, not by power analysis.

- AetherFlow is specified in this paper (16 references).
- Git + merge queues, speculative gating, and pre-submit + post-submit CI are selected as comparator systems because each represents a distinct architectural approach to integration.
- The three formal definitions and three propositions are derived from the published material and the author's own prior work (Baladi, 2026a; Baladi, 2026b).

No statistical power analysis is applicable because this is a formal architecture paper, not a hypothesis test.

A larger empirical benchmark (implementation of the three pillars, instrumentation of λ_fail and μ_remediate) is proposed as future work in Section 10.

### Starting and stopping rules

Starting rule:

Document analysis begins with the publication of Anthropic's October 2026 disclosure (Reference 1) and the author's prior papers (References 2–3). There is no pilot phase.

Stopping rule:

The analysis terminates when:
1. All three pillars have been specified (Section 3).
2. All three definitions have been stated (Section 3).
3. All three propositions have been proven (Section 3).
4. The illustrative worked example has been presented (Section 5).
5. The comparative positioning has been completed (Section 6).
6. The limitations have been stated (Section 9).

No sequential testing or early stopping is involved. The paper is not an empirical study.

The proposed implementation and benchmark (Section 10) have not been executed. If executed in the future, their starting and stopping rules would be specified in a separate registration.

---

## Variables

### Manipulated variables

None. This is a formal architecture paper. No variables are manipulated. No treatments or conditions are administered. No randomization is involved.

The paper specifies an architecture and formalizes three definitions. It does not assign conditions, treatments, or arms.

The illustrative worked example in Section 5 applies the formulas under stated hypothetical parameters (ρ = 0.6, γ = 0.15, T_react = 8). These are not manipulated variables — they are illustrative values chosen for clarity of exposition, not measured or assigned.

### Measured variables

This paper does not report empirical measurements. The variables below are analytical constructs drawn from the formal specification.

A. Formal definitions (3 variables):
- D1: Dynamic Conflict Window — W(cᵢ, cⱼ) = 1 − exp(−κ·O·e^(−τ/θ)). Measured as: formal statement; parameters (κ, θ, O, τ).
- D2: Post-Merge Verification Operator — V(c) = ⊕_V(δ_i, {V(p)}, CI(c_i)). Measured as: formal statement; three-valued range (verified, failed, tainted).
- D3: Auto-Remediation Bound — P(Remediation) ≥ 1 − (λ_fail/μ_remediate)^K · e^(−γ·T_react). Measured as: formal statement; parameters (λ_fail, μ_remediate, K, T_react, γ).

B. Propositions (3 variables):
- P1: Admission Independence — measured as: proven/not proven.
- P2: Monotonicity of Conflict Window — measured as: proven/not proven.
- P3: Minimum Tier Depth — measured as: proven/not proven.

C. Architectural pillars (3 variables):
- L1: Lock-Free Merge Entry — measured as: specified/not specified.
- L2: Post-Merge Verification Layer — measured as: specified/not specified.
- L3: Proactive Remediation Agents — measured as: specified/not specified.

D. Comparative properties (5 variables, Section 6):
- Verification placement (Git: before merge; Speculative: before merge; Pre-submit + post-submit: both; AetherFlow: after admission).
- Admission blocks on CI (Git: yes; Speculative: yes; Pre-submit + post-submit: pre-submit only; AetherFlow: no).
- Trunk invariant (Git: always green; Speculative: always green; Pre-submit + post-submit: green at pre-submit; AetherFlow: verified head green).
- Failure attribution (Git: per queued change; Speculative: per speculative build; Pre-submit + post-submit: culprit finding; AetherFlow: recursive, three-valued).
- Descendants of a failure (Git: not applicable; Speculative: not applicable; Pre-submit + post-submit: handled by triage; AetherFlow: marked tainted, not failed).
- Repair actor (Git: author/human; Speculative: author/human; Pre-submit + post-submit: human/tooling; AetherFlow: remediation agents with guardrails).
- Formal bound on repair (Git: none; Speculative: none; Pre-submit + post-submit: none; AetherFlow: Eq. 3–4, structural, unvalidated).

No covariates. No subsetting variables. No exclusion variables.

### Indices

No composite indices or derived variables are constructed.

The paper reports formal definitions, architectural specifications, and structural propositions — not numerical scores or composite indices.

The only numerical quantities reported are:
- The formula parameters in the illustrative worked example (κ = 3, θ = 4, ρ = 0.6, γ = 0.15, T_react = 8, K = 8). These are hypothetical illustrative values, not measured or combined into an index.
- Operational figures cited for Git and Scion are drawn from the cited published sources, not independently measured by this author. They are not combined into any index.

No composite index, score, or derived variable is constructed from the formal definitions or architectural pillars.

---

## Analysis Plan

### Statistical models

No statistical models are used. This is a formal architecture paper, not a hypothesis test. No inferential statistics are planned.

Analysis proceeds through five formal procedures:

Procedure 1 — Formal specification (Section 3):
Three definitions are stated and interpreted in prose:
- Definition 1: Dynamic Conflict Window.
- Definition 2: Post-Merge Verification Operator.
- Definition 3: Auto-Remediation Bound.

Each definition is stated as an explicit mathematical claim. No statistical estimation is involved.

Procedure 2 — Proof of propositions (Section 3, Appendix B):
Three propositions are stated and proven:
- Proposition 1: Admission Independence.
- Proposition 2: Monotonicity of Conflict Window.
- Proposition 3: Minimum Tier Depth.

Each proof is a formal derivation, not a statistical test.

Procedure 3 — Architectural specification (Section 3):
Three architectural pillars are specified. Each pillar is described as an architectural commitment, not a measured property.

Procedure 4 — Illustrative worked example (Section 5):
The formulas (Definitions 1–3) are applied under stated hypothetical parameters (κ = 3, θ = 4, ρ = 0.6, γ = 0.15, T_react = 8, K = 8). The bound is plotted as a function of K for three T_react values (2, 8, 20). This is an illustration of the formula, not a benchmark or simulation.

Procedure 5 — Comparative positioning (Section 6):
A table positions AetherFlow's specified properties against Git + merge queues, speculative gating, and pre-submit + post-submit CI. The rightmost column is phrased in terms of specification, not measurement.

No controls, no manipulation checks, no convergence criteria, no assumption tests.

### Transformations

No transformations are applied. No coding scheme, centering, recoding, logging, winsorizing, or other data transformation is performed.

The analysis works with:
- Formal mathematical statements (Equations 1–3).
- Architectural specifications (Section 3).
- Qualitative comparative properties (Section 6).

No numerical data is collected, coded, or transformed. The illustrative worked example (Section 5) uses stated hypothetical parameters (κ = 3, θ = 4, ρ = 0.6, γ = 0.15, T_react ∈ {2, 8, 20}, K ∈ {1, …, K_max}). These are not transformed — they are stated.

### Inference criteria

No p-values, Bayes factors, or model fit indices are used. The analysis is formal and architectural, not inferential.

Inferences are supported by:
1. Direct citation of the published architectural descriptions (Anthropic, 2026; Potvin & Levenberg, 2016; Corbett et al., 2013; Sapling SCM; Chacon & Straub, 2014).
2. Explicit distinction between (a) architectural claims reported in the source material, (b) structural inferences drawn from distributed-systems principles, and (c) self-reported operational figures that have not been independently verified.
3. Formal statements of the three definitions (Equations 1–3) and the three propositions (P1, P2, P3).

No one-tailed or two-tailed tests are used. No multiple-comparison correction is applied, because no hypothesis tests are performed.

The illustrative worked example in Section 5 is not an inferential test. It plots Equation 3 under stated hypothetical parameters. It does not establish that any real system satisfies those parameters.

### Data inclusion and exclusion

Inclusion criteria:
- Publicly accessible architectural descriptions of source-control systems (Git, Piper, Sapling/Mononoke, Scion).
- Published documentation of each system's own design.
- Peer-reviewed or officially published sources.
- Anthropic's October 2026 disclosure as the sole source for all Scion-specific claims.

Exclusion criteria:
- Internal design documents or source code not publicly available (Scion is not public at the time of writing).
- Independent benchmark data (none is available for AetherFlow).
- Any claim that cannot be traced to a published source.

Outliers:
No outliers are defined, because no numerical data are collected. All qualifying sources are included.

All observations (documents) meeting inclusion criteria are used. No subsetting is planned.

### Missing data

Not applicable. No empirical dataset is used, so no missing data arises.

Scion's source code and internal design documents are not publicly available. This absence is stated explicitly as a limitation of the manuscript (Section 9), not treated as missing data to be imputed.

No imputation is performed. No missing-data models are used.

### Other planned analysis

The paper proposes a future implementation and benchmark (Section 10). If executed, it would include:

1. Implementation of the three pillars: lock-free merge entry, post-merge verification layer, proactive remediation agents.

2. Instrumentation of λ_fail and μ_remediate under a real or realistically synthesized agentic request stream.

3. Measurement of observed P(Remediation) against the Equation 3 bound.

4. Instantiation of the verification operator ⊕_V for specific verification categories (build, test, semantic).

5. Execution of the empirical evaluation protocol proposed in Section 7.

This protocol has not been executed. It is presented as proposed future work, not as analysis performed for this manuscript.

---

## Other

### Context and additional information

Context of the research program:

AetherFlow is a formal architecture paper. It is a companion to AetherGit (Baladi, 2026b), which specifies a storage-layer architecture — always-online clients, sparse checkouts, lock-free incremental changesets, and a tiered cache — and which is itself a formal sequel to the author's structural analysis of Anthropic's published account of its Scion source-control system (Anthropic, 2026; Baladi, 2026a).

AetherFlow addresses a different layer: what happens after a changeset has been created, namely how it is admitted to shared history, how it is verified, and how failures are repaired. The two papers are methodologically independent; AetherFlow requires only that the underlying store expose an append-only changeset log with parent pointers, which AetherGit's changeset tuple provides.

What this registration does not include:

1. No implementation. AetherFlow has not been built. No benchmark has been executed. No empirical performance has been measured.
2. No independent verification of operational figures. All operational figures attributed to Git and Scion throughout the paper are drawn from the cited published sources, not independently measured by this author.
3. No causal claims. The paper's claims are structural and formal, not causal.
4. No integration with the author's other research programs. This paper is independent of the author's prior work on Research I (epistemic discipline) and Research II (production and control of representations). It is a direct companion to Baladi (2026b) on storage.

Related materials:

- Zenodo DOI: 10.5281/zenodo.23979129
- Official website: https://aetherflow-site.netlify.app
- GitHub: https://github.com/gitdeeper15/aetherflow
- ORCID: https://orcid.org/0009-0003-8903-0029

Primary external source:

Anthropic. (2026). Redesigning Source Control at Anthropic. Published October 13, 2026 (updated October 15, 2026). https://www.anthropic.com/research/redesigning-source-control

This is the sole source for all Scion-specific architectural and operational claims.

Comparator systems:

- Git + merge queues — Chacon & Straub (2014).
- Speculative gating — Ananthanarayanan et al. (2019).
- Pre-submit + post-submit CI — Potvin & Levenberg (2016).
- AetherFlow — this paper.

Ethics:

This study does not involve human subjects. No personal data is collected. All cited sources are public.

Protocol integrity:

The protocol is frozen at registration. Any change after registration will be documented as a protocol amendment with explicit rationale.

Next research stage:

Implementation of the three pillars; instrumentation and measurement of Equation 3 under synthetic or real agentic workload traces; per-category instantiation of the verification operator.

Version 1.0.0 — November 2026.

---

## Metadata

### Contributors

Samir Baladi

### Resource type

No resource type

### Description

AetherFlow is a formal architecture that replaces traditional merge queues with lock-free direct entry, backed by probabilistic post-merge verification and proactive auto-remediation agents.

The architecture is built on three pillars: lock-free merge entry, post-merge verification layer, and proactive remediation agents.

The paper gives three formal definitions:
(1) the dynamic conflict window W(cᵢ, cⱼ) = 1 − exp(−κ·O·e^(−τ/θ));
(2) the post-merge verification operator V(c) = ⊕_V(δ_i, {V(p)}, CI(c_i));
(3) the auto-remediation bound P(Remediation) ≥ 1 − (λ_fail/μ_remediate)^K · e^(−γ·T_react).

Three propositions are proven: admission independence, monotonicity of the conflict window, and a closed-form minimum tier depth for any target residual risk.

AetherFlow is the integration-layer complement to the AetherGit storage architecture. The paper reports no implementation, simulation, or benchmark.

Version 1.0.0 — November 2026.

DOI (Zenodo): 10.5281/zenodo.23979129
Website: https://aetherflow-site.netlify.app

### Registration Type

OSF Preregistration

### Registry

OSF Registries

### Associated project

https://osf.io/8k5gx

### Date Created

Nov 6, 2026, 9:58 AM

### Date registered

Nov 6, 2026, 9:58 AM

### Subjects

- Engineering
- Software Engineering
- Computer Sciences
- Physical Sciences and Mathematics

### Tags

- AetherFlow
- agentic software engineering
- auto-remediation
- conflict resolution
- distributed systems
- Distributed Systems
- formal methods
- Formal Methods
- merge queues
- post-merge verification
- source control

### Affiliated Institutions

No affiliated institutions

### Funder Names

No information

### Language

No language

### Associated project

https://osf.io/8k5gx

### Internet Archive link

https://archive.org/details/osf-registrations-92y3w-v1

### License

CC-By Attribution 4.0 International

### Registration DOI

10.17605/OSF.IO/92Y3W

---

## Citations

### APA

Baladi, S. (2026, November 6). AetherFlow: Automated Post-Merge Verification and Dynamic Conflict Resolution in Multi-Agent Programming Environments. OSF. https://doi.org/10.17605/OSF.IO/92Y3W

### MLA

Baladi, Samir. "AetherFlow: Automated Post-Merge Verification and Dynamic Conflict Resolution in Multi-Agent Programming Environments." OSF, 6 Nov. 2026. Web.

### Chicago

Baladi, Samir. 2026. "AetherFlow: Automated Post-Merge Verification and Dynamic Conflict Resolution in Multi-Agent Programming Environments." OSF. November 6. doi:10.17605/OSF.IO/92Y3W.

### BibTeX

```bibtex
@misc{baladi2026aetherflow_osf,
  author       = {Baladi, Samir},
  title        = {{AetherFlow: Automated Post-Merge Verification and Dynamic Conflict Resolution in Multi-Agent Programming Environments}},
  year         = {2026},
  month        = nov,
  day          = {6},
  publisher    = {OSF},
  doi          = {10.17605/OSF.IO/92Y3W},
  url          = {https://doi.org/10.17605/OSF.IO/92Y3W},
  note         = {OSF Preregistration. Associated project: https://osf.io/8k5gx}
}
```

---

Source: Center for Open Science · OSF Registries
Retrieved: 2026-11-06
