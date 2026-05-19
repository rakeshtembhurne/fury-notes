---
created: 2026-05-19
tags: [topics/personal/tech]
source: notes directory
---

# AI Landscape

_Auto-consolidated from multiple video and text sources covering AI tools, coding agents, video generation, GEO/SEO, influencers, and monetization._

## Key Takeaways

### AI Models & Coding Agents
- ==Always use **Opus 4.6 (Extended)** — it is the most capable model for the best results; Haiku and Sonnet are significantly less capable==
- ==**Co-work** (Claude Code) can read/write files, invoke terminal commands, and perform multi-step tasks; Chat mode cannot==
- ==**Plan Mode** (Shift+Tab) should be used before prompting for bigger changes — it prevents Claude from immediately touching files==
- ==Out of 10,000+ Claude Code plugins, only 6 are truly essential==
- ==Superpowers (90K+ GitHub stars) makes Claude plan, write tests, use sub-agents, and review its own work==
- ==Frontend Design (250K+ installs, by Anthropic) prevents generic AI-looking UIs==
- ==Code Review runs 5 parallel agents to check your codebase from different angles==
- ==Security Guidance scans your entire codebase for vulnerabilities before deployment==
- ==Claude Memory (40K+ stars) gives Claude persistent memory across sessions==
- ==Qwen 3.6-35B MoE — open-source, only ~3B active at inference but 35B-scale capacity==
- ==Claude Haiku 4.5 solves 65% of bug challenges; GEPA optimization improves it further==
- ==The orchestration harness wrapping an LLM drives more performance variation than the model itself — Stanford found 6x performance difference==
- ==Harness optimized on one model transfers to five others — the reusable asset is the harness, not the model==
- ==Self-evolution was the only consistently helpful module across benchmarks (+4.8 SWE, +2.7 OS World)==
- ==90% of all compute flows through delegated child agents, not the parent==
- ==Context rot is real — don't bloat CLAUDE.md; keep it short and point to reference files==
- ==Graphify builds a knowledge graph once; Claude reads that at session start instead of rereading files==
- ==Claude Code already has all five features that Hermes and OpenClaw offer — you don't need a separate framework==

### AI Video Generation
- ==13 cents per video== using Kling AI + Nano Banana Pro + CapCut workflow
- ==Use start frames== — garbage in, garbage out; quality start frame = 80% of result
- ==Write prompts like a movie director== — Who, where, what's happening, camera move, mood
- ==All-in-one tools > single subscriptions== — Weevi and Hicksfield are S-tier
- ==Hunyan by Tencent== — free AI video from text/image
- ==HeyGen = Best Talking Avatars== — ready avatars + custom + lip sync
- ==ElevenLabs = Best Text-to-Speech== — natural sounding AI voices
- ==Hicksfield = Best Video Generation== — VFX, upscaling, character animation
- ==Open Art = Best Value== — cheapest for quality models

### GEO (Generative Engine Optimization)
- ==GEO (Generative Engine Optimization) is the new SEO== — AI search traffic growing 500% YoY
- ==Most businesses are invisible to AI== — when asked for recommendations, AI doesn't mention them
- ==Claude Code geo-audit tool runs 5 parallel sub-agents== — PDF report generated is client-ready
- ==Market projected to grow to $7 billion== — only 23% of marketers are thinking about GEO
- ==SEO is dead — long live authority== — rankings no longer matter, citations do
- ==The game is now attribution== — being cited by AI Mode > ranking #1
- ==Complex queries are the moat== — 77% of 6+ word queries trigger AI Overviews vs only 23% for short queries
- ==Zeroclick is reality== — 59% of searches now don't result in a click
- ==Building authority takes 10 years== — there's no shortcut
- ==Google built a database of 54 billion real-world entities and 1.6 trillion facts==
- ==Schema markup is structured code that explicitly tells AI what entity you are==
- ==Three baseline schema types every business needs: Organization, Product/Service, Local Business==

### AI Influencers & Content
- ==100 billion fake AI influencers are coming== — AI influencers will seem 100% real
- ==Selfless content wins== — the more you care about audience value, the more you grow
- ==Post on ALL platforms== — YouTube Shorts is mandatory for AI/GEO defense
- ==Niche down further== — go even deeper to differentiate
- ==Real life is the moat== — AI can't replicate authentic human connection
- ==Stop chasing virality== — track average views per post instead
- ==Hire a journalist/writer== — for long-form content quality
- ==Live shopping/social commerce is the future== — Whatnot did $8-10B in GMV

### Shannon — Open Source AI Pentester
- ==AI pentesting is 10x cheaper than human pentesters== — but still ~$60 per scan in Claude credits
- ==Shannon is open source and free== — requires Claude API key (subscription doesn't work)
- ==Temporal ensures durability== — if credits run out, it resumes from checkpoint
- ==5 phases: Pre-flight → Pre-recon → Recon → Vulnerability + Exploit → Report==
- ==Found 11 critical vulnerabilities in OWASP Juice Shop, 4 fully exploited==
- ==Zero false positives== vs human pentesters

### Karpathy's Autonomous AI Researcher (March 2026)

Open-sourced autonomous researcher:
- Runs 100 experiments while you sleep
- Write prompts to direct AI research
- Demonstrates compound research loops

> Added from Twitter March 2026.

### Tools & Infrastructure
- ==OpenClaw fastest-growing project in GitHub history== — "stripper pole growth"
- ==1,142 security advisories received, 16.6/day, 99 critical== — most are AI slop, not real threats
- ==GhostClaw== — likely North Korea, distributing fake npm packages with rootkits
- ==Nvidia found 5 sandbox escape methods in NemoClaw within 30 minutes==
- ==Pi== — minimal self-modifying coding agent; "less is more" for tool design
- ==Karpathy's LLM Wiki== — persistent knowledge base vs RAG's zero compounding
- ==Passmark== — open-source AI agent for regression testing at scale
- ==Ollama now supports Hermes AI Agents== — fully local, zero-cost autonomous agents
- ==xAI Grok voice APIs== — ~10x cheaper than ElevenLabs
- ==Alibaba Qwen 3.6-35B MoE== — efficient open-source multimodal agentic coding model
- ==Graphify== — instant knowledge graph for Claude Code; runs locally, one API call
- ==SurfSense== — free, open-source alternative to NotebookLM

### JS Frameworks Referenced
- ExpressJS, Babel, Bluebird, KeystoneJS, Socket.io, Meteor, Passport.js, PM2, Chai

### NFT Basics
- An NFT (Non-Fungible Token) is part of the Ethereum blockchain
- "Non-fungible" means it's unique and can't be replaced with something identical
- Unlike Bitcoin (fungible — trade one for another and get exactly the same), a one-of-a-kind artwork is non-fungible

### Money & Monetization Ideas
- Become middleman between Google search and purchase (99K searches/second)
- Use AI video tools (Steve.ai, Pictory.ai) + ClickBank affiliate links for side hustle
- Etsy print-on-demand: find high-search, low-competition items on eRank, design in Canva
- YouTube Shorts monetization
- Personal management stack: Todoist + AnswerThePublic + Trello + Metricool + Jarvis/Jasper

---

## Notable Quotes

> "Stick with Opus 4.6 Extended. The other models make responses 'a little too slow' on complex tasks, but they produce significantly inferior results."
> "For anything involving code changes, architecture, or analysis — always set effort to High."
> "Co-work can invoke commands. It can invoke things which can read and write inside your folder that you have given it. Chat on the other hand does not do that right now."
> "The biggest mistake I see is typing a long prompt and hitting generate. That's text to video. And it's basically a slot machine. You have zero control over the composition."
> "Your start frame is responsible for 80% of your result. If you have a bad start frame, no amount of prompt engineering is going to save it."
> "Garbage in, garbage out — Invest time in the start frame, it's 80% of your result."
> "If you want to get ahead of 90% of the people, you can't keep thinking like a prompt engineer. You need to channel your inner movie director."
> "The tech is moving fast, but the principles of good cinematography stay the same."
> "Most businesses are completely invisible to AI search. They're invisible when someone asks AI for recommendations in that industry."
> "When you give Claude Code sub-agents, it's like hiring a main contractor who then hires electricians, concrete workers, HVAC specialists — each doing their specific job in parallel."
> "Agencies are charging $5,000 to $12,000 a month for GEO."
> "Google's not in the traffic business anymore. They're in the answer business."
> "You're not competing for position anymore. You're competing for attribution."
> "Simple questions get answered by AI directly. Complex questions still need sources — and that's where the entire game is moving."
> "Complexity is the moat."
> "Authority can't be gained — it has to be built. You can't skip it. You can't hack it."
> "Without schema, AI reads your content and guesses. With schema, AI reads your data and knows."
> "100 billion people that are pretty and charismatic are about to join social media. Unlike you, they are not real. But like you, they will seem real."
> "It takes me 5 seconds to look at your last 15 pieces of content and when it's 15 out of 15 that it was selfish for you."
> "The more you are selfless, the more you will win."
> "The human thing is about to explode in value."
> "The world is about to be a barbell. We're going extreme digital. AI is not far away. And I think one of the biggest opportunities... is real life."
> "A raw LLM is a CPU, powerful but inert. No RAM, no disk, no IO."
> "Agent = Model + Harness. If you're not the model, you're the harness."
> "We are very fast moving into a world where we have to change how we build software because all these AI tools are getting so good at identifying even the most weird multi-chained exploits."
> "Context rot happens when you feed too much context — outputs get worse, not better."

---

## AI Video Generation Workflow

```
1. Research → Find winning ad concepts (Facebook Ad Library)
         ↓
2. Storytelling → Define hook, problem, solution
         ↓
3. Clipping → Find/split reference clips
         ↓
4. Production →
   - Nano Banana Pro: Create AI avatar
   - Nano Banana Pro: Adapt to scenes
   - Kling AI: Generate video from image
         ↓
5. Editing → Build B-roll bank, assemble final video
```

**Tools:** Kling AI + Nano Banana Pro + CapCut (cost: ~13 cents/video)

---

## The Five Canonical Harness Patterns (Anthropic)

1. Prompt chaining
2. Routing
3. Parallelization
4. Orchestrator-workers
5. Evaluator-optimizer loops

---

## Claude Code Memory: Four-Layer Framework

| Layer | What It Is | What Goes In It |
|-------|-----------|-----------------|
| 1 — Agent Instructions | CLAUDE.md or AGENTS.md | Who the agent is, rules, behavior |
| 2 — Brand Context | Shared folder | Brand voice, ICP, positioning, client details |
| 3 — Agent Context | sold.md, user.md | How the agent should feel, common actions |
| 4 — Project Memory | Per-project history + plan | What was built, what worked, where to pick up |

---

## GEO Audit — Claude Code geo-audit Tool

- Runs 5 parallel sub-agents
- PDF report is client-ready
- ~60 seconds to run full audit
- Agencies charging $5,000–$12,000/month for this

---

## May 2026 Updates

### Opus 4.7 Issues — May 2026
Opus 4.7 is ignoring project instructions, skipping MCP servers, and burning through usage limits on tasks Opus 4.6 handles first try. Dozens of confirmed reports. Anthropic acknowledged the issue.

**Workaround:** If Opus 4.6 handles a task first try and 4.7 doesn't — use 4.6 for that task.

### Gemini 3.2 — May 2026
Gemini 3.2 drops today (May 19):
- Could get Gemini 3.2 and Gemini 3.5 simultaneously
- BridgeBench results coming
- Gemini 3.2 Flash may have leaked early — pricing signal suggests it cuts input costs while improving quality for coding tasks
- Google putting Gemini inside your phone, car, and laptop

### "Think Step By Step" is DEAD — May 2026
Nanjing University + Baidu paper:
- Cap reasoning at 60% of model's max = optimal
- Easy problems hit overthinking zone at 2,000 tokens
- 67.5% of reasoning flips are genuine overthinking
- Longer thinking = worse answers on simple tasks

### Hermes Agent 0.14 "Foundation Release" — May 2026
- Super Grok OAuth
- OpenAI Codex support
- Built-in XSearch
- Computer-use capabilities
- Pluggable video generation
- Early Windows support
- 88 commits, 633 merge requests, 1,293 files changed

---

## Action Items

- [ ] Switch to Opus 4.6 Extended if not already using it
- [ ] Practice using Plan Mode before any significant code changes
- [ ] Install 6 essential Claude Code plugins: Superpowers, Frontend Design, Code Review, Security Guidance, Claude Memory, GSD
- [ ] Audit CLAUDE.md — trim to under 200 lines, move detail to reference files
- [ ] Create a brand-context/ shared folder for use across all skills
- [ ] Run geo-audit on your own website(s)
- [ ] Implement Organization, Product/Service, and Local Business schema
- [ ] Post same content on YouTube Shorts (bare minimum defense)
- [ ] Identify 3 "uncool" parts of your life to share authentically
- [ ] Test OpenClaw + Gemma 4 locally for zero-cost AI agents
- [ ] Install Graphify on active projects
- [ ] Explore Karpathy's LLM Wiki pattern for research workflows
- [ ] Track AI citation presence as success metric, not just rankings
