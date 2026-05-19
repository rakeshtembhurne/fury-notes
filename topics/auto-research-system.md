---
created: 2026-05-19
tags: #system #research #automation
---

# Auto-Research System (Our Implementation)

## Architecture

```
research_program.md (human sets direction)
        ↓
  Hermes Agent (cron-driven)
        ↓
  1. Read vault notes (context)
  2. Web/Twitter research
  3. Write new notes / update existing
  4. Link related notes (wikilinks)
  5. Report digest → Telegram
```

## Vault Location

`~/ObsidianVault/` — Git-initialized for version control

## Folder Structure

```
ObsidianVault/
├── research_program.md   ← Human edits this to set agenda
├── daily/                ← Research logs by date
├── topics/               ← Synthesized findings
├── inbox/                ← Raw captures
├── outbox/               ← Processed/archived
└── README.md
```

## Agent Loop (on cron)

1. **Read** `research_program.md` for current goals
2. **Search** vault for related existing notes
3. **Research** via web/Twitter (aligns with Twitter digest)
4. **Write** findings to `topics/` or `inbox/`
5. **Link** new notes to existing ones via [[wikilinks]]
6. **Log** to `daily/[date].md`
7. **Digest** new notes → Telegram

## research_program.md Format

```markdown
# Research Program — [Focus]

## Current Goals
1. Investigate [topic]
2. Track [development]
3. Find [opportunities]

## Key Questions
- What are latest developments?
- Who are key players?
- What gaps exist?

## Constraints
- Prefer simple, practical insights
- Cite sources
- Log everything

## Never stop to ask — just execute
```

## Obsidian AI Plugins

For enhanced AI capabilities:
- **obsidian-local-llm-helper** — Chat with notes via Ollama (local)
- **obsidian-textgenerator-plugin** — Generate text via API
- **obsidian-ai-tagger-universe** — Auto-tag notes

## Git Integration

- Vault is git-initialized
- User will authenticate `gh` later for GitHub push
- Enables: version history, backup, sharing

## Related
- [[autoresearch-karpathy]]
- [[harness-engineering-ai-agents]]
