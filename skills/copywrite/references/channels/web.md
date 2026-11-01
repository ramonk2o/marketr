# Channel: web

Copy for website pages (home, about, product/service, category, FAQ, contact) and landing pages (lead capture, sales, event signup, waitlist, thank-you).

Verified: 2026-11-01

## Pieces and fields

| Field | Hard limit | Visible / truncation | Notes |
|---|---|---|---|
| Title tag | None (Google) | Truncated by device width, not a character count | Front-load the distinctive words; unique per page; site name at the end with a delimiter is a sensible default (Google accepts it at the start or end), and the home page title can carry a fuller description. Google may rewrite it from the H1, visible title, anchors or og:title when it is vague, stuffed or off-topic. |
| Meta description | None (Google) | Truncated by device width | Unique per page; a short pitch with concrete details (price from, hours, who it is for). Often replaced by page text, so the opening paragraph matters too. |
| H1 | None | Fully visible | One per page is the convention; usually the hero headline. Keep it consistent with the title, since Google uses both. |
| H2/H3 | None | Visible | Start with the words carrying the information: scanners read the first two words. Order does not affect Search but matters for screen readers. |
| URL slug | None practical | Shown in results as breadcrumbs | Readable words in the audience's language, hyphens, short. Keywords here have hardly any ranking effect, so do not stuff. |
| Image alt | None | Not visible (read aloud) | Describe what the image conveys; empty for decorative; for an image link, describe the destination. |
| og:title / og:description | Platform-dependent | Shown on social share cards | Can differ from title tag for social; draft only if the client shares pages socially. |
| Button / CTA | Template-dependent | Visible | Verb + outcome. Visible text must be part of the accessible name (speech users say what they see). |
| Form labels, hints, errors | Template-dependent | Visible | Label every field in visible text; errors say what is wrong and how to fix it, next to the field. |
| Builder blocks | Set by the CMS/template | Overflow breaks layout | Character limits per block live in channels.md; respect them over ideal copy. |

## What to deliver

Copy by section, in page order, each block labeled, no layout code:

```
Page: <name> | Type: <type> | Goal: <one action> | Traffic source: <ad/email/organic>
SEO: Title / Meta description / Slug / H1 (if different from hero)
[Hero] Headline / Subheadline / CTA / Microcopy under CTA
[Problem] H2 / body
[Solution] ...
[Proof] ...
[FAQ] Q / A pairs
[Final CTA] Headline / CTA
Forms: field labels, hints, error messages, button, privacy line
Alt text: <image> -> <alt>
Notes: claims to verify, numbers from the client, assumptions
```

Give approximate word counts per block when the user is filling a template. Offer one alternative headline for the hero; more alternatives dilute the review.

## Format agreement

Agree once per client, save in channels.md, and reuse. Infer first: if the client has a site, read it and propose a block skeleton with approximate sizes ("Hero 10-word headline + 25-word sub, 3 benefit cards of ~20 words, 3 testimonials, 6 FAQs, ~600 words total"). Concrete proposals get faster, better answers than abstract questions.

| Decision | Default options |
|---|---|
| Page length by type | Short (one or two screens) / medium / long-form. Default by awareness and risk, see below. |
| Blocks and order | Standard skeleton per type (below) / client's existing template order. |
| Headline style | Outcome-led ("Payroll done in 10 minutes") / problem-led / direct label ("Accounting for clinics"). Default: outcome-led for landing, direct for site pages. |
| CTA wording and count | One primary CTA repeated after key blocks / primary + one secondary (e.g., "See pricing"). Default: one goal, repeated. |
| FAQ | Yes for sales, service and product pages / no for thank-you and short lead pages. |
| Proof placement | Near hero (logos, rating) + full block mid-page + next to the final CTA. |
| Microcopy tone | Plain and neutral / brand voice. Default: plain; errors are never witty. |
| CMS / builder constraints | Fixed blocks with character limits, number of cards, whether H1 is editable, whether meta fields exist. |
| SEO priority | High (organic page) / low (paid-traffic landing page, often noindex). |

Length heuristic: the less aware the reader (does not know the problem or the solution) and the higher the price or risk, the more the page must explain and prove, so the longer it gets. A known product at low risk to a warm audience needs a short page; extra copy only delays the click.

## Structures by page type

- **Home** (medium): Hero (who it is for + main outcome) / what you offer (2-4 paths to key pages) / proof / how it works / final CTA. Its job is routing many audiences, so it introduces and sends people to deeper pages rather than selling everything.
- **About** (short-medium): why the company exists / who is behind it / track record / values shown as facts / CTA. Visitors come to judge trust; specifics beat mission slogans.
- **Product / service** (medium-long): Hero / problem / solution and how it works / 2-6 benefit highlights / details or specs / proof / pricing or "how to buy" / FAQ / final CTA. This is where the decision happens, so objections get answered here.
- **Category** (short): H1 + 1-3 sentences that help choose between items, optional buying guidance below the list. Shoppers came for the list; long text above it pushes products down.
- **FAQ** (as needed): real questions grouped by topic, answer in the first sentence, link to the detailed page. People arrive with one question; make each answer findable and self-contained.
- **Contact** (short): what to contact you for / channels with response time / form / address and hours. Response time sets expectations and reduces duplicate messages.
- **Lead capture** (short): Hero with the offer (what they get) + form / 3 bullets of what is inside / one proof element / privacy line. The exchange is small; the form should be visible without scrolling.
- **Sales, short form** (warm audience, low price): Hero / benefits / proof / offer + price / guarantee / CTA / short FAQ.
- **Sales, long form** (cold audience or high price): Hero / problem / agitation with specifics / mechanism (why this works when others failed) / benefits / proof / offer stack / price / guarantee / objections FAQ / final CTA, with the CTA repeated after each major block. Length earns its place only if every block answers a doubt.
- **Webinar / event signup** (short): what they will learn (3 bullets) / date, time with time zone, duration, format / speaker credibility / form. Clear logistics let people decide and put it in their calendar, so state date, time, time zone and duration plainly.
- **Waitlist** (short): what is coming / why join now (early access, price) / expected timing if known / email field. Honest timing protects trust at launch.
- **Thank-you** (short): confirm the action / exactly what happens next and when / one next step (add to calendar, check inbox, follow). The visitor is at peak attention; a dead end wastes it.

## Best practices

- One goal per landing page, and no competing links or menus where the builder allows: every extra exit is a chance to leave without converting.
- Message match: the hero repeats the promise and wording of the ad or email that brought the visitor, and the CTA mirrors the ad's call to action. Google Ads judges the landing page on relevance to the ad; visitors who do not recognize the promise bounce.
- Put the offer, who it is for and the primary CTA above the fold: in NN/g's 2018 eyetracking, about 57% of viewing time was above the fold and 74% within the first two screenfuls.
- Headline says the outcome, subheadline says how or for whom, CTA says the action: a reader who stops at the hero should still know what this is and what to do.
- Write for scanning: front-load the most important point in the first two paragraphs, start headings and bullets with information-carrying words, keep paragraphs to 1-3 sentences, bold sparingly. NN/g found most users scan, and F-pattern scanning misses whatever sits lower and to the right.
- Write objectively: concrete facts and numbers instead of promotional superlatives. In NN/g's 1997 test the objective (non-promotional) version was 27% more usable, and hype reads as hype to skeptical buyers.
- CTA text = verb + what they get ("Get the price list", "Book a 20-minute call"), not "Submit" or "Click here": the button is the last thing read before acting and must state the deal. Add a line under it that removes the last fear ("No card required", "Reply within 1 business day").
- Descriptive links: link text names the destination ("See plans and prices"), not "here" or "read more". WCAG 2.4.4 requires the purpose to be clear from the link or its context, and screen-reader users often browse a list of links alone. In the EU the European Accessibility Act (applying since 2025-06-28) makes alt text, link text and form labels legal requirements for e-commerce.
- Proof is real, specific and attributable: full name, role or city, photo or company when permitted, and a concrete result. Vague, anonymous praise does not persuade and invented proof is illegal in most markets.
- Product descriptions as 2-6 feature highlights (short heading + one paragraph each), secondary features in a plain list after: Baymard found highlights get read more thoroughly than walls of text or feature dumps.
- Forms: ask only for what the next step needs, visible label on every field, hint text for formats, and errors next to the field that say what is wrong and how to fix it without blame. Every extra field and every vague error costs completions.
- SEO without stuffing: one clear topic per page, the main term in title, H1 and the opening naturally, synonyms elsewhere. Google treats keyword stuffing and hidden text as spam and rewrites stuffed titles.
- Alt text describes what the image shows or does in context; decorative images get none. It serves blind users first and image search second.

## Policies and restrictions

- Claims: anything measurable ("30% faster", "best in Brazil", "No. 1") needs evidence from the client; flag unverified claims in Notes instead of softening them silently. Advertising law in most countries treats unsupported claims as misleading.
- Prices and conditions: state price, currency, billing period, what is included, fees, contract length and cancellation terms clearly near the CTA. Brazil's CDC (art. 31, 37) requires clear, precise offer information and treats omitting essential data as misleading; in the EU a "was" price must be the lowest price of the prior 30 days, and since CJEU C-330/23 (Aldi Süd, 2024) a percentage discount must be computed from that same price (Directive 98/6/EC art. 6a).
- Testimonials: real customers, honest opinion, unedited meaning; disclose paid or gifted relationships; if a result is exceptional, say what is typical (FTC Endorsement Guides; similar rules elsewhere). In the US the FTC Rule on Consumer Reviews and Testimonials (16 CFR 465, in effect since 2024-10-21) bans fake or AI-generated testimonials and undisclosed insider reviews, with civil penalties. Never write placeholder testimonials that could ship as real; mark them `[TESTIMONIAL NEEDED]`.
- Environmental claims in the EU: since 2026-09-27 Directive 2024/825 bans generic claims ("eco-friendly", "green", "sustainable") unless what they mean is clearly specified on the same medium, restricts sustainability labels, and bans "carbon neutral"-type claims based on offsetting. Write the specific, provable fact instead ("packaging made of 80% recycled cardboard").
- Guarantees and urgency: only real deadlines, real limited stock, and guarantee terms the client will honor, stated in full. Fake countdowns get noticed and break trust.
- Privacy near forms: a short line by the submit button saying what the data is used for, with a link to the privacy policy. GDPR (art. 13) requires the purpose, controller and rights at the moment of collection; LGPD (arts. 8-9) requires clear information and consent for specific purposes, and generic authorizations are void. Marketing opt-ins are a separate, unticked choice, not bundled into the main button. This is copy guidance, not legal advice; the client's lawyer decides final wording.
- Client-specific restrictions (regulated sector, forbidden words, mandatory disclaimers) live in company.md; read it before writing.

## Language notes

- Text expansion: translations from English into European languages grow, and short strings grow most (IBM figures via W3C give the resulting length: up to 10 characters becomes 200-300% of the original, 2-3 times as long; over 70 characters about 130% of the original, roughly 30% longer). Buttons, menu items and fixed card blocks break first; write to the block's limit in the target language, not in English.
- Width is not character count: CJK text can have fewer characters but take more horizontal space, so check against the actual block.
- Local formats: currency symbol and position, decimal and thousands separators, date order, 12/24-hour time and time zone for events, phone formats with country code, address order.
- Slugs in the audience's language, hyphen-separated; non-ASCII characters get percent-encoded by the CMS, so prefer a transliterated slug if the client's CMS mangles accents.
- Formal vs informal address (tu/você/vous/Sie) is a brand decision; record it once and keep microcopy consistent with page copy.

## Pitfalls

- Clever headline that hides what the product is: visitors decide in seconds and will not decode it.
- Hero that does not match the ad or email: the click was on a promise the page does not repeat.
- Several equal CTAs ("Buy", "Book a demo", "Download", "Subscribe") on a landing page: choice splits attention.
- "We" copy (our mission, our team, our passion) instead of the reader's problem and outcome.
- Benefits that are features in disguise ("AI-powered") with no consequence for the reader.
- Same title tag or meta description on every page: Google cannot tell pages apart and rewrites them.
- Keyword lists in titles, alt text or a footer block: spam signal and unreadable.
- Generic "Submit", "Learn more", "Click here".
- Error messages like "Invalid input" or that clear the form.
- Long text above a category list or above a short lead form.
- Writing to ideal length and ignoring the builder's character limits: the page breaks on publish.
- Thank-you page that only says "Thanks!" with no next step.

## Example

Client: accounting firm for dental clinics; traffic from a search ad "Accounting for dental clinics - free tax review".

Good:
```
[Hero]
Headline: Accounting built for dental clinics
Subheadline: We review your last 12 months of taxes for free and show where your clinic is overpaying. Answer in 5 business days.
CTA: Get my free tax review
Microcopy: No commitment. We only need your last tax return.
```
Why: repeats the ad's promise and wording (message match), names who it is for, the concrete offer, a time frame, and a CTA that says what they get; the microcopy removes the main fear (being locked in).

Bad:
```
[Hero]
Headline: Excellence that transforms your future
Subheadline: We are a team of passionate professionals committed to quality and innovation.
CTA: Learn more
```
Why: no audience, no offer, no outcome; it ignores the free review the ad promised, so the visitor wonders if they landed on the wrong page; "we" copy talks about the firm; "Learn more" gives no reason to click and fails as descriptive link text.

## Sources

- https://developers.google.com/search/docs/appearance/title-link (no title length limit; truncated to device width; sources Google uses to rewrite titles; no repeated keywords, no vague "Home")
- https://developers.google.com/search/docs/appearance/snippet (no meta description limit; truncated to device width; unique per page; snippets mostly built from page content; no keyword lists)
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide (heading order does not matter to Search; no ideal heading count; keywords in URL have hardly any effect; meta keywords unused)
- https://developers.google.com/search/docs/crawling-indexing/url-structure (readable words, hyphens, audience language in URLs)
- https://developers.google.com/search/docs/appearance/google-images (descriptive alt text; keyword-stuffed alt can be seen as spam)
- https://developers.google.com/search/docs/essentials/spam-policies (keyword stuffing and hidden text are spam)
- https://support.google.com/google-ads/answer/6238826 (landing page should closely match the ad and mirror its call to action; key info near the top)
- https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/ (F-pattern scanning and the writing remedies)
- https://www.nngroup.com/articles/scrolling-and-attention/ (2018: about 57% of viewing time above the fold, 74% in the first two screenfuls)
- https://www.nngroup.com/articles/how-users-read-on-the-web/ (1997 study: 79% scanned; objective text 27% more usable; concise + scannable + objective 124%)
- https://www.nngroup.com/articles/error-message-guidelines/ (error messages: visible, near the field, plain, precise, constructive, no blame, keep input)
- https://baymard.com/research-articles/structure-descriptions-by-highlights (product descriptions by 2-6 feature highlights; only 22% of sites do it)
- https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html (2.4.4, level A: link purpose clear from text or its context)
- https://www.w3.org/WAI/WCAG22/Understanding/headings-and-labels.html (2.4.6, level AA: headings and labels describe topic or purpose)
- https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html (2.5.3, level A: accessible name contains the visible label)
- https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html (3.3.3, level AA: suggest the fix when known)
- https://www.w3.org/WAI/tutorials/images/decision-tree/ (alt text: decorative empty, functional describes action, informative conveys meaning)
- https://www.w3.org/International/articles/article-text-size (IBM expansion rates from English: short strings grow most)
- https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking (testimonials: honest, real experience, typical results, disclose connections)
- https://gdpr-info.eu/art-13-gdpr/ (GDPR: information owed at the time data is collected)
- https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm (LGPD arts. 8-9: specific consent, clear information)
- https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm (Brazil CDC arts. 31, 37: clear offer information; misleading by omission)
- https://eur-lex.europa.eu/eli/dir/1998/6/2022-05-28/eng (EU art. 6a: "was" price = lowest price in the prior 30 days; CJEU C-330/23 Aldi Süd extends it to percentage discounts)
- https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials (FTC rule 16 CFR 465: fake or AI-generated reviews and testimonials, undisclosed insider reviews banned; civil penalties)
- https://eur-lex.europa.eu/eli/dir/2024/825/oj/eng (EU Empowering Consumers for the Green Transition Directive: generic environmental claims, sustainability labels, offset-based neutrality claims; applies from 2026-09-27)
- https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en (European Accessibility Act covers e-commerce; applies from 2025-06-28)
