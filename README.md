
# adventOfC0de2025

This repository contains solutions for the Advent of Code 2025 programming challenge, written in Python. Each day's puzzle is implemented in a modular way, with input files and tests for each day.

## Project Structure

- `app/` — Main application code
  - `main.py` — Entry point (if needed)
  - `days/` — Solutions for each day (e.g., `day01.py`, `day02.py`, ...)
- `inputs/` — Input files for each day (e.g., `day01.txt`)
- `tests/` — Unit tests for each day's solution
- `scripts/` — Helper scripts (e.g., `run.sh`)
- `requirements.txt` — Python dependencies
- `pyproject.toml` — Project metadata

## How to Run the Code

## Script Options

The `scripts/run.sh` script provides several commands to manage the environment, install dependencies, run tests, and execute solutions. Usage:

```bash
./run.sh [command] [args...]
```

Available commands:

- `venv` — Create the `.venv` virtual environment (if missing) and activate it for the script run.
- `install` — Create the virtual environment and install dependencies from `requirements.txt`.
- `test` — Run all tests using `pytest` inside the virtual environment.
- `run [day]` — Run the app for a specific day. For example, `./run.sh run 2` runs the solution for day 2 using the corresponding input file.
- `all` — Perform install, test, and then run (default if no command is given).

Example usage:

```bash
# Create and activate the virtual environment
./run.sh venv

# Install dependencies
./run.sh install

# Run all tests
./run.sh test

# Run the solution for day 2
./run.sh run 2

# Do install, test, and run in sequence
./run.sh all
```

This will execute the solution for the specified day using the corresponding input file from the `inputs/` directory.

## How to Run the Tests

The project uses `pytest` for testing. To run all tests:

```bash
pytest
```

Or, to run tests for a specific day:

```bash
pytest tests/test_day02.py
```

## How to Add a New Day

1. **Create the solution file:**
	- Copy an existing day file (e.g., `app/days/day01.py`) to a new file (e.g., `app/days/day03.py`).
	- Implement the solution for the new day.
2. **Add the input file:**
	- Place the input for the new day in `inputs/day03.txt`.
3. **Write tests:**
	- Create a new test file (e.g., `tests/test_day03.py`) based on previous days' tests.
	- Add test cases for your solution.
4. **Update scripts (if needed):**
	- Ensure `run.sh` or any other runner script supports the new day.

## Requirements

- Python 3.10+
- Install dependencies with:

```bash
pip install -r requirements.txt
```

---
