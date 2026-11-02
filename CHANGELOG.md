# Changelog

## 0.3.0 (2026-11-02)

### Added
- branding: positioning and tone of voice as decisions, not proofs. A short interview, 2 or 3 options for the team, a one-recommendation strategy page the client approves (pasteable into WhatsApp), and voice chosen from samples. Names the customer's main alternative, checks claims against each competitor, tells the client what the promise commits them to, and sends one page when positioning and voice run together. Resumes from the latest strategy page of each topic; a rejected rethink restores the approved text.
- Trigger tests for branding, and branding excluded where it should not fire.

### Changed
- Conventions version 4: channel id `strategy` (a proposal with `Proposes: _knowledge/<file>`); approving one removes the markers on its choices, not on the facts they point to; a higher version supersedes a draft. Existing projects: run `/marketr:setup`; no files move now, and branding restructures an old `positioning.md` the next time it runs.
- `positioning.md` guide: positioning statement whose "because" proves the difference, main alternative, we are / we are not, we don't say, pillars that point to facts and objections, lead pillar by segment, the obvious choice executed well. `brand.md` guide: traits with writing moves, signature moves, one screen.
- discovery leaves positioning decisions to branding; copywrite starts from the segment's lead pillar and owns taglines; research points to branding when findings touch a pillar.

## 0.2.0 (2026-11-02)

### Added
- research: audience and competitor research from evidence. Client exports first, then public reviews, search language and competitors' sites; verbatim, anonymized quotes tagged by whose voice they are; evidence rated strong, moderate or weak; collector subagents for larger scopes; a 5-question customer questionnaire when evidence is weak.
- Trigger tests in `evals/triggers/` (`claude plugin eval`), checking that discovery, research and copywrite fire on the right requests.

### Changed
- Conventions version 3: research collections live in `_in/` as `YYYY-MM-DD_research-<target>-<topic>.md`. Existing projects: run `/marketr:setup`; no files move.
- `icp.md` and `competitors.md` guides: segments by situation, awareness per segment, objections before and after buying, evidence notes, ranked purchase criteria, and a test for real gaps.
- discovery: skips research collections and leaves customer-voice mining to research.

## 0.1.0 (2026-11-01)

### Added
- copywrite: writes, revises, reviews and adapts copy for push, SMS, email, web pages, Instagram posts, short videos, Google Ads and Meta ads. One researched reference per channel with limits, what to deliver, policies and language notes, dated and sourced.
- copywrite's `check.py`: measures each field against its limit (full-width characters, ad placeholders) and gives SMS encoding, segments and a GSM-7 version.
- `channels.md` knowledge file and its guide: the formats agreed with each client, per channel.

### Changed
- Conventions version 2: `channels.md`, fixed channel ids, tables allowed in deliverables where the format needs them. Existing projects: run `/marketr:setup` to upgrade; no files move.

## 0.0.3 (2026-10-30)

### Changed

- `setup` explains the reason behind each step, so it handles cases its rules did not foresee. Suggests discovery as the next step.

## 0.0.2 (2026-10-30)

### Added

- `discovery` skill: builds and maintains the client's knowledge base from `_in/`, the client's web presence and an interview. Modes: first run, update, scope, review. Offers a questionnaire for the client.
- Shared guides in `references/knowledge/`, one per knowledge file.

### Changed

- Conventions version 1 refined before any real use: knowledge files answer one question each with an owner skill, section-based product overrides, contradiction, approval and campaign brief rules, interview as a source, frontmatter fully in English.

## 0.0.1 (2026-10-30)

### Added

- `setup` skill: creates or upgrades a client's marketing project (`_in/`, `_knowledge/`, `_out/`, `decisions.md`, `.gitattributes`). Conventions version 1, rendered into `.claude/rules/marketr.md`.
