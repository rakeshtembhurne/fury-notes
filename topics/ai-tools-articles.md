# AI Tools Articles — Consolidated Notes

## Overview
This document consolidates key insights from 46 AI tools articles covering Claude Code mastery, AI agent workflows, spec-driven development, frontend AI tooling, and local AI deployment.

---

## Core Themes

### 1. Context Engineering & Claude Code Mastery

**Golden Rule:** LLMs are pure functions — output quality is strictly limited by the quality and structure of provided context.

**Six Levels of Claude Code Proficiency:**
| Level | Title | Core Skill |
|-------|-------|-----------|
| 1 | Prompt Engineer | Clear prompts & output evaluation |
| 2 | Planner | Plan mode & collaborative iteration |
| 3 | Context Engineer | Context window management (`/clear` > `/compact`) |
| 4 | Tool Selector | MCPs, frameworks, surgical selection |
| 5 | Skill Architect | Custom skills & prompt chaining |
| 6 | Orchestrator | Multi-session & agent teams (Git worktrees) |

**Key Insights:**
- Context rot hits at 50-60% window capacity (~100-120K tokens) — use `/clear` over `/compact` 99% of the time
- Claude.md files can REDUCE task success rates by 20%+ — less context is often more
- Capability does not equal performance — be surgical about MCP and tool selection
- Diminishing returns past 2-3 terminals when orchestrating agents
- Skills are just text prompts — keep them project-based, not global

---

### 2. Spec-Driven Development vs. Vibe Coding

**The Spectrum:**
| Approach | Speed | Quality | Best For |
|----------|-------|--------|----------|
| Vibe Coding | Very fast | Inconsistent | Prototyping, simple apps |
| Spec-Driven Dev | Very slow | Thorough but rigid | Production apps with clear requirements |
| **Hybrid (Recommended)** | Fast | Good + iterative | Most real-world projects |

**GitHub SpecKit 4-Step Process:**
1. `/specify` — Define WHAT and WHY (requirements spec)
2. `/plan` — Architecture & technical details
3. `/task` — Break into manageable units (can run in parallel)
4. Test-driven development at each step

**Key Insight:** The pendulum has swung too far toward over-specification. After 2 years of AI-assisted development, a hybrid approach works best: start light, iterate fast, add structure incrementally, always build frontend-first with dummy data.

---

### 3. AI Agent Workflows

**The BMAD Method:** Parallelizing AI coding using multiple agents for simultaneous task execution.

**Key Workflow Patterns:**
- **Pre-filtering:** Use cheap models to eliminate 70-90% of irrelevant inputs before expensive models (87% cost reduction)
- **Git Worktrees:** Separate desks for separate tasks — work in parallel, merge later
- **Sub-agents in Worktrees:** Automated orchestration across isolated working copies
- **Pre-routing:** When all inputs must be processed, route by difficulty to different model tiers

**Rowan Cheung's 7 AI Workflows (The Rundown AI):**
1. AI Avatar for short-form content (HeyGen + ElevenLabs)
2. Voice-dictated tweet writing with Claude
3. Claude as newsletter editor-in-chief
4. AI meeting scheduler agent (Lindy)
5. AI-powered partnership & lead validation
6. Custom GPT for new hire onboarding
7. Email inbox triage agent (Zapier)

---

### 4. Frontend AI Tools (ShadCN, Cursor, Next.js)

**ShadCN UI MCP Server — The Fix for Broken AI-Generated UI:**
- Provides component demos, block templates, and metadata
- **get_component_demo** tool eliminates implementation errors
- Three-phase workflow: Plan structure → Map components → Implement
- Prioritize blocks over individual components

**ShadCN CLI v4 New Features:**
- Presets system — compresses entire design system into a shareable string
- Support for Radix and Base UI as selectable component libraries
- Official Claude Code skill (`npx skills add shadcn/ui`)
- New `--dry-run`, `--diff`, `--view` flags for safety
- Framework expansion: React Router, Astro, Laravel

**Cursor + ShadCN Workflow:**
1. Set up ShadCN MCP server with GitHub token
2. Theme customization with TweakCN
3. Unicorn Studio for GPU shader backgrounds
4. GSAP for character stagger and scroll animations

---

### 5. MCP (Model Context Protocol) Integrations

**Claude Code Playwright MCP Integration:** Giving AI "eyes" for UI verification — can test features on the fly using your actual browser environment with all login states intact.

**MCP Chrome by Hangin (5,000+ stars):**
- Uses existing Chrome session (preserves cookies, login states)
- True cross-tab functionality
- 20+ tools including screenshots, network monitoring, bookmarks
- vs. Playwright: spawns headless browser, no cross-tab context

**Multi-Config MCP:** Separate MCP servers into individual config files — load on-demand for specific tasks.

---

### 6. Local AI & Open Source

**Hugging Face as "GitHub for AI":**
- ~2 million models across all modalities
- GGUF format for local execution with Ollama
- Model cards are essential reading before downloading
- Spaces provide live interactive demos

**Running Models Locally:**
```bash
ollama run <model-id-from-hugging-face>
```

**Qwen 3 as Claude Code Alternative:**
- 2,000 free runs/day via Qwen OAuth
- Use inside Claude Code via Claude Code Router (CCR)
- Combine free model quality with superior agent framework

---

### 7. n8n & Automation

**Hosting n8n on AWS EC2 (Free Tier):**
- t2.micro: 750 hours/month free for 12 months
- Runs 24/7 without sleeping (vs. Render's restrictions)
- Docker deployment with `n8n_data` volume for persistence

**Nano Banana (Google's Image Model):**
- Outperforms ChatGPT 4o in photo editing, text rendering, color fidelity
- Preserves original image colors (no orange/yellow cast)
- Integration via File.AI (300+ AI models unified API)
- Key for UGC ad automation pipelines

**UGC Ad Automation Pipeline:**
Input (Prompt + Image) → Nano Banana (image generation) → V3 (video generation) → Telegram delivery

---

### 8. SEO & AI Traffic (Emerging)

**New SEO Playbook 2026:**
- AI-driven traffic converts up to 23x better than organic search
- AI platforms are decision engines, not search engines
- You're no longer being ranked — you're being cited
- New KPIs: AI visibility score, citation frequency, entity mention velocity
- 65% of LLM users never click, but 46% purchase from remembered brands

**Key Tactics:**
- Write content that helps AI make decisions (buyer guides, comparisons)
- Add summary boxes at article tops for AI extraction
- Schema markup for machine understanding
- Make content quotable — AI picks what's easiest to quote

---

## Action Items

### Immediate (This Week)
- [ ] Set up `cc-usage blocks --live` for token monitoring
- [ ] Configure custom status line using `/status-line`
- [ ] Install ShadCN UI MCP server with GitHub token (5,000 req/hour)
- [ ] Create a `shadcn.md` rule file for AI agent workflow
- [ ] Try pre-filtering in n8n — route obvious inputs through cheap model first

### Short-Term (This Month)
- [ ] Explore Git worktrees for parallel agent execution
- [ ] Test Nano Banana via File.AI for UGC ad workflows
- [ ] Set up Claude Code Router with Qwen 3 for free tier
- [ ] Audit content for AI extractability (summary boxes, schema markup)
- [ ] Try background bash commands (Ctrl+B) for dev server monitoring

### Learning
- [ ] Study the 6 Levels of Claude Code — identify your current level
- [ ] Read about spec-driven development vs. hybrid approach
- [ ] Learn FFmpeg basics for media processing automation
- [ ] Explore TweakCN for ShadCN theme customization

---

## Key Quotes

> "The fundamental problem with vibe coding is not the coding agents' ability — it's the LACK OF SPECIFICATIONS."

> "LLMs are pure functions. Output quality is strictly limited by the quality and structure of your context."

> "AI gets you 0-90%, humans provide the last 10% — never fully automate creative or high-stakes work."

> "Context rot hits at 50-60% window capacity regardless of total window size — a bigger window doesn't save you."

---

## Related Notes
- [[SixLevelsOfClaudeCode]] — Full breakdown of Claude Code proficiency levels
- [[GitHubSpecKitVibeCoding]] — Spec-driven development with GitHub tools
- [[ShadCNNotJustLibrary10x]] — ShadCN MCP server workflow
- [[AdvancedContextEngineeringForAgents]] — Context optimization for AI agents
- [[ReduceAIAutomationCosts87Percent]] — Pre-filtering cost optimization
