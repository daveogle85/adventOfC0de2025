"""Advent of Code 2025 - Day 06"""


def part1(puzzle_input: str):
    total = 0
    problems = get_problems(puzzle_input)
    for numbers, operator in problems:
        total += solve_problem(numbers, operator)
    return total


def part2(puzzle_input: str):
    total = 0
    problems = get_problems_right_to_left(puzzle_input)
    for numbers, operator in problems:
        total += solve_problem(numbers, operator)
    return total


def get_problems(puzzle_input: str) -> list[tuple[list[int], str]]:
    """Return a list of problems in the format list of (number list, operator)."""
    lines = puzzle_input.strip().splitlines()
    # remove the last line which contains the operators
    operators = lines.pop(-1).strip().split()
    problems: list[tuple[list[int], str]] = []
    for line in lines:
        row = line.split()
        if len(problems) == 0:
            for operator in operators:
                problems.append(([], operator))
        for i, number in enumerate(row):
            problems[i][0].append(int(number.strip()))

    return problems


def get_problems_right_to_left(input_str: str) -> list[tuple[list[int], str]]:
    lines = input_str.rstrip("\n").splitlines()

    # Last line contains operators
    operators = lines[-1].split()
    operators = reversed(operators)
    data_lines = lines[:-1]

    # Normalize rows: make all rows the same length by padding with spaces
    max_len = max(len(line) for line in data_lines)
    grid = [line.ljust(max_len) for line in data_lines]

    rows = len(grid)
    cols = max_len

    problem_number = ""
    numbers: list[int] = []
    problems: list[list[int]] = []
    result: list[tuple[list[int], str]] = []

    # Traverse columns from right to left
    for col in range(cols - 1, -1, -1):
        seen_chars_in_column = False
        for row_index, row in enumerate(range(rows)):
            char = grid[row][col]
            if char != " ":
                seen_chars_in_column = True
                problem_number += char
            if row_index + 1 == len(range(rows)) and seen_chars_in_column:
                numbers.append(int(problem_number))
                problem_number = ""
        if not seen_chars_in_column:
            problems.append(numbers)
            numbers = []

    problems.append(numbers)

    for problem in problems:
        operator = operators.__next__()
        result.append((problem, operator))

    return result


def solve_problem(numbers: list[int], operator: str) -> int:
    """Solve a single problem given the list of numbers and the operator."""
    if operator == "+":
        return sum(numbers)
    elif operator == "*":
        result = 1
        for number in numbers:
            result *= number
        return result
    else:
        raise ValueError(f"Unsupported operator: {operator}")
