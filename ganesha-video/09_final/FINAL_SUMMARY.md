# Ganesha's Big Race: final summary

**Result:** a finished 4:40 animated children's story (limit 5:00), 1920x1080, 24 fps, H.264 High, about 12 Mbps video, AAC 320 kbps 48 kHz, loudness -14.0 LUFS integrated, true peak -1.5 dBTP, plus captions, a 56-second Shorts teaser, three thumbnails and the YouTube package. No black frames, no frozen frames, audio and picture start together (checked with ffmpeg).

## 1. Files (all in `ganesha-video/09_final/` on branch `claude/amazing-pasteur-y5im4h`)

| What | File |
|---|---|
| **Full video, 1080p master** (stored in 5 parts because GitHub refuses files over 100 MB; see `parts/JOIN.md`) | `parts/Ganesha_Big_Race_1080p.mp4.part00` to `part04`, checksum in `SHA256SUMS.txt` |
| Quick-look copy of the video (540p, 25 MB) | `Ganesha_Big_Race_preview_540p.mp4` |
| **Shorts teaser** 9:16, 1080x1920, 56 s, ends on "Watch the full story on the channel!" | `Ganesha_Big_Race_Shorts_9x16.mp4` (preview: `Ganesha_Big_Race_Shorts_preview_540x960.mp4`) |
| **Captions** (63 cues) | `captions.srt` |
| **Thumbnails** 1280x720 (A recommended) | `thumbnail_A_ganesha_close_up.jpg/.png`, `thumbnail_B_who_will_win.jpg`, `thumbnail_C_golden_mango.jpg` |
| **YouTube package** (3 titles, description with chapters, tags, playlist, upload settings, end-screen layout) | `youtube_metadata.md`, `../07_graphics/end_screen_layout.md` |
| Full-mix audio (not in git, regenerate with `../06_audio/build_audio_final.py`) | `audio_final_48k.wav` |
| Canva | Thumbnail A is also saved as an editable Canva design: https://www.canva.com/d/2Mph8NZN_IFpVjK |

How it was built, so any piece can be redone: picture `08_edit/build_base.py`, graphics `07_graphics/projects/*` (HyperFrames, CLI v0.8.136), audio `06_audio/build_sfx_v2.py` and `build_audio_final.py`, final assembly `08_edit/build_final.py`, Shorts `08_edit/build_shorts.py`, captions `09_final/build_srt.py`. Every generation is logged in `log.md`; hand-over notes are in `HANDOFF.md`.

## 2. What is in the video

Intro (6 s, "Mooshak's Story Time"), title card, 32 story shots with 0.5 s crossfades, counting overlays for the modaks and the three circles, a "flap like a peacock" prompt, "Ganpati Bappa... Morya!" chant captions, the lesson card ("Our family is our whole world."), sing-along lyrics over the song, and a 20-second end screen with room for two video suggestions and the subscribe button. Sound: Sahana as narrator, Elmoe as Mooshak, Mini as Ganesha; a flute-and-tabla story bed that ducks under the voice; an original sung goodbye song; 41 gentle sound-effect cues on top of three looping ambience beds (morning, flight, evening).

## 3. Credits used

| Service | Used | Notes |
|---|---|---|
| Krea | about 66,000 units (76 images, 32 clips) | The API does not report per-job cost, so this is estimated from balance changes: stills about 4,000, three price tests about 5,300, 14 clips about 46,000, last 16 clips about 10,400. |
| ElevenLabs | about 12,250 credits (about $2.45) | Narration 2,233 (incl. 3 voice samples), first sound effects 200, music 4,245, song transcript check 209, shot 31 redo 4,848, sound effects v2 513 |
| HyperFrames | 0 | Installed locally from npm and rendered on this machine, so no HeyGen credits. |
| Canva | 0 | One design created and edited. |

## 4. Shots I am not fully happy with

- **Shots 23, 27 and 28** are slow push-ins on still pictures (Veo's moderation refused to animate them). They match in colour and look but the characters do not move.
- **Shot 21** had numbers (2 and 3) floating in the sky that Veo drew by itself. I removed them frame by frame (`08_edit/fix_shot21.py`); a few tiny specks of the melting digit remain for about two frames near 2:46-2:47. The thatched hut in that shot still differs from the other shots (accepted earlier).
- **Shot 31** had an extra girl who wandered in; I regenerated it from the approved keyframe with a locked cast and no camera pan, and it now shows exactly the five family members.
- **Lip-sync** was not done: when Mooshak, Ganesha or the narrator speak, mouths move gently but are not matched to the words.
- Several Veo shots are slowed down by up to 20% (and the last frame is held for up to 1 s) to fit the narration. Shot 33 ends with a slow push-in on its last frame.
- **I cannot listen**, so sound placement is calculated, not heard. Please listen once with headphones, especially: the song's joined verse and "Morya" (a 7.5-second cut made on the beat), the music level under the narrator, and the new wing-flap and footstep sounds (the wing flaps were slowed to half speed to sound like a bigger bird).

## 5. What I would improve next time

1. A listen-through by a person before picture lock: music balance, effects timing, the song splice.
2. A lip-sync pass for the character lines (price it first with `estimate_only`; I did not buy it unasked).
3. Generate the Shorts natively in 9:16 for 3-4 hero moments instead of putting the 16:9 picture on a blurred background.
4. Ask Krea for a price per job before submitting a batch (it would have avoided the one time the balance ran out).
5. Confirm the channel name early: it appears in the intro graphic and the description; it is a one-line change in `07_graphics/projects/intro/index.html` and a re-render.
6. Check your Studio settings: made-for-kids videos may not allow end screens or cards (see `youtube_metadata.md`).

## 6. Respect and safety checks

Ganesha, Shiva, Parvati and Kartikeya are never scared, hurt or laughed at; Mooshak carries the comedy. No flashing: all fades are at least 0.25 s and no element blinks. Sound is gentle (nothing loud or sudden), loudness is -14 LUFS with a true peak under -1 dBTP. Iconography choices are in `01_script/bible.md`; if your family's tradition differs, say so and I will change the affected prompts and re-render only those shots.
