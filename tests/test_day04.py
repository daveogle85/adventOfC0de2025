import pytest
from app.days.day04 import (
    part1,
    part2,
    find_number_of_adjacent_rolls,
    get_grid,
)


class TestGetGrid:
    """Test cases for the get_grid function."""

    def test_single_line(self):
        """Test converting a single line to a grid."""
        result = get_grid("@#@")
        assert result == [["@", "#", "@"]]

    def test_multiple_lines(self):
        """Test converting multiple lines to a grid."""
        result = get_grid("@#@\n#@#\n@#@")
        assert result == [["@", "#", "@"], ["#", "@", "#"], ["@", "#", "@"]]

    def test_with_whitespace(self):
        """Test that whitespace is stripped from each line."""
        result = get_grid("  @#@  \n  #@#  ")
        assert result == [["@", "#", "@"], ["#", "@", "#"]]

    def test_empty_input(self):
        """Test empty input."""
        result = get_grid("")
        assert result == []


class TestFindNumberOfAdjacentRolls:
    """Test cases for the find_number_of_adjacent_rolls function."""

    def test_no_adjacent_rolls(self):
        """Test when there are no adjacent rolls - should return grid with replacement."""
        grid = [["@", ".", "."], [".", ".", "."], [".", ".", "."]]
        result = find_number_of_adjacent_rolls((0, 0), grid)
        assert result is not None
        assert result[0][0] == "x"

    def test_one_adjacent_right(self):
        """Test with one adjacent roll to the right - should return grid with replacement."""
        grid = [["@", "@", "."], [".", ".", "."], [".", ".", "."]]
        result = find_number_of_adjacent_rolls((0, 0), grid)
        assert result is not None
        assert result[0][0] == "x"

    def test_multiple_adjacent(self):
        """Test with multiple adjacent rolls - should return grid with replacement."""
        grid = [["@", "@", "."], ["@", ".", "."], [".", ".", "."]]
        result = find_number_of_adjacent_rolls((0, 0), grid)
        assert result is not None
        assert result[0][0] == "x"

    def test_all_adjacent(self):
        """Test when all 8 adjacent positions contain '@' - should return None."""
        grid = [["@", "@", "@"], ["@", "@", "@"], ["@", "@", "@"]]
        result = find_number_of_adjacent_rolls((1, 1), grid)
        assert result is None

    def test_diagonal_adjacent(self):
        """Test diagonal adjacency - should return grid with replacement."""
        grid = [["@", ".", "."], [".", "@", "."], [".", ".", "."]]
        result = find_number_of_adjacent_rolls((1, 1), grid)
        assert result is not None
        assert result[1][1] == "x"

    def test_corner_position(self):
        """Test at corner (fewer possible adjacent positions) - should return grid with replacement."""
        grid = [["@", "@"], ["@", "."]]
        result = find_number_of_adjacent_rolls((0, 0), grid)
        assert result is not None
        assert result[0][0] == "x"

    def test_edge_position(self):
        """Test at edge with 3 adjacent - should return grid with replacement."""
        grid = [[".", "@", "."], ["@", "@", "@"], [".", ".", "."]]
        result = find_number_of_adjacent_rolls((0, 1), grid)
        assert result is not None
        assert result[0][1] == "x"

    def test_exactly_four_adjacent(self):
        """Test with exactly 4 adjacent - should return None."""
        grid = [[".", "@", "."], ["@", "@", "@"], [".", "@", "."]]
        result = find_number_of_adjacent_rolls((1, 1), grid)
        assert result is None


class TestPart1:
    """Test cases for the part1 function."""

    def test_single_roll_with_no_adjacent(self):
        """Test a single roll with no adjacent rolls."""
        result = part1("@")
        assert result == 1

    def test_single_roll_with_surrounding_rolls(self):
        """Test rolls surrounded by many other rolls."""
        puzzle = "@@@\n@@@\n@@@"
        result = part1(puzzle)
        # 4 corners with 3 adjacent each (< 4), so count = 4
        # 4 edges with 5 adjacent each (>= 4), so don't count
        # 1 center with 8 adjacent (>= 4), so don't count
        assert result == 4

    def test_no_rolls(self):
        """Test with no '@' characters."""
        result = part1("...\n...\n...")
        assert result == 0

    def test_roll_with_exactly_four_adjacent(self):
        """Test roll with exactly 4 adjacent (should NOT be replaced)."""
        puzzle = ".@.\n@@@\n.@."
        result = part1(puzzle)
        # Center roll at (1,1) has 4 adjacent rolls, so it should NOT be replaced
        # But the 4 edge rolls (0,1), (1,0), (1,2), (2,1) each have < 4 adjacent
        # With separate counting pass, all adjacencies are based on original grid
        assert result == 4

    def test_roll_with_three_adjacent(self):
        """Test rolls with < 4 adjacent (all should be replaced)."""
        puzzle = "@@@\n@..\n..."
        result = part1(puzzle)
        # All 4 rolls have < 4 adjacent, so all should be replaced
        assert result == 4


def test_part2_placeholder():
    """Test part2 (currently a stub)."""
    assert part2("") is None
