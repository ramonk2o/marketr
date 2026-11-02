# Collect: competitors

How to find out what the customer compares the client with. Fills `competitors.md` (see its guide for the sections).

## Who to research

- Start from the competitors in `competitors.md`, in discovery's interview, and the ones the user names.
- Complete by searching with the words customers use (from `icp.md` or the audience collection), in the client language and country, as a prospect would: whoever shows up is what the customer actually sees.
- Per product: a course, a subscription and a shop face different rivals. 3 to 5 direct competitors plus the main alternative per product. More is noise for a small business.
- Always include the alternatives: other categories, doing it themselves (free videos, the supermarket), doing nothing.

## Per competitor

| What | Where | Reachable |
|---|---|---|
| Offer, price range, offer mechanics (guarantee, shipping, cancellation, trial) | Site, product and pricing pages, FAQ | WebFetch usually works |
| Main promise and tone | Home page, ads, bio | WebFetch for the site; profiles rarely |
| Segment they seem to target | Who appears in their images, words and offers | Inference: mark it so |
| Proof they use | Testimonials, numbers, seals, press | Site |
| What their customers praise and complain about | Reviews, complaint sites, marketplaces | Often blocked; ask for links or screenshots when it fails |
| Where they invest | Ads running, active channels, posting frequency | Meta Ad Library and Google Ads Transparency Center load by script: use a browser tool if connected, or ask the user for screenshots or links |

Ads that have been running for 3 months or more are probably working: that is a stronger signal of what the competitor believes sells than the ad's text alone.

## Synthesis notes

- **Purchase criteria:** rank what customers say they choose on (price, freshness, convenience, trust, service) by evidence, and compare the client against each competitor on those, in that order. Criteria nobody mentions do not belong in the comparison.
- **Gaps:** apply the guide's test (customers want it, competitors do not deliver it, the client can prove it). Label each "unclaimed" or "claimed but undelivered", with its evidence level. Silence in the market is often silence because nobody cares; without customer evidence, it is an idea.
- **Competitors' customers are not the client's customers:** their priorities (price per kilo, say) may belong to a segment the client does not serve. Say so when a finding rests only on them.
- Facts the client states about a competitor ("they dropped their price") came through discovery; check them when you can and keep their source.

## Collector prompt

Fill the brackets and give each collector one or two competitors:

```
Research the competitor [name, link] of [client, what they sell, country, language], for the product [product].
Collect: offer and price range, offer mechanics (guarantee, shipping, cancellation, trial), main promise and tone in their own words, proof they use, segment they seem to target (mark as inference), and what their customers praise and complain about (reviews, complaint sites, marketplaces).
For each quote: the exact text (ask WebFetch for verbatim excerpts; never quote a search snippet), URL and posting date. Replace names, phone numbers, handles, emails and order numbers with [name], [phone] and so on.
Return a profile of at most 25 lines, at most 15 customer quotes, and the sources you could not reach and why.
Return results only: do not create or edit files, and do not start other agents.
```
