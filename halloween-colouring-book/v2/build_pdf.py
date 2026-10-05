"""Build the 20-page 8x8in professional edition PDF locally from the Canva artwork previews."""
import csv, sys
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
sys.path.insert(0, '.'); import story_v2 as s

T = '/root/.claude/projects/-home-user-Firmware/84cd95be-f03b-50b5-becb-ac67dfad7b4b/tool-results/'
D = '/usr/share/fonts/truetype/dejavu/'
L = '/usr/share/fonts/truetype/liberation/LiberationSans-'
pdfmetrics.registerFont(TTFont('Sans', L + 'Regular.ttf'))
pdfmetrics.registerFont(TTFont('Sans-Bold', L + 'Bold.ttf'))
pdfmetrics.registerFont(TTFont('Sans-BoldOblique', L + 'BoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('Sans-Oblique', L + 'Italic.ttf'))
pdfmetrics.registerFont(TTFont('Stars', D + 'DejaVuSans-Bold.ttf'))  # has the star glyph

PLUM, ORANGE, CREAM, PEACH, GOLD = map(HexColor, ['#4A2D5E', '#F08A24', '#FFF1D6', '#FFF6E8', '#FFB65C'])
S = 576.0 / 768  # Canva px -> pt (8in page = 576pt)

final = {p: f for p, m, f in csv.reader(open('../build/final.tsv'), delimiter='\t')}
COLOUR = dict(zip(range(1, 17), [
 'mcp-Canva-blob-1791227981439-u9zkbw.jpg', 'mcp-Canva-blob-1791227987448-try9hb.jpg', 'mcp-Canva-blob-1791227993081-r22ddh.jpg',
 'mcp-Canva-blob-1791227999416-kbb3e2.jpg', 'mcp-Canva-blob-1791228004677-lgched.jpg', 'mcp-Canva-blob-1791228010395-j94b80.jpg',
 'mcp-Canva-blob-1791228017444-74hcum.jpg', 'mcp-Canva-blob-1791228023696-gu41ee.jpg', 'mcp-Canva-blob-1791228035182-q7nhyu.jpg',
 'mcp-Canva-blob-1791228042192-m7m7yq.jpg', 'mcp-Canva-blob-1791228047921-dgy64q.jpg', 'mcp-Canva-blob-1791228053647-iqdro3.jpg',
 'mcp-Canva-blob-1791228060986-mkxqej.jpg', 'mcp-Canva-blob-1791228066878-jzxqnr.jpg', 'mcp-Canva-blob-1791228073117-qimd2z.jpg',
 'mcp-Canva-blob-1791228080519-orfcl7.jpg']))
FRONT = 'mcp-Canva-blob-1791228166308-qb6bj7.png'   # styled front cover render (600px)
BACK = 'mcp-Canva-blob-1791228086581-8zfq9j.jpg'    # back cover art
BELONGS = final['belongs']

def lineart(fname, px=1600):
    """Upscale a low-res line-art preview and re-threshold it to crisp pure black/white."""
    im = Image.open(T + fname).convert('L').resize((px, px), Image.LANCZOS).filter(ImageFilter.GaussianBlur(px / 530))
    a = np.asarray(im)
    return ImageReader(Image.fromarray(np.where(a < 150, 0, 255).astype('uint8')).convert('1'))

def colour(fname, px=600, sharpen=True):
    im = Image.open(T + fname).convert('RGB').resize((px, px), Image.LANCZOS)
    if sharpen: im = im.filter(ImageFilter.UnsharpMask(2, 80, 2))
    import io; b = io.BytesIO(); im.save(b, 'JPEG', quality=90); b.seek(0)
    return ImageReader(b)

def box(c, x, y, w, h):  # Canva top-left px -> reportlab bottom-left pt
    return x * S, 576 - (y + h) * S, w * S, h * S

def img(c, ir, x, y, w, h):
    c.drawImage(ir, *box(c, x, y, w, h))

def para(c, text, x, y, w, size, font='Sans-Bold', color=PLUM, align=TA_LEFT, lead=1.3):
    p = Paragraph(text, ParagraphStyle('p', fontName=font, fontSize=size * S, leading=size * S * lead, textColor=color, alignment=align))
    _, h = p.wrap(w * S, 1000)
    p.drawOn(c, x * S, 576 - y * S - h)
    return h / S

def rrect(c, x, y, w, h, r, fill, stroke=None, sw=0):
    c.setFillColor(fill)
    if stroke: c.setStrokeColor(stroke); c.setLineWidth(sw * S)
    c.roundRect(*box(c, x, y, w, h), r * S, stroke=1 if stroke else 0, fill=1)

c = canvas.Canvas('../export/cozy-spooky-corner-print.pdf', pagesize=(576, 576), initialFontName='Sans', initialFontSize=10)
c.setTitle("Cozy Spooky Corner - Pip's Pumpkin Moon Party"); c.setAuthor('Cozy Spooky Corner'); c.setSubject('Halloween story colouring book, ages 3+')

# 1 front cover
img(c, colour(FRONT, 1600, sharpen=True), 0, 0, 768, 768); c.showPage()

# 2 belongs-to
img(c, lineart(BELONGS, 2000), 32, 32, 704, 704)
para(c, 'This book belongs to', 166, 410, 480, 40, align=TA_CENTER, lead=1.1)
c.setStrokeColor(PLUM); c.setLineWidth(2.5 * S); c.line(196 * S, 576 - 528 * S, 616 * S, 576 - 528 * S)
c.showPage()

# 3 colour test page
para(c, 'Test Your Colours Here!', 40, 48, 688, 44, align=TA_CENTER)
para(c, 'Try your pencils, pens and crayons in the circles before you start colouring.', 84, 112, 600, 18, font='Sans-Oblique', align=TA_CENTER)
c.setStrokeColor(black); c.setFillColor(white); c.setLineWidth(4 * S)
for t in (180, 340, 500):
    for l in (84, 244, 404, 564):
        c.circle((l + 60) * S, 576 - (t + 60) * S, 58 * S, stroke=1, fill=1)
para(c, "Tip: slip a spare sheet of paper behind the page you are colouring so markers don't bleed through.", 84, 664, 600, 18, font='Sans-Oblique', align=TA_CENTER)
c.showPage()

# 4-19 story pages
for n, (src, text) in enumerate(s.PAGES, 1):
    para(c, text, 40, 44, 510, 24, lead=1.35)
    rrect(c, 574, 24, 160, 160, 14, PEACH, ORANGE, 4)
    img(c, colour(COLOUR[n]), 584, 34, 140, 140)
    para(c, 'Colour idea', 574, 190, 160, 15, font='Sans-BoldOblique', color=ORANGE, align=TA_CENTER)
    img(c, lineart(final[str(src)]), 122, 212, 524, 524)
    c.showPage()

# 20 back cover (KDP): art mirrored so Pip + moon sit bottom-left; 2 x 1.2 in barcode zone bottom-right kept clear
def mirrored(fname, px=1600):
    im = Image.open(T + fname).convert('RGB').resize((px, px), Image.LANCZOS).transpose(Image.FLIP_LEFT_RIGHT)
    import io; b = io.BytesIO(); im.save(b, 'JPEG', quality=90); b.seek(0)
    return ImageReader(b)
img(c, mirrored(BACK), 0, 0, 768, 768)
para(c, 'Cozy Spooky Corner', 40, 40, 688, 46, color=CREAM, align=TA_CENTER, lead=1.1)
para(c, "Pip's Pumpkin Moon Party", 40, 104, 688, 26, color=GOLD, align=TA_CENTER)
para(c, "Join Pip the little witch, Biscuit the cat and Boo the friendly ghost as they plan the cosiest "
        "Halloween party ever. Pick pumpkins, bake a pie, carve jack-o'-lanterns and dance under the "
        "Pumpkin Moon, colouring every step of the story as you go!", 64, 150, 640, 18, font='Sans', color=CREAM, align=TA_CENTER, lead=1.45)
for l, n in [(372, 7), (496, 10), (620, 13)]:
    rrect(c, l, 290, 116, 116, 12, PEACH, ORANGE, 4)
    img(c, colour(COLOUR[n], 400), l + 8, 298, 100, 100)
para(c, '★ 16 story pages to colour<br/>★ Bold, easy lines for little hands<br/>★ A colour idea on every page<br/>★ Colour test page included<br/>★ Ages 3+',
     402, 432, 330, 16, font='Stars', color=CREAM, lead=1.55)
# KDP barcode zone (bottom-right, 2 x 1.2 in, 0.25 in in from the edges) is intentionally left empty.
c.showPage()
c.save()
print('ok')
