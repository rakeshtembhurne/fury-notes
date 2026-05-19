---
created: 2026-05-19
tags: [claude-code, subagents, agents, workflow]
source: "YouTube transcript — Leon van Zyl"
---

# Claude Code Sub-Agents — Mastery Guide

## Key Insights

- **Claude Code has built-in sub-agents you can invoke with `@agent`**: Bash agent (terminal/CLI operations), General Purpose agent (multi-step research tasks), Explore agent (fast codebase scanning using Haiku — cheap/fast), Planning agent (investigates requirements and plans solutions), Status Line Setup agent, and Claude Code Guide agent.

- **Invoke agents directly with `@agentname` in the prompt** — Use `@bash` to delegate CLI work, `@explore` for fast file searches, `@planner` for architectural decisions. Each is specialized and outperforms a general-purpose agent on its specific task.

- **Build specialized self-validating agents** — The key advanced pattern: give each sub-agent its own validation logic. After the agent performs its task, it runs checks to confirm the output is correct before returning. This creates reliable pipelines.

- **Hooks enable validation at every step** — Hooks run inside skills, sub-agents, and custom slash commands. Use `post-tool` hooks to validate files after they're written, and `stop` hooks to run global validation across the codebase at the end of a workflow.

- **Self-validation is the path to scaling agent reliability** — Rather than a generalist "do everything" agent that nukes the context window, build focused specialists that do one thing well and validate that one thing. This pattern scales across tens/hundreds/thousands of runs.

## Summary

Sub-agents transform Claude Code from a single agent into a team of specialists. Use built-in agents for common tasks, and build custom specialized agents with their own validation logic. Hooks let you inject validation at every step — post-tool for per-file checks, stop hooks for end-of-workflow global validation. The "specialized + self-validating" pattern is the key to scaling agentic workflows reliably.
