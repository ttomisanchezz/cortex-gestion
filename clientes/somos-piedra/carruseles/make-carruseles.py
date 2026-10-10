"""Carruseles Somos Piedra — 1080x1080, franja oscura arriba, logo chico, etiqueta de precio vacía."""
import sys, os, zipfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

S = 1080
SRC = 'src'
OUT = 'out'
F_BIG = '/usr/share/fonts/opentype/inter/InterDisplay-Black.otf'
F_SMALL = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
GREEN = (141, 190, 64)      # verde del logo
INK = (24, 22, 18)
CIERRE = 'Belgrano 3090 · WhatsApp 299 459-0936 · 4,4 ★ en Google'

LOGO = None
def logo():
    global LOGO
    if LOGO is None:
        im = Image.open('cat/c-001.jpg').convert('RGB')      # logo del catálogo (243x174)
        im = im.crop((10, 30, 233, 140))                       # piedrita + "SOMOS PIEDRA" + bajada
        w = 190
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        m = Image.new('L', im.size, 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), 14, fill=255)
        LOGO = (im, m)
    return LOGO

def square(name, fy=0.5, fx=0.5, zoom=1.0):
    im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, name))).convert('RGB')
    w, h = im.size
    side = int(min(w, h) / zoom)
    x = int((w - side) * fx); y = int((h - side) * fy)
    return im.crop((x, y, x + side, y + side)).resize((S, S), Image.LANCZOS)

def wrap(draw, text, font, maxw):
    words, lines, cur = text.split(' '), [], ''
    for wd in words:
        t = (cur + ' ' + wd).strip()
        if draw.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = wd
    lines.append(cur)
    return lines

def card(bg, big, small=None, price=None, out=None):
    img = bg.convert('RGBA')
    ov = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    pad = 56
    lg, lm = logo()
    textw = S - 2 * pad - lg.width - 32
    size = 84
    while True:
        fb = ImageFont.truetype(F_BIG, size)
        lines = wrap(d, big, fb, textw)
        if len(lines) <= 3 or size <= 60: break
        size -= 4
    fs = ImageFont.truetype(F_SMALL, 38)
    slines = wrap(d, small, fs, textw) if small else []
    lh = int(size * 1.08); sh = 48
    h = pad + len(lines) * lh + (16 + len(slines) * sh if slines else 0) + pad - 10
    h = max(h, lg.height + 2 * 40)
    d.rectangle((0, 0, S, h), fill=(16, 14, 11, 168))
    y = pad - 6
    for ln in lines:
        d.text((pad, y), ln, font=fb, fill=(255, 255, 255, 255)); y += lh
    if slines:
        y += 16
        for ln in slines:
            d.text((pad, y), ln, font=fs, fill=(232, 226, 214, 255)); y += sh
    img = Image.alpha_composite(img, ov)
    img.paste(lg, (S - pad - lg.width, (h - lg.height) // 2 if h < 260 else pad - 6), lm)
    if price:
        d2 = ImageDraw.Draw(img)
        fp = ImageFont.truetype(F_BIG, 50)
        tw = d2.textlength(price, font=fp)
        x0, y0 = pad, h + 28
        d2.rounded_rectangle((x0, y0, x0 + tw + 56, y0 + 84), 18, fill=GREEN)
        d2.text((x0 + 28, y0 + 13), price, font=fp, fill=INK)
    img.convert('RGB').save(out, quality=92)

def dims(bg, box=(150, 930, 390, 950)):
    """Cotas dibujadas sobre la foto: 4 m de largo y 3 m de alto."""
    im = bg.copy(); d = ImageDraw.Draw(im)
    f = ImageFont.truetype(F_BIG, 54)
    x0, x1, y0, y1 = box
    d.rectangle((x0, y0, x1, y1), outline=(255, 255, 255), width=5)
    def arrow(a, b, horiz):
        d.line((a, b), fill=GREEN, width=9)
        (ax, ay), (bx, by) = a, b
        k = 26
        if horiz:
            d.polygon([(ax, ay), (ax + k, ay - k * .7), (ax + k, ay + k * .7)], fill=GREEN)
            d.polygon([(bx, by), (bx - k, by - k * .7), (bx - k, by + k * .7)], fill=GREEN)
        else:
            d.polygon([(ax, ay), (ax - k * .7, ay + k), (ax + k * .7, ay + k)], fill=GREEN)
            d.polygon([(bx, by), (bx - k * .7, by - k), (bx + k * .7, by - k)], fill=GREEN)
    arrow((x0, y1 + 50), (x1, y1 + 50), True)
    arrow((x1 + 55, y0), (x1 + 55, y1), False)
    def tag(cx, cy, t):
        w = d.textlength(t, font=f)
        d.rounded_rectangle((cx - w / 2 - 18, cy - 40, cx + w / 2 + 18, cy + 40), 14, fill=INK)
        d.text((cx - w / 2, cy - 33), t, font=f, fill=(255, 255, 255))
    tag((x0 + x1) / 2, y1 + 50, '4 m')
    tag(x1 + 55, (y0 + y1) / 2, '3 m')
    return im

def grid(names, gap=8):
    im = Image.new('RGB', (S, S), INK)
    half = (S - gap) // 2
    for i, n in enumerate(names):
        t = square(n).resize((half, half), Image.LANCZOS)
        im.paste(t, ((i % 2) * (half + gap), (i // 2) * (half + gap)))
    return im

def strip(names, gap=8):
    im = Image.new('RGB', (S, S), INK)
    w = (S - gap * (len(names) - 1)) // len(names)
    for i, n in enumerate(names):
        src = ImageOps.exif_transpose(Image.open(os.path.join(SRC, n))).convert('RGB')
        sc = S / src.height
        src = src.resize((round(src.width * sc), S), Image.LANCZOS)
        x = (src.width - w) // 2
        im.paste(src.crop((x, 0, x + w, S)), (i * (w + gap), 0))
    return im

def crop_box(name, box):
    im = Image.open(os.path.join(SRC, name)).convert('RGB').crop(box)
    s = min(im.size); x = (im.width - s) // 2; y = (im.height - s) // 2
    return im.crop((x, y, x + s, y + s)).resize((S, S), Image.LANCZOS)

# ---------------- carruseles ----------------
NB = '\u00a0'
def inset(bg, name, fy=0.5):
    """Foto chica de la pieza en la mano (IG/FB) abajo a la derecha, sobre la foto colocada."""
    im = bg.copy()
    t = square(name, fy=fy).resize((300, 300), Image.LANCZOS)
    m = Image.new('L', t.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, 299, 299), 22, fill=255)
    fr = Image.new('RGB', (312, 312), (255, 255, 255)); fm = Image.new('L', fr.size, 0)
    ImageDraw.Draw(fm).rounded_rectangle((0, 0, 311, 311), 27, fill=255)
    x, y = S - 56 - 312, S - 150 - 312          # deja libre la franja de abajo
    im.paste(fr, (x, y), fm); im.paste(t, (x + 6, y + 6), m)
    return im

def plain(name, blur=16, dark=0.55):
    im = square(name).filter(ImageFilter.GaussianBlur(blur))
    return Image.blend(im, Image.new('RGB', (S, S), INK), 1 - dark)

DIMBOX = tuple(map(int, os.environ.get('DIMBOX', '195,850,300,960').split(',')))
def c1():
    hero = square('all-003.jpg', fy=0.55)          # frente de piedra Bariloche (catálogo)
    return [
        (hero, '¿Cuánto sale revestir tu frente?', 'Te lo calculamos por WhatsApp', None),
        (dims(hero, DIMBOX), 'Medí largo × alto', '4 m × 3 m = 12 m²', None),
        (square('fb-ocre-canto.jpg', fy=0.6), 'Sumá 10% por los cortes', '12 m² → 13,2 m²', None),
        (strip(['all-033.jpg', 'all-038.jpg', 'all-035.jpg']), 'Elegí la piedra', 'Ocre · Verde bronce · Zapala', None),
        (square('all-044.jpg', fy=0.75), 'Te lo llevamos a tu obra', 'A granel en camioneta o paletizado en camión', None),
        (square('all-027.jpg', fy=0.45), 'Mandanos las medidas', 'Precio en el día · WhatsApp 299' + NB + '459-0936 · Belgrano 3090', 'Consultá precio'),
    ]

def c2():
    return [
        (square('porfido_1.jpg'), '¿Piedra o símil?', 'La diferencia se toca', None),
        (square('all-044.jpg', fy=0.75), 'Piedra de la Patagonia', 'Adoquín de pórfido', None),
        (square('all-027.jpg', fy=0.45), 'Hecha para estar afuera', 'Sol, viento y heladas', None),
        (square('all-010.jpg', fy=0.5), 'Ninguna pieza es igual', 'Verde bronce irregular', None),
        (square('fb-portada.jpg', fx=0.55), 'Vení a verla y tocarla', 'Belgrano 3090 · Stock permanente · WhatsApp 299' + NB + '459-0936', 'Consultá precio'),
    ]

def c3():
    return [
        (grid(['all-033.jpg', 'all-038.jpg', 'all-017.jpg', 'all-029.jpg']), '¿Qué piedra va con tu casa?', 'Deslizá →', None),
        (inset(square('all-003.jpg', fy=0.55), 'ocre_1.jpg', fy=0.6), 'Ocre (Bariloche)', 'Cálida · frentes y quinchos', 'Consultá precio'),
        (inset(square('all-027.jpg', fy=0.45), 'fb-verde-bronce-mano.jpg', fy=0.6), 'Verde bronce', 'Moderna · muros y paredes', 'Consultá precio'),
        (square('all-017.jpg'), 'Pizarra negra', 'Sobria · living, hogares y quinchos', 'Consultá precio'),
        (square('all-029.jpg', fy=0.6), 'Travertino', 'El clásico · pisos y bordes de pileta', 'Consultá precio'),
        (inset(square('all-044.jpg', fy=0.75), 'porfido_1.jpg', fy=0.6), 'Pórfido patagónico', 'Patios, veredas y accesos', 'Consultá precio'),
        (square('all-035.jpg', fy=0.5), '¿Dudás entre dos?', 'Mandanos una foto de tu casa · WhatsApp 299' + NB + '459-0936', None),
    ]

def c5():
    gris = square('granza-gris_2.jpg').filter(ImageFilter.GaussianBlur(14))
    return [
        (square('all-039.jpg', fy=0.6), 'Tu jardín listo en un finde', 'Granza y piedra decorativa', None),
        (square('all-040.jpg', fy=0.6), 'Primero, tela antimaleza', 'Chau yuyos', None),
        (strip(['all-020.jpg', 'all-021.jpg', 'granza-olavarria_2.jpg']), 'Elegí el color', 'Blanca · gris · Olavarría', None),
        (gris, '¿Cuánto necesito?', 'Bolsa de __ kg = __ m²', None),
        (square('granza-olavarria_1.jpg', fy=0.7), 'Te la llevamos', 'Bolsones o a granel en camioneta · Alto' + NB + 'Valle', None),
        (square('fb-portada.jpg', fx=0.55), 'Pedila por WhatsApp', 'Precio en el día · WhatsApp 299' + NB + '459-0936 · Belgrano 3090', 'Consultá precio'),
    ]

SPECIAL = {}

NAMES = {'c1': ('carrusel-1-frente', c1), 'c2': ('carrusel-2-piedra-o-simil', c2),
         'c3': ('carrusel-3-estilo', c3), 'c5': ('carrusel-5-granza', c5)}

if __name__ == '__main__':
    for key in sys.argv[1:]:
        folder, fn = NAMES[key]
        od = os.path.join(OUT, folder); os.makedirs(od, exist_ok=True)
        paths = []
        for i, (bg, big, small, price) in enumerate(fn(), 1):
            if bg is None: bg = SPECIAL[(key, i)]()
            p = os.path.join(od, f'{i:02d}.jpg'); card(bg, big, small, price, p); paths.append(p)
        with zipfile.ZipFile(os.path.join(OUT, folder + '.zip'), 'w') as z:
            for p in paths: z.write(p, os.path.join(folder, os.path.basename(p)))
        # hoja de contacto para revisar
        th = 360; sheet = Image.new('RGB', (th * min(4, len(paths)), th * ((len(paths) + 3) // 4)), 'white')
        for i, p in enumerate(paths):
            sheet.paste(Image.open(p).resize((th, th)), ((i % 4) * th, (i // 4) * th))
        sheet.save(os.path.join(OUT, folder + '-hoja.jpg'), quality=85)
        print(folder, len(paths))
