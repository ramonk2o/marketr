# Backlog

## In progress

## Next

## Ideas

- campaign planning: multichannel plan and content calendar. Copywrite writes the pieces of a plan; it does not decide what to publish when.
- results analysis: reads piece and campaign metrics and records what worked in `marketing.md`.
- Split short-video scripts into their own skill if scenes and production notes outgrow copywrite.

- research: one skill, one reference per target. Shares sources, collection dates, evidence quality and staleness.
  - Audience: voice of customer from customer data, reviews, comments and forums; segmentation; awareness levels. Interview and survey scripts for real customers as a section. Deepens `icp.md`.
  - Competitors: web research. Deepens `competitors.md`.
  - Subagents must be `general-purpose` with `context: fork` and a self-contained prompt: Explore and Plan do not load the project's rules.
  - Bring forward `claude plugin eval` trigger tests (grader `tool_used: Skill`) with this skill: it is the first that can collide with discovery.
- branding: positioning, tone of voice, personality, verbal identity. Deepens `positioning.md` and `brand.md`. Can run only the positioning part.
- When a second skill interviews the user (research or branding), move discovery's interview mechanics to `references/interview.md`.
- Per-deliverable language override (client with more than one market).
- With the first migration: move setup's "Migrations" to `skills/setup/references/migrations.md`, read only when upgrading.
- A PreToolUse hook blocking writes to `_in/`, only if the rule is broken in practice.
