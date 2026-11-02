---
name: branding
description: Defines and maintains how a client's brand wants to be seen and how it speaks. Positioning (positioning statement, what the brand is and is not, message pillars, the lead pillar per segment) in positioning.md, and tone of voice (personality, signature moves, tone by context, vocabulary, right and wrong examples) in brand.md, as options the team picks and a short strategy page the client approves. Use it to define, choose, rethink or review positioning, differentiation, value proposition, brand personality or voice ("how should the brand talk?", "why would anyone pick us over the competition?"), including after new research or a change at the client, and to record the client's approval of a strategy page. Not for recording what the client said (discovery), customer or competitor evidence (research), taglines, slogans, headlines or the voice of a single piece (copywrite), naming or visual identity.
---

# Branding

Requires conventions: 4
Reads: `_knowledge/` (company and product level), `_in/`, `decisions.md`, strategy pages and approved pieces in `_out/`, the guides in `${CLAUDE_PLUGIN_ROOT}/references/knowledge/`
Writes: owns `positioning.md` (company or `products/<slug>/`) and `brand.md`; strategy pages in `_out/`; interview facts in `company.md`, `product.md` and `icp.md`; `[question:]` markers in `product.md`; appends to `decisions.md`

## Rules that always apply

The project's conventions (`.claude/rules/marketr.md`) already apply. These are the points branding most often gets wrong, and why they matter:

- If `.claude/rules/marketr.md` is missing, run the marketr setup skill first, then continue. If its conventions version is lower than 4, suggest `/marketr:setup` and stop.
- Before writing `positioning.md` or `brand.md`, read its guide in `${CLAUDE_PLUGIN_ROOT}/references/knowledge/`. The guides hold the format copywrite reads.
- Positioning is a decision, not something to prove. Nobody can prove a positioning right in advance, and collecting proof is rarely viable for small clients. Use what the project already has; the client's approval is what makes the choice current.
- Every claim the client will see must be checkable as written against the project's files: "cheaper than A and B once shipping is counted", not "most subscriptions charge shipping". The client repeats it to customers, and one false comparison costs the trust the positioning is built on.
- Keep it fast: about 30 to 45 minutes of the agency's time, one round of questions and one touch with the client. Every extra round is time a small client does not pay for. When positioning and voice run in the same session, send one page.
- Write what the interview taught you into its files before proposing options. Options are cheap to regenerate; answers are not, and sessions get interrupted.
- The client sees one recommendation, not a menu. A business owner shown three options freezes or mixes them; options help the team decide. The exception is voice delegated to Claude (step 3).
- The team often answers on the client's behalf. Accept it and mark those answers `[hypothesis: team]`; the strategy page is where the client confirms them.
- A file counts as approved only when a `strategy` page with `status: approved` proposes it and does not list it as `Rejected:`. Discovery's drafts and the team's choices may carry no marker and still be unapproved.

## 1. Where are we

Search `_out/` for `_strategy-` files. Per topic, only the highest `v` counts; a lower version is superseded and needs no answer.
- **The request is about a pending page** (the client answered, approved, rejected): approved or approved with changes, apply it as the conventions say, then search `positioning.md` and `brand.md` for any wording the client replaced. Rejected: if it was a rethink, restore the parts it changed from the last approved page, which is the client's current agreement, and log it. Rejected or no answer: offer to rework it into the next version of that topic.
- **Otherwise:** mention any pending page in one line and go to the mode the request names: positioning (2) or voice (3). Voice can run before the positioning is approved; say that it may need redoing if the positioning changes, because the voice expresses it.

If `icp.md` or `competitors.md` is missing, or no `_in/*_research-*` file appears in its `sources` (discovery's draft only), say so and offer research first. If the user goes ahead, which is the normal path for a new company, proceed and keep the result `[hypothesis: team]`.

## 2. Positioning

Company level by default; product level (`products/<slug>/positioning.md`) only when that product has its own `icp.md` or `competitors.md`.

1. **Read** `company.md`, the products, `icp.md` and `competitors.md` (company and product level), `marketing.md` (what worked) and `decisions.md`. If `positioning.md` uses sections that are not in the guide, restructure it to the guide and show the user. If the file is approved, this is a rethink: show per pillar what new evidence or changes confirm or contradict, propose options only for what changed, and mark only the changed parts `[hypothesis: team]`.
2. **Today:** for an existing company, describe in 3 lines how it positions itself now, from what it says (site, material in `_in/`) and what `icp.md` says customers value. Skip for a new company.
3. **Interview:** one round; pick 4 or 5 of these, skipping what the files already answer. Concrete questions get concrete answers; "what do you want to be remembered for?" gets clichés.
   - Think of your best customer in the last few months: who are they, why did they buy, what did they say afterwards?
   - When someone almost bought and did not, why? What did they do instead?
   - What do you do that seems obvious to you but competitors do not do or do not tell anyone?
   - Which customers do you not want more of? (It feeds "we are not".)
   - What would you promise in writing, with a guarantee?
   - What would you hate a customer to say about you?

   "I don't know" is a valid answer: record it as `[question:]`. Then write the facts learned into `company.md`, `product.md` or `icp.md` with source `interview YYYY-MM-DD`.
4. **Options for the team:** 2 or 3. First name the main alternative the customer would pick instead, from `competitors.md` and the interview: often not a competitor but doing it themselves, the supermarket or doing nothing. Each option has the positioning statement (shape in the guide), with the difference stated against that alternative and the "because" fact proving that same difference; the facts behind it; a sample headline; one pro and one con; and one line on three questions: do customers care, can the client sustain it, does it pass the swap test against each competitor in `competitors.md` by name. When nothing sharper holds, one option is the obvious choice executed well, with 2 or 3 concrete executions. Recommend one and say why.
5. **Write** what the team picks into `positioning.md`, following the guide, as `[hypothesis: team]`, and log the choice. Offer problems found along the way (no guarantee when the main objection is risk, a price that does not fit the segment) become `[question:]` in `product.md`: the offer is the client's decision, not branding's.
6. **Strategy page:** if voice runs in this session, do step 3 first and write one page for both. Otherwise `_out/YYYY-MM-DD_strategy-<topic>_v<N>.md` (product slug when product level; topic in the client language, such as `posicionamento`; v1, or the next version of that topic), `status: draft`, `Proposes:` the file or files it changes. In the client language and plain words, about 150 to 250 words, pasteable into WhatsApp (short lines, bold only, no tables):
   1. how we want people to remember the brand: one short line that carries the lead pillar, or says why it does not;
   2. who we are talking to, in one line;
   3. why people will believe it: 3 facts the client already has, checkable as written;
   4. what changes: what we will say more, what we will stop saying;
   5. before and after of one real piece (Instagram bio, site headline, WhatsApp greeting); ask the user for one if `_in/` has none;
   6. two sample lines in the voice, if it is defined;
   7. what this asks of you: what the client must keep doing for the promise to hold (name the producer on every lot, keep the free shipping threshold);
   8. a closing question: does this sound like you, plus a yes or no on the main thing we stop saying.

   Pillars, segment lines and the options considered stay out: they are the agency's tools and live in `positioning.md` and `decisions.md`.

## 3. Voice

1. **Read** the `brand.md` draft, `positioning.md`, the client's own texts in `_in/` and approved pieces in `_out/`. Optionally ask for one brand, of any category, whose way of talking the client likes.
2. **Samples:** write the same short message (the lead pillar, or a real message from `_in/`, in a channel the client uses) in 3 versions that differ on two named dials where this client could really go either way (how much regional speech, humor or none, short or storytelling). Two versions are plausible for this client, one anchored in the client's own words; the third is the category default, how every competitor sounds, as a foil. People recognize the right voice when they see it and cannot describe it in advance.
3. The user picks and adjusts. If the team leaves the choice to Claude, recommend one but put both plausible versions on the strategy page for the client to choose. Then write one bad-news line (a delayed delivery) in the chosen voice: bad news is where voices break.
4. **Write** `brand.md` following the guide, with the chosen sample and a before and after of one real piece as its first right and wrong examples, as `[hypothesis: team]`, and log the choice.
5. **Strategy page:** together with positioning when both ran in this session (step 2.6), otherwise `_out/YYYY-MM-DD_strategy-<topic>_v<N>.md` (topic in the client language, such as `tom-de-voz`) with `Proposes: _knowledge/brand.md`: the 3 traits in plain words, the before and after, the samples to choose from if delegated, and the closing question.

## 4. Report

In the team language, short: files written, what to send the client and how, what their answer will change, and open `[question:]` markers. Offer a tagline from the positioning statement through copywrite.
