# Somos Piedra — Plan de contenido con IA (desde 15/10/2026)

## ⚠️ Datos fijos de producto — chequear ANTES de publicar o subir cualquier pieza (03/11/2026, Tomás)
- Granza: se vende en **bolsas**. **Nunca escribir "bolsón"/"bolsones"** (ni en placas, ni en caption, ni en hooks, ni en nombres de anuncio).
- Medida: **1 bolsa (~40 kg) cubre 1 m² a 3 cm.** No hay otra medida. Nunca "25 m²".
- Antes de entregar piezas: buscar `bols[oó]n` y `25 m` en los textos y en el HTML de las placas; si aparece, se corrige antes de mostrarlo.
- Cualquier medida, precio o unidad que no esté en esta sección o en `README.md` §Respuestas de Fran: **se pregunta a Tomás, no se deduce.**

Sistema: `E:\anuncios somos piedra\contenido\` (ver `LEEME.md` ahí). Generador de escenas `hf.py` (Higgsfield API, Marketing Studio Image) + compositor `componer.py` (texto, logo y rótulo).

## Decisiones (Tomás, 15/10 — cerradas)
- La IA va **por API** (open.higgsfield.ai, saldo USD 24,20 el 15/10), no por el conector (plan Plus con 0,15 créditos).
- La IA hace **ambientes de inspiración con la piedra real como referencia**, sin alterar la calidad, el color ni la textura de la piedra. Las obras se muestran solo con fotos reales. Toda escena IA lleva el rótulo "Idea de diseño · piedra real de Somos Piedra".
- El **texto lo pone el compositor**, no la IA.
- Arranque: **1 carrusel + 2 historias por semana** (no es prioridad). (Tomás dijo "por día"; se tomó "por semana" por el "no es prioridad": confirmar.)
- No se tocan las campañas de Meta en este frente.

## Costos (precios de la API al 15/10, con 15% de descuento)
- Escena 2k calidad low: USD 0,019. 1k low: USD 0,014. 4k high: USD 0,61 (no usar).
- Semana tipo (4 escenas IA): ~USD 0,08. Mes: ~USD 0,35. Con el saldo actual alcanza para ~1.200 escenas.

## Fases
**Fase 0 — puesta en marcha (esta semana)**
1. Tomás: agregar `*.higgsfield.ai` a los dominios permitidos de claude.ai (Settings → Capabilities) y crear `contenido\.env` con `HF_KEY_ID` y `HF_KEY_SECRET` (modelo en `env-ejemplo.txt`).
2. Primera corrida: pieza `2026-s42-carrusel-quincho-ideas` (3 escenas + 1 de historia, ~USD 0,08).
3. Prueba de fidelidad: comparar cada escena con la foto de la piedra. Si la cambia, probar `quality: high` en una sola escena y anotar costo y resultado.
4. OK de Tomás y publicación de la semana 42.

**Fase 1 — ritmo base (semanas 43 a 46)**
- 1 carrusel + 2 historias por semana, siguiendo el calendario de pilares.
- Fran manda fotos de obras reales una vez por mes (banco propio para placas "obra real" y para el ángulo 9, antes y después).
- Medir por pieza: alcance, guardados, compartidos y chats de WhatsApp que digan "vi el post". Anotar en el JSON de la pieza.

**Fase 2 — escalar (con 4 semanas de datos y la fidelidad OK)**
- Subir a 3 carruseles + 5 historias por semana (~USD 0,50/semana).
- Reels cortos: animar escenas aprobadas con image-to-video (Kling 3.0 desde USD 0,071/s; un reel de 5 s ≈ USD 0,35).
- Los carruseles orgánicos que mejor rindan pasan a probarse como anuncios (con OK de Tomás, en la cuenta de pauta).

**Fase 3 — fábrica**
- Lote mensual: las 4 semanas en una sola sesión; Fran aprueba todo junto.
- Skill `contenido-piedra` para que cualquier chat lo corra igual.
- Mismo sistema para Ibero (vivero): se vende como extra del abono.

## Calendario de pilares (rota cada 8 semanas)
| Semana | Pilar | Escenas IA | Fotos reales |
|---|---|---|---|
| s42 | Quincho (ocre, pizarra, verde bronce) | 3 + 1 historia | obra cat-035, piedra ocre |
| s43 | Pileta y patio (travertino, riojana, pórfido) | 3 | piezas en el local |
| s44 | Entrada y vereda en pórfido | 2 | adoquín, pórfido |
| s45 | Fachada (verde bronce, Zapala, Bariloche) | 3 | obras |
| s46 | Guía "5 cosas antes de revestir" | 0–1 | medición en el local |
| s47 | Obras reales + reseñas | 0 | obras de Fran |
| s48 | Vení a tocarla (local) | 0 | local y stock |
| s49 | Formas de pago (si Fran confirma) | 1 | — |

## Pendientes
- Confirmar que cat-035 es una obra propia y que cat-017 es la pizarra negra que venden.
- Si la subida de fotos falla por otro dominio de almacenamiento, agregarlo a los permitidos.

## Actualización 16/10
- Tomás confirmó: **mínimo 1 carrusel por día**. Calendario 19/10–15/11 (28 carruseles) en `E:\anuncios somos piedra\contenido\calendario\calendario.md`, briefs en `piezas/`.
- Reparto semanal: Lun autoridad · Mar inspiración · Mié prueba social · Jue autoridad · Vie oferta sin precio · Sáb inspiración · Dom local.
- 20 escenas IA en total (~USD 0,38). Pendiente: confirmaciones de Fran marcadas en `a_confirmar` (obras propias, reseñas literales, pagos, envío, horario, medición sin cargo).

## Portadas de carrusel con hook visual (02/11/2026, Tomás)
Las portadas eran todas iguales (texto arriba a la izquierda sobre una foto) y no frenaban el scroll. Somos iPhone se diferencia por el hook visual del primer slide, y Somos Piedra pasa a hacer lo mismo en **todos** los carruseles:
- **Protagonista visible:** la piedra puesta, el error (la lavandina, el revoque que se pela) o el antes. Foto real o escena IA.
- **Marca gráfica encima** (la dibuja el armador con `"marcas"`): `x` = el error, `check` = lo correcto, `circulo`, `flecha`, `sello` (ERROR, SOS, OJO), `cinta` (cinta de peligro).
- **El texto rota de lugar** con `"layout"`: `abajo`, `medio`, `arriba` o un split «esto o esto». Las 3 portadas del día van con layouts distintos; `arriba` solo si la imagen tiene cielo o pared limpia.
- Título que nombra el error o la elección en 3 a 5 palabras («Esto arruina tu piedra», «¿Ocre o verde bronce?»).
- Sin piedra de Somos Piedra en la imagen → `"rotulo": "Imagen ilustrativa"`.
- Dónde: regla en `ideas-dia\PROMPT.md` §3; armador en `ideas-dia\kit.zip` (`armar.py` con `layout`, `marcas` y `rotulo`; copia vieja `kit.zip.bak-2026-11-02`).
- Primeras portadas así: carruseles del 02/11 (A split ocre/verde bronce, B bidón de lavandina tachado, C frente descascarado con círculo y sello SOS).

## Imagen = texto (02/11/2026, Tomás)
Cada placa de cada carrusel muestra lo que dice su texto («Agua y cepillo suave» → balde y cepillo sobre la piedra). Orden: 1) foto real si muestra exactamente eso; 2) si no, escena nueva de ChatGPT Image para esa placa (con refs de la piedra si aparece); 3) nunca una foto que contradiga el texto. Sin tope de escenas en los carruseles; en placas sueltas, solo la recomendada. `armar_dia.py` ya es la versión con escenas (copia vieja `armar_dia.py.bak-2026-11-02`).

## Plantillas fijas de carruseles (05/11/2026, Tomás)
- 5 estilos elegidos entre 10 variaciones: **noche** (círculo a mano), **cinta** (cinta de obra), **lupa** (zoom a la piedra), **chat** (conversación de WhatsApp) y **sello** (sello circular, SIN porcentajes).
- Armador: `E:\anuncios somos piedra\contenido\carruseles-2026-11-05\plantillas.py` + `carruseles.json` (`mk.py` arma el JSON). Valida antes de armar: foto distinta por placa y nada de `%`, `$`, bolsón, gratis, descuento, cuotas, 25 m².
- Fotos: las 40 del predio (`referencias\fotos-2026-11-04\`) mejoradas con ChatGPT en Chrome (cuenta Franco Muñoz): luz cálida, nítidas, sin autos ni basura; la piedra queda igual. Mejoradas en `_trabajo-nuevos\stock-2026-11-04\ia\` (5) e `ia2\` (29). Se descargan solas a Descargas; si Chrome las deja como `.tmp`, se identifican por tamaño.
- Primer lote (05/11): S1 lupa «Mirala de cerca», S2 chat «¿Qué tienen?», S3 sello «¿Qué color va con tu casa?», S4 noche «¿Qué piedra va en cada lugar?», S5 cinta «Lista para tu obra». Cada carpeta tiene 01–06.jpg y `texto.txt` (caption, texto del anuncio y mensaje de WhatsApp). Más el VS1 «Todo esto en stock» del 04/11 en `_trabajo-nuevos\stock-2026-11-04\VS1\`.
- Fotos del predio todavía sin usar: IMG_1754, IMG_1755, IMG_1756, IMG_1757, lote2-09 y lote2-13 (gemela de lote2-12).

## Placas de datos con código (11/11/2026)
- Segunda pieza del día (13:30): placa de un solo dato, 1080×1350, hecha 100 % con código (HTML + SVG, sin fotos ni IA). Generador: `E:\anuncios somos piedra\contenido\semana-15-11\gen.py` (Playwright; valida las palabras prohibidas). Primera tanda P1–P7, del 15 al 21/11.
- Carruseles de plantillas de pauta (N1–N6) también van en orgánico con su «CAPTION (orgánico)» de `texto.txt`. Ya salieron todos: del 22/11 en adelante hay que armar nuevos.
- Cómo se programa sin ver la pantalla: `conocimiento/aprendizajes.md` (sección 11/11).

