# Changelog

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
