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
| 1 | 2026-10-05 | 3a Refs | Krea | google/nano-banana-pro 1K 16:9 | Ganesha sheet x4 (1 done, 3 queued), Mooshak x4, Kartikeya x4 | not shown by API | Job 60d1235b done (good, matches bible). Other 11 submitted 21:00 UTC. Job results show no credit cost; read balance/cost separately. |

## Running total

| Service | Credits spent | Estimate (set before Phase 3) | Alert at +20% |
|---------|---------------|-------------------------------|---------------|
| Krea | 0 | TBD | TBD |
| ElevenLabs | 0 | TBD | TBD |
| Canva | 0 | n/a | n/a |
