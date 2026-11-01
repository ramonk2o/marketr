# Channel: email

Marketing and lifecycle email copy (newsletter, promotional, launch, nurture, cart, reactivation, transactional): fields, structure, deliverability rules that touch the copy, and per-client format decisions.

Verified: 2026-11-01

## Pieces and fields

"Hard" = a technical or official limit. "Observed" = vendor tests that vary by device, font size, app version and the user's settings. Treat observed numbers as ranges, never as promises.

| Field | Hard limit | Visible before truncation | Notes |
|---|---|---|---|
| From name | None practical (RFC 5322 line 998 chars, folded) | Observed: roughly 20-25 chars on mobile lists | Recognition matters more than length. Gmail: no subject content and no recipient's name in the display name. |
| Subject line | None practical (998-char header lines, folded); some ESPs cap it | Observed: ~30-48 chars on phones (Gmail app ~30-37, iPhone Mail ~41-48); ~60-88 on desktop Gmail depending on width | Front-load the point in the first ~30-35 chars; the rest is a bonus for desktop. |
| Preheader / preview text | None hard | Litmus: from 0 up to ~278 chars (5 lines on some clients); recommended under 90 | If missing, clients pull the first body text, alt text or links ("View in browser", "Logo"). Some users turn snippets off. Apple Mail with Apple Intelligence may show a generated summary instead (Litmus); Gmail's Gemini summaries work similarly. |
| Body | None hard. Observed, widely consistent: Gmail clips HTML over ~102KB (not documented by Google; image files don't count, their code does) | Mobile first screen: observed roughly the first 2-4 short lines after the header | Clipping hides the end of the email, often the unsubscribe link and footer CTA. |
| Button (CTA) | None | Observed: buttons over ~25 chars wrap to two lines on phones | Verb + outcome. |
| Image alt text | None | Shown when images are blocked or not yet loaded | Some clients use it as preview text if it comes first. |
| Plain-text part | None | Shown by text-only clients, watches, some screen readers | Many ESPs auto-generate it; it often comes out messy. |
| Footer | Legal minimums by country (see Policies) | n/a | Unsubscribe link, sender identity, postal address where required. |

## What to deliver

- 3-5 subject lines, each paired with its preheader, with a one-line note on the angle (curiosity, benefit, urgency, news) so the client can A/B test meaningfully.
- From name, only if new or changing; otherwise reuse the agreed one.
- Body by labeled blocks (e.g., `[Header]`, `[Opening]`, `[Body]`, `[Offer]`, `[CTA]`, `[PS]`, `[Signature]`), so the designer or ESP template can map them.
- Button text for each CTA, plus the destination it should point to if known.
- Alt text for every image that carries meaning; mark decorative images as `alt=""`.
- Personalization tokens in the client's ESP syntax, each with its fallback.
- Plain-text notes: anything that needs rewriting for the text version (e.g., button becomes "Shop the sale: <link>").
- For sequences: a campaign brief (channel `brief`) with each email's trigger/delay, goal and exit condition, plus one file per email, following the project's one-file-per-piece convention.

## Format agreement

Agree these once per client and save them in the client's `channels.md`: every later email then starts from the same decisions, and the user is not asked the same questions twice. When the client's past emails are in the knowledge base or `_in/`, infer each decision from them and propose it ("Your last 6 newsletters average ~250 words, one button, signed by Ana. Keep that?"). Asking in the abstract ("How long should emails be?") gets vague answers; a concrete proposal gets a fast yes or a useful correction.

| Decision | Default options to propose |
|---|---|
| Length per type | Short (50-125 words) for promo/cart/reactivation; medium (150-300) for nurture/launch; long (300-700+) for content newsletters |
| Block structure | Header, opening, body, offer, CTA, PS, signature; or a lighter "letter" format (no header image, signed by a person) |
| Number of CTAs | One primary CTA repeated (top + bottom) for promos; several equal links for curated newsletters |
| Sender and signature | Brand name; person at brand ("Ana from Acme"); person only (founder-led) |
| Emojis in subject | None; occasional, one at most; regular, as part of the brand voice |
| Personalization | None; first name in greeting only; first name + behavior (last product, city) |
| Subject tone | Direct/benefit; curious/teasing; news-style; conversational lowercase |
| Images carrying text | Never (all text live); hero only, with the same words repeated in live text; designer-led |
| ESP and merge tags | e.g., Mailchimp `*|FNAME|*`, Klaviyo `{{ first_name|default:"there" }}`, HubSpot `{{ contact.firstname }}`, RD Station, Brevo; record the exact syntax and fallback support |
| Language/locale | Language, formal vs informal address, date and currency format |

## Structures by type

Lengths are starting points to propose, not rules; the client's past performance overrides them.

- **Newsletter (content):** header > short opening (why this issue matters) > 1 main story or 3-5 curated items, each with its own link > optional promo slot > sign-off. 300-700 words. Readers come for value; the promo slot stays small or they learn to ignore the whole email.
- **Promotional / offer:** offer in the first screen > 1-3 reasons or proof > CTA > terms (deadline, conditions) > PS restating the deadline. 50-150 words. Most readers decide in seconds; the offer and the deadline must survive a skim.
- **Launch:** news-style hook > what it is in one sentence > 3 benefits > proof or demo > CTA > PS. 150-300 words. Often a sequence: teaser, launch day, reminder, last call.
- **Nurture / sequence:** one idea per email > short story or example > soft CTA (read, reply, watch) > signature from a person. 150-300 words. Each email has one job; stacking several ideas makes the sequence harder to measure and to fix.
- **Abandoned cart:** reminder of the item (name, image, price) > reassurance (shipping, returns, support) > single CTA back to cart. 30-100 words. The reader already decided once; friction removal beats persuasion. Incentives only if the client agreed, since they teach buyers to abandon carts.
- **Reactivation / win-back:** honest acknowledgment of the silence > what is new or a reason to return > clear choice: stay (CTA) or leave (unsubscribe link prominent). 50-120 words. Removing people who will never engage protects the spam rate and sender reputation.
- **Transactional (receipt, shipping, password, account):** the facts first (what happened, what to do, order number) > support contact. Keep it free of promotion: Gmail says not to mix types, and under CAN-SPAM a mixed email whose subject or opening reads as promotional is treated as commercial and loses the transactional exemption. Similar rules exist elsewhere; check the client's country.

## Best practices

- Front-load subject lines: the first ~30-35 characters are what most phone users see.
- Make the preheader continue the subject, not repeat it: they are read as one line in many inboxes, so repetition wastes the second-best slot.
- Always write the preheader explicitly: otherwise the client shows "View in browser" or alt text, which wastes the slot.
- Put the main point and the CTA in the first screen on mobile: most opens are on phones and many readers never scroll.
- State the point plainly in the first body lines: Apple Intelligence and Gmail's Gemini can replace the preheader with an AI summary built from the body, so a teasing or vague opening produces a vague summary.
- Short paragraphs (1-3 lines on mobile) and one idea per block: phone screens turn a 5-line desktop paragraph into a wall.
- One primary action per email (it can appear more than once): several competing CTAs split clicks and make results hard to read.
- Button copy says what happens next ("See the 3 plans", "Get my discount") rather than "Click here" or "Submit": it tells the reader what they get, and it works as link text for screen readers.
- Keep key words, prices and deadlines in live text, not inside images: images may be blocked, unloaded, or inverted in dark mode, and live text is readable, searchable and accessible.
- Write alt text that carries the image's message ("30% off all boots until Sunday"), not its description ("banner image"): it is what blocked-image readers and screen readers get.
- Prefer a real, consistent From name: recognition of the sender is a main reason people open, and Gmail asks messages in the same category to use the same From address.
- Keep total HTML well under ~102KB (the designer's job, but long copy contributes): Gmail is observed to clip beyond that, hiding the footer and unsubscribe link.
- Every personalization token gets a fallback ("Hi there" when the name is empty): otherwise readers see "Hi ," or a raw tag.
- Check the plain-text version reads on its own: some clients and devices show only it.
- Dark mode: avoid copy that relies on color alone ("the items in red"), and flag to the designer any text inside images or dark logos on transparent backgrounds, which can disappear on dark backgrounds.

## Policies and restrictions

- **Gmail and Yahoo bulk senders (5,000+ messages/day to Gmail; Yahoo applies the same idea to bulk senders), in force since 2024:** marketing and subscribed messages need one-click unsubscribe (RFC 8058 headers) plus a clearly visible unsubscribe link in the body; unsubscribes honored within 48 hours (Gmail recommends) / 2 days (Yahoo requires); spam complaint rate kept below 0.10% and never at 0.30% or higher (Yahoo: below 0.3%). Gmail ramped up enforcement with rejections from November 2025. Transactional messages are excluded from the one-click requirement. Copy impact: never hide, shrink or disguise the unsubscribe link; a frustrated reader who cannot find it presses "Report spam", which counts against the client far more than an unsubscribe.
- **Microsoft (Outlook.com/Hotmail/Live):** since 5 May 2025, domains sending 5,000+ messages/day must pass SPF, DKIM and DMARC; non-compliant mail is rejected with "550 5.7.515". Copy impact is indirect: the authentication is the ESP's job, but the visible From address must be the authenticated domain.
- **Content rules from Gmail's guidelines:** headers and content must not be misleading; no "Re:" or "Fwd:" unless it is a real reply or forward; no subject content in the display name; no hidden text via HTML/CSS; links visible and easy to understand; no promotions inside receipts.
- **"Spam words" are mostly myth:** no major mailbox provider publishes a banned-word list. Filtering is driven by authentication, sender reputation, complaints and engagement. What does hurt in copy: deceptive subjects, fake reply prefixes, hidden text, all-image emails with little live text (look like spam and say nothing when images are off), link text that does not match the destination, URL shorteners, and sending to people who never asked. A word like "free" in an honest email to an engaged list is fine.
- **Consent and legal footer, by country (brief; not legal advice):**
  - US, CAN-SPAM: opt-out model (no prior consent needed), but truthful headers and subject, a valid postal address, an opt-out that keeps working for at least 30 days after sending and is honored within 10 business days, and a clear disclosure that it is an ad (not required when the recipient gave prior affirmative consent, 15 U.S.C. 7704(a)(5)(B)). Penalties apply per violating email, so one bad send to a large list is costly.
  - EU/UK, GDPR + ePrivacy/PECR: prior consent for marketing to individuals, except the "soft opt-in" for existing customers about similar products with an opt-out at collection and in every message; identify the sender and give an opt-out every time.
  - UK: the Data (Use and Access) Act 2025 added a charitable-purposes soft opt-in for registered charities (in force 5 February 2026, for contacts collected from then on); ICO guidance is being updated, so check the current ICO page.
  - Germany: double opt-in (confirmation email before the first marketing send) is expected in practice to prove consent.
  - Brazil, LGPD: marketing needs a valid legal basis (consent or legitimate interest), clear identification and an easy opt-out; consumer-protection rules also apply.
  - Other countries have their own rules (e.g., Canada's CASL is consent-based). The client's own legal restrictions, required disclaimers and regulated claims live in their `company.md`; read it before writing offers, health, finance or guarantee claims.

## Language notes

- Text expansion: German, French, Spanish and Portuguese often run noticeably longer than English for the same message, so a subject that fits in English may lose its key word in translation. Rewrite to front-load, do not just translate.
- Accents and non-Latin scripts are fine in subject, preheader and from name: modern ESPs encode them (RFC 2047). Test once if the client's ESP is old or custom; broken encoding shows as `=?UTF-8?...` or garbled characters.
- Emojis render differently per OS and some older clients show boxes; never put the key meaning in an emoji.
- Dates: write unambiguous dates ("Sunday, 8 November" / "domingo, 8 de novembro"), since 03/11 means different days in the US and elsewhere. Give time zone for deadlines when the list spans regions.
- Currency and numbers: use the locale's format (R$ 1.299,90 vs $1,299.90) and the currency symbol the audience expects.
- Formal vs informal address (tu/vous, du/Sie, você/o senhor) is a per-client decision; record it in `channels.md`.
- Personalization fallbacks must be grammatical in the language: gendered languages may need a neutral greeting instead of a name-based one.

## Pitfalls

- Subject and preheader that say the same thing: wastes the second line.
- Subject promising what the body does not deliver ("Your order", "Re: our meeting"): deceptive under Gmail guidelines and CAN-SPAM, and it trains readers to distrust the sender.
- The whole message in one image: unreadable with images off, invisible to screen readers, risky for filtering, and fragile in dark mode.
- Missing fallbacks: "Hi {{first_name}}," or "Hi ," in production.
- Fake urgency that repeats every week ("Last chance!"): readers stop believing deadlines.
- Promotional content added to receipts or password emails: can turn a transactional email into a commercial one legally and for filters.
- Long footers and heavy templates pushing the email past ~102KB: Gmail (observed) hides the unsubscribe link, which can drive spam reports.
- Writing for the desktop preview: the mobile reader sees a third of the subject and the first lines only.
- Hiding the unsubscribe link in reactivation emails, where people most want it.

## Example

Good subject + preheader (promotional, ESP Klaviyo):
- Subject: `Boots 30% off until Sunday`
- Preheader: `All sizes back in stock, free returns on every pair.`
- Why: the offer and deadline fit in 26 characters, so they survive any phone; the preheader adds new information (stock, free returns) that removes a common objection.

Bad subject + preheader:
- Subject: `Re: Hey {{ first_name }}!!! You won't BELIEVE this 🔥🔥🔥`
- Preheader: (empty, so the inbox shows "View this email in your browser | Logo")
- Why: fake "Re:" is deceptive and named in Gmail's guidelines; the token has no fallback; the key information never appears; the empty preheader wastes the slot.

Good body excerpt (labeled blocks):
```
[Opening] Hi {{ first_name|default:"there" }}, your size is back.
[Offer] Every boot is 30% off until Sunday, 8 November, 23:59 (CET).
[CTA button] Find my size
[PS] Returns are free for 60 days, so you can try two sizes at home.
```
Why: the offer and the deadline are in the first two lines in live text, the token has a fallback, the button says what happens, and the PS answers the main objection for skimmers who jump to the end.

Bad body excerpt:
```
[Image: banner with "30% OFF EVERYTHING" baked in, alt="banner"]
Dear valued customer, we are excited to announce that for a limited time
we are offering an amazing discount on our entire range of products...
[Button] Click here
```
Why: the offer lives only in the image (lost with images off and in screen readers), the alt text says nothing, the opening delays the point with filler, and "Click here" tells the reader nothing.

## Sources

- https://support.google.com/a/answer/81126 (Gmail sender guidelines: bulk sender rules, spam rate 0.10%/0.30%, one-click unsubscribe, visible unsubscribe link, no deceptive headers, no fake Re:/Fwd:, no hidden content, don't mix promotional and transactional content, consent)
- https://support.google.com/a/answer/14229414 (Gmail sender FAQ: unsubscribe within 48 hours, transactional messages excluded from one-click requirement, enforcement dates)
- https://senders.yahooinc.com/best-practices/ (Yahoo: spam rate below 0.3%, one-click unsubscribe, honor unsubscribes within 2 days, visible unsubscribe link)
- https://www.rfc-editor.org/rfc/rfc8058 (one-click unsubscribe headers: List-Unsubscribe with HTTPS URI + List-Unsubscribe-Post, DKIM-signed)
- https://www.rfc-editor.org/rfc/rfc5322 (header lines max 998 characters; long headers can be folded)
- https://www.litmus.com/blog/the-ultimate-guide-to-preview-text-support (preview text: up to ~278 characters / 5 lines shown on some clients, recommend under 90; missing preview text is pulled from body, alt text or links; Apple Intelligence summaries can replace it)
- https://www.emailonacid.com/?p=26940 (observed: Gmail clips messages over ~102KB and shows "View entire message"; not documented by Google)
- https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business (CAN-SPAM: truthful headers and subject, ad disclosure, postal address, opt-out working 30 days and honored within 10 business days, per-email penalties, primary purpose test for transactional)
- https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/ (UK/EU-style consent and soft opt-in)
- https://www.buzzstream.com/blog/email-subject-line-length/ and https://www.emailtooltester.com/en/blog/email-subject-lines-character-limit/ (observed subject truncation by client; vendor tests, not official)
- https://substrate.office.com/ip-domain-management-snds/Postmaster/Policies (Outlook.com high-volume sender requirements)
- https://support.microsoft.com/en-us/outlook/fix-ndr-error-550-5-7-515-in-outlook-com (5,000+ threshold, SPF/DKIM/DMARC, 550 5.7.515 rejection)
- https://www.law.cornell.edu/uscode/text/15/7704 (CAN-SPAM: ad identification not required with prior affirmative consent)
- https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/the-charitable-purpose-soft-opt-in/ (UK charitable-purposes soft opt-in)
