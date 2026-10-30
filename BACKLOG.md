# Backlog

## In progress

- **discovery:** builds and maintains the client's context from `_in/`, the client's own web presence and an interview with the team member.
  - Description covers first discovery ("anamnesis", "anamnese", onboarding a client), processing new material (call notes, transcripts, files added to `_in/`), changes the user reports ("the client changed X"), and reviewing the knowledge base. It is not for deep audience or competitor research (research) or for defining positioning and tone (branding).
  - Contract. Requires conventions 1. Reads `_in/`, `_knowledge/`. Drafts any missing `_knowledge/` file and owns `company.md`, `marketing.md` and `products/<slug>/product.md`. Appends to `decisions.md`. If `.claude/rules/marketr.md` is missing, runs setup first.
  - Modes:
    - First run: `_knowledge/` is empty. Full flow below.
    - Update: `_in/` has files not listed in any `sources`, or the user brings new information. Short path: read only what is new, show what it changes in each file (contradictions with both versions and sources), confirm, write, log. No interview beyond what the new material leaves unclear.
    - Scope: the user names a product or topic; touch only that.
    - Review, on request: contradictions between files, files over ~1,500 tokens, headings that break the override rule, past-due goals in `marketing.md`, old unconfirmed hypotheses. Ends with the meeting agenda.
  - Permanent rules at the top of SKILL.md, the detailed flow after.
  - Uses the shared guides in `references/knowledge/` (plugin root) for every file it drafts. They are created with this skill, one per `_knowledge/` file.
  - Full flow:
    1. Inventory `_in/`, read everything readable, say what could not be read.
    2. With the user's consent, look up the client's own web presence (site, social profiles, reviews). Record each URL in `sources`. Researching competitors is not part of this skill.
    3. Show a short summary of what is known, inferred and missing, before asking anything.
    4. Interview in blocks: company → products → customers → market and cited competitors → brand → goals, marketing and restrictions.
       - 3 to 5 questions at a time, in the team language, only about what is missing.
       - "I don't know" is a valid answer: it becomes `[question:]` or `[hypothesis:]`.
       - Any block can be skipped.
       - For a new company, questions become options proposed with reasoning. The user chooses, and the choice is logged as a decision.
    5. Write at the end of each block, so an interrupted session loses nothing. Running again resumes from the files and the `[question:]` markers.
    6. Close with a short report:
       - what was written;
       - the number of hypotheses and open questions;
       - the agenda for the next client conversation, from the `[question:]` markers;
       - the suggested next skill.

       Offer, without doing it by default, a questionnaire for the client in `_out/`, in the client language.

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

- Skill contract, introduced with discovery: every SKILL.md except setup opens with `Requires conventions: N`, `Reads: ...`, `Writes: ...` and "if `.claude/rules/marketr.md` is missing, run setup first". Add to the Ship step in `.claude/CLAUDE.md`: on a conventions bump, grep "Requires conventions" and review each skill.
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
