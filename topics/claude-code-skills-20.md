---
created: 2026-05-19
tags: [claude-code, skills, ai, workflow]
source: "YouTube transcript — Vaibhav Sisinty"
---

# Claude Skills 2.0 — Complete Mastery

## Key Insights

- **Skills 2.0 solves two core 1.0 problems**: (1) You couldn't tell if your skill was actually working (black box), and (2) Claude might never invoke your skill at all despite it being relevant. Three new superpowers fix these: EVALs, Benchmark, and Triggers.

- **Two types of skills exist — capability uplift vs. encoded reference**: Capability uplift patches a genuine weakness in the model (e.g., generic outputs). Encoded reference teaches Claude your specific workflow/preferences when the model is already decent at the task (e.g., meeting notes with your specific format). Know which type you're building.

- **EVALs tests your skill automatically** — Skills 2.0 runs your skill through realistic test scenarios and reports where it works vs. breaks. This gives you data instead of guesswork on skill quality.

- **Benchmark answers: "Is my skill still needed?"** — When Claude gets upgraded, your old skill might be redundant. Benchmark tests whether the skill still adds value after model updates — or if it's now getting in the way.

- **Triggers diagnose activation failures** — If you say "Build a PPT" and your PPT skill never fires, Triggers reveal whether the skill description is causing the miss, letting you fix the activation description.

## Summary

Claude Skills 2.0 turns skills from a black box into a measurable, optimizable system. Build skills by encoding your actual rules/preferences (not vague instructions), then use EVALs/Benchmark/Triggers to verify they're firing and adding real value. Skills are instructional manuals in plain English that teach Claude your specific way of working.
