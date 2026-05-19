---
created: 2026-05-19
tags: #inbox #system
author: Fury (AI)
updated: 2026-05-19
---

# Collaboration Protocol (Simplified)

**Human:** Director — approves big decisions, handles edge cases.
**AI:** Does all the work. Research, content, support, code, strategy.

---

## Human Intervention Points (Minimal)

Human only steps in when:

1. **Big decision needed** — AI creates `reviews/` note, human decides
2. **Edge case** — AI can't handle, flags for human
3. **Directive** — Human wants to override AI direction

---

## AI → Human (Flag for Review)

Create note in `reviews/`:

```markdown
tags: #review #decision
```

- `#[decision]` — Needs approval before proceeding
- `#[edge-case]` — AI hit something it can't handle
- `#[urgent]` — Handle soon

---

## Human → AI (Rare Directive)

Add to `inbox/`:

```markdown
tags: #inbox #directive
```

- `#[directive]` — Human override
- `#[priority]` — Shift priority immediately

---

## Daily Flow

1. AI reads `research_program.md`
2. AI checks `inbox/` for any directives
3. AI executes research/research loop
4. AI logs to `daily/`
5. AI creates `reviews/` if human needed
6. AI commits to git
7. AI delivers digest to Telegram

---

## Tags Reference

| Tag | Direction | Meaning |
|-----|-----------|---------|
| `#[decision]` | AI→Human | Needs approval |
| `#[edge-case]` | AI→Human | Can't handle |
| `#[urgent]` | AI→Human | Handle soon |
| `#[directive]` | Human→AI | Override instruction |
| `#[priority]` | Human→AI | Shift priority |
