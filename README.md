# Maurice Valdés Bermúdez

Sitio profesional y currículum del ingeniero Bermúdez, SRE en Nutanix México.

| | |
|---|---|
| **Sitio** | `index.html` — una página, sin dependencias, bilingüe ES/EN |
| **CV** | `cv-maurice-valdes-bermudez-{es,en}.pdf` en la raíz (los enlaza el sitio) |
| **Editable** | `cv/*.docx` — una página, mismo contenido |
| **Generadores** | `taller/` |

> **Lo que NO está aquí a propósito.** La revisión con el análisis de sueldo
> —marcada «documento interno, no se envía con la candidatura»—, su generador
> y el CV original del cliente se quedan fuera del repositorio, porque esto
> puede ser público para servir la página. Viven en la copia de trabajo.

---

## El sitio

El lenguaje visual sale de **cosmos.so**, abierto con un navegador de verdad y
medido: no se copió de memoria. De ahí salen el papel cálido `#F4F2EF`, la
tinta `#0D0D0D`, el tracking cerrado (−0.052em en el titular, −0.02em en el
cuerpo), el interlineado de prosa 1.277 y las píldoras de radio completo.

**El gancho es su nube de fichas.** Cosmos llena la suya de fotografía de
moda; un SRE no tiene fotos, porque su trabajo sólo se nota cuando falla. Así
que las fichas llevan **su material**: 8 PB, Pemex, Nutanix AHV, IMSS, CEH,
Lift & Shift, Bangalore, Sídney. La nube es su carrera, a la deriva en 3D con
desenfoque por profundidad.

Son nodos del DOM y no un lienzo: el texto es texto de verdad, y sólo se tocan
`transform` y `filter`, que resuelve el compositor sin recalcular nada.

### Lo que la nube resuelve sola, y por qué fue necesario

La composición no es aleatoria ni está escrita a mano: se **relaja**. Cada
pieza se siembra en una elipse con azar sembrado por su índice —misma
composición en cada carga— y después un bucle las separa hasta que ninguna
pisa a otra, al texto, a los botones, a la barra ni a la cinta.

Cada una de esas reglas existe porque algo se midió roto:

| Lo que se midió | Lo que se cambió |
|---|---|
| A 1280 px casi todas las fichas caían fuera del encuadre: cuatro restos en las esquinas en vez de una nube | Los semiejes se miden **contra la caja**, no contra un radio en píxeles |
| Tres fichas amontonadas encima del nombre y tres abajo a la izquierda | Relajación por pares, con el espacio que cada una va a **barrer**, no su caja en reposo |
| Una ficha encima de un botón que ninguna comprobación veía | La caja se **mide ya pintada**: la trigonometría daba 22 px de media caja donde el navegador pintaba 29 |
| El hueco del titular medía 1200 px de ancho en una ventana de 1280 y nada podía salirse | El hueco son los **renglones pintados**, uno por línea, con sus entrantes |
| Las fichas se metían bajo la barra —transparente arriba del todo— y el menú quedaba ilegible | Se reserva la franja de la barra y la de la cinta |

Si después de todo eso dos siguen cruzándose, **se quita una**. Cinco fichas
limpias se leen; seis amontonadas, no.

### Lo que se puede hacer con la página

- **«Provocar una caída».** La portada afirma que mantiene en pie sistemas que
  no se pueden caer; el botón lo **demuestra**. Se tira la página —las fichas
  se desenfocan, cuatro se ponen en rojo, el punto de la barra pasa a alarma,
  el titular se desplaza— y una consola sube desde abajo con telemetría real:
  latencia en vivo, gráfica de la serie y `T+`. Después se recupera sola por
  fases: alerta → diagnóstico → mitigando → resuelto, con su MTTR. Es
  voluntario, está anunciado como simulación y es la única forma honesta de
  enseñar un oficio que sólo se nota cuando falla.
- **Señalar una ficha enciende las de su mismo trabajo.** Pasar por «CEH» saca
  del fondo a Pentest, AAA+, Firewalls y Hacking ético, hunde el resto y marca
  a la vez el tramo de Grupo Elektra en la línea de tiempo y su puesto en el
  historial. Enseña de qué trabajo salió cada pieza del oficio, que es algo
  que un currículum en papel no consigue decir.
- **En el historial, cada puesto dibuja su parte de los doce años** en la
  columna fija: Nutanix 56 %, Elektra 34 %, bSide 10 %, calculado de las
  mismas fechas que la barra.
- **La cinta de tecnologías responde al scroll**: acelera al bajar, frena y da
  marcha atrás al subir. La mueve el mismo bucle que la nube.
- **Las cifras no cuentan, convergen**: 12 → 22 → 24 → 22 → 20 → 19 → 20. Un
  sistema que se estabiliza, con una barrita debajo que se encoge al dejar de
  oscilar.
- **Tocar la portada suelta un ping** que empuja las fichas al pasar.

Nada de esto se añadió sin comprobarlo. Con el foco puesto, ninguna ficha pisa
el texto ni los botones en ninguno de los tres trabajos, a siete anchos y en
los dos idiomas. Y con movimiento reducido el incidente sigue recorriendo sus
cuatro fases —eso es información— pero sin sacudida ni fichas revueltas.

Dos defectos que sólo salieron midiendo esto:

| Lo que se midió | Lo que se cambió |
|---|---|
| Con el puntero en una esquina el paralaje movía las fichas 52 px y metía las nítidas encima del nombre | El paralaje baja a 18 px y esos 18 px se reservan **sólo contra el texto**: entre fichas no hacen falta, porque el paralaje las mueve a todas en el mismo sentido |
| Al enfocar un trabajo, una ficha borrosa que pasaba por detrás del titular se volvía nítida **encima** de él | Las que pasan por detrás del texto quedan marcadas al repartir y el enfoque las ignora |

### Reglas que aquí no se negocian

- **Nunca `opacity` sobre texto.** El revelado sólo toca `transform`, con
  máscara. Un texto a media transición no cumple contraste y sale en blanco en
  cualquier captura.
- **Y el revelado tiene red de seguridad.** Un repaso manual destapa lo que ya
  está en pantalla, pase lo que pase con el observador: un titular que depende
  de que llegue un aviso es un titular que a veces no está —en una miniatura,
  al imprimir, al abrir a media página—.
- **El contraste se calcula, no se mira.** Los grises de la referencia
  (`#6E6A69` y `#9A9796`) **no se copiaron**: dan 4.78:1 y 2.60:1 sobre el
  papel, y el segundo reprueba AA de calle. Allá son etiquetas decorativas
  junto a fotos; aquí llevan contenido. Quedaron en `#56514F` y `#6B6361`:
  7.00:1 y 5.25:1 sobre el papel, 6.34:1 y 4.76:1 sobre el hueso.
- Nada de `backdrop-filter` sobre el fondo de la página.
- Tipografía **Host Grotesk** + **JetBrains Mono**.
- Bilingüe completo con un botón, incluidas las cadenas que calcula el
  JavaScript. Al cambiar de idioma la nube **se vuelve a sembrar**, porque el
  hueco se mide sobre el bloque de texto y ese bloque cambia de tamaño.

---

## El currículum

```bash
cd taller
pip install fonttools cu2qu python-docx pdfminer.six pypdf
python3 convertir_fuentes.py   # una vez
python3 hacer_cv.py            # PDF ES/EN  -> raíz del repo
python3 hacer_docx.py          # Word ES/EN -> cv/
python3 prueba_ats.py ../cv-maurice-valdes-bermudez-es.pdf "+52 55 4767 7080" "EC-Council"
```

Todo el texto vive en `taller/contenido.py`. **No se edita el PDF ni el
`.docx`: se cambia la cadena ahí y se regenera.** Cada generador escribe
directamente donde se publica, sin un copiado a mano en medio — ese copiado es
por donde el generador y lo servido se desfasan.

### Qué lo hace un CV de seis cifras y no una lista de tareas

- Título con nivel: **Senior** Site Reliability Engineer. Su cargo dentro de
  Nutanix se deja escrito tal cual aparece.
- **Cinco logros arriba del todo.** Un reclutador le da doce segundos a la
  primera pantalla: ahí tiene que estar 8 PB, 38 proyectos, cuatro regiones,
  instructor interno y doce años sin un hueco.
- Cada puesto abre con el **alcance**, no con la tarea.
- Dos páginas. Con 20 años de oficio, una sola se lee como un CV de alguien
  con cinco.
- Las cifras son las **cuatro reales que hay**. No hay una quinta inventada;
  las que faltan están preguntadas en `cv/revision-y-carta-de-presentacion.pdf`.

### ⚠ Las trampas del PDF

**1 · Type 3.** Chromium emite fuentes Type 3 cuando la de origen es `.otf`
con curvas CFF. Type 3 guarda cada glifo como un procedimiento de dibujo y
muchos ATS no saben extraer ese texto. Medido en esta máquina:

| Fuente | Formato | Sale como |
|---|---|---|
| Inter | `.otf` (CFF) | **Type 3** |
| DejaVu Sans, Carlito, Liberation Sans | `.ttf` (glyf) | CID TrueType |

Es el **formato**, no que la fuente sea variable o estática. Por eso
`convertir_fuentes.py` pasa Inter a TrueType con `cu2qu`.

**2 · Las alternativas contextuales de Inter se comían el `+` del teléfono.**
Extrayendo el PDF —que es exactamente lo que hace un ATS— salía esto:

```
INTER      52 55 4767 7080 HA ECCouncil
CARLITO    +52 55 4767 7080 (HA) EC-Council
```

Inter trae puntuación de caja alta en `calt`, Chromium la aplica por defecto y
los glifos sustituidos no tienen correspondencia Unicode: acaban en el Área de
Uso Privado. O sea que un sistema de reclutamiento guardaba el teléfono **sin
el código de país**. Se arregla con `font-feature-settings:"calt" 0`,
comprobado volviendo a extraer. Le pasa a cualquier CV hecho con Inter, que
son muchos.

**3 · Las competencias no van en tabla.** Con `<table>` de dos columnas la
extracción devolvía primero los seis rótulos y después los seis valores: un
lector automático pierde qué va con qué. Van como párrafos «rótulo: valores».

**4 · Las dos de siempre.** `position:relative` en un `<li>` manda ese texto al
final del PDF despegado de su encabezado (por eso las viñetas son `list-style`
con `::marker`), y un `letter-spacing` de 0.155em o más hace que la extracción
devuelva `E X P E R I E N C I A` (aquí el máximo es 0.07em).

`taller/prueba_ats.py` comprueba las cuatro sobre el PDF escrito, más el orden
de lectura y una lista de cadenas que no pueden faltar.

---

## Nada se inventa

El CV original es de **julio de 2021** y está a cinco años de distancia (decía
«Age 34» y «Experience 16 years»). Todo lo publicado sale de él o se deriva de
él.

Los datos que **no se pudieron verificar** están listados como preguntas en el
documento de revisión (fuera del repositorio), no escritos como hechos. Los tres
que más pesan:

1. Si sigue en Nutanix y con qué título exacto.
2. Su LinkedIn — no aparece en ningún lado.
3. Cómo quiere aparecer: Maurice, Mauro o Mauricio. El CV dice **Maurice** y
   eso es lo que se publicó; este repositorio se llama Mauricio.

Hay además una lista de **treinta palabras que probablemente son ciertas y no
están escritas** —Prism, vSphere, NKE, PowerShell, ITIL…— para que las marque.
Ninguna se puso sin confirmar: una palabra que no se sostiene en la entrevista
hace más daño que su ausencia.

Las siglas NCP, NCAP y NSS se dejan sin desarrollar a propósito: desarrollarlas
sería suponer.

## Detalles que se olvidan y aquí están resueltos

- **Tarjeta social** (`tarjeta-social.jpg`, 1200×630). Sin ella, pegar el
  enlace en WhatsApp o LinkedIn da una vista previa en blanco — y este sitio
  existe para enseñárselo a alguien. Se regenera con
  `taller/tarjeta-social.html`. **Cuando haya dominio, la ruta del `og:image`
  tiene que pasar a absoluta**: varios rastreadores no resuelven una relativa.
- **Hoja de impresión.** Impreso va sin nube, sin barra y sin cinta.
- **Hueco de LinkedIn** listo en la sección de contacto: faltan dos líneas de
  comentario por quitar y la dirección.
- **El reloj y el menú se retiran bajo 600 px.** Medido: a 320 px la marca
  (160 px), el reloj (90 px) y el botón de idioma (44 px) suman 334 sobre 272
  de ancho útil, y el que se salía de la pantalla era el botón de idioma — o
  sea que en un teléfono pequeño no había forma de cambiar a inglés.
- **Etiquetas de la barra de trayectoria ocultas bajo 720 px**, y sin padding:
  con `box-sizing:border-box` un tramo no puede ser más angosto que sus 36 px
  de padding, y el de bSide (10 % del total) desbordaba la barra 11 px a
  320 px de ancho.

## Publicación

`.github/workflows/publicar.yml` publica el sitio en GitHub Pages en cada push
a `main`. Arma una carpeta con lo que de verdad se sirve —`index.html`, el
retrato, la tarjeta social y los dos CV— y **aborta el despliegue** si se
cuela algo que no debería o si se perdió el `noindex`.

**Pages necesita que el repositorio sea público** si la cuenta no tiene plan de
pago: GitHub rechaza crear el sitio en un repositorio privado y lo hace con un
error de permisos, no de plan. Por eso lo interno ya está fuera. En cuanto el
repositorio se abra, el workflow enciende Pages solo —`configure-pages` con
`enablement: true`— y el sitio queda en
`https://bigtigermx.github.io/Mauricio-Berm-dez/`.

La página lleva `noindex, nofollow` mientras esto sea una sorpresa: es **una
sola línea** en `index.html` y se borra el día que Maurice diga que sí.
