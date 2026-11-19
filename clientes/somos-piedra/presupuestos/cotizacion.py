"""Genera la cotización en PDF de Somos Piedra.

Uso:  python cotizacion.py datos.json  [salida.pdf]

datos.json (ejemplo en ejemplo-0001-braidotti.json):
{
  "numero": "0001",
  "fecha": "2026-11-06",
  "cliente": {"nombre": "Santiago Braidotti", "cuit": "20-39128602-8"},
  "items": [{"cantidad": "42", "unidad": "m²", "descripcion": "Pórfido adoquín", "precio_unitario": 85000}],
  "leyenda_total": "PRECIO FINAL",   (opcional; si no está: SIN IVA / CON IVA según con_iva)
  "condiciones": ["Validez: 7 días desde la fecha.", "..."]
}
- precio_unitario en PESOS enteros (o "FALTA DATO"). El subtotal y el total los calcula el script en centavos.
- Sin nombre ni CUIT del cliente: el bloque CLIENTE no va (no se pregunta ni se completa).
- Si falta un precio, el PDF sale con FALTA DATO en rojo y sin total: no se manda así.
"""
import json, sys, os
from decimal import Decimal, ROUND_HALF_UP
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

AQUI = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(AQUI, "logo-somos-piedra.png")

# Quién emite (fijo; cambiar solo acá)
EMITE = {
    "titulo": "Somos Piedra",
    "lineas": ["Razón social: Franco Nicolás Muñoz", "CUIT 20-45734050-9", "Belgrano 3090, Neuquén Capital"],
    "firma": "Somos Piedra",
}
PIE = "Somos Piedra · Revestimientos naturales y vivero · Belgrano 3090, Neuquén Capital"

OSCURO = (0.180, 0.173, 0.157); GRIS = (0.420, 0.408, 0.384); VERDE = (0.498, 0.710, 0.224)
CLARO = (0.957, 0.949, 0.933); LINEA = (0.851, 0.839, 0.812); ROJO = (0.80, 0.10, 0.10); BLANCO = (1, 1, 1)
MESES = "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()
W, H = A4
FALTA = "FALTA DATO"


def pesos(centavos):
    p, c = divmod(centavos, 100)
    s = f"{p:,}".replace(",", ".")
    return f"${s},{c:02d}" if c else f"${s}"


def a_centavos(precio):
    if precio is None or precio == FALTA or precio == "":
        return None
    d = Decimal(str(precio))
    return int((d * 100).to_integral_value(ROUND_HALF_UP))


def generar(datos, salida):
    c = canvas.Canvas(salida, pagesize=A4)
    c.setTitle(f"Cotización {datos['numero']} - Somos Piedra")
    y = lambda top, size: H - top - size * 0.78  # top (desde arriba) -> línea de base

    def txt(x, top, s, size, font="Helvetica", color=OSCURO, align="l"):
        c.setFont(font, size); c.setFillColorRGB(*color)
        {"l": c.drawString, "r": c.drawRightString, "c": c.drawCentredString}[align](x, y(top, size), s)

    # Encabezado
    if os.path.exists(LOGO):
        c.drawImage(LOGO, 48, H - 48 - 92, width=200, height=92)
    txt(547, 53, "COTIZACIÓN", 22, "Helvetica-Bold", align="r")
    txt(547, 80, f"N° {datos['numero']}", 10, color=GRIS, align="r")
    f = date.fromisoformat(datos["fecha"])
    txt(547, 94, f"Neuquén, {f.day} de {MESES[f.month - 1]} de {f.year}", 10, color=GRIS, align="r")
    c.setFillColorRGB(*VERDE); c.rect(48, H - 151 - 3, 499, 3, stroke=0, fill=1)

    # Emite / Cliente
    txt(48, 175, "EMITE", 8.5, "Helvetica-Bold", VERDE)
    txt(48, 189, EMITE["titulo"], 10.5, "Helvetica-Bold")
    for i, l in enumerate(EMITE["lineas"]):
        txt(48, 204 + 14 * i, l, 9.5)
    cli = datos.get("cliente") or {}
    if cli.get("nombre") or cli.get("cuit"):  # sin nombre ni CUIT: no va el bloque CLIENTE
        txt(308, 175, "CLIENTE", 8.5, "Helvetica-Bold", VERDE)
        if cli.get("nombre"):
            txt(308, 189, cli["nombre"], 10.5, "Helvetica-Bold")
        else:
            txt(308, 189, f"CUIT {cli['cuit']}", 10.5, "Helvetica-Bold"); cli = {k: v for k, v in cli.items() if k != "cuit"}
    extra = [f"CUIT {cli['cuit']}"] if cli.get("cuit") else []
    extra += [l for l in (cli.get("direccion"), cli.get("telefono")) if l]
    for i, l in enumerate(extra):
        txt(308, 204 + 14 * i, l, 9.5)

    # Tabla
    top = 266
    c.setFillColorRGB(*OSCURO); c.rect(48, H - top - 24, 499, 24, stroke=0, fill=1)
    for x, t, a in ((56, "CANT.", "l"), (100, "UNIDAD", "l"), (156, "DESCRIPCIÓN", "l"), (438, "PRECIO UNIT.", "r"), (539, "SUBTOTAL", "r")):
        txt(x, top + 9, t, 8.5, "Helvetica-Bold", BLANCO, a)
    top += 24
    total, falta = 0, False
    for it in datos["items"]:
        unit = a_centavos(it.get("precio_unitario"))
        cant = Decimal(str(it["cantidad"]))
        txt(56, top + 14, str(it["cantidad"]).replace(".", ","), 10)
        txt(100, top + 14, it.get("unidad", ""), 10)
        txt(156, top + 14, it["descripcion"], 10)
        if unit is None:
            falta = True
            txt(438, top + 14, FALTA, 10, "Helvetica-Bold", ROJO, "r")
            txt(539, top + 14, FALTA, 10, "Helvetica-Bold", ROJO, "r")
        else:
            sub = int((cant * unit).to_integral_value(ROUND_HALF_UP))
            total += sub
            txt(438, top + 14, pesos(unit), 10, align="r")
            txt(539, top + 14, pesos(sub), 10, align="r")
        top += 40
        c.setStrokeColorRGB(*LINEA); c.setLineWidth(0.6); c.line(48, H - top, 547, H - top)

    # Total
    top += 6
    c.setFillColorRGB(*CLARO); c.rect(317, H - top - 38, 230, 38, stroke=0, fill=1)
    c.setFillColorRGB(*VERDE); c.rect(317, H - top - 38, 4, 38, stroke=0, fill=1)
    txt(333, top + 14, "TOTAL", 9, "Helvetica-Bold", GRIS)
    if falta:
        txt(539, top + 8, FALTA, 15, "Helvetica-Bold", ROJO, "r")
    else:
        txt(539, top + 6, pesos(total), 15, "Helvetica-Bold", align="r")
    txt(539, top + 24, datos.get("leyenda_total") or ("CON IVA" if datos.get("con_iva") else "SIN IVA"), 9, "Helvetica-Bold", VERDE, "r")
    top += 79

    # Condiciones
    txt(48, top, "CONDICIONES", 8.5, "Helvetica-Bold", VERDE)
    for i, l in enumerate(datos.get("condiciones", [])):
        txt(48, top + 15 + 14 * i, "•  " + l, 9.5)
    top += 15 + 14 * len(datos.get("condiciones", [])) + 26

    # Firma
    txt(48, top, "Saludos cordiales.", 10)
    c.setStrokeColorRGB(*OSCURO); c.setLineWidth(0.8); c.line(48, H - top - 30, 198, H - top - 30)
    txt(48, top + 34, EMITE["firma"], 10, "Helvetica-Bold")

    # Pie
    c.setFillColorRGB(*OSCURO); c.rect(0, 0, W, 30, stroke=0, fill=1)
    txt(W / 2, 824, PIE, 8.5, color=BLANCO, align="c")
    c.showPage(); c.save()
    return total, falta


if __name__ == "__main__":
    datos = json.load(open(sys.argv[1], encoding="utf-8"))
    nombre = ((datos.get("cliente") or {}).get("nombre") or "").split()
    sufijo = f"-{nombre[-1]}" if nombre else ""
    salida = sys.argv[2] if len(sys.argv) > 2 else os.path.join(AQUI, "salida", f"Cotizacion-{datos['numero']}{sufijo}.pdf")
    os.makedirs(os.path.dirname(salida), exist_ok=True)
    total, falta = generar(datos, salida)
    print(salida, "| TOTAL:", "FALTA DATO (no mandar)" if falta else pesos(total))
