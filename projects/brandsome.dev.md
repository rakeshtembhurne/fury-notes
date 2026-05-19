---
created: 2026-05-19
tags: [project]
source: notes directory
---

# Brandsome.dev Playbook

AI-powered logo and brand identity generator SaaS.

## Project Status

**Status:** 🟡 Planning
**Domains:** brandsome.dev, brandsome.app

Not started. Will use AI Boilerplate to build.

## Concept

### Problem
People have brand ideas but don't know how to create professional graphics.

### Solution
1. User enters brand name + tagline
2. AI generates 20-50 logo variations across layout styles:
   - Square logo (icon only)
   - Rectangle horizontal (icon + name)
   - Top-aligned (name on top, icon below)
   - Left logo (icon on left, name on right)
   - Minimalist text-only
   - Monogram styles
3. User browses and selects preferred design
4. Upsell: Additional brand assets

## Tech Stack

- **Frontend:** Next.js / React
- **AI:** Claude API for logo concept generation
- **Image Generation:** AI image API (Replicate, DALL-E, or Flux)
- **Payments:** Stripe
- **Reference:** Use AI Boilerplate to spin up quickly

## Pricing Model

| Item | Price |
|------|-------|
| Logo pack (5 variations + PNG + SVG) | $10 |
| Brand kit (logo + letterhead + business card) | $25 |
| Social media kit (profile images, covers, posts) | $15 |
| Full brand package (everything) | $40 |

## Next Steps

- [ ] Write detailed product spec
- [ ] Map out logo layout styles
- [ ] Research AI image generation APIs
- [ ] Design logo variation system
- [ ] Build MVP with AI Boilerplate

## Competitors

- logo.com (inspiration)
- looka.com
- brandmark.io
- hatchful.shopify.com

## Workflow

```
User Input (brand name, tagline)
       ↓
AI Logo Generation (multiple layouts)
       ↓
User Selection
       ↓
Asset Generation (SVG, PNG, brand kit)
       ↓
Payment → Download
       ↓
Upsell (letterhead, cards, social)
```

## Key Decisions

- Inspired by logo.com but AI-powered for speed and scale
- Using AI Boilerplate as starting point
- Stripe for payments
