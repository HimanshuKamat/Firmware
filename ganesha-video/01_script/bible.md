# Character and world bible (draft 1, for Checkpoint 1)

**How this file is used.** Every prompt is built the same way, with no paraphrasing:

`STYLE` + the `CHAR_*` block for every character in the shot (word for word) + the `LOC_*` block + the shot's action and camera + `NEGATIVES`.

If a description needs to change, change it here and rebuild the prompts. Never edit one prompt by hand.

---

## STYLE (same text in every shot)

```
Soft, rounded 3D character animation in a warm, bright, modern feature-film style. Soft global illumination, saturated but gentle colours, big clear expressive faces, simple uncluttered background, cosy and gentle mood.
```
Vivideo style: `animation_3d_character` (stylized 3D character animation, soft global illumination, playful and warm). Same style on every shot.

## NEGATIVES (same text in every shot)

```
no text, no logos, no scary expressions, no extra limbs, consistent character design
```
Your four negatives, unchanged. Ganesha's block says "exactly two arms" so "no extra limbs" works with it.

## Palette (keep colours consistent between characters, graphics and thumbnail)

| Name | Hex | Used for |
|---|---|---|
| Saffron orange | #F28C28 | Ganesha's skin, Shiva's waist cloth |
| Sunset red | #D63B2F | Ganesha's dhoti, Parvati's saree, Mooshak's scarf |
| Marigold gold | #F6B21A | Crowns, borders, jewellery, sash, title type |
| Peacock teal | #1AA6A0 | Kartikeya's dhoti, the peacock |
| Cream | #FFF3DC | Backgrounds, terrace stone, graphics |
| Sky blue | #8FD3F4 | Sky |
| Meadow green | #8CCB6B | Grass, hills |
| Rose pink | #F4A6B8 | Inner ears, Mooshak's ears, flowers |

---

## Characters (word-for-word prompt text)

### CHAR_GANESHA
```
Ganesha, a cheerful child Ganesha in soft rounded 3D animation. Toddler proportions, about three heads tall, with a big round head and a round chubby belly. Soft saffron-orange skin with lighter peach on his belly. A friendly elephant head with big floppy ears that are pink inside, two large kind dark-brown eyes with tiny white highlights, and a gently curled trunk turning to his left. One long ivory tusk on his left and one short broken tusk with a rounded tip on his right. A small gold crown, a red tilak on his forehead, a gold necklace and gold armbands. A deep sunset-red silk dhoti with a wide gold border and a marigold-yellow sash. Exactly two arms: his right hand holds a golden-brown modak, his left hand is open and relaxed. Bare feet with tiny gold anklets.
```

### CHAR_MOOSHAK
```
Mooshak, a small chubby baby mouse in soft rounded 3D animation, about knee-high to Ganesha. Soft warm grey-brown fur with a cream belly, big round pink ears, huge shiny black eyes with white highlights, a tiny pink nose, a few small whiskers, tiny pink paws and a long, thin, curled pink tail. He wears a small red-and-gold scarf. Cheeky, bouncy and always smiling.
```

### CHAR_KARTIKEYA
```
Kartikeya, Ganesha's brother, a cheerful boy with one face, in soft rounded 3D animation. Slightly taller than Ganesha, with warm golden-brown skin, big friendly dark eyes and a bright, kind smile. Black hair in a neat topknot with one small blue-green peacock feather. Bare chest, a peacock-teal silk dhoti with a gold border, gold earrings, a gold necklace and gold armbands. He carries a small golden leaf-shaped spear with a rounded, safe tip.
```

### CHAR_PEACOCK
```
Kartikeya's peacock, a big friendly peacock in soft rounded 3D animation, large enough for a child to ride. Shiny peacock-blue and teal feathers, a small gold crest, kind round eyes, wide soft wings, and a long tail of feathers with gold-and-green eye patterns.
```

### CHAR_SHIVA (called "Baba")
```
Shiva, called Baba, a calm, gentle, loving father in soft rounded 3D animation. Soft silvery-blue skin, three thin white ash stripes and a small closed third eye on his forehead, kind eyes and a peaceful smile. Black hair in a tall topknot with a silver crescent moon. A tiny smiling cobra rests around his neck like a necklace, with a rudraksha bead necklace. A saffron-orange cloth around his waist. His golden trident, with a small drum tied to it, stands beside him. Strong, warm and loving.
```

### CHAR_PARVATI (called "Amma")
```
Parvati, called Amma, a graceful, loving mother in soft rounded 3D animation. Warm golden-brown skin, big kind dark eyes, a warm smile and a small red bindi. Long black hair in a soft braid with white jasmine flowers and a small gold crown. A deep red silk saree with a wide gold border and a green shawl, gold bangles, earrings and necklace. Gentle, patient and glowing with love.
```

### Props
```
PROP_MODAK: a golden-brown modak, a small round dumpling with a softly pointed top and pleated edges, shiny and sweet-looking.
PROP_MANGO: a glowing golden mango, round and shiny, with a small green leaf and soft golden sparkles.
PROP_PLATE: a small round golden plate.
```

---

## Locations (word-for-word prompt text)

### LOC_KAILASH_MORNING
```
Mount Kailash home in soft rounded 3D animation, bright golden morning. A wide cream-white stone terrace on a green meadow with small pink and white flowers, a small round-roofed cosy home with a saffron flag, marigold garlands on a simple arch, a big friendly banyan tree, soft pastel snowy peaks and fluffy white clouds behind, warm golden sunlight, simple clean background.
```

### LOC_WIDE_WORLD
```
The wide world seen from the sky in soft rounded 3D animation. Gentle green hills, a silver winding river, round forests, pastel mountains and fluffy white clouds, tiny waving animals (an elephant, a deer and a monkey) far below, a bright blue sky, warm sunlight, simple clean shapes.
```

### LOC_KAILASH_EVENING
```
The same Mount Kailash terrace at golden evening in soft rounded 3D animation. A pink-gold sky, rows of small glowing clay lamps along the terrace, marigold garlands, a few soft fireflies, a big friendly banyan tree, warm gentle light, simple clean background.
```

---

## Sacred-detail decisions

**Approved by you**
- Ganesha has **two arms**.
- Kartikeya has **one face**.
- Shiva keeps his **cobra and third eye**, made friendly (tiny, smiling, gentle, closed eye).

**My choices. Please confirm or change.**

| Detail | What I did | Why |
|---|---|---|
| Ganesha's skin colour | Soft saffron-orange all over, including the elephant head | Orange or vermilion is a common devotional colouring. Traditions also use red, yellow, white or blue-grey. Tell me if your family's Ganpati looks different. |
| Which tusk is broken | His right tusk, on the viewer's left | I believe "right tusk broken" is the common convention, but pictures vary, so I'm not certain. The reference sheets will show it and you can flip it. |
| Trunk | Curled to his left | The most common home form. |
| Ganesha's snake belt and extra-hand items (axe, noose) | Left out | Two arms leave no room for them, and a snake on every character is too much for toddlers. The snake stays on Shiva only. |
| Shiva's Ganga (stream of water in his hair) and tiger-skin | Left out. Plain saffron waist cloth instead | Hard for the models to draw and easy to get wrong. |
| Shiva's blue throat | Not shown | Keeps his look simple. |
| Kartikeya's spear (vel) | Kept, small, with a rounded tip, never used as a weapon | It is his sacred symbol, and the rounded tip keeps it safe. |
| Mooshak's size | A small baby mouse, not a large rat | Friendlier for toddlers, and a better comic sidekick. |
| Jewellery, crowns, clothes | Simple gold-and-red styling | Respectful and readable on a small phone screen. |

## Respect rules for every shot

1. Ganesha, Shiva, Parvati and Kartikeya are never shown scared, angry, hurt, falling over or laughed at. All comedy comes from Mooshak.
2. No slapstick or pratfalls for the deities.
3. Sacred items (trident, drum, spear, modak) are shown carefully and never used as toys or weapons.
4. No written words or Sanskrit script inside generated images, because the models garble them. All text comes from HyperFrames and Canva.
5. Faces stay gentle at all times, with soft smiles and kind eyes.
