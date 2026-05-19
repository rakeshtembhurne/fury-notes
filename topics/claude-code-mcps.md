---
created: 2026-05-19
tags: [claude-code, mcp, tools, ai, coding]
source: "YouTube transcript — Sean Matthew"
---

# 3 Must-Have MCPs for Claude Code

## Key Insights

- **Supabase MCP automates database setup entirely** — No more copy-pasting SQL from the Supabase dashboard into the browser. Claude Code can create tables, set up Row Level Security (RLS), configure environment variables, and add sample data directly via the MCP. This cuts out the middleman workflow completely.

- **Clerk MCP streamlines authentication** — Clerk handles sign-in flows (Google, Apple, MFA) that are complex to build from scratch. The MCP automates the entire setup including the email verification loop. You provide the secret key, Claude Code handles the rest.

- **Smar MCP provides free automated security scanning** — With 2,000+ vulnerability signatures, it scans codebases for XSS, SQL injection, and other common bugs. Useful post-implementation before production deployment. Note: requires pinning `fastmcp` to an older version due to a dependency conflict.

- **All three MCPs have generous free tiers** — Supabase, Clerk, and Smar can all be used without paying. Only Supabase MCP requires an access token (generated from their website); Clerk uses the existing agent toolkit package via a local MCP server wrapper.

- **Restart Claude Code after installing any MCP** — New MCP servers are not detected until Claude is restarted. Use `/mcp` to verify installed MCPs.

## Summary

Three essential backend MCPs for Claude Code: Supabase (database), Clerk (auth), and Smar (security). Together they automate the most tedious parts of app development — backend setup, user authentication, and vulnerability scanning — directly from the terminal without switching to a browser dashboard.
