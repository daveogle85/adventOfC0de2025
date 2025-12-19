#!/usr/bin/env bash
set -euo pipefail

USAGE="Usage: $0 {venv|install|test|day|all} \n\nCommands:\n  venv    Create the .venv (if missing) and activate it for the script run\n  install Create venv and install requirements from requirements.txt\n  test    Run pytest inside the venv (requires pytest installed in venv)\n  day     Run the app via python -m app.main\n  all     Do install, test, then run\n"

COMMAND=${1:-all}
ARGS=("${@:2}")

# Resolve repository root (one level up from scripts/)
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd)"

# Run from the repository root so relative paths work the same regardless of CWD
cd "${REPO_ROOT}"


create_venv() {
  if [ ! -d "${REPO_ROOT}/.venv" ]; then
    echo "Creating virtual environment ${REPO_ROOT}/.venv..."
    python -m venv "${REPO_ROOT}/.venv"
  else
    echo "Virtual environment .venv already exists."
  fi

  if [ -f "${REPO_ROOT}/.venv/Scripts/activate" ]; then
    # Windows (Git Bash / MSYS)
    # shellcheck disable=SC1091
    # shellcheck source=/dev/null
    source "${REPO_ROOT}/.venv/Scripts/activate"
  elif [ -f "${REPO_ROOT}/.venv/bin/activate" ]; then
    # Unix
    # shellcheck disable=SC1091
    # shellcheck source=/dev/null
    source "${REPO_ROOT}/.venv/bin/activate"
  else
    echo "Cannot find activate script in .venv. Virtualenv may be broken." >&2
    return 1
  fi

  # Ensure the repository root is on PYTHONPATH so `python -m app.main` works
  export PYTHONPATH="${REPO_ROOT}${PYTHONPATH:+:}${PYTHONPATH:-}"
  echo "Exported PYTHONPATH=${REPO_ROOT}"
}

install_deps() {
  if [ ! -f requirements.txt ]; then
    echo "No requirements.txt found; skipping install.";
    return 0
  fi
  echo "Installing requirements..."
  pip install -r requirements.txt
}

run_tests() {
  if ! command -v pytest >/dev/null 2>&1; then
    echo "pytest not found in the venv. Run '$0 install' first to install dependencies." >&2
    return 2
  fi
  pytest
}

run_app() {
  python -m app.main "${ARGS[@]}"
}

case "$COMMAND" in
  venv)
    create_venv
    ;;
  install)
    create_venv
    install_deps
    ;;
  test)
    create_venv
    run_tests
    ;;
  day)
    create_venv
    run_app
    ;;
  all)
    create_venv
    install_deps || echo "install step failed; continuing to run tests and app"
    run_tests || echo "tests failed or pytest missing; continuing to run app"
    run_app
    ;;
  *)
    printf "%s" "$USAGE"
    exit 1
    ;;
esac
