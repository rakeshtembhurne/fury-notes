---
created: 2026-05-19
tags: #inbox #system #action
author: Fury (AI)
---

# AI Collaboration Protocol

## For Human (Rocky)

To communicate with me through the vault:

1. **Add note to `inbox/`** — I'll read it on every run
2. **Use tags:** `#[action]`, `#[idea]`, `#[feedback]`, `#[question]`
3. **I'll respond** by updating the note or creating a `reviews/` note
4. **Read my daily logs** in `daily/` to see what I worked on

## For AI (Fury)

On every research run:

```
1. READ inbox/ for new human notes
   ↓
2. PARSE tags: action, idea, feedback, question
   ↓
3. INCORPORATE into research plan
   ↓
4. EXECUTE research loop
   ↓
5. UPDATE/REPLY to human notes
   ↓
6. CREATE reviews/ for important findings
   ↓
7. LOG to daily/
   ↓
8. COMMIT to git
```

## Tags Reference

| Tag | Meaning | AI Response |
|-----|---------|-------------|
| `#[action]` | AI should act | Research, implement, or escalate |
| `#[idea]` | New idea to explore | Add to backlog, research |
| `#[feedback]` | Feedback on AI work | Incorporate into next iteration |
| `#[question]` | Question for AI | Research and answer |
| `#[approved]` | Human approved | Continue in this direction |
| `#[rejected]` | Human rejected | Stop, try different approach |
| `#[urgent]` | High priority | Handle before other tasks |

## Folder Purposes

- `inbox/` — Shared communication (human + AI)
- `daily/` — AI's work log (what researched, what created)
- `topics/` — Permanent research knowledge (AI-created)
- `reviews/` — AI findings needing human review
- `backlog/` — Ideas queued for future research
- `outbox/` — Processed/archived notes
