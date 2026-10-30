# {{CLIENT_NAME}}: marketing project

Managed by the marketr plugin. Conventions version: 1.
`/marketr:setup` overwrites this file on upgrade. Put project-specific notes in `CLAUDE.md`, never here.

## Languages

- Team language: {{TEAM_LANGUAGE}}. Write `decisions.md` in it. Talk to each user in the language they write in.
- Client language: {{CLIENT_LANGUAGE}}. Write all content of `_knowledge/` and `_out/` in it, including headings and `_out/` filenames.
- English: instructions, the fixed folder and file names below, frontmatter keys and values.
- Slugs (product folders, `_out/` filenames) follow the client language, written in lowercase ASCII with hyphens, no accents: `cafe-assinatura`, not `café-assinatura`.

## Folders

- `_in/`: raw material from the client (PDFs, screenshots, briefings, call notes). Read only: never edit, move or delete.
- `_knowledge/`: curated, durable knowledge about the client. The source every skill reads.
- `_out/`: deliverables.
- `decisions.md`: append-only history of decisions. To check the current state, read `_knowledge/`; search `decisions.md` for a term instead of reading it whole.

## Knowledge

```
_knowledge/
  company.md        who the client is, history, current position, strengths
  brand.md          tone of voice, personality, verbal identity
  competitors.md
  icp.md            ideal customer
  products/<slug>/
    product.md      what it is, price, differentiators, objections
    positioning.md
```

- Any company-level file can also exist in `products/<slug>/` with the same name. Read the company file first, then the product's: the product file overrides where they conflict and complements the rest.
- To find what exists, search `_knowledge/` once for `^summary:`. Read full files only when needed.
- Every file starts with:
  ```
  ---
  summary: one line
  updated: YYYY-MM-DD
  sources: [_in/<file>, https://...]
  ---
  ```
- `company.md` has a section for restrictions: forbidden claims, legal and regulatory limits, words to avoid.
- Every `product.md` has a section for proof: numbers, cases, testimonials, certifications. Real ones only, each with its source.
- Inline markers, the same in every language:
  - `[hypothesis: <origin>]` after anything the client has not confirmed (inferred from material, suggested by Claude, user's guess).
  - `[missing: <what>]` where information is needed but unknown. Never invent proof, numbers, testimonials or claims; leave this marker instead.
  - `[question: <what to ask the client>]` for open questions. Search for `[question:` to build the agenda for the next client conversation.
- Temporary information (offers, campaigns, deadlines) belongs in the deliverable's brief, never in `_knowledge/`.
- When a skill reads `competitors.md` or an `icp.md` whose `updated` is older than 6 months, warn the user. Do not warn about other files.

## Deliverables

- `_out/` is flat. Filename: `YYYY-MM-DD_<product-slug>_<channel>-<topic>_v<N>.md` (drop the product slug when company-wide). Example: `2026-10-30_cafe-assinatura_email-lancamento_v1.md`.
- A new version is a new file with `v<N+1>`. Never overwrite an earlier version.
- Every deliverable starts with:
  ```
  ---
  status: draft | approved
  product: <slug> | company
  channel: <channel>
  ---
  ```
  followed by a short brief: objective, offer, deadline, mandatory items, hypotheses the copy relies on.
- Keep formatting light so it pastes cleanly into Google Docs or WhatsApp: no tables, no nested lists.

## Decisions and feedback

- Append to `decisions.md` as `## YYYY-MM-DD: <title>`, then what was decided, why, and which files changed.
- Log without being asked when the user approves a strategic choice (positioning, angle, big idea, tone), when a hypothesis is confirmed or rejected, and when feedback becomes a permanent rule.
- When the user relays client feedback, ask whether it is a one-off or a permanent rule. If permanent, record it in the relevant `_knowledge/` file.
- A decision that changes knowledge updates the `_knowledge/` file and is logged. Always both.

## Skills

- If a needed `_knowledge/` file is missing, say so and offer the marketr skill that produces it, or proceed with hypotheses flagged in the deliverable.
- If a marketr skill expects a higher conventions version than this file's, suggest running `/marketr:setup` to upgrade.
