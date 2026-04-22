from pathlib import Path

from dev_health_bot.checks import run_checks


def test_report_shape(tmp_path: Path):
    report = run_checks(tmp_path)
    assert report["status"] in {"ok", "needs_attention"}
    assert report["total"] == 5
    assert len(report["checks"]) == 5


def test_report_ok_when_required_files_present(tmp_path: Path):
    (tmp_path / ".git").mkdir()
    (tmp_path / "tests").mkdir()
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    (tmp_path / "README.md").write_text("x", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text("x", encoding="utf-8")
    (tmp_path / ".github" / "workflows" / "ci.yml").write_text("x", encoding="utf-8")

    report = run_checks(tmp_path)
    assert report["status"] == "ok"
    assert report["failed"] == 0

