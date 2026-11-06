# -*- coding: utf-8 -*-
"""Lo que un ATS ve. No lo que yo creo que ve: lo que sale de extraer el PDF."""
import sys, re, unicodedata
from pdfminer.high_level import extract_text
from pypdf import PdfReader

ruta = sys.argv[1]
t1 = extract_text(ruta)
r = PdfReader(ruta)
t2 = "".join(p.extract_text() for p in r.pages)

print("=" * 72)
print(ruta.split("/")[-1], "·", len(r.pages), "pagina(s)")
print("pdfminer:", len(t1), "caracteres   pypdf:", len(t2), "caracteres")

# 1 · fuentes: Type 3 = ilegible para casi todo ATS
tipos = set()
for pg in r.pages:
    fo = pg.get("/Resources", {}).get("/Font", {})
    for k in fo:
        f = fo[k].get_object()
        sub = str(f.get("/Subtype"))
        if sub == "/Type0":
            d = f.get("/DescendantFonts")[0].get_object()
            sub += " > " + str(d.get("/Subtype"))
        tipos.add(sub + "  " + str(f.get("/BaseFont")))
for x in sorted(tipos):
    mal = "Type3" in x
    print(("  ✗ " if mal else "  ✓ "), x)

# 2 · caracteres del Area de Uso Privado: glifos sin correspondencia Unicode
pua = sorted({c for c in t1 + t2 if 0xE000 <= ord(c) <= 0xF8FF})
print("  ", "✗ PUA:" if pua else "✓ sin caracteres de Uso Privado",
      [hex(ord(c)) for c in pua] if pua else "")

# 3 · palabras partidas: «E X P E R I E N C I A»
part = re.findall(r"(?:\b\w\s){4,}\w\b", t1)
print("  ", "✗ texto partido:" if part else "✓ sin texto partido en glifos",
      part[:3] if part else "")

# 4 · lo que no puede faltar
faltan = []
for q in sys.argv[2:]:
    if q not in t1 and q not in t2:
        faltan.append(q)
print("  ", "✗ NO SE EXTRAE:" if faltan else "✓ se extrae todo lo exigido", faltan)

# 5 · orden de lectura: los encabezados deben salir en orden
print("-" * 72)
for ln in t1.splitlines():
    s = ln.strip()
    if s and s == s.upper() and len(s) > 4 and any(c.isalpha() for c in s):
        print("  SECCION:", s)
print("-" * 72)
print(t1[:700])
