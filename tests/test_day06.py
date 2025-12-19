import pytest

from app.days.day06 import get_problems, get_problems_right_to_left, solve_problem


# ---------------------------
# Tests for get_problems
# ---------------------------
def test_get_problems_basic():
    input_str = """1 2 3
4 5 6
+
* - /"""
    # Adjusted example with consistent number/operator mapping
    input_str = """1 2 3
4 5 6
+ * /"""
    problems = get_problems(input_str)

    assert problems == [([1, 4], "+"), ([2, 5], "*"), ([3, 6], "/")]


def test_get_problems_single_row():
    input_str = """10 20 30
+ - *"""
    problems = get_problems(input_str)

    assert problems == [([10], "+"), ([20], "-"), ([30], "*")]


def test_get_problems_single_number():
    input_str = """42
+"""
    problems = get_problems(input_str)

    assert problems == [([42], "+")]


# ---------------------------
# Tests for get_problems_right_to_left
# ---------------------------
def test_get_problems_right_to_left_basic():
    input_str = """123 456
789 101
+ *"""
    problems = get_problems_right_to_left(input_str)

    # We expect numbers read top → bottom, right → left per your function
    assert len(problems) == 2
    assert all(isinstance(p[0], list) for p in problems)
    assert all(isinstance(p[1], str) for p in problems)


def test_get_problems_right_to_left_single_column():
    input_str = """12
34
+"""
    problems = get_problems_right_to_left(input_str)
    # Each number should be read as one integer from top → bottom
    numbers, operator = problems[0]
    assert numbers == [24, 13]
    assert operator == "+"


# ---------------------------
# Tests for solve_problem
# ---------------------------
def test_solve_problem_addition():
    numbers = [1, 2, 3]
    result = solve_problem(numbers, "+")
    assert result == 6


def test_solve_problem_multiplication():
    numbers = [2, 3, 4]
    result = solve_problem(numbers, "*")
    assert result == 24


def test_solve_problem_single_number():
    numbers = [5]
    result_sum = solve_problem(numbers, "+")
    result_mul = solve_problem(numbers, "*")
    assert result_sum == 5
    assert result_mul == 5


def test_solve_problem_empty_list():
    assert solve_problem([], "+") == 0
    assert solve_problem([], "*") == 1


def test_solve_problem_invalid_operator():
    numbers = [1, 2, 3]
    with pytest.raises(ValueError):
        solve_problem(numbers, "-")
