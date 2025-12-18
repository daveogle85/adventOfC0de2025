from app.days.day01 import turn_dial, part1, part2, number_of_times_past_zero


# Tests for turn_dial function
def test_turn_dial_right_basic():
    """Test basic clockwise (right) movement."""
    assert turn_dial(0, "R5") == 5
    assert turn_dial(10, "R20") == 30


def test_turn_dial_left_basic():
    """Test basic counter-clockwise (left) movement."""
    assert turn_dial(10, "L3") == 7
    assert turn_dial(5, "L5") == 0


def test_turn_dial_wrapping_right():
    """Test clockwise wrapping around 99 to 0."""
    assert turn_dial(95, "R10") == 5
    assert turn_dial(99, "R1") == 0


def test_turn_dial_wrapping_left():
    """Test counter-clockwise wrapping around 0 to 99."""
    assert turn_dial(5, "L10") == 95
    assert turn_dial(0, "L1") == 99


def test_turn_dial_no_movement():
    """Test zero movement."""
    assert turn_dial(50, "R0") == 50
    assert turn_dial(50, "L0") == 50


def test_turn_dial_full_rotation():
    """Test full rotations."""
    assert turn_dial(50, "R100") == 50
    assert turn_dial(50, "L100") == 50


def test_turn_dial_large_steps():
    """Test large step counts that wrap multiple times."""
    assert turn_dial(0, "R105") == 5
    assert turn_dial(0, "L105") == 95


# Tests for part1 function
def test_part1_empty_input():
    """Test with empty input."""
    assert part1("") == 0


def test_part1_single_line_to_zero():
    """Test single line that results in dial position 0.
    Start at 50, R50 -> position 0."""
    assert part1("R50") == 1


def test_part1_single_line_not_zero():
    """Test single line that doesn't result in position 0.
    Start at 50, R10 -> position 60."""
    assert part1("R10") == 0


def test_part1_multiple_lines_mixed():
    """Test multiple lines with persistent position tracking.
    Start at 50:
    - R50: 50 + 50 = 0 (mod 100) -> count = 1
    - R10: 0 + 10 = 10 -> count = 1
    - L50: 10 - 50 = -40 = 60 (mod 100) -> count = 1"""
    input_str = "R50\nR10\nL50"
    assert part1(input_str) == 1


def test_part1_with_blank_lines():
    """Test input with blank lines (which should be stripped).
    Start at 50:
    - R50: 50 + 50 = 0 (mod 100) -> count = 1
    - (blank line skipped)
    - L50: 0 - 50 = -50 = 50 (mod 100) -> count = 1"""
    input_str = "R50\n\nL50"
    assert part1(input_str) == 1


def test_part1_sequence_to_zero():
    """Test sequence where position lands on zero multiple times.
    Start at 50:
    - R50: 50 + 50 = 0 (mod 100) -> count = 1
    - L0: 0 - 0 = 0 -> count = 2
    - R50: 0 + 50 = 50 -> count = 2"""
    input_str = "R50\nL0\nR50"
    assert part1(input_str) == 2


def test_part1_no_lines_to_zero():
    """Test where position never lands on zero.
    Start at 50:
    - R10: 50 + 10 = 60 -> count = 0
    - R20: 60 + 20 = 80 -> count = 0
    - L10: 80 - 10 = 70 -> count = 0"""
    input_str = "R10\nR20\nL10"
    assert part1(input_str) == 0


# Tests for number_of_times_past_zero function
def test_number_of_times_past_zero_right_no_crossing():
    """Test right movement that doesn't cross zero."""
    assert number_of_times_past_zero(10, "R20") == 0
    assert number_of_times_past_zero(30, "R40") == 0


def test_number_of_times_past_zero_right_one_crossing():
    """Test right movement that crosses zero once."""
    assert number_of_times_past_zero(90, "R20") == 1  # 90 + 20 = 110, crosses once
    assert number_of_times_past_zero(95, "R10") == 1  # 95 + 10 = 105, crosses once
    assert number_of_times_past_zero(50, "R50") == 1  # 50 + 50 = 100, crosses once


def test_number_of_times_past_zero_right_multiple_crossings():
    """Test right movement that crosses zero multiple times."""
    assert number_of_times_past_zero(50, "R150") == 2  # 50 + 150 = 200, crosses twice
    assert number_of_times_past_zero(0, "R250") == 2  # 0 + 250 = 250, crosses twice
    assert number_of_times_past_zero(25, "R375") == 4  # 25 + 375 = 400, crosses 4 times


def test_number_of_times_past_zero_left_no_crossing():
    """Test left movement that doesn't cross zero."""
    assert number_of_times_past_zero(50, "L10") == 0  # Final position 40, no crossing
    assert number_of_times_past_zero(30, "L5") == 0   # Final position 25, no crossing


def test_number_of_times_past_zero_left_one_crossing():
    """Test left movement that crosses zero once."""
    assert number_of_times_past_zero(5, "L10") == 1   # 5 - 10 wraps, crosses once
    assert number_of_times_past_zero(25, "L50") == 1  # 25 - 50 wraps, crosses once
    assert number_of_times_past_zero(50, "L60") == 1  # 50 - 60 wraps, crosses once


def test_number_of_times_past_zero_left_multiple_crossings():
    """Test left movement that crosses zero multiple times."""
    assert number_of_times_past_zero(50, "L150") == 2  # Crosses 0 at steps 50 and 150
    assert number_of_times_past_zero(25, "L225") == 3  # Crosses 0 at steps 25, 125, 225
    assert number_of_times_past_zero(10, "L310") == 4  # Multiple wraps


def test_number_of_times_past_zero_no_movement():
    """Test zero movement - should never cross zero."""
    assert number_of_times_past_zero(0, "R0") == 0
    assert number_of_times_past_zero(50, "L0") == 0
    assert number_of_times_past_zero(99, "R0") == 0


def test_number_of_times_past_zero_right_exact_rotation():
    """Test right movement with exact 100-step rotations."""
    assert number_of_times_past_zero(0, "R100") == 1   # Exactly to 0
    assert number_of_times_past_zero(50, "R100") == 1  # Back to start, but crosses
    assert number_of_times_past_zero(0, "R200") == 2   # Two complete rotations


def test_number_of_times_past_zero_left_exact_rotation():
    """Test left movement with exact 100-step rotations."""
    assert number_of_times_past_zero(0, "L100") == 1   # Exactly to 0
    assert number_of_times_past_zero(50, "L100") == 1  # Back to start, but crosses
    assert number_of_times_past_zero(0, "L200") == 2   # Two complete rotations
