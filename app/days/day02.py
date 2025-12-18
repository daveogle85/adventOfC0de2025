from typing import Callable, List


def part1(puzzle_input: str) -> int:
    if not puzzle_input:
        return 0
    
    repeated_twice: list[str] = []
    
    for line in puzzle_input.split(","):
        stripped_line = line.strip()
        if not stripped_line:
            continue
        repeated_twice.extend(find_twice_repeated(stripped_line))
    return sum_list(repeated_twice)

def part2(puzzle_input: str) -> int:
    if not puzzle_input:
        return 0
    
    repeated_at_least_twice: list[str] = []
    
    for line in puzzle_input.split(","):
        stripped_line = line.strip()
        if not stripped_line:
            continue
        repeated_at_least_twice.extend(
            find_repeated_at_least_twice(stripped_line)
        )
    return sum_list(repeated_at_least_twice)

def find_twice_repeated(range_str: str) -> List[str]:
    """
    Find numbers in the given range (inclusive) that are constructed of a pattern repeated twice.
    The range is given as a string in the format "start-end".
    """
    return find_repeated_by_predicate(range_str, is_repeated_twice)

def find_repeated_at_least_twice(range_str: str) -> List[str]:
    """
    Find numbers in the given range (inclusive) that are constructed of a pattern repeated at least twice.
    The range is given as a string in the format "start-end".
    """
    return find_repeated_by_predicate(range_str, is_repeated_at_least_twice)

def sum_list(list_to_sum: list[str]) -> int:
    """
    Sum the numbers in the given list.
    """
    total = 0
    for value in list_to_sum:
        total += int(value)
    return total

def find_repeated_by_predicate(
    range_str: str,
    predicate: Callable[[str], bool]
) -> List[str]:
    """
    Find the numbers in the given range (inclusive) which satisfy the given predicate.
    """
    start_str, end_str = range_str.split("-")
    start = int(start_str.strip())
    end = int(end_str.strip())
    return [str(i) for i in range(start, end + 1) if predicate(str(i))]

def is_repeated_twice(s: str) -> bool:
    """Check if a string is constructed of a pattern repeated twice."""
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]

def is_repeated_at_least_twice(s: str) -> bool:
    """Check if a string is constructed of a pattern repeated at least twice."""
    length = len(s)
    for sub_length in range(1, length // 2 + 1):
        if length % sub_length == 0:
            pattern = s[:sub_length]
            if pattern * (length // sub_length) == s:
                return True
    return False