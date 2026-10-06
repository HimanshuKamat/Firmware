# YouTube package: "Ganesha's Big Race"

Channel name used on screen: **Mooshak's Story Time** (assumed in Phase 0; the channel name appears only in the intro graphic, so it is a one-line change in `07_graphics/projects/intro/index.html` and a re-render).

Files to upload (all in `09_final/`):

| File | What it is |
|---|---|
| `Ganesha_Big_Race_1080p.mp4` | The video. 1920x1080, 24 fps, H.264 High, about 12 Mbps, AAC 320 kbps 48 kHz, -14 LUFS integrated, true peak below -1 dBTP, 4:40 long |
| `captions.srt` | Captions made from the narration timings (English, 63 cues). Upload under *Subtitles > Add language > English > Upload file > With timing* |
| `thumbnail_A_ganesha_close_up.jpg` (recommended), `thumbnail_B_who_will_win.jpg`, `thumbnail_C_golden_mango.jpg` | Three 1280x720 thumbnails (under 2 MB each) |
| `Ganesha_Big_Race_Shorts_9x16.mp4` | 60-second 1080x1920 Shorts teaser that ends on a "full story on the channel" card |

## 1. Title options (under 60 characters)

1. **Ganesha's Big Race | A Ganesha Story for Kids** (46 characters, recommended: it matches the on-screen title card)
2. **How Ganesha Won the Race! Ganpati Bappa Morya** (49)
3. **Ganesha and the Golden Mango | Kids Story** (43)

## 2. Description (paste as is)

```
Join Mooshak the little mouse for a gentle Ganesha story made for children aged 3 to 6!

Baba Shiva holds a golden mango and invites his sons to a race: go around the world three times, and the first one back wins. Kartikeya zooms off on his shiny blue peacock. But little Ganesha has no peacock... so he thinks and thinks, and has the loveliest idea. What does he do? Watch to find out!

Sing along, count the modaks, count the circles, flap like a peacock, and say "Ganpati Bappa... Morya!" with us.

The lesson: Our family is our whole world.

Chapters
0:00 Welcome to Mooshak's Story Time
0:06 Hello, I am Mooshak!
0:20 Say it with me: Ganpati Bappa Morya!
0:27 Life on Mount Kailash
0:59 Can you count the modaks?
1:09 The golden mango
1:17 Baba's big race
1:34 Kartikeya flies over the world
1:42 Can you flap your arms?
1:51 Ganesha has no peacock
2:07 Ganesha has an idea!
2:23 Around Amma and Baba, slow and steady
2:39 One... two... three circles!
2:47 Kartikeya is surprised
3:03 "They are my whole world!"
3:12 The golden mango for Ganesha
3:21 Hooray for Ganesha!
3:28 Sharing the mango
3:45 A cosy evening on Kailash
3:54 The secret: our family is our whole world
4:02 Sing-along: Hold your family, hold them near
4:20 Bye-bye, little friend!

Song lyrics
Hold your family, hold them near,
They are your whole world, dear!
Ganpati Bappa... Morya!
Ganpati Bappa... Morya!

Made with love for little ones. This video was created with the help of AI tools: the pictures and animation were generated with Krea (Veo and Seedance video models), the voices, music and sound effects with ElevenLabs, and the titles and graphics with HyperFrames, then edited and assembled by hand.

#Ganesha #KidsStories #GanpatiBappaMorya
```

## 3. Tags (15, paste comma separated)

```
Ganesha story for kids, Ganesh Chaturthi for kids, Ganpati Bappa Morya, Ganesha animated story, Hindu stories for children, Indian bedtime story, Ganesha and Kartikeya race, Ganesha golden mango story, moral story for kids, family values for kids, count with me for toddlers, interactive story for toddlers, Mooshak the mouse, preschool story, animated kids story English
```

## 4. Playlist

Create or use the playlist **"Ganesha Stories for Kids"**. If you plan a series, name the next ones the same way ("Ganesha and the Moon", "Ganesha's Broken Tusk") and keep Mooshak in the title or the thumbnail so the series is easy to spot.

## 5. Upload settings (YouTube Studio)

| Setting | Choose | Why |
|---|---|---|
| Audience | **"Yes, it's made for kids"** | It is aimed at toddlers and young children (COPPA). This turns off comments, personalised ads, notifications and some other features. |
| Altered or synthetic content | **No** (recommended), see note below | YouTube's disclosure question is about *realistic* altered or synthetic content that viewers could mistake for real people, places or events. This is clearly stylised 3D animation with cartoon characters, which YouTube says does not need the label. The AI credit line in the description is kept anyway, for transparency. |
| Category | **Education** (alternative: Film & Animation) | Education suits a story with a moral and counting games. |
| Captions | Upload `captions.srt` | Helps parents watching with the sound off and helps search. |
| Video language | English | |
| Thumbnail | `thumbnail_A_ganesha_close_up.jpg` | Close-up Ganesha with the modak, Mooshak in the corner, big words readable at phone size. Use B or C for an A/B test if your account offers "Test & compare". |
| Visibility | Public (after you have watched it once) | |

**Note on the AI-disclosure setting.** I could not check YouTube's live help pages from this environment, so this is my understanding of the rule as I last knew it: the label is required for *realistic* content made or altered with AI (for example a real person's face or voice, or a realistic event), and not for clearly unrealistic content such as animation. Open the "Altered content" help link in the upload form to confirm today's wording. If you are unsure, choosing "Yes" is harmless for a clearly animated video; it only adds a small "Altered or synthetic content" line under the video.

**Note on end screens and cards for "made for kids" videos.** The end screen at 4:20 has room for YouTube's subscribe button and two video suggestions (see below). As far as I know, YouTube turns off cards and end screens on videos marked "made for kids". If *End screen* is greyed out in the editor, the video still works: the frames and circle read as a friendly "more stories" frame. If you add end-screen elements, position them as follows (1920x1080 frame; percentages of width and height):

| Element | Left (px) | Top (px) | Width x Height (px) | Left % | Top % |
|---|---|---|---|---|---|
| Video suggestion 1 ("Watch next") | 108 | 108 | 480 x 270 | 5.6 | 10.0 |
| Video suggestion 2 ("More stories") | 640 | 108 | 480 x 270 | 33.3 | 10.0 |
| Subscribe (circle) | 108 | 766 | 200 x 200 | 5.6 | 70.9 |

Start the end screen at 4:20 (the last 20 seconds). Full table: `07_graphics/end_screen_layout.md`.

## 6. Shorts upload (optional)

Title: **Ganesha's Big Race in 60 seconds! #shorts** (46 characters). Description: "Mooshak and Ganesha race around the world! Full story on the channel: Ganesha's Big Race | A Ganesha Story for Kids. #Ganesha #KidsStories #shorts". Same audience setting (made for kids) and category.

## 7. Respect and accuracy notes

- Ganesha, Shiva, Parvati and Kartikeya are always shown gently and kindly; all comedy comes from Mooshak.
- Iconography choices (two arms for Ganesha, one face for Kartikeya, Shiva's small friendly cobra and closed third eye, Ganesha's right tusk broken) are the choices recorded in `01_script/bible.md`. Ganesha is shown with orange skin, which is a common devotional colour. If your family's tradition differs, the details are in the bible.
- The story is told as many families tell it: the race around the world, and Ganesha circling his parents because they are his whole world.
