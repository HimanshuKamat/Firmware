# Canva MCP — hands-on test report

Run: 2026-10-05, 15:30–15:40 UTC (about 10 minutes of wall-clock for everything below).
Connection: claude.ai **Canva connector** (`mcp__Canva__*`). The repo-level `.mcp.json` entry
(`https://mcp.canva.com/mcp`) could not connect from the cloud container:
`canva (ERR_PROXY_TUNNEL): "Proxy refused to open a tunnel: 403 Forbidden"`.

Account: Canva's own `help` tool reports the account as **Canva Pro**. Two brand kits exist
(one unnamed, one "Rail and Beans"). Before the test there were no brand templates.

Everything created is in the Canva folder **Claude Test**: https://www.canva.com/folder/FAHXJwmiLKA
Nothing was deleted.

---

## 1. Discovery — tools available (41)

| Tool | What it does | Key params | Plan notes (tested) |
|---|---|---|---|
| `search-designs` | Find your designs | `query`, `sort_by`, `limit`, `ownership` | Works on Pro |
| `read-design` | Text, metadata, page thumbnails, presenter notes, full element tree | `design_id`, `filter.fields`, `open_transaction` | Works |
| `create-design` | AI-generate a design from a brief (async job) | `brief`, `format`, `outline` | Works. **Can't use a brand kit** |
| `get-create-design-async-job` | Poll `create-design` | `job_id`, `continuation_token` | — |
| `generate-design` (legacy) | AI-generate candidates; the only route that takes a brand kit | `query`, `design_type`, `brand_kit_id`, `asset_ids` | Works on Pro, brand kit included |
| `create-design-from-candidate` | Save a `generate-design` candidate | `job_id`, `candidate_id` | Works |
| `generate-design-structured`, `request-outline-review` | Presentation generation from an approved outline (legacy) | `topic`, `presentation_outlines` | Not tested (out of scope) |
| `generate-image`, `get-generate-image-job` | Text-to-image / image edit | `prompt`, `aspectRatio`, `imageReferences` | Not tested |
| `edit-design` | Transactional element edits: text, format, move, resize, recolor, shapes, autofill labels | `transaction_id`, `operations[]`, `finalize` | Works |
| `resize-design` | New copy at another size | `design_id`, `design_type` (custom w/h) | Works |
| `copy-design` | Duplicate a design or some pages | `design_id`, `page_numbers` | Works |
| `merge-designs` | Combine/reorder/delete pages | `type`, `operations[]` | Not tested (destructive) |
| `get-export-formats` | Which formats a design supports | `design_id` | Works (pdf/jpg/png/pptx/gif/mp4) |
| `export-design` | Export to a download URL | `design_id`, `format{type,width,height,pages,…}` | Works on Canva's side. **Download blocked here** (see below) |
| `import-design-from-url` | Turn a public PDF/MD/PPTX/DOCX/HTML into a design | `url`, `name`, `intended_design_type` | Works |
| `create-upload-url` | One-shot URL for uploading local file bytes | — | URL issued. **POST blocked here** |
| `upload-asset-from-url` | Import public image/video into your library | `url`, `name` | Not tested |
| `get-assets` | Image/video metadata | `asset_ids` | Not tested |
| `remove-background` | Background removal on an uploaded image | `sourceMedia` | Not tested (needs an upload) |
| `separate-image-layers` (+ job poll) | Flat PNG → editable layered design | `asset_id` | Not tested (needs an upload) |
| `list-brand-kits` | Your brand kits | — | **Works on Pro** (2 kits returned) |
| `search-brand-templates` | Find brand templates | `query`, `dataset` | Works (was empty) |
| `publish-brand-template` | Publish a design as a brand template | `design_id` | **Worked on Pro** |
| `create-brand-template-draft` | Editable draft of a brand template | `brand_template_id` | Not tested |
| `create-design-from-brand-template` | New design from a brand template | `brand_template_id` | Not tested |
| `get-brand-template-dataset` / `get-design-dataset` | List autofill fields | `template_id` / `design_id` | Works |
| `autofill-design` | Fill named fields → new design | `brand_template_id` or `design_id`, `data{}` | **Worked on Pro, both routes** |
| `create-folder`, `search-folders`, `list-folder-items`, `move-item-to-folder` | Folder management | `name`, `parent_folder_id`, `item_id`, `to_folder_id` | Works |
| `comment-on-design`, `list-comments`, `list-replies`, `reply-to-comment` | Comments | `design_id`, `message_plaintext` | Works (comment tested) |
| `resolve-shortlink` | `canva.link/…` → full URL | `shortlink_id` | Not tested |
| `help` | Canva Help Center answers | `prompt` | Works |

**About plan restrictions:** Canva's `help` tool said *"Filling Brand Templates with your own data
through that connector requires Canva Enterprise."* That didn't match what happened here. On
this Pro account, `publish-brand-template` and brand-template autofill both succeeded. Canva may
tighten this later, so don't build anything critical on it without re-testing.

---

## 2. Capability tests

| Step | Result | Time |
|---|---|---|
| Search 5 most recent | ✅ | ~2 s |
| Read content | ✅ | ~2 s |
| Generate ×2 styles | ✅ | ~45–60 s each (async, ran in parallel) |
| Resize → 1280×720 | ✅ technically, ❌ in quality | ~5 s |
| Export PNG + PDF | ✅ in Canva / ❌ download to `./canva-test` | ~3–5 s per export |
| Import (PDF + Markdown) | ❌ via upload / ✅ via public URL | ~4 s each |
| Brand kit | ✅ runs, ⚠️ poor result | ~10 s (synchronous) |
| Autofill | ✅ runs, ❌ layout breaks | ~10–15 s each |
| Folder, move, comment | ✅ | ~1–2 s each |

### Search: 5 most recent designs
1. **Neutral Minimalist Coffee Shop Instagram Carousel Post**: a 1-page 1080×1350 post for
   "Common Room Café" with mock reviewer quotes ("The perfect brew…").
2. **Beige and Pink Playful Affirmation Cards Carousel**: 5-page "pick a card" affirmation
   carousel (template placeholder handle `@reallygreatsite` still in it).
3. **Cosy Nursery Scene**: a 1-page image, no text.
4. **Day 2**: 62 pages, children's-story content ("For 300 years, Mr. Wolf has been the big bad guy…").
5. **Day 1**: 58 pages, parenting content ("Our kids are running a race they never signed up for").

### Read
`read-design` on the coffee-shop post returned all text in one flat string:
`"90 50 50 Kunal Desai Katie LawsonLaura Bennett Fueling the creative hustle…"`. Reading order
is unclear, and adjacent text boxes run together ("Katie LawsonLaura Bennett"). With
`open_transaction: true` you get a full element tree instead: every text box with position,
size, font size, colour, alignment and a font *reference ID*. That version is far more useful.

### Generate (2 styles)
- **A: "bold broadcast"** (navy/red, condensed type, ball + bat): **good**. Strong hierarchy, all
  three text lines present and correct. Could post as-is. Preview: `previews/varA-broadcast-thumb.png`.
- **B: "minimal heritage"** (cream/green/gold serif, line-art stumps): **good**, tasteful,
  correct text. Preview: `previews/varB-heritage-thumb.png`.
- Both came out **1080×1440 (3:4)**, not the classic 1080×1350 (4:5), even though the format
  was "Instagram Post (Portrait)". Fine for the current IG grid, but you can't choose.
- Variation A's stored text is "Adamstown Cc" (title-cased). It looks right only because the
  font is all-caps. Switch fonts and the error shows.

### Resize → YouTube thumbnail (1280×720)
Works mechanically, but the result is weak. Canva shrank the portrait layout into a centred
column with dark filler on both sides. Nothing was re-laid out for 16:9, and the text is small.
**Not usable as a thumbnail**. You'd generate a fresh `youtube_thumbnail` instead.
Preview: `previews/youtube-thumb-resized-thumb.png`.

### Export
Every `export-design` call succeeded and returned a signed URL (PNG for A, B, the thumbnail and
3 batch graphics; PDF for A, B and the thumbnail). **The files could not be saved into
`./canva-test`** because this cloud container's network policy blocks Canva's download host:

```
curl: (56) CONNECT tunnel failed, response 403
proxy log: export-download.canva.com:443 — connect_rejected (gateway answered 403 to CONNECT)
```

The export links expire after a few hours, so they're not listed here. To fix: allow
`export-download.canva.com` and `www.canva.com` in the environment's network settings (Edit
environment → Network access → Custom → Allowed domains), or run this on your own machine.
**Stand-ins:** `previews/*.png` are the 387–600 px renders that come back *inside* the MCP
responses. Good for review, **not** production resolution.

### Import
- **Local-file upload: failed.** `create-upload-url` returned a URL, but POSTing the bytes was
  blocked by the same egress policy:
  `curl: (56) CONNECT tunnel failed, response 403` (host `www.canva.com:443`).
- **Public URL import: worked.** I pushed `import-test.pdf` and `import-test.md` to this
  (public) GitHub repo and imported them from their raw URLs:
  - PDF → fixed 794×1123 design with editable text, faithful layout (`previews/imported-pdf.png`).
    One quirk: in the text read-back, the lines were joined without spaces.
  - Markdown → a Canva **Doc** with a real H1, bold line and bullet list (`previews/imported-markdown.png`).

### Brand kit
`generate-design` with `brand_kit_id = kAG8NgAiY4w` ("Rail and Beans") **succeeded**
(design `DAHXJwejQIk`), but the output is the worst of the test:
- It **dropped the two key facts**, "Live on YouTube" and "Saturday 2pm", and invented filler
  copy ("Don't miss this exciting local showdown!", "Tune in now!").
- The hero is an AI stadium photo with **garbled fake sponsor boards** and a player in yellow
  kit with no connection to Adamstown.
- The brand's green/yellow did show up. Note that "Rail and Beans" is a coffee brand, so this
  only tests the mechanics.
- Only **1 candidate** came back, so there was nothing to pick from.
Preview: `previews/brandkit-test-thumb.png`. Verdict: **draft only**, and the text must be checked.

### Autofill
No error anywhere. Exact sequence:
1. `get-design-dataset` on an existing design → `{}`: AI-generated designs have **no fields**.
2. Copied variation B, then labelled two text boxes via `edit-design`
   (`update_autofill_field`: `opponent`, `when`) and committed.
   `get-design-dataset` → `{"when":{"type":"text"},"opponent":{"type":"text"}}`.
3. `autofill-design` with `design_id` × 3 rows → 3 new designs (~15 s each).
4. `publish-brand-template` on the labelled copy → brand template `EAHXJ1yQ0Jc` ✅ (on Pro).
5. `autofill-design` with `brand_template_id` → new design ✅.

**The output quality is the problem, not access.** Text boxes keep their width and don't shrink:
- "Merewether CC" breaks mid-word as **"Mereweth / er CC"** and collides with the divider and
  "Live on YouTube" (`previews/autofill-merewether-cc.png`).
- "Hamilton-Wickham CC" wraps to three lines and **overprints** the date
  (`previews/autofill-hamilton-wickham-cc.png`).
- "Sat 17 Oct · 1:00 PM" wraps to two lines.
To fix this you'd have to hand-tune the template in Canva: wider boxes, smaller type and a
fixed line count. There's no auto-fit setting in the API. I left a comment on the
Hamilton-Wickham design explaining the overflow.

### Folders and comments
- `create-folder` → **Claude Test** (`FAHXJwmiLKA`).
- `move-item-to-folder` × 14, all succeeded; `list-folder-items` confirms them.
- `comment-on-design` on `DAHXJ1DJVO4` → thread `KAHXJ6HNabA` (posted under your account name).

---

## 3. Batch test: `fixtures.csv` → 3 match-day graphics

Method: one `create-design` call per row, with the **same style brief word for word**; only
the fixture text changed. All 3 ran in parallel and finished in about 50 s. Renamed
`Claude Test - Batch - <Opponent>`. PNG exports succeeded in Canva but couldn't be downloaded
(see Export). Previews are named by opponent:

- `previews/batch-bowral-cc.png`
- `previews/batch-merewether-cc.png`
- `previews/batch-hamilton-wickham-cc.png`

**Consistency: same mood, different designs.** Shown side by side, they read as three
different designers working from one brief:

| | Bowral | Merewether | Hamilton-Wickham |
|---|---|---|---|
| Palette | navy / red / white | navy / red / white | navy / red / white |
| Headline alignment | centred | centred | **left** |
| Headline font | condensed sans | condensed **italic** sans | different condensed sans, red "VS" |
| Info rows | icons + rules | `///` slashes in a red box | boxed icons |
| Ball position | right edge, cropped | centre | right-centre |
| Defects | ball overlaps "2026" | none obvious | stray `|` glyph after "2:30 PM", date row in a smaller size than the others |

All 7 facts were correct in all 3 (dates, times, venues, "Live on YouTube"). But for a
season's worth of fixtures that should look like one series, **AI generation is not
consistent enough**. The autofill route *is* consistent (identical layout by definition), but
it breaks on long names, as shown above.

---

## 4. Quality verdict

- **Single AI posts (variations A/B):** the best result here. Good-looking and close to
  postable, as long as you check the text yourself (e.g. "Adamstown Cc").
- **AI batch:** correct facts, inconsistent look. Fine for one-offs, not for a recognisable series.
- **Brand-kit generation:** draft only. It dropped required text and made up copy and imagery.
- **Resize:** not usable for 4:5 → 16:9.
- **Autofill:** consistent but fragile. Needs a hand-built template designed for your longest
  club name.
- **Imports:** clean and faithful.

## 5. How much control do you get?

| Lever | Control |
|---|---|
| Text content | **Full**: replace / find-replace any text box |
| Text position & size | **Full**: exact px `top/left/width` per element |
| Font size, weight, italic, colour, alignment, line height | **Full** via `format_text` |
| **Font family** | **None**: fonts are opaque IDs (`fontRef: "YAFcfq7XuZE,0"`). No operation sets a font |
| Colours of shapes | Recolour vector shapes; add shapes from SVG path data |
| **Decorative art** | Very little: frames, dividers, stumps and stripes come as **flat images** (`rect` with an image fill). You can move, crop or swap them, not restyle them |
| Layout of AI output | Only by describing it in the brief. You can't pin a grid or exact positions at generation time |
| Canvas size | Picked by Canva (asked for 4:5, got 3:4). Exact sizes only via `resize-design` (which just scales) or `add_page` |
| Text auto-fit | **None**: no shrink-to-fit, so autofill overflows |

Bottom line: you can steer and fine-tune the AI's output, but you can't specify a design
exactly. Exact control means editing elements one at a time, in pixels, through
`edit-design`, without being able to change fonts.

## 6. Timing (approximate)

| Step | Time |
|---|---|
| search / read / list / folder / move / comment | 1–3 s each |
| `create-design` (AI) | 45–60 s per design (async; parallel calls don't slow each other down) |
| `generate-design` + brand kit | ~10 s, returns 1 candidate; saving it takes another ~3 s |
| `resize-design` | ~5 s |
| `export-design` | 3–5 s each (synchronous) |
| `import-design-from-url` | ~4 s each |
| `autofill-design` | 10–15 s each |
| Whole test end-to-end | ~10 min, mostly AI generation and rendering |

## 7. Five workflows worth automating (given what actually worked)

1. **Weekly fixture graphic from a template.** Build one Canva template designed for your
   longest opponent name, label its fields, then for each row in your fixtures sheet call
   `autofill-design` → `export-design` (PNG) → file into a season folder. Consistent and fast
   (~15 s per graphic). The template design has to be done carefully by hand first.
2. **"Ideas board" for one-off posts.** For special matches (finals, presentation night),
   generate 3–4 `create-design` styles in parallel, file them into a folder, and comment on
   each with the brief used. A human picks one and tweaks it in Canva. This uses the AI for
   what it did best here.
3. **Results/scorecard updates on an existing post.** Open a transaction and swap only the
   score/result text with `find_and_replace_text`, then export. Same layout, new numbers.
   Better suited to `edit-design` than to new generation.
4. **Turn club documents into Canva.** Newsletters, AGM notices and committee reports as
   Markdown or PDF → `import-design-from-url` → Canva Doc, ready for someone to style. This
   worked cleanly, but the file needs a public URL (or local upload once the network allows it).
5. **Content audit and housekeeping.** Run `search-designs` / `read-design` across the account
   to list designs with leftover template text (e.g. `@reallygreatsite` in the affirmation
   carousel), then file them into folders and leave review comments. All read-only plus
   folder moves, low risk.

## 8. Where SVG/HTML generated in code beats Canva

- **Fixture series / anything data-driven.** A code template (SVG or HTML → PNG through a
  headless browser) gives pixel-identical layouts and real shrink-to-fit text, runs offline in
  milliseconds per graphic, and can be version-controlled. Canva's AI batch drifted in layout,
  and its autofill overflowed.
- **Exact sizes for each channel.** In code, 1080×1350, 1280×720 and 1500×500 are just
  parameters, each laid out properly. Canva's resize only scaled the design.
- **Fonts and brand colours.** In code you choose the exact font file and hex values. Through
  this API you can't set a font family at all.
- **Live data graphics** (scores, ladders, run-rate charts). Canva has nothing for this here;
  SVG/D3 does it natively.
- **No account, network or plan dependency.** No export URLs, upload hosts, proxy rules or
  plan limits. The generated file sits in the repo.

**Canva is better for** photo-rich, polished one-off looks (variations A/B were genuinely
nice), stock imagery and illustration, and handing the design to a non-technical volunteer to
tweak in the Canva editor.

---

## Files in this folder

| File | What it is |
|---|---|
| `fixtures.csv` | the 3 test fixtures |
| `import-test.md`, `import-test.pdf` | import test inputs |
| `previews/*.png` | low-res renders returned through MCP (stand-ins for the blocked exports) |
| `REPORT.md` | this report |

## Canva items created (all in "Claude Test")

| Design | ID |
|---|---|
| Variation A — broadcast | `DAHXJw3CKHM` |
| Variation B — heritage | `DAHXJ4m21v8` |
| Brand-kit test | `DAHXJwejQIk` |
| YouTube thumbnail (resized A) | `DAHXJwY8cXE` |
| Imported PDF | `DAHXJ7Z5wYs` |
| Imported Markdown | `DAHXJ7zrFEo` |
| Autofill template (labelled copy of B) | `DAHXJ_eykBg` |
| Autofill — Bowral / Merewether / Hamilton-Wickham | `DAHXJ2YXmRk` / `DAHXJxR-Yoc` / `DAHXJ1DJVO4` |
| Brand-template autofill — Bowral | `DAHXJxM4bqE` |
| Batch — Bowral / Merewether / Hamilton-Wickham | `DAHXJ3tB1xU` / `DAHXJ1PMhnY` / `DAHXJ90da4I` |

Also created outside that folder:
- **Brand template** `EAHXJ1yQ0Jc`, "Claude Test - Autofill template". It sits in your brand
  templates list, not the folder. Remove it if you don't want it there; I haven't deleted anything.
