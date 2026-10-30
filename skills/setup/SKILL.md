---
name: setup
description: Sets up a client's marketing project in the current folder (folders, marketr conventions, decisions log), or upgrades one created by an older marketr version. Use when starting work for a new client, when another marketr skill finds the folder is not a marketr project, or when a marketr skill reports outdated conventions.
---

# Setup

Prepares the current folder as one client's marketing project. The conventions live in `${CLAUDE_SKILL_DIR}/assets/rules.template.md`, the single source of truth for the project's structure and rules. Setup renders it into `.claude/rules/marketr.md`, which Claude loads in every session in the folder. Talk to the user in their language; the files follow the language rules in the template.

Setup owns `.claude/rules/marketr.md` and never touches `CLAUDE.md`, `AGENTS.md` or anything in `_in/`, `_knowledge/` and `_out/` beyond what is listed below.

## 1. Detect the state

Read `.claude/rules/marketr.md` if it exists, and compare its "Conventions version" with the template's.

- **New:** the file does not exist. Go to step 2.
- **Outdated:** lower version. Go to step 5.
- **Current:** same version. Create anything missing from step 3, tell the user the project is up to date, and stop.
- **Newer:** higher version. Tell the user to update the marketr plugin, and stop.
- **Unreadable:** no version found. Describe what you found and ask the user how to proceed.

## 2. Ask

Ask only what the user's message has not already given:
1. The client's name.
2. The client's language: the language of their audience, used for knowledge and deliverables.

Infer the team language from the language the user is writing in. Do not ask; state it in the final summary so the user can correct it.

Products, market and everything else belong to later skills. Do not ask about them.

## 3. Create

- `_in/`, `_out/` and `_knowledge/products/`. Put an empty `.gitkeep` in each folder you create, so git keeps it. Never add anything to an `_in/` that already exists.
- `.claude/rules/marketr.md`: the template with `{{CLIENT_NAME}}`, `{{TEAM_LANGUAGE}}` and `{{CLIENT_LANGUAGE}}` filled in. Claude Code asks for approval before writing in `.claude/`: tell the user beforehand that this is expected. If the write is denied, say the project is incomplete without it and stop.
- `decisions.md`, in the team language: if it does not exist, create it with a title. Then append an entry recording that the project was set up with marketr, the client's name and both languages.
- `.gitattributes` with the line `decisions.md merge=union`, so entries added by different people merge without conflicts. If the file exists, add the line only if missing.

## 4. Finish

- If the folder is not a git repository, offer `git init`. Do it only if the user accepts.
- In the team language, explain in one line each what goes in `_in/`, `_knowledge/` and `_out/`, that `decisions.md` records decisions, and that project-specific notes go in `CLAUDE.md`.
- If `_in/` already has files, say that they will be used when building the client's context.

## 5. Upgrade

1. From the existing file, keep the client's name and both languages.
2. Overwrite `.claude/rules/marketr.md` with the template, refilled with those values.
3. Apply each migration below whose version is higher than the project's, in order.
4. Create anything missing from step 3.
5. Log the upgrade in `decisions.md`: from which version to which, and what changed.

### Migrations

None yet.
