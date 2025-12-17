import argparse
import importlib
import sys
from pathlib import Path
from typing import Optional


def load_input(path: Optional[Path]) -> str:
    if path and path.exists():
        return path.read_text(encoding="utf-8")
    # fallback: empty input
    return ""


def run_day(day: int, part: Optional[int], input_path: Optional[Path]) -> int:
    module_name = f"app.days.day{day:02d}"
    try:
        mod = importlib.import_module(module_name)
    except Exception as e:
        print(f"Error: could not import module '{module_name}': {e}", file=sys.stderr)
        return 2

    data = load_input(input_path)

    def call_fn(name: str):
        fn = getattr(mod, name, None)
        if not callable(fn):
            print(f"{module_name} has no function '{name}'", file=sys.stderr)
            return None
        try:
            return fn(data)
        except Exception as e:
            print(f"{module_name}.{name} raised: {e}", file=sys.stderr)
            return None

    if part is None:
        print(f"Running day {day:02d} parts 1 and 2")
        p1 = call_fn("part1")
        print("Part 1:", p1)
        p2 = call_fn("part2")
        print("Part 2:", p2)
    else:
        name = f"part{part}"
        print(f"Running day {day:02d} {name}")
        result = call_fn(name)
        print(name.capitalize() + ":", result)

    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="advent", description="Run Advent of Code day solutions")
    p.add_argument("day", type=int, help="Day number to run (e.g. 1)")
    p.add_argument("--part", type=int, choices=[1, 2], help="Run only part 1 or 2")
    p.add_argument("--input", type=str, help="Path to input file (defaults to inputs/dayXX.txt)")
    args = p.parse_args(argv)

    input_path = Path(args.input) if args.input else Path("inputs") / f"day{args.day:02d}.txt"
    return run_day(args.day, args.part, input_path)


if __name__ == "__main__":
    raise SystemExit(main())
