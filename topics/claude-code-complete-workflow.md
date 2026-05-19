---
created: 2026-05-19
tags: [claude-code, workflow, testing, memory]
source: "YouTube transcript — Yifan - Beyond the Hype"
---

# The Complete Claude Code Workflow

## Key Insights

- **Write tests and give Claude Code the ability to run them** — This creates an automatic feedback loop. When Claude implements features, it runs tests to verify correctness before returning to you. Without tests, you're stuck in a manual copy-paste error-debug cycle. Even just adding "test this feature before returning" in CLAUDE.md makes Claude try to write ad-hoc tests or temporary scripts.

- **Use `/init` to generate CLAUDE.md intelligently** — The init command reads your codebase, project conventions, stack, and folder structure to auto-generate a CLAUDE.md file. Re-run `/init` as you iterate to keep it updated. Keep CLAUDE.md high-level (pointers to where info lives), not exhaustive — Claude Code is good at discovering information on the run.

- **Use `/clear` to reset context at the end of every task** — Claude Code's quality degrades as context fills up (context rot starts around 50-60% of context window). Use `/clear` to start fresh after each task. `/compact` auto-summarizes but don't rely on it picking the right things — `/clear` is more reliable.

- **Use `#` to add memories ad-hoc** — Type `#` anywhere in the prompt input to save a rule or memory to CLAUDE.md. Claude semanticall inserts it in the right places automatically.

- **Version control workflow: `git add` → review → commit** — After Claude completes a working solution, `git add` the changed files. Claude can auto-generate commit messages by reviewing changes + git history. Add pre-commit hooks (Husky) for compile checks, lints, and quick unit tests — this enforces that the repo never goes broken.

- **Use `@agent` to invoke specialized sub-agents** — Bash agent for terminal work, explore agent for fast codebase scanning, general purpose agent for complex multi-step tasks. Keep the main agent for orchestration.

## Summary

Key workflow: use tests for automated feedback, keep CLAUDE.md high-level, reset context frequently, commit regularly with pre-commit hooks, and invoke specialized sub-agents rather than overloading a single agent. Claude Code's built-in tools (init, clear, compact, hooks, custom commands) are designed to work together — use them all.
