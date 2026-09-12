---
created: 2026-09-12
updated: 2026-09-12
tags: #research #reddit-lead-finder #distribution #agency-system #deep-dive
source: 3-track parallel research (product teardown + India-US distribution + agency automation), Sept 2026
---

# Reddit Lead Finder — Deep Research Findings (Sept 2026)

> Question: clone it, sell to the US from India, automate everything. Sellable in 1–2 weeks?
> Verdict: **yes, with a safety-first wedge.** Details below.

## 1. Product teardown

**Shelf (all $19–49/mo, crowded):**
- redditgrow (redditgrow.ai): Starter ~$29/mo (1 project, 6 subs, 100 opps total, 300 AI replies); Growth ~$29–49 (25 subs, 1,000 opps/mo, 1,500 replies). Live proof: $1,102 MRR, 1,590% 30-day growth, $40K TrustMRR ask (~36x — rich vs 2–5x norm)
- Redreach (redreach.ai): from $19/mo, $12 3-day pass as trial wedge. Inbound AI replies + outbound Chrome DM automation, unlimited AI replies, white-label tiers. Positions vs Notifier ($49–499), ReplyGuy ($49), Octolens ($59–359)
- Syften (from $19.95, Standard $39.95): 10+ platform monitoring, <1min alerts — NO reply generation, NO safety, NO ROI analytics
- ReplyGuy ($49): fully automated replies — cautionary tale, robotic, deleted, bans
- Pattern: monitors ($20–40) vs engagement platforms ($29–49) vs enterprise listening ($59–499)

**Moat is safety + ROI proof, not keyword alerts.** ReplyGuy proves automation-first gets you banned and hated.

**Reddit API 2026 (the load-bearing facts):**
- Free: 100 queries/min per OAuth client — shared bucket across ALL your customers. Fine single-tenant, breaks multi-tenant fast
- Commercial: $0.24/1,000 calls, no public rate card, manual use-case review, reported ~$12K/yr minimums (unconfirmed), approval "rare"
- ToS: no ML training on Reddit data, no raw-data resale, honor deletions. Pushshift dead. Unit math: 1M calls/mo = $240 — fine at $39 ARPU only with efficient polling
- v1 rule: **manual-post-only, never auto-post.** 7-day warm-up guidance, rate limits, shadowban detector, rule-aware prompts

**Who pays:** US SaaS founders/indies ($19–39, strongest fit) → agencies ($39–79+, seats + white-label, least churn) → DTC/local services (competitor alerts). Avoid affiliates (ban-risk segment). Non-payers: casual users, enterprise (buys Brandwatch).

**Week-1 MVP:** URL → auto keywords + competitors → 10-sub monitor (15-min poll, in free tier) → intent score 0–100 + Google-index flag → opportunity feed → AI reply drafter (copy-post, never auto) → email/Slack alerts + digest → thread tracking → Stripe $19/$39 hard caps. OUT: auto-post, DMs, multi-platform, seats. Stack: Next.js + Supabase + Vercel cron + Resend + Stripe (~$1/mo).

## 2. India → US distribution

**Conversion math (plan against this):** 1,000 targeted visits → 20–70 trials → 1–4 paying, zero touch. Visitor-to-signup 2–7%, trial-to-paid 2–5% self-serve. Anything promising 10%+ no-touch at this price is fiction.

**Channels that convert:**
- Reddit problem-threads + long-tail SEO: highest intent, free. 90/10 value rule or bans. First 100–300 users from niche subs is the documented norm
- X build-in-public: Tue 9am ET peak (Buffer 8.7M-post study), converts via DMs/waitlist not clicks (~1–3% CTR)
- Product Hunt: spike not channel. 487 of 500 analyzed SaaS launches effectively dead after. Needs 150–200 upvotes in 4h + 400 waitlist for top-5 odds. Defer unless armed
- Directories triple-shot (BetaList + Microlaunch + Uneed): 100–300 visits + backlinks, same assets reused
- AppSumo LTD: SKIP week 1 — 340 LTDs at $149 then 18 months of regret supporting lifetime users
- Cold email: SKIP week 1. Inbox placement 65–83%, avg reply 3.43%, Gmail/Yahoo/Microsoft enforcement burns fresh domains. Warm separate domain in background

**IST mechanics (Sept = EDT, 9.5h gap):** X for US mornings = post 6:30–7:30pm IST Tue–Thu. Reddit US subs 7–10am ET = 4:30–7:30pm IST. PH resets 12:01am PT = 12:31pm IST. Mornings = build, evenings = ship + engage + support sweep. Turn timezone into coverage story: "US-overnight support from IST."

**Trust fixes:** .com + real name + face; Stripe badge + USD + 30-day refund; state data region explicitly; async SLA published ("median 6h, max 12h"); 2-click cancel; first 10 US users hand-onboarded free for logos/quotes.

**Week-1 ranked list:** Reddit (5 threads/day, 3 subs) → X ship loop (1 post + 1 demo/day) → directories triple-shot → PH only if 200+ waitlist → 50 hand-picked Looms. Scoreboard: 500–1,000 visits → 15–50 trials → 1–5 paying. Zero paid by visit 750 = fix headline + 60s Loom, not traffic.

## 3. Automated agency setup (his stack, +2 free additions)

**Add only:** Chatwoot self-hosted (support inbox + widget, replaces Intercom $0) + Tally free (surveys/forms). No ChurnBuster, no ConvertKit — n8n + Stripe webhooks + ListMonk cover it.

**Stages (human/auto split):** Validate 90/10 (10 waitlist + 2 Stripe pre-pays or kill) → Build 70/30 (Claude Code, Vercel previews, Sentry, docs-from-day-1 feeds support bot) → Launch 60/40 (Postiz queue, ListMonk T-7/T-0/T+3) → Distribute 30/70 (1 long-form/wk human, Postiz recycle + n8n repurpose auto) → Sell 40/60 (Stripe Checkout + portal, 7-email trial drip, PostHog PQL alerts, Loom not calls) → Support 15/85 (Chatwoot → n8n AI agent → Supabase pgvector KB, auto-reply ≥0.8 confidence, Telegram ping + <12h SLA below) → Retain 20/80 (Stripe Smart Retries + n8n dunning d1/d3/d7, cancel → Tally exit → winback 30/60/90d, founder replies to every cancel <24h).

**Solo week (25–30h IST):** Mon build → Tue distribute → Wed sell+support → Thu retain → Fri mini-launch. Daily 30min Hermes digest (MRR, signups, errors, tickets). Rules: support >5h/wk → write KB article not hire; churn >7% → fix onboarding before features.

## Decision matrix
- Build it? Yes — week-1 MVP is real, free-tier API suffices single-tenant, wedge = safety-first manual posting vs ReplyGuy's ban-machine
- Price: $19 starter (50 opps) / $39 growth (500 opps) / $79 agency later
- First move: validation tweet + landing waitlist, NOT code. 10 waitlist + 2 pre-pays or kill
- Biggest risk, ranked: (1) account bans if automation creeps in — hold manual-only line; (2) API bucket at multi-tenant scale — per-customer polling budgets from day 1; (3) crowded shelf — win on safety + ROI proof

## Related
- [[clone-list-sept-2026]] · [[validated-micro-startup-ideas]] · [[micro-startup-playbook]]
- [[startup-business-learnings]] · [[content-distribution-learnings]] · [[dev-tech-learnings]]
