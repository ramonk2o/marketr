# marketr: plugin project

A Claude Code plugin with marketing skills for people who run marketing for clients. Each skill reads and writes a per-client knowledge base inside the client's project folder (the "generated project"). This repo is the "plugin project".

## Maintenance with sensei

This repository is maintained with the sensei plugin. If sensei is installed:
- creating or changing a skill, judging an issue or pull request, or auditing consistency: the `train` skill;
- BACKLOG.md and CHANGELOG.md: the `log` skill (`train` writes its own changelog entries);
- releasing a version: `/sensei:graduate`.

Other skills or plugins that write skills or manage these files don't apply in this repository. Without sensei, follow `docs/principles.md` and keep CHANGELOG.md in the Keep a Changelog format.

**The skills are the object of the work here, not tools.** When the conversation is about the plugin's subject (client discovery, research, positioning, tone of voice, copy), it's about improving the skills. Don't run a skill's flow unless explicitly asked to use it.

## Layout

```
.claude-plugin/plugin.json        plugin manifest; the only place with the version
.claude-plugin/marketplace.json   this repo is also the marketplace (ramonk2o-marketr)
skills/<name>/SKILL.md            one folder per skill; extra material in references/, assets/ or scripts/
references/knowledge/<file>.md    how to fill each _knowledge file, shared by every skill that writes it
docs/principles.md                principles and limits; every change is checked against them
example/_in/                      raw material of a fictional client, for testing
evals/triggers/                   trigger tests: which skill fires on which request
BACKLOG.md  CHANGELOG.md  README.md  LICENSE
```

## Project facts

- **Documents:** English.
- **Principles:** `docs/principles.md`. Every change is checked against them.
- **Skills stand alone:** no. Skills share `references/knowledge/` and the conventions template; one owner per fact.
- **Validate:** sensei's check script on every change (it runs `claude plugin validate` on the last commit); `--release` at release, which adds `--profile directory`.
- **Commits:** Ramon K. <contato@ramonk.com>; trailers: the environment's default (Co-Authored-By).
- **Integration:** local merge with `--no-ff`; push main when the maintainer says so or at release.
- **Tags:** `vX.Y.Z`.
- Reference a skill's own files with `${CLAUDE_SKILL_DIR}/...` and shared files with `${CLAUDE_PLUGIN_ROOT}/references/...`: the working directory is the client's project, not this repo.
- Never name a file `CLAUDE.md` inside `skills/`: Claude would load it as instructions.
- Every SKILL.md except setup opens with its contract (`Requires conventions: N`, `Reads: ...`, `Writes: ...`), then a rule to run setup when `.claude/rules/marketr.md` is missing and to suggest `/marketr:setup` when its version is lower. See `skills/discovery/SKILL.md`.
- Shared references hold only how to do things (section meanings, examples). Move logic into one only when a second skill needs it.
- Test against a copy of the example, outside this repo, so this file is not loaded:
  ```
  rm -rf "$TMPDIR/marketr-test" && mkdir -p "$TMPDIR/marketr-test"
  cp -R example/_in "$TMPDIR/marketr-test/"
  cd "$TMPDIR/marketr-test" && claude --plugin-dir <path-to-this-repo>
  ```
  Non-interactive runs (`claude -p`) cannot read the plugin folder unless you pass `--add-dir <path-to-this-repo>`.
- Trigger tests (real, billed runs): `claude plugin eval . --tag triggers --ablation none -j 4`.
- When the generated project's structure or rules change: bump "Conventions version" in the template, grep "Requires conventions" and review each skill, add a migration to setup's "Migrations" section when existing projects need files moved or rewritten, and note it in the CHANGELOG.
