---
created: 2026-05-19
tags: #research #ai-agents #harness-engineering
---

# Harness Engineering for AI Agents

## What is a Harness?

A **harness** in AI agent context is the scaffolding/external system that wraps an LLM to make it do useful work. It includes:
- Prompting strategies
- Tool definitions
- Evaluation frameworks
- Control mechanisms

## Key Frameworks Available

| Framework | Stars | Language | Notes |
|-----------|-------|----------|-------|
| [[Microsoft AutoGen]] | 58.2k | Python | Enterprise production-ready, event-driven |
| [[OpenAI Swarm]] | 21.5k | Python | Lightweight, educational |
| [[LangChain deepagents]] | 23k | Python | LangGraph integration |
| [[Aden Hive/hive]] | 10.4k | Python | MCP-native, production-ready |
| [[JCode]] | 6.3k | Rust | CLI-native, fast |

## Key Insights

1. **Harness = stream processor** - Harnesses should be modeled as stream processors that call `append({event})` and `stream()` an append-only event log
2. **Event-sourced state** - All state in agent harnesses should be event-sourced
3. **Plugin = stream processor** - Harness plugins are just stream processors that can run on other machines

## Terminal-Bench 2 Rankings

Claude Code ranked as "worst harness for Opus 4.6" among all harnesses tested.

## Neurosymbolic Shift

Claude Code uses a 3,167-line symbolic kernel (`print.ts`) - pure scaling isn't enough. The future is combining LLMs with deterministic symbolic components.

## Related
- [[autoresearch-karpathy]]
- [[auto-research-system]]
