---
created: 2026-05-19
tags: [topics, ai, coding, agents, mcp]
source: YouTube transcripts
---

# MCP (Model Context Protocol)

## Overview

MCP (Model Context Protocol) is Anthropic's open protocol for connecting AI agents to external tools and data sources. Think of it as "USB for AI applications" - a standardized way to connect AI models to the tools they need.

---

## Why MCP Matters

1. **Standardization** - One protocol that all AI tools can use
2. **Ecosystem Growth** - 10,000+ MCP servers built in months (vs. platforms that raised millions)
3. **Flexibility** - Connect any AI model to any tool
4. **Monetization** - New opportunity for developers to build and sell MCP servers

---

## Three MCP Primitives

### 1. Resources (Lowest Leverage)
Static data files that AI can read:
- Documentation
- Configuration files
- Reference materials

### 2. Tools (Medium Leverage)
Actions the AI can perform:
- API calls
- Database operations
- File manipulations
- Web searches

### 3. Prompts (Highest Leverage) ⚠️
**Most underutilized capability!**

Pre-defined prompt templates that:
- Encode complex workflows
- Bundle multiple tool calls
- Encode business logic

> [!important]
> Most engineers skip prompts and go straight to tools. But prompts are the highest leverage primitive for MCP servers.

---

## Best MCP Servers for Claude Code

### Context7
Pulls up-to-date, version-specific documentation directly into the AI coding agent.
- Eliminates dependency mismatch issues
- Provides knowledge base on how to use any library
- Free plan available (limited to open-source libraries)

### Docker MCP Catalog
One-click installs for MCP servers:
- Beautiful curated list
- Single-click connection
- 10-minute setup for complex workflows

### Quick Data MCP Server
Gives agents arbitrary data analysis capabilities on JSON and CSV files.

### Chrome DevTools MCP
Programmatic control of browser for debugging and web scraping.

---

## MCP for Making Money

### The Opportunity

1. **Build MCP servers** for popular tools
2. **Add authentication** (Stripe integration)
3. **Charge subscription** or usage-based pricing
4. **Agent sends Stripe link** directly to end user

### Platforms Supporting MCP

- Claude Desktop
- Claude Code
- Cursor
- VS Code
- n8n
- Custom agents

---

## Docker MCP Integration

Docker has made MCP servers 100x easier:

1. Find MCP server in Docker catalog
2. One-click connect
3. Use immediately in your AI tools

**Example Workflow (10-minute setup):**
1. Pull YouTube transcript
2. Summarize in Obsidian vault
3. Read Slack for context
4. Create GitHub issue
5. Kick off Claude Code agent to implement

---

## Common Use Cases

### Research Automation
```
YouTube → Transcript → Summary → GitHub Issue → Claude Code Implementation
```

### Business Tools
- Slack integration
- Google Calendar
- Email
- CRM
- WhatsApp
- LinkedIn

### Development
- GitHub actions
- Database management
- API integrations
- Testing automation

---

## Key Insights

> "MCP is not just a protocol - it's the new standard in the AI industry. Everyone is now using it to build AI systems."

> "The highest leverage primitive of MCP servers is prompts, not tools. Most engineers completely miss this."

---

## Related Notes

- [[claude-code]] - Claude Code integration with MCP
- [[ai-agents]] - Agent patterns
- [[vibe-coding]] - Vibe coding workflows
