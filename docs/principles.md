# marketr principles

marketr's skills build and use a per-client marketing knowledge base inside the client's project folder. Every skill follows these principles. A change that breaks one is a design decision and needs the maintainer's explicit agreement.

<!-- sensei:limits
skill_tokens: 5000
description_chars: 1024
-->

## Before writing

1. Every skill except setup checks the client folder's conventions first: it runs setup when `.claude/rules/marketr.md` is missing and suggests `/marketr:setup` when its version is lower than the skill requires.
2. Before writing a `_knowledge/` file, a skill reads its fill guide in `references/knowledge/`, so files stay consistent across clients and skills.
3. A skill adds to a file owned by another skill with a source, and asks before rewriting what is there.
4. Positioning and tone of voice are proposed for the client to approve, never written as settled.

## Building skills

5. Lean: a file, section or skill is added only when it is useful now; otherwise it goes to BACKLOG.md.
6. Rules explain why: each rule says what it protects. A model that understands the reason handles cases the rule did not foresee; bare MUSTs and NEVERs get followed literally or not at all.
7. One owner per fact, so skills do not stand alone. The client folder's conventions live only in `skills/setup/assets/rules.template.md`; how to fill each knowledge file lives only in `references/knowledge/`. Skills rely on them and do not repeat them.
8. A skill's permanent rules sit at the top of its SKILL.md, and the SKILL.md stays within `skill_tokens`: after compaction only its first ~5,000 tokens survive.
9. Each description says what the skill is for and what it is not for, naming the sibling that owns the rest, within `description_chars`.
10. Every file in this repo is in English. Skills talk to the user in their language. In the client folder, the languages follow the conventions template.

## Checking results

11. Every change is tested on a copy of `example/_in` outside this repo, with `--plugin-dir`, and passes `claude plugin validate`.
12. A changed description also runs the trigger tests in `evals/triggers/`.
13. A new or rewritten skill gets independent reviewer agents. No formal eval loop, unless a skill shows regressions or trigger collisions.

## Judging a proposal

1. Which real case does it come from?
2. Is it useful now, or does it belong in BACKLOG.md?
3. Does a rule it adds already have an owner (the conventions template, a knowledge guide, a sibling skill)?
4. Does it change the client folder's structure or rules? If so, does it bump the conventions version and need a migration?
5. Does it move work between sibling skills, and do both descriptions still say who owns what?
