# Backlog

## In progress

## Next

- **anamnesis:** builds the client's context from `_in/` and an interview.
  - Writes `company.md` and `products/<slug>/product.md` (+ `positioning.md`).
  - Runs setup first when the folder is not a marketr project.
  - Works with missing information: new companies (it defines rather than documents, and logs choices as decisions), unavailable info (looks up the web where possible), hypotheses marked, open questions listed.
  - Writes a provisional `brand.md` with the tone inferred from existing material, marked as hypothesis.
  - Decide here whether ICP is a section of anamnesis or a skill of its own.
  - Introduce the skill contract: every SKILL.md except setup opens with `Requires conventions: N`, `Reads: ...`, `Writes: ...` and "if `.claude/rules/marketr.md` is missing, run setup first". Add to the Ship step in `.claude/CLAUDE.md`: on a conventions bump, grep "Requires conventions" and review each skill.
- **copywrite:** writes for any channel using `_knowledge/`.
  - Planning depth proportional to the channel: direct (SMS, push, subject lines), brief (posts, nurture emails, long ads), full (landing pages, sales emails, VSL).
  - The structure approval in full mode is a pause for the user, not a mandatory client approval.
  - Modes: write, review a given text, adapt one piece into others.
  - One reference file per channel, loaded on demand. Choose the first two channels.
  - Fixed English channel ids, defined by the channel references, used in both frontmatter and `_out/` filenames; the topic stays in the client language. Settle before its first release (no `_out/` exists yet, so no migration).
  - Move the "light formatting" rule from the conventions template to the channel references.

## Ideas

- competitors: web research on competitors, writes `competitors.md`. If it uses a subagent, use `general-purpose`: Explore and Plan do not load the project's rules.
- branding: tone of voice, personality, verbal identity, writes `brand.md`.
- icp: only if anamnesis does not cover it well.
- Per-deliverable language override (client with more than one market).
- With the first migration: move setup's "Migrations" to `skills/setup/references/migrations.md`, read only when upgrading.
- With three skills: a few `claude plugin eval` cases on `example/` instead of manual retests.
- A PreToolUse hook blocking writes to `_in/`, only if the rule is broken in practice.
