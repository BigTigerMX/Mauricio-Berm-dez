# -*- coding: utf-8 -*-
"""Convierte Inter de .otf (CFF) a .ttf (TrueType) en fuentes/.

POR QUE EXISTE ESTE PASO, QUE PARECE DE MANIAS Y NO LO ES:
Chromium emite un PDF con fuentes Type 3 cuando la fuente de origen es .otf
con curvas CFF. Type 3 guarda cada glifo como un procedimiento de dibujo y
muchos ATS —los sistemas que filtran candidaturas antes de que las vea una
persona— no saben extraer ese texto. Medido en esta misma máquina:

    Inter .otf (CFF)       -> Type 3
    DejaVu / Carlito .ttf  -> CID TrueType

O sea que es el FORMATO, no que la fuente sea variable o estática. Con las
curvas pasadas a cuadráticas el PDF sale CID TrueType, el texto se extrae
completo y en orden, y de paso el archivo baja de 131 KB a 57 KB.

    pip install fonttools cu2qu && python3 convertir_fuentes.py
"""
import pathlib
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import table__g_l_y_f
from fontTools.ttLib.tables._l_o_c_a import table__l_o_c_a
from fontTools.pens.ttGlyphPen import TTGlyphPen
from cu2qu.pens import Cu2QuPen

ORIGEN = pathlib.Path('/usr/share/fonts/opentype/inter')
SALE = pathlib.Path(__file__).resolve().parent / 'fuentes'
TOLERANCIA = 1.0

def a_ttf(src, dst):
    f = TTFont(str(src))
    gs = f.getGlyphSet()
    glifos = {}
    for nombre in f.getGlyphOrder():
        pluma = TTGlyphPen(gs)
        gs[nombre].draw(Cu2QuPen(pluma, TOLERANCIA, reverse_direction=True))
        glifos[nombre] = pluma.glyph()
    t = table__g_l_y_f(); t.glyphs = glifos; t.glyphOrder = f.getGlyphOrder()
    f['glyf'] = t
    f['loca'] = table__l_o_c_a()
    m = f['maxp']; m.tableVersion = 0x00010000
    for campo in ('maxZones','maxTwilightPoints','maxStorage','maxFunctionDefs',
                  'maxInstructionDefs','maxStackElements','maxSizeOfInstructions',
                  'maxComponentElements'):
        setattr(m, campo, 1 if campo == 'maxZones' else 0)
    for sobra in ('CFF ', 'VORG'):
        if sobra in f: del f[sobra]
    f.sfntVersion = '\000\001\000\000'
    f.save(str(dst))

if __name__ == '__main__':
    SALE.mkdir(exist_ok=True)
    for peso in ('Regular', 'Medium', 'SemiBold', 'Bold'):
        src = ORIGEN / f'Inter-{peso}.otf'
        if not src.exists():
            print('falta', src); continue
        dst = SALE / f'Inter-{peso}.ttf'
        a_ttf(src, dst)
        print(f'{dst.name}  {dst.stat().st_size:,} bytes')
