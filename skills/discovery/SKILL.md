---
name: discovery
description: Builds and maintains a client's marketing knowledge base (_knowledge/) from the material in _in/, the client's own web presence and an interview with the team. Use it for a client's first discovery or onboarding (also called anamnesis or anamnese), whenever new material arrives (call notes, meeting transcripts, briefings, files dropped in _in/), whenever the user mentions that something about the client changed (prices, products, goals, people), and to review or audit what is known about the client. Use it even when the user just says "process this", "the client sent new stuff" or "let's get to know this client". Not for mining what end customers say (reviews, support chats, comment exports) or studying competitors (research), or for defining positioning and tone of voice (branding).
---

# Discovery

Requires conventions: 1
Reads: `_in/`, `_knowledge/`, the client's own web presence (with consent)
Writes: drafts of any missing `_knowledge/` file; owns `company.md`, `marketing.md`, `products/<slug>/product.md`; appends to `decisions.md`

## Rules that always apply

The project's conventions (`.claude/rules/marketr.md`) already apply. These are the points discovery most often gets wrong, and why they matter:

- If `.claude/rules/marketr.md` is missing, run the marketr setup skill first, then continue. If its conventions version is lower than 1, suggest `/marketr:setup` and stop.
- Before writing a `_knowledge/` file, read its guide in `${CLAUDE_PLUGIN_ROOT}/references/knowledge/` (`product.md` for any product file). The guides keep files consistent across clients and skills.
- Write what you learn at the end of each block or step. Sessions get interrupted or compacted; what is only in the conversation is lost.
- Each fact lives in one file, the one whose question it answers; other files refer to it. Copies drift apart at the first update: a price repeated in `company.md` stays wrong after the product's price changes.
- The knowledge base is evidence for everything other skills will write, so it must not overstate. Quotes are literal, with no words added. Facts without a source in `_in/` or the web came from the interview: add `interview YYYY-MM-DD` to `sources`.
- Use absolute dates ("since 2026-07"). Relative ones ("3 months ago") become wrong without anyone noticing.
- Frontmatter is in English, `summary` included: it is the index other skills search. Only the body follows the client language.
- Summarize, do not transcribe: about 1,500 tokens per file, because other skills read several files at once.
- Files owned by another skill (`icp.md`, `competitors.md`, `positioning.md`, `brand.md`) may hold its deeper work. Add new information with its source, and ask before rewriting anything already there.

## 1. Choose the mode

Search `_knowledge/` for `^summary:` and `^sources:`, and list `_in/`. Then pick the mode; if the user's request already says what they want, follow it.

- **First run:** `_knowledge/` is empty, or a first run was interrupted (some files from step 2.4 are missing). Go to 2, skipping what is done.
- **Update:** `_in/` has files no `sources` lists, or the user brings new information. Go to 3. Skip `_in/*_research-*` files: they are what customers and competitors say, gathered by research, and reading them as client statements would put a reviewer's words in the client's mouth.
- **Scope:** the user names one product or topic. Run only the matching part of 2 or 3.
- **Review:** the user asks to review or audit the knowledge base. Go to 4.

## 2. First run

1. **Read the material.** Read every file in `_in/`, images included. List what you could not read and why.
2. **Web presence.** Ask whether to look up the client's own site, social profiles and reviews, and for the addresses if the material does not give them. Fetch only with consent, and add each URL to `sources`. Do not research competitors.
3. **Show what you understood**, before asking anything: per block below, a few lines on what is known, what you inferred, and what is missing. Ask the user to correct it.
4. **Interview in blocks**, in this order. Each block writes its files before the next starts.

   | Block | Writes |
   |---|---|
   | Company | `company.md` (with portfolio and restrictions) |
   | Products and services | `products/<slug>/product.md` for each one |
   | Customers | draft `icp.md` |
   | Market and competitors | draft `competitors.md` |
   | Brand and positioning | draft `brand.md`; draft `positioning.md` only from clear client statements or a choice made in this interview |
   | Goals and marketing | `marketing.md` |

   - Ask 3 to 5 questions at a time, only about what is missing: the user's time is the scarce resource. Prefer concrete questions ("what does a customer usually ask before buying?") over abstract ones ("what is your value proposition?"); people answer the first well and the second with clichés.
   - If an answer belongs to another block, record it there anyway.
   - "I don't know" is a valid answer: record it as `[question:]`, or as a hypothesis if the user offers a guess.
   - The user can skip any block. Note it in the report.
   - For a new company, where there is nothing to document yet, turn decisions into 2 or 3 options with your reasoning. The user chooses; log the choice in `decisions.md`.
5. **Close** with the report (section 5).

## 3. Update

1. Read only what is new: the unlisted files in `_in/`, or what the user said.
2. Show, per `_knowledge/` file, what would change: additions, and contradictions with both versions and their sources.
3. Ask only about what the new material leaves unclear. Confirm the changes.
4. Write, add the new sources, update `updated`, and log in `decisions.md` anything that changes a fact or confirms or rejects a hypothesis.
5. Close with the report, shortened to what changed.

## 4. Review

Check and list, file by file:
- contradictions between files, and information copied instead of pointed to;
- files over about 1,500 tokens;
- product headings that do not match the company file's;
- goals in `marketing.md` whose date has passed;
- hypotheses older than 3 months (by the file's `updated`).

Propose fixes and apply only the ones the user accepts. End with the agenda for the next client meeting.

## 5. Report

In the team language, short:
- files written or changed;
- how many hypotheses and open questions remain, and which blocks were skipped;
- the agenda for the next client conversation: the `[question:]` markers, grouped by topic;
- the suggested next step (another block, research, branding, or producing work).

Then offer, without doing it by default, a questionnaire to send the client: the open questions rewritten for the client in the client language, grouped and in plain words. Save it in `_out/` with channel `questionnaire`.
