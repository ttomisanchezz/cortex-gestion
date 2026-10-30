
CIERRE — somos-piedra — 19/10 18:05 (sesiones del 17/10 noche y 19/10)

Hecho:
- 17/10: análisis de la pauta desde el 13/10 (MADRE 69 chats a $558; conjunta 41 a $1.184). Boceto "Granza" con la plantilla de retención (Anton, color único, chip, número calado, botón que adelanta, barra, casilla, cierre con repaso) y prueba de 3 estilos de escena (A foto real con IA, B portada Pixar, C todo Pixar), ~USD 0,84.
- 17/10: investigación de cómo pautan los grandes de piedra en Meta (Argentina, exterior, Brasil y México, con capturas en Chrome para BR y MX). Resumen en el proyecto de Claude: `claude/referencias-anuncios-2026-10-17.md`.
- 17/10: boceto "la mano con la pieza" (7 tarjetas con fotos reales del IG, sin texto) en `E:\anuncios somos piedra\anuncios-v2\boceto-mano\`.
- 19/10: Granza con la plantilla v2 Pixar (6 escenas, ~USD 1,70): a Tomás le gustó pero "muy surrealista". Versión "por código" (fotos reales + esquemas SVG): aprobada.
- 19/10: 5 carruseles v2 por código (Granza, Frente, 5 errores al revestir, Cuánta piedra necesito, Patio y pileta), 31 placas 1080×1350 en `E:\anuncios somos piedra\anuncios-v2\final\<tema>\`. 3 portadas fotorrealistas nuevas con la piedra real (frente, pileta, errores), ~USD 0,84. Armador: `anuncios-v2\armar.py` + `carruseles_v2.py`/`svgs.py` (en el chat) y `contenido\fotos_v2.py`.
- 19/10 Meta: MADRE (120250759505930411) a $7.000/día (el cambio por API la pausó; reactivada). Campaña nueva "Somos Piedra - TEST v2 codigo (5 carruseles) - Oct 2026" (120250865076760411, CBO $13.000/día), conjunto 120250865080500411 (CONVERSATIONS / WHATSAPP, misma zona que la MADRE, Advantage+), 5 anuncios ACTIVOS: Granza 120250865085520411, Frente 120250865088950411, 5 errores 120250865092770411, Cuánta piedra 120250865095370411, Patio y pileta 120250865098250411; todos con orden fijo de tarjetas. Conjunta Día de la Madre (120250805457440411) PAUSADA.
- Reporte al 19/10: MADRE 86 chats a $563 desde el 13/10 (C5 Granza 69 a $546, C1 Frente 14 a $651); 7, 8 y 10 chats el 17, 18 y 19/10. Conjunta: 46 chats a $1.221.
Decisiones (qué y por qué):
- Pauta Somos Piedra a $20.000/día: MADRE $7.000 + TEST v2 $13.000 (más consultas; la MADRE estaba limitada por presupuesto).
- Estilo de los carruseles de anuncios: v2 "por código" (fotos reales + esquemas), IA solo en portadas fotorrealistas con rótulo. Pixar descartado por surrealista.
- Pausar la conjunta (ya no gastaba y con $1.221/chat).
Pendientes nuevos:
- [ ] Fran revisa 3 frases del carrusel "5 errores" (pared a plomo, presentar piezas, adhesivo para piedra natural) — Tomás / Fran
- [ ] Revisión del TEST v2 el 26/10: apagar los 2 carruseles con peor costo por chat y meter 2 nuevos — Claude / Tomás
- [ ] Ver en el Administrador si los anuncios nuevos salen en Instagram (la API no ve cuenta de IG vinculada) — Tomás
- [ ] Los 5 anuncios v2 no tienen mensaje armado de WhatsApp (no se pudo por API) — Tomás, si lo quiere, desde el Administrador
- [ ] Conjunto/campaña de Reels: alguien de Somos Piedra hablando a cámara en el acopio (formato Super Pedras / Piedra Urbana) — Tomás edita
- [ ] Contar ventas de los chats con la etiqueta "anuncio" — Fran
Pendientes cerrados:
- Test 1-1-3 (A quincho, B pileta, D obras) del 15/10: reemplazado por el TEST v2.
Aprendizajes:
- Cambiar el presupuesto por API pausa la campaña: reactivar y verificar.
- En esta cuenta `ads_create_creative` rechaza el CTA WHATSAPP_MESSAGE; funciona `ads_create_ad` con object_story_spec inline (link_data + child_attachments con `picture` = URL pública, multi_share_optimized false).
- URL pública para las placas: subirlas a Higgsfield (/files/generate-upload-url) da una URL de cloudfront que Meta acepta.
- GPT Image 2 no está en la API de Higgsfield con esta clave (model_not_found).
Próximo paso: revisión del TEST v2 el 26/10 y corregir "5 errores" si Fran cambia algo — Modelo: —
Cambia una regla de plata o del método: no
