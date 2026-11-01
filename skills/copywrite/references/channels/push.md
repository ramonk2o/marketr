# Channel: push

Mobile push notifications on iOS and Android, plus a short section on web push (Chrome, Safari, Windows).

Verified: 2026-11-01

## Pieces and fields

Neither Apple nor Google documents a character limit for title or body. The only hard limit is the payload size, which includes the JSON keys, the deep link and custom data, not just the copy. Everything under "visible" is observed, not documented: it changes with device width, font size setting, OS version, language and whether the notification is grouped.

| Field | Hard limit | Visible before truncation (observed) | Notes |
|---|---|---|---|
| Title (iOS) | Payload 4 KB total | 1 line, roughly 30-50 characters | Bold. Shown on Apple Watch short look. HIG (English): title case for the title, no ending punctuation; skip it if it would be generic, since the app name shows anyway. |
| Subtitle (iOS only) | Payload 4 KB total | 1 line, roughly 30-50 characters | Android has no equivalent; anything vital in it is lost on Android. Optional. |
| Body (iOS) | Payload 4 KB total | Lock screen / banner: about 4 lines, ~110-180 characters; long-press or expanded: full text | HIG: sentence case, complete sentences, proper punctuation. Grouped stacks show only the latest notification's text until expanded. |
| Title (Android) | Payload 4 KB total (FCM) | 1 line, roughly 30-50 characters | Shares the row with app name and time on some skins. |
| Body (Android) | Payload 4 KB total (FCM) | Collapsed: 1 line, ~40-60 characters; expanded (BigTextStyle): several lines | Documented: "truncated to fit one line" by default. Collapsed is what most users see in the drawer. |
| Image | Payload carries a URL, not the file | Thumbnail collapsed, large when expanded | iOS needs a Notification Service Extension in the app; Android uses BigPictureStyle. Copy must make sense if the image fails to load. |
| Action buttons | iOS: up to 4 in detail view; Android: up to 3 | Hidden until the user expands or long-presses | Defined by the app, often as fixed categories: confirm with the client which exist before writing labels. HIG: short title-case label that says the result, without the app name. |
| Deep link | Counts toward payload | Not visible | Target screen, not the home screen. |
| Relevance score (iOS) | Number 0-1 | Not visible | The system uses it to sort the app's notifications; the highest score is featured in the notification summary. |
| Firebase console campaign | 1000 characters (console only) | Same as above | API sends are bound by the 4096-byte payload instead. |

Payload sizes: APNs refuses payloads over 4 KB (4096 bytes; 5 KB for VoIP). FCM caps notification and data messages at 4096 bytes. Copy never comes close to this alone; trouble comes from long custom data or many localized strings in one payload.

How iOS may show it instead of your exact text:
- Scheduled Summary: users can have non-time-sensitive notifications held and delivered in a batch at set times. Your send time then does not decide when the message is seen, and it competes with other apps in the summary; relevance score decides which of your notifications is featured. Time-sensitive notifications are delivered immediately, outside the summary.
- Apple Intelligence summaries (iOS 18.1+, where available and enabled): the system may paraphrase a notification or a stack of them into one line. Front-load the point and use concrete nouns early (item, price, date) so the paraphrase keeps them; wordplay and teasers tend to be lost.
- Previews hidden: the lock screen may show only the app name or a generic line. When the app supports a placeholder for hidden previews, write a short descriptive one ("Shipment", "Friend request", "Reminder"), as the HIG suggests.

## What to deliver

- 3 variations per notification, each as title + body (+ iOS subtitle only if the brief uses it). Variations should differ in angle (benefit, urgency, curiosity), not just wording, so an A/B test teaches something.
- Mark the first ~40 characters of each body: that is what Android collapsed shows. A reviewer should be able to judge the notification from that slice alone.
- Deep link target: which screen the tap should open (e.g., "cart with the item preselected"), in words; the client's team maps it to the real route.
- Action button labels, only if the app supports them.
- Image suggestion, if any, with the copy still working without it.
- Send time suggestion in the recipient's local time zone, noting that on iOS it may arrive in a Scheduled Summary instead; interruption level on iOS (normally active; time-sensitive only if it genuinely is) and a relevance score when several notifications may compete.
- Personalization tokens marked with the client's syntax, plus a fallback for when the field is empty.

## Best practices

- Put the reason to tap in the first 40 characters of the body: Android collapses to one line and that is the most common view; the rest is a bonus.
- Leave the app name out of title and body: the system already shows the name and icon, so repeating it burns the most visible space (Apple HIG says so explicitly).
- Make title and body say different things: if the body restates the title, the notification carries half the information in the same space.
- Write complete sentences and let the system truncate (HIG): manually cut text ("Your order is...") reads as broken, and a sentence that front-loads its point survives truncation anyway.
- Keep anything essential out of the iOS subtitle when the same copy goes to Android: Android has no subtitle and drops it.
- Be specific with numbers, names and items ("Your size 42 is back in stock") rather than generic ("New arrivals!"): generic pushes are what make users turn notifications off, and on Android 13+ and iOS turning them off is one tap.
- Personalize from behaviour, not just first name: a name in a generic message adds little; a reference to what the user did (left in cart, followed, booked) is what earns the tap. Always give a fallback for empty fields so no one gets "Hi {first_name}".
- Use at most one or two emojis, at the start or end, never replacing a word: rendering differs by OS version, an emoji that stands for a key word can show as a box or be misread, and system summaries may drop it.
- Send at the recipient's local time and respect frequency: Android shows users per-app notification counts and both OSs make revoking easy, so each low-value push costs future reach.
- Use time-sensitive (iOS) only for things that lose value within hours (delivery arriving, booking starting): it breaks through notification controls and skips the summary, and users can turn it off per app if abused. Use passive for low-priority news: it lands in the list without lighting the screen.
- Match the deep link to the promise: if the copy says "your 20% coupon", the tap must land on the coupon, not the home screen, or the trust built by the push is lost.
- Assume previews may be hidden on the lock screen: the user may only see the app name, so never rely on the lock screen for anything private.

## Policies and restrictions

- Apple App Review 4.5.4: push for promotions or direct marketing needs explicit opt-in via consent language in the app's UI and an in-app way to opt out. Check that the client has this before writing promotional push; transactional and service pushes are a different category.
- Apple: no sensitive personal or confidential information in push (4.5.4 and HIG). Others may see the screen: no health details, balances, full addresses, passwords or one-time codes beyond what the client's security policy allows.
- Google Play: notifications that look like system notifications or alerts count as deceptive ads. Avoid copy that imitates the OS ("Your phone is at risk", "System update required") or fake warning formats.
- Android 13+: notifications need a runtime permission and are off by default for new installs. The opt-in prompt itself (pre-permission screen copy) is copy worth writing: Google recommends asking in context, after a user action, explaining the value.
- Android channels (8.0+): users can mute one channel (e.g., "Promotions") while keeping others (e.g., "Orders"). Ask the client which channel each push goes to; sending promotional copy through a transactional channel invites users to mute the important one.
- Critical alerts (iOS) require a special Apple entitlement and are for health, safety and security, never marketing.
- Legal (check against the client's restrictions in company.md, not legal advice): marketing consent rules such as GDPR/ePrivacy in the EU and LGPD in Brazil may apply to promotional push; sector rules (finance, health, gambling, alcohol) often restrict claims or audiences.

## Language notes

- Push uses Unicode, so accents and non-Latin scripts are safe, unlike SMS.
- Visible space is measured in width, not characters: German, Finnish, Portuguese and French typically run noticeably longer than English (20-35% is a common rule of thumb, not a measured limit) for the same idea, so translated copy truncates earlier. Write in the target language directly, or re-check the first 40 characters after translating.
- CJK characters are wider: fewer characters fit per line, but each carries more meaning; judge by the visible slice, not by the count.
- Right-to-left languages (Arabic, Hebrew): the OS mirrors the layout if the device is set to that language; mixing Latin brand names or numbers into RTL text can reorder visually, so check punctuation placement around them.
- Capitalization follows the language: the English HIG asks for title case in titles and sentence case in bodies, but most other languages use sentence case for both; follow the client's language and style guide.

## Pitfalls

- Writing for the iOS lock screen and forgetting Android collapsed: the hook ends up on line 3.
- Body that starts with filler ("Hey there! We have some exciting news..."): the visible slice says nothing, and a system summary has nothing to keep.
- Promising a discount or item without saying which deep link delivers it.
- Clickbait ("You won't believe this"): earns one tap and then an opt-out.
- Urgency every day: "Last chance" loses meaning and users learn to ignore the app.
- Personalization token without a fallback.
- Sending at a fixed server time, so half the audience gets it at 3 a.m.
- Copy that depends on the image to make sense.

## Web push

Browsers show title, body, icon and sometimes a large image and action buttons, but the OS controls the look: Windows, macOS and Android Chrome all render differently, and the number of actions varies by browser (`Notification.maxActions`; commonly observed as 2 on Chrome, not documented as fixed). Observed visible text is short on desktop: roughly 1 line of title and 2-3 lines of body, with the site's domain shown by the browser. On iOS/iPadOS 16.4+ web push works only for web apps added to the Home Screen and only after the user taps to subscribe; they then behave like app notifications and respect Focus. The same rules apply: point first, specific, link to the exact page, low frequency. The opt-in prompt matters even more than on mobile: browsers hide or quiet sites that ask on page load.

## Example

Good (Android collapsed shows title + "We're holding a pair in size 42"):
- Title: Trail Runner X Is Back
- Body: We're holding a pair in size 42 for you until 8 p.m. After that it goes to the waitlist.
- Deep link: product page, size 42 preselected. Send: 12:30 local. iOS interruption level: active.

Why: the title gives the news, the body adds what the title does not (size, hold, deadline), the item and deadline survive a system summary, and the deep link delivers exactly what the copy promises.

Bad:
- Title: ShoeShop
- Body: Hi {first_name}! 🔥🔥 Don't miss our amazing offers, check out the app now!!!

Why: the title repeats the app name the system already shows, the visible slice is a greeting, the token has no fallback, emojis replace content, and there is nothing specific to tap for.

## Sources
- https://developer.apple.com/documentation/usernotifications/generating-a-remote-notification (APNs payload 4 KB / VoIP 5 KB, refused if larger; title, subtitle, body keys; interruption-level; relevance-score 0-1, highest featured in the summary)
- https://developer.apple.com/documentation/usernotifications/unnotificationinterruptionlevel (what passive, active, time-sensitive, critical do)
- https://developer.apple.com/design/human-interface-guidelines/notifications (brevity, no app name, title case titles, sentence case body, system truncates, up to 4 title-case actions without the app name, generic text when previews are hidden, no sensitive data)
- https://developer.apple.com/app-store/review/guidelines/ (4.5.4: promotional push only with explicit in-app opt-in and an in-app opt-out)
- https://support.apple.com/guide/iphone/iph1fbe7d2b9/ios (Apple Intelligence notification summaries and Prioritize Notifications)
- https://developer.apple.com/videos/play/wwdc2021/10091/ (time-sensitive notifications and Scheduled Summary; time-sensitive delivered immediately)
- https://support.google.com/googleplay/android-developer/answer/9899004 (deceptive ads include notifications similar to system notifications and alerts)
- https://firebase.google.com/docs/cloud-messaging/customize-messages/set-message-type (FCM 4096 bytes for notification and data messages; Firebase console 1000 characters)
- https://developer.android.com/develop/ui/views/notifications/build-notification (text cut to one line by default; expandable styles; up to 3 action buttons that must not duplicate the tap)
- https://developer.android.com/develop/ui/views/notifications/notification-permission (Android 13+ runtime permission; ask in context)
- https://doc.batch.com/guides-and-best-practices/message/push-notifications/page-4 (observed: iOS lock screen about 4 lines / ~180 characters; Android one line / ~50 characters)
- https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/ (iOS/iPadOS 16.4+ web push only for Home Screen web apps, after a user gesture)
- https://developer.mozilla.org/en-US/docs/Web/API/Notification/maxActions_static (web push action count varies by browser)
