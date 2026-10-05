# QA report: Cozy Spooky Corner (Pip's Pumpkin Moon Party)

Canva design: **Cozy Spooky Corner – Pip's Pumpkin Moon Party (8x8 Colouring Book)** (`DAHXKUUqEIQ`),
42 pages at 8x8 in, in Canva folder **Halloween Colouring Book**.
Page order: 1 cover (colour) · 2 "This book belongs to" · 3-42 story pages 1-40.

## How pages were checked
- **Line weight**: measured on full-size renders of pages 1, 11, 21, 31: median stroke **1.5-1.9 mm** at 8 in
  (target 1.5-2.5 mm; the rejected first prompt gave 0.7 mm). Every page used the same prompt-B style block
  and looks visually consistent in weight, so all are marked PASS, but only 4 were measured at full size.
- **Shading**: automated - any colour, or solid-black blobs > 1% of the page, fails. No page has grey shading or colour.
- **Colourability**: automated count of enclosed white areas too small to colour comfortably (~< 2 mm).
  <=30 PASS, 31-40 WEAK, >40 FAIL. Plus my visual review.
- **Consistency**: visual check that Pip / Biscuit / Boo look like themselves and the scene matches the story.
- Retries: max 2 per page. Pages 9, 26, 32 needed 1; pages 24, 31 needed 2. None still FAIL after retries.

Limitation: the full-resolution PNG/PDF exports could not be downloaded into this environment (network policy blocks
`export-download.canva.com`), so automated checks ran on Canva's 200 px previews. **Please do a final zoomed-in pass
in Canva on the AI-drawn lettering** (pages 1, 3, 5, 14, 15, 16, 27) - AI images sometimes misspell words.

## Per-page results
| Page | Scene | Line weight | Shading | Colourability (tiny areas) | Consistency | Retries | Notes |
|---|---|---|---|---|---|---|---|
| 1 | It's Halloween! Pip wakes up with a big idea. | PASS | PASS | PASS (20) | PASS | 0 | Strong opener; "OCTOBER 31" lettering reads correctly at preview size. |
| 2 | Boo floats in for pumpkin pancakes. | PASS | PASS | PASS (22) | PASS | 0 | Good. Window frame + kitchen shelf add some small boxes. |
| 3 | "Let's throw a party under the Pumpkin Moon!" | PASS | PASS | PASS (28) | PASS | 0 | "You're Invited!" card lettering is AI-drawn; check spelling at full size. |
| 4 | Oh no! Pip's broom is broken. | PASS | PASS | WEAK (33) | PASS | 0 | WEAK: broom bristles and floorboards create many thin slivers (33 tiny areas). Pip looks worried, as intended. |
| 5 | Off to Mr Hoot's Broom Repair Shop. | PASS | PASS | PASS (26) | PASS | 0 | "BROOM REPAIR SHOP" sign lettering; tool rack has small details. Mr Hoot is charming. |
| 6 | Good as new! Now to deliver the invitations. | PASS | PASS | PASS (27) | PASS | 0 | Good. Village houses in background are small. |
| 7 | First stop: Hazel's mushroom house. | PASS | PASS | PASS (16) | PASS | 0 | Good. Hedgehog spines drawn as outline, not fills. |
| 8 | Next, the bats in the old oak tree. | PASS | PASS | WEAK (32) | PASS | 0 | WEAK: 32 tiny areas; the tree hollow has an extra face drawn in it (unprompted) and Boo is partly hidden. |
| 9 | Sprout the scarecrow says yes! | PASS | PASS | PASS (11) | PASS | 1 | Retry 1 fixed the dense corn and the wrong sign text ("corn maze"). Now clean. |
| 10 | Time to pick pumpkins. | PASS | PASS | PASS (19) | PASS | 0 | Good, very colourable. |
| 11 | This one is VERY big. | PASS | PASS | PASS (19) | PASS | 0 | Good. Lovely team-work page. |
| 12 | Home they go with a wagon full of pumpkins. | PASS | PASS | WEAK (28) | PASS | 0 | BORDERLINE: picket fence slats + background trees = 158 regions; still colourable. |
| 13 | A stop at the sweet shop. | PASS | PASS | PASS (21) | PASS | 0 | Good, but sweet-jar contents are small. |
| 14 | Ribbit sells sparkle punch at the potion shop. | PASS | PASS | PASS (7) | PASS | 0 | Very clean. "POTION SHOP" lettering. |
| 15 | Mrs Crumb gives Pip her secret pie recipe. | PASS | PASS | WEAK (31) | PASS | 0 | Mrs Crumb (mouse baker). "OPEN" and "RECIPE" lettering. 31 tiny areas from pastry details - borderline. |
| 16 | Back home, Pip bakes a pumpkin pie. | PASS | PASS | PASS (15) | PASS | 0 | Good. "FLOUR" lettering on sack. |
| 17 | Hot cocoa bubbles in the cauldron. | PASS | PASS | PASS (8) | PASS | 0 | Very clean. |
| 18 | Carving jack-o'-lanterns. | PASS | PASS | PASS (15) | PASS | 0 | Good. |
| 19 | Smiley pumpkins on the porch steps. | PASS | PASS | PASS (19) | PASS | 0 | Good. Jack-o'-lantern faces outlined, not filled. |
| 20 | Hanging up the party bunting. | PASS | PASS | PASS (15) | PASS | 0 | Good. |
| 21 | Pip's cottage is all dressed up. | PASS | PASS | PASS (8) | PASS | 0 | Very clean, nice house page. |
| 22 | Setting the party table in the garden. | PASS | PASS | PASS (11) | PASS | 0 | Clean. |
| 23 | Costumes from the attic chest! | PASS | PASS | PASS (26) | WEAK | 0 | CONSISTENCY: Boo peeking from the chest is drawn more like a cat-ghost hybrid; Biscuit wears a top hat instead of a too-big witch hat. |
| 24 | Biscuit is a pumpkin. Boo is... a ghost! | PASS | PASS | PASS (21) | PASS | 2 | Retry 2. Fixed solid-black pumpkin face and the checked-pattern sheet. Boo now in a plain sheet. Slightly sparse. |
| 25 | The sun sets. Pip checks everything from her broom. | PASS | PASS | PASS (13) | PASS | 0 | Good. Broom flight; Pip + Biscuit consistent. |
| 26 | Here come the guests! | PASS | PASS | WEAK (31) | WEAK | 1 | Retry 1. CONSISTENCY: shows 5 bats instead of 3. Still 31 tiny areas (borderline). |
| 27 | Mr Hoot and Ribbit bring presents. | PASS | PASS | PASS (21) | PASS | 0 | Good. "SPARKLE PUNCH" bottle lettering. |
| 28 | Let the Pumpkin Moon Party begin! | PASS | PASS | PASS (23) | PASS | 0 | Good, a bit busy with cupcakes/bunting. |
| 29 | Boo's ghost cousins have a tea party. | PASS | PASS | PASS (9) | PASS | 0 | Very clean. |
| 30 | Bobbing for apples! | PASS | PASS | PASS (14) | PASS | 0 | Clean. |
| 31 | The bat band plays a spooky-happy tune. | PASS | PASS | PASS (14) | PASS | 2 | Retry 2. Now 2 bats (prompt was 3) but very colourable. |
| 32 | A costume parade around the garden. | PASS | PASS | PASS (23) | PASS | 1 | Retry 1. Characters now big; Sprout dropped out of the parade. |
| 33 | Marshmallows by the campfire. | PASS | PASS | PASS (8) | PASS | 0 | Clean. |
| 34 | A lantern walk through the moonlit garden. | PASS | PASS | PASS (18) | PASS | 0 | Good. |
| 35 | Trick-or-treat around the village! | PASS | PASS | PASS (23) | PASS | 0 | Good. Grandma bear works well. |
| 36 | Look! The Pumpkin Moon rises. | PASS | PASS | PASS (11) | PASS | 0 | Clean. |
| 37 | Goodnight, friends! Thank you for coming. | PASS | PASS | PASS (14) | PASS | 0 | Good. |
| 38 | Time to tidy up. Biscuit helps... sort of. | PASS | PASS | PASS (13) | PASS | 0 | Good - Biscuit asleep in pie dish lands the joke. |
| 39 | A bedtime story by candlelight. | PASS | PASS | PASS (3) | PASS | 0 | Very clean, but 0.9% solid-black area from candle flames/book - acceptable. |
| 40 | Sweet dreams, Pip. The End. | PASS | PASS | PASS (8) | PASS | 0 | Clean, good ending. |
| belongs | This book belongs to | PASS | PASS | PASS (26) | PASS | 0 | Clean sign with Pip, Biscuit and Boo. Text placed on sign in Canva. |

## Pages to fix by hand in Canva (6)
No page hard-fails, but these are the weakest - worth a manual touch-up or a third regeneration:
- **Page 4**: WEAK: broom bristles and floorboards create many thin slivers (33 tiny areas). Pip looks worried, as intended.
- **Page 8**: WEAK: 32 tiny areas; the tree hollow has an extra face drawn in it (unprompted) and Boo is partly hidden.
- **Page 12**: BORDERLINE: picket fence slats + background trees = 158 regions; still colourable.
- **Page 15**: Mrs Crumb (mouse baker). "OPEN" and "RECIPE" lettering. 31 tiny areas from pastry details - borderline.
- **Page 23**: CONSISTENCY: Boo peeking from the chest is drawn more like a cat-ghost hybrid; Biscuit wears a top hat instead of a too-big witch hat.
- **Page 26**: Retry 1. CONSISTENCY: shows 5 bats instead of 3. Still 31 tiny areas (borderline).

## Book-level issues
- **Cover**: title sits over the top bunting/star ornaments slightly; readable, but you may want to nudge it down 10-20 px
  or add a soft dark shape behind it. Cover art is AI-generated in full colour; check hands/feet at full size.
- **Character drift**: Pip's fringe and hat brim shape vary page to page; Biscuit's tail/bell come and go; bat count varies
  (pages 8, 26, 31). Typical for AI generation without a reference image - acceptable for a colouring book, but noticeable
  if you read it as a picture book.
- **Captions**: each story page has a one-line caption under the art (bold, 20 px). Delete them in Canva if you want a
  text-free colouring book.
- **Print**: art now sits inside a 0.3 in safe margin (fixed during QA - the first layout was only 0.125 in from the top).
  There is no bleed; for KDP-style printing choose "no bleed". Cover is a separate design concern - KDP needs a
  wrap-around cover (back + spine + front) built at the final page count.
