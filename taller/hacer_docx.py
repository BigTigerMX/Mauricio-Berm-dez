# -*- coding: utf-8 -*-
"""Versiones editables del CV en Word (.docx), una por idioma.

Por qué Carlito y no Inter: Carlito es métricamente compatible con Calibri,
así que el documento se abre en el Word de cualquiera sin recolocarse. Un CV
editable que al abrirlo salta de página no sirve de nada. (Y, medido en esta
misma sesión, Carlito extrae su puntuación limpia: «+52», «(HA)» y
«EC-Council» salen enteros. Inter, sin desactivar `calt`, no.)

⚠ EL ANCHO ÚTIL SE CALCULA, NO SE RECUERDA. En otro CV de esta sesión los
topes de tabulación quedaron a una pulgada de donde debían porque el ancho se
escribió de memoria. Carta son 8.5 in; con márgenes de 0.55 in el ancho útil
es 8.5 - 0.55*2, y de ahí salen los tabuladores de la derecha.

SIN TABLAS EN EL CONTENIDO. La versión anterior metía las competencias en una
tabla de dos columnas; al extraer el PDF equivalente salían PRIMERO los seis
rótulos y DESPUÉS los seis valores, y un lector automático pierde qué va con
qué. Aquí van como párrafos «rótulo: valor», igual que en el PDF.

Las dos únicas tablas son de MAQUETA y están medidas: la cabecera —texto a la
izquierda, retrato a la derecha— y la banda de cifras, que va a dos columnas y
con cada cifra en UN SOLO renglón junto a su frase, porque a cuatro columnas
los números caían en una banda y las frases en otra y la extracción los
separaba de su pareja.
"""
import pathlib, sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_TAB_ALIGNMENT, WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

AQUI = pathlib.Path(__file__).resolve().parent
SALE = AQUI / "cv"; SALE.mkdir(exist_ok=True)
sys.path.insert(0, str(AQUI))
from contenido import DATOS, ES, EN   # noqa: E402

MARGEN = 0.55
ANCHO = Inches(8.5 - MARGEN * 2)      # calculado, no recordado
AMBAR = RGBColor(0x9A, 0x64, 0x14)
TINTA = RGBColor(0x0D, 0x10, 0x16)
GRIS = RGBColor(0x5A, 0x62, 0x73)
CUERPO = RGBColor(0x2B, 0x31, 0x3D)


def filete(par, grosor=6, color="D8DCE3"):
    pPr = par._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(grosor))
    bottom.set(qn("w:space"), "3")
    bottom.set(qn("w:color"), color)
    bdr.append(bottom)
    pPr.append(bdr)


def tramo(par, texto, tam=10, negrita=False, color=CUERPO, mayus=False, espaciado=None):
    r = par.add_run(texto)
    r.font.size = Pt(tam); r.font.bold = negrita; r.font.color.rgb = color
    r.font.name = "Carlito"
    if mayus: r.font.all_caps = True
    if espaciado is not None:
        rPr = r._element.get_or_add_rPr()
        sp = OxmlElement("w:spacing"); sp.set(qn("w:val"), str(espaciado))
        rPr.append(sp)
    return r


def p(doc, texto="", tam=10, negrita=False, color=CUERPO, antes=0, despues=2,
      interlineado=1.12, mayus=False, espaciado=None, alineado=None, estilo=None,
      sangria=None):
    par = doc.add_paragraph(style=estilo) if estilo else doc.add_paragraph()
    par.paragraph_format.space_before = Pt(antes)
    par.paragraph_format.space_after = Pt(despues)
    par.paragraph_format.line_spacing = interlineado
    if alineado is not None:
        par.alignment = alineado
    if sangria is not None:
        par.paragraph_format.left_indent = Inches(sangria)
    if texto:
        tramo(par, texto, tam, negrita, color, mayus, espaciado)
    return par


def encabezado(doc, texto):
    par = p(doc, texto, tam=8.5, negrita=True, color=AMBAR, antes=7, despues=3,
            mayus=True, espaciado=14)
    filete(par)
    return par


def construir(d, lang, destino):
    doc = Document()
    s = doc.sections[0]
    # Igual que el PDF: una sola página. Word mide distinto, así que los
    # márgenes y los espacios se aprietan un punto más que allá.
    s.top_margin = s.bottom_margin = Inches(0.42)
    s.left_margin = s.right_margin = Inches(MARGEN)

    normal = doc.styles["Normal"]
    normal.font.name = "Carlito"
    normal.font.size = Pt(9.5)
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Carlito")

    ciudad = DATOS["ciudad_es"] if lang == "es" else DATOS["ciudad_en"]

    # ── cabecera: texto a la izquierda, retrato a la derecha ────────────
    tc = doc.add_table(rows=1, cols=2)
    tc.autofit = False
    tc.columns[0].width = ANCHO - Inches(1.05)
    tc.columns[1].width = Inches(1.05)
    izq, der = tc.rows[0].cells
    izq.width = ANCHO - Inches(1.05); der.width = Inches(1.05)
    izq.paragraphs[0]._p.getparent().remove(izq.paragraphs[0]._p)

    def pc(celda, texto, tam, neg=False, col=CUERPO, despues=0):
        par = celda.add_paragraph()
        par.paragraph_format.space_before = Pt(0)
        par.paragraph_format.space_after = Pt(despues)
        par.paragraph_format.line_spacing = 1.05
        tramo(par, texto, tam, neg, col)
        return par

    pc(izq, DATOS["nombre"], 23, True, TINTA)
    pc(izq, d["titulo"], 12, True, AMBAR)
    pc(izq, d["bajada"], 9, False, GRIS, despues=3)
    pc(izq, "  ·  ".join([ciudad, DATOS["correo"], DATOS["tel"], DATOS["sitio"]]),
       9, False, CUERPO)

    foto = AQUI / DATOS["retrato"].replace("img/", "cv/img/")
    pr = der.paragraphs[0]
    pr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if foto.exists():
        pr.add_run().add_picture(str(foto), width=Inches(0.98))

    linea = p(doc, despues=5)
    filete(linea, grosor=16, color="B4761A")

    # ── cifras: dos columnas, cada una en un renglón con su frase ───────
    tn = doc.add_table(rows=2, cols=2)
    tn.autofit = False
    for fila in tn.rows:
        for c in fila.cells:
            c.width = ANCHO // 2
    for i, (num, frase) in enumerate(d["cifras"]):
        celda = tn.rows[i // 2].cells[i % 2]
        par = celda.paragraphs[0]
        par.paragraph_format.space_after = Pt(2)
        tramo(par, num + "  ", tam=16, negrita=True, color=AMBAR)
        tramo(par, frase, tam=9.5, color=CUERPO)

    # ── perfil ──────────────────────────────────────────────────────────
    encabezado(doc, d["h_perfil"])
    p(doc, d["perfil"], tam=9.5, despues=2, interlineado=1.12,
      alineado=WD_ALIGN_PARAGRAPH.JUSTIFY)

    # ── competencias: párrafos, nunca tabla ─────────────────────────────
    encabezado(doc, d["h_comp"])
    for k, v in d["comp"]:
        par = doc.add_paragraph()
        par.paragraph_format.space_after = Pt(2)
        par.paragraph_format.line_spacing = 1.1
        par.paragraph_format.left_indent = Inches(0.14)
        par.paragraph_format.first_line_indent = Inches(-0.14)
        tramo(par, k + ": ", tam=9, negrita=True, color=TINTA)
        tramo(par, v, tam=9, color=CUERPO)

    # ── experiencia ─────────────────────────────────────────────────────
    encabezado(doc, d["h_exp"])
    for i, puesto in enumerate(d["exp"]):
        par = doc.add_paragraph()
        par.paragraph_format.space_before = Pt(6 if i else 1)
        par.paragraph_format.space_after = Pt(0)
        par.paragraph_format.keep_with_next = True
        # el tope derecho sale del ancho útil calculado arriba
        par.paragraph_format.tab_stops.add_tab_stop(ANCHO, WD_TAB_ALIGNMENT.RIGHT)
        tramo(par, puesto["puesto"], tam=11, negrita=True, color=TINTA)
        tramo(par, "\t" + puesto["fechas"], tam=8.5, negrita=True, color=GRIS)

        par2 = doc.add_paragraph()
        par2.paragraph_format.space_after = Pt(3)
        par2.paragraph_format.keep_with_next = True
        tramo(par2, puesto["empresa"], tam=9.2, negrita=True, color=AMBAR)
        tramo(par2, "  ·  " + puesto["lugar"], tam=9.2, color=GRIS)

        for punto in puesto["puntos"]:
            p(doc, punto, tam=9, despues=1, interlineado=1.08,
              estilo="List Bullet", sangria=0.22)

    # ── certificaciones y formación ─────────────────────────────────────
    for titulo, filas in ((d["h_cert"], [(a, "", b) for a, b in d["cert"]]),
                          (d["h_edu"], d["edu"])):
        encabezado(doc, titulo)
        for a, sub, der in filas:
            par = doc.add_paragraph()
            par.paragraph_format.space_after = Pt(0.5)
            par.paragraph_format.tab_stops.add_tab_stop(ANCHO, WD_TAB_ALIGNMENT.RIGHT)
            tramo(par, a, tam=9.3, negrita=True, color=TINTA)
            # La institución va EN LÍNEA, no en su propio párrafo: tres
            # estudios a dos párrafos cada uno son seis renglones, y es
            # exactamente lo que empujaba el .docx a una segunda página.
            if sub:
                tramo(par, "   " + sub, tam=8.6, color=GRIS)
            tramo(par, "\t" + der, tam=8.8, negrita=True, color=GRIS)

    doc.save(str(destino))
    return destino


if __name__ == "__main__":
    for lang, d in (("es", ES), ("en", EN)):
        f = construir(d, lang, SALE / f"cv-maurice-valdes-bermudez-{lang}.docx")
        print(f"{f.name}  {f.stat().st_size:,} bytes")
