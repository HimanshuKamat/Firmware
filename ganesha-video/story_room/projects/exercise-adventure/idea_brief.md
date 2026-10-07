# Idea Brief: Kids' exercise adventure (working title)

**Slug:** exercise-adventure   **Date:** 2026-10-07   **Owner:** project owner

## The owner's idea, word for word
> i want to create a video for kids to exercise. simple exercises that kids can do and follow making it interesting so they keep watching it. video should be 15-30 mins. timer counter. story based

## Defaults chosen (the owner can change any of them)
| Item | Default | Note |
|---|---|---|
| Audience | ages 3 to 6, core 4 to 5, watching at home with a parent nearby | Older kids (6 to 10) would change the exercises and the pace |
| Runtime | one 20-minute master built from short chapters, so it can be cut to 15 or extended to 30 | Hard range 15 to 30 minutes |
| Format | 16:9, 1920x1080, 24 fps, 3D-animated, English | Same look as "Ganesha's Big Race" |
| World and guide | Mooshak's world (Mooshak the mouse leads; Ganesha and family can appear) | Reusing the approved character references saves the whole reference stage |
| Who shows the moves | animated characters, with a clear simple pose for each move | No real instructor |
| Structure | a quest with stations: welcome, warm-up, 4 adventure chapters, cool-down, goodbye | Each station is a short story beat plus a few exercises |
| Timer and counter | on-screen countdown ring, rep counter, journey map with stars collected | Made as graphics (free, local), voiced counting in sync |
| Intensity | alternates energetic and calm; no jumping from furniture, no fast spinning; seated option for every move | Safety rules in `roles/movement_designer.md` |
| Treatment | gentle, positive, respectful, comedy from Mooshak | |
| Release | Trend Scout decides | |

## Early flags from the Facilitator (before any research comes back)
1. **Length drives cost, so the film must be designed around reuse.** The first film (4:40) cost about 66,000 Krea units (about USD 115) [E]. If every second of a 20-minute film were a new clip: Veo about 148 units per second x 1,200 s = about 178,000 units (about USD 311); Seedance about 421 per second = about 505,000 units (about USD 884). Not acceptable. The plan: loopable exercise clips (the same 8 s move repeated while a counter runs), few unique story shots, graphics for timer and counter.
2. **Preliminary clip budget for a 20-minute master** [E, to be refined by the Production-Feasibility critic]: welcome 1:00 + warm-up 2:00 + 4 adventures of about 3:45 each (about 45 s story, three exercises of about 50 s, a short transition) + cool-down 1:30 + goodbye 0:30. About 45 to 50 unique 8 s clips (24 story, 12 exercise, about 10 for warm-up, cool-down and ends). That is about 56,000 units lean (about USD 97) and about 80,000 expected (about USD 140), similar to the first film.
3. **Unproven risk: do repeated clips look good?** An 8 s move looped six times can look robotic. Mitigations to test with one clip before committing: two clips per exercise from different angles, forward-and-reverse playback for symmetrical moves, small zooms, changing backgrounds, and the counter and music carrying the rhythm. This costs about 1,185 units (about USD 2) for the test; no credits are spent without approval.
4. **Safety:** exercises must be age-appropriate and safe in a small room, each with a seated alternative; an adult should be nearby. Official physical-activity guidance (WHO and others) will be checked by the researchers before the concept locks [verify].
5. **Voice and timing are the easy part:** counting aloud ("one, two, three...") is generated as text-to-speech, so its timing is exact and the on-screen counter can be cued to it.

## Must-haves and must-nots from the owner
- Must include: simple exercises kids can follow; a timer and counter on screen; story based; 15 to 30 minutes; keeps kids watching.
- Must not include: nothing stated yet.
- Lesson the owner has in mind: none stated (default: moving together is fun and makes us strong and happy).

## Questions for the owner (only these three are essential)
1. **Age range:** 3 to 6 (default), or older?
2. **World:** Mooshak's world with Ganesha and family (default, saves credits), or a brand-new world (jungle, space, ocean)?
3. **Who shows the moves:** animated characters (default), or a real person shown on screen?

---

## Update 2026-10-07: the owner's answers
- **Audience:** ages 3 to 6 (confirmed).
- **Cast:** two new sisters, **Tisha (4 to 5)** and **Raahi (2 to 3)**. Mooshak is no longer assumed; a new world is open (the Spark will propose worlds).
- **Who shows the moves:** animated characters. The owner will consider a real person only if the Facilitator judges it more engaging, and then as an AI avatar.
- **Video provider:** Google's Gemini API directly (Veo 3.1), not Krea.

## Facilitator findings on the provider (checked 2026-10-07 against Google's pricing page, last updated 2026-10-07)
| Veo 3.1 tier on the Gemini API | 720p | 1080p | 4K | Per 8 s clip at 1080p |
|---|---|---|---|---|
| Standard | $0.40 / s | $0.40 / s | $0.60 / s | $3.20 |
| Fast | $0.10 / s | $0.12 / s | $0.30 / s | $0.96 |
| Lite | $0.05 / s | $0.08 / s | not supported | $0.64 |

Audio is included in the price (it cannot be switched off; strip it in the edit). You are charged only for videos that generate successfully. Paid tier only; no batch discount for Veo.
- **Compared with Krea:** the first film's Veo 3.1 clips cost 1,185 Krea units per 8 s, about $2.07 at the Max plan rate, or about $0.26 per second. So **Google Standard ($0.40 / s) is about 54 percent MORE expensive than Krea.** Google Fast is about 54 percent cheaper and Lite about 69 percent cheaper. ElevenLabs' hosted Veo 3.1 Fast was $0.97 per 8 s, the same as Google Fast. **The saving comes from using the Fast or Lite tier, not from going direct.** Whether Fast or Lite is good enough is untested; the shot-31 redo on Fast was clean.
- **Images (keyframes):** Google lists Nano Banana Pro at $0.134 per 1K or 2K image ($0.067 in batch), Nano Banana 2 at $0.067 (1K), and newer cheaper models from about $0.034.
- **Rough cost of the 20-minute plan** (about 47 clips of 8 s = 376 s of video) [E]: Lite about $30, Fast about $45, Standard about $150, Krea about $97. Add about 40 percent for redo clips and images.
- **Practical:** `generativelanguage.googleapis.com` is reachable from this environment, but no Gemini API key is set here and this session has no Google video connector. To generate through Google directly, the owner needs a paid-tier API key added as an environment secret (see the session's environment settings). Until then the plan stays on paper.
- **Not verified:** the exact Veo rules on depicting children (this session could not read Google's Veo guide page). Earlier on Krea, the same Veo 3.1 model refused three shots with two child-like characters together. Two small girls in most shots is the biggest production risk; test two or three typical shots before committing.

## Update 2026-10-07 (2): one child to start
- **Cast now:** one girl, aged 3 to 4, working name **Tisha** (change if the owner prefers another). **Raahi** is parked as a possible little sister in a later episode.
- **Companion:** none human. Optional non-speaking animal or creature friend per world. The viewer is Tisha's buddy: she speaks to the camera and waits for the child, as in participatory shows.
- **Effect on production:** one child per shot (no child-pair shots), one character to keep on-model, simpler tests.

## Findings from the market research that change this brief (market_trends.md, verified later)
- **Made for Kids switches off cards, end screens, comments and notifications** [S]. Next-watch prompts must be inside the picture.
- **"Inauthentic content" rule:** character series with a different story problem and ending per episode are allowed; templated, repeated scenarios are at risk [S]. So each chapter of this film needs its own problem and twist; "story beat + three exercises" must not feel stamped out.
- **Fully animated work needs no AI disclosure label, but YouTube has been under pressure** over AI content in kids' feeds (Fairplay letter, April 2026; YouTube says AI in YouTube Kids is limited to "a small set of high-quality channels") [S, one point conflicting]. Trust signals: low cadence, consistent characters, named human reviewer, no scary beats, a plain "made with AI tools" note.
- **Calendar:** Children's Day is 14 Nov 2026 (go-live about 24 Oct); Makar Sankranti and Pongal 15 Jan 2027 (go-live about 25 Dec). Diwali (8 Nov 2026) is too close for a new 20-minute film.
- **Brand flag:** "Bal Ganesh" (Shemaroo) already features Ganesha with a mouse called Mooshak [S, weak]. This new film uses new characters, so it is unaffected, but the channel name "Mooshak's Story Time" for the first film should be checked before publishing.
