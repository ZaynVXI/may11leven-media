# Publishing transport gate

Good copy can still arrive broken if a scheduler stores escaped text or platform markup differently.

## Before scheduling

Inspect the exact payload that will be sent:

- paragraph breaks are real newline characters;
- the content contains no literal `\\n` sequence;
- raw `<p>`, `<br>`, or editor markup is absent unless the API explicitly requires HTML;
- there is intentional whitespace between the hook, body, example, and CTA;
- conversational asides use parentheses rather than em dashes when the brand voice is informal and spoken;
- the media belongs to the correct account and platform;
- the date and timezone are explicit.

## After scheduling

Fetch the post back from the scheduling API and inspect the stored content, not only the local source.

Release blockers:

- literal escape sequences;
- collapsed paragraphs;
- HTML tags that will be visible on the platform;
- missing media;
- wrong profile or integration;
- an unexpected duplicate at the same time.

## Safe correction when posts are immutable

If the API cannot edit a scheduled post:

1. Create the corrected replacement as a draft.
2. Fetch it back and verify content, media, account, and date.
3. Move the defective scheduled item to draft.
4. Promote the verified replacement to the queue.
5. Fetch the queue again and assert one active post at that slot.

Do not delete the original. Do not retry an ambiguous write before checking whether it already succeeded.
