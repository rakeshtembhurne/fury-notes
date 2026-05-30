---
created: 2026-03-26
tags: [inbox, draft, blog, ai, coding, claude-code]
summary: "A comprehensive guide to Claude Code Agent Teams — how they work, when to use them, how to set them up, and real-world use cases that will change how you ship software."
draft: true

## Related

- [[micro-startup-playbook]] — Build methodology using Claude Code
- [[vibe-coding]] — Vibe coding workflow context
- [[ai-coding-workflow]] — AI coding workflow patterns
- [[ai-model-war-career-strategy]] — Career leverage via Claude Code mastery

---

# Claude Code Agent Teams: The Complete Guide to Multi-Agent Development

> "Agent teams don't just run tasks in parallel — they talk to each other, coordinate, and actually collaborate. That's the fundamental difference from sub-agents."

If you've been using Claude Code for a while, you probably know about sub-agents. You fire one up, it handles a task, you get the result. It's like cloning yourself for a quick job.

But what if those clones could *talk to each other*?

That's exactly what **Agent Teams** unlock. And after spending weeks testing them across full-stack builds, code reviews, writing pipelines, and automation workflows — I can tell you: this is the biggest leap in AI-assisted development since Claude Code itself.

## The Three Modes of Claude Code

Before we dive into agent teams, understand that Claude Code operates in three distinct modes:

| Mode | Description | Use When |
|------|-------------|----------|
| **Default Mode** | Single session, single context | Simple tasks, one-off changes |
| **Sub-Agent Mode** | One session spawning isolated task agents | Parallel but non-collaborative work |
| **Agent Teams Mode** | Supervisor + communicating teammates | Complex multi-domain work requiring coordination |

The key difference between sub-agents and agent teams: **sub-agents can't talk to each other**. They only report back to the main session. In agent teams, teammates coordinate directly — they share a task list, send messages, and collaborate on the same problem from different angles simultaneously.

> [!important] The Context Rule
> Agents do NOT get your full conversation history. They only receive what you explicitly feed them via task descriptions or leader broadcasts. Context sharing is intentional, not automatic.

## What Are Agent Teams, Exactly?

An agent team consists of:

- **Leader/Orchestrator** — your main Claude Code session that spawns and coordinates the team
- **Teammates** — specialized sub-agents, each with a defined role
- **Shared Task List** — the leader distributes tasks; agents check in and pick up work
- **Direct Communication** — teammates message each other, not just the leader

## [Rest of guide continues — 306 lines total, draft status]