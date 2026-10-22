# Réplicas de C5/C1 — campaña 1-3-6 (spec aprobada por Tomás, 21/10/2026 23:00)

## Por qué
Análisis 13–21/10 (cuenta 1945796639629607):
- C5 Granza (MADRE): $54.246, 94 chats, **$577/chat**; 38 de cada 100 clics chatean.
- C1 Frente (MADRE): $9.441, 14 chats, $674/chat; 25 de cada 100.
- v2 Granza (TEST, código): $18.681, 7 chats, $2.669/chat; 12 de cada 100. Mismo CTR (2%) que C5.
- Diferencia clave: el texto de C5/C1 **pide un dato y deja la respuesta para el chat** ("Mandanos los m² y te calculamos cuánto necesitás"); el v2 daba la respuesta en el anuncio ("1 bolsa cubre 1 m² a 3 cm"). Además, placas estilo C5 (las retocadas de Tomás) vs. v2 de código, y el TEST le competía a la MADRE con el mismo público.
- Mensaje armado: no se ve por API en ninguno; no se toma como causa.

## Estado de la cuenta (21/10 23:00)
- MADRE 120250759505930411: **$9.000/día** (subida desde $7.000 el 21/10), C5 + C1. No se toca.
- Apagados el 21/10: v2 Granza y v2 Cuánta piedra (prendidos desde el 19/10), LAB Autoridad 120250880028210411 (desde el 20/10) y la campaña TEST v2 entera 120250865076760411. Conjunta Día de la Madre: pausada desde el 19/10.

## Qué se arma
- Campaña nueva **"Somos Piedra - Réplicas C5 1-3-6 - Oct 2026"**, CBO **$24.000/día**, mensajes a WhatsApp 299 459-0936. Total cuenta: **$33.000/día** desde el 22/10.
- 3 conjuntos, mismo público que la MADRE ("Toda la zona - abierto"), 6 carruseles cada uno (18):
  - **A Jardín (copia de C5):** patio con granza, entrada de auto, borde de pileta, canteros, "sin barro con perros y chicos", sendero.
  - **B Revestimiento (copia de C1):** cuánto sale el frente, quincho, pared del living, hogar, medianera, local comercial.
  - **C Pisos de afuera:** vereda de pórfido, entrada, patio, borde de pileta, escalones, adoquín.
- Cada carrusel = copia exacta de la fórmula C5: 6 tarjetas paso a paso, orden fijo (apagar "mejor rendimiento primero"), texto principal que **pide un dato sin dar la respuesta**, cierre a WhatsApp, mensaje armado distinto por carrusel (para saber de cuál vino el chat).
- **Fotos: solo reales** (IG, FB, catálogo y las placas de C5/C1), repartidas entre los 18 carruseles. Nada de IA en la piedra.
- Todo en **HTML → PNG 1080×1080**, con un sistema (plantilla + datos por carrusel), tests de calidad automáticos (texto legible, sin desbordes, contraste, máx. 8 palabras grandes, nada sin confirmar) y **3 o 4 vueltas** de revisión antes de entregar.
- Referencia visual: `E:\anuncios somos piedra\nuevooss\_subir\c5-01..06.jpg` y `c1-01..06.png`.
- Datos sin confirmar con Fran (precios, envío a Añelo, etc.): no van.

## Regla de corte (aprobada)
- Apagar una pieza si gastó **$3.000 sin chat**, o si pasa **$900 por chat con $5.000 gastados**.
- No decidir por ángulo con menos de $5.000 por pieza (aprendizaje del juez de Somos iPhone).
- MADRE: si pasa ~$800/chat dos días seguidos, vuelve a $7.000.

## Pendiente
- Saldo: ~$99.000 para 3 días a $33.000 (+ impuestos) — Tomás.
- Subida: placas a URL pública (Higgsfield) + `ads_create_ad` con object_story_spec inline (ver bitácora 19/10). Activar con OK de Tomás.
