---
created: 2026-05-19
tags: [topics, product-idea, trading, pine-script]
source: notes directory
---

# AaalooPyaz Backup — PineScript Trading Indicator

> [!warning]
> This file appears to contain PineScript code for a TradingView indicator, not a product idea as the filename suggests. Verify before using.

## File Content

This is a PineScript v6 indicator called "DELETE" with short title, overlay enabled, max_bars_back set to 2584.

### Key Components

**AVWAP (Anchored Volume Weighted Average Price) Calculation:**
- Uses volume-weighted average price across specific lookback periods
- Calculates separate AVWAPs for highest and lowest bars

**Multiple Moving Average Levels:**
- MA1: 17 bars
- MA2: 72 bars
- MA3: 305 bars
- MA4: 1292 bars

**Visualization:**
- Red lines for highest price AVWAPs
- Green lines for lowest price AVWAPs
- Fill between mid and extreme values
- Line thickness increases with higher MA levels (1, 2, 4, 6)

**Pattern Detection:**
- Pin bar detection (upper and lower rejection candles)
- ATR-based minimum pin size
- Doji detection (body/range ratio < 0.1)
- Bullish and bearish engulfing patterns

**Separation Signals:**
- Detects when MA levels separate from each other
- Used to trigger background color changes (green/red zones)

**Background Color Logic:**
- Tracks separations at each MA level
- Green background when lower MAs are separating upward
- Red background when upper MAs are separating downward
- Yellow when both are active simultaneously

---

> Note: This appears to be a trading strategy implementation. The filename "AaalooPyaz" suggests it may have been mislabeled or was a codename during development.
