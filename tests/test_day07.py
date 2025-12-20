import pytest
from app.days.day07 import (
    part1,
    part2,
    get_grid,
    get_start_index,
    move_down_to_splitter,
    count_splitters,
)


# ----------------------------
# Basic grid parsing tests
# ----------------------------
def test_get_grid():
    puzzle_input = "S..\n.^.\n..."
    grid = get_grid(puzzle_input)
    assert grid == ["S..", ".^.", "..."]


def test_get_start_index():
    assert get_start_index("..S..") == 2


def test_move_down_to_splitter_found():
    grid = ["S..", ".^.", "..."]
    assert move_down_to_splitter(grid, 0, 1) == 1


def test_move_down_to_splitter_not_found():
    grid = ["S..", "...", "..."]
    assert move_down_to_splitter(grid, 0, 1) == -1


# ----------------------------
# Part 1 - Classical splitters
# ----------------------------
def test_single_splitter():
    puzzle_input = "S.\n^.\n.."
    assert part1(puzzle_input) == 1


def test_no_double_counting_with_visited():
    puzzle_input = "..S..\n" "..^..\n" ".^.^.\n" "....."
    # Only count each splitter once
    assert part1(puzzle_input) == 3


def test_edge_column_bounds_part1():
    puzzle_input = "S....\n" "^...."
    assert part1(puzzle_input) == 1


# ----------------------------
# Part 2 - Quantum timelines
# ----------------------------
def test_single_splitter_part2():
    puzzle_input = "S.\n^.\n.."
    assert part2(puzzle_input) == 1


def test_edge_column_bounds_part2():
    puzzle_input = "S....\n" "^...."
    assert part2(puzzle_input) == 1
