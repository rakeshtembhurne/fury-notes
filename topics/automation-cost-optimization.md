---
created: 2026-05-19
tags: [topics, automation, n8n, cost-optimization, ai]
source: YouTube transcripts
---

# AI Automation Cost Optimization

## The Cost Problem

- Flagship AI models: $1-20 per API call
- Automations run 100s-1000s times/day
- Costs quickly spiral out of control
- Quality vs cost tradeoff is real

## Pre-Filtering: The Solution

### What is Pre-filtering?
Before sending to expensive AI:
1. Filter with cheap criteria first
2. Only expensive AI for qualified items
3. Dramatic cost reduction

### Example Results
- AI Marketing Automation: **87% cost reduction**
- AI Newsletter Automation: **91% cost reduction**
- General automations: **40-60% reduction**

## Implementation Strategy

### Tiered Architecture
```
Level 1: Cheap/Fast (filter)
  ↓ passes?
Level 2: Moderate AI (simpler task)
  ↓ passes?
Level 3: Expensive AI (full analysis)
```

### Example: Newsletter Automation

**Before (Expensive)**
```
RSS → GPT-4 (analyze EVERY article) → Save
```
Cost: $0.01-0.05 per article, thousands daily

**After (Optimized)**
```
RSS → Simple keyword filter (free) → 
      If relevant → GPT-4 (analyze) → Save
```
Cost: ~$0.001 per article, 10x reduction

### Example: Lead Qualification

**Before**: Every lead → Expensive AI → Score

**After**: 
1. Basic criteria filter (budget, industry)
2. Cheap model pre-qualification
3. Only hot leads → Expensive AI

## n8n Cost Saving Features

### 1. Pin Data
- Save API responses
- Don't re-call expensive endpoints
- Test workflow without costs

### 2. Mock Data
- Test without any API calls
- Full workflow testing free

### 3. Expression Shortcuts
- `=` to switch to expression mode
- Faster workflow building

### 4. Pre-filtering Nodes
- IF/Filter nodes before AI
- Switch node for routing
- Code node for custom logic

## Model Selection Strategy

| Task Type | Use This | Cost |
|-----------|----------|------|
| Simple classification | GPT-3.5 | $0.001 |
| Routing/deduplication | Gemini Flash | $0.01 |
| Standard analysis | GPT-4 | $0.03 |
| Complex reasoning | Claude Opus | $0.10 |

## Practical Workflow Design

### Optimized Content Pipeline
```
1. RSS/Crawler (free)
   ↓
2. Keyword filter (free)
   ↓
3. Content score (cheap model)
   ↓ (if score > threshold)
4. Full AI analysis (expensive)
   ↓
5. Publish/Save
```

### Optimized Customer Service
```
1. Message received (free)
   ↓
2. Intent detection (cheap)
   ↓
3. FAQ match? → Auto-reply (free)
   ↓ (no match)
4. Route to agent (human/AI)
```

## Measuring ROI

Track:
- Cost per automation run
- Cost per output (article, lead, etc.)
- Time saved vs manual
- Quality maintained?

## Key Takeaways

1. **Filter first**: Never send everything to expensive AI
2. **Use right model**: Don't use Opus for simple tasks
3. **Cache responses**: Pin data when possible
4. **Monitor costs**: Track every automation expense
5. **Iterate**: Measure, adjust, optimize

--
**Sources**: Mike Pekka (AI Automation)

## Related
- [[automation-workflow-patterns]] — Core automation patterns
- [[n8n-ai-agents-workflows]] — n8n AI workflows
- [[productized-ai-system-n8n-airtable]] — Productized AI service model
