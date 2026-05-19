---
created: 2026-05-19
tags: [claude-code, context-engineering, performance, tokens]
source: "YouTube transcript — AI Jason"
---

# Context Engineering — Making Claude Code 10x Better

## Key Insights

- **Context engineering optimizes what goes into the conversation thread** — Claude Code has a 200k token context window, but quality degrades past ~50-60%. Context engineering means ensuring only relevant, necessary information enters the thread — reducing noise while keeping critical context.

- **Remove unused MCPs that consume tokens** — Each inactive MCP in your agent consumes context budget. Removing unused MCPs can immediately free up 2%+ of your context window. Regularly audit with `/context` to see token consumption breakdown.

- **CLAUDE.md should have high-level pointers, not exhaustive detail** — As projects grow, CLAUDE.md can become so large it crowds out actual messages. Keep it to high-level conventions and architectural patterns. Let Claude Code discover details from the codebase on its own.

- **Sub-agents reduce context load** — Instead of one agent doing everything, delegate tasks to specialized sub-agents. The main agent orchestrates; sub-agents handle specifics. This prevents the main agent's context from being flooded with task-specific details.

- **Use `/context` to see token consumption breakdown** — Claude Code's `/context` command shows which categories consume tokens. Categories include: system prompt, assistant messages, tools, MCP tools, and memory files. This transparency lets you make targeted optimizations.

## Summary

Context engineering is the key to keeping Claude Code performant as projects scale. Regularly audit and remove unused MCPs, keep CLAUDE.md high-level (not exhaustive), use sub-agents to distribute cognitive load, and monitor token consumption with `/context`. The goal: only relevant information in the thread at all times.
