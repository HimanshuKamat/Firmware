# Original brief (verbatim from the user's first message)

You are my producer, writer and editor for an animated children's story video for my YouTube channel. Work through the phases below in order. Stop at every CHECKPOINT and wait for my approval before spending any generation credits.
The brief

* Story: A story about Lord Ganesha (Ganpati Bappa), told respectfully and warmly.
* Audience: Toddlers aged 4–5. Parents will be watching too.
* Length: 4 to 5 minutes total, including the intro and outro. Never more than 5:00.
* Format: 16:9, 1920×1080, 24 or 30 fps. Also export a 60-second 9:16 Shorts teaser.
* Language: Simple English with Indian names and words kept as they are (Bappa, modak, Mooshak, Amma). Keep the script easy to re-voice in Hindi or Marathi later.
* Look: Soft, rounded 3D character animation in a warm, bright, modern feature style. Gentle and cosy, never scary.

Toddler rules (apply to every phase)

* Story choice: Suggest 3 options and recommend one. My default is "Ganesha and Kartikeya's race around the world": Ganesha circles his parents, because they are his whole world. Other options are Ganesha and the moon, or Ganesha and Kubera's feast. Do not use the elephant-head origin story. The beheading is too frightening for this age.
* One simple lesson, said clearly at the end, for example "Our family is our whole world."
* Narration: Slow and warm, about 110–120 words per minute. Short sentences of 5–8 words. Total script about 450–550 words.
* Repetition: One catchy line or sound that comes back 3–4 times, such as "Ganpati Bappa Morya!" or Mooshak's "squeak-squeak!". Toddlers love predicting it.
* Interaction moments: 2–3 pauses where the narrator asks the child something, like "Can you count the modaks with me? One… two… three!" Leave a 2-second gap for the child to answer.
* Pacing: Shots of 6–10 seconds. No fast cuts, flashing, loud bangs, villains, chases or crying that goes on too long. Any conflict is resolved quickly and kindly.
* Visuals: Bright, saturated but soft colours; big, clear faces; simple backgrounds; one main action per shot.
* Characters: Ganesha (child-like and cheerful, traditional elephant head, one broken tusk, holding a modak, gold and red clothes), Mooshak the mouse (comic sidekick), Kartikeya on his peacock, Shiva and Parvati (gentle and loving). Depict them respectfully, in line with traditional iconography. Ask me before simplifying any sacred details, such as two arms instead of four.

Phase 0: Setup check
Before anything else, check which of these tools are available to you and tell me what's missing, with the exact setup command or step:

1. Vivideo AI Video Prompt Generator (MCP): shot prompts
2. Krea (MCP): images and video clips. Add with `claude mcp add --transport http krea-ai https://api.krea.ai/mcp`
3. ElevenLabs (MCP): voiceover, sound effects, music
4. HyperFrames by HeyGen: titles and motion graphics. In Claude Code, use the local skills (`npx skills add heygen-com/hyperframes`), because the hosted compose and render tools are disabled for CLI agents.
5. Canva (MCP): thumbnail and channel graphics
6. ffmpeg (local): final assembly, loudness, captions burn-in

Create this project folder:

```
ganesha-video/
  01_script/       script.md, shotlist.md, bible.md
  02_prompts/      prompts.json
  03_refs/         character and location reference images
  04_keyframes/    one still per shot
  05_clips/        approved video clips (shot_01.mp4 …)
  06_audio/        narration, sfx, music
  07_graphics/     HyperFrames title, cards, end screen
  08_edit/         working files
  09_final/        final MP4, Shorts MP4, SRT, thumbnail, youtube_metadata.md
```

Keep a `log.md` with every generation made, the model used and the credits spent.
Phase 1: Story and script

1. Pitch the 3 story options with one line each and your recommendation.
2. Write the script in three acts:
   * Hook (0:00–0:20): Mooshak or Ganesha greets the child directly.
   * Story (0:20–4:00)
   * Lesson and goodbye song (4:00–4:45)
   * Leave room for the intro and end card.
3. Write a shot list of about 28–36 shots. For each shot give: shot number, duration, the narration line it covers, the action, the camera move, the emotion, and whether it needs a Krea clip or a HyperFrames graphic.
4. Write a character and world bible: a fixed, word-for-word description of each character and location (colours, clothes, proportions, props). Every prompt must reuse this exact text.

CHECKPOINT 1: Show me the script, shot list and bible. Wait for my approval.
Phase 2: Prompts (Vivideo)

5. Use `list_video_prompt_styles` and pick `animation_3d_character` (or the style I choose). Use the same style for every shot.
6. Run `build_video_prompt` for each shot. Then add the bible text for any characters and location in that shot, plus these negatives: "no text, no logos, no scary expressions, no extra limbs, consistent character design".
7. Save everything to `02_prompts/prompts.json`.

Phase 3: Visuals (Krea)

8. References first. Generate character sheets for Ganesha, Mooshak, Kartikeya, Shiva and Parvati (front and 3/4 views on a plain background), plus one image of each main location. Give me 3–4 options of each, I'll pick, and you save the picks to `03_refs/`. If Krea supports styles or moodboards, create one from the approved references and use it for every later generation.
9. Keyframes. Generate one still per shot using the references. Show them to me as a numbered contact sheet.

CHECKPOINT 2: I approve the references and keyframes. Redo any that are off-model before moving on.

10. Animate. Turn each approved keyframe into a clip with image-to-video:
   * Default model: Seedance 2.5
   * Hero moments (opening shot, the race, the circling of the parents, the ending): Veo 3.1
   * Backup if a character drifts: Kling 3.0
   * Turn off the models' own audio, or ignore it. All sound comes from Phase 4.
11. Make 2 versions per shot, pick the better one, and log why. Don't retry the same prompt more than twice. Flag it to me instead.

CHECKPOINT 3: Show me all the clips in order (a rough ffmpeg stitch is fine). I flag any to redo.
Credit rule: Before Phase 3 starts, estimate the total generations and credits, and wait for my go-ahead. Stop and tell me if usage goes 20% over the estimate.
Phase 4: Voice, music and sound (ElevenLabs)

12. Narrator: a warm, gentle, friendly voice with a soft Indian-English accent. Give me 3 voice options with a 15-second sample each.
13. Character voices (if there's dialogue): a squeaky, playful Mooshak; a sweet, cheerful young Ganesha.
14. Generate the narration line by line, matched to the shot list, so each line can be re-timed.
15. Music: soft Indian instrumental (flute, tabla, gentle bells). A short, singable "Ganpati Bappa Morya" chant for the ending.
16. Sound effects: mouse squeaks, peacock call, temple bells, soft whooshes. Nothing loud or sudden.

CHECKPOINT 4: I approve the narrator voice and the full narration before the edit.
Phase 5: Motion graphics (HyperFrames)

17. Build these at 1920×1080 to match the 3D look:
   * Channel intro (5–7 seconds)
   * Title card: "[Story title] – A Ganesha Story for Kids"
   * Animated counting overlays for the interaction moments (big, friendly numbers)
   * Lesson card with the moral in large, simple words
   * End screen (20 seconds) with space for YouTube's subscribe button and 2 video suggestions
18. Use big, rounded, high-contrast type and keep text on screen for at least 3 seconds.

Phase 6: Assembly (ffmpeg)

19. Put the full timeline together in order: intro, title, clips, overlays, lesson card, end screen.
20. Audio mix:
   * Narration on top
   * Music ducked under the narration (about −18 to −20 dB under voice)
   * Sound effects in between
   * Gentle 0.5-second crossfades between shots, no hard cuts on emotional beats
21. Normalise loudness to −14 LUFS integrated, −1 dBTP.
22. Export as H.264 High profile, 1920×1080, 30 fps (or 24), about 12–16 Mbps, AAC 320 kbps, 48 kHz.
23. Make an SRT caption file from the narration timings.
24. Make the 60-second Shorts teaser at 9:16, 1080×1920, from the strongest moments, with a "full story on the channel" card at the end.
25. Check the final duration is at most 5:00, and watch for audio sync, black frames and glitches.

Phase 7: Thumbnail and YouTube package (Canva)

26. Thumbnail: 1280×720 in Canva. Close-up of a happy Ganesha holding a modak, Mooshak in the corner, 2–4 big words at most (e.g. "Ganesha's Big Race!"), bright colours, readable at phone size. Give me 3 options.
27. Write `09_final/youtube_metadata.md` with:
   * 3 title options under 60 characters
   * A description: short summary, the moral, chapters with timestamps, and a credit line saying the video was made with AI tools
   * 10–15 tags
   * Suggested playlist
   * These upload settings:
      * Audience: "Yes, it's made for kids" (COPPA), which turns off comments and personalised ads
      * Altered or synthetic content: tell me whether YouTube's current rules need the AI disclosure for clearly animated content, and recommend a setting
      * Category: Education or Film & Animation
      * Captions: upload the SRT

FINAL CHECKPOINT: Give me a one-page summary covering the final file paths, total credits used, any shots you weren't happy with, and what you'd improve next time.
Working rules

* Ask me questions in one batch at the start, then work. Don't ask things you can decide sensibly yourself; note your assumptions instead.
* Keep everything respectful to the Hindu tradition. If you're unsure about a detail of the story or iconography, say so rather than inventing it.
* Save every approved asset with a clear name, and never overwrite an approved file.
* Use plain language in your updates and be brief.
