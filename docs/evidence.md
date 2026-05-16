# 使用证明与影响力证明

项目链接：https://github.com/0ling271/application-agent-studio

## 1. Agent 工作流

本项目实现了一个用于申请材料生成与证据审查的多 Agent pipeline：

1. `PlannerAgent`：识别申请问题，规划回答结构。
2. `EvidenceAgent`：检查项目名、技术栈、个人贡献、成果、GitHub 链接等证据是否完整。
3. `WriterAgent`：生成可直接粘贴到申请表的中文成果描述。
4. `ReviewAgent`：给出 Evidence score、Review score 和改进建议。

## 2. 可复现运行方式

```powershell
python -m src.app --profile examples/profile.json
```

## 3. 运行日志示例

```text
# Agent Generated Application Answer

## 可直接填写的回答
我构建了一个名为 Application Agent Studio 的 Agent/AI 驱动项目，用来解决“申请表经常要求描述 AI/Agent 具体成果，但很多人只有零散经历，难以写成可信、具体、可验证的答案”的问题。项目采用多 Agent 流程：PlannerAgent 规划回答结构、EvidenceAgent 检查 GitHub、技术栈、个人贡献和结果证据、WriterAgent 生成适合申请表粘贴的中文回答、ReviewAgent 根据完整度和可信度给出评分与修改建议。我主要负责设计了多 Agent 工作流和评分标准；实现了从结构化背景到申请回答的自动生成 CLI；补充了示例输入、示例输出和项目说明文档。技术上使用 Python、dataclasses、CLI、JSON profile、GitHub README，将申请者的项目背景、技术栈、个人贡献和结果证据结构化，再由 Agent 自动生成适合表单填写的成果描述，并给出证据完整度评分。目前成果包括：可以在一分钟内生成一版 300-500 字的申请成果描述；能够自动指出缺失的证据材料，减少空泛表述；形成了可公开展示的 GitHub 项目骨架。GitHub：https://github.com/0ling271/application-agent-studio。这个项目的价值在于，它把一次性的 AI 文本生成变成了可复用、可审查、可迭代的 Agent 工作流，能帮助申请者更真实、具体地表达自己使用 AI 构建产品的能力。

## Agent 审查
- Evidence score: 88/100
- Review score: 93/100
- Present: 项目名称、明确问题、Agent 工作流、技术栈、个人贡献、结果/影响、GitHub 链接
- Missing: 演示链接
```

## 4. 影响力说明

这个工具把一次性的 AI 对话生成拆成可复用的 Agent 工作流，能够在一分钟内生成一版结构完整的申请成果描述，并自动指出缺失证据。它适合用于 token plan、开发者计划、实习项目、奖学金等需要描述 AI/Agent 实践成果的申请场景。

