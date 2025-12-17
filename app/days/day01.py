from typing import Optional


def part1(puzzle_input: str) -> Optional[int]:
    """Sample part1: count number of lines in the input."""
    if not puzzle_input:
        return 0
    return len([l for l in puzzle_input.splitlines() if l.strip()])


def part2(puzzle_input: str) -> Optional[int]:
    """Sample part2: sum integer lines in the input (ignores non-int)."""
    total = 0
    for line in puzzle_input.splitlines():
        s = line.strip()
        if not s:
            continue
        try:
            total += int(s)
        except ValueError:
            continue
    return total
