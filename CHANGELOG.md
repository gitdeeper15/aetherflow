# AetherFlow — Changelog

All notable changes to this research project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Version numbers track **manuscript revisions** at the formalization stage,
and follow **SemVer** for the PyPI package.

---

## [2.0.0] — 2026-11-06

### Empirical Implementation

First implementation of AetherFlow formal architecture.
Also published on **PyPI** as `aetherflow` (alpha release).

### Added — Source Code

- `src/aetherflow/` package with 5 modules (14 files):
  - `admission/` — ChangesetLog (Pillar 1)
  - `verification/` — operator, scheduler (Pillar 2)
  - `remediation/` — bound, guardrails (Pillar 3)
  - `conflict/` — window (Definition 1)
  - `models.py`, `cli.py`
- `pyproject.toml` — PEP 621 compliant
- 24 tests, 98% coverage

### Added — Experiments (all 5 completed)

| # | Experiment | Result |
|---|------------|--------|
| 1 | Conflict Window (Eq. 1a) | κ=2.892, θ=4.000, AUC=0.894 |
| 2 | Remediation Bound (Eq. 3) | K=8 → P ≥ 1.0000 |
| 3 | Attribution Accuracy | F1=1.000 (mitigated) |
| 4 | Guardrail Effectiveness | 100% block rate |
| 5 | Scheduler Simulation | 2.5x speedup |

### Added — Reports

- `REPORTS/v2.0.0/report.md` — full evaluation report

### Added — PyPI Publication

- Package: `aetherflow` on **PyPI**
- Version: `0.1.0a1` (alpha — API may change)
- URL: https://pypi.org/project/aetherflow/
- Install: `pip install aetherflow==0.1.0a1`

### Changed

- `VERSION`: 1.0.0 → 2.0.0
- `CITATION.cff`: 1.0.0 → 2.0.0 (version + date)
- `manifest.json`: 1.0.0 → 2.0.0
- `scientific_state.json`: 1.0.0 → 2.0.0
- `PROJECT_SUMMARY.txt`: 1.0.0 → 2.0.0
- `INVENTORY.md`: 1.0.0 → 2.0.0
- `README.md`: added PyPI badges, Installation section, v2.0.0 status
- `CHANGELOG.md`: this entry

### Technical Notes

- `pyproject.toml` uses PEP 621
- Python 3.9+ required
- `scikit-learn` moved to `[experiments]` extras
- CLI uses `>=` instead of Unicode `≥`
- PyPI package version `0.1.0a1` is separate from manuscript `VERSION=2.0.0`

### Related Identifiers

- **Zenodo DOI**: [10.5281/zenodo.23979129](https://doi.org/10.5281/zenodo.23979129)
- **OSF Registration**: [10.17605/OSF.IO/92Y3W](https://doi.org/10.17605/OSF.IO/92Y3W)
- **PyPI**: [pypi.org/project/aetherflow](https://pypi.org/project/aetherflow/)
- **GitHub Release**: [v2.0.0](https://github.com/gitdeeper15/aetherflow/releases/tag/v2.0.0)

### Status

| Dimension | Status |
|-----------|--------|
| Manuscript | Complete (18 pages, PDF) |
| Formal Definitions | 3 |
| Propositions | 3 (all proven) |
| Architectural Pillars | 3 |
| Figures | 4 |
| References | 17 |
| Implementation | ✅ Built (`src/aetherflow/`) |
| Tests | ✅ 24 passed, 98% coverage |
| Experiments | ✅ 5/5 completed |
| PyPI Package | ✅ Published (0.1.0a1) |
| Real-world deployment | ❌ Not evaluated |
| Causal claims | None (formal analysis only) |

---

## [1.0.0] — 2026-11-05

### Initial Program Manuscript

First public release: formal architecture proposal, 18-page PDF, 3 definitions, 3 propositions, 3 architectural pillars, 4 figures, 17 references.

No implementation, no empirical results.

---

**Last Updated:** 2026-11-06
**Current Version:** 2.0.0 (manuscript) / 0.1.0a1 (PyPI)
