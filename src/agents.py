from __future__ import annotations

from .models import AgentResult, Draft, EvidenceReport, Plan, ProjectProfile, Review


class PlannerAgent:
    def run(self, profile: ProjectProfile) -> Plan:
        return Plan(
            angle="突出自己从 0 到 1 构建了可运行的 Agent 工作流，而不是泛泛说用过 AI。",
            required_points=[
                "具体问题",
                "Agent 分工",
                "技术栈",
                "个人贡献",
                "可验证成果",
                "下一步迭代",
            ],
            answer_outline=[
                "先说明项目解决什么申请/写作痛点。",
                "再描述多 Agent pipeline 如何协作。",
                "补充自己实现的关键模块和工程化工作。",
                "最后给出 GitHub、示例输出和可量化收益。",
            ],
        )


class EvidenceAgent:
    def run(self, profile: ProjectProfile) -> EvidenceReport:
        checks = {
            "项目名称": bool(profile.project_name),
            "明确问题": bool(profile.problem),
            "Agent 工作流": len(profile.agent_workflow) >= 3,
            "技术栈": bool(profile.tech_stack),
            "个人贡献": len(profile.personal_contribution) >= 2,
            "结果/影响": bool(profile.outcome),
            "GitHub 链接": bool(profile.repository_url),
            "演示链接": bool(profile.demo_url),
        }
        present = [name for name, ok in checks.items() if ok]
        missing = [name for name, ok in checks.items() if not ok]
        score = round(len(present) / len(checks) * 100)
        return EvidenceReport(score=score, present=present, missing=missing)


class WriterAgent:
    def run(self, profile: ProjectProfile, plan: Plan, evidence: EvidenceReport) -> Draft:
        workflow = "、".join(profile.agent_workflow)
        stack = "、".join(profile.tech_stack)
        contribution = "；".join(profile.personal_contribution)
        outcome = "；".join(profile.outcome)

        links = []
        if profile.repository_url:
            links.append(f"GitHub：{profile.repository_url}")
        if profile.demo_url:
            links.append(f"Demo：{profile.demo_url}")
        link_text = "；".join(links) if links else "目前已整理本地仓库和示例输出，后续会补充公开链接。"

        text = (
            f"我构建了一个名为 {profile.project_name} 的 Agent/AI 驱动项目，用来解决"
            f"“{profile.problem}”的问题。项目采用多 Agent 流程：{workflow}。"
            f"我主要负责{contribution}。技术上使用 {stack}，将申请者的项目背景、技术栈、"
            f"个人贡献和结果证据结构化，再由 Agent 自动生成适合表单填写的成果描述，并给出证据完整度评分。"
            f"目前成果包括：{outcome}。{link_text}"
            f"这个项目的价值在于，它把一次性的 AI 文本生成变成了可复用、可审查、可迭代的 Agent 工作流，"
            f"能帮助申请者更真实、具体地表达自己使用 AI 构建产品的能力。"
        )
        return Draft(text=text)


class ReviewAgent:
    def run(self, draft: Draft, evidence: EvidenceReport) -> Review:
        improvements = []
        if evidence.missing:
            improvements.append("补齐缺失证据：" + "、".join(evidence.missing))
        if len(draft.text) > 700:
            improvements.append("申请表字数较紧时，可以压缩到 300-500 字。")
        if "我主要负责" not in draft.text:
            improvements.append("增加第一人称贡献，避免像团队项目介绍。")

        strengths = [
            "回答包含具体项目名和应用场景。",
            "说明了 Agent 分工，而不是笼统描述使用 AI。",
            "包含技术栈、个人贡献和成果证据。",
        ]
        score = min(100, evidence.score + 10)
        if improvements:
            score -= min(15, len(improvements) * 5)
        return Review(score=score, strengths=strengths, improvements=improvements)


class ApplicationAgentPipeline:
    def __init__(self) -> None:
        self.planner = PlannerAgent()
        self.evidence = EvidenceAgent()
        self.writer = WriterAgent()
        self.reviewer = ReviewAgent()

    def run(self, profile: ProjectProfile) -> AgentResult:
        plan = self.planner.run(profile)
        evidence = self.evidence.run(profile)
        draft = self.writer.run(profile, plan, evidence)
        review = self.reviewer.run(draft, evidence)
        return AgentResult(plan=plan, evidence=evidence, draft=draft, review=review)
