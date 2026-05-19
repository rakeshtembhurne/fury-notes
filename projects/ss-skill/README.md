# /ss — Screenshot Skill for AI Coding Tools

**Status:** Building — Validation tweet pending

## What is /ss?

A skill that reads screenshots from a configurable folder and lets you ask questions about them. Visual mode for vibe coding.

**Use case:** You're coding with Codex/Claude Code and want to show it a screenshot of what you're seeing.

## How It Works

```
/ss 3          → Shows last 3 screenshots with paths
/ss --latest   → Shows the most recent screenshot
/ss --ask "..." → Ask a question about the screenshots
```

## Tech Stack

- Python 3
- Pillow (image handling)
- Watchdog (file watching, optional)
- Claude Code / Codex compatible

## Files

- `ss.py` — Main skill script
- `skill.md` — Instructions for Claude Code
- `config.py` — Screenshot folder configuration

## Pricing

- Free tier: 50 screenshots/month
- Pro ($9/mo): Unlimited, Ask mode

## To Do

- [ ] Post validation tweet
- [ ] Build v0.001 in Codex
- [ ] Test with real screenshots
- [ ] Ship to GitHub
- [ ] List on TrustMRR when MRR > $100
