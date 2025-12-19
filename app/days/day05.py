"""Advent of Code 2025 - Day 05"""


def part1(puzzle_input: str):
    count = 0
    fresh_ranges = get_fresh_ranges(puzzle_input)
    ingredients = get_ingredients(puzzle_input)
    for ingredient in ingredients:
        if is_fresh(ingredient, fresh_ranges):
            count += 1

    return count


def part2(puzzle_input: str):
    complete_ranges = build_complete_ranges(get_fresh_ranges(puzzle_input))
    return count_total_numbers_in_ranges(complete_ranges)


# Get a list of ingredients from the puzzle input
def get_ingredients(puzzle_input: str) -> list[str]:
    return puzzle_input.split("\n\n")[1].strip().splitlines()


def get_fresh_ranges(puzzle_input: str) -> list[str]:
    return puzzle_input.split("\n\n")[0].strip().splitlines()


def is_fresh(ingredient: str, fresh_ranges: list[str]) -> bool:
    """Check if the ingredient contains any fresh numbers within the given ranges."""
    for range_str in fresh_ranges:
        if is_in_rage(int(ingredient), range_str):
            return True
    return False


def is_in_rage(number: int, range_str: str) -> bool:
    """Check if a number is within the given range string."""
    start_str, end_str = range_str.split("-")
    start, end = int(start_str), int(end_str)
    return start <= number <= end


def build_complete_ranges(fresh_ranges: list[str]) -> list[tuple[int, int]]:
    """Convert range strings into a list of tuples representing the ranges."""
    complete_ranges = []
    for range_str in fresh_ranges:
        start_str, end_str = range_str.split("-")
        start, end = int(start_str), int(end_str)
        if len(complete_ranges) == 0:
            complete_ranges.append((start, end))
        else:
            if has_overlap(complete_ranges, start, end):
                complete_ranges = merge_ranges(complete_ranges, start, end)
            else:
                complete_ranges.append((start, end))
        print(complete_ranges)
    return complete_ranges


def has_overlap(complete_ranges: list[tuple[int, int]], start: int, end: int) -> bool:
    """Check if the given range overlaps with any existing ranges."""
    for existing_start, existing_end in complete_ranges:
        if start <= existing_end and end >= existing_start:
            return True
    return False


def merge_ranges(
    complete_ranges: list[tuple[int, int]], start: int, end: int
) -> list[tuple[int, int]]:
    """Merge the given range with overlapping existing ranges."""
    merged_ranges = []
    new_start, new_end = start, end
    for existing_start, existing_end in complete_ranges:
        if new_start <= existing_end and new_end >= existing_start:
            new_start = min(new_start, existing_start)
            new_end = max(new_end, existing_end)
        else:
            merged_ranges.append((existing_start, existing_end))
    merged_ranges.append((new_start, new_end))
    return merged_ranges


def count_total_numbers_in_ranges(complete_ranges: list[tuple[int, int]]) -> int:
    """Count the total numbers covered by the given ranges."""
    total = 0
    for start, end in complete_ranges:
        total += end - start + 1
    return total
