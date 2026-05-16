from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ProjectProfile:
    applicant: str
    project_name: str
    problem: str
    agent_workflow: list[str]
    tech_stack: list[str]
    personal_contribution: list[str]
    outcome: list[str]
    repository_url: str = ""
    demo_url: str = ""

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ProjectProfile":
        return cls(
            applicant=str(data.get("applicant", "申请人")),
            project_name=str(data.get("project_name", "AI Agent Project")),
            problem=str(data.get("problem", "")),
            agent_workflow=list(data.get("agent_workflow", [])),
            tech_stack=list(data.get("tech_stack", [])),
            personal_contribution=list(data.get("personal_contribution", [])),
            outcome=list(data.get("outcome", [])),
            repository_url=str(data.get("repository_url", "")),
            demo_url=str(data.get("demo_url", "")),
        )


@dataclass(frozen=True)
class Plan:
    angle: str
    required_points: list[str]
    answer_outline: list[str]


@dataclass(frozen=True)
class EvidenceReport:
    score: int
    present: list[str] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Draft:
    text: str


@dataclass(frozen=True)
class Review:
    score: int
    strengths: list[str]
    improvements: list[str]


@dataclass(frozen=True)
class AgentResult:
    plan: Plan
    evidence: EvidenceReport
    draft: Draft
    review: Review

