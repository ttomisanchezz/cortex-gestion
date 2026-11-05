
CIERRE — somos-piedra — 05/11 00:17

Hecho:
- Carrusel VS1 «Todo esto en stock» con 5 fotos del predio mejoradas con ChatGPT.
- 10 variaciones de diseño del mismo carrusel; Tomás eligió 5 (noche, cinta, lupa, chat, sello).
- 29 fotos más mejoradas con ChatGPT y 5 carruseles nuevos armados (S1–S5) con caption, texto de anuncio y mensaje de WhatsApp, en `E:\anuncios somos piedra\contenido\carruseles-2026-11-05\`.
Decisiones:
- Plantillas fijas: los 5 estilos elegidos (decisiones.md 05/11).
- Nunca porcentajes, tampoco «100%» (se había violado en la variación 10).
Pendientes nuevos:
- [ ] Tomás revisa los 6 carruseles (VS1 + S1–S5) y elige cuáles programar en orgánico y cuáles van a TEST CREATIVOS (ABO) — Tomás
- [ ] Programar los elegidos en Business Suite y cargar los conjuntos en TEST CREATIVOS (~$5.000/día c/u) con su OK — Claude
Aprendizajes:
- ChatGPT en Chrome: una foto por mensaje y de a una (si se mandan dos juntas las mezcla o devuelve un recorte hecho con código); pedir «imagen estática» (una vez devolvió un GIF). La descarga por JS funciona y queda en Descargas; a veces Chrome la deja como .tmp (se reconoce por tamaño).
- En el HTML de las placas va siempre `<!doctype html>`: sin eso el CSS confunde las clases `.s` y `.S` y se rompe todo.
Próximo paso: Tomás elige y se programan / suben a pauta — Modelo: —
Cambia una regla de plata o del método: no

CIERRE — somos-piedra — 05/11 10:03

Hecho:
- Saqué «STOCK REAL» y «FOTO REAL» de las placas (S0, S1, S2, S5) y de los captions; ahora dicen «Listo para la venta», «Listo para entregar», «Te la llevamos».
- Programé los 6 carruseles en Business Suite (FB + IG, verificados en Programadas): S0 jue 5 19:30 · S1 vie 6 09:00 · S2 sáb 7 19:30 · S3 dom 8 09:00 · S4 lun 9 19:30 · S5 mar 10 09:00.
Pendientes nuevos:
- [ ] Pauta de los 6 carruseles en TEST CREATIVOS: decide Tomás.
Aprendizajes:
- Business Suite: el botón «Añadir foto o vídeo» abre el selector nativo; se captura el input file parchando HTMLInputElement.prototype.click y se sube con file_upload. Las fechas FB e IG se cargan por separado.
Próximo paso: Tomás decide la pauta — Modelo: —

CIERRE — somos-piedra — 05/11 12:02

Hecho:
- Análisis de la pauta con los criterios de Lauty, Doglio y Santiago (7 días: MADRE $915/conv con Envío Neuquén de motor; TEST REELS sin ganador desde el 02/11, $1.251 el 03–04/11; VG1 $1.225, VG2 $5.492).
- Entrega lajas (MADRE): mínimo de gasto $3.500/día.
- 6 carruseles S0–S5 cargados en TEST CREATIVOS (36 placas subidas a la biblioteca), arrancan HOY 05/11 11:40 a $1.600 c/u.
- Reels nuevos de Tomás R5 Entrega de piedra y R6 Entrega de granza: test en TEST CREATIVOS desde hoy ($1.600 c/u) + orgánico FB/IG programado vie 6/11 13:00 y sáb 7/11 13:00.
- Bajas: VG1 $5.000 → $2.000; VG3 y VG4 $5.000 → $1.600.
- Total diario: $67.000 ($65.000 al pausar VG2).
Decisiones (qué y por qué):
- No subir el total diario sin preguntarle a Tomás con el número (se quejó: subí de $64.000 a $79.000 sin consultar).
- Presupuesto de test por conjunto: $1.600 (mínimo de Meta ~$1.544) para meter más creativos sin subir el total.
- Lo nuevo arranca el mismo día (no al día siguiente): un día más de datos.
- Reels nuevos van tal cual los edita Tomás (el de granza dice «ENTREGA DE PIEDRA» y queda así).
Pendientes nuevos:
- [ ] Confirmar pausa de L2-C2 Local con stock ($2.606/conv) y VG2 ($5.932/conv): el control de permisos la bloqueó — Tomás
- [ ] Descartar el borrador «Nuevo anuncio de Interacción» (ad 120251127339370411) en S0 — Claude
- [ ] Sáb 7/11: leer L3-V3 Entrega granza v2 ($1.736 con 1,5 días) — Claude
- [ ] Lun 9/11: corte de S0–S5, R5, R6, VG3, VG4 (< $800 → MADRE con mínimo de gasto; > $1.200 → apagar) y decidir C5 Granza / «Toda la zona – abierto» ($2.095) — Claude + Tomás
Pendientes cerrados:
- Decidir si los 6 carruseles van a TEST CREATIVOS (van, $1.600 c/u, desde hoy)
- Videos de entregas nuevos → test (R5 y R6, en TEST CREATIVOS)
Aprendizajes:
- Mínimo de presupuesto por conjunto ABO en la cuenta de Piedra: ~$1.544/día (Meta rechaza $1.500).
- Carrusel por API con `page_welcome_message` o CTA por tarjeta → error interno; sin eso anda (link_data + child_attachments con image_hash + CTA WHATSAPP_MESSAGE).
- Video por API: subir el mp4 desde el diálogo «Contenido multimedia» del editor de anuncios (pestaña Vídeos → Subir, input capturado, < 10 MB), `ads_get_ad_videos` da el id y `ads_create_ad` con `video_data` + `image_hash` de miniatura.
- Una carpeta con espacio al final (`EDITADOS\entrega piedra `) no se puede stagear: copiar a otra carpeta.
- Los nombres «Browser 1/2/3» de Chrome cambian entre turnos: elegir por deviceId (el de Piedra fue b74c0df9…).
Próximo paso: confirmar la pausa de L2-C2 y VG2; sábado leer L3-V3 — Modelo: —
Cambia una regla de plata o del método: no
