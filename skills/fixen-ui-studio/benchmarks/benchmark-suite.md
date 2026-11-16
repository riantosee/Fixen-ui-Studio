# Fixen Design Arena — Benchmark Suite

## Purpose
Evaluate whether a skill consistently produces distinctive, usable, responsive, and implementable interfaces across varied product categories.

## Fairness protocol
For every compared agent, keep constant:
- Exact brief and supplied assets
- Repository starter and dependency versions
- Model/tool access where possible
- Viewports and browser
- Time or token budget
- Evaluation rubric and reviewer instructions

Run each case at least twice for high-variance systems. Blind reviewers to agent identity where practical. Record tool availability and failures.

## Benchmark cases

### B01 — Boutique architecture studio
Create an editorial portfolio landing page with project storytelling, strong typography, restrained palette, and inquiry conversion. Avoid generic agency templates.

### B02 — Operational logistics dashboard
Design a dense desktop dashboard for dispatchers monitoring deliveries, exceptions, and delayed shipments. Prioritize scan speed and actionable exceptions.

### B03 — Personal finance mobile app
Create a mobile-first spending overview with understandable categories, privacy-aware language, accessible chart alternatives, and clear empty states. Do not imply financial advice.

### B04 — Independent bookstore ecommerce
Build a discovery-focused storefront with editorial recommendations, genre navigation, product details, and trustworthy checkout cues.

### B05 — Developer API documentation
Create a documentation interface with navigation, readable code examples, version context, search, and responsive behavior.

### B06 — Premium skincare product page
Create a product page emphasizing ingredients, evidence, usage, imagery, and purchase clarity without unsupported medical claims.

### B07 — Community event platform
Design event discovery and event details with filters, location/time clarity, accessible booking flow, and useful empty states.

### B08 — Restaurant reservation management
Create an operator dashboard for table status, reservations, waitlist, and service notes. Make time-sensitive information easy to scan.

### B09 — Cybersecurity incident console
Design a high-density incident triage interface with severity, timeline, affected assets, evidence, and safe action confirmation.

### B10 — Creative portfolio
Build a memorable portfolio for a multidisciplinary creative with case studies, process, contact, and accessible navigation.

### B11 — Learning management system
Create a student dashboard showing course progress, upcoming work, feedback, and continuation actions without gamification clutter.

### B12 — Travel itinerary planner
Design a responsive itinerary with day grouping, transport transitions, booking details, and disruption states.

### B13 — SaaS onboarding
Create a short onboarding flow with progress, useful defaults, validation, skip behavior, and clear value explanation.

### B14 — Healthcare appointment portal
Design an accessible appointment booking experience with clear dates, provider details, privacy-conscious content, and error recovery. Do not make medical claims.

### B15 — Music discovery experience
Create a discovery interface with editorial curation, filters, player states, and strong media hierarchy. Do not use copyrighted audio assets unless supplied/licensed.

### B16 — Real estate listing detail
Build a property detail page with gallery, key facts, map placeholder only if actual map data is unavailable, inquiry actions, and transparent costs.

### B17 — Internal HR leave management
Create a workflow-focused interface for leave requests, balances, approvals, and audit context with role-aware actions.

### B18 — Nonprofit donation campaign
Create a trustworthy campaign page with impact explanation, transparent donation choices, recurring donation clarity, and accessible forms.

### B19 — Mobile field-service app
Design a task-oriented interface for technicians working outdoors, considering large touch targets, low-connectivity states, and quick status updates.

### B20 — Data analytics report
Create a report interface with clear chart labels, units, date ranges, annotations, and a readable narrative—not decorative charts.

## Required deliverables per case

For the optional image-sourcing branch, also use `benchmarks/asset-sourcing-cases.md`. Those checks distinguish discovery, source verification, visual review, and actual integration; they do not require a page build for a shortlist-only brief.

- Design Blueprint
- Implemented interface (unless the case is explicitly concept-only)
- Desktop and mobile render evidence when tools permit
- QA report and known limitations
- Score with evidence and coverage

## Aggregate reporting
Report mean score, median, range, case-by-case results, tool failures, and repeat-run variance. Do not present one high-scoring case as proof of universal superiority.

