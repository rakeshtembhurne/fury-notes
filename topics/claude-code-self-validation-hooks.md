---
created: 2026-05-19
tags: [claude-code, hooks, validation, agents, tools]
source: "YouTube transcript — IndyDevDan"
---

# Claude Code Self-Validating Agents — Hooks Feature

## Key Insights

- **Hooks run validation inside skills, sub-agents, and custom slash commands** — This is the feature senior engineers consistently miss. Hooks let you inject self-validation at every step of an agent's work, not just at the end.

- **Two hook types: `post-tool` and `stop`** — `post-tool` hooks run after each file read/edit/write, giving you the file path to validate immediately. `stop` hooks run globally across the codebase when the agent finishes. Use `post-tool` for per-file validation, `stop` for codebase-wide checks.

- **Build specialized single-purpose validators** — Rather than one general agent doing everything, build agents that do one thing (e.g., CSV editing) and validate that one thing rigorously. This "specialized + self-validating" pattern scales reliably.

- **Pass hooks via JSON settings to your primary agent** — You can inject an entire settings file as JSON (including hooks definitions) into your primary agent, enabling sophisticated multi-agent pipelines with built-in validation at every level.

- **Context engineering optimizes Claude Code performance** — As the codebase grows, use sub-agents to reduce context noise. Remove unused MCPs that consume tokens. The Claude.md file grows over time — keep only high-level pointers, not every detail.

## Summary

Hooks are the missing piece for reliable agentic workflows. Build specialized agents with their own validation logic, use `post-tool` hooks for immediate per-file validation and `stop` hooks for end-of-workflow global checks. The pattern: agents + self-validation beats general-purpose agents every time for scaling. Context management (sub-agents, pruning unused MCPs, compact CLAUDE.md) keeps Claude Code performant as projects grow.
