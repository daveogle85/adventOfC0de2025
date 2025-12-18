"""Advent of Code 2025 - Day 04"""


def part1(puzzle_input: str):
    grid = get_grid(puzzle_input)
    total_adjacent = find_total_movable_rolls(grid)[0]
    return total_adjacent


def part2(puzzle_input: str):
    grid = get_grid(puzzle_input)
    total_adjacent, grid = find_total_movable_rolls(grid)
    result = total_adjacent
    grid = remove_all_rolls(grid)
    while total_adjacent > 0:
        (total_adjacent, grid) = find_total_movable_rolls(grid)
        result += total_adjacent
        grid = remove_all_rolls(grid)
    return result


def find_total_movable_rolls(grid: list[list[str]]) -> tuple[int, list[list[str]]]:
    """Find total rolls that can be moved (i.e., have fewer than 4 adjacent rolls)."""
    roll_marker = "@"
    total_movable = 0

    for row_index, row in enumerate(grid):
        for col_index, _ in enumerate(row):
            if grid[row_index][col_index] != roll_marker:
                continue
            roll_coords = (row_index, col_index)
            new_grid = find_number_of_adjacent_rolls(roll_coords, grid)
            if new_grid is not None:
                grid = new_grid
                total_movable += 1

    return total_movable, grid


def remove_all_rolls(grid: list[list[str]]) -> list[list[str]]:
    return [[cell if cell != "m" else "." for cell in row] for row in grid]


def find_number_of_adjacent_rolls(
    roll_coords: tuple[int, int], grid: list[list[str]]
) -> list[list[str]] | None:
    """Count how many adjacent coordinates (including diagonals) contain '@'."""
    total_adjacent = 0
    max_row = len(grid)
    max_col = len(grid[0]) if max_row > 0 else 0

    r, c = roll_coords
    roll_marker = "@"
    marked_for_replacement = "m"

    # Check all 8 adjacent directions (up, down, left, right, and diagonals)
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),  # up-left, up, up-right
        (0, -1),
        (0, 1),  # left, right
        (1, -1),
        (1, 0),
        (1, 1),  # down-left, down, down-right
    ]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if (
            0 <= nr < max_row
            and 0 <= nc < max_col
            and (grid[nr][nc] == roll_marker or grid[nr][nc] == marked_for_replacement)
        ):
            total_adjacent += 1

    if total_adjacent < 4:
        grid[r][c] = "m"
        return grid

    return None


def get_grid(puzzle_input: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in puzzle_input.splitlines():
        rows.append(list(line.strip()))
    return rows
