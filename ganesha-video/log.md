# Generation log

Every generation: tool, model, what it was for, credits spent, and the outcome.
Read-only calls (listing models, voices, styles) cost nothing and are logged once as "setup".

| # | Date | Phase | Tool | Model / voice | Purpose | Credits | Outcome / notes |
|---|------|-------|------|---------------|---------|---------|-----------------|
| 0 | 2026-10-05 | 0 Setup | Vivideo | list_video_prompt_styles | Confirm `animation_3d_character` exists | 0 | Found: animation_anime, animation_3d_character, animation_motion_graphics |
| 0 | 2026-10-05 | 0 Setup | Krea | list_models (image, video), list_styles | Confirm Seedance 2.5, Veo 3.1, Kling 3.0 | 0 | All present. No custom styles yet. |
| 0 | 2026-10-05 | 0 Setup | ElevenLabs | list_voices, get_flow_node_types | Confirm TTS, music, SFX, Indian-English voices | 0 | 25 Indian-English voices found. TTS v3/v4, SFX v2, Music v1/v2/v2.5 available. |
| 0 | 2026-10-05 | 1 Script | (writing) | – | script.md, shotlist.md, bible.md written and approved at Checkpoint 1 | 0 | Approved files are now read-only. |
| 0 | 2026-10-05 | 2 Prompts | Vivideo | build_video_prompt x32 (animation_3d_character) | One image-to-video prompt per shot (02-33) | 0 | Saved in 02_prompts/prompts.json. Text only, no credits. |
| 0 | 2026-10-05 | 2 Prompts | Krea | get_model_schema x3, get_prompting_guide x1, show_plans | Read limits and wording rules for Seedance 2.5, Veo 3.1, Nano Banana Pro | 0 | Krea tools show no per-generation price. Plan card only: Pro 20,000 units $35, Max 40,000 units $70. |
| 0 | 2026-10-05 | 2 Prompts | ElevenLabs | creative_generate_speech estimate_only x2 | Price check for narration (v3 and multilingual v2) | 0 | 437 credits = $0.0874 for 437 characters on both models, so about 1 credit per character. These calls left 2 empty flows in the workspace. Nothing was generated or charged. |
| 1 | 2026-10-05 | 3a Refs | Krea | google/nano-banana-pro 1K 16:9 | 36 images: 6 character sheets x4 (Ganesha, Mooshak, Kartikeya, Peacock, Shiva, Parvati) + 3 locations x4 | not shown by API (see note) | Submitted in 3 waves 21:00-21:03 UTC. Job IDs in 03_refs/options/jobs.md. Within 45-image estimate (36). All 36 completed, downloaded to 03_refs/options/ with numbered contact sheets (sheet_*.png). Four files came back as small JPEGs (mooshak 1-2, peacock 4, parvati 2), lower quality. No credit cost reported by any job; real cost still unknown. |
| 2 | 2026-10-05 | 3a Refs | Krea | google/nano-banana-pro 2K 16:9 | Parvati re-render x1 (user-approved), job e0793c43 | not shown by API | Done. 2752x1536 JPEG, sharp, but body is heavier and more adult than the family style. Saved as options/parvati_rerender1.jpg, NOT yet approved. Used 2K by mistake (plan was 1K), so it may cost more than the other images. Total 3a images now 37. |
| 3 | 2026-10-05 | 3b Keyframes | Krea | google/nano-banana-pro 1K 16:9, refs as image_urls | Test keyframes: shot 03 (job b3318a05), shot 11 (job 2ac8e818), shot 03 retest with Ganesha clarification (job 95e823e3) | not shown by API | Shot 11 good. Shot 03: Mooshak good, Ganesha drifted (ornate crown, visible dark hair, paler skin), so added one clarifying sentence to the preamble for Ganesha shots (bible text unchanged) and retested. Files in 04_keyframes/options/. |
| 4 | 2026-10-05 | 3b Keyframes | Krea | google/nano-banana-pro 1K 16:9, refs as image_urls | Keyframes for the remaining 30 shots (02, 04-10, 12-33), one attempt each. Job IDs in 04_keyframes/jobs.json | not shown by API | Submitted 21:24-21:29 UTC. Stage 3b so far 33 images (3 tests + 30), estimate was 43 (alert at 52). Results pending review. |
| 5 | 2026-10-05 | 3b Keyframes | Krea | google/nano-banana-pro 1K 16:9 | Redo round 1: shots 18, 21, 23, 29 (jobs 9ad2b305, 1cd71833, 9c5f8e38, 54726641) | not shown by API | Reason: 18 had a face on the banyan tree and a thatched hut; 21, 23, 29 had Ganesha in a yellow dhoti, Shiva in leopard print, location drift; 29 far too dark. Added a clothing/location clause to the preamble. 3b total now 37 images (estimate 43, alert 52). Shots 26 and 33 still rendering at this point. |

## Running total

| Service | Credits spent | Estimate (set before Phase 3) | Alert at +20% |
|---------|---------------|-------------------------------|---------------|
| Krea | 74 images (units not reported by API) | 3a: 45 images | 54 images |
| ElevenLabs | 0 | TBD | TBD |
| Canva | 0 | n/a | n/a |
