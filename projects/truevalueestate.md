---
title: "TrueValueEstate"
date: 2026-03-21
tags:
  - project/truevalueestate
type: project
domain: PropTech
status: 🟡 In Development
---

# TrueValueEstate.com

## Project Overview

Professional property valuation software for valuers in India. Create accurate valuation reports for land, flats, and buildings with comprehensive valuation algorithms, incentive factors, multi-format reports, and approval workflows.

## Domain

- truevalueestate.com
- support@truevalueestate.com

## Tech Stack

- **Framework:** Next.js (App Router + Turbopack)
- **Runtime:** Bun
- **Auth:** Better Auth
- **Database:** PostgreSQL + Prisma ORM
- **Email:** React Email
- **Deployment:** Docker/Podman containerized
- **Content:** Contentlayer
- **Dev Tools:** Husky (git hooks), ESLint, Prettier

## Core Features

### Valuation Engine
Three core valuation methods:
1. **Market Comparison** — For residential properties (comparable sales approach)
2. **Income Capitalization** — For rental/investment properties
3. **Cost Approach** — For new constructions

### Report Types
- Land valuation
- Flat/apartment valuation
- Building valuation
- Multi-format PDF reports with company branding

### Valuation Factors
| Factor | Impact |
|--------|--------|
| Property Demarcated | +2% |
| Property Merged/Colluded | -5% |
| Metro Location | 1.5x multiplier |
| Urban Location | 1.3x multiplier |
| Semi-Urban | 1.1x multiplier |
| Main Road Position | 1.2x multiplier |
| Corner Position | 1.15x multiplier |

### Workflow
- Dashboard for report management
- Approval workflows
- Report generation and export

## Project Structure

```
truevalueestate.com/
├── app/                    # Next.js app (auth, dashboard, marketing, protected routes)
├── config/                # Site configuration (landing, dashboard, marketing, blog)
├── api/                   # API routes
├── emails/                # React Email templates
├── podman/                # Container configuration
├── prisma/                # Database schema
├── types/                 # TypeScript types
└── valuation.md           # Valuation algorithm question bank

## Research & Sources

See `RESEARCH_SOURCES.md` for Indian property valuation methodology sources:
- RBI/banking guidelines
- IBBI standards
- RERA compliance requirements
- Real estate industry best practices
- Tax and depreciation standards

## Status

🟡 In Development — Core valuation engine and reporting built

## Next Steps

- [ ] Complete valuation form workflow
- [ ] Add more comparable property data
- [ ] Build approval workflow
- [ ] Add more report templates
- [ ] Production deployment

## Related

- [[Projects/]] — All projects
- [[_MOCs/WorkMOC|Work MOC]]
