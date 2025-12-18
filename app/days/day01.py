def part1(puzzle_input: str) -> int:
    """Sample part1: count number of lines in the input."""
    if not puzzle_input:
        return 0
    
    zero_count=0
    position = 50
    for line in puzzle_input.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            continue
        position = turn_dial(position, stripped_line)
        if position == 0:
            zero_count += 1
    return zero_count


def part2(puzzle_input: str) -> int:
    """Sample part2: sum integer lines in the input (ignores non-int)."""
    if not puzzle_input:
        return 0
    
    zero_count=0
    position = 50
    for line in puzzle_input.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            continue
        new_position = turn_dial(position, stripped_line)
        zero_count += number_of_times_past_zero(position, stripped_line)
        position = new_position
    return zero_count

def turn_dial(current: int, steps: str) -> int:
    """Turn a dial with values 0-99 by 'steps' positions. 
    Steps can be positive (clockwise) or negative (counter-clockwise).
    and is a string like L43 where L means left (counter-clockwise) and R means right (clockwise).
    return the final position of the dial.
    """
    direction = steps[0]
    amount = int(steps[1:])
    
    if direction == 'R':
        return (current + amount) % 100
    else:
        return (current - amount) % 100
    
def number_of_times_past_zero(current: int, steps: str) -> int:
    """Calculate how many times the dial passes position 0 when moving from start to end.
    """
    direction = steps[0]
    amount = int(steps[1:])
    
    if direction == 'R':
        return (current + amount) // 100
    else:
        if current == 0:
            return amount // 100
        else:
            return max(0, (amount - current) // 100 + 1)
