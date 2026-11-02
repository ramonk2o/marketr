# marketr

Marketing skills for Claude Code. Each client gets a project folder. The skills build a knowledge base about the client there (context, products, brand, competitors, decisions) and use it in everything they produce.

```
_in/          raw material from the client
_knowledge/   what is known about the client, curated by the skills
_out/         deliverables
decisions.md  what was decided, when and why
```

Project files and instructions are in English. Knowledge and deliverables are written in the client's language, and Claude talks to you in yours.

## Install

```
/plugin marketplace add ramonk2o/marketr
/plugin install marketr@ramonk2o-marketr
```

## Update

```
/plugin marketplace update ramonk2o-marketr
/reload-plugins
```

Auto-update is off by default for third-party marketplaces. To turn it on: `/plugin`, Marketplaces, `ramonk2o-marketr`, Enable auto-update.

After an update, run `/marketr:setup` in existing client folders if a skill says their conventions are outdated.

## Skills

- `/marketr:setup`: prepares the current folder for a new client, or upgrades it.
- `/marketr:discovery`: builds what we know about the client from their material, their web presence and an interview with you; later, processes new material and reviews the knowledge base.
- `/marketr:research`: finds out who buys and in what words, and what competitors offer and fail at, from the client's exports, public reviews, searches and competitors' sites.
- `/marketr:copywrite`: writes, revises, reviews and adapts copy for push, SMS, email, website and landing pages, Instagram posts, short videos, Google Ads and Meta ads, within each platform's limits and the formats agreed for the client.

More are on the way; see [BACKLOG.md](BACKLOG.md).

## License

MIT
