---
created: 2026-05-28
tags: #research #khabaronline #content #gap #action-needed
author: Fury (AI)
---

# KhabarOnline Content System — Gap Analysis

> **Status:** Gap identified — no content system exists
> **Priority:** High — KhabarOnline listed as "LIVE, needs content" in research_program.md
> **Blocker:** Requires Rocky input on brand voice + content priorities before prompts can be built

---

## What KhabarOnline Needs (vs Trigyaa)

Trigyaa has a comprehensive 400-line prompt library. KhabarOnline has NOTHING.

| Component | Trigyaa | KhabarOnline |
|-----------|---------|--------------|
| Hermes prompts | ✅ 400 lines | ❌ None |
| Content calendar | ✅ 30-day IG calendar | ❌ None |
| Image workflow | ✅ Flux AI workflow | ❌ None |
| Brand voice doc | ✅ In prompts | ❌ None |
| Platform strategy | ✅ Defined | ❌ None |

---

## What KhabarOnline Content System Should Include

### Brand Voice
Different from Trigyaa — news site, not fashion:
- **Tone:** Professional, credible, informative
- **Voice:** Authoritative but accessible (not academic, not tabloid)
- **Humor:** Low (news context, not brand comedy)
- **Emoji:** Minimal, professional only
- **ICC:** Indian readers interested in news, local affairs, national events

### Content Types Needed

1. **Breaking news posts** — Twitter/X, Facebook
2. **Article excerpts** — compelling pull quotes for social
3. **Headlines** — punchy, click-worthy versions
4. **News summaries** — "5 things you missed today" format
5. **Local India angles** — state/city specific news hooks
6. **Opinion/analysis** — expert commentary posts
7. **Fact checks** — debunk viral misinformation

### Platform Strategy

| Platform | Content Type | Priority |
|----------|--------------|----------|
| Twitter/X | Breaking news, headlines, threads | HIGH |
| Facebook | Article links + summaries, community posts | HIGH |
| Instagram | Less relevant for news — maybe infographics | MEDIUM |
| WhatsApp | Shareable headlines (if channel exists) | MEDIUM |

### Hermes Prompt Pattern (Similar to Trigyaa)

```
BRAND: KhabarOnline
PRODUCT: Indian news website, regional + national coverage
TONE: Professional, credible, informative
VOICE: Authoritative but accessible
HUMOR: Minimal (news context)
EMOJI: Professional only (📰, 🇮🇳)
...
```

---

## Action Needed From Rocky

Before prompts can be built, Rocky needs to define:

1. **Brand voice specifics** — What's the editorial stance? Political leaning? Target audience?
2. **Content priorities** — Which sections of khabaronline.in get the most traffic? What should social focus on?
3. **Regional focus** — Is it national news only, or specific states/regions?
4. **Posting frequency** — How many posts/day? Which platforms?
5. **Existing social accounts** — Are they already set up? What handles?

---

## Related

- [[research_program.md]] — "KhabarOnline: LIVE, needs content"
- [[trigyaa-hermes-content-prompts]] — Example of complete content system
- [[trigyaa-content-calendar-30day]] — Content calendar template
- [[brandsome-app-social-media-saas]] — AI content generation (could be used here)
