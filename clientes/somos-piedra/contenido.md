# Somos Piedra — Plan de contenido con IA (desde 15/10/2026)

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
