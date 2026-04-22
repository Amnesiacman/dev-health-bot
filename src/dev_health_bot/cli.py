import argparse
import json
from pathlib import Path

from dev_health_bot.checks import run_checks


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dev-health-bot",
        description="Repository health scanner for CI and local checks.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero exit code when any check fails",
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Target repository path",
    )
    return parser


def _render_text(report: dict) -> str:
    lines = [
        f"Target: {report['target']}",
        f"Status: {report['status']}",
        f"Checks: {report['passed']}/{report['total']} passed",
    ]
    for check in report["checks"]:
        marker = "OK" if check["ok"] else "FAIL"
        line = f"- [{marker}] {check['id']}: {check['description']}"
        if not check["ok"]:
            line += f" | hint: {check['hint']}"
        lines.append(line)
    return "\n".join(lines)


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    report = run_checks(Path(args.path).resolve())
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=True))
    else:
        print(_render_text(report))
    if args.strict and report["failed"] > 0:
        return 1
    return 0

