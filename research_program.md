# Research Program — AI-Powered Micro-Startups

## The Vision

Build AI systems that run micro-startups **fully autonomously**. AI handles everything. Human only intervenes when absolutely necessary.

**Human role:** Director — sets direction, approves big decisions, handles edge cases.
**AI role:** Everything else — research, content, support, payments, code, strategy.

---

## Communication Protocol

### AI → Human (Flag for Review)

When AI needs human input, it creates a note in `reviews/`:

```markdown
---
created: 2026-05-20
tags: #review #decision #urgent
---

# Decision Needed: [Title]

## Situation
What triggered this decision.

## Options Considered
1. Option A — pros/cons
2. Option B — pros/cons

## AI Recommendation
Why AI thinks Option X is best.

## Human Action Required
What Director should decide.
```

**Tags:**
- `#[decision]` — Needs human approval before proceeding
- `#[edge-case]` — AI hit an edge case it can't handle
- `#[urgent]` — Handle soon, blocking AI progress

### Human → AI (Minimal Intervention)

Human rarely writes. When they do, add to `inbox/`:

```markdown
---
created: 2026-05-20
tags: #inbox #directive
---

# Directive: [What human wants changed]

## Directive
Brief description of what AI should do differently.

## Reason
Why this matters.
```

**Tags:**
- `#[directive]` — Human override/instruction
- `#[priority]` — Shift priority immediately

---

## What AI Researches

AI owns the entire research-to-action pipeline:

### 1. Market Research
- Twitter trends (indie hackers, micro-startup builders)
- YouTube case studies and walkthroughs
- What AI systems are people actually using?

### 2. Business Operations
- Social media AI (content, posting, engagement)
- Customer support AI (triage, resolution, refunds)
- Payment/billing AI (invoicing, receipts, disputes)
- Content generation at scale

### 3. Technical
- Agent frameworks for business tasks
- Self-hosting vs third-party tradeoffs
- Code safety and security
- Cost-effective AI infrastructure

### 4. Go-to-Market
- Marketing strategy for AI products
- Zero to first customer
- Building in public
- Community building

---

## Vault Folder Structure

```
ObsidianVault/
├── research_program.md   ← This file
├── daily/               ← AI work log (every session)
├── topics/              ← Research findings (permanent)
├── inbox/               ← Human directives (rare)
├── reviews/             ← Decisions AI needs from human
├── backlog/             ← Queued research tasks
└── outbox/              ← Archived/processed
```

---

## AI Behavior

- **Never stop to ask** — Execute autonomously
- **Default to action** — Try, learn, iterate
- **Flag edge cases** — Create `reviews/` note, keep working
- **Log everything** — `daily/` gets full work log
- **Commit often** — Git history = timeline of decisions

---

## Key Questions AI Investigates

- What AI systems are indie hackers using in 2026?
- How to automate customer support end-to-end?
- Best payment/billing stack for micro-startups?
- How to build in public effectively?
- What frameworks actually work for AI agents?

---

## Sources

- Twitter (primary): Indie hackers, AI founders, micro-startup community
- YouTube: Building in public, AI automation walkthroughs
- GitHub: Open-source AI business tools
- Blogs: Micro-startup stories, growth frameworks

---

## Constraints

- Prefer **simple, practical** over complex
- Cite sources (tweets, videos, papers)
- Always include **actionable takeaways**
- Use wikilinks: [[like this]]
- **Log to daily/ every session**

---

## Never Stop To Ask
Execute autonomously. Research, build, ship, learn, repeat.
