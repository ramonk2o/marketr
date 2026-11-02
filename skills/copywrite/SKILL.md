---
name: copywrite
description: Writes, revises, reviews and adapts copy for a client's brand channels, organic or paid, using what the project knows about them (_knowledge/). Channels - push notifications, SMS, email, website and landing pages, Instagram posts and carousels, short videos (Reels, TikTok, Shorts), Google Ads (all campaign types) and Meta ads (Facebook and Instagram). Use whenever the user wants copy, a headline, a tagline or slogan, a subject line, an ad, a caption, a script or a page for the client, rewritten from feedback, critiqued, or turned into another channel ("adapt this email to SMS", "the client asked for changes to the post", "what do you think of this copy?"), even without the word copy. Not for building the client's knowledge (discovery), audience or competitor research (research), defining positioning or tone of voice (branding), or the user's own personal essays, posts and emails.
---

# Copywrite

Requires conventions: 2
Reads: `_knowledge/`, the piece's campaign brief and earlier versions in `_out/`, past pieces in `_in/`, `${CLAUDE_SKILL_DIR}/references/channels/<channel>.md`
Writes: pieces and campaign briefs in `_out/`; owns `channels.md`; adds to other `_knowledge/` files; appends to `decisions.md`

## Rules that always apply

The project's conventions (`.claude/rules/marketr.md`) already apply. These are the points copy most often gets wrong, and why they matter:

- If `.claude/rules/marketr.md` is missing, run the marketr setup skill first, then continue. If its conventions version is lower than 2, suggest `/marketr:setup` and stop.
- Read the channel's reference before writing: its limits, what to deliver and its `Policies and restrictions`. Copy that ignores them is rejected by the platform or cut on the screen. If the reference's `Verified` date is more than 12 months old, say so and offer to check the official sources listed at its end, because platforms change fields and limits often.
- If a reference or the script cannot be read or run, tell the user which file failed and that the plugin folder needs read access. Do not write limits or policies from memory: memory is what the references correct, and a wrong limit gets the piece rejected. A review may go on with its limits marked as unverified.
- Count with the script, never by eye: models miscount characters, and one headline over the limit is rejected. Pass the lines on stdin, so nothing is written to the project:
  ```
  python3 ${CLAUDE_SKILL_DIR}/scripts/check.py fields - <<'EOF'
  H1 | 30 | headline text
  EOF
  ```
  Use `--wide` for Google Ads in Chinese, Japanese or Korean. `check.py sms -` gives encoding, segments and the characters forcing UCS-2; replace personalization tokens with their longest expected value first, and treat its GSM-7 version as a starting point to rewrite, not a finished message.
- Every fact, number, proof and testimonial comes from `_knowledge/` or from the user. If it is in neither, write `[missing: ...]` instead of inventing it: copy is public, and the client answers for every claim in it. A durable fact the user states (a price, a guarantee) goes into its `_knowledge/` file with source `interview YYYY-MM-DD`; a temporary one (an offer, a deadline) goes into the brief.
- Before writing a `_knowledge/` file, read its guide in `${CLAUDE_PLUGIN_ROOT}/references/knowledge/`. In files owned by another skill, add with source and ask before rewriting what is there.
- Check `company.md` restrictions and the channel's policies before saving. When a claim might break one, ask instead of guessing.
- Write to the customer in their own words: the literal language, pains and objections in `icp.md`. Their awareness level decides how much to explain before the offer.
- One piece, one goal, one main message. A piece asking for two actions gets neither.
- The angle and the hypotheses the copy relies on go in the piece's brief, so the client validates them when approving the piece.
- Read the channel's section in `channels.md` and ask only what is specific to the piece. When a client-level convention comes up in any channel (SMS sender and opt-out wording, merge tags, emoji use, how the brand is written), record it there. Asking again what was agreed wastes the user's time and makes pieces drift apart.

## 1. Choose the mode

- **Write:** a new piece or a set of pieces. Go to 2.
- **Revise:** one of our pieces, with feedback. Go to 5.
- **Review:** copy someone else wrote, in `_in/` or pasted. Go to 6.
- **Adapt:** turn one piece into others. Go to 7.
- **Campaign brief changed:** go to 8.

Search `_knowledge/` for `^summary:` first. To write without the product (or `company.md` for an institutional piece) there is nothing true to say: ask the user for the essentials or offer discovery. Without `icp.md`, `brand.md` or `positioning.md`, proceed and flag the gaps as hypotheses in the brief. If the user wants a piece in a language other than the client's, follow them and note it in the brief.

## 2. Brief

Fill from the request, `_knowledge/` and the campaign brief if the piece belongs to one. Ask only what is still missing, 3 to 5 questions at most:
- objective: the one action the reader should take;
- product and offer, with deadline and conditions;
- audience: segment and awareness level;
- channel and format (for ads, the campaign type; for web, the page type);
- mandatory items.

Offers and deadlines live in the brief, never in `_knowledge/`: they expire. Several pieces for one campaign get a campaign brief file first (channel `brief`). Each piece's brief opens with `Campaign brief: <filename>` and keeps only what is specific to it.

## 3. Plan

Plan in proportion to the piece, since a full plan for an SMS wastes more time than it saves:
- **Direct** (push, SMS, ad asset sets): variations, each from a different angle. No separate angle step.
- **Standard** (email, post, short video): choose the angle, then write.
- **Full** (landing page, sales page, long sales email, video over 60 s): choose the angle, then get the structure approved by the user before writing. Rewriting a page costs more than approving an outline. This is a pause for the user, not a client approval.

**Format.** For channels whose reference has a "Format agreement" section (email, web, post, video) and no section yet in `channels.md`, this is the client's first piece in the channel:
1. Infer the format from the client's past pieces in `_in/`, approved pieces in `_out/` and their site.
2. Propose a skeleton: blocks in order with approximate sizes, from what you inferred and the reference's defaults. Concrete proposals get precise answers; "how long do you want it?" gets a shrug. In full mode, this skeleton is the piece's structure: one proposal, one approval.
3. Write what the user accepts to `channels.md`, with its origin, before writing the piece.

**Angle:** the idea that makes this reader act now.
- If `positioning.md` has message pillars, start from the lead pillar of the brief's segment and say which. Respect its "we don't say" list and the signature moves in `brand.md`. Check what was tested and its results in `marketing.md`, so a failed angle is not repeated.
- Otherwise, or for a campaign or a long piece, propose 2 or 3 angles, each with a sample opening line and why it fits this reader. The user chooses.
- Record the chosen angle in the brief. Log it in `decisions.md` only when it is a campaign's angle or will be reused: a log of every piece's angle buries the decisions that matter.

## 4. Write, check, save

1. Write what the reference's "What to deliver" says, in the client language. Where a channel uses variations (ad assets, subject lines, SMS), deliver distinct ideas, not rewordings of one.
2. Check, and fix before saving:
   - limits, with the script;
   - `company.md` restrictions and the channel's policies;
   - every claim backed by `_knowledge/` or the user, or marked `[missing:]`;
   - voice against `brand.md` and its examples;
   - the opening: would the person in the brief stop for it?
   - one clear call to action.
3. Save to `_out/` with the conventions' name, frontmatter and brief.
4. Tell the user, in the team language: the file, the angle, the hypotheses the copy relies on, and any `[missing:]` the client must fill. Ask them to tell you when the client approves it.

## 5. Revise

1. Read the piece and the feedback. If the feedback is vague ("make it punchier"), point to the lines you would change and how, before rewriting.
2. Rewrite, check as in 4.2, and save a new `v<N+1>` with `status: draft`. Never overwrite: the earlier version is what the client compared against, and an approved one stays approved until the new one is.
3. When the feedback is a permanent rule, record it where it belongs: format in `channels.md`, voice in `brand.md`, forbidden claims in `company.md` restrictions.
4. Tell the user what changed and why.

## 6. Review

Never edit the original: it is the client's material. If it was pasted, offer to save it to `_in/` with a date prefix, so the rewrite has a traceable source.
1. Identify the channel and read its reference.
2. Judge, against the reference, `_knowledge/` and `brand.md`: limits and policies, false or unbacked claims, clarity of the goal and the call to action, the opening, the voice, whether it speaks to the customer in `icp.md`. Limits, policies and clarity can be judged without knowledge of the client; say which checks you could not make.
3. Report what works, then the problems in order of impact, each with why and a suggested fix.
4. Offer a rewrite, saved as a new piece in `_out/`.

## 7. Adapt

Adapting is rewriting for the new channel, not cutting: keep the message and the angle, change the opening, length, structure and call to action to what the channel needs.
1. Read the source piece and each target channel's reference.
2. If it becomes a campaign of several pieces and has no brief file yet, create one from the source piece's brief.
3. For each target, apply step 3's format agreement if the channel has none yet, then step 4. One file per piece.

## 8. Campaign brief changed

When an offer, deadline or condition changes:
1. Save the brief as a new `v<N+1>`.
2. Search `_out/` for `Campaign brief:` lines naming earlier versions, and list those pieces with what the change affects in each.
3. Offer to revise them (5). Approved pieces whose offer changed need a new version and a new approval.
