---
created: 2026-05-19
tags: [topics, ai, coding, agents, crewai]
source: YouTube transcripts
---

# CrewAI

## Overview

CrewAI is a multi-agent framework for building AI crews that work together on complex tasks. It supports hierarchical processes, async tasks, expected outputs, and callbacks.

---

## Key Features

### 1. Hierarchical Processes

Crews now support chain of command:
- **Manager agents** coordinate the work
- **Senior agents** handle complex delegation
- **Junior agents** execute specific tasks

### 2. Async Tasks

Run multiple agents simultaneously:
- Parallel task execution
- Non-blocking workflows
- Faster completion times

### 3. Expected Outputs

Define structured responses:
- Consistent output format
- Validation mechanisms
- Type-safe results

### 4. Callbacks

Post-task automation:
- Trigger actions after task completion
- Integration with external systems
- Workflow automation

---

## CrewAI Tutorial - Building Newsletter

### Example: AI Newsletter Crew

**Workflow:**
1. Research agent - Searches web for AI articles
2. Summarize agent - Condenses content
3. Format agent - Creates newsletter layout

### Setup

```python
from crewai import Agent, Crew, Task, Process

# Create agents
researcher = Agent(role='Researcher', ...)
summarizer = Agent(role='Summarizer', ...)
formatter = Agent(role='Formatter', ...)

# Create crew
newsletter_crew = Crew(
    agents=[researcher, summarizer, formatter],
    tasks=[...],
    process=Process.hierarchical
)
```

---

## Use Cases

### Content Creation
- Research → Write → Edit → Format → Publish

### Business Automation
- Analyze → Decide → Act → Report

### Research
- Search → Extract → Synthesize → Present

---

## Best Practices

### 1. Define Clear Roles
Each agent should have:
- Specific role
- Clear goals
- Defined tools

### 2. Structure Tasks
- Clear descriptions
- Expected outputs
- Dependencies

### 3. Use Callbacks
- Post-task notifications
- Integration triggers
- Error handling

---

## Related Notes

- [[ai-agents]] - General agent patterns
- [[vibe-coding]] - Vibe coding workflows
- [[claude-code]] - Claude Code
