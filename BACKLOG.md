# Backlog

Ideas, bugs and debt for this plugin, managed with sensei's log skill. Each entry starts from a real case. Done work leaves this file: what changed goes to CHANGELOG.md.

## branding

### Naming
- **Type:** Idea
- **Motivation:** no case recorded
- **Description:** branding helps name a business.
- **Decisions:**
  - New companies only.

## copywrite

### WhatsApp channel
- **Type:** Idea
- **Motivation:** no case recorded
- **Description:** a WhatsApp channel for sales and follow-up scripts, widely used by small businesses in Brazil.

### Short-video scripts in their own skill
- **Type:** Debt
- **Motivation:** no case recorded
- **Description:** split short-video scripts out of copywrite into their own skill.
- **Decisions:**
  - Only if scenes and production notes outgrow copywrite.

## research

### Interview script and survey for real customers
- **Type:** Idea
- **Motivation:** no case recorded
- **Description:** research writes an interview script and a survey for real customers. Today it offers a 5-question questionnaire.
- **Decisions:**
  - Needs deliverable channel ids for them, a conventions change.

### Researcher agent
- **Type:** Debt
- **Motivation:** no case recorded
- **Description:** a plugin agent (`agents/researcher.md`, web and read tools only) for research's collector subagents.
- **Decisions:**
  - Only if collector subagents ever write files.

## setup

### Migrations in a reference file
- **Type:** Debt
- **Motivation:** no case recorded
- **Description:** move setup's "Migrations" to `skills/setup/references/migrations.md`, read only when upgrading.
- **Decisions:**
  - Once it grows past a few entries.

## Plugin

### Campaign and content planning
- **Type:** Idea
- **Motivation:** no case recorded
- **Description:** campaign plans and the monthly content calendar, built on the message pillars. Creates campaign briefs; copywrite writes the pieces.
- **Decisions:**
  - Next in line.

### Results analysis
- **Type:** Idea
- **Motivation:** no case recorded
- **Description:** reads piece and campaign metrics and records what worked in `marketing.md`.

### Offer design
- **Type:** Idea
- **Motivation:** no case recorded
- **Description:** price, bundles, guarantee. Today branding only flags offer problems as `[question:]` in `product.md`.

### Per-deliverable language override
- **Type:** Idea
- **Motivation:** no case recorded
- **Description:** a deliverable can use a language other than the project's, for a client with more than one market.

### Hook blocking writes to `_in/`
- **Type:** Idea
- **Motivation:** no case recorded
- **Description:** a PreToolUse hook that blocks writes to `_in/`.
- **Decisions:**
  - Only if the rule is broken in practice.
