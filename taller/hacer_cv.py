# -*- coding: utf-8 -*-
"""Genera el CV en HTML (y de ahí el PDF) en español e inglés.

LAS TRAMPAS DEL PDF. Ninguna es teoría: cada una se midió sobre el PDF
escrito, y cada una rompía el entregable de una forma que no se ve mirándolo.

 1. FUENTE VARIABLE / CFF → TIPO 3. Un .otf (curvas CFF) entregado a Chromium
    sale como Type 3 —los glifos como procedimientos de dibujo— y muchos
    lectores y casi todos los ATS NO pueden extraer ese texto. Aquí se usan
    las Inter convertidas a TrueType (glyf), que salen como CID TrueType.

 2. ⚠ LAS ALTERNATIVAS CONTEXTUALES DE INTER SE COMEN EL «+» DEL TELÉFONO.
    MEDIDO sobre el PDF: «+52 55 4767 7080 (HA) EC-Council» se extraía como
    «52 55 4767 7080 HA ECCouncil». Inter tiene
    puntuación de caja alta en `calt`, Chromium la aplica por defecto, y los
    glifos sustituidos no tienen correspondencia Unicode: acaban en el Área de
    Uso Privado. O sea que un ATS guardaba el teléfono SIN el código de país.
    `font-feature-settings:"calt" 0` lo arregla, comprobado extrayendo otra vez.

 3. LAS COMPETENCIAS NO VAN EN TABLA. Con <table> de dos columnas la
    extracción devolvía PRIMERO los seis rótulos y DESPUÉS los seis valores:
    un ATS que lee eso pierde qué pertenece a qué. Van como párrafos
    «rótulo + valor», que se extraen en el orden en que se leen.

 4. `position:relative` EN LOS <li> ROMPE EL ORDEN DE LECTURA: el PDF emite el
    texto en orden de pintado y esos elementos se van al final del documento,
    despegados de su encabezado. Aquí las viñetas son `list-style` con
    `::marker`, sin posicionamiento.

 5. letter-spacing ALTO PARTE LAS PALABRAS. A partir de ~0.155em Chromium
    emite cada glifo por separado y la extracción devuelve «E X P E R I E N C
    I A». Aquí el máximo es 0.07em.

 6. Y TODO SE COMPRUEBA SOBRE EL PDF ESCRITO, no sobre la intención.
"""
import pathlib, subprocess, sys, html as H

AQUI = pathlib.Path(__file__).resolve().parent
SALE = AQUI / "cv"
SALE.mkdir(exist_ok=True)
FUENTES = (AQUI / "fuentes").as_uri()
sys.path.insert(0, str(AQUI))
from contenido import DATOS, ES, EN   # noqa: E402

CHROME = "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome"

# Se construye fuera del literal de CSS: en una versión anterior la ruta se
# interpoló dentro de un """...""" que no interpola nada, el @font-face apuntaba
# a la cadena literal, fallaba en silencio y el PDF salía con otra fuente.
FONTFACE = "".join(
    '@font-face{font-family:"InterCV";font-weight:%d;font-style:normal;'
    'src:url("%s/Inter-%s.ttf") format("truetype")}' % (peso, FUENTES, nombre)
    for peso, nombre in ((400, "Regular"), (500, "Medium"),
                         (600, "SemiBold"), (700, "Bold"))
)

CSS = FONTFACE + """
/* UNA PÁGINA. Con dos, la segunda se quedaba al 40 % y un currículum que
   acaba a media hoja se lee como inacabado. Todo lo de abajo —cuerpo a 9pt,
   interlineado 1.36, credenciales a un renglón— existe para que quepa sin
   apretarlo: el texto ya se recortó un 27 % antes de tocar un solo tamaño. */
@page { size: Letter; margin: 11mm 12mm; }
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  font-family:"InterCV","Carlito","Liberation Sans",Arial,sans-serif;
  font-size:9pt; line-height:1.36; color:#15181F;
  -webkit-print-color-adjust:exact; print-color-adjust:exact;
  /* La línea que le devuelve el «+» al teléfono. Ver trampa 2 arriba. */
  font-feature-settings:"calt" 0;
  font-variant-ligatures:none;
}

/* ── cabecera ─────────────────────────────────────────────────────────── */
/* El retrato va posicionado y NO flotado: un float mete la imagen en el
   flujo del texto y la extracción se desordena. Posicionado, el texto se
   extrae en su orden y la foto no participa. */
.cab{position:relative;border-bottom:2.2pt solid #B4761A;padding-bottom:7pt;
  margin-bottom:8pt;min-height:66pt}
.cab .txt{padding-right:82pt}
.foto{position:absolute;top:0;right:0;width:67pt;height:67pt;border-radius:50%;
  overflow:hidden;background:#EAE7E3}
.foto img{width:100%;height:100%;object-fit:cover;display:block}
h1{font-size:21pt;font-weight:700;letter-spacing:-0.018em;margin:0 0 2pt;color:#0D1016}
.rol{font-size:10.8pt;font-weight:600;color:#9A6414;margin:0 0 1pt;letter-spacing:0.004em}
.bajada{font-size:8.4pt;color:#5A6273;margin:0 0 6pt;letter-spacing:0.05em}
.contacto{font-size:8.5pt;color:#2B313D;margin:0}
.contacto span{white-space:nowrap}
.contacto i{color:#A9B0BD;font-style:normal;margin:0 6pt}

/* ── secciones ────────────────────────────────────────────────────────── */
h2{
  font-size:8.2pt;font-weight:700;letter-spacing:0.07em;text-transform:uppercase;
  color:#9A6414;margin:5.5pt 0 2.5pt;padding-bottom:1.8pt;
  border-bottom:0.6pt solid #D8DCE3;
}
h2:first-of-type{margin-top:0}

/* ── la banda de cifras: lo primero que mira un humano ──────────────────
   DOS COLUMNAS Y UNA SOLA LÍNEA POR CELDA, y las dos cosas por la misma
   razón. MEDIDO sobre el PDF: con cuatro columnas el número y su frase caían
   en bandas distintas y la extracción devolvía «20 · 4 · 8 PB · +38» y
   DESPUÉS las cuatro frases sueltas, sin pareja. pdfminer agrupa por altura,
   así que el número tiene que ir en el MISMO renglón que su frase, y el
   renglón tiene que caber sin partirse. A media página sí cabe.
   Ahora cada cifra se extrae como una oración entera. */
table.cifras{width:100%;border-collapse:collapse;margin:0 0 6pt}
table.cifras td{width:50%;padding:1.5pt 14pt 1.5pt 0;vertical-align:baseline;
  white-space:nowrap;border-bottom:0.6pt solid #E6E3DF}
table.cifras tr:last-child td{border-bottom:0}
table.cifras b{font-size:15pt;font-weight:700;color:#9A6414;
  letter-spacing:-0.02em;margin-right:7pt}
table.cifras span{font-size:9.2pt;color:#2B313D}
p{margin:0 0 5pt}
.perfil{text-align:justify;margin:0}

/* ── logros: lo primero que lee un humano ─────────────────────────────── */
ul.logros{margin:0;padding:0 0 0 11pt;list-style:disc outside}
ul.logros li{margin:0 0 3pt;padding-left:2pt;color:#15181F;font-weight:500}
ul.logros li::marker{color:#B4761A}
ul.logros li:last-child{margin-bottom:0}

/* ── competencias: párrafos, NUNCA tabla. Ver trampa 3 arriba ─────────── */
p.comp{margin:0 0 1.9pt;color:#2B313D;text-indent:-10pt;padding-left:10pt}
p.comp:last-child{margin-bottom:0}
p.comp b{font-weight:600;color:#0D1016}

/* ── experiencia ──────────────────────────────────────────────────────── */
.puesto{margin:0 0 5.6pt}
.puesto:last-child{margin-bottom:0}
.fila{display:flex;justify-content:space-between;align-items:baseline;gap:10pt;margin:0 0 1pt}
.cargo{font-size:10.2pt;font-weight:700;color:#0D1016;margin:0}
.fechas{font-size:8.5pt;color:#5A6273;white-space:nowrap;font-weight:600}
.donde{font-size:8.9pt;color:#9A6414;font-weight:600;margin:0 0 3pt}
.donde em{color:#5A6273;font-style:normal;font-weight:400}

/* Viñetas con list-style: NUNCA position:relative, que manda estos párrafos
   al final del PDF y los despega de su encabezado. */
ul{margin:0;padding:0 0 0 11pt;list-style:disc outside}
li{margin:0 0 1.2pt;padding-left:2pt;color:#2B313D}
li::marker{color:#C79043;font-size:0.85em}
li:last-child{margin-bottom:0}

/* ── credenciales ─────────────────────────────────────────────────────── */
p.lista{margin:0 0 1.6pt;color:#0D1016;display:flex;gap:9pt;align-items:baseline}
p.lista:last-child{margin-bottom:0}
p.lista b{font-weight:600;flex:1 1 auto}
/* El subtítulo va EN LÍNEA y no en su propio renglón: tres estudios a dos
   renglones cada uno son seis, y a uno son tres. */
p.lista b small{color:#5A6273;font-size:8.4pt;font-weight:400;margin-left:5pt}
p.lista span{color:#5A6273;font-size:8.7pt;white-space:nowrap;font-weight:600;flex:0 0 auto}

/* Un puesto SÍ se puede partir entre páginas, y tiene que poder. Con
   `break-inside:avoid` el primer puesto no cabía en lo que quedaba de la
   página 1 y se iba entero a la 2: la primera hoja quedaba vacía en su tercio
   inferior, que es justo donde un reclutador decide si sigue leyendo. Lo que
   no se parte es lo pequeño: una viñeta, una línea de credencial, y un
   encabezado nunca se queda solo al pie. */
p.lista,li{break-inside:avoid}
h2,.fila,.donde{break-after:avoid}
.puesto{orphans:3;widows:3}
"""

PLANTILLA = """<!doctype html>
<html lang="{lang}">
<head><meta charset="utf-8"><title>{nombre} - {titulo}</title>
<style>{css}</style></head>
<body>
<header class="cab">
  <div class="txt">
    <h1>{nombre}</h1>
    <p class="rol">{titulo}</p>
    <p class="bajada">{bajada}</p>
    <p class="contacto">
      <span>{ciudad}</span><i>·</i><span>{correo}</span><i>·</i><span>{tel}</span><i>·</i><span>{sitio}</span>
    </p>
  </div>
  <div class="foto"><img src="{retrato}" alt="{nombre}"></div>
</header>

<table class="cifras">{cifras}</table>

<h2>{h_perfil}</h2>
<p class="perfil">{perfil}</p>

<h2>{h_comp}</h2>
{comp}

<h2>{h_exp}</h2>
{exp}

<h2>{h_cert}</h2>
{cert}

<h2>{h_edu}</h2>
{edu}
</body></html>
"""


def e(s):
    return H.escape(str(s), quote=False)


def armar(d, lang):
    ciudad = DATOS["ciudad_es"] if lang == "es" else DATOS["ciudad_en"]

    cel = ['<td><b>%s</b><span>%s</span></td>' % (e(n), e(q)) for n, q in d["cifras"]]
    cifras = "<tr>" + cel[0] + cel[1] + "</tr><tr>" + cel[2] + cel[3] + "</tr>"

    comp = "".join(
        f'<p class="comp"><b>{e(k)}:</b> {e(v)}</p>' for k, v in d["comp"]
    )

    exp = ""
    for p in d["exp"]:
        puntos = "".join(f"<li>{e(x)}</li>" for x in p["puntos"])
        exp += (
            '<div class="puesto">'
            f'<div class="fila"><p class="cargo">{e(p["puesto"])}</p>'
            f'<span class="fechas">{e(p["fechas"])}</span></div>'
            f'<p class="donde">{e(p["empresa"])} <em>· {e(p["lugar"])}</em></p>'
            f"<ul>{puntos}</ul></div>"
        )

    cert = "".join(
        f'<p class="lista"><b>{e(a)}</b><span>{e(b)}</span></p>'
        for a, b in d["cert"]
    )

    edu = "".join(
        f'<p class="lista"><b>{e(t)}'
        + (f"<small>{e(s)}</small>" if s else "")
        + f'</b><span>{e(f)}</span></p>'
        for t, s, f in d["edu"]
    )

    return PLANTILLA.format(
        lang=lang, css=CSS, nombre=e(DATOS["nombre"]), titulo=e(d["titulo"]),
        bajada=e(d["bajada"]), ciudad=e(ciudad), correo=e(DATOS["correo"]),
        tel=e(DATOS["tel"]), sitio=e(DATOS["sitio"]),
        h_perfil=e(d["h_perfil"]), perfil=e(d["perfil"]),
        cifras=cifras, retrato=e(DATOS["retrato"]),
        h_comp=e(d["h_comp"]), comp=comp,
        h_exp=e(d["h_exp"]), exp=exp,
        h_cert=e(d["h_cert"]), cert=cert,
        h_edu=e(d["h_edu"]), edu=edu,
    )


def pdf(src_html, destino):
    subprocess.run([
        CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
        "--no-pdf-header-footer",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=5000",
        "--print-to-pdf=" + str(destino),
        src_html.as_uri(),
    ], check=True, capture_output=True, timeout=120)


if __name__ == "__main__":
    for lang, d in (("es", ES), ("en", EN)):
        h = SALE / f"cv-maurice-valdes-bermudez-{lang}.html"
        h.write_text(armar(d, lang), encoding="utf-8")
        p = SALE / f"cv-maurice-valdes-bermudez-{lang}.pdf"
        pdf(h, p)
        print(f"{p.name}  {p.stat().st_size:,} bytes")
