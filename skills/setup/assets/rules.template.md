# {{CLIENT_NAME}}: marketing project

Managed by the marketr plugin. Conventions version: 2.
`/marketr:setup` overwrites this file on upgrade. Put project-specific notes in `CLAUDE.md`, never here.

## Languages

- Team language: {{TEAM_LANGUAGE}}. Write `decisions.md` in it. Talk to each user in the language they write in.
- Client language: {{CLIENT_LANGUAGE}}. Write all content of `_knowledge/` and `_out/` in it, including headings and `_out/` filenames.
- English: instructions, the fixed folder and file names below, frontmatter keys and values (`summary` included).
- Slugs (product folders, `_out/` filenames) follow the client language, written in lowercase ASCII with hyphens, no accents: `cafe-assinatura`, not `café-assinatura`.

## Folders

- `_in/`: raw material from the client and the team's own notes and call transcripts. Name new files with a date prefix: `2026-10-30_call-kickoff.md`. Read only: never edit, move or delete.
- `_knowledge/`: curated, durable knowledge about the client. The source every skill reads.
- `_out/`: deliverables.
- `decisions.md`: append-only history of decisions. To check the current state, read `_knowledge/`; search `decisions.md` for a term instead of reading it whole.

## Knowledge

Each file answers one question and has one owner skill that deepens it. Any skill may draft a missing file; the owner deepens that same file. Information that fits two files goes in the one whose question it answers; the other points there and never copies it.

| File | Question | Owner | Sections |
|---|---|---|---|
| `company.md` | who we are | discovery | what it does, business model, size and stage, history (facts), portfolio and offer architecture, restrictions (legal, regulatory, forbidden claims and words), institutional proof |
| `icp.md` | who buys | research | segments, decision maker and influencers, pains, desires, triggers, objections (in the customer's words, no answers), awareness level, where they are, literal language |
| `competitors.md` | against whom | research | direct competitors, alternatives (including doing nothing), comparison, how they position, gaps |
| `positioning.md` | why us | branding | category, for whom, main difference, reason to believe, core promise, message pillars |
| `brand.md` | how we speak | branding | personality, tone by context, vocabulary (use, avoid for style), told story, right and wrong examples |
| `channels.md` | how we do each channel | copywrite | one section per channel in use: format (length, blocks, CTAs), conventions (emojis, hashtags, signature), tools and their constraints, client rules |
| `marketing.md` | what we do and what worked | discovery | dated goals with KPIs, budget, approvers, journey and sales process, channels and their state, what was tested and results, recurring seasonality, asset inventory (what and where, not the content) |
| `products/<slug>/product.md` | what we sell (products or services) | discovery | what it is, mechanism, transformation, segment served (pointing to `icp.md`), price, format and guarantee, how it is bought, attributes, product proof, answers to objections |

- Sections are a checklist, not mandatory headings: write a section only when there is content. Unknowns become `[question:]` markers.
- Write headings in the client language, using the same heading for the same section everywhere.
- Any company-level file can also exist in `products/<slug>/` with the same name. Read the company file, then the product's: a product section replaces the company section with the same heading; other sections are inherited. A product file copies the company file's heading literally; if the company file lacks that section, add it there first.
- Keep each file under about 1,500 tokens.
- To find what exists, search `_knowledge/` once for `^summary:`. Read full files only when needed.
- Every file starts with:
  ```
  ---
  summary: one line
  updated: YYYY-MM-DD
  sources: [_in/<file>, https://..., interview YYYY-MM-DD]
  ---
  ```
- Proof is real only, each item with its source.
- Inline markers, the same in every language:
  - `[hypothesis: <origin>]` after anything the client has not confirmed (inferred from material, suggested by Claude, team). What the team says about the client's customers or market is `[hypothesis: team]` until the client or research confirms it.
  - `[missing: <what>]` where information is needed but unknown. Never invent proof, numbers, testimonials or claims; leave this marker instead.
  - `[question: <what to ask the client>]` for open questions. Search for `[question:` to build the agenda for the next client conversation.
- New information that contradicts `_knowledge/` never overwrites it silently: show both versions with their sources, ask the user, then update and log.
- Temporary information (offers, campaigns, deadlines) belongs in a brief, never in `_knowledge/`.
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
  `channel` is a fixed English id: `push`, `sms`, `email`, `web`, `post`, `video`, `google-ads`, `meta-ads`, or `brief` and `questionnaire`. It is followed by a short brief: objective, offer, deadline, mandatory items, hypotheses the copy relies on.
- A campaign with several pieces gets its own brief file in `_out/` with channel `brief` (`2026-11-01_cafe-assinatura_brief-black-friday_v1.md`). Its pieces point to it instead of repeating it, and keep only what is specific to them.
- When the user says the client approved a piece, set `status: approved` and log it. Offer to add it to `brand.md` as an example of the right tone.
- Keep formatting light so it pastes cleanly into Google Docs or WhatsApp: no nested lists, and tables only where the format needs one (ad assets with character counts, a video script by time).

## Decisions and feedback

- Append to `decisions.md` as `## YYYY-MM-DD: <title>`, then what was decided, why, and which files changed.
- Log without being asked when the user approves a strategic choice (positioning, angle, big idea, tone), when a hypothesis is confirmed or rejected, and when feedback becomes a permanent rule.
- When the user relays client feedback, ask whether it is a one-off or a permanent rule. If permanent, record it in the relevant `_knowledge/` file.
- A decision that changes knowledge updates the `_knowledge/` file and is logged. Always both.

## Status and meetings

- Project status: the `summary` of each `_knowledge/` file, deliverables with `status: draft`, and the latest entries of `decisions.md`.
- Agenda for the next client meeting: the `[question:]` markers, the `[hypothesis:]` markers worth validating, and deliverables awaiting approval.

## Skills

- If a needed `_knowledge/` file is missing, say so and offer the marketr skill that produces it, or proceed with hypotheses flagged in the deliverable.
- If a marketr skill expects a higher conventions version than this file's, suggest running `/marketr:setup` to upgrade.
