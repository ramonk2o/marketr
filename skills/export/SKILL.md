---
name: export
description: Packages a client's knowledge base (_knowledge/) for use outside this project. A zip for another marketr project, a developer or another agency, or one consolidated Markdown file for a Claude, ChatGPT or Gemini project. Use it when the user wants to export, package, zip, hand off or share what is known about the client, or to bring the client's context into another project or AI tool ("zip the knowledge base", "I want to use this in a GPT", "send the client's context to the web developer"). Not for reviewing or fixing the knowledge base (discovery), or for writing marketing deliverables.
---

# Export

Requires conventions: 5
Reads: `_knowledge/`, strategy pages in `_out/`, optionally `decisions.md` and `_in/`
Writes: one `export` in `_out/` (`.zip` or `.md`); appends to `decisions.md`

## Rules that always apply

The project's conventions (`.claude/rules/marketr.md`) already apply. These are the points export most often gets wrong, and why they matter:

- If `.claude/rules/marketr.md` is missing, run the marketr setup skill first, then continue. If its conventions version is lower than 5, suggest `/marketr:setup` and stop.
- Export copies; it never changes `_knowledge/`. If you spot a problem while reading, mention it in the report and suggest discovery. Fixing it here would change the source without the review the owner skill does.
- Keep every marker (`[hypothesis:]`, `[missing:]`, `[question:]`) and explain them to the reader. Stripping them would turn guesses into facts in the other project, which will then write copy on top of them.
- The reader does not know marketr's conventions. Anything the files rely on without saying it (markers, product inheritance, what is approved) goes in the README or the header, or the reader will misread it.
- Ask before including internal information. The package leaves the team's hands, and a budget or an approver's name in a developer's repository is hard to take back.

## 1. Ask

Ask only what the user's message has not already given, in one message:

1. **Where it goes.** Pick the format from the answer:
   - **Another marketr project** (the same client with another team, or a new folder): a zip with `_knowledge/` exactly as it is, frontmatter included, because the skills there search `summary` and `sources`.
   - **An AI assistant project** (Claude, ChatGPT, Gemini, a custom GPT): one consolidated `.md`, not a zip. Those tools limit the number of files, cannot open a zip as project knowledge, and answer better from one coherent document.
   - **Anything else** (a developer's repository, another agency, a shared drive): a zip with a README and `_knowledge/`.
2. **What to leave out.** Search `_knowledge/` for internal information and list what you find, by file and section: budget, approvers, results of tests and campaigns, named people. Ask whether to keep each. Offer `decisions.md` only for another marketr project, where its history keeps the team from reopening settled choices, and `_in/` too, if the receiving team will run discovery or research again.

## 2. Check before packaging

- Count the markers per file and note files whose `updated` is older than 6 months. A long list means the package carries many open points; say so, so the user can run discovery first if the export is for something that matters.
- Check whether `positioning.md` and `brand.md` (company and products) are approved: a `strategy` page in `_out/` with `status: approved` proposes them and does not list them as `Rejected:`. A file without that approval goes out labeled "not yet approved by the client"; otherwise the other project treats a draft positioning as settled.
- Skip `.gitkeep`, `.DS_Store` and any file outside the conventions. They mean nothing to the reader.

## 3. Build

Write the README or the header in the client language, like the files it describes. It always says:
- what this is: the knowledge base of <client>, exported on <date> from a marketr project, which stays the source of truth (a copy goes stale the day the client changes a price);
- what each marker means;
- that a file in `products/<slug>/` replaces the company section with the same heading and inherits the rest;
- which files are not yet approved by the client, and what was left out on purpose.

### Zip

1. Stage in a new folder under `$TMPDIR`, never inside the project: a half-built package must not end up in `_out/` or `_in/`.
2. Copy the files at their paths (`_knowledge/...`, plus `decisions.md` or `_in/` if chosen), removing only the sections the user chose to leave out. Leaving out a section leaves its heading out too; add `[missing: left out of this export]` where the gap would confuse the reader.
3. Add `README.md` at the root: the points above, then an index with one line per file, taken from its `summary`. For another marketr project, add how to import: in a folder with no `_knowledge/`, run `/marketr:setup` and unzip at the root; in one that already has a knowledge base, put the files in `_in/` and run discovery, because unzipping would overwrite the work there.
4. Zip from inside the staging folder, so the paths start at `README.md` and `_knowledge/`: `zip -r <project>/_out/<name>.zip .`, or `python3 -m zipfile -c <project>/_out/<name>.zip README.md _knowledge` (adding anything else you staged) when `zip` is missing. List the zip's contents to check it.

### Consolidated file

One `.md` in `_out/`:
1. The header (the points above).
2. Each file in this order: `company.md`, `positioning.md`, `brand.md`, `icp.md`, `competitors.md`, `marketing.md`, `channels.md`, then each product, with `product.md` followed by its other files. Open each with a `##` heading that names what the file answers, in the client language, and its `updated` date. Shift its own headings down one level, so the document has one outline.
3. Drop the frontmatter: the reader cannot open the `_in/` files that `sources` lists, and the date is already in the heading.

Name either one `YYYY-MM-DD_export-<destination>_v<N>`, with the destination as a slug in the client language (`export-site`, `export-chatgpt`). A new export for the same destination is a new version.

## 4. Close

- Append to `decisions.md`: what was exported, for where, and what was left out. When the knowledge base changes later, this is how the team knows another project holds an old copy and should get a new export.
- Report in the team language, briefly: the file in `_out/`, what went in and what was left out, the marker counts and unapproved files, and how to use it at the destination (where to upload the `.md`, or where to unzip).
