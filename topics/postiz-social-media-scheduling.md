---
created: 2026-05-19
updated: 2026-05-19
tags: #research #social-media #scheduling #postiz #open-source #saas
source: postiz.com pricing page, product hunt, Discord reviews
---

# Postiz — Social Media Scheduling Tool ($43K MRR)

## What Is Postiz?

Open-source, self-hostable social media scheduling tool with built-in AI content generation. Hit **$43K MRR** (verified indie hacker revenue). Built by [@wickedguro](https://x.com/wickedguro).

**Website:** https://postiz.com
**Dev Docs:** https://docs.postiz.com
**Self-hostable:** Yes (Docker/Podman)
**License:** AGPL-3.0 (fully open source)

---

## Why Postiz Is Key to Our Stack

Postiz is NOT a competitor to Brandsome.app — it's the **scheduling layer** in our social media pipeline:

```
Brandsome.app (content creation)
       ↓ brand-consistent images/videos
Postiz (scheduling + posting)
       ↓
Facebook, Instagram, Twitter/X, YouTube, etc.
```

Postiz can integrate with our Hermes agent via:
- **MCP server** — Hermes can drive Postiz via Claude Code / Codex
- **Public API** — OAuth2, SDK for custom integrations
- **CLI tool** — terminal-based scheduling

---

## Postiz Pricing (May 2026)

| Plan | Price | Channels | Posts/mo | AI Images | AI Videos |
|------|-------|----------|----------|-----------|----------|
| Standard | $29/mo | 5 | 400 | Yes | 3/mo |
| Team | $39/mo | 10 | Unlimited | Yes | 10/mo |
| Pro | $49/mo | 30 | Unlimited | Yes | 30/mo |
| Ultimate | $99/mo | 100 | Unlimited | Yes | 60/mo |

**Self-hosted:** Available (no monthly fees, one-time setup)

### Key Features (All Plans)
- AI Content Assistant (built-in)
- AI Image generation (Canva-like editor + AI)
- AI Video generation (built-in)
- Cross-posting to 30+ social networks
- Auto-post, auto-like, auto-comment
- Team collaboration
- RSS auto-post
- Webhooks + API
- Calendar views
- Analytics

---

## AI Integrations (Built-in)

Postiz already has AI image and video generation BUILT IN:
- AI Picture Editor (Canva-like, with AI)
- AI Image generation
- AI Video generation
- AI Copilot for content drafting

This means Brandsome.app's value is in **branded content creation** — Postiz handles the generation AND scheduling. We don't need to duplicate effort.

---

## Agentic Scheduling

Postiz explicitly markets "agentic scheduling" — use AI agents to drive Postiz:

| Integration | How It Works |
|-------------|--------------|
| **ChatGPT** | Generate and refine posts via ChatGPT |
| **OpenClaw** | Automate via Telegram workflows |
| **Claude Code** | Create and schedule posts from terminal |
| **n8n/Make.com** | Full workflow automation |
| **Zapier** | Connect to 5,000+ apps |
| **Public API** | Build custom posting apps |

**This is exactly what Hermes does.** We can integrate Hermes with Postiz to auto-generate + auto-schedule content for Trigyaa and KhabarOnline.

---

## Self-Hosting Economics

Postiz is AGPL-3.0 — self-host it for free:

```bash
# One-time setup cost (our servers)
# 2x legacy servers: already paid for
# Postiz Docker: free

# vs. Postiz Cloud
$29-99/month per workspace
```

**For our stack:** Self-host Postiz on existing infrastructure. Free forever.

---

## TrustMRR Data

Postiz is one of the few **open-source** SaaS tools hitting serious MRR:
- **$43K MRR** — verified
- **100% public** — AGPL-3.0 repo
- **Growing fast** — founder active on Twitter/X

**Key insight:** Open-source + good marketing = serious revenue. Postiz proves that indie hackers will pay for convenience (hosting, support, updates) even when the code is free.

---

## How We Use Postiz

### For Trigyaa.com + KhabarOnline.com (Priority #1)
1. Brandsome.app generates branded content (images/videos)
2. Hermes agent calls Postiz API to draft + schedule posts
3. Human reviews via Postiz dashboard
4. Auto-post or manual publish

### For Brandsome.app Integration
- Postiz IS the scheduler for Brandsome.app
- No need to build scheduling — just integrate via API
- Brandsome.app focuses purely on AI content creation
- Upsell: "Connect to Postiz" as a feature

### For JciAlumni.org
- 40K members — massive content opportunity
- Postiz auto-posting to Facebook groups, Instagram, Twitter
- Hermes generates content based on new member activity

---

## Competitive Positioning

| Tool | Postiz | Brandsome.app |
|------|--------|---------------|
| Focus | Scheduling + posting | Content creation |
| AI Images | Yes (built-in) | Yes (brand-focused) |
| AI Videos | Yes (built-in) | Yes (brand-focused) |
| Brand kit | No | Yes (core feature) |
| Self-hostable | Yes | TBD |
| API | Yes | Yes |
| Price | $29-99/mo | $TBD |

**Strategy:** Position Brandsome.app as "Postiz + brand consistency layer." Users who want brand-consistent content use Brandsome.app → Postiz for scheduling.

---

## Related

- [[brandsome-dev-app]] — Brandsome.app architecture
- [[flux-ai-social-media-automation]] — FLUX AI for social media
- [[ai-video-creation]] — AI video tools comparison
- [[research_program]] — Priority #1: Social Media AI Content System
- [[micro-startup-playbook]] — Build with open-source tools
