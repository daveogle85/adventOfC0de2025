import pytest
from app.days.day02 import part1, find_twice_repeated, is_repeated_twice, sum_list, find_repeated_by_predicate, is_repeated_at_least_twice


# Tests for is_repeated_twice function
class TestIsRepeatedTwice:
    """Test cases for the is_repeated_twice function."""

    def test_repeated_twice_basic(self):
        """Test basic cases where pattern is repeated twice."""
        assert is_repeated_twice("aa") is True
        assert is_repeated_twice("abab") is True
        assert is_repeated_twice("123123") is True
        assert is_repeated_twice("xyxy") is True

    def test_repeated_twice_longer_pattern(self):
        """Test with longer patterns repeated twice."""
        assert is_repeated_twice("abcabc") is True
        assert is_repeated_twice("123456123456") is True
        assert is_repeated_twice("helloworld" + "helloworld") is True

    def test_not_repeated_twice(self):
        """Test strings that are NOT repeated twice."""
        assert is_repeated_twice("a") is False
        assert is_repeated_twice("ab") is False
        assert is_repeated_twice("abc") is False
        assert is_repeated_twice("abcde") is False

    def test_odd_length_strings(self):
        """Test that odd-length strings always return False."""
        assert is_repeated_twice("aaa") is False
        assert is_repeated_twice("abcde") is False
        assert is_repeated_twice("12345") is False

    def test_even_length_but_not_pattern(self):
        """Test even-length strings that don't have pattern repeated twice."""
        assert is_repeated_twice("aaab") is False
        assert is_repeated_twice("abcd") is False
        assert is_repeated_twice("1234") is False

    def test_empty_string(self):
        """Test empty string."""
        assert is_repeated_twice("") is True

    def test_single_character_repeated(self):
        """Test single character repeated twice."""
        assert is_repeated_twice("aa") is True
        assert is_repeated_twice("bb") is True
        assert is_repeated_twice("zz") is True




# Tests for find_repeated_by_predicate function
class TestFindRepeatedByPredicate:
    """Test cases for the find_repeated_by_predicate function with different predicates."""

    def test_simple_range_twice(self):
        result = find_repeated_by_predicate("0-10", is_repeated_twice)
        assert result == []

    def test_range_with_repeated_patterns_twice(self):
        result = find_repeated_by_predicate("10-40", is_repeated_twice)
        assert result == ["11", "22", "33"]

    def test_single_number_range_twice(self):
        result = find_repeated_by_predicate("11-11", is_repeated_twice)
        assert result == ["11"]
        result = find_repeated_by_predicate("12-12", is_repeated_twice)
        assert result == []

    def test_range_with_whitespace_twice(self):
        result1 = find_repeated_by_predicate("11-22", is_repeated_twice)
        result2 = find_repeated_by_predicate(" 11 - 22 ", is_repeated_twice)
        assert result1 == result2

    def test_larger_range_twice(self):
        result = find_repeated_by_predicate("1000-9999", is_repeated_twice)
        assert isinstance(result, list)
        assert all(is_repeated_twice(x) for x in result)

    def test_simple_range_at_least_twice(self):
        result = find_repeated_by_predicate("0-10", is_repeated_at_least_twice)
        assert result == []

    def test_range_with_repeated_patterns_at_least_twice(self):
        result = find_repeated_by_predicate("10-40", is_repeated_at_least_twice)
        # 11, 22, 33 are repeated twice; nothing else in this range is repeated at least twice
        assert result == ["11", "22", "33"]

    def test_single_number_range_at_least_twice(self):
        result = find_repeated_by_predicate("11-11", is_repeated_at_least_twice)
        assert result == ["11"]
        result = find_repeated_by_predicate("12-12", is_repeated_at_least_twice)
        assert result == []

    def test_range_with_whitespace_at_least_twice(self):
        result1 = find_repeated_by_predicate("11-22", is_repeated_at_least_twice)
        result2 = find_repeated_by_predicate(" 11 - 22 ", is_repeated_at_least_twice)
        assert result1 == result2

    def test_larger_range_at_least_twice(self):
        result = find_repeated_by_predicate("1000-9999", is_repeated_at_least_twice)
        assert isinstance(result, list)
        assert all(is_repeated_at_least_twice(x) for x in result)

# Tests for sum_list function
class TestSumList:
    def test_sum_empty(self):
        assert sum_list([]) == 0

    def test_sum_single(self):
        assert sum_list(["11"]) == 11

    def test_sum_multiple(self):
        assert sum_list(["11", "22", "33"]) == 66


# Tests for part1 function
class TestPart1:
    """Test cases for the part1 function."""

    def test_part1_empty_input(self):
        result = part1("")
        assert result == 0

    def test_part1_single_range(self):
        result = part1("11-22")
        # 11, 22
        assert result == 33

    def test_part1_multiple_ranges_comma(self):
        result = part1("11-22,33-44")
        # 11, 22, 33, 44
        assert result == 110

    def test_part1_ignores_empty_ranges(self):
        result = part1(",11-11,,22-22,")
        assert result == 33
