# Handoff: pick up here in a new session

Read `BRIEF.md` first (the user's full brief, word for word), then this file. The user wants plain language and short updates.

## Where we are

| Phase | Status |
|---|---|
| 0 Setup check | Done |
| 1 Script, shot list, bible | Done. **Checkpoint 1 approved** by the user ("Approved"). |
| 2 Prompts | Done. `02_prompts/prompts.json` has 32 shot prompts plus 6 graphics briefs. No checkpoint. |
| 3 Visuals (Krea) | **Not started. On hold.** The user chose "Hold for now" at the credit gate. |

**Credits spent so far: 0** (Krea 0, ElevenLabs 0). Every call so far was read-only or text-only. Two empty ElevenLabs flows were created by price checks and can be ignored.

## Blocker to clear first

The old session's network policy blocked `api.krea.ai`, `www.krea.ai`, `gen.krea.ai`, `api.elevenlabs.io` and `elevenlabs.io` (CONNECT 403). The MCP generation tools work through connectors, but you cannot download generated files into the sandbox, so the contact sheet and the ffmpeg edit would fail.

**First action in the new session:** test the hosts (free):

```
for u in https://api.krea.ai https://www.krea.ai https://gen.krea.ai https://api.elevenlabs.io https://elevenlabs.io; do curl -sS -m 15 -o /dev/null -w "$u http=%{http_code}\n" "$u"; done
```

If they still return 403, tell the user which hosts are denied. Their fix: the cloud icon above the message box at claude.ai/code (or the Desktop app prompt box), then Cloud, then the gear icon beside the environment, then Network access: **Full**, or **Custom** with those five hosts plus "Also include default list of common package managers". Canva's export host and Krea's media host may also need adding. Name them when they appear.

Also make sure the Krea, ElevenLabs, Vivideo, Canva and HyperFrames connectors are enabled in the new session.

## The user's decisions (all confirmed)

- **Story:** "Ganesha's Big Race": Kartikeya races on his peacock, Ganesha walks around his parents, "Our family is our whole world." Title card: "Ganesha's Big Race – A Ganesha Story for Kids".
- **Sacred details:** Ganesha has **two arms** (approved). Kartikeya has **one face** (approved). Shiva keeps his **tiny smiling cobra and gentle closed third eye** (approved).
- **Checkpoint 1 approved as written,** including the story details listed at the end of `01_script/script.md` (golden mango as the prize, the kind sharing ending, "brother" only, no Narada).
- **Word count 310** (below the 450–550 guide) accepted. The 5:00 cap makes 450 words impossible. Runtime is 4:40.
- **Peacock reference sheet: yes.** Add a 6th sheet for Kartikeya's peacock (it is in 6 shots).
- **Backup of text files to the branch: yes** (done).
- **Channel name:** the user asked me to suggest one. I recommended **"Mooshak's Story Time"** and have used it in the graphics briefs. The user has not explicitly confirmed it.
- **Credit gate:** the user picked **"Hold for now"**. Do not spend until the user says "go". Recommended next spend: stage 3a only.

## Files (the md files are APPROVED: do not edit or overwrite them)

- `BRIEF.md`: the original brief.
- `01_script/script.md`, `shotlist.md`, `bible.md`: approved. 33 shots, 4:40, 24 fps. Chant at shots 04, 19, 26, 32. Mooshak squeak at 02, 09, 16, 33. Child question pauses at 09, 14, 20–21.
- `02_prompts/prompts.json`: per shot: `vivideo` (raw output), `prompt_full` (Vivideo prompt + bible text + negatives), `prompt_short`, `prompt_seedance` (Seedance shots only), `keyframe_prompt`, models, durations, bible keys. Also `graphics` (G01, G02, G09, G21, G30, G33) and `krea_settings`.
- `log.md`: running log and credit totals. Keep it updated with every generation, model and credit cost.
- Timing source of truth: `01_script/shotlist.md` (net durations). Veo shots: 02, 13, 19, 20, 21, 30, 32 (8 s). Seedance shots: the other 25 (shot 33's 10 s background clip is Seedance). Shot 01 is a HyperFrames graphic.

## Tool findings

- **Vivideo:** style `animation_3d_character`. Text only, free.
- **Krea models:** `bytedance/seedance-2-5`, `google/veo-3.1`, `kling/kling-3.0` (backup), `google/nano-banana-pro`, `krea/krea-2/medium` and `/large`. No custom styles or moodboards yet. Moodboards only work with Krea 2 image models. Nano Banana Pro takes `image_urls` references.
- **Seedance 2.5:** 4–30 s, resolution `480p/720p/1080p` (**default is 720p, so set 1080p**), `start_image` plus `reference_images` (up to 30, not with `end_image`), `draft:true` gives a cheap 480p preview. `generate_audio` is deprecated and ignored, so strip audio in ffmpeg (`-an`). No negative-prompt field. Submit at most 12 jobs at once. A "completed" job with no result URL means the content filter refused it. Krea's guide says "slow/gentle/soft" can make clips run in slow motion, which is why `prompt_seedance` exists.
- **Veo 3.1:** durations 4, 6 or 8 s only. `generate_audio` default false. Resolution 720p/1080p/4K (set 1080p). No negative-prompt field.
- **Kling 3.0:** fetch `get_prompting_guide` for `kling/kling-3.0` before first use.
- **Krea pricing:** no per-generation price is shown anywhere. The plan card only: Pro 20,000 units for $35, Max 40,000 units for $70 (about $0.00175 per unit; Max includes unlimited relaxed generations). Roughly 78 units per Nano Banana 2 image, 241 per Seedance 2.0 video (length unstated). **After the first generations, read the real cost and re-estimate before any video spend.**
- **ElevenLabs:** TTS models `eleven_v3`, `eleven_v4`, `eleven_multilingual_v2`; SFX `eleven_text_to_sound_v2`; music `eleven_music_v1/v2/v2_5`; `creative_design_voice`; lipsync models `sync-lipsync-v3`, `veed-lipsync-v2`. Measured price: about 1 credit per character, $0.0002 per credit. The script is 1,639 spoken characters per full narration pass (narrator 1,409, Mooshak 152, Ganesha 78). Use `estimate_only` before every ElevenLabs generation.
- **Narrator shortlist** (soft Indian-English): Ria – Warm Indian Narrator `M6udCbeLpbqc4ZtMMDGJ`; Sahana – Expressive & Warm Storyteller `17cum4YqukEcj2pUa0hd`; Arjun – Gentle Indian Narrator `dahpPHJ9zA9ckbsyrVfz`. Alternatives: Surabhi `ch9J8IB6HKlEHQaWQFdk`, Prince `SuZjJOmejdKQNzQbif43`.
- **HyperFrames:** local skills **not installed**. Hosted compose and render are blocked for CLI agents. Setup: `npx skills add heygen-com/hyperframes` (npm registry is reachable). Ask the user to say "install it" first. Needed at Phase 5.
- **ffmpeg 6.1.1** has libx264, aac, loudnorm, xfade, sidechaincompress, subtitles and drawtext. Chromium and Node 22 are installed.
- **Canva:** thumbnail design tools are connected. Export URLs may need a network host allowed.

## Credit estimate the user was shown (guesses; counts are firm)

| Stage | Generations | Guessed cost |
|---|---|---|
| 3a References: 6 sheets × 4 options + 3 locations × 4 options, +25% re-rolls | about 45 images | 3,500–7,000 units ($6–$12) |
| 3b Keyframes: 32 stills, +35% redos | about 43 images | 3,400–6,700 units ($6–$12) |
| 3c Clips as briefed (Scenario A): 2 versions, +20% retries, 4 Kling backups | about 81 videos (Veo about 17, Seedance about 60, Kling 4), about 730 s | 61,000–113,000 units |
| Scenario A total | | about 70,000–130,000 units ($120–$230) |
| Scenario B total (lean): 1 version + about 1.4 tries, Veo only on shots 02, 13, 21 | | about 40,000–70,000 units ($70–$125) |

Alert the user if any stage goes 20% over (stage 3a: more than 54 images).

## Next steps, in order

1. Test the network (above). Fix with the user if needed.
2. When the user says **"go"**, run **stage 3a only**:
   - Character sheets with 4 options each for Ganesha, Mooshak, Kartikeya, Peacock, Shiva, Parvati: front view and 3/4 view side by side on a plain light background, using the `CHAR_*` text from `01_script/bible.md` word for word, plus the STYLE block and the negatives. No text in the image.
   - One image each for LOC_KAILASH_MORNING, LOC_WIDE_WORLD, LOC_KAILASH_EVENING (4 options each).
   - Show the options as a numbered contact sheet, let the user pick, and save picks to `03_refs/` with clear names (for example `ref_char_ganesha.png`). Never overwrite an approved file.
   - Confirm which tusk is broken and Ganesha's colour with the user on the sheets (see the bible's "Please confirm" table).
   - Create a Krea moodboard from the approved refs (Krea 2 models only). For Nano Banana Pro and Seedance/Veo, pass the refs as `image_urls` or `reference_images`.
   - Log every generation in `log.md`. Read the real credit cost from the first job and re-estimate.
3. Re-estimate 3b and 3c with real prices. Get the user's go-ahead. Then keyframes (contact sheet), **Checkpoint 2**, then clips (2 versions per shot, log why one was chosen, at most 2 retries per prompt), **Checkpoint 3**.
4. Phases 4–7 as in the brief, each with its checkpoint.

## Open items

- HyperFrames install (ask "install it").
- Channel name unconfirmed (assumed "Mooshak's Story Time").
- Optional lip-sync pass for shots 02, 17, 24 (price with `estimate_only`).
- Shorts approach (60 s, 9:16): either the 16:9 clips on a blurred background, or native 9:16 generations for 3–4 hero moments (extra credits). Ask when we reach Phase 6.
- Shot 21: the prompt leaves Mooshak out although the shot list has him.


---
## Update (2026-10-05, later session)

- Network: all Krea and ElevenLabs hosts now reachable.
- Stage 3a done: 9 references approved, saved in `03_refs/` (see `03_refs/PICKS.md`). Parvati uses `ref_char_parvati_v2.jpg`.
- Stage 3b done: 32 keyframes approved at Checkpoint 2, saved in `04_keyframes/approved/`. Prompts and reference URLs in `02_prompts/keyframe_requests.json`; job IDs in `04_keyframes/jobs.json`.
- Krea images used: 76 (all nano-banana-pro, 1K). Krea does not report per-job cost. The user's balance was 16k before keyframes. Ask for the current balance to calibrate.
- User is on Krea Pro.
- NEXT: stage 3c (clips). Do not spend until the user says go. Proposed first step is 3 test generations to learn real video prices: Seedance 2.5 draft 480p and 1080p of shot 04, and Veo 3.1 1080p 8 s of shot 02. Then re-plan the rest.
- Open: HyperFrames install, channel name, Shorts approach, shot 21 omits Mooshak.

- Video tests (see log #9-10): Veo 3.1 shot 02 and Seedance draft shot 04 look good, files in 05_clips/tests/. Seedance 1080p shot 04 (job 16449df1-3f57-4247-9012-bdf0ad44a90b) was still processing at 21:47 UTC; check with get_job before re-planning. Real per-clip costs are still unknown: need the user's Krea balance before and after.

- Seedance 1080p test finished and looks good (job 16449df1). User balance now 6,500 units. Krea plans (show_plans): Pro 20,000 units $35 (no unlimited relaxed), Max 40,000 units $70 (unlimited relaxed generations), compute unit packs available. Waiting for the user to choose how to fund or cut the remaining 29 clips.

- **CLIP RUN PAUSED (2026-10-05, 22:05 UTC), balance ~495 units.** Submitted: shots 03,05,06,07,08,09,10,11,12,13,14,15,21,32 (see 05_clips/jobs.json; finished files go to 05_clips/raw/, test finals for 02 and 04 are in 05_clips/tests/). NOT submitted: 16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,33 (16 shots).
- Real prices (units): Veo 3.1 1080p 8 s no audio = 1,185; Seedance 1080p 9 s = 3,791; Seedance 720p 9 s = 1,541. Refused requests return a free price quote.
- Proposed plan for the 16 remaining: Veo 3.1 1080p 8 s, start image only, prompt_full (no reference_images). About 19,000 units. Shots with a longer timeline (24, 25, 27, 29, 31, 33) get the 8 s clip stretched a little or held in the edit. Needs a unit top-up first.

- Clips downloaded so far (05_clips/raw/ + 05_clips/tests/): 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 15, 21, 32. Shot 14 job 9eafe136-bc2d-40af-8d4c-e60f1a2186df was still processing at 22:09 UTC: download it. Veo requests for the remaining 16 shots are ready in 02_prompts/clip_requests_veo_remaining.json (16,17,18,19,20,22,23,24,25,26,27,28,29,30,31,33). User said 8k credits available but the API reported 495 units: check the connected Krea account.

- **CLIPS STATUS (22:25 UTC):** 29 of 32 done, in 05_clips/raw/ (02 and 04 in 05_clips/tests/). Missing: 23, 27, 28 (Veo content_policy rejection; not charged). Shot 31 has an extra girl on the right edge (crop in the edit or redo). Balance 88 units. Options for the 3: Veo again with reworded prompt (1,185 each; rejected jobs seem not charged) or Seedance 720p 8 s (~1,370 each; Seedance accepted similar shots 07, 11, 12, 14). Shot 21 has a floating '3'.
