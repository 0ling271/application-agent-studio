from __future__ import annotations

import argparse
import json
from pathlib import Path

from .agents import ApplicationAgentPipeline
from .models import ProjectProfile


def load_profile(path: Path) -> ProjectProfile:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return ProjectProfile.from_dict(data)


def render_result(profile: ProjectProfile) -> str:
    result = ApplicationAgentPipeline().run(profile)

    lines = [
        "# Agent Generated Application Answer",
        "",
        "## 可直接填写的回答",
        result.draft.text,
        "",
        "## Agent 审查",
        f"- Evidence score: {result.evidence.score}/100",
        f"- Review score: {result.review.score}/100",
        "- Present: " + "、".join(result.evidence.present),
        "- Missing: " + ("、".join(result.evidence.missing) or "无"),
        "",
        "## 改进建议",
    ]
    lines.extend(f"- {item}" for item in (result.review.improvements or ["当前信息已经足够提交。"]))
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an agent-reviewed application answer.")
    parser.add_argument("--profile", type=Path, required=True, help="Path to a JSON profile.")
    args = parser.parse_args()

    profile = load_profile(args.profile)
    print(render_result(profile))


if __name__ == "__main__":
    main()

