# Pendientes
Lista viva, ordenada por la prioridad de `proyectos.json`.
- La actualiza el comando `cierre`.
- Formato: `- [ ] qué — quién — desde DD/MM`.
- Acá va solo lo abierto. Lo cerrado se mueve a `pendientes-archivo.md`.

## 1. Sistema multi-negocio (`producto`)
- [ ] **Decisiones de plata de la corrida 2026-10-08a** (recomendación de Claude entre paréntesis; detalle en `bitacora/2026-10-09/producto.md` y `E:\vivero\REVISAR.md` §4 y §8) — Tomás / contador — desde 09/10
  1. ~~El crédito de IVA de las facturas A pesa dos veces~~ **Hecho el 09/10** (base de la corrida 2026-10-09a: septiembre de Piedra $583.875,20, verificado a mano).
  2. Una venta sin factura deja el IVA en $0 (e2e de Piedra: +$963.854,55 con IVA $0). **Cambió el 09/10:** Somos Piedra vende sin factura a propósito, así que la venta marca "con factura" o "sin factura". Sin factura → sin débito (correcto). Con factura pero todavía sin emitir → FALTA DATO. Ya está en el método §3.8.
  3. El sobrante del arqueo en dólares (que sume, igual que en pesos).
  4. Anular una venta con la factura pendiente (configurar ARCA antes de cargar las alícuotas, y poder descartar con nota una factura pendiente sin CAE).
  5. La factura en PDF con medios (una línea aparte de recargo o descuento; confirma el contador).
  6. Lo vendido antes de cargar los medios (aceptar FALTA DATO y cargar los medios antes de la primera venta real).
  7. El cobro posterior de una deuda (a precio de lista, sin el % del medio).
  - No son de plata: `devuelto` derivado (sin migración); cheques: vuelto no, editar datos no monetarios con nota sí, cobrar deuda con cheque más adelante; `activo = false` = solo lectura.
- [ ] Borrar a mano las carpetas vacías de `E:\vivero\.wt\` al cerrar las sesiones de VS Code de las ramas — Tomás — desde 09/10
- [ ] De la integración (`REVISAR.md` §8): CUIT de cada negocio en `negocios/*.json`, `VITE_SUPABASE_URL` y `VITE_SUPABASE_ANON_KEY` también para las funciones en Vercel, sacar `VITE_LOGIN_EMAIL` de `.env.example` — Tomás — desde 09/10
- [ ] Logos y colores de cada cliente (hoy `FALTA DATO`: la app usa un ícono con la inicial y la paleta neutra). Van en `public/marcas/<slug>/` y en `negocios.marca` — Tomás / clientes — desde 08/10
- [ ] Hosting: Vercel Pro u otro con funciones Node (Vercel Hobby no permite uso comercial). Como va un dominio por cliente, tiene que aceptar dominios propios — Tomás — desde 08/10
- [ ] Supabase: crear el proyecto único del sistema. Al crearlo, `npm run db:migrate` aplica 0001–0060 (incluidas 0050 y 0060 de la corrida 2026-10-09a) antes de que un teléfono confirme un corte — Tomás — desde 08/10
- [ ] Nombre y carpeta definitivos del repo (hoy `E:\vivero`; por ejemplo `E:\sistema-gestion`). Renombrar después de la corrida, sin sesiones corriendo — Tomás decide — desde 08/10
- [ ] Precio del abono — Tomás — desde 08/10
- [ ] Dominios, uno por cliente: quién los compra y quién los paga (el cliente, o Tomás dentro del abono) — Tomás — desde 08/10
- [ ] Avisarle a cada cliente que Tomás tiene un usuario de soporte que entra a su negocio. Va en los términos y en la política de privacidad — Tomás — desde 08/10
- [ ] Cobro del abono (transferencia o Mercado Pago Suscripciones), nombre comercial del sistema y borradores legales — Tomás — desde 08/10
- [ ] Decidir si Números estima los Ingresos Brutos como el IVA. Hoy se cargan como gasto cuando se pagan; en Somos Piedra son 5% minorista, o 2% con la escala de microempresa — Tomás — desde 08/10

## 2. Somos Piedra (`somos-piedra`)

### Cotizaciones en PDF (desde 18/11)
- [ ] Confirmar el dígito verificador del CUIT de la razón social (20-45734050-9) — Tomás — desde 18/11
- [ ] «Precio final» en la 0002 y 0003: ¿IVA incluido? ¿La granza va también en bolsas? — Tomás — desde 18/11
- [ ] Cotización 0003 (piedra ocre $250.000): ¿El Sauce o sin cliente? — Tomás — desde 18/11

### Erasmo — para salir a todos (desde 17/11 noche)
- [ ] **Mirar Erasmo en vivo a la mañana** (`E:\bot-piedra\data\consola.log`): que los chats nuevos los atienda Sonnet (`chat nuevo, lo atiende Sonnet`), ninguno en sombra, y la primera transcripción de audio (si Gemini da error, crear una key nueva en AI Studio y cambiar `GEMINI_API_KEY`) — Claude, desde 18/11
- [ ] Crédito de Gemini (AI Studio, tomassanchez2018): USD 3,81 al 18/11; cargar USD 10 con recarga automática y tope mensual, o mirar Usage el viernes — Tomás, desde 18/11
- [ ] Rotar la key de OpenAI del `.env` de Erasmo si la captura del 18/11 (se ven los primeros caracteres) quedó en algún lado — Tomás, desde 18/11
- [ ] Recarga automática en la Console (o confirmar de qué cuenta es la `ANTHROPIC_API_KEY` de Erasmo y si Chiara gasta de ahí); con todos, ~US$12/día — Tomás, desde 17/11
- [ ] Número de Somos Piedra en `CONTACTOS_PERSONALES` de Chiara — Tomás, desde 17/11
- [ ] Fran confirma: localidades a $45.000 (General Roca quedó afuera), envío sin IVA aunque haya factura, ya no "pocas bolsas no se cobra" — Fran, desde 17/11
- [ ] Fran: 12-14 bolsas de granza salen más caras que 15 (efectivo 13-14, tarjeta 12-14) — Fran, desde 17/11
- [ ] Push: `cd E:\bot-piedra; git push -u origin piedra/archivos-excluidos` (hasta `d19e0b7`, el arreglo de `nuevos` del 18/11) — Tomás, desde 17/11
- [ ] `CEREBRO_USD_CACHE_LEIDA` por defecto 0,20 y es 0,10 (el gasto estimado sale inflado) — Claude, desde 17/11
- [ ] Cruce WhatsApp del Excel → chat de Erasmo → anuncio → venta: falta el Excel en `E:\somos-piedra-panel\datos\dia-a-dia\` — Tomás/Claude, desde 17/11
- [ ] Borrar los 2 mensajes de prueba mandados por error al grupo UN MOSTACHOW (17/11 17:09) — Tomás, desde 17/11
- [x] CBO «IA – Nov 2026» a $20.000/día publicada el 17/11 (64 Veo, 66 IA, 67 IA, 76 sin rótulo; un mensaje precargado por anuncio) — ver `clientes/somos-piedra/pauta-piedra.md`
- [ ] Leer la CBO IA a las 48-72 h y pasar el ganador a la ESCALA — Claude — desde 17/11
- [ ] **Reconectar Erasmo:** correr `powershell -ExecutionPolicy Bypass -File E:\bot-piedra\conectar-piedra.ps1` con el celu de Somos Piedra a mano y escanear el QR (Dispositivos vinculados) dentro de los 6 min; NO correr otro `npm start` (el bot ya corre) — Tomás — desde 17/11
- [ ] Push de `E:\bot-piedra`: `cd E:\bot-piedra; git push -u origin piedra/archivos-excluidos` (la rama no está en GitHub) — Tomás — desde 17/11
- [ ] Revisar la corrida 2026-11-17a de Erasmo (`cea7308`, REVISAR.md) y el `package-lock.json` que modificó `npm install` de `conectar-piedra.ps1` (sacó 26 paquetes): no commitearlo hasta revisarlo — Claude — desde 17/11
- [ ] **Corrida 2026-11-17b (Excel → panel):** Tomás pone el Excel más nuevo (Drive del papá de Fran) en `E:\somos-piedra-panel\datos\dia-a-dia\`, cierra las sesiones de la 17b que quedaron esperando y relanza las 7 (`prompts\2026-11-17b\LANZAR.md`); Claude revisa la integración; Tomás corre `SUBIR-EXCEL.cmd` — Tomás → Claude — desde 17/11
- [ ] Excel: columna con el WhatsApp del cliente en las hojas de VENTAS, desde hoy (para el cruce anuncio → venta) — Tomás/Fran — desde 17/11
- [ ] Panel: apagar «Allow new users to sign up» en Supabase **`msanpdcnkroqczwosocr`** (no en appsomospiedra) — Tomás — desde 17/11
- [ ] Panel: commitear el `.gitignore` con `datos/` y `.vercel`; crear el repo en GitHub para poder hacer push — Claude/Tomás — desde 17/11
- [ ] Supabase Pro para el panel (el free se pausa a los 7 días sin uso) — Tomás decide — desde 17/11
- [ ] 76 sin rótulo para el orgánico: está en `editor-reels-tomas\.sesiones\2026-11-16d\piedra-ia-9a\trabajo\P76IA\reel-codigo.mp4` (no se entregó al lote) — Tomás — desde 17/11
- [ ] Rehacer las piezas JSON de los reels IA 77–81 (se perdieron al cortarse el puente) y el prompt de VS Code; tope USD 10 — Claude, después de que Tomás cargue USD 10 en APIMart — desde 17/11
- [ ] Cargar USD 10 en APIMart — Tomás — desde 17/11
- [ ] «Entrega lajas» (MADRE): revisar/descartar sus «Cambios sin publicar» y recién ahí sacar el mínimo de $3.500; mirar los 15 borradores de «Revisar y publicar» — Tomás — desde 17/11
- [x] 17/11 Avisarle a Fran: cada venta → `#vendido <número del cliente>` en el grupo «Bot Erasmo» (nunca en el chat del cliente) — Tomás — desde 17/11
- [ ] Cruce automático venta del panel (teléfono de «Vender») ↔ anuncio que guarda el bot → costo por venta por anuncio — Claude — desde 17/11
- [ ] Confirmar con Fran: «la piedra no se pinta más / aguanta helada y viento» (cierres de 78 y 81) y si la granza roja rinde 1 bolsa = 1 m² — Tomás — desde 17/11
- [x] 17/11 **Erasmo, corrida 2026-11-17a** (respuestas de Fran: pagos, IVA, tarjeta/posnet, bolsón, granza tarjeta 15-19, `#sinstock`, envíos): Tomás pega `E:\bot-piedra\bot\prompts\PROMPT-vscode-2026-11-17a-erasmo-fran.md` en VS Code; después Claude revisa REVISAR, reinicio en tester y prueba con el 298 440-9447 — Tomás / Claude — desde 17/11
- [ ] **Excel ↔ panel** (chat nuevo): diseñar la sincronización del Excel «día a día» (Drive del papá de Fran) con el panel: LISTADO + ventas, gastos, proveedores y gastos fijos desde 01/2025, alias de productos (~20 por producto), sin duplicados entre Excel y panel; después prompts de VS Code — Claude — desde 17/11
- [ ] Instalar Google Drive para escritorio con la cuenta del papá de Fran en la PC del local y mover ahí el Excel «día a día» — Tomás — desde 17/11
- [ ] Mudar Erasmo a la PC del local (Docker Desktop, Node 22, Git, Drive; QR de nuevo) cuando esté todo listo — Tomás / Claude — desde 17/11
- [ ] Panel: «Envío» y «Flete paletizado» sin precio (el envío depende de la zona y el flete se cotiza aparte): decidir si se sacan como producto — Claude / Tomás — desde 17/11
- [ ] 19/11 15:17: tarea programada trig_01Fc8bUSDdz97ibDzboaEQPD programa los 14 reels de la 11e del 11 al 17/12 con texto; revisar el resultado — Claude — desde 12/11
- [x] 13/11 23:40 Primera lectura de R61–R65, ESCALA R13 y R21–R34: día $918/conv, sin pausas (R21–R34 llevan 2 días). Detalle en la bitácora del 13/11 — Claude
- [ ] 14/11 noche: cortar los R21–R34 con 3 días > $1.200/conv (candidatos R22, R24, R25, R28, R29, R30, R33, R34; al límite R26 y R32) y segunda lectura de R61–R65 — Claude — desde 13/11
- [x] 12/11 23:40 lectura nocturna hecha (bitácora 12/11): día $89.645 / 93 = $964/conv; no se pausó nada (R08, R11, R13, R14 bajo $1.200 con 3 días) — Claude — 12/11
- [x] 14/11 Escalón aplicado con OK de Tomás: ESCALA 120251195297760411 $36.000 → $43.200/día (total ~$115.000/día). El pago todavía no se hizo porque no se llegó al límite de facturación — Tomás / Claude
- [x] 13/11 ESCALA Granza R21 + R27 día 1: $1.760 / 3 = $587 (C5 estaba en $1.651), solo 5% de la ESCALA; MADRE sin C5 $961/conv — Claude
- [x] 11/11 Los 14 reels del `lote-2026-11-11` (R21–R34) subidos a TEST CREATIVOS: un conjunto por reel a $1.600/día, inicio 12/11 00:00, textos del REVISAR, tapa = cuadro del segundo 1. Verificado por Graph: 14 conjuntos y 14 anuncios ACTIVE — Claude
- [ ] **Meta, cobros de la tarjeta (vigilar):** el 11/11 09:56 Tomás pagó $69.056,35 (figura «Pagado») y la cuenta 1945796639629607 volvió a estado activo tras ~1 h 40 sin entregar (08:15–09:56). A las 10:02 el «saldo pendiente» era $59.008,30, sin pago atrasado pero arriba del umbral de cobro automático ($52.194): si la Mastercard ···· 6432 vuelve a rechazar (el 10/11 rechazó $52.194 una vez y $17.176,51 dos veces), se corta de nuevo. Ver con el banco el límite, o sumar un segundo método de pago — Tomás — desde 11/11
- [x] 12/11 Lectura del 11/11 hecha (bitácora 12/11): pausados N1, N3, R16, R18, VG3-H1; R13 califica para la ESCALA; día $86.560 / 81 = $1.069/conv. Antes: juzgar N1, N3, N6, R16, R18, R19, VG3-H1 (0 conv), R13, N5, R17 y la ESCALA con R11, R08, R14; ESCALA +20% solo si el día cierra < $1.200/conv (sin pedir OK) — Claude — desde 11/11
- [ ] Decidir: ¿la regla de corte juzga todo recién con $3.000 de gasto? (hoy 1 conv cara se corta antes que 0 conv) — Tomás — desde 11/11
- [ ] Decidir si quiere un tope real de gasto: Meta gasta hasta +75% sobre el diario en un día (10/11: $138.231 con $109.000 programados) — Tomás — desde 11/11
- [ ] Pasar las ventas de noviembre para la primera tasa de cierre (chats de Meta contra ventas) — Tomás — desde 10/11
- [ ] Cargar en el panel cada cotización y cada venta con monto y con el teléfono del cliente (obligatorio desde el 11/11) (hoy 1 venta y 0 cotizaciones) — Fran — desde 10/11
- [x] 11/11 Orgánico: 27 reels con código programados en FB + IG, uno por día a las 20:30 del 11/11 al 7/12 (verificado en Programadas: 68 filas = 34 publicaciones × 2). El calendario NO estaba vacío: ya había 7 piezas del 11 al 14/11 (10:30 y 13:30) y el extra del 13/11 10:30 sigue — Claude
- [x] 11/11 Piezas de siempre del 15 al 21/11 programadas en FB + IG: carrusel 10:30 (N3, N5, N1, N2, N6, A «¿Ocre o verde bronce?», N4) y placa de datos con código 13:30 (P1–P7, `contenido\semana-15-11\`). Verificado en Programadas (94 filas = 47 × 2) — Claude
- [x] **Añelo (Tomás aprobó lo recomendado el 11/11):** orgánico limpio (pies del 12–21/11, P6, N2, N4, N6, reels R17, R19, R01, R27 y el R20 del 7/12 cambiado por R11 sin Añelo) y R11 (TEST + ESCALA), R17 y R27 (TEST) de vuelta en la pauta con videos sin Añelo. Detalle en la bitácora 11/11 16:45–20:10 — Claude — 11/11
- [ ] Lectura del 12/11 (próxima): N6 ($2.981 / 0) y R19 ($2.904 / 0) tienen el anuncio pausado por Añelo; si vuelven, se cortan al pasar $3.000. Sumar los 4 anuncios sin Añelo (R11 TEST y ESCALA, R17 y R27 TEST; arrancaron 11/11 ~19:45, en revisión) a las reglas de corte — Claude — desde 11/11
- [x] Videos reales Envío Neuquén / Entrega: se dejan como están (Tomás, 11/11 22:49). Antes: ¿dicen Añelo en el audio? — Tomás — desde 11/11
- [x] N2, N4 y N6 (18, 19 y 21/11) se quedan como están (Tomás, 11/11 22:49).  Antes: ¿se quedan así o se cambian? Traen personas/manos en fotos de IA, cartel de obra ajeno (N6-02), pantalla de WhatsApp imitada y «En pocos días» (N2-04, plazo no confirmado) — Tomás — desde 11/11
- [ ] Escuchar las voces nuevas: R11, R17 y R27 sin Añelo ya corren en pauta; los 14 del lote 13 antes del 26/11 — Tomás — desde 11/11
- [x] El R20 repetido del 7/12 20:30 se cambió por el R11 sin Añelo (11/11) — Claude
- [ ] **Orgánico: 2 reels por día como mínimo (pedido de Tomás, 11/11 14:16).** Cubierto con texto hasta el 9/12 (18:00) y el 7/12 (20:30), verificado en Programadas el 12/11. Para seguir: los 18 de la corrida 11e (61–75 + 42, 42b y 42c) alcanzan del 8/12 al 17/12 si Tomás los manda al orgánico. Carrusel y placa: programados hasta el 28/11 — Claude programa cuando haya material — desde 11/11
- [x] 12/11 (Tomás aprobó lo recomendado) Mirar los 18 reels de la corrida 11e (`reels\lote-2026-11-14\` y `reels\sin-anelo-2026-11-11\42-pedilo-en-tres-mensajes\`) y escuchar: 42b (1,2 s, ¿«te lleva a tres»?), 64 (4,4 s, «Es para donde se pisa»), 70 («este») y 71 (los primeros 2 s, «lavandina»). En el 62, la franja CLAROS es la foto ocre5_2: si no es «claro», se cambia — Tomás — desde 12/11
- [x] 12/11 61–65 al TEST desde el 13/11; los 18 al orgánico 8–17/12 (4 programados, 14 el 19/11). Decidir qué de la 11e va a la pauta (TEST CREATIVOS a $1.600 c/u) y si los 18 van al orgánico desde el 8/12 (2 por día hasta el 17/12). Ojo: el 72 se parece al 35c y el 73 al 19 (no ponerlos en el mismo conjunto ni seguidos). Textos de anuncio y de orgánico en `REVISAR-codigo-2026-11-11e-a|b|c.md` — Tomás — desde 12/11
- [ ] **Reels con código, lote 35–46 (corrida `2026-11-11c`):** Tomás aprobó el lote el 11/11 12:04. Prompt listo en `E:\anuncios somos piedra\reels\PROMPT-vscode-2026-11-11c-formatos-nuevos.md` (12 reels + 6 arranques alternativos = 18 videos; salida en `reels\lote-2026-11-12\`; ~4.700 caracteres de ElevenLabs). Falta: que Tomás lo corra en VS Code, revisar el REVISAR y los videos, y decidir cuántos suben al test (+$1.600/día cada uno: 12 = +$19.200, 18 = +$28.800) — Tomás corre, Claude revisa — desde 11/11
- [ ] **Piezas de siempre desde el dom 22/11:** el carrusel/placa llega hasta el sáb 21/11 13:30 (los reels de las 20:30 siguen hasta el 7/12). Ya no quedan carruseles aprobados sin publicar: hay que armar nuevos con `plantillas.py` (fotos nuevas por ChatGPT) y otra tanda de placas con `semana-15-11\gen.py` — Claude arma, Tomás elige — desde 11/11
- [ ] El sáb 14/11 10:30 no tiene carrusel programado (ese día solo sale la placa de las 13:30 y el reel) — Tomás decide si se suma — desde 11/11
- [x] 11/11 Borrada `E:\anuncios somos piedra\reels\_subida-2026-11-11` (partes y copias de la subida, 275 MB). El calendario con los textos quedó en `reels\lote-2026-11-11\organico-programado-2026-11-11.json` — Claude
- [ ] Orgánico de los 13 reels de la 09b: el REVISAR de la 09b no traía texto para orgánico; se usó el texto del anuncio que ya corre + 4 hashtags. Si Tomás quiere otro texto, se edita en Programadas antes de que salgan — Tomás — desde 11/11
- [x] 12/11 10:00 hecho: ESCALA $36.000 y ESCALA R13 (120251245765800411). **Confirmar (frenado por el control de permisos el 12/11 00:05):** (1) ESCALA +20% $30.000 → $36.000 (el 11/11 cerró $1.069/conv; gasto programado pasa de ~$95.400 a ~$101.400/día); (2) R13 Adoquín entrada a la ESCALA con el mismo post ($458/conv en 10–11/11). Con el OK, Claude lo hace por Graph — Tomás — desde 12/11
- [x] 13/11 MADRE + ESCALA en una CBO: recomendado no por ahora (MADRE $961, ESCALA $706 el 13/11; reinicia aprendizaje) — Claude
- [ ] **Error de Claude (10/11):** 8 mensajes de prueba salieron al grupo de WhatsApp «vibes a coding»; decidir si se eliminan — Tomás — desde 11/11
- [x] 11/11 Granza: Tomás decidió $310.000 por 20 m² en efectivo y $26.500 por 1 m² con tarjeta; Erasmo ya lo tiene (commit `eefad6a`) — Tomás / Claude
- [ ] **Granza en el panel (Tomás 12/11: no se cambia el precio por ahora):** los 3 productos de granza siguen con los precios viejos (lista de 1 a 9 bolsas $27.000; 20 o más $15.000 en efectivo). Pasarlos a $26.500 y $15.500 para que el panel y Erasmo digan lo mismo — Fran lo edita en el panel, o Claude con el OK de Tomás — desde 11/11
- [x] 11/11 Erasmo con `082f0b3` probado en vivo: el seguimiento queda anotado (26/11 para «en 15 días arranco»; causa confirmada: la herramienta venía junto con la respuesta y se descartaba) y la repetición textual de la pregunta ya no sale — Claude
- [x] 11/11 Erasmo con `3956ef9` probado en vivo (reiniciado 13:01): tras «se puede pagar en cuotas?», «y con factura?» y «ah ok, gracias» no repitió ni rehízo ninguna pregunta (una corrida). Si reaparece en el borrador: vuelta de corrección cuando la pregunta nueva se parece a una hecha — Claude
- [x] 17/11 (contestado: Verde Bronce Irregular $30.000 OK; tarjeta granza 15-19 $19.000; sin stock con `#sinstock`) **Fran:** revisar los precios del panel (Verde Bronce a $35.000 en efectivo y su precio con tarjeta) y pasar el precio con tarjeta de la granza de 15 a 19 bolsas; cómo avisamos cuando falta un color de granza (hoy la roja) — Fran — desde 16/11
- [x] 16/11 Erasmo "Enseguida te respondemos." al escalar (5720211)
- [x] 16/11 (probado con el 298 440-9447, todo OK) Reiniciar Erasmo en modo tester (CEREBRO_MODO=tester) y probar los cambios del 16/11; después decidir pilotos — Tomás / Claude — desde 16/11
- [ ] Push de E:\\bot-piedra (piedra/archivos-excluidos hasta 5720211) — Tomás — desde 16/11
- [x] 16/11 Sombra revisada (ver bitácora 16/11). Nuevos pendientes: anuncio → producto (precio de entrada como Fran), «4 cuadrados» ≠ 40 m², precio de 1 bolsa, y decisiones: bolsón $310.000 sí/no, Verde Bronce panel $30.000 vs Fran $29.000, colores de granza en stock, mensaje al escalar, tope de gasto (US$ 60–100/mes) — Claude / Tomás / Fran
- [x] (cerrado 16/11) **Erasmo en sombra hasta el 13/11** (prendido el 11/11 14:17; `/salud`: `cerebro.modo` sombra, `sombraPersona` activa hasta 2026-11-13, tope US$5/día). Claude arma el resumen del 12/11 y del 13/11 desde `data/aprendizaje-v2.jsonl`: lo que Erasmo hubiera contestado (`propuesta` y `propuesta-sonnet`) contra lo que contestó Fran (`humano`), con los casos donde se equivoca; mirar en especial «laja», la granza a los precios nuevos y si rehace preguntas. Después: decidir pilotos (frase de Tomás). Para volver a las pruebas con el tester: `CEREBRO_MODO=tester` y reiniciar — Claude / Tomás — desde 11/11
- [ ] **Planilla del local → app:** quedan dos preguntas de `claude/analisis-planilla-2026-11-11.md`: la mercadería de Cinco Saltos / Cipolletti (¿consignación?) y quién carga las ventas y desde qué día se corta la planilla; volver a pedir la planilla del 6-11, que llegó vacía. (La venta por anuncio quedó resuelta el 11/11: teléfono en Vender.) — Tomás — desde 11/11
- [ ] **Fran decide sobre Erasmo:** mensaje de espera al escalar (hoy silencio), recomendaciones por uso (frente/patio/pileta/quincho), si pregunta la variante (pizarra tiene 3), tramos de granza 1-9/10-19/20+, velocidad (60–90 s) — Fran — desde 10/11
- [ ] Reactivación de Erasmo como Chiara (2 mensajes al cliente que dejó de contestar sin comprar) — Claude, con OK de Tomás — desde 10/11
- [ ] Sumar el parche de Baileys (ack de <status>) a la imagen `evolution-api-baileys-fix`: hoy vive solo en el contenedor y se pierde si se recrea — Claude arma, Tomás corre — desde 10/11
- [ ] Push de `E:\bot-piedra` (rama `piedra/archivos-excluidos`, hasta `eefad6a`: reglas, buscador, diagnóstico, pregunta repetida, seguimiento, lista de preguntas hechas, laja y precios de granza) y de `E:\somos-piedra-panel` (`main`, hasta `08e953f`) — Tomás — desde 11/11
- [ ] Panel: deploy (`vercel --prod`) de `08e953f` (FALTA DATO en la lista y la ficha de Meta sin lectura de hoy; órdenes pendientes de más de 24 horas). Sin migración. No urge: no cambia nada hasta cargar `META_TOKEN` — Tomás dice cuándo — desde 11/11
- [ ] `reglas/cerebro-reglas-piedra.md` (aprobado 06/11) quedó desfasado de `src/cerebro-reglas.md` (el que usa el bot): decidir la fuente — Tomás — desde 10/11
- [x] 11/11 Panel: los cuatro e2e en verde sobre `b6cb9af` (corte 24 pasos, empleados 12, meta 11, piedra 40), en una copia de Linux desde el chat (`herramientas/e2e-panel-vm/`) — Claude
- [ ] Avisarle a Fran que Vender ahora pide el teléfono; probar una venta real con teléfono en producción — Tomás — desde 11/11
- [x] 11/11 «Laja» definida por Tomás: toda piedra que se puede abrir; la granza, la laca y las baldosas no. Erasmo ya lo aplica en el código y en las reglas (commit `53bf162`) — Tomás / Claude
- [x] 11/11 Erasmo corre `eefad6a` (reiniciado 14:05 y 14:17): laja y precios de granza cargados. No se probaron con el tester (la pestaña de WhatsApp estaba en otro chat y después pasó a sombra): se miran en las propuestas de la sombra, con clientes reales — Claude
- [ ] Confirmar si el Garden Block 35X35 cuenta como laja (Claude lo dejó afuera, junto con el envío y el flete) — Tomás / Fran — desde 11/11
- [ ] Fotos de productos por WhatsApp (hoy solo el catálogo PDF): decidir prioridad — Tomás — desde 10/11
- [ ] Push de la rama `voz/elevenlabs-2026-11-08b` del editor de reels — Tomás — desde 09/11
- [ ] Fran confirma los nombres y usos de las piedras de la página de guiones (pizarra, travertino, Zapala y Bariloche no figuran en el catálogo 2026) y graba las ideas ★ con los lentes — Fran — desde 09/11
- [ ] Panel: verificar que se corrió `SUBIR-COTIZACIONES.cmd` y que el sign-up está apagado (Tomás dijo el 09/11 que hizo sus pasos); darle empresa/rol al usuario de Erasmo — Claude — desde 09/11
- [ ] Cargar 299 459-0936 en `EMISORES` (`src/domain/presupuesto.ts`) del panel y confirmar que «Cotizaciones» aparece en el menú en línea — Claude — desde 09/11
- [ ] Monto de EPAS en gastos fijos (cargado sin monto) y los gastos fijos que faltan — Tomás — desde 09/11
- [ ] Confirmar que las piedras del LISTADO van por m² (Garden Block por unidad y laca por litro ya confirmados) — Tomás — desde 09/11
- [ ] Cargar saldo (≥ $500.000) o poner tarjeta con pago automático en la cuenta 1945796639629607: el 08/11 la entrega se cortó por saldo — Tomás — desde 09/11
- [ ] Hacer la verificación del anunciante que pide Meta — Tomás — desde 09/11
- [ ] Escalera de pauta: lun 9/11 $85.000 · mar $100.000 · mié $115.000 · jue $130.000 · vie $150.000; cada escalón solo si ayer < $1.200/conv y con el número confirmado por Tomás esa mañana; plata nueva a conjuntos nuevos (campaña ESCALA CBO + test), MADRE no se toca — Claude + Tomás — desde 09/11
- [ ] Subir N1, N2 y N3 (`E:\anuncios somos piedra\carruseles-2026-11-08\`) a TEST CREATIVOS a $1.600 c/u — Claude con OK — desde 09/11
- [ ] Escuchar las voces dudosas del lote 08b: 03 y 07 («metros»), 12 («placas») — Tomás — desde 09/11
- [ ] Grabar la lista de 10 tomas (barro → granza, entrega, depósito, frente, WhatsApp) — Tomás — desde 09/11
- [ ] OK de Fran sobre los 4 cuidados (agua y cepillo, sin ácido ni lavandina, manguera, rastrillo) para el reel 06 — Fran — desde 09/11
- [ ] Marca somospiedra del editor: licencia de la música copiada de metodoexpress y logo sin fondo — Tomás — desde 09/11
- [ ] Permisos para Claude: extensión en business.facebook.com (ver saldo) y la carpeta Descargas (imágenes de ChatGPT) — Tomás — desde 09/11
- [ ] Push opcional de la rama `voz/elevenlabs-2026-11-08b`: `git -C C:\Users\PC\Documents\editor-reels-tomas\.wt\voz-elevenlabs push -u origin voz/elevenlabs-2026-11-08b` — Tomás — desde 09/11
- [ ] Confirmar pausa de L2-C2 Local con stock y VG2 (bloqueada por permisos) — Tomás — desde 05/11
- [ ] Descartar borrador ad 120251127339370411 («Nuevo anuncio de Interacción» en S0) — Claude — desde 05/11
- [ ] Sáb 7/11: leer L3-V3 Entrega granza v2 — Claude — desde 05/11
- [ ] Lun 9/11: corte de S0–S5, R5, R6, VG3, VG4 + decidir C5 / «Toda la zona – abierto» — Claude + Tomás — desde 05/11
- [x] 05/11 Los 6 carruseles (S0–S5) programados en FB + IG: jue 5 19:30, vie 6 09:00, sáb 7 19:30, dom 8 09:00, lun 9 19:30, mar 10 09:00 — Claude
- [ ] Pasar ventas desde octubre (cantidad, $ y anuncio que trajo cada una) — Tomás — desde 04/11
- [ ] Costo por cliente + presupuesto semanal con las ventas — Claude — desde 04/11
- [ ] Revisar si la Madre mejoró tras subirla a $35.000 (4/11 16:10) — Claude — desde 04/11
- [ ] 5 variaciones de hook de L1-R1 Envío Neuquén — Claude — desde 04/11
- [ ] Fran graba 10 guiones (cuántas bolsas + precio a cámara) — Fran — desde 04/11
- [ ] Subir carruseles VG3/VG4/VF3/VF4 con presupuesto bajo — Claude — desde 04/11
- [ ] Descartar borrador viejo L3-V3 (ad 120251109138600411) — Claude — desde 04/11
- [ ] **Panel — subir rediseño + Cotizaciones:** Tomás hace doble clic en `E:\somos-piedra-panel\SUBIR-COTIZACIONES.cmd` (migra la 0072 y hace `vercel --prod`; si Vercel pide login, `npx vercel login`). Después Claude prueba en el celu y la compu. A Claude el control automático no lo dejó migrar la base real — Tomás — desde 06/11
- [ ] Cotizaciones: el WhatsApp del negocio para el PDF y confirmar validez (7 días) y forma de pago (transferencia o efectivo) por defecto; `npm test` en Windows (`marca/sin-logo` y `meta/prueba` no corren en la VM) — Tomás/Claude — desde 06/11
- [ ] Panel: arreglar las funciones de `api/` en Vercel (ERR_MODULE_NOT_FOUND: sin manifest ni ícono; la factura no anda) — Claude/VS Code — desde 02/11
- [ ] Panel: apagar «Allow new users to sign up» en Supabase (Authentication → Sign In / Providers → Email) — Tomás — desde 02/11
- [ ] Panel: qué hacer con `panel@somospiedra.com` (creado sin acceso) — Tomás — desde 02/11
- [ ] Panel de Meta: arreglar los 2 hallazgos del /codex:review (CONTEXTO §7 del repo) y después cargar `META_TOKEN` y crear la tarea «Meta - Piedra» (vuelta completa). Los leads ya suben solos desde el 11/11 (tarea «Leads - Piedra», solo lectura); sin el token el panel no tiene gasto ni nombres de anuncios — Claude/Tomás — desde 02/11
- [ ] Panel: Supabase free se pausa a los 7 días sin uso (Pro para uso real) y el repo no tiene remoto en GitHub — Tomás — desde 02/11
- [ ] **Cyber Monday — seguimiento (sin tocar presupuestos, decidido 02/11):** ver cómo entregan las 4 variaciones de granza (conjunto 120251076731010411) y el 5/11 confirmar que todo terminó el 4/11 23:59 — Claude — desde 02/11
- [ ] **Ventas reales por anuncio:** Tomás pasa cuáles ventas vinieron de anuncio → comparar costo por venta Cyber / Madre / Test — Tomás → Claude — desde 02/11
- [ ] **Etiqueta «pago confirmado» en WhatsApp Business:** definir quién etiqueta (Erasmo no puede); después pasar la Madre a «compras por mensajes» — Tomás — desde 02/11
- [ ] **R3 Retest:** la tarea programada del 3/11 12:00 lo apaga si no funciona; revisar el aviso — Claude — desde 02/11
- [ ] Sacar el duplicado «Tu frente, antes y después» del vie 13/11 10:30 (ya sale el sáb 7/11) si Tomás confirma — Claude — desde 02/11
- [ ] Fran confirma que pórfido, ocre rectificada y riojana van en escalones exteriores (carrusel E sale el 14/11) — Tomás — desde 02/11
- [ ] No hay reels programados desde el 9/11: subir la tanda que graba Tomás — Tomás/Claude — desde 02/11
- [ ] Revisar R3 Retest y R4 Lote 3 a las 48 h: seguir < $450/chat, cortar > $900 con $3.000 gastados — Claude — desde 02/11
- [ ] Ver que R4 salga en IG con @somospiedranqn y cargar el mensaje armado de WhatsApp de R3/R4 en el Administrador — Tomás/Claude — desde 02/11
- [ ] Grabar reels con los guiones del artifact (BOFU 13, 14, 17 primero) y dejarlos en EDITADOS — Tomás — desde 02/11
- [ ] Confirmar con Fran datos de los guiones: origen de cada piedra, medidas verde bronce, formas de pago, frases técnicas, Añelo y Roca — Tomás — desde 02/11
- [ ] **Datos para la app** (no frenan la construcción: quedan `FALTA DATO`):
  - los medios de pago: nombre, cuenta, % y comisión de cada uno (efectivo, transferencia, débito, crédito, cuotas);
  - planes de cuotas, con su recargo y su comisión;
  - comisiones de MP y del posnet;
  - % de desperdicio;
  - precio del envío (fijo o por zona);
  - categorías y gastos fijos.

  — Tomás / cliente — desde 08/10
- [ ] El Excel o planilla actual, con la cobertura de cada producto (ojo: no se vende en cajas; la piedra va a granel o paletizada y la granza por m²), para el importador — cliente — desde 08/10
- [ ] **Para facturar:**
  - razón social y CUIT (verificar 33-71680803-9);
  - IIBB e inicio de actividades;
  - punto de venta para web services;
  - delegación de wsfe al CUIT de Tomás.

  — cliente — desde 08/10
- [ ] Con el contador: alícuotas de IVA de plantas, envío y parquización, y el régimen de IIBB — Tomás / contador — desde 08/10
- [ ] **Pauta:** que Fran diga qué fotos de la web son propias (hasta entonces no se usan); definir si el artifact dice "la gestión la hace Tomás, sin cargo" — Tomás / Fran — desde 09/10
- [ ] Descartar el borrador vacío "Nuevo anuncio de Interacción" (120250759520900411) en la cuenta 1945796639629607 — Tomás — desde 13/10
- [ ] Descartar los borradores de Somos Piedra en la cuenta vieja 2044879766141120 (Facebook de Somos iPhone) — Tomás — desde 13/10
- [ ] **Test 1-1-3 (A quincho, B pileta, D obras), $5.000/día:** 18 PNG listos en `E:\anuncios somos piedra\nuevos-8-angulos\`; falta subirlas a Meta (Chrome, vía del 13/10), crear campaña/conjunto/3 anuncios en borrador y activar con OK de Tomás. Textos y mensajes en `textos-y-mensajes.md`. La campaña del 13/10 ya es la **MADRE** ($5.000/día, solo C5 + C1; C2 y C3 pausados) — Claude / Tomás — desde 15/10
- [ ] Confirmar con Fran los datos de los 8 carruseles nuevos antes de publicarlos (reseñas G, pagos E, horarios/stock H, paletizado/Añelo D, Adoquín 10×10 C, % cortes F) y pasarle fotos de obras para el ángulo "antes y después" — Tomás / Fran — desde 15/10
- [x] (hecho 26 y 28/10) **Revisar la campaña MADRE y el test el lunes 20/10:** costo por chat de cada carrusel y ventas (etiqueta "anuncio" en WhatsApp Business); rotar si la frecuencia del conjunto pasa 2,5 o C5 supera ~$650/chat dos días seguidos (criterio propuesto, no del método) — Tomás / Claude — desde 13/10
- [ ] Fondos de la cuenta 1945796639629607: $30.000 cargados alcanzan ~3 días a $10.000/día; recargar antes del 16/10 (15/10: para la campaña conjunta del Día de la Madre hacen falta ~$40.000 más; Tomás recarga después de armar todo) — Tomás — desde 13/10
- [x] Autenticar la identidad en el Administrador de anuncios de la cuenta 1945796639629607 — hecho 15/10 (Tomás)
- [ ] Elegir el número de WhatsApp de la campaña conjunta: 459-0936 (el de la página) o 404-1698 (el de las tarjetas, hay que conectarlo a la página) — Tomás — desde 15/10
- [ ] **Campaña conjunta Somos Piedra + Vivero, Día de la Madre — ACTIVA desde 15/10** ($20.000/día desde 15/10 12:50, fin sáb 17/10 23:59, destino 459-0936). Anuncios v2 C1 120250807043320411, C2 120250807043650411, C3 120250807044920411, C4 120250807045860411 en revisión de Meta. Falta: (1) Tomás carga saldo (~$60.000 para esta campaña a $20.000/día) — sin eso no entrega; (2) Claude verifica a la tarde que los 4 pasaron la revisión; (3) Tomás confirma con el vivero nombres, precios y horarios (por si se vuelve a poner); (4) Tomás cobra al vivero su mitad ($15.000) y deriva los chats al vivero; (5) mirar resultados el 17/10 y cerrar — Tomás / Claude — desde 15/10
- [ ] WhatsApp de la campaña conjunta: el destino es el del vivero (299 404-1698, el de los creativos); el de la página es 299 459-0936. Hace falta el enlace wa.me — Claude / Tomás — desde 15/10
- [ ] Confirmar con el vivero: nombres de las plantas, que el precio incluye maceta y granza, y el sello "OFERTA" solo si hay oferta real — Tomás — desde 15/10
- [ ] Recargar saldo (~$40.000 para 4 días) y cobrarle al vivero su mitad ($5.000/día) — Tomás — desde 15/10
- [ ] Editar los 3 videos de los lentes Meta → campaña de Reels de $5.000/día — Tomás — desde 09/10
- [ ] **Vincular IG @somospiedranqn a la página y a la cuenta publicitaria** (a la página: hecho 29/10; falta verificar la cuenta publicitaria) (desde el 15/10 frena los anuncios del Día de la Madre: sin esto no se pueden promocionar los posts); píxel de Meta y etiqueta de Google en la web; perfil de Google (categoría, fotos, productos, horario); mensaje fuera de horario y etiqueta "anuncio" en WhatsApp Business — Tomás — desde 09/10
- [ ] Invitación pendiente a tomassanchez2018@gmail.com en el portfolio de Piedra: dejar vencer o cancelar — Tomás — desde 12/10
- [ ] Cerrar las cuentas viejas (IG @somospiedra.cipolletti, FB elijapiedrasas y ElijaPiedra) y pedir el retiro con la herramienta de Google — Tomás / dueño — desde 09/10
- [ ] Probar Somos Piedra en modo local (`npm run local`, "Piedra de prueba", recorrido de `REVISAR.md` §9) — Tomás — desde 09/10
- [ ] Fotos de obras propias (antes y después, para el carrusel 4) — Fran — desde 09/10
- [ ] **Corrida 2026-10-09a (v1.1):** leer el PARA COPIAR Y PEGAR de la integración y `E:\vivero\REVISAR.md` (sección de la corrida); verificar las cuentas — Tomás / Claude — desde 09/10
- [ ] **Decisiones de plata de las ramas** (recomendación de Claude: sí a 1–6):
  1. fecha del corte de Somos Piedra: 01/11/2026;
  2. envío en camioneta con costo $0 y nota (no FALTA DATO);
  3. con IVA sumado, IVA antes del % del medio (difiere hasta 2 centavos del orden de la spec);
  4. saldo inicial de IVA sin cargar = FALTA DATO (en el corte se carga $0);
  5. Ibero: el corte queda como constancia, sin saldos;
  6. lo anulado cuenta como "nunca pasó";
  7. los gastos con factura A no suman crédito de IVA (pide una columna en `movimientos`): hacerlo antes del 01/11 y ver con el contador qué gastos facturan A;
  8. no cargar ventas de prueba con factura en el negocio real antes del corte (una factura pendiente no se anula y deja el corte como constancia).

  — Tomás — desde 09/10
- [ ] Probar la demo para el dueño: `npm run local`, "Piedra de prueba", importar `tests/fixtures/piedra-ejemplo.csv`, probar Vender (laja 12 m² = $528.000, baldosa 83 u. = $498.000), IVA al día, Empleados y el corte. Si ya se abrió antes, usar incógnito — Tomás — desde 09/10
- [ ] Datos de empleados: cuántos, día de pago, si hay boleta de sindicato. Que el contador confirme el cambio de titular al 01/11 — Tomás / contador — desde 09/10
- [ ] Cargar la alícuota del 21 % en las categorías de piedra y la del envío (contador): sin eso "IVA sumado" queda apagado — Tomás — desde 09/10
- [ ] **Corte inicial ("día cero")** cuando la app esté lista: arqueo de cada cuenta (pesos, dólares, MP, banco), cheques en cartera, conteo de stock, deudas con proveedores y de clientes. Fecha de corte y, desde ahí, todo en la app. Copiar cómo se hizo en Somos iPhone, si Tomás deja leer ese Cortex — Tomás / Claude — desde 09/10

- [ ] Fran revisa 3 frases del carrusel "5 errores" (placas 3 a 5: pared firme, limpia y a plomo; presentar las piezas en el piso; adhesivo para piedra natural). Si cambia algo, se reemplaza el anuncio 120250865092770411 — Tomás / Fran — desde 19/10
- [ ] Revisión del TEST v2 (120250865076760411) el 26/10: apagar los 2 carruseles con peor costo por chat y meter 2 nuevos — Claude / Tomás — desde 19/10
- [ ] Ver en el Administrador si los anuncios v2 salen en Instagram (la API no ve la cuenta de IG vinculada) — Tomás — desde 19/10
- [ ] Los 5 anuncios v2 no tienen mensaje armado de WhatsApp (no se pudo por API): cargarlo desde el Administrador si se quiere — Tomás — desde 19/10
- [ ] Reels: alguien de Somos Piedra hablando a cámara en el acopio (formato Super Pedras / Piedra Urbana), para un conjunto de Reels — Tomás — desde 17/10
- [ ] Contar las ventas de los chats con la etiqueta "anuncio" en WhatsApp Business — Fran — desde 17/10

- [ ] **Bot y simulador:** cargar en el `.env` del bot `OPENAI_API_KEY` y `GEMINI_IMAGEN_API_KEY` (proyecto con facturación) y dejar 5 a 10 fotos de clientes en `E:\bot-piedra\fotos\prueba-ab\` — Tomás — desde 23/10
- [ ] **Fran, ronda 2** (`E:\bot-piedra\preguntas-fran-ronda2.md`): IVA con efectivo y con tarjeta, logo y datos del PDF, tramos de precio de la granza por cantidad de bolsas (bolsón descartado: no se vende, 03/11), seguimiento (cuándo y cuántas veces), horario final del bot, cuotas; además el Excel, las fotos de cada piedra (`guia-fotos-piedra.md`), los contactos excluidos y las cuentas — Fran — desde 23/10
- [ ] Decidir qué Cortex manda para el bot: el `CLAUDE.md` del bot apunta a `cortex-somosiphone\piedra\` y el proyecto a `cortex-gestion` — Tomás — desde 23/10
- [ ] Aprobar las reglas del bot (`E:\bot-piedra\reglas\cerebro-reglas-piedra.md`, v2 del 23/10) y la spec v1 del simulador (`E:\bot-piedra\bot\spec-simulador-v1.md`) — Tomás — desde 23/10

- [ ] Fran confirma qué calientes de anuncios compraron (lista en `claude/traspaso-2026-10-29.md`) — Fran — desde 29/10
- [ ] Anotar el origen de cada venta en el mostrador ("¿cómo nos conociste?") o con #vendido en el chat — Tomás / Fran — desde 29/10
- [ ] Que el bot de Piedra arranque solo al prender la PC (caído del 24/10 19 h al 28/10 9:41) — Tomás / Claude — desde 29/10
- [ ] Spec del agente nocturno que lee los chats y anota ventas por anuncio — Claude — desde 29/10
- [ ] Reels orgánicos con música en IG: programarlos desde la app de IG si se quiere (Business Suite solo deja música en FB) — Tomás — desde 30/10
- [ ] Medir las piezas orgánicas de la semana 30/10–5/11 (alcance, guardados, chats) y ajustar horarios — Claude / Tomás — desde 30/10
- [ ] Armar y programar la semana de contenido desde el vie 6/11 — Claude — desde 30/10

- [ ] **Programar en Business Suite las piezas del 30/10** (carpeta `contenido\ideas-dia\2026-10-30\`: 3 carruseles + 3 placas, y `extra-antes-y-despues\`: 4 carruseles; más el reel B armado con fotos reales). Desde el vie 6/11, después de la semana-30-10. Plan en `claude/traspaso-2026-10-30.md` — chat nuevo — desde 30/10
- [ ] Actualizar `contenido\ideas-dia\armar_dia.py` de la PC con soporte de escenas de IA ("escena:<id>", "split" con fotos reales, 4.º argumento con la carpeta de escenas, escenas en JPG de 1200 px para que pieza.html pese menos de 30 MB) — Claude — desde 30/10
- [ ] Elegir uno de los 3 bocetos de estilo (Tierra, Ficha de cantera, Cuaderno de obra: https://claude.ai/artifact/XD2Hrs6a6bDGiSHHqGm8ms) o rotarlos, y sumarlo al armador — Tomás — desde 30/10
- [ ] Fran: grabar el reel A (camioneta cargando y saliendo) y el C (rociador mojando la piedra); confirmar horario del sábado (9 a 14), espesores por piedra y granza roja de Olavarría en stock — Fran / Tomás — desde 30/10
- [ ] Revisar TEST REELS (120251035611560411, $16.000/día) a las 24 h: costo por chat por anuncio y por lote; si un lote recibe <20% del gasto, gasto mínimo — Claude (tarea programada sáb 31/10 12:30) — desde 30/10
- [ ] Cargar el mensaje armado de WhatsApp de cada uno de los 7 reels (Plantilla de mensaje en Ads Manager) — Tomás / Claude por Chrome — desde 30/10
- [ ] Descartar el borrador vacío "L1-R1" en Ads Manager — Tomás — desde 30/10
- [ ] Saldo de Higgsfield (API) en 0 desde el 30/10: recargar para que la tarea diaria tenga escenas (3 por día ≈ USD 0,84) — Tomás — desde 30/10

- [ ] Programar en Business Suite FB + IG los carruseles B «Esto arruina tu piedra» y C «Tu frente pide piedra a gritos» del 02/11 (aprobados) — chat — desde 02/11
- [ ] Generar 2 carruseles nuevos con la regla nueva (portada hook visual + imagen = texto, escenas por ChatGPT) — chat — desde 02/11
- [ ] Agregar a la tarea diaria el armado con `layout`/`marcas` en el PROMPT-DEL-DIA (ya está en PROMPT.md; verificar que la tarea del 03/11 lo use) — chat — desde 02/11
- [ ] Borrar los lock viejos de git del Cortex (`.git\stale-HEAD-lock-0211`, `.git\stale-HEAD-lock-0211b`) — Tomás — desde 02/11
- [ ] Cambiar el punto 3 del texto de la tarea «Ideas del día · Somos Piedra» (nombra hf.py) — Tomás — desde 02/11
- [ ] BANCO.md: marcar usado el par del frente (extra programado 13/11 10:30) — chat — desde 02/11
- [ ] Confirmar con Fran: cuidados de la piedra, granza junto a un fogón, cat-017 pizarra, cat-027 verde bronce, "a granel o paletizada" — Tomás — desde 02/11

- [ ] **Trial Reels:** crear app de Meta (Business + Instagram, «inicio de sesión de Instagram») y token de @somospiedranqn (instagram_business_basic, instagram_business_content_publish, instagram_business_manage_insights) en `E:\anuncios somos piedra\trial-reels\.env` (`IG_TOKEN=`, modelo en `env-ejemplo.txt`); no pasarlo por el chat — Tomás — desde 16/11
- [ ] **Trial Reels:** elegir el reel de la prueba (uno que NO esté programado en Business Suite: reels programados hasta el 10/12, fotos y carruseles hasta el 28/11, verificado el 16/11) — Tomás — desde 16/11
- [ ] **Videos de entregas reales:** pedirle a Fran que filme cada carga/entrega con el celular (es lo que más rinde: «Así llega tu piedra» 5.364 vistas) — Tomás — desde 16/11
- [ ] **Trial Reels:** OK para el Programador de tareas de Windows (3 publicaciones por día + ranking nocturno; PC prendida) — Tomás — desde 16/11
- [ ] **Trial Reels:** probar el script con 1 reel (`trial.cmd estado`, después `trial.cmd publicar --video … --caption …`) y al día siguiente `trial.cmd ranking` para ver qué métricas da la API en un trial; después registrar las tareas y apagar lo programado en Business Suite — Claude/Tomás — desde 16/11 (script hecho el 16/11: `trial-reels\`, 7 tests en verde)
- [ ] **Elegir modelo IA para el gancho de 64 y 61** (Veo o Seedance; mirar `E:\anuncios somos piedra\reels\lote-2026-11-16-ia\COMPARAR.md`; 61-Veo tiene toallas azul y amarillo) — Tomás — desde 16/11
- [ ] **Trial reels a `cola\`:** T02, T04, T05, T06, T07 y T09 ya; T01 y T03 si «bajamos a mano / te lo llevamos» es lo de siempre; T08 no el 18/11 (placa P4 con 5×4); T05 y T06 no el mismo día; escuchar el arranque de T08 y T09 — Tomás — desde 16/11
- [ ] **Mirar 66 y 67 con IA** (`E:\anuncios somos piedra\reels\lote-2026-11-16-ia-2\`, `COMPARAR.md`) y decidir el recorte de `67-lluvia-2` (recomendación: dejarlo) — Tomás — desde 16/11
- [ ] **Reel 76 todo IA:** pegar el resultado de la sesión piedra-ia-9a en un chat nuevo; revisar la granza IA contra la real y el rótulo «Imagen ilustrativa» (`reels\lote-2026-11-16-ia-3\`) — Claude revisa / Tomás decide — desde 16/11
- [ ] **Video IA: quedan USD 0,946 del tope de 10** (`gastos-apimart.csv` en 9,054); otra tanda necesita tope nuevo — Tomás — desde 16/11
- [ ] Selector de VS Code en Sonnet 5.5 (la sesión 8a corrió con Fable 5.2) — Tomás — desde 16/11
- [ ] **Jue 19/11: decidir R61 y R65 (TEST) y «Toda la zona – abierto» (MADRE, $1.278/conv del 9 al 15/11)** — Claude + Tomás — desde 16/11
- [ ] **Ventas por anuncio:** los empleados anotan las ventas que vinieron de anuncios; Tomás las carga en un chat nuevo y Claude las cruza con `meta_leads` por teléfono → costo por venta por anuncio — Tomás / Claude — desde 16/11
- [ ] **Meta:** 10 pagos con error en los últimos 7 días (de 18) y 15 borradores sin publicar («Revisar y publicar (15)»; «ESCALA Granza R21 + R27» con cambios sin publicar) — Tomás — desde 16/11
- [ ] Ver si «pago confirmado» / optimizar a «compras a través de mensajes» se puede con el número actual (Evolution) — Claude — desde 16/11

## 3. Ibero (`ibero`)
- [ ] Probar la app en modo local (`npm run local`, negocio "Vivero de prueba") siguiendo los 6 pasos de `metodo/` §5.7, **después de la corrida 2026-10-08a**, sobre la versión multi-negocio que va a estar en línea. Pasar todo lo que cambiar en un solo mensaje. Lo cargado antes en modo local no se ve más (la base local cambia de nombre por negocio) — Tomás — desde 08/10
- [ ] Lo que falta del cliente (`E:\vivero\REVISAR.md` §4): datos fiscales, punto de venta y delegación de wsfe, alícuotas de IVA, comisiones reales, nombre, precios de los servicios y gastos fijos — Tomás / cliente — desde 08/10
- [ ] Lista "Con el contador" de `REVISAR.md` §4, incluido el arrastre del IVA a favor — Tomás — desde 08/10
- [ ] Export del sistema viejo (comprado en Mercado Libre), para probar el importador con el archivo real — cliente — desde 08/10
- [ ] Puesta en línea (etapa 8), después del multi-negocio — Claude (Sonnet 5.5 + advisor) — desde 08/10

## Cortex (`cortex`)
- [ ] Crear `.claude/agents/` (`explorer`, `researcher`, `worker`) y el advisor donde se abre VS Code, o sacarlos del bloque de delegación: en la corrida 2026-10-09a no existían y las sesiones usaron Plan/general-purpose con Opus — Tomás / Claude — desde 09/10
- [ ] `/codex:review` de la corrida 2026-10-09a después del 14/10 (Codex sin cupo hasta el 14/10 9:47) — Tomás — desde 09/10
- [ ] Crear el repo privado en GitHub para este Cortex y conectarlo (`git remote add origin <url>`): hasta entonces `sync.cmd` solo commitea — Tomás — desde 08/10
- [ ] Pegar `herramientas/instrucciones-proyectos/sistema-gestion.md` en las instrucciones del proyecto de Claude "Sistema de Gestión de Empresas" — Tomás — desde 08/10
- [ ] Sacar de las instrucciones del proyecto de Claude el prompt del bot de Somos iPhone que quedó pegado al final ("Otro modelo con la entrega ya dicha…") — Tomás — desde 08/10
- [somos-piedra] Subir VG3/VG4/VF3/VF4 a test de carruseles (decidir presupuesto) · revisar V1 · descartar borrador viejo L3-V3 (ad 120251109138600411) · confirmar entrega de L3-V3 (04/11)
