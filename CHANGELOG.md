# AetherFlow — Changelog

## [2.0.0] — 2026-11-06

### Empirical Implementation

First implementation of AetherFlow formal architecture.

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

### Changed

- `VERSION`: 1.0.0 → 2.0.0
- `CHANGELOG.md`: this entry

### Technical Notes

- `pyproject.toml` uses PEP 621
- Python 3.9+ required
- `scikit-learn` moved to `[experiments]` extras
- CLI uses `>=` instead of Unicode `≥`

---

## [1.0.0] — 2026-11-05

### Initial Program Manuscript

First public release: formal architecture proposal, 18-page PDF, 3 definitions, 3 propositions, 3 architectural pillars, 4 figures, 17 references.

No implementation, no empirical results.
