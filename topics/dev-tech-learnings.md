---
created: 2026-05-19
updated: 2026-05-19
tags: #dev #tech #stack #learnings
---

# Dev & Tech Stack Learnings

> Related: [[vibe-coding]] · [[claude-code]] · [[n8n-ai-agents-workflows]] · [[micro-startup-playbook]] · [[n8n-infrastructure-deployment]]

## Consolidated from notes/ folder — May 2026

---

## Near-Zero Cost Stack ($1/month)

| Service | Cost | Limit | Use Case |
|---------|------|-------|----------|
| Vercel | Free | Unlimited | Frontend hosting |
| Supabase | Free | 50K users | Database, auth |
| Cloudflare | Free | Unlimited | CDN, DNS, Workers |
| Stripe | 2.9% + $0.30 | Per transaction | Payments |
| Clerk | Free | 10K users | Auth |
| Resend | Free | 3K emails/mo | Transactional email |
| PostHog | Free | Unlimited | Analytics |
| GitHub | Free | Unlimited | Code hosting |

**Total fixed cost: ~$1/month**

---

## Tech Stack by Project Type

### E-commerce (Trigyaa model)
- Astro + Cloudflare Pages
- Cloudflare D1 (SQLite) + R2 (storage)
- Cloudflare KV (sessions)
- Tailwind CSS v4

### SaaS / Web App
- Next.js (App Router) + TypeScript
- Tailwind CSS v3
- PostgreSQL + Prisma ORM
- Bun runtime
- Better Auth
- React Email
- Docker/Podman (deployment)

### Blog / Personal Site
- Next.js (App Router) + TypeScript
- Tailwind CSS v3
- Contentlayer (MDX)
- Vercel (deployment)
- Umami + Google Analytics

### Self-hosted Tools (Server Infrastructure)
- ListMonk (email newsletter — already on Rocky server)
- Postiz (social scheduling — already on Rocky server, $100K MRR product)
- SearXNG (private search — already on Rocky server)
- OpenClaw (AI agent framework — already on Rocky server)
- Hermes (our AI agent — already on Rocky server)

---

## AI Coding Tools

### Vibe Coding Stack
- **Claude Code:** Primary AI coding tool
- **Codex:** Faster than Claude Code for some tasks
- **Pi-Starter:** AI coding assistant template (Rocky's open source project)
- **KiloCode:** Alternative
- **OpenCode:** Alternative

### AI Agent Frameworks
- OpenClaw (self-hosted, already running on server)
- LangChain, LlamaIndex (RAG/agent frameworks)
- n8n (workflow automation — use for integrations)

### Local AI
- Ollama (local LLM — Qwen3.5 runs well on local)
- MLX (Apple Silicon optimized)
- LM Studio (desktop local LLM)

---

## Key Development Notes

### AI Image Generation
- Replicate (API for Flux, Stable Diffusion)
- DALL-E (OpenAI)
- Hedra (video generation — nano banana pro)
- Kling (video generation)

### Payments
- Stripe (primary — international)
- Instamojo (India)
- Razorpay (India)
- PhonePe (India — check for lower MDR vs Razorpay/Cashfree)

### Database Options
- **SQLite (D1):** Good for small-medium apps, simple, cheap
- **PostgreSQL:** Full relational, use for complex queries
- **Supabase:** PostgreSQL + auth + realtime + edge functions
- **PlanetScale:** MySQL-compatible serverless

---

## Useful Tools for Builders

### Deployment
- Vercel, Railway, Render, Cloudflare Pages, Fly.io

### Monitoring
- PostHog (product analytics)
- Umami (simple analytics)
- Sentry (error tracking)

### CI/CD
- GitHub Actions (free)
- GitHub PR workflow

---

## Related
- [[vibe-coding]]
- [[micro-startup-playbook]]
