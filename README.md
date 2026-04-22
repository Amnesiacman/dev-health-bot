# dev-health-bot

[Русская версия](README.ru.md)

CLI and GitHub Action helper to quickly assess repository readiness.

## What it checks

- `.git` exists
- `README.md` exists
- `pyproject.toml` exists
- `tests/` exists
- `.github/workflows/ci.yml` exists

## Usage

```bash
python3 main.py --path .
python3 main.py --path . --format json
python3 main.py --path . --strict
```

## CI usage

Use strict mode to fail builds when required repository hygiene checks are missing.

## Exit codes

- `0` scan completed (and strict checks passed)
- `1` strict mode failed
