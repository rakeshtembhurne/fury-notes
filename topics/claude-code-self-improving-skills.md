---
created: 2026-05-19
tags: [claude-code, skills, self-improvement, karpathy, agents]
source: "YouTube transcript — Simon Scrapes"
---

# Self-Improving Claude Code Skills (Karpathy Autoresearch Loop)

## Key Insights

- **Skills can self-improve overnight using the Karpathy Autoresearch pattern** — The loop: read skill.md → make an experimental change → run evaluation against evals.json → check if pass rate improved → keep or revert → repeat. Run it all night and wake up to a better skill.

- **Two layers of self-improvement: activation and output quality** — Layer 1 (Activation): Skills 2.0 has built-in description optimization. Vague descriptions cause as low as 20% activation. The system tests multiple description variants and picks the best. Layer 2 (Output Quality): The Karpathy loop runs the skill, checks binary assertions in evals.json, and autonomously refines the skill.md.

- **Binary assertions are critical** — Each assertion in evals.json must be true/false (pass/fail). Subjective criteria can't be automated. Ask Claude Code to generate the evals.json automatically based on your skill.md requirements.

- **The "Never Stop" principle** — Once the experiment loop starts, don't pause to ask if it should continue. The human might be asleep. Run multiple agents running multiple tests simultaneously. Let it run until manually stopped or no gains remain.

- **Skills improved via this loop are structurally more sound** — Multi-run testing across many variations produces skills that are more robust than manually created ones. Set up once, run indefinitely.

## Summary

The Karpathy Autoresearch loop applied to Claude Code Skills: create an `eval/evals.json` with binary pass/fail assertions, then let the skill run overnight with autonomous experimentation. Layer 1 (activation) is built into Skills 2.0. Layer 2 (output quality) uses the Karpathy loop. Multiple agents can run multiple tests in parallel. Binary assertions only — subjective criteria cannot be automated.
