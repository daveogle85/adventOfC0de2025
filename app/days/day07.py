from functools import lru_cache


def part1(puzzle_input: str):
    grid = get_grid(puzzle_input)
    start_index = get_start_index(grid[0])
    visited = set()
    return count_splitters(grid, 0, start_index, visited)


def get_grid(puzzle_input: str) -> list[str]:
    return puzzle_input.splitlines()


def get_start_index(first_line: str) -> int:
    return first_line.index("S")


def move_down_to_splitter(grid: list[str], row: int, col: int) -> int:
    for r in range(row + 1, len(grid)):
        if grid[r][col] == "^":
            return r
    return -1


def is_out_of_bounds(grid: list[str], row: int, col: int) -> bool:
    return col < 0 or col >= len(grid[0]) or row < 0 or row >= len(grid)


def count_splitters(grid, row: int, col: int, visited):
    if is_out_of_bounds(grid, row, col):
        return 0

    splitter_row = move_down_to_splitter(grid, row, col)
    if splitter_row == -1:
        return 0

    pos = (splitter_row, col)
    if pos in visited:
        return 0

    visited.add(pos)

    # recurse left and right from the splitter
    return (
        1
        + count_splitters(grid, splitter_row, col - 1, visited)
        + count_splitters(grid, splitter_row, col + 1, visited)
    )


def part2(puzzle_input: str) -> int:
    grid = puzzle_input.splitlines()
    start_col = grid[0].index("S")

    @lru_cache(maxsize=None)
    def count_timelines(row: int, col: int) -> int:
        # Bounds check
        if is_out_of_bounds(grid, row, col):
            return 0

        # # Move down to next splitter
        splitter_row = move_down_to_splitter(grid, row, col)
        if splitter_row == -1:
            # No splitter below → one timeline ends
            return 1

        # Quantum splitting: left and right paths
        return count_timelines(splitter_row, col - 1) + count_timelines(
            splitter_row, col + 1
        )

    return count_timelines(0, start_col)
