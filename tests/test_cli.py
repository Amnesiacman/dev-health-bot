import json
from pathlib import Path

from dev_health_bot.cli import main


def test_cli_json_output(tmp_path: Path, capsys):
    exit_code = main(["--format", "json", "--path", str(tmp_path)])
    output = capsys.readouterr().out.strip()
    payload = json.loads(output)
    assert exit_code == 0
    assert payload["status"] == "needs_attention"


def test_cli_strict_mode_fails_on_unhealthy(tmp_path: Path):
    exit_code = main(["--strict", "--path", str(tmp_path)])
    assert exit_code == 1
