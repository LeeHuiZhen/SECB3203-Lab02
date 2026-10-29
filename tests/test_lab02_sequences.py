"""Lab 2 - Student test suite for biological sequence functions."""

import pytest

from lab02_sequences import (
    find_motif,
    gc_content,
    transcribe,
)


def test_find_motif_normal():
    """Normal test: finding non-overlapping motif matches in standard DNA."""
    assert find_motif("GATCGATC", "ATC") == [1, 5]


def test_find_motif_boundary_overlapping_and_case():
    """Boundary test: overlapping occurrences and case insensitivity."""
    assert find_motif("AAAA", "AA") == [0, 1, 2]
    assert find_motif("atgcgt", "CGT") == [3]
    assert find_motif("ATGC", "TTT") == []


def test_find_motif_invalid_empty_motif_raises():
    """Invalid input test: empty motif string must raise ValueError."""
    with pytest.raises(ValueError):
        find_motif("ATGCGT", "")


def test_gc_content_lowercase_and_boundaries():
    """Boundary test: lowercase sequence handling and extreme GC percentages."""
    assert gc_content("atgc") == pytest.approx(50.0)
    assert gc_content("GGCC") == pytest.approx(100.0)
    with pytest.raises(ValueError):
        gc_content("")
    with pytest.raises(ValueError):
        gc_content("ATGCN")


def test_transcribe_invalid_raises():
    """Invalid input test: transcribe rejects non-DNA bases and empty sequence."""
    with pytest.raises(ValueError):
        transcribe("ATGCN")
    with pytest.raises(ValueError):
        transcribe("")