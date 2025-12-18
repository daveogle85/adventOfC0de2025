"""Advent of Code 2025 - Day 03"""


def part1(puzzle_input: str):
    result = 0
    if not puzzle_input:
        return 0
    for line in puzzle_input.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            continue
        result += int(find_largest_number_from_string(stripped_line, 2))
    return result


def part2(puzzle_input: str):
    result = 0
    if not puzzle_input:
        return 0
    for line in puzzle_input.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            continue
        result += int(find_largest_number_from_string(stripped_line, 12))
    return result


def find_largest_number_from_string(bank: str, choices: int) -> str:
    current_index = 0
    result: list[str] = []
    for choice in range(choices):
        available_choices = bank[current_index : len(bank) - (choices - 1 - choice)]
        if not available_choices:
            break
        largest_int_index = available_choices.index(max(available_choices))
        result.append(available_choices[largest_int_index])
        current_index += largest_int_index + 1

    return "".join(result) if result else "0"
