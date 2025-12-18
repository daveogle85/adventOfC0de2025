import pytest
from app.days.day03 import part1, part2, find_largest_number_from_string


def test_part1_example():
    assert part1("") == 0


def test_part2_example():
    assert part2("") == 0


def test_find_largest_number_from_string_simple():
    # "1934" with 2 choices -> 9 then 4 => "94"
    assert find_largest_number_from_string("1934", 2) == "94"


def test_find_largest_number_from_string_identical():
    # "99" with 2 choices -> 9 then 9 => "99"
    assert find_largest_number_from_string("99", 2) == "99"


def test_find_largest_number_from_string_repeated_max():
    # "12939" with 2 choices -> 9 then 9 => "99"
    assert find_largest_number_from_string("12939", 2) == "99"


def test_find_largest_number_from_string_descending():
    # "987654321" with 2 choices -> 9 then 8 => "98"
    assert find_largest_number_from_string("987654321", 2) == "98"


def test_find_largest_number_from_string_ties():
    # "2773" with 2 choices -> 7 then 7 => "77"
    assert find_largest_number_from_string("2773", 2) == "77"


def test_find_largest_number_from_string_with_zeros():
    # "100" with 2 choices -> 1 then 0 => "10"
    assert find_largest_number_from_string("100", 2) == "10"


def test_find_largest_number_from_string_three_choices():
    # "123456" with 3 choices -> greedy: 4 (from "1234"), then 5 (from "56"), then 6 => "456"
    assert find_largest_number_from_string("123456", 3) == "456"


def test_find_largest_number_from_string_too_short():
    # "12" with 3 choices -> not enough digits available => "0"
    assert find_largest_number_from_string("12", 3) == "0"


def test_part1_single_line():
    # "1934" -> find_largest_number_from_string("1934", 2) = "94" -> int("94") = 94
    assert part1("1934") == 94


def test_part1_multiple_lines():
    # "1934\n2773" -> 94 + 77 = 171
    assert part1("1934\n2773") == 171


def test_part2_single_line():
    # part2 uses 12 choices
    assert part2("123456789012345") == int(
        find_largest_number_from_string("123456789012345", 12)
    )
