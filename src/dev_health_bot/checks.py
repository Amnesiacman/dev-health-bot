from pathlib import Path


def _exists(path: Path) -> bool:
    return path.exists()


def run_checks(target: Path) -> dict:
    checks = [
        {
            "id": "git_repository",
            "description": "Repository has .git directory",
            "ok": _exists(target / ".git"),
            "hint": "Run this tool in repository root.",
        },
        {
            "id": "readme_present",
            "description": "Repository has README.md",
            "ok": _exists(target / "README.md"),
            "hint": "Add usage docs to README.md.",
        },
        {
            "id": "python_project_file",
            "description": "Python project has pyproject.toml",
            "ok": _exists(target / "pyproject.toml"),
            "hint": "Add pyproject.toml for reproducible builds.",
        },
        {
            "id": "tests_present",
            "description": "Repository has tests directory",
            "ok": _exists(target / "tests"),
            "hint": "Add tests/ with at least smoke tests.",
        },
        {
            "id": "ci_workflow_present",
            "description": "GitHub Actions CI workflow exists",
            "ok": _exists(target / ".github" / "workflows" / "ci.yml"),
            "hint": "Add .github/workflows/ci.yml to run tests.",
        },
    ]
    failed = [c for c in checks if not c["ok"]]
    return {
        "target": str(target),
        "status": "ok" if not failed else "needs_attention",
        "total": len(checks),
        "passed": len(checks) - len(failed),
        "failed": len(failed),
        "checks": checks,
    }
