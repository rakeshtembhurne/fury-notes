---
created: 2026-05-19
tags: [topics, ai, coding, workflow, agents]
source: YouTube transcripts
---

# AI Coding Workflows & Frameworks

## Overview

Multiple frameworks exist for structuring AI coding workflows. Each serves different project types and planning styles.

---

## GSD (Get Stuff Done)

**Best for:** Uncertain requirements, iterative building, experimentation

### The Problem GSD Solves

Traditional vibe coding creates hundreds of files at once based on complex architecture → most fail.

### GSD Workflow

| Phase | Description |
|-------|-------------|
| **Discussion** | Agent questions you, creates context.md |
| **Research** | Parallel sub-agents research different aspects |
| **Planning** | Planner + Verifier work adversarially |
| **Implementation** | Wave-based parallel execution |
| **Verification** | Cross-checks implementation against goals |

### Key Features

- **Wave-based:** Breaks plan into parallelizable independent tasks
- **Adversarial Planning:** Dedicated planner + verifier agents
- **Context Recovery:** Phase docs enable resume after context clear
- **Sub-Agent Isolation:** Spawns separate processes to keep main context clean

---

## Superpowers

**Best for:** Known requirements, TDD approach, preventing agent mistakes

### What It Does

Forces agent through structured workflow:
1. Brainstorming
2. Implementation
3. Red/Green test-driven development
4. Sub-agents for parallel execution and code review

### Key Features

- 18 structured commands
- Persona flags (9 personas for different development aspects)
- Test-first development
- Prevents rushing and mistakes

---

## BMAD Method

**Best for:** Complex products, multi-role teams, locked-in prompts

### What BMAD Means

Breakthrough Method for Agile AI-Driven Development

### Structure

Simulates real software team:
- **Architect Agent** - System design
- **Product Manager** - Requirements
- **Scrum Master** - Sprint planning
- **Developers** - Implementation
- **Reviewers** - Code review

### Workflow

PRD → Architecture → Sprint Planning → Coding → Review

### Key Advantage

Locked prompts prevent agent deviation from process.

---

## Framework Comparison

| Framework | Best For | Planning Style | Edge Case Handling |
|-----------|----------|---------------|-------------------|
| **GSD** | Uncertain requirements | Light, feature-by-feature | Moderate |
| **Superpowers** | Known requirements | Test-first | High |
| **BMAD** | Complex products | Locked PRD → Tasks | Medium |

---

## Context Mode

**Problem:** MCP tool calls dump full output into context window → context bloat after ~30 minutes

**Solution:** Context Mode virtualization layer
- Indexes outputs in SQLite with FTS5
- 99% token reduction (56KB → 299 bytes)
- Session continuity via hooks

---

## Git Worktrees for Parallelization

Advanced technique for putting multiple agents to work:

1. Create plan
2. Deploy plan against multiple agents
3. Each works on own version of codebase
4. Take best version
5. Merge back to main branch

---

## OpenClaw + BMAD Integration

### OpenClaw Features
- Long-term agent orchestration
- Memory across sessions
- Web browsing
- Tool connections (Discord, Telegram, etc.)
- Full machine control

### Combined with BMAD
- OpenClaw manages agents
- BMAD provides structured development process
- Memory + structure = autonomous SaaS building

---

## Key Principles

1. **Context Rot Prevention** - Use sub-agents for isolation
2. **Iteration Over Pre-planning** - Build incrementally
3. **Verification Loops** - Ensure implementation matches goals
4. **Right Model for Right Task** - Sonnet vs Opus optimization

---

## Commands & Setup

```bash
# Enable experimental agents
ENABLE_EXPERIMENTAL_AGENT_TEAMS=true

# T-Max setup
t-max new

# GSD installation
# Copy install command in project folder
# Select agent (Claude, etc.)
# Choose scope: project level (recommended)
```

---

## When to Use Each

| Scenario | Use |
|----------|-----|
| Unclear requirements | GSD |
| Known what to build | Superpowers |
| Complex multi-role project | BMAD |
| Preventing context rot | GSD with sub-agents |
| Need visual monitoring | T-Max |
| Combining frameworks | GSD (core) + Superpowers (remaining) |

---

## Related Notes

- [[claude-code]] - Claude Code specifics
- [[claude-code-agent-teams]] - Agent Teams
- [[vibe-coding]] - Vibe coding philosophy
- [[ai-agents]] - General agent patterns
