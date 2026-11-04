# Accessibility checks for our posts and screens
- a11y.py: import before any Pillow post script (run.sh script.py name). Checks every line of text against the real pixels under it: 4.5:1 for text under 48 px, 3:1 for larger. FIX=1 nudges the colour (keeping its hue) until it passes; MINPX sets a minimum font size (20 for posts, 24 for reels). Log: log.jsonl.
- webaudit.js: node webaudit.js page.html ... checks contrast and text under 12 px in our HTML mock screens (text on photos needs a visual check).
- Reels: keep key text between y 220 and 1500 on a 1080x1920 canvas (Instagram UI covers the bottom and right edge).
