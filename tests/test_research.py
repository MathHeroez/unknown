"""Tests for reproducibility and basic invariants of the research prototype."""

from __future__ import annotations

import numpy as np
import pytest

from dirac_t3 import count_states
from random_baseline import (
    candidate_radii,
    normalize_volume,
    sample_unit_volume_radii,
    summarize,
    write_results,
)


def test_normalize_volume_enforces_unit_volume() -> None:
    radii = normalize_volume(np.array([2.0, 3.0, 5.0]))
    assert np.isclose(np.prod(radii), 1.0, atol=1e-12)


def test_normalize_volume_rejects_invalid_input() -> None:
    with pytest.raises(ValueError):
        normalize_volume(np.array([1.0, 2.0]))
    with pytest.raises(ValueError):
        normalize_volume(np.array([1.0, 0.0, 2.0]))


def test_candidate_has_unit_volume() -> None:
    assert np.isclose(np.prod(candidate_radii()), 1.0, atol=1e-12)


def test_sampling_is_deterministic_and_unit_volume() -> None:
    first = sample_unit_volume_radii(20, np.random.default_rng(1234))
    second = sample_unit_volume_radii(20, np.random.default_rng(1234))
    np.testing.assert_array_equal(first, second)
    np.testing.assert_allclose(np.prod(first, axis=1), 1.0, atol=1e-12)


def test_sampling_rejects_nonpositive_sample_count() -> None:
    with pytest.raises(ValueError):
        sample_unit_volume_radii(0, np.random.default_rng(1))


def test_count_states_is_nonnegative() -> None:
    assert count_states((1.0, 1.0, 1.0), Lambda=12, cutoff=5) >= 0


def test_summary_rank_is_lower_is_better() -> None:
    summary = summarize(3, np.array([1, 2, 3, 4]))
    assert summary["rank"] == 3
    assert summary["strictly_better"] == 2


def test_write_results_writes_header_and_rows(tmp_path) -> None:
    output = tmp_path / "baseline.csv"
    radii = np.array([[1.0, 1.0, 1.0]])
    write_results(output, radii, np.array([7]))
    assert output.read_text(encoding="utf-8").splitlines() == [
        "r1,r2,r3,N",
        "1.0,1.0,1.0,7",
    ]
