---
created: 2026-05-19
updated: 2026-05-19
tags: [topics, ai-video, prompt-engineering, cinematography, ai-tools]
source: YouTube transcripts
---

# AI Video Prompt Engineering

## Source Videos
- Why Your AI Videos Look Fake — Adil / Kling AI (2026-03-11)
- 38 Camera Moves for Cinematic AI Videos (2026-03-11)

---

## Core Philosophy

> "If you want to get ahead of 90% of the people, you can't keep thinking like a prompt engineer. You need to channel your inner movie director."

> "The tech is moving fast, but the principles of good cinematography stay the same."

---

## The Start Frame = 80% of Result

**The #1 mistake:** Typing a long prompt and hitting generate — that's text-to-video, a slot machine with zero composition control.

**The fix:** Invest time in quality start frames.

### What makes a bad start frame:
- Blurry images
- AI-looking plasticky skin (the AI carries this through every second)
- Generic/unclear composition

### What makes a great start frame:
- High-quality generated image (Soul 2, Nana Banana Pro)
- Clear subject and composition
- Describes: who, where, what's happening, camera move, mood

> "Garbage in, garbage out. Invest time in the start frame — it's 80% of your result."

---

## The 5 Elements of Every Prompt

1. **Who** — subject/person in the scene
2. **Where** — location/setting
3. **What's happening** — action/event
4. **Camera move** — dolly, zoom, orbital, etc.
5. **Mood** — emotional quality (dramatic, peaceful, tense, etc.)

---

## Character Consistency

**The problem:** Generate multiple clips, stitch together → same actor with different hair color, eye color, birthmark jumping around.

**The solution:**
- Use character sheets (consistent reference images)
- Tag characters in tools to maintain consistency
- Use multi-shot mode and prompt each scene separately

> "Look, no face drift, no morphing, same person even from different angles, even from the back."

---

## Controlling Complexity

> "You can't ask it to generate 15 different explosions and an earthquake while the actors are having an emotional conversation. It's also not how film works."

**One primary action per scene** — don't overwhelm the AI or the viewer.

---

## Simpler Prompts = Better Results

> "When you have simpler prompts, the model tends towards output it's actually good at."

**Tip:** Enable multiple generations and let the model find what it's good at. General prompts often outperform highly specific ones.

---

## Gemini Prompting Tip

**Quirk:** Gemini might start animating instead of giving you the prompt.

**Fix:** Add "Do not generate. Just give me the prompt in all caps" at the end of your request.

---

## 38 Camera Moves (Summarized)

| Category | Description |
|----------|-------------|
| **Dolly** | Camera on wheeled platform, moves forward/backward through space |
| **Zoom** | Lens manipulation for dramatic effect |
| **Orbital** | Camera rotating around the subject |
| **Vertical** | Crane shots for dramatic reveals |
| **Subject-based** | Camera follows the action |

**Pro combinations:**
- Dolly + Zoom = vertigo effect
- Slow dolly + close-up = emotional tension
- Fast orbital + wide = energy and scale

---

## Slow-Mo Trick

For complex fast action: try the slow-mo trick — prompt for slow motion version of complex scene, then speed up in editing.

---

## Action Items

- [ ] Always use start frames — never text-to-video alone
- [ ] Invest time in creating quality start frames (80% of result)
- [ ] Write prompts like a director: who, where, action, camera, mood
- [ ] Build character sheets for consistent characters
- [ ] Generate one primary action per scene
- [ ] Use LLM to help generate detailed prompts
- [ ] Try the slow-mo trick for complex fast action
- [ ] Memorize the 12 camera categories
- [ ] Practice dolly moves first, then combine techniques

---

## Related Notes

- [[ai-video-creation]] — Full AI video creation guide
- [[ai-tools-2026]] — AI tools overview
- [[38CameraMovesCinematicAIVideos]] — Detailed camera techniques
