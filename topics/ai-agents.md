---
created: 2026-05-19
tags: [topics, ai, coding, agents]
source: YouTube transcripts
---

# AI Agents

## Overview

AI agents are intelligent systems that handle tasks without human intervention. They represent a new paradigm in how we build software and automate workflows.

---

## What Are AI Agents?

**Definition:** Digital employees that:
- Work 24/7, never get tired
- Automate tedious tasks
- Communicate, analyze data, make decisions
- Bridge the gap between humans and machines

### Real-World Examples

- **Salesforce Agent Force** - Finance and manufacturing optimization
- **M&A Research** - Scraping, analyzing, personalized outreach
- **Software Development** - Autonomous coding teams

---

## Agent Architectures

### Memory Systems

**Problem:** Stateless applications don't remember past interactions.

**Solution:** Agent memory patterns:
1. **Short-term:** Context window
2. **Long-term:** Persistent storage (SQLite, vector DBs)
3. **Semantic:** Learned patterns and preferences

### Levels of Agenticity

Agenticity exists on a spectrum:
- **Level 1:** Single prompt, single response
- **Level 2:** Tool use
- **Level 3:** Multi-step reasoning
- **Level 4:** Planning and sub-agent delegation
- **Level 5:** Full autonomy with self-improvement

---

## Agent Patterns

### 1. Orchestrator-Worker

```
Main Agent (Orchestrator)
    ├── Worker Agent 1 (Frontend)
    ├── Worker Agent 2 (Backend)
    └── Worker Agent 3 (QA)
```

### 2. Hierarchical

```
Manager Agent
    ├── Senior Agent 1
    │   └── Junior Agent 1
    │   └── Junior Agent 2
    └── Senior Agent 2
```

### 3. Collaborative

```
Agent A ←→ Agent B
    ↓           ↓
  Task      Task
```

---

## Building AI Agents

### n8n Workflows

Popular for building agents without code:
1. Define trigger (Telegram, Slack, Discord, etc.)
2. Add AI agent node
3. Connect tools and data sources
4. Set up authentication

### Claude Agent SDK

```typescript
// Basic example
import { query } from 'claude-code';
const result = await query({
  prompt: 'What model should I use?',
  model: 'claude-sonnet'
});
```

### OpenClaw

Open-source agent platform:
- Supervisor for sub-agents
- Long-term semantic memory
- Tool connections (Discord, Telegram, etc.)
- Gateway for browser/messaging interaction

---

## Claude 4 + Agent Capabilities

### Opus 4.6 Features

- Extended thinking for complex tasks
- Better error recovery
- 1M token context window option
- Agent Teams support

### Sonnet 4

- Fast workhorse model
- Cost-effective for routine tasks
- Good for agents that don't need deep reasoning

---

## Agent Teams

### Benefits

1. **360-Degree Perspective** - Different agents examine different angles
2. **Parallel Execution** - Multiple agents work simultaneously
3. **Specialization** - Each agent focused on domain
4. **Quality Control** - Review agents check work

### Best Practices

- Assign explicit file ownership
- Define clear task dependencies
- Use plan approval mode for quality
- Keep 3-5 agents max

---

## Self-Improving Agents

### Hermes Agent

First self-improving agent:
1. Execute task with current prompt
2. Evaluate output quality
3. Analyze failure modes
4. Refine prompt/parameters
5. Re-execute
6. Repeat until convergence

### Claude + Hermes

- Claude Code: Fast, single-prompt coding
- Hermes: Iterative, learning-based workflows
- Combined: 10x productivity

---

## CrewAI

Multi-agent framework with hierarchical processes:

### Key Features

1. **Hierarchical Processes** - Manager agents coordinate crews
2. **Async Tasks** - Parallel task execution
3. **Expected Outputs** - Structured agent responses
4. **Callbacks** - Post-task automation

### Use Cases

- Research crews (search → summarize → format)
- Content creation (research → write → edit → publish)
- Business automation (analyze → decide → act)

---

## 5 Must-Have AI Agents

1. **Accountant Agent** - Automates bookkeeping
2. **Research Agent** - Gathers and synthesizes information
3. **Outreach Agent** - Personalized communication at scale
4. **Analyzer Agent** - Data processing and insights
5. **Coordinator Agent** - Orchestrates other agents

---

## Business Applications

### M&A Automation
```
Web Scraping → Company Analysis → Personalized Outreach → CRM Updates
```

### Content Workflow
```
Research → Write → Edit → Format → Publish
```

### Customer Service
```
Query → Classify → Respond → Escalate → Follow-up
```

---

## Key Quotes

> "Agent teams have a shared task list. The huge unlock is that teammates can talk to each other."

> "You can deploy each agent and tell them: look at this from the left side, look at this from the right side, and go upstairs and look at it from the top down."

> "Companies are now hiring AI agents instead of actual humans."

---

## Related Notes

- [[claude-code]] - Claude Code agent capabilities
- [[claude-code-agent-teams]] - Agent Teams
- [[mcp]] - MCP for agent tool connections
- [[vibe-coding]] - Building with agents
