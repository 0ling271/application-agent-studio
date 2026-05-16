# Sample Answer

下面是运行 `python -m src.app --profile examples/profile.json` 后生成的示例回答。

> 我构建了一个名为 Application Agent Studio 的 Agent/AI 驱动项目，用来解决“申请表经常要求描述 AI/Agent 具体成果，但很多人只有零散经历，难以写成可信、具体、可验证的答案”的问题。项目采用多 Agent 流程：PlannerAgent 规划回答结构、EvidenceAgent 检查 GitHub、技术栈、个人贡献和结果证据、WriterAgent 生成适合申请表粘贴的中文回答、ReviewAgent 根据完整度和可信度给出评分与修改建议。我主要负责设计了多 Agent 工作流和评分标准；实现了从结构化背景到申请回答的自动生成 CLI；补充了示例输入、示例输出和项目说明文档。技术上使用 Python、dataclasses、CLI、JSON profile、GitHub README，将申请者的项目背景、技术栈、个人贡献和结果证据结构化，再由 Agent 自动生成适合表单填写的成果描述，并给出证据完整度评分。目前成果包括：可以在一分钟内生成一版 300-500 字的申请成果描述；能够自动指出缺失的证据材料，减少空泛表述；形成了可公开展示的 GitHub 项目骨架。GitHub：https://github.com/0ling271/application-agent-studio 这个项目的价值在于，它把一次性的 AI 文本生成变成了可复用、可审查、可迭代的 Agent 工作流，能帮助申请者更真实、具体地表达自己使用 AI 构建产品的能力。

## 更短版本

我做了一个名为 Application Agent Studio 的 Agent 项目，用来把零散项目经历整理成申请表可直接填写的“AI/Agent 具体成果”描述。它包含 Planner、Evidence、Writer、Review 四个 Agent：先规划回答结构，再检查 GitHub/技术栈/个人贡献/成果证据，随后生成中文回答，最后给出可信度评分和补充建议。我负责设计工作流、实现 Python CLI、编写示例输入输出和 README。项目展示了我如何把 AI 文本生成工程化为可复用、可审查的 Agent pipeline，而不是只做一次性对话生成。
