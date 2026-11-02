# Collect: audience

How to find out who buys and in what words. Fills `icp.md` (see its guide for the sections).

## What to ask the client for

Ask in this order: the first items are cheap and the richest. Tailor to the business type (local shop, e-commerce, services, subscription, B2B) and skip what does not apply.

| Source | Why it matters | How to get it |
|---|---|---|
| 15 minutes with whoever answers WhatsApp, DMs or the counter | Knows the top questions before buying, why people do not buy, why they leave | Ask the user to run it and drop the notes in `_in/`, or to answer here: the 5 most common questions before buying, the most common reasons for not buying, for cancelling, for coming back |
| Cancellation or refund reasons | Broken promises and real objections, decisive for subscriptions | Export from the subscription, payment or store platform |
| WhatsApp Business chats | Prospect questions in their own words | In the chat: More, Export chat, Without media (.txt). A handful of typical chats is enough |
| Instagram comments and DMs | Questions and praise in the customer's words | Accounts Center, Your information and permissions, Download your information; or screenshots |
| Google Business Profile reviews | Public, dated, often detailed | No export: copy and paste or screenshots of the latest 50 to 100 |
| Marketplace and store reviews | Purchase-level detail | Seller panel export (Mercado Livre, Amazon, Shopee, Shopify apps) |
| Survey answers, NPS comments, support tickets | Already collected, often ignored | Export as CSV or text |
| Sales call recordings or notes (B2B, services) | Triggers, decision makers, objections | Transcripts or notes in `_in/` |
| Customer list without personal data | Situation segments: tenure, gift or self, city, plan | Spreadsheet with names, emails and phones removed |

## Public sources

| Source | What it gives | Reachable |
|---|---|---|
| Search language: autocomplete, "people also ask", related searches, in the client language and country | The exact words prospects use, awareness level, works even with zero reviews | WebSearch; Google Trends for seasonality (feeds `marketing.md`) |
| Competitors' reviews and complaint sites (Reclame Aqui in Brazil, Trustpilot elsewhere) | Unmet pains and desires, objections | Often blocked or thin through WebFetch; ask for links or screenshots when it fails |
| Marketplaces (Mercado Livre, Amazon, Shopee) | Category reviews from real buyers | Product pages sometimes open; reviews often load by script |
| YouTube comments on category videos (tutorials, comparisons) | Prospect language, the "do it myself" alternative | Rarely through WebFetch; the user can paste the best |
| Forums and groups (Reddit, Facebook groups, niche forums) | Unfiltered talk; Reddit is thin for Brazil | Reddit sometimes opens; groups need the user |
| Category review sites (Tripadvisor, iFood, Yelp, G2 for software) | Detailed reviews by business type | Varies; try, and report failures |

Google Maps reviews, Instagram, TikTok and Facebook rarely open through WebFetch. If a browser tool is connected, it can read them; otherwise ask the user.

## What to extract

Tag each quote with its role in the buying story, because a list of pains does not tell copy which angle to take:
- **Before:** what they used or did before (feeds Triggers and the alternatives in `competitors.md`).
- **Push:** what made them start looking (Triggers).
- **Pull:** what attracted them to this kind of solution (Desires).
- **Anxiety:** what almost stopped them (Objections, before buying).
- **Outcome:** what changed after buying, or what disappointed them (Literal language; disappointments go to Objections, after buying).

Also note the words customers use for the product and the category, and the words they never use: they feed copy and the vocabulary in `brand.md`.

## Synthesis notes

- **Segments by situation, not demographics:** group people by the job they hire the product for and the situation they are in. Two or three segments are usually enough for a small business; more are noise.
- **Awareness per segment:** problem words in their searches ("coffee at home tastes bad") mean problem-aware; category words ("coffee subscription") mean solution-aware; brand words mean product-aware. Mentions of a previous solution in reviews point the same way.
- **Literal language:** keep the best 10 or so quotes in `icp.md`, grouped by use; the collection keeps the rest.
- **Low-information reviews** ("great coffee, 10/10") count for satisfaction, not for pains or desires.

## Collector prompt

Fill the brackets and give each collector one source group:

```
Collect evidence for audience research about [client, what they sell, country, language].
Source group: [e.g. competitor reviews on Reclame Aqui and marketplaces for: X, Y].
Search in [language] with the words customers use: [examples].
For each quote: the exact text (ask WebFetch for verbatim excerpts; never quote a search snippet), URL, posting date, whose voice (client customer / competitor customer: name / prospect), role (before, push, pull, anxiety, outcome) and theme.
Replace names, phone numbers, handles, emails and order numbers with [name], [phone] and so on.
Return at most 25 quotes, a 5-line summary of themes with how many people support each, and the sources you could not reach and why.
Return results only: do not create or edit files, and do not start other agents.
```

## Customer questionnaire

When evidence is weak, offer these questions for the client to send to about 10 recent customers, in the client language and in plain words:
1. What were you using or doing before you found us?
2. What made you start looking for something different?
3. What almost made you give up on buying?
4. What changed after you started?
5. How would you describe us to a friend?
