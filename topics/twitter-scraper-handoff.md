---
created: 2026-09-12
tags: #twitter #pipeline #handoff #scraping-contract
---

# Twitter Scraper Handoff — Contract for External Scraper AI

> Rocky gives the scraper AI access to this repo. Its ONLY job: fill `tweets` with fresh rows. Everything downstream (learnings, digests) is owned here and untouched.

## What to scrape
- Accounts: `accounts/following_handles.txt` (504 handles) + `accounts/ai_twitter_handles.txt` (32 handles) — handle = X username without @.
- Cadence: all accounts, every 6 hours. New tweets only — never re-insert (see dedupe rule).
- Content: original tweets + quote-tweets. SKIP pure retweets (text starting with `RT @`) — the learnings stage filters these anyway, so don't waste writes on them.

## Where to write
- SQLite DB: `data/tweetdb/tweets.db` (schema auto-created by `data/tweetdb/db.py::init_db()` — import and call it; never hand-write CREATE TABLE).
- Tables:
  - `accounts(handle UNIQUE, name, fetched_at)` — upsert one row per handle, update `fetched_at` each run.
  - `tweets(account_id FK, tweet_id UNIQUE, text, clean_text, link, pub_date, ist_time)` — `tweet_id` = X status ID as TEXT. `text` = raw; `clean_text` = HTML-stripped via `db.clean_html()`. `pub_date` = UTC timestamp from X; `ist_time` = Asia/Kolkata (+05:30). `UNIQUE(account_id, tweet_id)` — use `INSERT OR IGNORE`.
  - `tweets_fts(tweet_id, account_handle, clean_text)` — FTS5; insert matching row for every new tweet so search keeps working. Tokenizer: `unicode61 remove_diacritics 2`.
- `feeds` table: read-only for you. `enabled=0` = skip that handle.

## Rules
1. `INSERT OR IGNORE` everywhere — duplicates are a contract violation, not a minor bug.
2. Never modify `tweet2learnings.py`, the checkpoint file (`~/.hermes/tweet_learnings_checkpoint.txt`), or anything under `~/ObsidianVault/`. Those are downstream.
3. Never commit without Rocky's explicit go-ahead (repo rule).
4. If X rate-limits or blocks: back off, log to `data/scrape_output.log`, resume next cycle. Report blocks to Rocky instead of hammering.
5. Verify each run: print `accounts scraped / new tweets inserted / skipped duplicates`, and confirm with `SELECT COUNT(*)` before/after.

## Test protocol (before full runs)
Scrape 5–10 accounts only, show Rocky the inserted-row counts, wait for his confirmation. Then scale to full 536 on the 6-hour cadence.
