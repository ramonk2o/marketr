---
name: research
description: Researches a client's end customers and competitors from evidence. Customers - what they say in reviews, support and WhatsApp chats, sales calls, cancellation reasons, comments, forums and searches (pains, desires, triggers, objections, awareness, their literal words). Competitors - what they offer and promise, what their customers praise and complain about, and the gaps nobody covers. Use it to build or update icp.md and competitors.md, whenever the user brings customer exports to mine ("pull the pains out of these reviews"), wants to know who really buys or how competitors position, or when those files are stale. Not for recording what the client or team says or processing briefing material (discovery), writing or critiquing a piece of copy, including a single competitor ad (copywrite), defining positioning or tone (branding), or market size.
---

# Research

Requires conventions: 3
Reads: `_in/`, `_knowledge/`, the web (with consent), `${CLAUDE_SKILL_DIR}/references/collect-<target>.md`
Writes: owns `icp.md` and `competitors.md` (company or product level); research collections in `_in/`; appends to `decisions.md`; offers a customer questionnaire in `_out/`

## Rules that always apply

The project's conventions (`.claude/rules/marketr.md`) already apply. These are the points research most often gets wrong, and why they matter:

- If `.claude/rules/marketr.md` is missing, run the marketr setup skill first, then continue. If its conventions version is lower than 3, suggest `/marketr:setup` and stop.
- Read the target's reference (`collect-audience.md` or `collect-competitors.md` in `${CLAUDE_SKILL_DIR}/references/`) and the file's guide in `${CLAUDE_PLUGIN_ROOT}/references/knowledge/` before collecting. If one cannot be read, say which and that the plugin folder needs read access; do not improvise the method from memory.
- Quotes are verbatim. WebFetch summarizes pages and search snippets are cut, so ask WebFetch for exact text, never quote a snippet, and give every quote its URL or file and its posting date. Copywrite puts these words in public copy as the customer's own; a paraphrase passed off as a quote becomes a claim the client has to answer for.
- Never fill a source from memory. List every source you could not reach and what to do instead (an export, a screenshot, a link). An empty section is honest; an invented one misleads every skill that reads it.
- Strip personal data, in the collection file too: replace names, phone numbers, handles, emails and order numbers with `[name]`, `[phone]` and so on, and copy only the excerpts you use, never a whole export. Personal data is useless for copy, the files circulate, and privacy laws (LGPD, GDPR) apply. Use only public data or data the client gave; nothing behind someone else's login.
- Tag whose voice each quote is: client customer, competitor customer (which one) or prospect. They tell different things: the client's reviewers already bought, competitors' customers chose someone else, prospects are still deciding. Mixing them overgeneralizes.
- Separate evidence from inference, and rate evidence by people, not mentions:
  - **strong:** 5 or more people across 2 or more source types;
  - **moderate:** 3 or 4 people, or a single source type;
  - **weak:** 1 or 2 people.

  No percentages under about 30 data points. Prefer the last 24 months. A long, specific review or a 3-star one says more than a 5-star one-liner. One vivid quote can go in literal language but cannot become a pain on its own. Segments and awareness levels are inference: mark them `[hypothesis: inferred from _in/<collection>]` until the client confirms them.
- What the team believed (`[hypothesis: team]`, `[hypothesis: client]`) stays marked until evidence says otherwise. Strong evidence confirms it: remove the marker and keep the support note. Contrary evidence is a contradiction: show both, ask, then update. Log confirmations and rejections in `decisions.md`.
- Keep files lean (about 1,500 tokens): the best evidence goes in the knowledge file, everything else stays in the collection, which `sources` lists.

## 1. Scope

Search `_knowledge/` for `^summary:` and read `company.md`, the products and any existing `icp.md` or `competitors.md`. Then settle, from the request or with a question:
- **Target:** audience, competitors or both; optionally one product, segment or competitor.
- **New or update:** an update uses the existing file as the baseline and looks for what changed.

When products have different buyers or rivals (a course and a subscription), research them separately and write `products/<slug>/icp.md` or `competitors.md`.

## 2. What the client has

The client's own material is the richest source and usually exists. Check `_in/` first, then ask the user for what is missing, using the reference's checklist for the business type and country, with how to export each item. Say early if evidence will be thin, so nobody expects more than the sources can give. Continue with what is reachable; material that arrives later is picked up by an update.

## 3. Plan the collection

List the sources for this scope, saying which ones you can reach and which need the user. Ask consent before searching the web.

With more than about 3 source groups or competitors, use collector subagents:
- Tell the user first: collection takes a while, and each subagent asks for web access, so approving WebSearch and WebFetch for the session saves interruptions.
- Spawn them all in one message, at most 5, `general-purpose`, each with the collector prompt from the reference filled in. The prompt says to return results only: no files, no agents.
- Wait until every collector has reported before synthesizing; a synthesis from part of the evidence reads as complete when it is not.

Stop collecting a theme when about 10 new quotes add nothing new, and say so: that is saturation, and more searching only costs time.

## 4. Save the collection

Write `_in/YYYY-MM-DD_research-<target>-<topic>.md` (slug in the client language), opening with: collected by research, date, scope, quotes verbatim and anonymized. Then the quotes grouped by theme, each with voice, source and date, and the list of sources not reached. Never edit an earlier collection: a new run writes a new file.

## 5. Synthesize and compare

Fill the knowledge file following its guide and the reference's synthesis notes, with the evidence level on each item. Then show the user, per file:
- what the team believed that the evidence confirms, contradicts or cannot judge;
- what is new;
- the evidence behind each.

Write after the user confirms. Add the collection to `sources`, update `updated`, and log confirmations, rejections and strategic findings in `decisions.md`.

## 6. Report

In the team language, short:
- files written or changed;
- the strongest findings, with their evidence level;
- what stays weak or unknown, written as `[question:]` markers in the knowledge file so it reaches the next client meeting;
- sources not reached and how to get them;
- a reminder to spot-check web quotes before using them in public copy;
- the next step: copywrite, or branding to define or rethink the positioning when findings support or contradict a pillar.

When evidence is weak, offer the customer questionnaire from the reference (about 5 questions the client can send to 10 customers on WhatsApp), saved in `_out/` with channel `questionnaire`. Answers dropped in `_in/` feed the next update.
