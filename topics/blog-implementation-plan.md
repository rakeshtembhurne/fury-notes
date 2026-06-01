---
created: 2026-05-19
tags: [topic, content-planning, implementation, blog]
source: notes directory
---

# Blog Implementation Plan — GSC Prioritized

> Based on Google Search Console data analysis. All articles target proven high-CTR queries.

## Priority Queue

| # | Priority | Article | Status | Notes |
|---|----------|---------|--------|-------|
| 1 | URGENT | `01-Claude-Code-Router-Multi-Model-Guide.md` | Draft | Targets query at pos 4.76 |
| 2 | URGENT | `02-Strengthen-Top-Claude-Post.md` | Update | Protect 82% of traffic |
| 3 | HIGH | `03-Docker-Guide-Fix-CTR.md` | Update | 12K impressions, low CTR |
| 4 | MEDIUM | `04-NextJS-Modular-Architecture.md` | Draft | 12.7% CTR, pos 5.87 |
| 5 | MEDIUM | `05-Anthropic-Custom-Headers-Deep-Dive.md` | Draft | Top query by clicks (18) |
| 6 | FROM VAULT | `06-Claude-Code-Agent-Teams-Complete.md` | Draft | Move from Inbox |
| 7 | FROM VAULT | `07-AI-Model-War-Career-Strategy.md` | Draft | Move from Inbox |
| 8 | NEW | `08-Remotion-Video-Automation.md` | Draft | AI-powered video generation story |

## Status Legend

- `[ ]` Not started
- `[o]` In progress
- `[x]` Complete

## How to Use

1. Read each article draft in numbered order
2. Edit/refine the content
3. Move to blog project: `data/blog/ai/` (for AI articles) or appropriate folder
4. Publish and monitor GSC for position changes

## GSC Data Reference

| Metric | Value |
|--------|-------|
| Top post clicks | 343 (extend-claude-code-multiple-models guide) |
| Best query | `claude code multiple models` — 9.85% CTR, pos 4.76 |
| Quick CTR win | Docker guide — 12,605 impressions, 0.04% CTR |

---

# Article 01: Claude Code Router: Connect Any AI Model (DeepSeek, Qwen, Gemini)

> [!quote]
> "Use Qwen 3 Coder inside Claude Code's agent framework via Claude Code Router — giving you ~1,000 free requests per day with Claude Code's agent quality, all without paying $100/month for Claude Max."

Your GSC data shows the query `claude code multiple models` gets **9.85% CTR at position 4.76** — one solid article gets you to page one. This is that article.

## What Is Claude Code Router?

Claude Code Router (CCR) is an open-source wrapper (7,600+ GitHub stars) that lets you run Claude Code with *any* LLM provider — not just Anthropic's models.

The setup: you run `ccr code` instead of `claude`. Inside, you get Claude Code's full agent interface — hooks, sub-agents, MCP, `/commands` — but every model call routes through OpenRouter to your chosen provider.

| What you use | Cost | What you get |
|-------------|------|-------------|
| Claude Code native (Sonnet/Opus) | $20-100/month | Best agent, your chosen model |
| CCR + Qwen 3 Coder | Free (1,000 req/day via OpenRouter) | Nearly same quality, zero cost |
| CCR + DeepSeek V3 | ~$0.01/M tokens | Fast, very cheap |
| CCR + Gemini 2.0 Flash | ~$0.10/M tokens | Extremely fast |

## Why You Probably Don't Need Claude Max ($100/month)

Here's what nobody tells you about the Claude Max plan:

**Opus pricing is $30 per million tokens.** That's 5x more expensive than Sonnet ($6/M tokens).

In practice, even on the $100/month Max plan, Opus hits usage limits in as little as 2 minutes of heavy coding. Reddit is full of complaints: "Opus hits limit after 2 minutes," " Opus 4 reaches usage limits 5x faster than expected."

| Plan | Monthly Cost | Opus Access | Real-World Limit |
|------|-------------|-------------|-----------------|
| Pro | $20 | Web/desktop only, 5-hour windows | Enough for thoughtful work |
| Max 5x | $100 | All platforms + CLI | Burns through limits fast |
| CCR + OpenRouter | Free-$5 | Any model, any platform | Unlimited at free tier |

**The CCR strategy**: Use your Pro plan's 5-hour windows normally. Hit the limit at hour 4? Switch to `ccr code` routed through OpenRouter — get a fresh session without touching your Anthropic quota.

## What You Need Before Starting

1. **Claude Code installed** (Pro or Max plan)
2. **OpenRouter account** — sign up at openrouter.ai (free tier available)
3. **An API key** from OpenRouter
4. **Node.js 18+** — for running CCR

## Step 1: Install Claude Code Router

Clone the official repo:

```bash
git clone https://github.com/anthropics/claude-code-router
cd claude-code-router
npm install
```

Or install globally via npm:

```bash
npm install -g claude-code-router
```

Verify the installation:

```bash
ccr --version
```

## Step 2: Get Your OpenRouter API Key

1. Go to [openrouter.ai/keys](https://openrouter.ai/keys)
2. Create a new key
3. Copy it — you'll paste it into the CCR config

**Free tier limits worth knowing:**

| Provider | Free Tier | Notes |
|---------|----------|-------|
| OpenRouter | 1,000 requests/day | Resets every 24 hours |
| Qwen 3 Coder (via OpenRouter) | 1,000 requests/day | Best free coding model |
| DeepSeek V3 | ~$0 budget | Very cheap after free tier |

## Step 3: Configure CCR

Create a config file at `~/.config/ccr/config.json`:

```json
{
  "provider": "openrouter",
  "apiKey": "***",
  "defaultModel": "anthropic/claude-3.5-sonnet"
}
```

**Available models to configure:**

| Model | Model ID (OpenRouter) | Cost | Best For |
|-------|----------------------|------|----------|
| Qwen 3 Coder 32B | `qwen/qwen3-coder-32b` | Free (1K/day) | Quick tasks, boilerplate |
| DeepSeek V3 | `deepseek-ai/deepseek-chat-v3` | ~$0.01/M tokens | General coding |
| Gemini 2.0 Flash | `google/gemini-2.0-flash` | ~$0.10/M tokens | Fast responses |
| Claude Sonnet (via OpenRouter) | `anthropic/claude-3.5-sonnet` | ~$3/M tokens | Balanced |
| Claude Opus (via OpenRouter) | `anthropic/claude-3-opus` | ~$15/M tokens | Complex reasoning |

**Pro tip**: Set Qwen 3 Coder as your default for routine tasks, switch to Opus only for architectural decisions.

## Step 4: Launch and Verify

Start Claude Code with CCR:

```bash
ccr code
```

Verify your setup is working correctly:

```bash
ccr doctor
```

This checks:
- API connectivity to OpenRouter
- Model availability for your plan
- Token cost estimates for your default model

You should see output like:

```
✅ OpenRouter connection: OK
✅ Default model: qwen/qwen3-coder-32b
✅ Estimated cost per 1K tokens: $0.00 (free tier)
⚠️  Rate limit: 1,000 requests/day (resets in 14 hours)
```

## Step 5: Switch Models Mid-Session

One of CCR's most powerful features: switch models with a command.

Inside any Claude Code session:

```
/model qwen/qwen3-coder-32b
```

Or for complex tasks that need deeper reasoning:

```
/model anthropic/claude-3-opus
```

CCR intercepts this and routes to the correct provider through OpenRouter — no restart needed.

## Real-World Workflow: How I Use CCR

Here's my actual setup after 3 months of using CCR daily:

**Morning (Pro plan, fresh window):**
- Use Claude Code native for architecture planning
- Start new projects, set up folders
- Anything requiring deep Opus reasoning

**Afternoon (CCR + Qwen, when Pro quota runs low):**
- `ccr code` — switched to Qwen 3 Coder
- Quick features, bug fixes, refactoring
- Documentation updates

** Evening (CCR + DeepSeek, for bulk work):**
- Batch processing, test writing
- Anything that needs speed over depth

This workflow costs me roughly **$3-5/month** on OpenRouter instead of $100 for Max.

## The Code Review Pipeline (Real Example)

With CCR and Claude Code Agent Teams, I set up a pipeline where different agents use different models:

```
/agent-team create code-review-team
- Architecture specialist: anthropic/claude-3-opus (deep reasoning)
- Implementation agents (2x): qwen/qwen3-coder-32b (fast, free)
- Review specialist: deepseek-ai/deepseek-chat-v3 (cheap review)
```

Each agent routes through its optimal model. The leader (my main session) coordinates. Total cost for a full-stack code review: roughly $0.02.

## Common Mistakes and How to Avoid Them

**Mistake 1: Forgetting to set budget alerts on OpenRouter**
Even cheap models add up. Go to openrouter.ai/settings and set a monthly spend cap.

**Mistake 2: Using Opus by default**
Opus is extraordinary but $15/M tokens. Use it only when you genuinely need deep reasoning. Set Qwen or DeepSeek as your default.

**Mistake 3: Not running `ccr doctor` after config changes**
Every time you change your config, verify before starting a session.

**Mistake 4: Mixing up the config file location**
 CCR looks for config at `~/.config/ccr/config.json`. If yours is elsewhere, specify it:

```bash
ccr code --config /path/to/your/config.json
```

## Limitations to Know

- **Context window varies by provider** — Qwen 3 Coder has 32K context; DeepSeek V3 has 128K; check before starting large refactors
- **Not all providers support streaming** — CCR handles this, but some features may degrade
- **MCP server behavior varies** — test your MCP setup with each model
- **Free tier rate limits** — OpenRouter's 1K/day resets every 24 hours; plan accordingly

## Quick Reference

```bash
# Install
git clone https://github.com/anthropics/claude-code-router && cd claude-code-router && npm install

# Launch
ccr code

# Check setup
ccr doctor

# Switch model mid-session
/model qwen/qwen3-coder-32b

# Check status
ccr status
```

---

# Article 02: [UPDATE] Extend Claude Code: Connect Multiple AI Models — Complete Guide

> **Status: Update needed** — This is your #1 traffic post (343 clicks). Currently ranking at position 8.6. Goal: push to page 1.

## What's Working (Keep)

- Post title matches high-CTR query: `claude code multiple models` (9.85% CTR, pos 4.76)
- Topic is clearly relevant — people are searching for this
- 39,011 impressions — strong discovery

## What Needs Improvement

### 1. Expand the "Why" Section
Add a stronger opening argument for *why* you'd want multiple models:
- Cost optimization (use cheap models for simple tasks)
- Specialization (different models for different job types)
- Free tier access (Qwen 3 Coder via OpenRouter)
- Backup when Anthropic is down

### 2. Add a Comparison Table

| Task Type | Best Model | Why |
|-----------|------------|-----|
| Architecture/planning | Claude Opus | Deep reasoning |
| Quick scripts | Qwen 3 Coder | Fast, free |
| Long boring tasks | DeepSeek V3 | Cheap |
| Documentation | Gemini Flash | Speed |

### 3. Add Internal Links
Link to:
- Docker guide (infrastructure context)
- Terminal commands (developer tooling)
- Any other Claude Code posts you publish

### 4. Update the CCR Section
Claude Code Router has evolved. Update the install commands and add:
- The `ccr status` command
- The `ccr doctor` diagnostic tool
- The `/model` natural language switching

### 5. Add "Common Mistakes" Section
- Forgetting to set API keys in environment variables
- Using the wrong base URL for different providers
- Not monitoring token usage

### 6. Strengthen the CTA
End with: "Try CCR with Qwen 3 Coder today — it's free and takes 5 minutes to set up."

## Suggested New Structure

```
1. Introduction (expand "why")
2. What Is Claude Code Router?
3. Prerequisites
4. Step-by-Step Setup (update commands)
5. Model Comparison Table (NEW)
6. The Hybrid Workflow (NEW)
7. Common Mistakes (NEW)
8. FAQ
9. Stronger CTA
```

## Target Keyword
`claude code multiple models` — you're at 4.76. Push to 1-3.

## Check Before Publishing
- [ ] Updated install commands work
- [ ] Screenshots reflect current CCR version
- [ ] Links to other blog posts added
- [ ] Meta description updated: "Learn how to use Claude Code with multiple AI models including DeepSeek, Qwen, and Gemini. Complete 2026 guide."

---

# Article 03: [UPDATE] Docker Complete Guide for Developers — Fix the CTR

> **Status: Update needed** — 12,605 impressions, 0.04% CTR, position 8.18. You're close to page 1. The fix is in the title and opening.

## Why You Have Low CTR

Your Docker guide ranks at position 8.18 — great! But 12,605 impressions with only 5 clicks means people are seeing your result and *not clicking*.

Common reasons:
1. **Title doesn't feel specific enough** — "Docker Complete Guide" is too generic
2. **Meta description is weak** — doesn't promise a specific outcome
3. **URL slug is too long** — `docker-complete-guide-for-developers` vs something tighter
4. **Google picked a bad snippet** — your actual page content is better than what's showing

## The Fix: Title & Meta Description

**Current title:**
`docker complete guide for developers`

**New title options (pick one):**
- `Docker for Developers in 2026: The Only Guide You'll Need` — modern, confident
- `Docker Complete Guide: From Zero to Production (2026)` — outcome-focused
- `How to Use Docker: A Practical Guide for Developers` — clear, simple

**Current meta description:**
*(check what's currently set in the frontmatter)*

**New meta description:**
> "Step-by-step Docker tutorial for developers. Learn containers, images, Docker Compose, and production deployment. Covers Docker 2026 best practices."

## Content Audit Checklist

### Keep (What's Working)
- Structure seems solid — keep the existing format
- Developer audience is correct
- Topic relevance is high (12K impressions prove it)

### Fix
- [ ] Update title to be more specific and modern
- [ ] Update meta description with specific outcome promise
- [ ] Add "Last updated: 2026" indicator — shows freshness
- [ ] Add a quick-start code snippet at the top — readers want to copy-paste fast
- [ ] Check if URL slug can be shortened

### Optional (If You Have Time)
- Add a "Common Docker Mistakes" section
- Add comparison table: Docker vs Podman vs containerd
- Add a TL;DR at the top for skimmers

## Quick Win: Add This to Your Opening

Add before the first heading:

```markdown
> **In this guide:** Docker installation, images, containers, volumes, Docker Compose, and production deployment — all with code examples you can copy and run.
```

This gives Google a rich snippet and sets clear expectations for the reader.

## Target Query
`docker complete guide for developers` — you're at 8.18. Move to 1-5 and you'll see clicks jump significantly.

---

# Article 04: Next.js Modular Architecture: A Practical Guide (2026)

> [!quote]
> "Modular architecture in Next.js isn't about folder structure — it's about creating systems where each piece has one job, can be understood in isolation, and can be replaced without breaking the whole."

Your blog has a post on Next.js plugin architecture that pulls 51 clicks at position 8.03. This article targets `next js modular architecture` — **12.7% CTR at position 5.87**, nearly page one. That CTR tells you everything: developers searching for this term know exactly what they want, and the page that delivers it wins.

## Why Modular Architecture Matters More in Next.js 15

Next.js 15 changed the game in three ways that make modularity non-negotiable:

1. **React Server Components (RSC) by default** — components render on the server unless you explicitly opt into client behavior.
2. **Route Handler improvements** — `/app` route handlers are now the standard for API routes.
3. **Server Actions stable since Next.js 14.2** — actions live inside components.

## The Three Pillars of Next.js Modular Architecture

### Pillar 1: Feature-Based Folder Structure

The standard `components/` folder is a junk drawer. Instead, co-locate by feature:

```
/app
  /(marketing)           # Route group: marketing pages
    /landing
    /pricing
  /(dashboard)           # Route group: authenticated app
    /settings
    /analytics
/components
  /(marketing)           # Matches route group
    /pricing-table
    /faq-accordion
  /(dashboard)
    /metric-card
    /date-range-picker
  /(shared)              # Truly cross-cutting
    /button
    /modal
    /form-input
/lib
  /modules
    /auth               # Auth module: all auth-related logic
    /billing            # Billing module
    /analytics          # Analytics module
  /plugins              # Plugin system
  /providers            # React context providers
```

The rule: if you can't move a folder to a different project without breaking it, the boundaries are wrong.

### Pillar 2: The Module Pattern

A module in Next.js modular architecture isn't just a TypeScript file — it's a self-contained unit with explicit dependencies and a public interface.

### Pillar 3: Plugin Architecture for Extension Points

Next.js 15's plugin system lets you build extension points into your app.

## Quick Reference: Modular Architecture Checklist

```
Before shipping any Next.js 15 route:
□ Is this route part of a route group?
□ Where do the imports come from — components or modules?
□ Can this route work if I replace its dependencies?
□ Is business logic in a module, not a Server Component?
□ Can I test this in isolation without mounting the full app?
```

---

# Article 05: Anthropic Custom Headers in Claude Code: The Complete Guide

> [!quote]
> "Custom headers let you pass additional context to Anthropic's API — metadata, user identifiers, experiment flags, anything you need — without touching the model parameters."

Your GSC data shows `anthropic_custom_headers` as your **#1 query by clicks** — 18 clicks, 764 impressions, 2.36% CTR at position 7.62. That position 7.62 is a fast page-one jump.

## What Are Custom Headers?

Anthropic's API accepts custom HTTP headers on every request, prefixed with `x-`. These headers:
- **Never reach the model** — they're metadata only
- **Appear in your usage logs** — filter, segment, and analyze by any header value
- **Don't affect output quality** — purely operational/cost/logging metadata
- **Work with any Claude model** — Sonnet, Opus, Haiku, all support them

## How to Configure Custom Headers in Claude Code

### Method 1: Environment Variable (Global)
```bash
export ANTHROPIC_CUSTOM_HEADERS="x-user-id:user123,x-session:abc456,x-project:website-redesign"
```

### Method 2: Claude Code Settings File (Per-User)
Add to `~/.claude/settings.json`:
```json
{
  "customHeaders": {
    "x-user-id": "user-abc123",
    "x-session": "claude-code-prod",
    "x-environment": "production",
    "x-experiment-flag": "prompt-v3-test"
  }
}
```

### Method 3: Per-Project Config (Best for Teams)
In your project's `.claude/config.json`:
```json
{
  "customHeaders": {
    "x-project-id": "my-nextjs-app",
    "x-environment": "development",
    "x-team": "frontend",
    "x-cost-center": "platform-engineering"
  }
}
```

### Method 4: Claude Code Router (CCR)
```bash
export ANTHROPIC_CUSTOM_HEADERS="x-provider:openrouter,x-request-source:ccr"
```

## Advanced Use Cases

### Multi-Tenant Cost Attribution (Agency Use)
```bash
export ANTHROPIC_CUSTOM_HEADERS="x-client-id:acme-corp,x-client-project:website-redesign-v2,x-billing-category:full-service"
```

### Prompt Experiment Tracking
```json
{
  "customHeaders": {
    "x-experiment": "system-prompt-v3",
    "x-variant": "B",
    "x-hypothesis": "more-structured-output-reduces-errors"
  }
}
```

## Common Issues and Fixes

| Problem | Cause | Fix |
|---------|-------|-----|
| Headers not applying | Claude Code not restarted after env var change | Quit and relaunch Claude Code |
| Format wrong | Using `=` in env var format | Use colon: `key:value`, not `key=value` |
| Headers in logs but not billing | Headers are metadata only | They appear in detailed API logs, not the billing summary page |
| Per-project headers bleeding | Config in wrong location | Use `.claude/config.json` for project-level |

### The Restart Rule
Claude Code reads env vars at startup, not continuously. If you set `ANTHROPIC_CUSTOM_HEADERS` in your shell profile and have Claude Code open, the change won't take effect until you fully quit and relaunch.

## Quick Reference

```bash
# Global env var (add to ~/.zshrc)
export ANTHROPIC_CUSTOM_HEADERS="x-user-id:your-id,x-project:your-project"

# In ~/.claude/settings.json (per-user, all projects)
{
  "customHeaders": {
    "x-user-id": "user-abc",
    "x-environment": "production"
  }
}

# In .claude/config.json (per-project)
{
  "customHeaders": {
    "x-project-id": "my-app",
    "x-team": "frontend"
  }
}

# Verify inside Claude Code
/echo $ANTHROPIC_CUSTOM_HEADERS
```

---

# Article 06: [MOVE FROM INBOX] Claude Code Agent Teams: The Complete Guide to Multi-Agent Development

> **STATUS: Move this file from `Inbox/Claude-Code-Agent-Teams-Complete-Guide.md`**

## Action Required

1. Move `Inbox/Claude-Code-Agent-Teams-Complete-Guide.md` → `data/blog/ai/claude-code-agent-teams-complete-guide.mdx`
2. Update frontmatter `date` to today's date
3. Update `picsumId` to a relevant image ID
4. Remove `[MOVE FROM INBOX]` from title
5. Add internal links to other Claude Code posts on the blog

## Cross-Link Opportunities
- Link to `extend-claude-code-multiple-models-complete-guide` (your top post!)
- Link to `most-essential-terminal-commands` (developer tooling context)
- Link to Docker guide (infrastructure context)

## Meta Description Suggestion
> "Learn Claude Code Agent Teams — how to set up multi-agent development, use cases, setup configuration, and real-world examples. The complete 2026 guide."

---

# Article 07: [MOVE FROM INBOX] The AI Model War: Why Claude Is Your Best Career Bet

> **STATUS: Move this file from `Inbox/AI-Model-War-Career-Strategy.md`**

## Action Required

1. Move `Inbox/AI-Model-War-Career-Strategy.md` → `data/blog/ai/ai-model-war-career-strategy.mdx`
2. Update frontmatter `date` to today's date
3. Update `picsumId` to a relevant image ID
4. Remove `[MOVE FROM INBOX]` from title
5. Add internal links to the Claude Code Agent Teams article and the top multi-model post

## Why This Article Fits Your GSC Strategy

This article aligns with your proven high-CTR queries:
- `claude code` — dominant theme
- `claude code multiple models` — mentioned in ecosystem section
- `claude code other models` — covered via Claude Code Router discussion

## Cross-Link Opportunities
- Link to `claude-code-agent-teams-complete-guide` (Agent Teams ecosystem section)
- Link to `claude-code-router-multi-model-guide` (mentioned as solution)
- Link to `extend-claude-code-multiple-models-complete-guide` (your top post!)

## Meta Description Suggestion
> "The AI model war is like the JavaScript framework wars. Here's how to pick the right model for your career — and why Claude Code is the React of 2026."

---

# Article 08: How I Built an AI-Powered Remotion Video Generator

## Meta

- **Target Length:** 2000-3000 words
- **Target Audience:** Developers, content creators, AI enthusiasts
- **Primary Keyword:** "remotion video generator"
- **Secondary Keywords:** "ai video creation", "automated video production", "remotion react"
- **Publish Date:** TBD

## Hook (Opening Paragraph)

I've always wanted to create YouTube videos, but the editing process was always a bottleneck. Recording, editing, adding animations—it all takes hours. So I asked myself: **What if I could generate videos from my notes automatically?**

In this post, I'll show you how I built a complete video generation system that turns markdown notes into animated videos in under 30 minutes.

## Outline

### 1. The Problem: Why Video Creation Takes So Long
- Traditional workflow breakdown (6-8 hours per video)
- The scaling problem for consistent publishing
- My frustration with manual editing

### 2. The Solution: Programmatic Video Generation
- Why Remotion? (React-based, programmatic)
- The architecture: Notes → AI Skill → Script → Video
- Key insight: Config-based animations, not keyframes

### 3. Architecture Deep Dive
```
remotion-videos/
├── .pi/skills/video-generator/    # AI skill for generation
├── src/
│   ├── components/primitives/      # Reusable animation components
│   ├── videos/                    # Generated video compositions
│   └── Root.tsx                   # Video registry
└── public/expressions/            # 44 emotion-based images
```

### 4. The Video Generator Skill
- How it reads markdown notes
- Extracts key points and structure
- Generates timed script with image selections
- Creates complete Remotion composition code

### 5. Expression Image System
- 44 curated images organized by emotion
- Automatic selection based on content tone
- Layout direction matching (_left/_right suffixes)

| Emotion | Use Case | Example Images |
|---------|----------|----------------|
| Thinking | Contemplative content | male-thinking-meme_left.png |
| Shocked | Revelations, big numbers | male-shocked-eyes-wide.png |
| Happy | Wins, celebrations | male-proud-fist-pump-meme.png |
| Confused | Problems, challenges | male-confused-meme_left.png |
| Sarcastic | Hot takes, contrarian | male-sarcastic-clapping.png |

### 6. Animation System
- Config-based approach (no manual keyframing)
- Entrance/Exit/Loop patterns
- Pre-built animation presets

### 7. Text Rules That Work
- Maximum 1-3 words per line
- Large fonts (120px headlines, 100px quotes)
- Color coding:
  - White (#ffffff) - primary text
  - Teal (#91EAE4) - accents
  - Orange (#F7B267) - highlights

### 8. Results: Before vs After

| Metric | Before | After |
|--------|--------|-------|
| Time per video | 6-8 hours | 30 mins |
| Script writing | Manual | AI-generated |
| Animation | Manual keyframes | Config-based |
| Consistency | Variable | Uniform style |

### 9. Getting Started

```bash
# Clone the repo
git clone https://github.com/rakeshtembhurne/remotion-videos

# Install dependencies
bun install

# Start preview
bun run remotion preview

# Generate a video from notes
/skill:video-generator path/to/notes.md
```

## Publishing Checklist

- [ ] Add architecture diagram
- [ ] Add Remotion preview screenshot
- [ ] Add expression image grid
- [ ] Add sample video frame
- [ ] Proofread and edit
- [ ] Add meta description

## Related
- [[blog-content-plan-2026]] · [[micro-startup-playbook]] · [[claude-code]] · [[vibe-coding]]

## Status

- [ ] Create featured image for social
