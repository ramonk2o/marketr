# marketr: plugin project

A Claude Code plugin with marketing skills. Each skill reads and writes a per-client knowledge base inside the client's project folder (the "generated project"). This repo is the "plugin project".

## Principles

- Lean: add a file, section or skill only when it is useful now. If in doubt, put it in BACKLOG.md.
- Every file in this repo is in English. Talk to the user in their language.
- Skills explain why, not just what: each rule says what it protects ("write at the end of each block: sessions get interrupted and what is only in the conversation is lost"). A model that understands the reason generalizes to cases the rule did not foresee; bare MUSTs and NEVERs get followed literally or not at all.
- The conventions of the generated project live in one place: `skills/setup/assets/rules.template.md`, which setup renders into the generated project's `.claude/rules/marketr.md`. Skills rely on those conventions and do not repeat them.

## Layout

```
.claude-plugin/plugin.json        plugin manifest; the only place with the version
.claude-plugin/marketplace.json   this repo is also the marketplace (ramonk2o-marketr)
skills/<name>/SKILL.md            one folder per skill; extra material in references/, assets/ or scripts/
references/knowledge/<file>.md    how to fill each _knowledge file, shared by every skill that writes it
example/_in/                      raw material of a fictional client, for testing
BACKLOG.md  CHANGELOG.md  README.md  LICENSE
```

- Reference a skill's own files with `${CLAUDE_SKILL_DIR}/...` and shared files with `${CLAUDE_PLUGIN_ROOT}/references/...`. The working directory is the client's project, not this repo.
- Rules belong in the conventions template; shared references hold only how to do things (section meanings, examples). Move logic into a shared reference only when a second skill needs it.
- Put a skill's permanent rules at the top of its SKILL.md: after compaction only its first ~5,000 tokens survive.
- Each description says what the skill is for and what it is not for, to avoid collisions with other marketr skills.
- Never name a file `CLAUDE.md` inside `skills/`: Claude would load it as instructions.
- Every SKILL.md except setup opens with its contract: `Requires conventions: N`, `Reads: ...`, `Writes: ...`, then a rule to run setup when `.claude/rules/marketr.md` is missing and to suggest `/marketr:setup` when its version is lower. See `skills/discovery/SKILL.md`.

## Cycle

1. **Idea:** one line under "Ideas" in BACKLOG.md.
2. **Start:** move it to "In progress" with a mini-brief: what it does, what it reads, what it writes.
3. **Build:** write or change the skill.
4. **Test:** run it against a copy of the example, outside this repo, so this file is not loaded:
   ```
   rm -rf "$TMPDIR/marketr-test" && mkdir -p "$TMPDIR/marketr-test"
   cp -R example/_in "$TMPDIR/marketr-test/"
   cd "$TMPDIR/marketr-test" && claude --plugin-dir <path-to-this-repo>
   ```
   Then run `claude plugin validate .` from this repo.
5. **Ship:**
   - Remove the item from BACKLOG.md and add it to CHANGELOG.md under a new version.
   - Bump `version` in plugin.json. Without a bump, users do not receive the update.
   - If the generated project's structure or rules changed:
     - Bump "Conventions version" in the template, then grep "Requires conventions" and review each skill.
     - Add a migration to setup's "Migrations" section when existing projects need files moved or rewritten.
     - Note it in the CHANGELOG.

## BACKLOG.md and CHANGELOG.md

- BACKLOG.md has three sections: In progress, Next, Ideas. Remove items when shipped or discarded; the history lives in CHANGELOG.md.
- CHANGELOG.md: newest version first, `## <version> (YYYY-MM-DD)`, then Added / Changed / Fixed / Removed as needed.
