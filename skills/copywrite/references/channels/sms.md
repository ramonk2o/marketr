# Channel: sms

Text messages (A2P marketing and transactional SMS) in any country: encoding, segments, sender types, links, consent and timing.

Verified: 2026-11-01

## Pieces and fields

| Field | Hard limit | Visible | Notes |
|---|---|---|---|
| Body, GSM-7, single | 160 characters | Whole message (preview in lock screen/list shows ~1-2 lines, varies by phone) | Above 160 it splits. |
| Body, GSM-7, multi-part | 153 characters per segment | Reassembled as one message on the phone | 7 characters per segment go to the header. US/Canada toll-free: 152. |
| Body, GSM-7 with national shift table | 155 per single SMS with one table; 152 with two (locking + single) | Same | The header that selects the table takes space. Secondary sources; provider support varies. |
| Body, UCS-2, single | 70 characters | Same | Triggered by a single character outside GSM-7 (one ã, one emoji, one curly quote). |
| Body, UCS-2, multi-part | 67 characters per segment | Same | US/Canada toll-free: 66. |
| Extension characters | Each counts as 2 in GSM-7 | Shown normally | `€ [ ] { } ~ ^ \ |` and form feed. |
| Total length | Provider caps (e.g., Twilio 1,600 characters) | | Twilio recommends under 320 characters for deliverability. |
| Sender | Alphanumeric ID: up to 11 characters (letters, digits, space) | Shown as the sender name | Not available in US/Canada; one-way (no replies); registration required in some countries. |

Billing is per segment: 161 GSM-7 characters cost two messages; a 140-character message with one non-GSM character becomes UCS-2 and also costs two.

GSM-7 basic set, non-ASCII letters (the ones that are safe):
`à è é ì ò ù Ä ä Å å Æ æ Ç É Ñ ñ Ö ö Ø ø Ü ü ß`, Greek capitals `Δ Φ Γ Λ Ω Π Ψ Σ Θ Ξ`, and `¡ ¿ £ ¥ ¤ § @ $ _`.

Not in GSM-7 (any one of these forces UCS-2 unless the provider substitutes it):
- Accents: `á í ó ú â ê î ô û ã õ ë ï ÿ œ` and every accented capital except `Ä Å Æ Ç É Ñ Ö Ø Ü` (so `À È Á Ó Ú Ê Ô Ã Õ` are out).
- Typography: curly quotes `“ ” ‘ ’`, dashes `– —`, ellipsis `…`, bullet `•`, backtick `` ` ``, non-breaking space.
- All emojis.
- Position 0x09: 3GPP TS 23.038 shows it as `Ç`; the Unicode mapping recommends displaying it as `ç`. In practice gateways differ: some send lowercase `ç` as GSM-7, some switch to UCS-2. Test with the client's provider.

National language shift tables (3GPP Release 8) add Turkish, Spanish, Portuguese and some Indic characters while staying 7-bit, at slightly lower capacity (see table), but support depends on the provider, the network and the handset. Plan on them only when the client's provider confirms.

## What to deliver

- 2-3 variations, each with its character count, encoding (GSM-7 or UCS-2) and segment count, so the client sees the cost before sending.
- Count with tokens replaced by their longest expected value (the longest first name, the longest product name): a long name can push the message into a second segment, and the raw token's braces are GSM extension characters that would be miscounted as 2 each. Give a fallback for empty fields.
- When the language has accents outside GSM-7 (Portuguese, French, many Spanish words), deliver both: the correct-accent version (UCS-2) and a GSM-7 version without the unsafe accents, rewritten so it does not read as misspelled (choose words without the accent where possible, rather than stripping accents mechanically). The client chooses cost vs correctness.
- The link: the client's own domain or branded short domain, with UTM or tracking parameters noted; count its full length in the total.
- Opt-out line in the form required by the client's country and provider.
- Send time suggestion in the recipient's local time.
- For a new US program, the opt-in confirmation message too (see Policies).

## Best practices

- Start with the brand name ("Acme: ..."): on a long number or short code the recipient sees only digits, and an unidentified text reads as spam or phishing. In the US, CTIA guidance expects the program or brand to be identified.
- Fit in one segment when possible (160 GSM-7, 70 UCS-2): cost doubles at the boundary, and long concatenated messages are more often filtered or delayed.
- Check every character, not just letters: one curly apostrophe pasted from a document turns 160 into 70. Write with straight quotes `'` `"` and a plain hyphen `-`.
- Put the offer and the action in the first line: phones preview only the start in the notification.
- Use the client's own domain or a branded short domain, never public shorteners (bit.ly, tinyurl and similar): US carriers block or filter them, and Twilio rejects 10DLC campaigns that use them. Avoid bare IP links and too many links; one link per message.
- Write like a person, plainly: all-caps words, many exclamation marks, "FREE!!!", "$$$" and similar patterns trigger carrier spam filters.
- Avoid emojis in marketing SMS unless the client accepts UCS-2 cost: one emoji caps the message at 70 characters. Older or basic phones may also show them as boxes.
- Say when an offer ends, with a date or time, not "soon": SMS is read within minutes and acted on fast, so a concrete deadline works.
- Keep frequency to what the opt-in promised: in the US, the frequency stated at opt-in is part of the consent; elsewhere, surprise volume drives opt-outs and complaints.

## Policies and restrictions

Check every point against the client's country and the restrictions in their company.md. This is not legal advice.

- Consent: most countries require prior consent for marketing SMS. Examples: US TCPA (texts count as calls; prior express written consent for marketing) and CTIA carrier guidelines; EU GDPR/ePrivacy; Brazil LGPD (needs a legal basis such as consent, plus clear opt-out). Transactional messages (order status, OTP) often follow different rules; keep promotional content out of them, since that turns them into marketing.
- US opt-in confirmation (CTIA): the first message after opt-in should state the program or brand name, message frequency, "Msg & data rates may apply", and how to get help and stop (HELP / STOP).
- US revocation (FCC 24-24, 47 CFR 64.1200(a)(10), in force since 2025-04-11): consumers can revoke consent by any reasonable means, and words like stop, quit, end, revoke, opt out, cancel or unsubscribe all count; the sender has to honor it within 10 business days. A single confirmation text is allowed within five minutes, only to confirm scope, with no marketing and no attempt to win the user back. The "revoke all" part (one opt-out covering all of a sender's message types) is delayed to 2027-01-31. For copy: the opt-out line can name STOP, but the program has to honor any wording, and the reply to an opt-out is plain confirmation, not an offer.
- Opt-out wording elsewhere: "SAIR" or "PARAR" in Brazil and "STOP" in much of Europe are market practice, not legal text; use the keyword the client's provider actually processes, otherwise the instruction is false. France: marketing SMS carry "STOP au 36xxx" (the short number depends on the operator/provider; confirm it).
- Quiet hours: the US TCPA rule (47 CFR 64.1200(c)(1)) bars telephone solicitations before 8 a.m. and after 9 p.m. recipient local time, and is being applied to marketing texts in class actions; some US states are stricter, ending at 8 p.m. France: the af2m charter allows promotional SMS 8:00-21:30; its 2026 version (from 2026-03-01) tolerates Sundays and public holidays but does not recommend them, where older versions banned them. Other countries have their own windows. Default to daytime on weekdays in the recipient's time zone unless the client's rules say otherwise.
- Pre-registration: some countries block any message that does not match a pre-registered sender and template exactly (India: TRAI DLT; one extra space or a different variable format can get it blocked), and some require fixed prefixes or sender formats. When the client sends there, write to the registered template.
- Sender type: alphanumeric sender IDs (brand name, up to 11 characters) work in many countries but not in the US/Canada, and are one-way, so "reply YES" cannot work from them. Short codes and long numbers (10DLC in the US) allow replies but usually require registration of the brand and the use case; sample messages must match what is sent.
- US 10DLC/toll-free registration: messages that do not match the registered use case, or that contain public shorteners, get filtered or the campaign gets rejected.
- Restricted content: US carriers treat SHAFT content (Sex, Hate, Alcohol, Firearms, Tobacco) as restricted, usually needing age gating or being disallowed; cannabis, gambling and high-risk loans are separate restricted categories. Many other countries restrict similar categories. Flag it if the client's offer falls there.

## Language notes

- Portuguese: `ã õ á í ó ú â ê ô` are all outside GSM-7 (only `à é` and, gateway dependent, `ç` are safe), so nearly every Portuguese sentence is UCS-2 with accents. Offer the GSM-7 version and prefer words that avoid the accent ("oferta", "hoje", "agora") over stripped spellings that look wrong ("promocao").
- Spanish: `é ñ ü ¡ ¿` are safe; `á í ó ú` are not. Many short messages can be rewritten to avoid them.
- French: `é è à ù` are safe; `â ê î ô û ë ï œ` and lowercase `ç` (gateway dependent) are not. Of the accented capitals only `É` and `Ç` are in GSM-7.
- German, Swedish, Danish, Norwegian: `ä ö ü ß å æ ø` (and capitals `Ä Ö Ü Å Æ Ø`) are safe; German SMS is usually GSM-7.
- Italian: `à è é ì ò ù` are safe; of the accented capitals only `É` is in GSM-7 (`È`, `À` and the rest are not).
- Turkish, Polish, Czech, Romanian and other Latin languages with letters outside the table, and every non-Latin script (Cyrillic, Arabic, Hebrew, Greek lowercase, CJK, Indic): UCS-2, 70/67, unless a confirmed shift table applies. Write shorter.
- Fixed limits plus text expansion: copy translated from English often crosses 160; write in the target language and count.
- Right-to-left: phones handle RTL, but a Latin link or brand name next to punctuation can display in a confusing order; put the link at the end on its own line.

## Pitfalls

- Pasting from Word/Google Docs and bringing curly quotes, en dashes or non-breaking spaces: invisible UCS-2 switch.
- Counting `€` or `[ ]` as one character.
- Counting characters without the link, the brand prefix, the opt-out line or the longest value of each token.
- Stripping accents mechanically so the message reads as misspelled.
- Using bit.ly or similar.
- "Reply YES" from an alphanumeric sender that cannot receive replies.
- No brand at the start, so the message looks like phishing.
- Sending at night or on the client's schedule instead of the recipient's time zone.
- Answering an opt-out with a discount to stay.

## RCS

RCS (rich messaging, on Android and on iOS 18+) adds verified sender, images and buttons, but needs separate registration and falls back to SMS where unsupported, so always deliver the SMS version too.

## Example

Good (GSM-7, 107 characters, 1 segment):
`Acme: your size 42 Trail Runner is back. We'll hold it until 8pm today: acme.com/r/42 Reply STOP to opt out`

Why: brand first, specific item, real deadline, own domain, opt-out, straight apostrophe, no characters outside GSM-7.

Bad (UCS-2, so capped at 70 characters):
`🔥 SUPER PROMOÇÃO!!! Só hoje – aproveite já: bit.ly/x9k2`

Why: no brand; the emoji, `Ã`, `ó`, the `á` in "já" and the en dash each force UCS-2 (the `Ç` alone would not); caps and exclamation marks look like spam; the public shortener is filtered by carriers; and there is no opt-out.

## Sources
- https://www.3gpp.org/dynareport/23038.htm (3GPP TS 23.038, primary: GSM 7-bit default alphabet, extension table, national language shift tables; 0x09 shown as Ç)
- https://en.wikipedia.org/wiki/GSM_03.38 (readable copy of the 23.038 tables; Unicode mapping recommends ç at 0x09; 160 GSM-7 / 70 UCS-2 per single message; shift tables added in Release 8)
- https://en.wikipedia.org/wiki/Data_Coding_Scheme (shift-table capacity: 155 with a single shift table, 152 with locking + single; secondary)
- https://www.twilio.com/docs/glossary/what-sms-character-limit (153 GSM-7 / 67 UCS-2 per concatenated segment; 152/66 for US/Canada toll-free; billing per segment; keep under 320 characters)
- https://www.twilio.com/docs/glossary/what-is-gsm-7-character-encoding (extension characters count as two)
- https://support.twilio.com/hc/en-us/articles/1260804572090 (public shared shorteners raise filtering risk with no recourse)
- https://www.twilio.com/docs/api/errors/30963 (US A2P 10DLC campaigns rejected for public URL shorteners)
- https://support.bitly.com/hc/en-us/articles/20441769384589-Why-can-t-I-use-Bitly-links-in-some-SMS-campaigns (carriers block public shortener links; use a custom domain)
- https://www.twilio.com/docs/trust-hub/registrations/alphanumeric-sender-id (alphanumeric sender ID up to 11 characters; not available in US/Canada; registration in some countries)
- https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200 (US TCPA: (c)(1) quiet hours 8 a.m.-9 p.m. recipient local time; (a)(10) revocation of consent)
- https://www.kelleydrye.com/viewpoints/blogs/ad-law-access/fcc-adopts-changes-to-tcpa-consent-revocation-rules (FCC 24-24: any reasonable means, 10 business days, one confirmation text within five minutes without marketing)
- https://www.burr.com/telephone-consumer-protection-act/the-fcc-delays-effective-date-of-tcpa-revoke-all-rule-until-january-31-2027 ("revoke all" delayed to 2027-01-31)
- https://www.ctia.org/the-wireless-industry/industry-commitments/messaging-interoperability-sms-mms (CTIA Messaging Principles and Best Practices: brand identification, opt-in confirmation, HELP/STOP)
- https://lareclame.fr/af2m-smspromotionnels-dimanche-jourferie-330088 (France af2m 2026 charter: Sundays and holidays now possible under conditions)
- https://www.telerivet.com/blog/india-sms-compliance-trai-dlt-registration-and-tcccpr-guide (India TRAI DLT: entity, header and template registration; mismatches blocked)
