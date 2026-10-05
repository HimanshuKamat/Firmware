"""Story beats and Canva prompts for 'Cozy Spooky Corner: Pip's Pumpkin Moon Party'."""
import json

STYLE = ("Simple bold colouring page for children. Very thick black marker outlines, all lines the same "
         "heavy weight, like drawn with a fat felt-tip pen. Pure white inside every shape. Strictly black "
         "lines on white only: no grey, no shading, no hatching, no texture, no patterns, no gradients, no "
         "colour, no solid black fills, no border frame. Few large rounded shapes with big open white spaces "
         "to colour, no tiny details, no small repeated objects. Cute chubby kawaii characters with simple "
         "happy faces. Full scene filling the whole square page.")

CHARS = {
    "pip": "Pip, a little girl witch with a round face, big happy eyes, a short bob haircut, an oversized "
           "floppy pointed witch hat with one star on it, a simple dress and striped stockings",
    "biscuit": "Biscuit, Pip's chubby round white cat with a bell collar",
    "boo": "Boo, a small round friendly ghost with a little bow on top of its head",
    "hoot": "Mr Hoot, a round owl wearing big goggles and an apron",
    "hazel": "Hazel, a chubby hedgehog in a scarf",
    "ribbit": "Ribbit, a round frog wearing a tiny bow tie",
    "bats": "three little round bats",
    "sprout": "Sprout, a friendly smiling scarecrow with a pumpkin-patch hat",
}

# (caption, characters, scene)
BEATS = [
 ("It's Halloween! Pip wakes up with a big idea.", "pip biscuit",
  "a cosy attic bedroom in the morning, Pip stretching in bed, Biscuit curled on the quilt, a wall calendar with October 31 circled, a round window with the sun rising"),
 ("Boo floats in for pumpkin pancakes.", "pip biscuit boo",
  "a cosy kitchen breakfast table with a stack of pumpkin pancakes, Pip and Biscuit at the table, Boo floating in through an open window waving"),
 ("\"Let's throw a party under the Pumpkin Moon!\"", "pip boo biscuit",
  "Pip at a little wooden desk writing big invitation cards with a feather quill, Boo holding an envelope, Biscuit sitting on the desk"),
 ("Oh no! Pip's broom is broken.", "pip biscuit",
  "in a cosy hallway, Pip holding a broom with a snapped handle and messy bristles, looking surprised, Biscuit peeking from behind her"),
 ("Off to Mr Hoot's Broom Repair Shop.", "pip boo hoot",
  "a small broom repair shop with brooms hanging on a wall rack, Mr Hoot at a workbench fixing Pip's broom with a big hammer, Pip and Boo watching, a sign shaped like a broom"),
 ("Good as new! Now to deliver the invitations.", "pip boo",
  "Pip holding her fixed broom and a satchel full of envelopes, Boo carrying one big envelope, a winding path leading into a village of round cottages"),
 ("First stop: Hazel's mushroom house.", "pip boo hazel",
  "a big round mushroom-shaped house with a round door, Hazel opening an invitation at the door, Pip and Boo waving, a small mailbox and a few large leaves"),
 ("Next, the bats in the old oak tree.", "pip boo bats",
  "a big friendly old oak tree with a round hollow, the three little bats hanging upside down from a branch holding an invitation, Pip and Boo looking up and smiling"),
 ("Sprout the scarecrow says yes!", "pip boo sprout",
  "a cornfield with a few tall corn stalks, Sprout the scarecrow waving and holding an invitation, Pip and Boo standing by a wooden fence, a big sun"),
 ("Time to pick pumpkins.", "pip biscuit boo",
  "a pumpkin patch with five big round pumpkins and curly vines, Pip hugging the biggest pumpkin, Biscuit sitting on a pumpkin, Boo floating above"),
 ("This one is VERY big.", "pip biscuit hazel sprout",
  "Pip, Hazel and Sprout pushing one giant round pumpkin up a gentle hill, Biscuit riding on top of the pumpkin"),
 ("Home they go with a wagon full of pumpkins.", "pip biscuit boo",
  "Pip pulling a wooden wagon full of round pumpkins along a country lane with a picket fence, Biscuit walking beside, Boo pushing the wagon from behind"),
 ("A stop at the sweet shop.", "pip boo",
  "a sweet shop counter with three giant candy jars, big lollipops and wrapped sweets, Pip pointing at a lollipop, Boo carrying a paper bag"),
 ("Ribbit sells sparkle punch at the potion shop.", "pip ribbit",
  "a little potion shop with a counter and a shelf of four big round bottles with star and heart labels, Ribbit behind the counter handing a big bottle to Pip"),
 ("Mrs Crumb gives Pip her secret pie recipe.", "pip biscuit",
  "a bakery with a round mouse baker in a chef hat handing Pip a recipe card, pumpkin pies on the counter, a big pumpkin-shaped open sign, Biscuit sniffing a pie"),
 ("Back home, Pip bakes a pumpkin pie.", "pip biscuit",
  "a cosy kitchen, Pip stirring a big mixing bowl, Biscuit covered in flour sitting in a flour sack, a rolling pin and a pie dish on the table, an oven"),
 ("Hot cocoa bubbles in the cauldron.", "pip boo",
  "a big round cauldron over a small fire with bubbling cocoa and big marshmallows floating, Pip stirring with a long spoon, Boo holding two mugs"),
 ("Carving jack-o'-lanterns.", "pip boo biscuit",
  "Pip and Boo at a kitchen table carving two big pumpkins with smiley faces, a bowl of pumpkin seeds, Biscuit batting a pumpkin stem"),
 ("Smiley pumpkins on the porch steps.", "pip biscuit",
  "the front porch of a cottage with wide wooden steps, five jack-o'-lanterns with different happy faces lined up on the steps, Pip placing the last one, Biscuit sitting on the top step"),
 ("Hanging up the party bunting.", "pip boo",
  "Pip standing on a small step ladder hanging bunting with bat and pumpkin flags across a garden, Boo holding the other end of the bunting"),
 ("Pip's cottage is all dressed up.", "pip boo biscuit",
  "a cute crooked cottage with a round window, a pointy roof, a moon-shaped door knocker, pumpkins by the door, bunting on the roof, Pip, Boo and Biscuit admiring it from the garden path"),
 ("Setting the party table in the garden.", "pip boo",
  "a long garden table with a tablecloth, round lanterns, plates and cups, Pip laying out plates, Boo carrying a big lantern, a tree with hanging lanterns"),
 ("Costumes from the attic chest!", "pip biscuit boo",
  "an attic with a big open wooden chest overflowing with costumes, Pip holding up a cape, Biscuit wearing a too-big hat, Boo peeking out of the chest"),
 ("Biscuit is a pumpkin. Boo is... a ghost!", "biscuit boo pip",
  "Biscuit wearing a round pumpkin costume and Boo wearing a funny bedsheet with two eye holes, Pip laughing and clapping"),
 ("The sun sets. Pip checks everything from her broom.", "pip biscuit",
  "Pip and Biscuit flying on the broom over the village rooftops, round cottages with pumpkins below, a big setting sun and two round clouds"),
 ("Here come the guests!", "pip hazel bats sprout",
  "a garden gate with a lantern on each post, Pip opening the gate, Hazel, the three bats and Sprout arriving with smiles"),
 ("Mr Hoot and Ribbit bring presents.", "pip hoot ribbit",
  "Mr Hoot carrying a round gift box with a bow and Ribbit carrying a big bottle of sparkle punch, Pip greeting them at the door"),
 ("Let the Pumpkin Moon Party begin!", "pip boo biscuit hazel",
  "the garden party table with the pumpkin pie, punch bowl and cupcakes, Pip, Boo, Biscuit and Hazel cheering and raising cups, bunting overhead"),
 ("Boo's ghost cousins have a tea party.", "boo",
  "Boo and two other round friendly ghosts sitting at a small round table with a teapot, teacups and cupcakes, a candelabra with three candles"),
 ("Bobbing for apples!", "pip hazel ribbit",
  "a big wooden tub of water with floating apples, Ribbit diving in happily, Pip and Hazel laughing beside the tub"),
 ("The bat band plays a spooky-happy tune.", "bats pip boo",
  "the three little bats playing a drum, a tiny guitar and a trumpet on a small stage of pumpkins, Pip and Boo dancing in front"),
 ("A costume parade around the garden.", "pip biscuit boo hazel sprout",
  "a line of friends marching in costumes along a garden path, Pip in a cape, Biscuit in the pumpkin costume, Boo in the bedsheet, Hazel with a crown, Sprout at the back"),
 ("Marshmallows by the campfire.", "pip boo hazel",
  "a small campfire ringed with round stones, Pip, Boo and Hazel sitting on logs toasting big marshmallows on sticks, a starry sky"),
 ("A lantern walk through the moonlit garden.", "pip biscuit boo",
  "Pip carrying a round lantern along a stone path through a garden with big mushrooms and tall flowers, Biscuit and Boo following, a few big fireflies drawn as stars"),
 ("Trick-or-treat around the village!", "pip boo biscuit",
  "Pip, Boo and Biscuit holding pumpkin buckets at the door of a round cottage, a smiling grandma bear giving sweets, jack-o'-lanterns on the doorstep"),
 ("Look! The Pumpkin Moon rises.", "pip biscuit boo hazel bats",
  "friends sitting on a big picnic blanket on a grassy hill looking up at a giant round full moon, Pip pointing, the bats flying across the moon"),
 ("Goodnight, friends! Thank you for coming.", "pip boo hazel sprout",
  "at the garden gate at night, Pip and Boo waving goodbye, Hazel and Sprout walking away down the path waving back, lanterns on the gate posts"),
 ("Time to tidy up. Biscuit helps... sort of.", "pip biscuit boo",
  "a kitchen sink with bubbles and a stack of plates, Pip washing up, Boo drying a cup, Biscuit asleep inside an empty pie dish"),
 ("A bedtime story by candlelight.", "pip biscuit boo",
  "a cosy reading nook with a big armchair and a blanket, Pip reading a big book, Biscuit on her lap, Boo yawning, three chunky candles on a side table"),
 ("Sweet dreams, Pip. The End.", "pip biscuit boo",
  "Pip asleep in her attic bed under a quilt, Biscuit and Boo snuggled at the end of the bed, a round window with a big smiling moon and two stars"),
]

def prompt(chars, scene):
    who = " ".join(CHARS[c] + "." for c in chars.split())
    return f"{STYLE} Characters: {who} Scene: {scene}."

BELONGS = (f"{STYLE} Characters: {CHARS['pip']}. {CHARS['biscuit']}. {CHARS['boo']}. Scene: Pip, Biscuit and Boo "
           "holding up one big blank wooden sign with nothing written on it, the sign takes up the middle of the page, "
           "two smiling pumpkins at the bottom corners.")
COVER = ("Cute cosy kawaii Halloween children's book cover illustration, full colour, soft warm palette of pumpkin "
         "orange, plum purple, cream, mint green and deep navy night sky. Bold clean outlines, rounded chubby shapes. "
         f"{CHARS['pip']}, sitting on a stack of big pumpkins in a cosy garden at night, hugging {CHARS['biscuit']}, with "
         f"{CHARS['boo']} floating beside her, bunting with bats and stars overhead, glowing lanterns, a huge orange "
         "full moon behind them. Leave a large empty area of plain night sky at the top for a title. No text, no letters.")

if __name__ == "__main__":
    out = [{"page": i + 1, "caption": c, "prompt": prompt(ch, s)} for i, (c, ch, s) in enumerate(BEATS)]
    out.append({"page": "belongs", "caption": "This book belongs to", "prompt": BELONGS})
    out.append({"page": "cover", "caption": "Cozy Spooky Corner", "prompt": COVER})
    json.dump(out, open("build/prompts.json", "w"), indent=1)
    print(len(BEATS), "beats")
