---
created: 2026-05-19
tags: [topics, ai, coding, agents, claude-code, skills]
source: YouTube transcripts
---

# Claude Code Skills 2.0

## What Are Skills?

A skill is NOT:
- Not code
- Not an app
- Not a typical prompt

A skill IS:
- An instructional manual written in plain English
- Teaches Claude how to do something YOUR way
- Like giving a carpenter a detailed specification for building a chair

---

## The 7 Levels of Skills

### Level 1: Install & Use Marketplace Skills

**Starting point** - download skills from marketplace.

**What to look for:**
- Proper trigger descriptions
- Clear outcome statements
- Structured instructions

> [!warning]
> Many marketplace skills only activate 1 in 5 times. If a skill doesn't have clear triggers, it's nearly useless.

**Three-part framework for writing triggers:**
1. **What triggers it** - keywords, events, situations
2. **What does NOT trigger it** - exclusions
3. **Outcome produced** - what the skill delivers

---

### Level 2: Refactor & Structure Skills

**The Problem:**
- More information ≠ better output
- Skills with 1,000+ lines cause context explosions
- When multiple skills activate together, context can hit 5,000-7,000 lines

**The Solution - 3-Tier Structure:**

| Tier | Content | When Loaded |
|------|---------|-------------|
| **Tier 1** | YAML description | Always (max 15,000 chars) |
| **Tier 2** | skill.md (process steps) | Only when skill activates |
| **Tier 3** | Reference files, scripts | Only when needed for specific steps |

**Refactoring Process:**
1. Take your 1,000+ line skill.md
2. Ask: "What does Claude need to see immediately?"
3. Put that in skill.md
4. Move everything else to reference folders

> [!tip]
> Use Anthropic's built-in skill creator skill to help refactor existing skills.

---

### Level 3: Add Context & Personalization

Give skills your business context for personalized outputs.

**Foundation Context Files:**
- Voice profile
- Positioning/angles to target
- ICP (Ideal Customer Profile)
- Brand guidelines

> [!important]
> Once foundation files exist, every new skill immediately benefits from shared context.

---

### Level 4: Benchmark with Evals

Measure skill quality objectively using `evals.json`

**What are Evals:**
- Binary true/false assertions
- Validated automatically

**Example Assertions:**
- "Does the first line appear as standalone sentence?"
- "Does it contain at least one specific number or statistic?"
- "Is the total word count under 300?"
- "Does it use the reference file?"

**Workflow:**
1. Create eval folder with `evals.json`
2. Run skill against multiple test prompts
3. Get pass rate scores
4. Compare benchmark scores before/after changes

> [!tip]
> Ask Claude Code to auto-generate `evals.json` based on your skill.md requirements.

---

### Level 5: Build Learnings Files

Create feedback loop where skills learn from every interaction.

**What Gets Logged:**
- "Did the article answer the search query in the first 100 words?"
- "Did it include structured data patterns from reference file?"
- "Did it follow the voice profile?"

> [!warning]
> Keep learnings file under control. Prune obvious stuff weekly or it becomes its own context problem.

---

### Level 6: Self-Improving Skills

Skills that accumulate knowledge over time and get better the more you use them.

**The Self-Improvement Loop:**
1. Run skill → produces output
2. Checks against learnings file
3. Logs if it missed something
4. Uses evals to validate improvements
5. Benchmark scores improve without manual testing

---

### Level 7: Connected AI Workforce

Everything connects. Skills work together as a complete system.

**Example: Copywriting Skill in Aentic OS**
1. Pulls context from voice profile
2. Gets angles to target from positioning
3. Uses full ICP to tailor copy
4. Connects with OTHER skills for workflows
5. Before saving, passes through "humanizer" tool

**Result:** Not separate tools anymore, but a complete AI workforce.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                    YOUR BUSINESS                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │
│  │Voice Profile│  │Positioning  │  │    ICP      │   │
│  └─────────────┘  └─────────────┘  └─────────────┘   │
│                    (Shared Context)                      │
├─────────────────────────────────────────────────────────┤
│                   SKILL ECOSYSTEM                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌───────┐│
│  │  SEO     │  │ Copywrite│  │  Research│  │Social ││
│  │  Skill   │  │  Skill   │  │  Skill   │  │ Media ││
│  └──────────┘  └──────────┘  └──────────┘  └───────┘│
├─────────────────────────────────────────────────────────┤
│              AUTONOMOUS IMPROVEMENT                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐             │
│  │ Evals    │→ │ Learnings│→ │ Benchmark│             │
│  │(.json)   │  │  File    │  │ Scores   │             │
│  └──────────┘  └──────────┘  └──────────┘             │
└─────────────────────────────────────────────────────────┘
```

---

## Key Principles

| Principle | Description |
|-----------|-------------|
| **Lean is Better** | 500 lines well-structured beats 1,000 lines of bloat |
| **Context Loading** | Only load what's needed when it's needed |
| **Binary Metrics** | True/false assertions enable automation |
| **Never Stop** | Let autonomous loops run until manually stopped |
| **Prune Regularly** | Keep learnings files structured and lean |
| **Foundation First** | Build context files before complex skills |

---

## Skills 2.0 Improvements

1. **Eval Tracking** - Know if your skill is actually helping
2. **Better Trigger Detection** - Skills actually activate when needed
3. **Self-Improvement** - Model updates don't break your workflow
4. **Skill Creator** - Built-in tool to help write better skills

---

## Quotes

> "More information equals a better output - and that's exactly what level two is about solving."

> "You don't need to be technical to build this. Everything can be done by a business owner who knows their own processes."

> "At level seven, your skills aren't separate tools anymore. They're a complete system."

---

## Related Notes

- [[claude-code]] - General Claude Code guide
- [[claude-code-agent-teams]] - Agent Teams
- [[ai-coding-workflow]] - Workflow frameworks
