---
created: 2026-05-19
updated: 2026-05-19
tags: #project #brandsome #priority #brand #saas
---

# Brandsome.dev + Brandsome.app

**Corrected scope (May 19, 2026):**
- **brandsome.dev** — Logo + brand identity tool (logo.com clone). Fonts, theme, logo generation. CLI + MCP for AI coding tools.
- **brandsome.app** — Social media content SaaS. Branded images, videos, Instagram reels, auto-posting via Postiz integration.
- Both are priority because Trigyaa, KhabarOnline, JciAlumni, and TrueValueEstate all depend on them for social media marketing and brand consistency.

Multi-tenant SaaS. Any startup can subscribe. Self-serve signup.

---

## Two Products

### brandsome.dev — Logo & Brand Identity Tool

**What:** Logo.com for the AI era. User enters brand name + tagline → AI generates 20-50 logo variations → select → upsell brand kit.

**Also provides:** CLI tool + AI Skills/MCPs (connectable to any AI coding tool like Codex, Claude Code, etc.)

**Pricing:**
| Item | Price |
|------|-------|
| Logo pack (5 variations + PNG + SVG) | $10 |
| Brand kit (logo + letterhead + business card) | $25 |
| Social media kit (profile images, covers, posts) | $15 |
| Full brand package (everything) | $40 |

**Tech:**
- Next.js frontend
- Claude API for logo concept generation
- AI image gen: Replicate/DALL-E/Flux
- Stripe for payments
- Clerk for auth

**Output formats:**
- Square logo (icon only)
- Rectangle horizontal (icon + name)
- Top-aligned (name on top, icon below)
- Left logo (icon on left, name on right)
- Minimalist text-only
- Monogram styles

**Workflow:**
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

**Competitors:** logo.com, looka.com, brandmark.io, hatchful.shopify.com

---

### brandsome.app — Social Media Content SaaS

**What:** Create branded images, videos, Instagram reels. Uses brand kit from brandsome.dev. Integrates with Postiz for scheduling.

**Features:**
- Create branded images, videos, Instagram reels
- AI-powered content generation using brand identity
- Auto-scheduling and posting via Postiz integration
- Works with brandsome.dev brand kit OR manual brand setup

**User Journey:**
1. Connect brand (from brandsome.dev or manual)
2. Select content type (reel, post, story, thumbnail)
3. AI generates variations
4. Download or send directly to Postiz for posting

**Tech:**
- Next.js frontend
- AI image/video gen APIs
- Postiz API integration for scheduling
- Clerk auth + Stripe billing

**Competitors:** Canva, Capcut (but focused on AI-generated branded content)

---

## Key Insight

**Brandsome.dev provides CLI + MCPs** — not just a web app. AI coding tools (Codex, Claude Code) can call the brand system to generate brand-consistent content automatically.

This means:
- Any indie hacker using Codex/Claude Code can generate brand assets via CLI
- Brandsome.dev becomes a backend for AI-assisted branding
- Works as both standalone web app AND as AI tool integration

---

## Both Products Share

1. **Brand kit data model** — colors, fonts, logo assets, voice guidelines
2. **Multi-tenant architecture** — each subscriber has their own brand workspace
3. **Postiz integration** — content from brandsome.app goes to Postiz for scheduling

---

## First Customers (Dogfood)

1. **Trigyaa.com** — Women's D2C, needs social content
2. **KhabarOnline.in** — News site, needs content
3. **JciAlumni.org** — 40K member community, needs outreach
4. **TrueValueEstate.com** — Property valuation SaaS, needs marketing

Validate with own projects → Open to public

---

## Status

🟡 Planning — Not started. Fresh start.

## Next Steps

- [ ] Write detailed product spec for both products
- [ ] Map out logo layout styles
- [ ] Research AI image generation APIs (Flux vs DALL-E vs Replicate)
- [ ] Design brand kit data model
- [ ] Plan multi-tenant architecture
- [ ] Design Postiz integration
- [ ] Build MVP using vibe coding

---

## Related
- [[trigyaa-playbook]]
- [[project-priorities-2026]]
- [[research_program]]
