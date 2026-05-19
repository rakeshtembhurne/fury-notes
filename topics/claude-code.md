---
created: 2026-05-19
tags: [topics, ai, coding, agents, claude-code]
source: YouTube transcripts
---

# Claude Code - Key Learnings

## Overview

Claude Code is Anthropic's CLI coding agent that has become the gold standard for AI-powered software development. It combines terminal integration with powerful agentic capabilities including sub-agents, skills, and team collaboration.

---

## Core Capabilities

### 1. Three Operational Modes

| Mode | Description | Best For |
|------|-------------|----------|
| **Default** | Single session, direct interaction | General tasks, skill setup, team planning |
| **Sub-Agent** | One main session delegates tasks to agents | Isolated one-off tasks (e.g., adding OAuth to auth system) |
| **Agent Teams** | Multiple independent sessions working in parallel | Complex multi-faceted projects needing different perspectives |

### `/goal` — Autonomous Task Completion — May 2026

Biggest thing in AI nobody is using:
- Gives the agent an end result; it keeps working until it achieves it
- Removes you from the loop — the agent manages itself
- Running 5+ hours autonomously in production
- Quality depends on how precisely you define the loss function:
  - Bad: "/goal build this system"
  - Good: "/goal build this system with X architecture, Y output, Z constraints"
- It's NOT about prompting better — it's about defining the right objective function

### `/loop` — Recurring Task Scheduling

`/loop` schedules recurring tasks up to 3 days at a time. Examples:
- Auto-fix build issues across all PRs
- Babysit all PRs, auto-fix issues
- Worktree agents for PR auto-fix
- MCP integrations (Slack, etc.)

> Not in vault before March 2026 — added from Twitter March 2026.

### Claude Code Skills 2.0

**What Skills Are:**
- Not code, not an app, not a typical prompt
- An instructional manual in plain English teaching Claude your preferred way of doing things
- Stored as `skill.md` files in your repository

**Key Improvements in 2.0:**
- Eval tracking to measure skill effectiveness
- Better trigger detection
- Self-improvement loops

**3-Tier Skill Structure:**
```
Tier 1: YAML description (always loaded, max 15,000 chars)
Tier 2: skill.md - process steps (only when skill activates)
Tier 3: Reference files/scripts (only when needed)
```

### 3. Context Mode MCP

**Problem:** Every MCP tool call dumps full output into the 200K context window, causing context bloat after ~30 minutes.

**Solution:** Context Mode acts as a virtualization layer:
- Indexes outputs in local SQLite database using FTS5 (full-text search)
- 56KB Playwright snapshot → 299 bytes (99% reduction)
- Maintains session continuity with hooks to monitor file edits, git operations, sub-agent tasks

---

## Agent Teams

### Setup Requirements

1. Update Claude Code: `claude update`
2. Install T-Max for terminal split panes
3. Configure settings.json:
```json
{
  "tmaxSplitPanes": true,
  "claude code experimental agents": "enabled"
}
```

### Key Patterns

- **Enable via:** `ENABLE_EXPERIMENTAL_AGENT_TEAMS=true` in settings.local.json
- **Team Leader:** Handles delegation and context distribution via MD files
- **File Ownership:** Each agent should own specific files to prevent conflicts
- **Optimal Size:** 3-5 teammates max (cost scales linearly)
- **Race Condition Protection:** Built-in via Anthropic's prevention of concurrent task work

### T-Max Terminal

Creates separate terminal windows (rooms) for each agent - essential for visual monitoring. Only works in core terminal, NOT VS Code or Cursor.

---

## Workflow Frameworks

### GSD (Get Stuff Done)

For uncertain requirements where you don't want to pre-plan everything:
- **Discussion Phase:** Agent questions you to understand what to build
- **Research Phase:** Parallel sub-agents research different aspects
- **Planning Phase:** Planner + Verifier work adversarially
- **Implementation Phase:** Wave-based parallel execution
- **Verification Phase:** Cross-checks implementation against goals

### Superpowers

For known requirements with TDD approach:
- Structured workflow: brainstorming → implementation → red/green testing
- Forces agent through structured process preventing rushing
- 18 structured commands with persona flags

### BMAD Method

Breakthrough Method for Agile AI-Driven Development:
- Simulates real software team (architect, PM, developers, reviewers)
- PRD → Architecture → Sprint Planning → Coding → Review
- Multi-role locked prompts prevent agent deviation

---

## Pricing Optimization

### Claude Code Router (CCR)

Allows using Claude Code with any model from OpenRouter:
- Try new models without changing setup
- Swap Sonnet with Qwen, GLM, or others
- Free OpenAI Codex plugin for code reviews

### Cost-Saving Strategies

- Use cheaper models (Sonnet) for agents when Opus isn't necessary
- Context Mode reduces token consumption by 99%
- Check Cost tab after each session
- Claude Code Router enables free-tier models

---

## Memory & Context Management

### Preventing Context Rot

1. **Sub-Agent Isolation:** Spawn separate processes for isolated tasks
2. **Concise Documentation:** Keep project.md and context.md deliberately short
3. **Phase Tracking:** Document phases in `phases/` folder
4. **Context Recovery:** Even after clearing, agents know where to resume via phase docs

### Shared Memory Strategy

Create shared memory MD file where agents log:
- Bugs encountered
- Debugging attempts
- Fixes applied

---

### Excalidraw MCP Server

Turn codebases into visual architecture diagrams. Great for:
- Visualizing system architecture
- Understanding complex codebases at a glance
- Documenting workflows visually

> Added from Twitter March 2026.

## Key Quotes

> "AI coding agents can now deliver one-shot custom apps straight from a tweet."

> "You use GSD where you aren't really sure what to build and you don't want to pre-plan everything."

> "T-Max is like setting up rooms for each of your agents."

> "More information ≠ better output - level two is about solving skill bloat."

---

## Commands & Setup

```bash
# Update Claude Code
claude update

# Enable experimental agents
# Add to ~/.config/claude-code/settings.json:
{
  "tmaxSplitPanes": true,
  "claude code experimental agents": "enabled"
}

# Start T-Max session (before Claude)
t-max new
```

---

## Related Notes
## Cursor Composer 2.5 — May 2026

Trained on Elon Musk's Colossus 2 (200,000 GPU supercomputer):
- Near-Opus 4.7 benchmarks at a fraction of the cost
- Terminal Bench: 69.3 (Opus 4.7: 69.4)
- SWE-bench Multilingual: 79.8 (Opus 4.7: 80.5)
- $0.50/M input tokens
- Built for long-running agent work
- Being called the "Cursor killer" for solo developers

## Local Computer-Use Agents — May 2026

Run a computer-use AI agent locally for free:
- Stack: Ollama + local model + Claude Code or Codex + CUA Driver
- No cloud setup
- No data leaving your machine
- No babysitting every click

## Related Notes
- [[claude-code-agent-teams]] - Detailed Agent Teams guide
- [[claude-code-skills]] - Skills 7-level progression
- [[mcp]] - MCP servers and integrations
- [[vibe-coding]] - Vibe coding philosophy and workflows
- [[ai-agents]] - General AI agent patterns
