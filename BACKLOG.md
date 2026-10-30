# Backlog

## In progress

## Next

- **copywrite:** writes for any channel using `_knowledge/`.
  - Planning depth proportional to the channel: direct (SMS, push, subject lines), brief (posts, nurture emails, long ads), full (landing pages, sales emails, VSL).
  - The structure approval in full mode is a pause for the user, not a mandatory client approval.
  - Modes: write; revise one of our pieces from feedback (new `v<N+1>`); review a text from someone else; adapt one piece into others.
  - Reads the campaign brief when a piece belongs to one.
  - One reference file per channel, loaded on demand. Choose the first two channels.
  - Fixed English channel ids, defined by the channel references, used in both frontmatter and `_out/` filenames; the topic stays in the client language. Settle before its first release (no `_out/` exists yet, so no migration).
  - Move the "light formatting" rule from the conventions template to the channel references.

## Ideas

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
