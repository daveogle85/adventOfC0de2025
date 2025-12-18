#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "Usage: $0 <day_number>"
  exit 1
fi

# Resolve repository root (one level up from scripts/)
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd)"

# Run from the repository root so relative paths work the same regardless of CWD
cd "${REPO_ROOT}"

DAY_NUM=$(printf "%02d" "$1")
DAY_PY="app/days/day${DAY_NUM}.py"
TEST_PY="tests/test_day${DAY_NUM}.py"
INPUT_TXT="inputs/day${DAY_NUM}.txt"

# Create day solution file if it doesn't exist
if [ ! -f "$DAY_PY" ]; then
  cat > "$DAY_PY" <<EOF
"""Advent of Code 2025 - Day ${DAY_NUM}"""

def part1(puzzle_input: str):
    pass

def part2(puzzle_input: str):
    pass
EOF
  echo "Created $DAY_PY"
else
  echo "$DAY_PY already exists, skipping."
fi

# Create test file if it doesn't exist
if [ ! -f "$TEST_PY" ]; then
  cat > "$TEST_PY" <<EOF
import pytest
from app.days.day${DAY_NUM} import part1, part2

def test_part1_example():
    assert part1("") is None  # TODO: Replace with real test

def test_part2_example():
    assert part2("") is None  # TODO: Replace with real test
EOF
  echo "Created $TEST_PY"
else
  echo "$TEST_PY already exists, skipping."
fi

# Create input file if it doesn't exist
if [ ! -f "$INPUT_TXT" ]; then
  touch "$INPUT_TXT"
  echo "Created $INPUT_TXT"
else
  echo "$INPUT_TXT already exists, skipping."
fi
