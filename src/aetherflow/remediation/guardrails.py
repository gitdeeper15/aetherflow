"""Guardrails against test-weakening behavior."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class ViolationType(str, Enum):
    TEST_DELETED = "test_deleted"
    TEST_DISABLED = "test_disabled"
    TOLERANCE_WIDENED = "tolerance_widened"
    OUTSIDE_BLAST_RADIUS = "outside_blast_radius"


@dataclass
class Patch:
    files_changed: set[str]
    deleted_tests: set[str]
    disabled_tests: set[str]
    widened_assertions: list[str]
    blast_radius: set[str]


def check_guardrails(patch: Patch) -> list[ViolationType]:
    violations = []
    if patch.deleted_tests:
        violations.append(ViolationType.TEST_DELETED)
    if patch.disabled_tests:
        violations.append(ViolationType.TEST_DISABLED)
    if patch.widened_assertions:
        violations.append(ViolationType.TOLERANCE_WIDENED)
    if not patch.files_changed.issubset(patch.blast_radius):
        violations.append(ViolationType.OUTSIDE_BLAST_RADIUS)
    return violations
