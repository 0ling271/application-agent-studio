# Application Agent Studio

一个面向申请表、奖学金、实习项目和 token plan 额度申请的 AI Agent 小工具。它把零散经历整理成“可验证的具体成果描述”，并用多 Agent 工作流检查可信度、完整性和表达质量。

## What It Builds

本项目实现了一个轻量级 Agent pipeline：

- `PlannerAgent`：识别申请问题、提取成果要点、规划回答结构。
- `EvidenceAgent`：检查是否包含项目链接、技术栈、个人贡献和量化结果。
- `WriterAgent`：生成适合申请表粘贴的中文成果描述。
- `ReviewAgent`：根据评估标准打分，并给出可补充的信息。

默认使用本地规则引擎，方便离线演示；如果配置 `OPENAI_API_KEY`，也可以把 `WriterAgent` 扩展为真实 LLM 调用。

## Quick Start

```powershell
python -m src.app --profile examples/profile.json
```

## Test

```powershell
python -m unittest discover
```

运行后会输出：

- 可直接粘贴到申请表的问题回答。
- Agent 审查分数。
- 缺失证据清单。
- 建议补充的 GitHub/README/演示材料。

## Example Output

见 [docs/sample-answer.md](docs/sample-answer.md)。

## Why This Counts As Agent/AI Driven Work

这个项目不是只调用一次模型生成文本，而是把申请描述拆成多个 Agent 任务：规划、证据审查、写作、复核。每个 Agent 有明确输入输出，最终形成可追踪的工作流，适合用来说明“我使用 Agent 或 AI 驱动构建了什么具体成果”。

## Project Structure

```text
src/
  agents.py      # Agent 角色和审查逻辑
  app.py         # CLI 入口
  models.py      # 数据结构
examples/
  profile.json   # 示例申请背景
docs/
  sample-answer.md
```

## Roadmap

- 接入真实 OpenAI Responses API。
- 增加网页表单模式。
- 自动生成 README 证据段落和项目截图清单。
- 支持英文申请回答。
