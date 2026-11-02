---
name: setup
description: Sets up a client's marketing project in the current folder (folders, marketr conventions, decisions log), or upgrades one created by an older marketr version. Use when starting work for a new client, when another marketr skill finds the folder is not a marketr project, or when a marketr skill reports outdated conventions.
---

# Setup

Prepares the current folder as one client's marketing project. The conventions live in `${CLAUDE_SKILL_DIR}/assets/rules.template.md`, the single source of truth for the project's structure and rules. Setup renders it into `.claude/rules/marketr.md`, which Claude loads in every session in the folder, so every skill and every plain conversation follows the same rules without repeating them. Talk to the user in their language; the files follow the language rules in the template.

Setup owns `.claude/rules/marketr.md` and nothing else of the user's. `CLAUDE.md` and `AGENTS.md` hold the user's own instructions, and `_in/`, `_knowledge/` and `_out/` hold client work: changing them would silently alter what the user wrote or what the client sent. Touch them only as listed below.

## 1. Detect the state

Read `.claude/rules/marketr.md` if it exists, and compare its "Conventions version" with the template's. The version tells you whether the project follows the rules the installed skills expect.

- **New:** the file does not exist. Go to step 2.
- **Outdated:** lower version. Go to step 5.
- **Current:** same version. Create anything missing from step 3, tell the user the project is up to date, and stop.
- **Newer:** higher version. The project was set up by a newer marketr than the one installed; downgrading its rules would break it. Tell the user to update the plugin, and stop.
- **Unreadable:** no version found. Someone edited the file by hand; overwriting it could discard their changes. Describe what you found and ask the user how to proceed.

## 2. Ask

Ask only what the user's message has not already given, so a user who typed `/marketr:setup Client X, Portuguese` is not asked again:
1. The client's name.
2. The client's language: the language of their audience. Knowledge and deliverables are written in it, so copy can quote the client and their customers without translation.

Infer the team language from the language the user is writing in, and state it in the final summary so the user can correct it. Asking would add a question whose answer is already in front of you.

Products, market and everything else belong to discovery, which asks about them with the client's material at hand. Asking here would mean asking twice.

## 3. Create

- `_in/`, `_out/` and `_knowledge/products/`. Put an empty `.gitkeep` in each folder you create, because git does not keep empty folders. Never add anything to an `_in/` that already exists: it is the client's raw material, kept exactly as received.
- `.claude/rules/marketr.md`: the template with `{{CLIENT_NAME}}`, `{{TEAM_LANGUAGE}}` and `{{CLIENT_LANGUAGE}}` filled in. Claude Code asks for approval before writing in `.claude/`; tell the user beforehand so the prompt does not look suspicious. If the write is denied, say the project is incomplete without it, since no other skill would find the conventions, and stop.
- `decisions.md`, in the team language: if it does not exist, create it with a title. Then append an entry recording that the project was set up with marketr, the client's name and both languages. Appending instead of recreating keeps any history already there.
- `.gitattributes` with the line `decisions.md merge=union`, so entries added by different people at the same time merge without conflicts. If the file exists, add the line only if missing.

## 4. Finish

- If the folder is not a git repository, offer `git init`. Do it only if the user accepts: many teams share folders through a drive instead.
- In the team language, explain in one line each what goes in `_in/`, `_knowledge/` and `_out/`, that `decisions.md` records decisions, and that project-specific notes go in `CLAUDE.md`. Someone new to marketr needs to know where to drop material and where to find work.
- If `_in/` already has files, say that they will be used when building the client's context, and suggest discovery as the next step.

## 5. Upgrade

1. From the existing file, keep the client's name and both languages.
2. Overwrite `.claude/rules/marketr.md` with the template, refilled with those values. The whole file belongs to marketr, so nothing of the user's is lost.
3. Apply each migration below whose version is higher than the project's, in order. Migrations change client files when a convention moved or renamed something; skipping one leaves files the skills can no longer find.
4. Create anything missing from step 3.
5. Log the upgrade in `decisions.md`: from which version to which, and what changed, so the team knows why files moved.

### Migrations

- **2:** adds `channels.md`, which copywrite creates when first needed. No existing file changes.
- **3:** research collections go in `_in/` as `YYYY-MM-DD_research-<target>-<topic>.md`. No existing file changes.
- **4:** adds the channel id `strategy` and the rule for applying an approved strategy page, and new sections in `positioning.md` and `brand.md`. No file changes now: branding restructures an existing `positioning.md` the next time it runs.
