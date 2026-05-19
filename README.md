# Obsidian Research Vault

Autonomous AI research vault managed by Fury (Hermes Agent).

## Purpose
This vault is used for AI-powered note-taking and auto-research.
- Human sets direction via `research_program.md`
- Agent autonomously researches, synthesizes, and links notes

## Structure
- `research_program.md` — Research goals and constraints
- `daily/` — Research logs by date
- `topics/` — Synthesized findings by topic
- `inbox/` — Raw captures
- `outbox/` — Processed/archived

## How It Works
1. Edit `research_program.md` with your research goals
2. Hermes (the agent) runs on cron, reads the program
3. Agent researches, creates/updates notes, links ideas
4. Digest delivered to Telegram

## Powered By
- [Obsidian](https://obsidian.md/) — Markdown notes
- [Hermes Agent](https://github.com) — AI agent
- Local LLM (Ollama) or API for AI processing
