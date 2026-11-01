# Channel: google-ads

Text assets for Google Ads campaigns. Google combines them, so every piece has to work alone and in any order.

Verified: 2026-11-01

## Pieces and fields

Limits are the same in every language. Each double-width character (Chinese, Japanese, Korean) counts as 2, so a 30-limit headline holds 15 of them. Where a limit says "not documented", the help page gives none: use the counter in the Google Ads form and say so in the deliverable.

**Search: responsive search ad (RSA)**

| Field | Limit | Count (min / max / rec.) | Notes |
|---|---|---|---|
| Headline | 30 | 3 / 15 / as many unique as possible | Up to 3 show at once; H1 and H2 positions always show, H3 not guaranteed |
| Description | 90 | 2 / 4 / 4 | D1 position always shows, D2 not guaranteed |
| Display path 1, 2 | 15 each | 0 / 2 | Text after the domain: `site.com/path1/path2` |

Ad Strength rates Poor to Excellent; Google recommends at least 2 RSAs rated Good or Excellent per ad group. Pinning lowers it.

**Search: assets with text** (also used by Performance Max)

| Asset | Field | Limit | Count | Notes |
|---|---|---|---|---|
| Sitelink | Link text | 25 (12 double-width) | min 2 to show; rec. 4+ per account, 6+ with descriptions per busy campaign | Up to 6 show on desktop, 8 on mobile |
| Sitelink | Description line 1, 2 | 35 each (API ref.) | 0 or both | Fill both or none; descriptions unlock larger formats |
| Callout | Text | 25 (12 double-width) | no min documented; up to 10 show | Keep short: how many show depends on length |
| Structured snippet | Header | from a fixed list | 1 per snippet | Amenities, Brands, Courses, Degree programs, Destinations, Featured hotels, Insurance coverage, Models, Neighborhoods, Service catalog, Shows, Styles, Types |
| Structured snippet | Value | 25 (API ref.) | 3 / 10 / 4+ | Values must be examples of the header, or it is disapproved |
| Price | Header, description | 25 each | 3 items min, 5+ rec., up to 8 cards show | No prices or sales wording ("Sale", "Free Shipping") here; the price has its own field. Qualifiers required by local law are allowed |
| Promotion | Item | not documented | 1 | Plus occasion (list), % or amount off, optional promo code or min. order, dates |
| Lead form | Headline, business name, description, CTA description, post-submit headline and description | not documented | 1 form | CTA type from a list; up to 5 custom questions (API ref.) |
| Call | Phone number | n/a | 1 | No copy; number must appear as text on your site to verify |
| Business name | Name | 25 | 1 | See Policies: domain or recognized business name, nothing generic or promotional |
| Image | none | n/a | n/a | No text field; images with overlaid text are a design matter, not copy |

**Performance Max: asset group**

| Field | Limit | Count (min / max / rec.) | Notes |
|---|---|---|---|
| Headline | 30 | 3 / 15 / 11+ | Include at least one of 15 or fewer |
| Long headline | 90 | 1 / 5 / 2+ | Aim for at least 30 |
| Description | 90 | 2 / 5 / 4+ | The help page no longer lists a separate 60-char short description; older guides do |
| Business name | 25 | 1 | Same rule as Search |
| Call to action | from a list | 1 | Automated by default |
| Display path | 15 each | 0 / 2 | |
| Search themes | not documented in current help (80 cited elsewhere) | up to 50 per asset group | Signals, not copy: short phrases people search, written like keywords |

**Display: responsive display ad**

| Field | Limit | Count (min / max) | Notes |
|---|---|---|---|
| Short headline | 30 | 1 / 5 | May show with or without the description |
| Long headline | 90 | 1 | Shows in larger formats instead of the short headline |
| Description | 90 | 1 / 5 | Adds to the headline and invites action |
| Business name | not documented (25 elsewhere) | 1 | Shown exactly as entered |
| Call to action | from a list | optional | Under "More options" |

**Demand Gen** (also the home of video action ads: see Video)

| Format | Field | Limit | Count | Notes |
|---|---|---|---|---|
| Single image | Headline | 40 | up to 5, at least 3 unique | |
| Single image | Description | 90 | up to 5, at least 3 unique | |
| Carousel | Ad-level headline | 40 | 1 | Shows on every card |
| Carousel | Ad-level description | 40 | 1 | Shows on every card; no per-card description |
| Carousel | Card headline | 40 | 1 per card, 2-10 cards | Not used on Discover, which repeats the ad-level headline |
| Video | Headline | 40 | at least 3 unique | Used in skippable in-stream |
| Video | Long headline | 90 | at least 3 unique | Used in in-feed (Discover, YouTube) |
| Video | Description | 90 | at least 3 unique | On Shorts any headline, long headline or description can become the description |
| All | Business name | 25 | 1 | On in-feed and Shorts the channel name may show instead |
| All | Call to action | from a list | 1 | Not covered on the specs pages |

**Video / YouTube**

Video action campaigns were upgraded to Demand Gen: no new ones since April 2025, the last ones converted by April 2026. For a video brief with a conversion goal, write to the Demand Gen video row above. The old VAC limits (headline 30, long headline 90, description 90, CTA 10) only matter when editing a legacy account's history.

| Format | Field | Limit | Notes |
|---|---|---|---|
| Demand Gen video (in-stream, in-feed, Shorts) | see Demand Gen | 40 / 90 / 90 | The default for video copy |
| Skippable in-stream (help page 6055025) | Headline or description / CTA | 15 / 10 | Conflicts with the 40-char Demand Gen video headline; check the form |
| In-feed (in-video ads on YouTube) | Headline / description | 2 lines x 40 / 2 lines x 35 | Headlines may not show on desktop and TV watch pages |
| Masthead | Headline / description / CTA | 40 / 60 / 15 | |
| Bumper (6 s, non-skippable) | no text fields documented | | Copy is the script and on-screen text; the companion banner is an image (300x60) |
| Display URL | not documented | | Must match the domain people land on |

Skippable ads can be skipped after 5 seconds.

**App campaigns**

| Field | Limit | Count | Notes |
|---|---|---|---|
| Headline | 30 | up to 5 | Min not documented; store listing assets are added automatically |
| Description | 90 | up to 5 | |

**Shopping: Merchant Center feed** (product data, not ad copy)

| Field | Limit | Notes |
|---|---|---|
| `title` | 150 | Users notice the first 70 or fewer, depending on screen: product name and brand first, then variant (size, color) |
| `description` | 5,000 | Most important details in the first 160-500; only the product itself |

**Dynamic text** (Search)

| Syntax | Where | Limit rule |
|---|---|---|
| `{KeyWord:Default}` | headlines, descriptions, paths; not final URL | The ad cannot exceed 30/90/15 with the keyword inserted. When the keyword does not fit, the default shows (API customizer doc), so the default itself has to fit the field |
| Case: `keyword` lower, `Keyword` first letter, `KeyWord` each word, `KEYWord` first word caps, `KeyWORD` last word caps | | Inserts the keyword, not the search term |
| `{CUSTOMIZER.Name:Default}` | RSA text | Needs values or the ad cannot be reviewed |
| `{LOCATION(City):Default}` (City, State, Country) | RSA text | Default shows when location is unknown |
| `{COUNTDOWN(yyyy-MM-dd HH:mm:ss,daysBefore)}`, `GLOBAL_COUNTDOWN` | RSA text | Renders up to 8 characters; starts 5 days before by default; add 3+ headlines without it |

**Text Google writes for you.** Automatically created assets, now "text customization" inside AI Max for Search (campaigns using it move to AI Max from September 2026), and final URL expansion in Performance Max generate extra headlines and descriptions from the landing page and existing assets. They serve next to the client's copy and are marked "Google AI" in the asset report. Ask the client whether they want this on: generated lines can contradict brand voice, legal wording or the offer, and the copywriter is blamed for them. If it stays on, review the previews and the asset report.

## What to deliver

One table per asset type, so the deliverable pastes into Google Docs and the counter script and the reviewer can check each line. For double-width scripts give the weighted count (CJK = 2). For dynamic text, count the rendered default and keep the code in the text column.

Headlines (limit 30)

| # | Text | Chars/limit | Pin | Role |
|---|---|---|---|---|
| H1 | Bike Repair in Lisbon | 21/30 | 1 | keyword |
| H2 | Same-Day Fix or It's Free | 25/30 | | offer |
| ... | | | | |

Use the same columns for descriptions (90), paths (15), sitelinks (link text 25 plus two description columns of 35), callouts (25) and snippet values (25); leave Pin empty where pinning does not exist.

- **Search RSA:** 15 headlines (about 3 keyword, 3 benefit, 2 offer, 2 proof, 2 CTA, 1-2 brand), 4 descriptions, 2 paths. Pin only when needed (legal text, brand rule), and then pin 2-3 alternatives to the slot so it still rotates. Plus: 6-8 sitelinks with both description lines, 6-10 callouts, 1-2 structured snippets with 4+ values, business name; price, promotion, lead form only if the brief has them.
- **Performance Max:** 15 headlines (at least one of 15 or fewer), 5 long headlines, 5 descriptions, business name, CTA suggestion, 2 paths, and up to 50 search themes when asked.
- **Display:** 5 short headlines, 1 long headline, 5 descriptions, business name.
- **Demand Gen:** image: 5 headlines (40), 5 descriptions; carousel: 1 headline, 1 description (40), one card headline per card; video: 5 headlines, 5 long headlines, 5 descriptions; business name.
- **Video:** Demand Gen video assets (5 headlines of 40, 5 long headlines, 5 descriptions, business name) plus a script with timings (0-5 s, rest, end card). Masthead or in-feed only when the brief names them.
- **App:** 5 headlines, 5 descriptions.
- **Shopping:** title and description per product, title front-loaded within the first 70.

## Best practices

- Write each headline as a full thought: Google may show it alone or next to any other, so one that needs another to make sense breaks the ad.
- Cover different angles (keyword, benefit, offer, proof, CTA, brand): Google avoids redundant combinations, so near-duplicates are wasted slots and lower Ad Strength.
- Put the main keyword in at least one headline, intact in a single headline: it shows relevance; a keyword over 30 belongs in a description.
- Make descriptions add what headlines cannot (detail, reasons, conditions), not repeat them: they show under any headline set.
- Write the first 3 headlines so they read well together and put must-show text there: H1, H2 and D1 are the only guaranteed positions.
- Pin sparingly: each pin cuts combinations. If a slot must be pinned, rotate 2-3 different headlines in it.
- In Performance Max, include one headline of 15 characters or fewer: Google asks for it so short placements have something to show.
- Match the landing page: an offer, price or product in the ad must be easy to find there, or the ad is disapproved and the click wasted.
- Fill sitelink descriptions: without them sitelinks use smaller formats.
- In video, show the brand and the promise in the first 5 seconds: viewers can skip after that, and bumpers (6 s) have only that.

## Policies and restrictions

Each rule below is a common reason for disapproval; a disapproved asset stops serving until it is fixed and re-reviewed.

- **Capitalization:** standard case. Google's own violations are "FLOWERS" and "FlOwErS"; common abbreviations like "ASAP", coupon codes, brand and product names may use non-standard case (after a review request). Shouting a word in caps reads as spam and is rejected.
- **Punctuation and symbols:** use them for their normal purpose. Disallowed: emoji (strip them from copy reused from Meta or other social ads), repeated punctuation ("flowers!!"), letters or numbers swapped for look-alikes ("fl@wers", "f1owers"), decorative bullets or asterisks ("*flowers*"), gimmicky dots ("F.L.O.W.E.R.S."), non-standard superscripts, single-byte katakana. An asterisk for a star rating ("5* hotel") or for legally required conditions is accepted only after a review request, so prefer writing the condition out.
- **Style and clarity:** commonly accepted spelling and grammar, the informational style of search results. Disallowed: bullet points or numbered lists in ad text, cut-off or incomplete text, vague or generic promotions, and generic CTAs like "click here" that could fit any ad. Double-width text over the limit is also rejected.
- **Spacing:** no missing or extra spaces ("F R E E", "Buy.Now").
- **Repetition:** no gimmicky or needless repetition of names, words or phrases, within an asset or across assets in the same ad group, campaign or account, and no asset that repeats the ad text. Repeating the advertiser or product name is Google's own example: say the brand once, in the brand headline or business name.
- **Phone numbers:** never in headlines or descriptions; use a call asset.
- **Business name:** the domain, the recognized business name or the promoted app, and it must relate directly to the landing page domain. Disallowed: generic or place-plus-service names ("Mountain View Plumber"), promotional names ("Sale at Acme Home Services"), extra symbols. Authorized resellers qualify the brand ("Acme of San Antonio"); affiliates and intermediaries cannot use the brand name alone.
- **Trademarks:** competitors' marks in ad text are restricted when the owner complains; resellers and informational sites can use them if the page makes that clear. Ask the client before naming another brand.
- **Claims and superlatives:** Google's current pages do not mention "best" or "#1" by name, but misrepresentation forbids inaccurate claims and improbable results presented as likely. Use a superlative or ranking only with a source the landing page shows (award, review score, survey); otherwise state the fact behind it. Flag every such claim for the client.
- **Restricted categories:** healthcare and medicines, financial services, gambling, alcohol (and others) need certification or country-specific rules. Check the policy for the client's country before writing and flag it in the deliverable.
- **Prices and offers:** state full costs and conditions; an offer missing at the destination is an "unavailable offer". The promo code field takes only codes.

## Language notes

- **Expansion:** 30 characters is tight. Portuguese, Spanish, French and German usually run longer than English (rule of thumb, not a Google figure): "Bike Repair" 11 vs "Reparação de Bicicletas" 23 vs "Fahrradreparatur" 16 in one word. Write natively in the client's language instead of translating English headlines, and expect fewer words per headline.
- **Accents count as one** (ç, ã, é, ü): the counter must count characters, not bytes.
- **Double-width:** Chinese, Japanese and Korean count 2 each; sitelinks and callouts are 12 double-width characters. Use full-width katakana: single-byte katakana is disapproved.
- **Keyword insertion:** check how inserted keywords read in languages with gender, case or declension; a keyword dropped into a sentence may break grammar. Prefer it where it stands alone ("{KeyWord:Bike Repair} Lisbon").
- **Countdown** language follows the ad text and cannot be changed.

## Pitfalls

- Headlines that only work in sequence ("Looking for a Fix?" + "We Have It"): Google will show them apart.
- Fifteen headlines that are the same idea reworded: counts as one, wastes slots, lowers Ad Strength.
- Pinning one headline to each slot: turns the RSA into a fixed ad and unpinned assets never show.
- Counting `{KeyWord:Default}` syntax instead of the default text, or a default that pushes past 30.
- Writing long copy for "description" in Demand Gen carousel (40, not 90) or for skippable in-stream (15).
- Brand or URL in every headline: one brand headline is enough; the display URL already shows the domain, and repeated names break the repetition policy.
- Callouts that repeat headlines or sitelinks: each asset should add something new.
- Copy reused from social ads: emoji, bullet lists and "click here" all get disapproved here.
- Merchant Center titles starting with filler ("New! Great Deal on..."): the first 70 characters are what people see, and promotional text in titles is not allowed.

## Example

RSA headlines for a bike repair shop in Lisbon.

Good:

| # | Text | Chars/limit | Role | Why |
|---|---|---|---|---|
| H1 | Bike Repair in Lisbon | 21/30 | keyword | Keyword intact, stands alone |
| H2 | Same-Day Fix or It's Free | 25/30 | offer | Concrete promise the page must honor |
| H3 | Rated 4.9 by 1,200 Riders | 25/30 | proof | Checkable, no superlative |

Each makes sense alone and with the other two in any order, and each adds a different reason to click.

Bad:

| # | Text | Chars/limit | Why |
|---|---|---|---|
| H1 | BEST Bike Repair in Lisbon!! | 28/30 | Caps for emphasis, repeated "!", unsupported superlative: disapproval risk |
| H2 | Lisbon Bike Repair Shop | 23/30 | Same idea as H1: Google treats it as redundant |
| H3 | Call 21 123 4567 Today | 22/30 | Phone number in ad text is disapproved; use a call asset |

## Sources

- https://support.google.com/google-ads/answer/7684791 (RSA: 30/90/15 limits, 3-15 headlines, 2-4 descriptions, pinning, Ad Strength, double-width)
- https://support.google.com/google-ads/answer/1704389 (limits are the same in every language; CJK counts as 2)
- https://support.google.com/google-ads/answer/14528373 (Performance Max text assets and counts)
- https://support.google.com/google-ads/answer/14767319 (Performance Max search themes, up to 50 per asset group)
- https://support.google.com/google-ads/answer/7005917 (responsive display ads)
- https://support.google.com/google-ads/answer/17140672 (Demand Gen image and carousel)
- https://support.google.com/google-ads/answer/17141078 (Demand Gen video)
- https://support.google.com/google-ads/answer/15110871 (video action campaigns upgraded to Demand Gen, last ones by April 2026)
- https://support.google.com/google-ads/answer/17091270 (video ad specs: in-feed, Masthead, legacy video action)
- https://support.google.com/google-ads/answer/6055025 (skippable in-stream, skip after 5 seconds)
- https://support.google.com/google-ads/answer/9948381 (App campaign assets)
- https://support.google.com/google-ads/answer/2375416 (sitelinks)
- https://support.google.com/google-ads/answer/6079510 (callouts)
- https://support.google.com/google-ads/answer/6280012 (structured snippets, header list)
- https://support.google.com/google-ads/answer/7065415 (price assets)
- https://support.google.com/adspolicy/answer/7048464 (price asset requirements: no prices or sales wording in header/description, legal qualifiers exempt)
- https://support.google.com/adspolicy/answer/7374309 (promotion asset requirements)
- https://support.google.com/google-ads/answer/16726130 (lead form fields)
- https://support.google.com/google-ads/answer/6099637 (call assets: phone verification)
- https://support.google.com/adspolicy/answer/14847993 (business name requirements: generic, place-based, promotional, resellers)
- https://support.google.com/adspolicy/answer/12499303 (business information requirements)
- https://support.google.com/google-ads/answer/6371157 (keyword insertion syntax and limits)
- https://support.google.com/google-ads/answer/6193743 (countdown customizer)
- https://developers.google.com/google-ads/api/docs/ads/customize-responsive-search-ads (customizer, location syntax, keyword insertion default fallback)
- https://developers.google.com/google-ads/api/reference/rpc/v26/SitelinkAsset (sitelink description 35, both lines required)
- https://developers.google.com/google-ads/api/reference/rpc/v26/StructuredSnippetAsset (3-10 values, 25 each)
- https://support.google.com/google-ads/answer/11259373 (text customization in Search and AI Max: generated headlines and descriptions)
- https://support.google.com/merchants/answer/6324415 (product title: 150, first ~70 seen)
- https://support.google.com/merchants/answer/6324468 (product description: 5,000)
- https://support.google.com/adspolicy/answer/6021546 (editorial policy overview)
- https://support.google.com/adspolicy/answer/14848295 (capitalization: FLOWERS, FlOwErS; ASAP and coupon codes)
- https://support.google.com/adspolicy/answer/14847994 (punctuation and symbols: emoji, look-alikes, decorative asterisks, single-byte katakana)
- https://support.google.com/adspolicy/answer/14848297 (style and spelling: lists, cut-off text, "click here")
- https://support.google.com/adspolicy/answer/14848296 (repetition: ad group, campaign, account; names)
- https://support.google.com/adspolicy/answer/6020955 (misrepresentation, unreliable claims)
- https://support.google.com/adspolicy/answer/6118 (trademarks)
