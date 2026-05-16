import unittest

from src.agents import ApplicationAgentPipeline
from src.models import ProjectProfile


class PipelineTest(unittest.TestCase):
    def test_pipeline_generates_application_answer(self) -> None:
        profile = ProjectProfile(
            applicant="Tester",
            project_name="Application Agent Studio",
            problem="申请回答缺少结构化证据",
            agent_workflow=["plan", "check", "write", "review"],
            tech_stack=["Python", "CLI"],
            personal_contribution=["设计 Agent 流程", "实现 CLI"],
            outcome=["生成申请回答", "输出证据评分"],
        )

        result = ApplicationAgentPipeline().run(profile)

        self.assertIn("Application Agent Studio", result.draft.text)
        self.assertGreaterEqual(result.evidence.score, 70)
        self.assertGreater(result.review.score, 0)


if __name__ == "__main__":
    unittest.main()
