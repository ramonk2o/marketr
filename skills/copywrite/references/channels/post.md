# Channel: post

Organic Instagram feed posts (single image and carousel), with what changes when the same post goes to Facebook or LinkedIn.

Verified: 2026-11-01 (sources at the end)

## Pieces and fields

| Field | Hard limit | Visible before truncation | Notes |
|---|---|---|---|
| Caption | 2,200 characters (official, API doc) | about 125 characters, often 1 to 2 lines (observed, varies by device) | Spaces, emojis, line breaks and hashtags all count. |
| Hashtags | 5 per post (official, Help Center: a comment with more than 5 is not posted) | n/a | Caption and comments seem to count together (observed). Older guides and the API doc say 30; Instagram announced the cut to 5 on Dec 18, 2025 (Social Media Today). Put them in the caption: Instagram search reads the caption, not the comments (official). |
| @ mentions in caption | 20 (official for the API; observed similar in the app) | n/a | Tagging people on the image is a separate field. |
| Alt text | No limit stated | Read only by screen readers | Automatic alt text exists; custom text replaces it. |
| Carousel | 1 to 20 photos or videos (official) | Slide 1 in feed; grid shows slide 1 cropped | One orientation for all slides. Nothing can be added after posting. Carousel videos are not Reels. |
| Image ratio | 4:5 portrait to 1.91:1 landscape (official, Graph API; Help Center names square, portrait, landscape); native 3:4 uploads (reported) | n/a | The profile grid shows vertical 3:4 tiles since early 2025 (reported, no official pixel spec). Keep key text inside a centered 3:4 area of a 4:5 image. |
| Collaborators | No number stated in Help Center; up to 5 (observed) | Both names shown in the header | The invited account must accept. Mobile app only (observed). |
| Links | Not clickable in captions (observed) | n/a | Use the bio link, a story link sticker, or "comment KEYWORD" plus a DM if the client runs one. |

## What to deliver

- **Single image:** the caption ready to paste, the on-image text (headline plus at most one support line), alt text, hashtags, any mentions and collaborators.
- **Carousel:** a script with one line per slide, then the caption, alt text per slide, and hashtags:
  ```
  1 (hook): <headline on the slide> | <visual note>
  2: <text> | <visual note>
  ...
  N (CTA): <text> | <visual note>
  ```
  One line per slide lets the user and the designer judge flow and length at a glance before anything is designed.
- Mark the first line of the caption: it is all most people see.

## Format agreement

Agree on these once per client and save them in `channels.md`. When the client already has posts, read them, infer the current pattern and propose it ("your posts run about 600 characters, hook plus 3 short paragraphs, 3 hashtags at the end; keep that?"). Asking in the abstract gets vague answers; a proposal gets a yes or a correction.

| Decision | Default options |
|---|---|
| Caption length | Short (under 300 characters) / medium (300 to 1,000) / long (1,000+, for educational or story posts) |
| Structure | Hook, body, CTA, hashtags / hook plus CTA only / storytelling |
| Hashtag policy | 0 / 1 to 3 specific / up to 5 (the cap), always in the caption; local language or English; branded tag yes or no |
| Emoji use | None / as bullets or markers only / free in the client's voice |
| CTA conventions | Save, share, comment, link in bio, DM; one per post; the client's usual wording |
| Text on image | None (photo speaks) / headline only / headline plus one line |
| Carousel length | 5 to 7 / 8 to 10 / up to 20 for guides or photo dumps |
| Line breaks | Short paragraphs with blank lines / dense text |

## Structures

- **Educational carousel:** slide 1 promise ("5 mistakes that..."), one idea per slide, last slide recap plus CTA (save or share). The promise earns the swipe; one idea per slide keeps each slide readable on a phone.
- **Offer post:** image with the offer in a few words; caption opens with the benefit, then the details (price, date, conditions), then how to get it. People decide in the first line whether the offer concerns them.
- **Testimonial post:** quote on the image (short, in the customer's words), caption with context and the result, CTA. A real voice persuades more than the brand describing itself.
- **Behind the scenes / story:** caption opens in the middle of the scene, short paragraphs, a closing question. Starting with "Today we want to share..." spends the visible characters on nothing.
- **Announcement:** what changes for the reader first, the news second. The reader cares about the effect, not the event.

## Best practices

- Put the hook in the first ~125 characters: the rest sits behind "more" and is only read by people the hook already convinced.
- Make slide 1 a hook, not a cover with the logo: it is the only slide shown in feed and the one cropped in the grid, so it decides the swipe.
- Give each slide one idea and few words, at a size legible on a phone without zooming: people read carousels at thumb speed on a small screen.
- End the carousel with a reason to act (save, share, comment): the last slide is where engaged readers are, and saves and shares signal value.
- Write the topic in plain words in the caption (what it is, for whom, where): Instagram says the search text is the most important signal and is matched against usernames, bios, captions, hashtags and places. Google can also index public professional posts since July 2025 (reported).
- Put keywords and hashtags in the caption, not in the first comment: Instagram says that is what makes a post findable in search; hashtags hidden in a comment do not help.
- Use a few specific hashtags rather than generic ones: the cap is 5 and Instagram said the change targets generic tags; specific tags help classify the post.
- Write custom alt text describing the image and any text on it: screen reader users otherwise get a vague automatic description or nothing about the text.
- Break lines into short paragraphs: dense blocks look long on a phone and get skipped.
- Use one CTA: two CTAs split attention and neither gets done.

## Policies and restrictions

- **Paid partnership label (Meta):** required whenever a post features a business partner in exchange for value: payment, free or lent products, or affiliate links with commission. Not required for the client's own products. The label does not replace local legal disclosure.
- **Collab posts with a partner brand:** still branded content if value was exchanged; collab and the paid partnership label are separate.
- **Health, finance, before and after, weight loss, alcohol:** Meta community and branded content rules restrict some claims and audiences. Check `restrictions` in the client's knowledge for the client's sector.
- **Country disclosure rules:** many countries require visible ad disclosure (e.g., "ad", "publi", "#anzeige") in addition to the platform label. Check the client's restrictions for the country; if nothing is recorded, ask before writing sponsored copy.
- **Contests and giveaways:** Instagram's promotion guidelines require official rules, a complete release of Instagram by each entrant and a statement that Instagram does not sponsor or run the promotion. They also forbid asking people to tag content inaccurately (e.g., tagging themselves in photos they are not in), so "tag 3 friends in this photo" mechanics need care. Local law may require registration.

## Language notes

- Character counts favor short languages: the same hook in German or Portuguese can run 20 to 35% longer than in English (observed), so the visible ~125 characters hold fewer words. Write the hook in the target language from the start rather than translating it.
- Text on slides expands too: leave space in the layout, or the designer will shrink the font until it is illegible.
- Hashtags work in the language people search in. A local business in Brazil gets more from #confeitariasp than #bakery.
- Emoji meaning and politeness vary by culture; follow the client's existing usage.

## Cross-posting

- **Facebook:** captions can be much longer and links are clickable, so "link in bio" makes no sense there; replace it with the link. Hashtags matter little. Collab and tags do not carry over.
- **LinkedIn:** 3,000 characters per post (LinkedIn Help); about 200 visible before "see more" (observed). A more professional register, no "link in bio", hashtags optional. A carousel goes as a PDF document post. Reports say external links in the post reduce reach (unconfirmed).

## Pitfalls

- Opening with a greeting or "New post!": wastes the only visible line.
- Writing 10 to 30 hashtags out of habit: Instagram now rejects more than 5, and the user finds out only when publishing.
- Text-heavy slides copied from a blog: unreadable on a phone and too long to swipe.
- "Link in bio" when the bio has no matching link: the reader looks, finds nothing and leaves.
- A cover slide with only the logo or the post title: no reason to swipe.
- Mixed portrait and square images in one carousel: Instagram applies one orientation and crops the rest.
- Key text near the edges of a 4:5 image: the 3:4 grid tile cuts it.

## Example

Good caption opening (bakery, educational carousel):
> Your bread is dense because of one step, and it is not the flour. Swipe to see which one.

Why: names the reader's problem, promises the answer and asks for the swipe, all within the visible line.

Bad caption opening:
> Hello friends! 🌞 Happy Monday! Today we have a very special post for all of you who love baking...

Why: the visible characters go on a greeting; nothing tells the reader what they get or why to keep reading.

## Sources

- https://www.facebook.com/help/instagram/351460621611097 (Help Center: up to 5 hashtags per post; a comment with more than 5 is not posted)
- https://www.socialmediatoday.com/news/instagram-implements-new-limits-on-hashtag-use/808309/ (Instagram statement, Dec 18 2025: caption hashtags for posts and reels cut to 5, rolled out gradually)
- https://about.instagram.com/blog/announcements/break-down-how-instagram-search-works/ (search text is the main signal, matched against usernames, bios, captions, hashtags, places; keywords and hashtags go in the caption, not the comments)
- https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media (caption max 2,200 characters and 20 @ tags; carousel up to 20 items; aspect ratio 4:5 to 1.91:1; the "30 hashtags" figure there predates the 5 cap)
- https://www.facebook.com/help/instagram/269314186824048 (Help Center: carousel up to 20 photos and videos, one orientation for the whole post, nothing can be added after sharing)
- https://www.facebook.com/help/instagram/503708446705527 (Help Center: automatic alt text, custom alt text under Accessibility, editable after posting)
- https://www.facebook.com/help/instagram/291200585956732 (Help Center: collab posts appear on both profiles and credit both accounts)
- https://www.facebook.com/help/instagram/616901995832907 (Help Center: when the paid partnership label is required)
- https://help.instagram.com/179379842258600 (promotion guidelines: release, non-sponsorship statement, no inaccurate tagging)
- https://www.linkedin.com/help/linkedin/answer/a528176 (LinkedIn Help: post limit 3,000 characters)
