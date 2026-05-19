---
created: 2026-04-08
tags: [topic, ai, tools, llm, coding, twitter-favorites]
source: "Twitter favorites (1023 tweets)"
---

# AI & Machine Learning — Key Learnings

## AI Coding Tools
- **Claude Code** — Anthropic's CLI coding agent; skills, hooks, MCP, subagents, multi-session
- **Cursor** — AI code editor (VS Code fork), inline completions + chat
- **Codex** — OpenAI's CLI coding agent; can run inside Claude Code via codex-plugin-cc
- **Windsurf** — AI IDE from Codeium with deep codebase awareness
- **Cline** — Open-source autonomous coding agent for VS Code
- **Aider** — Terminal-based AI pair programming with local repos
- **Devin** — Autonomous AI software engineer by Cognition Labs
- **OpenCode** — Open-source CLI with multi-model support

## Vibe Coding / App Builders
- **Lovable** — AI app builder from prompts (full-stack)
- **Bolt.new** — StackBlitz AI full-stack builder in browser
- **Replit** — Browser IDE with AI agent
- **v0** — Vercel's AI UI generator (React from prompts)

## LLM Providers & Models
| Provider | Models |
|----------|--------|
| Anthropic | Claude, Opus 4.6 |
| OpenAI | ChatGPT, GPT-5 |
| Google | Gemini, Gemma 4 (free open-weight) |
| Meta | Llama (open-weight) |
| Alibaba | Qwen3-coder, Qwen3-TTS |
| DeepSeek | Strong reasoning, free research alternative |
| Groq | Ultra-fast inference hardware |
| Ollama | Run open-source LLMs locally (single command) |
| OpenRouter | Unified API for multiple providers |
| Together AI | Cloud for open-source models |

## AI Agents & Automation
- **OpenClaw** — 340K+ GitHub stars; trading bots, CRM, automations
- **Hermes** — Nous Research agentic harness; runs in Telegram, social media automation
- **n8n** — Open-source workflow automation with AI agent nodes
- **CrewAI** — Multi-agent AI orchestration
- **MCP** — Anthropic's Model Context Protocol; connects AI to external tools
- **Paperclip** — AI agent monitoring; 1-click zero-human company setup
- **Onyx** — Self-hostable AI platform with agentic RAG, 50+ connectors
- **Composio** — 47,000-action integration database; prevents agents from hallucinating API knowledge

## Image & Video
| Category | Tools |
|----------|-------|
| Image | Midjourney, DALL-E, Stable Diffusion, Flux (open), Ideogram, Leonardo |
| Video | Runway, Sora, Kling, HeyGen (avatars) |
| Voice | ElevenLabs |
| Music | Suno |

## Dev Infrastructure (Rocky's Stack)
- **Supabase** — Postgres, auth, storage, message queues (pgmq)
- **Vercel** — Frontend deployment (free)
- **Cloudflare** — DNS, CDN, workers, edge
- **Stripe** — Payment processing
- **Clerk** — Auth (free for 10K users)
- **PostHog** — Session replay, product analytics

## Key Insights
- Claude Code is a 4-layer execution system, not a chatbot
- Context engineering > prompt engineering for complex projects
- "1-person company" era: CEO, CTO, CMO, QA — all AI agents, zero humans
- Running 10-15 Claude Code sessions simultaneously = power-user workflow
- SEO at scale: 10,000 pages in 48 hours using Claude Code + Firecrawl
- AI video production cost collapsed: full product ad for $0.69

## Claude Code Project Setup
1. `.claude/` folder in project root
2. `CLAUDE.md` = instruction manual for Claude
3. `rules/` = modular instructions
4. `skills/` = reusable capability modules
5. `hooks/` = pre/post-action automation
6. `commands/` = custom slash commands

## 10,000 SEO Pages in 48 Hours
1. Pick long-tail keyword pattern ("best CRM for dentists")
2. Scrape competitor data with Firecrawl
3. Build template, let AI generate unique content per page
4. Deploy 10K pages (target: 30 visitors each = 300K/month)
5. At 2% conversion = $60K/month from pages built once

## Best Free Alternatives
| Paid | Free |
|------|------|
| ChatGPT | DeepSeek |
| HeyGen | AirMore.ai |
| Midjourney | Flux / Leonardo |
| Fotor (watermark) | AirMore.ai |

## Resources
- github.com/HandsOnLLM/Hands-On-Large-Language-Models
- github.com/DataTalksClub/llm-zoomcamp (free)
- github.com/affaan-m/everything-claude-code (65K+ stars)
- github.com/obra/superpowers (61K+ stars)
- github.com/nousresearch/hermes-agent
- github.com/openclaw/openclaw (340K+ stars)
