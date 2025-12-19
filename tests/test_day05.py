import pytest

from app.days.day05 import (
    build_complete_ranges,
    count_total_numbers_in_ranges,
    get_ingredients,
    get_fresh_ranges,
    has_overlap,
    is_fresh,
    is_in_rage,
    merge_ranges,
)


def test_get_fresh_ranges_basic():
    puzzle_input = "1-3\n" "5-7\n\n" "10\n" "20\n"

    result = get_fresh_ranges(puzzle_input)

    assert result == ["1-3", "5-7"]


def test_get_ingredients_basic():
    puzzle_input = "1-3\n" "5-7\n\n" "10\n" "20\n"

    result = get_ingredients(puzzle_input)

    assert result == ["10", "20"]


@pytest.mark.parametrize(
    "number, range_str, expected",
    [
        (1, "1-3", True),  # start boundary
        (2, "1-3", True),  # inside range
        (3, "1-3", True),  # end boundary
        (0, "1-3", False),  # below range
        (4, "1-3", False),  # above range
    ],
)
def test_is_in_rage(number, range_str, expected):
    assert is_in_rage(number, range_str) is expected


def test_is_fresh_true_when_any_range_matches():
    fresh_ranges = ["1-3", "10-20"]

    assert is_fresh("2", fresh_ranges) is True
    assert is_fresh("15", fresh_ranges) is True


def test_is_fresh_false_when_no_ranges_match():
    fresh_ranges = ["1-3", "10-20"]

    assert is_fresh("5", fresh_ranges) is False
    assert is_fresh("25", fresh_ranges) is False


def test_is_fresh_with_single_range():
    fresh_ranges = ["100-200"]

    assert is_fresh("150", fresh_ranges) is True
    assert is_fresh("99", fresh_ranges) is False


def test_full_integration_example():
    puzzle_input = "1-3\n" "5-7\n\n" "2\n" "4\n" "6\n"

    fresh_ranges = get_fresh_ranges(puzzle_input)
    ingredients = get_ingredients(puzzle_input)

    results = [is_fresh(ingredient, fresh_ranges) for ingredient in ingredients]

    assert results == [True, False, True]


@pytest.mark.parametrize(
    "existing, start, end, expected",
    [
        ([(1, 3)], 2, 4, True),  # partial overlap
        ([(1, 3)], 3, 5, True),  # touching at boundary
        ([(1, 3)], 0, 1, True),  # touching at boundary
        ([(1, 3)], 4, 6, False),  # no overlap
        ([(5, 10)], 1, 4, False),  # completely before
        ([(5, 10)], 1, 20, True),  # fully covering
    ],
)
def test_has_overlap(existing, start, end, expected):
    assert has_overlap(existing, start, end) is expected


def test_merge_ranges_single_overlap():
    existing = [(1, 3)]
    result = merge_ranges(existing, 2, 5)

    assert result == [(1, 5)]


def test_merge_ranges_multiple_overlaps():
    existing = [(1, 3), (6, 8)]
    result = merge_ranges(existing, 2, 7)

    assert result == [(1, 8)]


def test_merge_ranges_no_overlap_keeps_existing():
    existing = [(1, 3)]
    result = merge_ranges(existing, 5, 7)

    assert sorted(result) == [(1, 3), (5, 7)]


def test_build_complete_ranges_single_range():
    fresh_ranges = ["1-3"]

    result = build_complete_ranges(fresh_ranges)

    assert result == [(1, 3)]


def test_build_complete_ranges_non_overlapping():
    fresh_ranges = ["1-3", "5-7"]

    result = build_complete_ranges(fresh_ranges)

    assert sorted(result) == [(1, 3), (5, 7)]


def test_build_complete_ranges_overlapping():
    fresh_ranges = ["1-3", "2-6"]

    result = build_complete_ranges(fresh_ranges)

    assert result == [(1, 6)]


def test_build_complete_ranges_chain_overlap():
    fresh_ranges = ["1-3", "5-7", "2-6"]

    result = build_complete_ranges(fresh_ranges)

    assert result == [(1, 7)]


def test_build_complete_ranges_unsorted_input():
    fresh_ranges = ["10-12", "1-3", "4-9"]

    result = build_complete_ranges(fresh_ranges)
    total = count_total_numbers_in_ranges(result)

    assert total == 12


def test_ranges_build_and_count_integration():
    fresh_ranges = ["1-3", "5-7", "2-6"]

    complete = build_complete_ranges(fresh_ranges)
    total = count_total_numbers_in_ranges(complete)

    assert complete == [(1, 7)]
    assert total == 7
