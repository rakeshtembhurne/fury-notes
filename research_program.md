# Research Program — AI-Powered Micro-Startups

## The Vision

Build AI systems that run micro-startups **fully or mostly autonomously**. AI handles the entire lifecycle:
- Research trends
- Social media management
- Content creation
- Feature strategy (data-driven learnings)
- Code management (safe, secure)
- Taking products to market
- Payments & billing
- Customer support & issue resolution

Human in the loop — but AI does the work.

---

## Human-AI Collaboration System

**Obsidian vault is our shared communication channel.** Both human and AI write notes here to communicate.

### How It Works

| Person | Writes To | Purpose |
|--------|-----------|---------|
| Human | `inbox/` | Quick captures, ideas, observations, feedback |
| Human | `reviews/` | Review AI's work, approve/reject ideas |
| AI | `topics/` | Research findings, synthesized notes |
| AI | `daily/` | Research logs, what AI worked on |
| AI | `inbox/` | Flags things for human attention |

### Communication Protocol

**Human → AI (via inbox):**
- Add a note in `inbox/` with a `#[priority]` tag
- Use `#[action]`, `#[idea]`, `#[feedback]`, `#[question]` tags
- AI reads inbox on every run and incorporates into research

**AI → Human (via inbox + Telegram):**
- AI creates notes in `inbox/` flagged for human review
- AI delivers summaries to Telegram via cron
- Human reads AI notes directly in Obsidian

### Human Writing Notes

When you (human) add notes:

```markdown
---
created: 2026-05-19
tags: #inbox #idea #priority
---

# [Brief Title]

## Capture
What you want to communicate.

## Context
Why this matters right now.

## Related
[[existing-note]] [[another-note]]
```

**Tags for AI attention:**
- `#[action]` — AI should do something with this
- `#[idea]` — New idea to research
- `#[feedback]` — Feedback on AI's previous work
- `#[question]` — Question for AI to answer
- `#[approved]` — Human approved AI's suggestion
- `#[rejected]` — Human rejected AI's suggestion

### AI Reading Human Notes

On every research run, AI:
1. Checks `inbox/` for new human notes
2. Reads `reviews/` for feedback on previous work
3. Incorporates human input into next research cycle
4. Acknowledges and acts on human notes

---

## Current Research Focus

### 1. Learn from What's Working
- How are people using AI systems to run businesses? (Twitter, YouTube)
- What AI tools/workflows are indie hackers and micro-startup founders sharing?
- What are the real-world patterns that work?

### 2. Build Better Systems
- AI agent frameworks for business operations
- Social media AI (posting, scheduling, engagement)
- Customer support AI (issue triage, resolution)
- Payment/billing AI integration
- Content generation at scale
- Data-driven feature decisions

### 3. Micro-Startup Specific
- Marketing strategy for AI products
- How to go from zero to first customer
- Pricing, payments, invoicing (fully automated)
- Building in public — sharing progress
- Community building (Twitter, Discord, etc.)

### 4. Technical Architecture
- Agent orchestration for business tasks
- Safety & security in AI code execution
- Self-hosting vs third-party tradeoffs
- Cost-effective AI infrastructure

---

## Key Questions

- What AI systems are people actually using to run businesses in 2026?
- How do successful indie hackers use AI vs traditional approaches?
- What's the best way to handle customer support with AI?
- How to automate payments and billing end-to-end?
- What does "human in the loop" actually look like in practice?
- How to research trends and validate ideas quickly?

---

## Vault Structure

```
ObsidianVault/
├── research_program.md   ← This file (goals + collaboration protocol)
├── daily/                ← Research logs by date
│   └── YYYY-MM-DD.md     ← AI logs what it did today
├── topics/               ← Synthesized research findings (AI)
│   └── [topic].md
├── inbox/                ← Shared inbox (human + AI)
│   └── YYYY-MM-DD-[source].md
├── reviews/              ← Human reviews AI's work
│   └── YYYY-MM-DD-[item].md
├── outbox/               ← Archived/processed notes
├── backlog/              ← Ideas queued for research
└── README.md
```

---

## Sources to Follow

- Twitter: Indie hackers, AI tool founders, micro-startup builders
- YouTube: Case studies, building in public, AI automation walkthroughs
- Blogs: Micro-startup stories, AI business frameworks
- GitHub: Open-source AI business tools

---

## Constraints

- Prefer **simple, practical** over complex/theoretical
- Cite sources (tweets, videos, papers, blogs)
- Always include **actionable takeaways**
- Log every research session to `daily/`
- Use wikilinks: [[like this]]
- **Read inbox/ on every run** — human may have left notes

---

## Never Stop To Ask
Execute autonomously. Research, synthesize, link, build.
