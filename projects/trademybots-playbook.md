---
project: TradeMyBots
type: playbook
updated: 2026-04-15
---

# TradeMyBots Playbook

Retail trading bot marketplace for India. Forward-tested, transparent, killswitch-first.

## Story

Indian retail traders lose more to emotion than to strategy. I've watched friends freeze during entries, panic during drawdowns, and hand money to tipster groups on Telegram. Existing "algo" platforms are either too technical (write pine script) or too shady (fake backtests). TradeMyBots curates bots with real forward-tested P&L, published R-multiples, and one-click kill. No code. No tipsters. Just rules.

## Voice & Tone

**Would write:**
1. "Bot #4 hit -12% drawdown this week. Kill switch activated at -10% as designed. Account intact."
2. "Backtest said 78% win rate. Live shows 52%. This is why we forward-test for 90 days before listing."
3. "R-multiple: your profit divided by your risk. If this is under 1, you're losing even when you win."

**Would NOT write:**
1. "🚀 Bot made 500% this month, link in bio 💰💰💰"
2. "Guaranteed returns. No loss strategy."
3. "DM me for free tips"

**Words we use:** forward-test, R-multiple, drawdown, capital, rules, kill-switch, live, verified
**Words we avoid:** guaranteed, holy-grail, secret, unlimited, profit-only, 100%, free tip
**Formality (0-10):** 6
**Humor (0-10):** 2 (risk-serious audience, be respectful)
**Emoji policy:** 📊 for numbers, ⚠️ for risk callouts. No 🚀🔥💰.

## Content Pillars

### Pillar 1: Live P&L Transparency
- Angle: Weekly real numbers from live bots
- Example hook: "Week 12 live P&L: +₹34K / -₹8K drawdown. Full trade log."
- ICP pain: "Scam fatigue"

### Pillar 2: Backtest vs Live
- Angle: Why backtests lie
- Example hook: "78% in backtest, 52% live — here's the gap"
- ICP pain: "Bots that fake results"

### Pillar 3: Risk Education
- Angle: R-multiples, position sizing
- Example hook: "You made ₹50K. You risked ₹3L. That's 0.17R. Unsustainable."
- ICP pain: "Don't know how to size positions"

### Pillar 4: Creator Spotlights
- Angle: Humanize successful bot creators
- Example hook: "How Amit, Pune accountant, earns ₹80K/mo from his nifty bot"
- ICP pain: "Who can I trust?"

## Launch Plan

Pre-launch (product not yet built). These steps before MVP ship:

### T-60 days
- [ ] 20 trader interviews (validate ICP + pain)
- [ ] 3 bot-creator interviews (supply side)
- [ ] Landing page with waitlist
- [ ] Domain purchased

### T-30 days
- [ ] MVP: paper-trading mode with 1-2 bots
- [ ] Telegram community launched
- [ ] YouTube channel with 3 educational videos
- [ ] 100 waitlist signups

### Launch day
- [ ] Open beta for waitlist
- [ ] ProductHunt India submission
- [ ] Reddit r/IndiaInvestments launch post
- [ ] YT launch video
- [ ] Twitter thread

### Week 1-4 post-launch
- [ ] Onboard 10 beta traders
- [ ] Daily live P&L broadcasts
- [ ] Reply to every objection
- [ ] Iterate on kill-switch UX

## Channel Strategy

- **YouTube:** Primary. Traders watch long-form to evaluate bots before paying.
- **Twitter:** FinTwit India conversation lives here. Live P&L snapshots drive daily engagement.
- **Reddit:** r/IndiaInvestments, r/IndianStockMarket — educational posts build trust.
- **Telegram:** Community + daily alerts. High-engagement for active traders.
- **Blog:** SEO for "algo trading India", "best trading bot India" long-tail.

## Key Messages

- **1-line:** "Vetted trading bots for Indian retail. Live P&L, real risk stats, one-click kill."
- **3-line:** "Indian retail traders lose to emotion, not strategy. TradeMyBots curates bots with real forward-tested P&L, transparent R-multiples, and one-click kill switches. No code. No tipster groups. Just rules that execute."
- **Elevator:** "Part-time traders can't code, can't afford fund managers, and don't trust tipster groups. We vet trading bots on real live capital for 90 days before listing. You see actual P&L, actual drawdowns, actual R-multiples. Pick one, subscribe, one-click kill anytime."

### Objection handlers

| Objection | Response |
|---|---|
| "What if it blows up my account?" | Every bot has a mandatory kill-switch at your chosen drawdown %. Stops trading, sends alert. You decide to restart. |
| "How do I know the P&L is real?" | Every listed bot trades our live capital for 90 days. Broker statements published. |
| "Why not just trade manually?" | You already do. How many entries did emotion cost you last month? |
| "Existing platforms do this" | They sell code. We sell verified performance. Different product. |
| "Is this legal?" | Yes. Users run bots on their own broker account via API. We don't manage funds. |

## Competitors & Wedge

- **They:** Tradetron/Streak sell tooling (build your own). Algoji sells premium strategies.
- **We:** Sell curation + verification. The buyer trusts the platform, not a stranger's claim.
- **Wedge:** 90-day forward test with published broker statements. Nobody in India does this publicly.

## Content Repurposing Map

| Source | Twitter | YouTube | Reddit | Telegram | Blog |
|---|---|---|---|---|---|
| Weekly P&L | snapshot tweet | detailed video | case-study post | daily updates | monthly recap |
| Bot walkthrough | thread w/ clips | main video | deep-dive post | live Q&A | long-form |
| Risk lesson | thread | short explainer | educational | daily tip | SEO pillar |

## Glossary / Lore

- **"R-multiple":** Profit ÷ risk per trade. Van Tharp framework.
- **"Forward test":** Real-money testing on live market (not historical backtest).
- **"Kill switch":** Drawdown threshold that auto-stops bot.
- **"Verified bot":** Passed 90-day forward test with published broker statement.

## Decisions Log

- `2026-04-15` — scaffolded with startups skill
- `2026-04-15` — India-first, INR pricing
- `2026-04-15` — forward-test mandatory before listing (wedge vs competitors)
- `2026-04-15` — pre-launch phase — build MVP before any bot onboarding

## Open Questions

- Regulatory — SEBI requirements for publishing bot P&L?
- Broker integration priority — Zerodha first, Fyers second?
- Creator revenue share — what % retains creators?
- Kill switch UX — app notification vs hard broker-API cutoff?
- Paper-trading first 30 days mandatory?

---

> Related: [[trademybots-setup]] · [[startup-business-learnings]] · [[trust-mrr-platform]] · [[research_program]]
