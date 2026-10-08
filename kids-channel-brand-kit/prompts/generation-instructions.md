# Generation instructions (for the agent)

Use the Gemini API directly with `$GEMINI_API_KEY` (never print or store the key). Do not use Krea.

1. Verify the key is set: `[ -n "$GEMINI_API_KEY" ] && echo set`.
2. Pick a Gemini image-generation model currently available to the key (list models via `GET https://generativelanguage.googleapis.com/v1beta/models?key=...` and choose one that supports image output; prefer the newest "image" model).
3. Generate the hero mascot from `prompts.md` section 1; show it to the user and get approval before continuing.
4. For every later asset, send the approved hero image as an inline reference image with the prompt, so the character stays identical.
5. Save outputs into `mascot/`, `logo/`, `banner/`, `thumbnails/` with clear names (e.g. `mascot/pose-1-happy.png`).
6. Check dimensions (resize/crop with ImageMagick or Pillow if the model returns a different size): logo 800x800, banner 2560x1440, thumbnails 1280x720.
7. Track progress with a visible to-do list (TaskCreate/TaskUpdate), one task per asset group.
8. Update README.md status and fill in the channel name in `brand-guide.md` if chosen.
