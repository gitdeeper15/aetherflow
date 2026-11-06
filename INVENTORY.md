# AetherFlow — Complete Inventory

**Version:** 2.0.0 (manuscript revision) / 0.1.0a1 (PyPI package)
**Release Date:** 2026-11-06
**Author:** Samir Baladi
**Email:** gitdeeper@gmail.com
**ORCID:** [0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029)
**License:** MIT (code) · CC-BY-4.0 (docs, manuscript, figures)
**Status:** Empirical Implementation · Reference implementation · Preliminary results
**DOI (Zenodo):** [10.5281/zenodo.23979129](https://doi.org/10.5281/zenodo.23979129)
**DOI (OSF):** [10.17605/OSF.IO/92Y3W](https://doi.org/10.17605/OSF.IO/92Y3W)

---

## Repository Links

| Platform | URL | Role | Status |
|----------|-----|------|--------|
| GitHub | https://github.com/gitdeeper15/aetherflow | Primary | ✅ Active |
| GitLab | https://gitlab.com/gitdeeper15/aetherflow | Mirror | ✅ Active |
| Codeberg | https://codeberg.org/gitdeeper15/aetherflow | Mirror | ✅ Active |
| Bitbucket | https://bitbucket.org/gitdeeper15/aetherflow | Mirror | ✅ Active |
| PyPI | https://pypi.org/project/aetherflow/ | Python package | ✅ **Published (0.1.0a1)** |
| Zenodo | https://doi.org/10.5281/zenodo.23979129 | DOI (manuscript) | ✅ Published |
| OSF | https://doi.org/10.17605/OSF.IO/92Y3W | Registration | ✅ Published |
| Website | https://aetherflow-site.netlify.app | Live documentation | ✅ Active |
| ORCID | https://orcid.org/0009-0003-8903-0029 | Identity | ✅ Active |

> **PyPI note:** Published as `aetherflow` version `0.1.0a1` (alpha). Install with
> `pip install aetherflow==0.1.0a1`. The alpha status signals that the API may
> change before `1.0.0`. This is a reference implementation, not a production system.

---

## Root Files

| File | Purpose |
|------|---------|
| `.gitignore` | Git ignore rules |
| `AUTHORS.md` | Contributors |
| `CHANGELOG.md` | Version history |
| `CITATION.cff` | Citation metadata (v2.0.0) |
| `CONTRIBUTING.md` | Contribution guidelines |
| `INVENTORY.md` | Complete inventory (this file) |
| `LICENSE` | MIT + CC-BY-4.0 |
| `PROJECT_SUMMARY.txt` | One-page summary (v2.0.0) |
| `README.md` | Main documentation (v2.0.0) |
| `VERSION` | 2.0.0 |
| `manifest.json` | Project manifest (v2.0.0) |
| `scientific_state.json` | Scientific state record (v2.0.0) |
| `requirements.txt` | Python deps |
| `pyproject.toml` | PEP 621 build config (v0.1.0a1) |
| `upload_aetherflow.py` | PyPI uploader script |

---

## Directories

| Directory | Purpose |
|-----------|---------|
| `src/aetherflow/` | Reference implementation (v2.0.0) |
| `tests/` | Test suite (24 tests, 98% coverage) |
| `experiments/` | 5 experiment protocols + results |
| `PUBLICATION/` | Manuscript, figures, Netlify |
| `DATA/` | Data (raw, processed, schemas) |
| `ANALYSIS/` | Analysis notes |
| `REPORTS/` | Governance/audit reports + v2.0.0 report |
| `EXTERNAL_REVIEW/` | Review records |
| `VALIDATION/` | Validation checks, schemas |
| `docs/` | Formal documents (4) + v2.0.0 implementation |
| `protocol/` | Methodological scope |
| `literature/` | Literature review (Git, Piper, Sapling, Scion) |
| `figures/` | Conceptual diagrams (4) |

---

## Source Code Structure (v2.0.0)

| Module | Purpose | Pillar |
|--------|---------|--------|
| `admission/log.py` | ChangesetLog (append-only log) | Pillar 1 |
| `verification/operator.py` | Three-valued verification operator | Pillar 2 |
| `verification/scheduler.py` | Adaptive verification scheduler | Pillar 2 |
| `remediation/bound.py` | Auto-remediation bound (Eq. 3) | Pillar 3 |
| `remediation/guardrails.py` | Test-weakening prevention | Pillar 3 |
| `conflict/window.py` | Dynamic conflict window (Eq. 1a) | Definition 1 |
| `models.py` | Changeset, Status, VerificationResult | — |
| `cli.py` | Command-line interface | — |

---

## Formal Definitions

| Document | Version | Status |
|----------|---------|--------|
| Definition 1 — Dynamic Conflict Window | 1.0.0 | ✅ Defined |
| Definition 2 — Post-Merge Verification Operator | 1.0.0 | ✅ Defined |
| Definition 3 — Auto-Remediation Bound | 1.0.0 | ✅ Defined |
| Three Architectural Pillars | 1.0.0 | ✅ Specified |

---

## Propositions

| # | Proposition | Status |
|---|-------------|--------|
| P1 | Admission Independence | ✅ Proven |
| P2 | Monotonicity of Conflict Window | ✅ Proven |
| P3 | Minimum Tier Depth | ✅ Proven |

---

## Empirical Results (v2.0.0)

| # | Experiment | Result | Status |
|---|------------|--------|--------|
| 1 | Conflict Window (Eq. 1a) | κ=2.892, θ=4.000, AUC=0.894 | ✅ |
| 2 | Remediation Bound (Eq. 3) | K=8 → P ≥ 1.0000 | ✅ |
| 3 | Attribution Accuracy | F1=1.000 (mitigated) | ✅ |
| 4 | Guardrail Effectiveness | 100% block rate (192/192) | ✅ |
| 5 | Scheduler Simulation | 2.5× speedup vs FIFO | ✅ |

> **Status note:** Experiment 1 uses synthetic data (self-consistency test).
> Experiments 2–5 use simulated logs. No real-world deployment evaluated.

---

## Key Results

| Benchmark | Metric | Value | Baseline | Improvement |
|-----------|--------|-------|----------|-------------|
| Integration Latency | Admission | `O(\|δ\|)` | Grows with queue depth (Eq. 5) | **Structural** (Prop. 1) |
| Queue Starvation | Rate | 0 | Possible near ρ_q = 1 | **Eliminated** (structural) |
| Conflict Resolution | Method | Agentic | Manual | **Design target** |
| Remediation Success | P(Remediation) | ≥ 99.2% | Human-dependent | **K = 8 suffices** (design target) |

> **Status note:** The "~100x faster" and "≥99.2% success" figures are
> **design targets, not results**. Only the structural claims (Prop. 1,
> Prop. 3) are proven. See Section 7 of the manuscript for the evaluation protocol.

---

## Figures

| Figure | File | Status |
|--------|------|--------|
| 1 — Dynamic Conflict Window | `PUBLICATION/figures/fig1_conflict_window.png` | ✅ Added |
| 2 — Post-Merge Verification Operator | `PUBLICATION/figures/fig2_verification_operator.png` | ✅ Added |
| 3 — Auto-Remediation Bound | `PUBLICATION/figures/fig3_remediation_bound.png` | ✅ Added |
| 4 — Three Architectural Pillars | `PUBLICATION/figures/fig4_architecture.png` | ✅ Added |

---

## References

17 references (see Section "References" of the manuscript, pages 17–18).

Key related identifiers:
- **Zenodo DOI (this manuscript):** [10.5281/zenodo.23979129](https://doi.org/10.5281/zenodo.23979129)
- **OSF Registration:** [10.17605/OSF.IO/92Y3W](https://doi.org/10.17605/OSF.IO/92Y3W)
- **PyPI Package:** [pypi.org/project/aetherflow](https://pypi.org/project/aetherflow/)
- **AetherGit (companion, 2026b):** [10.5281/zenodo.23966896](https://doi.org/10.5281/zenodo.23966896)
- **Prior work (2026a):** [10.5281/zenodo.23934465](https://doi.org/10.5281/zenodo.23934465)

---

## Dependencies

### Python (runtime — v2.0.0)

- `numpy >= 1.24.0`

### Python (dev)

- `pytest >= 7.0`
- `pytest-cov >= 4.0`
- `ruff >= 0.1`
- `mypy >= 1.0`

### Python (experiments — optional)

- `scikit-learn >= 1.3`
- `matplotlib >= 3.7`

### External APIs

- None (reference implementation; no API calls).

---

## Completion Summary

```

Project:              AetherFlow — Automated Post-Merge Verification and
Dynamic Conflict Resolution in Multi-Agent Programming
Environments
Version:              2.0.0 (manuscript) / 0.1.0a1 (PyPI package)
Status:               Empirical Implementation · Reference implementation
Formal Definitions:   3
Propositions:         3 (all proven)
Architectural Pillars: 3
Figures:              4
References:           17
Source files:         14 (src/aetherflow/)
Tests:                24 passed, 98% coverage
Experiments:          5/5 completed
PyPI package:         ✅ Published (aetherflow 0.1.0a1)
Real-world deployment: ❌ Not evaluated
Causal Claims:        None (formal analysis only)
License:              MIT (code) + CC-BY-4.0 (manuscript, figures, docs)
DOI (Zenodo):         10.5281/zenodo.23979129
DOI (OSF):            10.17605/OSF.IO/92Y3W
PyPI:                 https://pypi.org/project/aetherflow/

```

---

## Citation

### Primary Manuscript (AetherFlow v1.0.0)

```bibtex
@techreport{baladi2026aetherflow,
  author       = {Baladi, Samir},
  title        = {AetherFlow: Automated Post-Merge Verification and Dynamic
                  Conflict Resolution in Multi-Agent Programming Environments},
  institution  = {Ronin Institute / Rite of Renaissance},
  type         = {Research Paper},
  year         = {2026},
  month        = {November},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.23979129},
  url          = {https://doi.org/10.5281/zenodo.23979129},
  note         = {Initial Program Manuscript --- Formalization Stage.
                  Three formal definitions, three architectural pillars,
                  three propositions with proofs. No empirical results.}
}
```

Software Archive (PyPI + Zenodo)

```bibtex
@software{baladi2026aetherflow_v2,
  author       = {Baladi, Samir},
  title        = {{AetherFlow} v2.0.0: Empirical Implementation of Automated
                  Post-Merge Verification and Dynamic Conflict Resolution},
  year         = {2026},
  month        = {November},
  publisher    = {PyPI},
  version      = {0.1.0a1},
  doi          = {10.5281/zenodo.23979129},
  url          = {https://pypi.org/project/aetherflow/},
  note         = {Reference implementation.
                  Available via pip install aetherflow==0.1.0a1.}
}
```

---

Generated: 2026-11-06
Inventory Version: 2.0.0
