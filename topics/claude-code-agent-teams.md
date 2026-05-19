---
created: 2026-05-19
tags: [topics, ai, coding, agents, claude-code, agent-teams]
source: YouTube transcripts
---

# Claude Code Agent Teams

## Overview

Agent Teams is Claude Code's multi-agent collaboration feature where specialized agents work together on complex projects. It solves the "tunnel vision" problem where single agents gravitate toward one area and struggle to see problems from multiple perspectives.

---

## Three Modes of Claude Code

| Mode | Sessions | Use Case | Limitation |
|------|----------|----------|------------|
| **Default** | Single | General admin, model selection, skill setup | Tunnel vision on large codebases |
| **Sub-Agent** | One main + agents | Delegating single tasks | Returns only final output, no steps |
| **Agent Teams** | Multiple independent | Complex multi-faceted tasks | Cost scales linearly |

---

## Agent Teams vs Sub-Agents

| Feature | Sub-Agents | Agent Teams |
|---------|-----------|-------------|
| Communication | Only through main agent | Teammates talk directly |
| Task List | Individual, isolated | Shared task list |
| Best For | Quick, one-off tasks | Multi-domain, collaborative |
| Cost | 1x | Scales with agent count |

---

## Setup Requirements

### 1. Enable Experimental Flag

Add to project settings.local.json:
```json
{
  "ENABLE_EXPERIMENTAL_AGENT_TEAMS": true
}
```

### 2. Install T-Max

Creates separate terminal windows for each agent - essential for managing multiple agents.

> [!important]
> T-Max only works in core terminal, NOT in VS Code or Cursor.

### 3. Configure Claude Code

```bash
# Add to settings.json:
{
  "tmaxSplitPanes": true,
  "claude code experimental agents": "enabled"
}
```

### 4. Start T-Max First

```bash
t-max new
# Then launch Claude Code
```

---

## Prompting Pattern

```
Goal: [what you want to achieve]
Create a team of [X] teammates using [model].
The first agent is [role] and should [task]. It can talk to [other agents].
The second agent is [role] and should [task]. It should wait for [agent's] message.
Final deliverables: [specific outputs you want]
```

---

## Best Practices

### Do's

- ✅ Assign each agent specific files
- ✅ Define clear, specific outputs
- ✅ Name recipients for messages
- ✅ Keep 3–5 teammates
- ✅ Give full context at startup
- ✅ Use T-Max for visual monitoring

### Don'ts

- ❌ Have agents share/edit same files
- ❌ Use vague deliverables
- ❌ Assume agents know who to talk to
- ❌ Use massive agent swarms (10+)
- ❌ Leave agents without initial context

---

## Team Workflow Example

For a landing page project:

1. **Main Agent** creates team with three members:
   - Frontend developer (UI, animations, copy)
   - Backend developer (server-side logic)
   - QA agent (reviews and finds issues)

2. **Parallel Execution:**
   - Frontend and backend send work to QA
   - QA finds issues and sends back
   - Agents take another pass to resolve

3. **Final Delivery:** Polished, one-shot landing page

---

## Key Features

### Shared Task List
- All teammates see same task list
- Enables coordination and priority management

### Direct Communication
- Teammates can talk without going through main agent
- Enables real-time collaboration

### Plan Approval Mode
- Teammates can plan first before executing
- Get approval from main agent before running

### Clean Shutdown
- Send shutdown requests via main agent
- Wait for each agent to confirm saving
- Release shared resources

---

## Monitoring with T-Max

T-Max terminal provides:
- Split-pane view showing each agent
- Agent names and colors
- Real-time thinking and actions
- Direct messaging to any teammate
- Team status updates

---

## Cost Considerations

- Check Cost tab after each session
- Use cheaper models (Sonnet) for agents when Opus isn't necessary
- 3–5 teammates optimal - beyond 5, coordination overhead outweighs parallelism gains
- Use fewer agents to save tokens

---

## Common Pitfalls & Fixes

| Problem | Fix |
|---------|-----|
| Agents keep asking for permissions | Pre-approve tools in project settings |
| Deliverables feel fragmented | Assign explicit file owners |
| One agent is sitting idle | Define explicit tasks and dependencies |
| Burning too many tokens | Use fewer agents |
| Agents losing work | Have them save to temporary files |

---

## When to Use Agent Teams

**Use Agent Teams when:**
- Project has multiple different areas needing specialization
- Tasks can be done in parallel
- Agents need to communicate and react to each other
- High quality with multiple review steps is required

**Use Sub-Agents instead when:**
- Tasks are purely sequential (1 → 2 → 3)
- Everything must be in one context window
- Multiple agents working on same files
- Simple, straightforward tasks
- You want to save tokens

---

## Related Notes

- [[claude-code]] - General Claude Code guide
- [[claude-code-skills]] - Skills progression
- [[ai-coding-workflow]] - Workflow frameworks (GSD, Superpowers, BMAD)
