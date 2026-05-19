---
created: 2026-05-19
tags: #research #ai-agents #autonomous-research
---

# Karpathy's AutoResearch (81.8k stars)

## Overview

GitHub: https://github.com/karpathy/autoresearch

AI agents running research on single-GPU nanochat training automatically.

## How It Works

1. **Human programs goals** via `program.md` (Markdown = instructions)
2. **Agent modifies code** in `train.py` (GPT model code)
3. **Fixed 5-min experiments** - train, evaluate, iterate
4. **Metric**: val_bpb (validation bits per byte) - lower is better
5. **Agent creates branches**, auto-commits improvements, discards failures
6. **Human wakes up** to log of experiments + better model

## Key Files

- `program.md` — Instructions humans edit to set research direction
- `train.py` — The GPT model code agent modifies
- `prepare.py` — Fixed constants, data prep (never modified)

## Core Loop

```
Tune → Run → Evaluate → Decide (keep/discard) → Repeat
```

## Key Instruction: "NEVER STOP"

The agent is explicitly told:
- Don't ask for permission
- Don't pause to ask the human
- Work indefinitely until manually stopped
- If out of ideas → "think harder"

## Key Insight

> You don't write the implementation code. You program the goals/context via Markdown.

## Connection to Our System

We're building a similar approach for note-taking:
- `research_program.md` = goals/context
- Hermes = the agent
- Obsidian vault = knowledge base
- Cron = autonomous execution loop

## Related
- [[harness-engineering-ai-agents]]
- [[auto-research-system]]
