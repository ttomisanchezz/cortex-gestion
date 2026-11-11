# Pendientes cerrados
Lo que se cerró de `pendientes.md`, en la misma sección, con la fecha. No se borra nada.

## Ibero (`ibero`)
- [x] Especificación v1 aprobada — 08/10
- [x] v1 construida en ramas paralelas e integrada en `main` (269 tests, e2e en verde) — 08/10
- [x] Ajustes de plata: IVA a favor aparte, merma y arqueo restan, comisión solo en MP y Posnet (275 tests) — 08/10

## Somos Piedra (`somos-piedra`)
- [x] (hecho 30/10: 15 escenas, fidelidad buena) Probar generación de carruseles con la API de Higgsfield — Tomás — desde 15/10
- [x] **Lanzar los carruseles:** Tomás sube las 24 placas de `E:\anuncios somos piedra\nuevooss` a la cuenta 2044879766141120; Claude las revisa antes (color de la piedra, sin precio ni "envío gratis", falta la placa 6 de c3), arma los 4 anuncios en el conjunto "Toda la zona - abierto" (identidad = la página, no @somosiphone_nqn), borra el anuncio vacío y publica con el OK de Tomás — Tomás / Claude — desde 12/10 → hecho el 13/10: publicada en la cuenta 1945796639629607, $10.000/día
- [x] **Antes de pautar:** cuenta publicitaria con tarjeta en la página "Somos Piedra, elija piedra" (https://www.facebook.com/profile.php?id=61589214484295), vincular @somospiedranqn y el WhatsApp Business 299 459-0936 (mensaje fuera de horario, etiqueta "anuncio"), píxel de Meta y etiqueta de Google en la web, perfil de Google (categoría, fotos, productos, horario) — Tomás — desde 09/10 → 12/10: tarjeta cargada en la cuenta 2044879766141120 y WhatsApp conectado a la página; lo que falta pasó a un pendiente nuevo
- [x] **Lista de precios** de Somos Piedra, para completar las etiquetas "Desde $__ el m²" de los 4 carruseles y la carga de productos — Tomás — desde 09/10 → 09/10: Fran no quiere precios en los anuncios; etiqueta "Consultá precio"
- [x] Spec v1.1 (solo piedras, con y sin factura, IVA al día, empleados, corte inicial) aprobada por Tomás — 09/10
- [x] Preguntas para la v1.1 (titular y CUIT, tres formas de precio, empleados) — 09/10
- [x] **Generar los carruseles 1, 2, 3 y 5** con código sobre las fotos del IG (1080×1080, etiqueta "Desde $__ el m²" vacía, entrega en el chat). Detalle en `clientes/somos-piedra/pauta-piedra.md` §7 a §9 — Claude, chat nuevo — desde 09/10 → hechos el 09/10 (`clientes/somos-piedra/carruseles/`, un .zip por carrusel)
- [x] Confirmar con Fran: precios "desde" por m² y del bolsón de granza; % en efectivo; si el envío se cobra y si llega a Añelo; cuotas sin interés o no; cuánto cubre una bolsa de granza — Tomás — desde 09/10 → respondido el 09/10 (README, "Respuestas de Fran"); los precios llegan con la lista
- [x] Confirmar si "Vivero Somos Piedra" de Cinco Saltos (@viverosomospiedra, San Lorenzo y Güemes, WhatsApp 299 463-7323) es la misma empresa. Hasta entonces no se usan sus fotos — Tomás — desde 09/10 → 09/10: es el vivero del papá de Fran, negocio aparte; no se usa
- [x] **Pauta:** confirmar si la página FB "SomosPiedraoficial" y el IG @viverosomospiedra son de ellos, y si las fotos de la web son de obras propias; si el artifact dice "la gestión la hace Tomás, sin cargo"; precio "desde" por m² (opcional) — Tomás / dueño — desde 09/10 → 09/10: la página es "Somos Piedra, elija piedra" (id 61589214484295); @viverosomospiedra queda afuera; fotos de la web: algunas propias y otras de Google
- [x] Investigación del rubro con dos agentes en paralelo (`claude/investigacion-piedra.md`) — 08/10
- [x] Preguntas hasta el 90%: 5 rondas, con las respuestas en `clientes/somos-piedra/README.md` — 08/10
- [x] Spec v1 (`claude/spec-piedra-v1.md`), aprobada por Tomás — 08/10
- [x] Prompts de la construcción: ramas unidades, importador, medios, dolares, cheques y servicios, en la corrida 2026-10-08a — 08/10
- [x] Datos del cliente: nombre legal, zona, condición fiscal, quién carga y cómo vende hoy — 08/10

## Sistema multi-negocio (`producto`)
- [x] Prompt de VS Code con el arreglo (a): hecho en la base de la corrida 2026-10-09a (septiembre de Piedra $583.875,20) — 09/10
- [x] Preguntas del diseño:
  - un dueño por negocio;
  - usuario de soporte de Tomás;
  - alta a mano;
  - marca por cliente;
  - un dominio por cliente.

  — 08/10
- [x] Diseño multi-negocio leyendo `E:\vivero` (`contexto/multinegocio.md`, commit `d15851d`) y corrida 2026-10-08a lanzada — 08/10

## 1. Sistema multi-negocio (`producto`)
- [x] (09/10) **Corrida 2026-10-08a en curso** (lanzada el 08/10 a las 17:48; 9 sesiones; diseño en `E:\vivero\contexto\multinegocio.md`).
  - Cuando termine, pegar en un chat nuevo de `producto` el PARA COPIAR Y PEGAR de la integración (o el de la base si no dio la señal).
  - Claude verifica las cuentas a mano, lee `REVISAR.md` y trae las decisiones de plata con su recomendación.
  - Tomás / Claude — desde 08/10

- [x] (hecho 30/10: TEST REELS armada y prendida a $16.000/día, TEST 1-3-6 apagado) **Reels del 28/10:** subirlos a `E:\anuncios somos piedra\reels-2026-10-28\`; Claude arma la campaña de test (CBO $4.900/día, un mensaje armado por reel) y, con el OK de Tomás, la prende y apaga el TEST 1-3-6 (T1 Granza). La MADRE no se toca — Tomás / Claude — desde 29/10

## 2. Somos Piedra (`somos-piedra`)
- [x] **Erasmo a tester (chat nuevo con `E:\bot-piedra`):** pasar al cotizador los precios del panel (36 productos + granza); modo que conteste solo al 299 429-5806; conectar cerebro ↔ cotizador; permitir mandar archivos (catálogo PDF, fotos de anuncios, PDF de cotización, simulador); seguimiento «volver a contactar el día X»; escalar al grupo «Bot Erasmo»; logs para iterar — Claude — desde 09/11 — cerrado 10/11: tester andando, precios del panel, cotizador, catálogo y escalado (falta fotos y PDF de cotización: pendientes aparte)
- [x] 09/11 Volver a adjuntar el Excel «día a día» para contar las ventas cargadas — Tomás — desde 09/11
- [x] 09/11 Cortar carruseles V1 flojos el viernes 6/11 si siguen > $1.200/conv — Claude — desde 04/11

- [x] **Cyber Monday — seguimiento:** revisar mar 3/11 (< $500/chat +25%; > $900/chat −25%) y los 6 anuncios en revisión; campaña 120251071669960411, IDs en `contenido\cyber-2026\meta-campana.md` — Claude — desde 02/11 — cerrado 02/11: los 16 anuncios salieron; Tomás decidió no aplicar la regla ±25%
- [x] **Publicar los carruseles Cyber A–F en orgánico** FB + IG (`contenido\cyber-2026\`) — Claude — desde 02/11 — cerrado 02/11: A publicado; D 2/11 20:30, B 3/11 11:00, E 3/11 19:00, F 4/11 11:00, C 4/11 18:00 (FB + IG)
- [x] Crear el proyecto de ChatGPT «Somos Piedra · escenas» (instrucciones + fuentes de `contenido\chatgpt-proyecto\`) — Tomás — desde 02/11 — hecho 02/11
- [x] Generar las 2 escenas del 02/11 (frente ocre / verde bronce) y rearmar la portada del carrusel A — Tomás + chat — desde 02/11 — hecho 02/11
- [x] Reemplazar `ideas-dia\armar_dia.py` por la versión con escenas (`2026-10-31\armar_dia_ia.py`) — chat — desde 02/11 — hecho 02/11


## Somos Piedra (`somos-piedra`) — cerrados 02/11
- [x] **Cyber Monday (2 al 4/11):** terminar 3–5 carruseles más con la dinámica del A + 2 reels ganadores con cinta; crear campaña «Cyber Monday» $20.000/día (sug. $15.000 prospección + $5.000 retargeting) hasta 4/11 23:59 con OK de Tomás; publicar en orgánico. Oferta: 20% OFF desde 2 m²; bolsón granza $20.000 (antes $27.000). Archivos en `contenido\cyber-2026\` — Claude/Tomás — desde 02/11 — hecho 02/11: carruseles D, E, F + reels L1-R1/L2-C1 con cinta; campaña Cyber activa a $20.000/día

## Somos Piedra (05/11)
- [x] 05/11 Decidir si los 6 carruseles van a TEST CREATIVOS — van a $1.600 c/u desde el 05/11
- [x] 05/11 Videos de entregas nuevos → test — R5 y R6 en TEST CREATIVOS

## Somos Piedra (`somos-piedra`) — cerrados 06/11
- [x] **Panel — corrida 2026-11-02a (rediseño visual Mostrador):** pegar el PARA COPIAR de la integración; Claude revisa capturas (`capturas\2026-11-02a\final\`) y REVISAR; después, deploy — Tomás/Claude — desde 02/11 — cerrado 06/11 (rediseño aprobado por Tomás; el script ya está commiteado en a0e9fba)
- [x] Panel: commitear `scripts/cambiar-dueno.mjs` y `CAMBIAR-DUENO.cmd` en `E:\somos-piedra-panel` después de la integración — Claude — desde 02/11 — cerrado 06/11 (rediseño aprobado por Tomás; el script ya está commiteado en a0e9fba)


## 2. Somos Piedra (`somos-piedra`) — cerrados el 09/11 (tarde)
- [x] Crear el grupo de WhatsApp «Bot Erasmo» con el número del bot, y dejar `Catalogo-Somos-Piedra-2026_3.pdf` en `E:\bot-piedra` — Tomás — desde 09/11 — hecho 09/11
- [x] Crearle un mail a Erasmo para darle usuario en el panel — Tomás — desde 09/11 — hecho 09/11
- [x] Lectura de 14 días por anuncio: ganador de carruseles y de reels → variaciones (estilo N1 «¿Tu entrada es de tierra?») — Claude — desde 09/11 — hecho 09/11
- [x] Correr `PROMPT-vscode-2026-11-09a-reels-codigo.md` (3 reels 100 % código, voz jIgvw3W75cbd6IP0JYwL) en VS Code con Sonnet 5.5 — Tomás — desde 09/11 — hecho 09/11

- [x] Rehacer carruseles con fotos IA: N4–N6 rehechos y subidos al test (09/11)
- [x] **Mañana 10/11 — escalar:** Tomás confirma número y saldo → crear ESCALA (CBO) con L1-R1 y L2-C1 Envío Neuquén y C1 Frente; subir N1–N3 + reels + carruseles nuevos al test; MADRE no se toca — Tomás → Claude — desde 09/11 — hecho el 09/11, programado para el 10/11 00:00
- [x] **Erasmo: reiniciar y testear las reglas de setter** («caro», «lo pienso», preguntas de la obra) desde el tester 298 440-9447 (Browser 3) — Tomás reinicia, Claude testea — desde 10/11 — cerrado 11/11

## 2. Somos Piedra (`somos-piedra`) — cerrados el 11/11 (pauta)
- [x] **Correr `E:\anuncios somos piedra\reels\PROMPT-vscode-2026-11-09b-voz-nueva-10-reels.md`** en VS Code (Sonnet 5.5): voz LZj1dIzYRl9rc9TIXnMt más rápida, regenera los 3 reels con código y hace 10 nuevos (lote-2026-11-10) — Tomás — desde 09/11 — cerrado 11/11
- [x] Revisar los 13 reels de la 09b y programar el orgánico IG+FB, uno por día — Claude — desde 09/11 — cerrado 11/11
- [x] 10/11 a la mañana: leer el arranque de ESCALA (CBO $30.000: L1-R1, L2-C1, L3-V3) y N1–N6 en el test, y aplicar reglas de corte — Claude — desde 09/11 — cerrado 11/11
- [x] Revisar los 13 reels de la 09b (YA ESTÁN: 01/03/08 en `reels\lote-2026-11-07`, 11–20 en `reels\lote-2026-11-10`; palabras dudosas en el REVISAR), subir los aprobados al test y programar orgánico IG+FB, uno por día — Claude + Tomás — desde 09/11 — cerrado 11/11
- [x] **Correr `E:\anuncios somos piedra\reels\PROMPT-vscode-2026-11-10a-variaciones-granza.md`** (14 reels: 8 de granza + 2 de R08, R13, R14) en VS Code, carpeta `editor-reels-tomas`, Sonnet 5.5 — Tomás — desde 11/11 — cerrado 11/11
