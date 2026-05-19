---
created: 2026-05-19
tags: [topics, ai, coding, cursor]
source: YouTube transcripts
---

# Cursor AI

## Overview

Cursor is an AI-first code editor that combines traditional IDE features with powerful AI capabilities. It's designed to make AI coding accessible and efficient.

---

## Key Features

### Agent Mode

Cursor has AI agents that can:
- Work on specific tasks independently
- Handle security concerns
- Fix bugs autonomously
- Build features end-to-end

### Model Selection

Available models:
- Claude 4 Sonnet (default)
- Claude 4 Opus
- GPT models
- Gemini
- DeepSeek
- Grok

### Interface

- **Left sidebar:** File explorer
- **Bottom:** Terminal
- **Right:** AI agent panel
- **Settings:** Model configuration, rules

---

## Getting Started

### Opening Projects

1. **Open** - Local folder
2. **Clone** - From GitHub URL
3. **Connect** - SSH for remote development

### Basic Workflow

1. Open/create project
2. Configure AI rules
3. Start chatting with AI
4. Accept/reject suggestions
5. Use agent mode for autonomous tasks

---

## Cursor Rules

Rules define how Cursor AI should behave:

### Types of Rules

1. **Project Rules** - Project-specific behavior
2. **User Rules** - Personal preferences
3. **Workspace Rules** - Team-wide standards

### Best Practices

- Be specific about coding standards
- Define file structure preferences
- Set testing requirements
- Specify commit message format

---

## Agent Configuration

### Setting Up Models

1. Go to Settings → Models
2. Enable desired models
3. Set default model
4. Configure API keys

### Agent Capabilities

```markdown
- Code completion
- Inline edits
- Chat context
- File creation
- Git operations
- Terminal commands
```

---

## Vibe Coding with Cursor

Cursor is excellent for vibe coding:

### Advantages

1. **No context limits** - Unlike cloud-based tools
2. **No death spirals** - Local processing
3. **Full IDE features** - Debugging, git, terminal
4. **Model flexibility** - Use any model

### Workflow

1. Describe what you want to build
2. Cursor generates code
3. Review and iterate
4. Use agent mode for complex tasks

---

## Integration with Claude Code

Cursor can work alongside Claude Code:

### When to Use Each

| Task | Tool |
|------|------|
| Quick edits | Cursor |
| Complex refactoring | Claude Code |
| Debugging | Cursor |
| Large features | Claude Code |
| Multi-file changes | Claude Code |

### Combined Workflow

1. Plan in Cursor
2. Implement in Claude Code
3. Debug in Cursor
4. Review in Cursor

---

## Pricing Comparison

### vs. Other Tools

| Tool | Cost | Context Limit |
|------|------|---------------|
| Cursor Pro | $20/month | High |
| Claude Code | $20-100/month | 200K tokens |
| Lovable | $20+/month | Limited |
| Bolt | Varies | Limited |
| v0 | $20+/month | Limited |

---

## Tips for Cursor

### 1. Use Rules Files

Create `.cursorrules` file in project root for project-specific AI behavior.

### 2. Model Selection

- Use Sonnet for fast, routine tasks
- Use Opus for complex, reasoning tasks
- Use Claude Code for terminal-heavy work

### 3. Agent Mode

Let Cursor agents work autonomously on:
- Bug fixes
- Security patches
- Test writing
- Documentation

### 4. Keyboard Shortcuts

- Cmd+K - Inline edit
- Cmd+L - Chat panel
- Cmd+Enter - Accept suggestion

---

## Related Notes

- [[claude-code]] - Claude Code workflows
- [[vibe-coding]] - Vibe coding philosophy
- [[ai-coding-workflow]] - Workflow frameworks
- [[ai-agents]] - Agent patterns
