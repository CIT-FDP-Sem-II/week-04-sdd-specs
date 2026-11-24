"""A small spec linter. No API calls.

It checks the shape of SPEC.md, not the quality of it - structure a machine
can see. Reading for meaning is still your job and your partner's.
"""

import re
from pathlib import Path

SPEC = (Path(__file__).parent.parent / "SPEC.md").read_text(encoding="utf-8")

REQUIRED_SECTIONS = [
    "Problem Statement",
    "Functional Requirements",
    "Non-Functional Requirements",
    "Out of Scope",
    "Acceptance Criteria",
    "Evaluation",
]


def test_spec_has_all_six_components():
    for section in REQUIRED_SECTIONS:
        assert section in SPEC, f"SPEC.md is missing: {section}"


def test_there_are_exactly_eight_acceptance_criteria():
    criteria = set(re.findall(r"\*\*AC-(\d+)\*\*", SPEC))
    assert len(criteria) == 8, f"found {len(criteria)} acceptance criteria, expected 8"


def test_every_acceptance_criterion_maps_to_a_requirement():
    """An AC that points at nothing is a wish with a number on it."""
    rows = re.findall(r"\*\*AC-\d+\*\*.*", SPEC)
    for row in rows:
        assert re.search(r"(FR|NFR)-\d+", row), f"AC with no requirement mapped: {row[:60]}"


def test_every_requirement_id_is_unique():
    ids = re.findall(r"\*\*((?:FR|NFR|AC)-\d+)\*\*", SPEC)
    assert len(ids) == len(set(ids)), "duplicate requirement IDs in SPEC.md"


MEASURABLE = re.compile(
    r"\d"                                   # 60 seconds, 80 lines, 10 pages
    r"|\b(one|two|three|four|five|six|seven|eight|nine|ten)\b"
    r"|\b(no|none|zero|every|all)\b",       # "appears in no file" is measurable
    re.IGNORECASE,
)


def test_non_functional_requirements_are_quantified():
    """An NFR with nothing countable in it is a wish with an ID on it.

    This is the check that catches "fast", "robust" and "user-friendly" -
    the three words that cause the most rework in Week 7.
    """
    rows = re.findall(r"\*\*NFR-\d+\*\*\s*\|([^|]*)\|", SPEC)
    assert rows, "no NFR rows found"
    for row in rows:
        assert MEASURABLE.search(row), f"NFR with nothing measurable in it: {row.strip()[:60]}"


def test_spec_contains_no_unquantified_weasel_words():
    """The words that look like requirements and are not."""
    weasel = ["user-friendly", "as fast as possible", "appropriately", "etc."]
    found = [w for w in weasel if w in SPEC.lower()]
    assert not found, f"unquantified wording in SPEC.md: {found}"
