
CIERRE — somos-piedra (Erasmo, test del setter) — 11/11 00:30

Hecho:
- /salud: Erasmo seguía con reglas dd62fcec (arranque 11:32 del 10/11; las reglas se editaron 12:25). Tomás lo reinició a las 22:17: ahora corre 0ac6b308 (modo setter cargado).
- El tester 298 440-9447 es el WhatsApp personal de Tomás y está en el Chrome «Browser 2» (no el 3: el 3 tiene el WhatsApp de Somos Piedra 299 459-0936, con clientes).
- Test con reglas viejas (5 casos): laja para frente 6 x 2,5 (bien); «pasame fotos» con catálogo ya enviado (escala, silencio); pileta + quincho 5 x 2,4 (recomienda y cotiza travertino blanco 12 m² $1.320.000 / $1.872.000, coincide con el panel); «que no queme ni resbale» (escala, silencio); granza 150 m² (escala por >100 m², silencio).
- Test con reglas nuevas 0ac6b308 (montos verificados contra el panel y la tabla de granza): granza blanca 12 m² $240.000 / $300.000; «está caro» (valida, compara bolsas vs bolsones, pide el otro presupuesto, pregunta de la obra); «lo pienso» (pregunta qué lo hace dudar); «en 15 días arranco» (sigue la charla, no promete escribir); pizarra negra 30 cm 4 x 2,8 en efectivo $336.000; «ya compré» (cierra con la frase de la regla); mensajes cortados y con faltas + dirección y horario (granza 8 m² $176.000 / $216.000, Belgrano 3090, horarios bien); «lo quiero, ¿cómo pago?» (escala, silencio); travertino caro → ofrece Travertino Irregular 12 m² $726.000 / $1.044.000.
- Un subagente revisó el repo (solo lectura): no falta código bloqueante para salir a clientes; evaluar --offline 18/18; npm test se corta en el entorno de Cowork por un EACCES en /tmp (no por el código).
- Se leyó la planilla del local (SOMOS PIEDRA PLANILLA 10-11, 97 hojas: ventas y gastos por mes desde 2023 + LISTADO). El archivo «6-11» llegó vacío (165 bytes). Análisis en claude/analisis-planilla-2026-11-11.md del proyecto. No se cargó ningún dato.

Decisiones (qué y por qué):
- Erasmo NO busca en la web (Tomás, 10/11): lo que no sabe se cubre con datos del local, no con Google.
- La planilla no se importa como historia ni como dashboard: se arranca de cero anotando todo (Tomás, 11/11).

Pendientes nuevos:
- [ ] Error de Claude (10/11 22:16–22:19): 8 mensajes de prueba salieron al grupo de WhatsApp «vibes a coding» de Tomás (el chat abierto cambió y no se verificó). Tomás decide si se eliminan — Tomás
- [ ] Granza: la planilla y una venta real del 05/11 dan 20 m² en $310.000 efectivo (Erasmo cotiza $300.000) y la lista de 1 m² en $26.500 (Erasmo $27.000). Definir con los tramos — Fran
- [ ] Silencio al escalar: «lo quiero, ¿cómo pago?», «pasame fotos» (con catálogo ya enviado), dudas técnicas y >100 m² dejan al cliente sin respuesta; de noche el aviso al grupo espera hasta las 9 — Fran (ya estaba: se confirma como lo que más frena la salida)
- [ ] Erasmo repite la misma pregunta («el barro, el polvo?») si el cliente no la contestó: ajustar la regla — Claude
- [ ] Planilla → app: definir dónde se anota «venta por anuncio» y el resto de lo que hoy lleva la planilla (ver el análisis) — Tomás
- [ ] Volver a pedir la planilla del 6-11 (llegó vacía) — Tomás

Pendientes cerrados:
- Erasmo: reiniciar y testear las reglas de setter (cerrado 11/11; faltó probar proveedor, cuotas/factura y un segundo «lo pienso»).

Aprendizajes:
- Antes de CADA envío por WhatsApp Web hay que verificar el encabezado del chat abierto (y que los autores sean solo el tester y Somos Piedra): la pestaña es el WhatsApp personal de Tomás y un clic suyo cambia el chat.
- Los nombres «Browser 1/2/3» de Claude in Chrome se reasignan al reconectar: identificar el navegador por la cuenta de WhatsApp, no por el número.
- Desde Cowork no se puede reiniciar a Erasmo (terminales y VS Code son solo clic): el reinicio lo hace Tomás. `npm run dev` (node --watch) recargaría las reglas solo.
- Mensajes mandados mientras Erasmo arranca se ignoran (incluido #reset): reenviar después del arranque.

Próximo paso: Fran decide el mensaje de espera y los tramos de granza; después 2 días en borrador con clientes reales (frase de Tomás + .env) — Modelo: —
Cambia una regla de plata o del método: no

CIERRE — somos-piedra (pauta y reels) — 11/11 08:20

Hecho:
- 09/11 noche: los 13 reels de la 09b (R01, R03, R08, R11–R20), aprobados por Tomás, subidos a TEST CREATIVOS (ABO), un conjunto por reel a $1.600, programados 10/11 00:00. Textos escritos por Claude con las reglas de contenido. Gasto programado: ~$109.000/día.
- 10/11: lecturas a las 8:00, 16:30 y 21:20. Día cerrado: $138.231 / 104 conv = $1.329 (09/11: $77.372 / 69 = $1.121).
- 11/11 00:10 (tarea programada, sin OK por pedido de Tomás): ESCALA no sube (día > $1.200). Pasan a la ESCALA con el mismo post R11 Granza gris ($368, 7 conv), R08 Tu frente ($732, 3) y R14 Laja ocre ($774, 3). Pausados R01, R03, R12, R15, R20, N2, N4 y «R4 Lote 3» de TEST REELS ($1.798). Gasto programado ahora: ~$85.800/día (MADRE $35.000 + ESCALA $30.000 + 13 conjuntos de test × $1.600).
- Consulta a Santiago, Lauty y Doglio: el cuello es lo que pasa después del chat, no los anuncios. No subir más de 30%, estabilizar, medir ventas.
- Prompt listo: `E:\anuncios somos piedra\reels\PROMPT-vscode-2026-11-10a-variaciones-granza.md` (14 reels: 8 de granza 21–28 + 2 de R08, R13 y R14; deja textos de anuncio y de orgánico). Se corre en VS Code con la carpeta `editor-reels-tomas`.
- Borrada `reels\_subida-2026-11-10` (partes de video de la subida), con permiso de Tomás.
- Por qué el 10/11 gastó $138.231 con $109.000 programados (+27%): el presupuesto diario de Meta es un promedio, no un tope (hasta +75% en un día, 7× el diario por semana dom–sáb). Por campaña: ESCALA $41.570 (+39%), TEST CREATIVOS $42.592 (+33%), TEST REELS $14.386 (+20%), MADRE $39.683 (+13%).

Decisiones (qué y por qué):
- Los 13 reels van todos al test a $1.600 (Tomás, 09/11); el gasto queda en ~$109.000 y Tomás lo deja así (10/11).
- La lectura nocturna, los cortes y el escalón no necesitan el OK de Tomás (Tomás, 10/11: «a la noche no necesitas el ok, hacelo»). Escalón: ESCALA +20% solo si el día cierra < $1.200/conv; tope $150.000; MADRE no se toca.
- No subir la ESCALA y estabilizar 3 días; variaciones del ganador R11 con código (Tomás dio el OK el 10/11).
- Erasmo se conecta por QR (Tomás, 10/11). Erasmo de guardia 18–9 recién después del testeo y de las decisiones de Fran.
- Ventas: todavía no se puede decir qué anuncio trajo cada venta; Tomás pasa las de noviembre. Se mide con chats, cotizaciones y ventas por día (panel), no por anuncio.
- Sin carruseles nuevos por ahora: N1–N6 trajeron 0–2 conv contra $368–$774 de los reels.

Pendientes nuevos:
- [ ] Correr el prompt 2026-11-10a (14 reels) en VS Code, carpeta editor-reels-tomas, Sonnet 5.5 — Tomás
- [ ] Revisar los 14 reels del lote-2026-11-11 y subirlos al test a $1.600 — Claude
- [ ] Lectura del 11/11: juzgar N1, N3, N6, R16, R18, R19, VG3-H1 (0 conv), R13, N5, R17 y cómo reparte la ESCALA con R11, R08, R14 — Claude
- [ ] Decidir si la regla de corte juzga todo recién con $3.000 de gasto (hoy 1 conv cara se corta antes que 0 conv) — Tomás
- [ ] Decidir si quiere tope real de gasto (Meta puede gastar hasta +75% en un día) — Tomás
- [ ] Pasar las ventas de noviembre para sacar la primera tasa de cierre — Tomás
- [ ] Cargar en el panel cada cotización y cada venta con monto — Fran
- [ ] Programar el orgánico IG+FB de los 13 reels de la 09b, uno por día — Claude
- [ ] 13/11: evaluar juntar MADRE y ESCALA en una sola CBO con los números del 10 al 12/11 — Claude

Pendientes cerrados:
- Correr el prompt 09b; revisar los 13 reels y subirlos al test; leer el arranque de la ESCALA y N1–N6 y aplicar cortes.

Aprendizajes:
- Subir videos a Meta desde Chrome: `file_upload` acepta 3,8 MB por llamada. Partir con `split -b 3600000`, stagear las partes, input file inyectado, unir con Blob y POST a graph-video `/advideos`. Borrar las partes al final.
- `javascript_tool` corta a los 45 s y bloquea salidas con ids o query strings: lanzar lo largo en segundo plano, guardar en `window` y devolver tablas cortas.
- El grupo de pestañas se pierde entre turnos largos: `tabs_context_mcp` y navegar de nuevo a Ads Manager.
- El presupuesto diario de Meta no es tope: planificar con hasta +30–40% el primer día de una campaña nueva.

Próximo paso: chat nuevo; lectura del 11/11 y subir los 14 reels cuando termine VS Code — Modelo: Sonnet 5.5
Cambia una regla de plata o del método: no

Agregado 11/11 08:25 — corrida 2026-11-10a terminada (lo pegó Tomás):
- Los 14 reels (21–34) están en `E:\anuncios somos piedra\reels\lote-2026-11-11\<carpeta>\reel-codigo.mp4`, de 11,6 a 18,6 s. REVISAR: `lote-2026-11-11\REVISAR-codigo-2026-11-10a.md` (trae texto de anuncio y de orgánico por reel).
- ElevenLabs: 3.219 caracteres mandados, 1.415 cobrados (dato de la sesión, sin contrastar con el panel de la cuenta).
- Palabras dudosas para escuchar: 21 «Viene en bolsas» (8,0 s), 24 «granza» (0,8 s, whisper oyó «granja»), 34 el arranque «Este».
- Sin subir a Meta: falta que Tomás los mire con sonido y apruebe.

Agregado 11/11 08:45:
- Tomás pide para el chat nuevo: programar todo el orgánico (las piezas de contenido de siempre + 1 reel con código adicional por día) y subir los reels a pauta.
- Calendario orgánico: por Graph la página «Somos Piedra, elija piedra» tiene 0 publicaciones programadas; la última publicada es del 10/11 13:30 (venía con 2–3 por día). El extra del 13/11 10:30 anotado el 02/11 no se pudo confirmar por API.
- Recomendación de Claude para pauta: los 14 reels al test a $1.600 c/u ($22.400/día), entrando junto con los cortes de la lectura del 11/11.

## 11/11 08:40 — Erasmo: buscador singular/plural y regla de no repetir preguntas
- `E:\bot-piedra\src\catalogo-piedra.js`: `buscarProductos` iguala singular y plural («adoquines» → Adoquines Ojito, Baldosa 40X40 Adoquin Recto Grande, Micosa Adoquin 10X10, Porfido Adoquin 10X10). Prueba nueva en `test/catalogo-piedra.test.js`; `npm test` completo: 613 ok, 0 mal (en la VM hace falta `TMPDIR=/tmp/...`, `/sessions` está lleno).
- `src/cerebro-reglas.md`: «cada pregunta una sola vez por chat» (3 toques). Hash nuevo `db50529e`; corre recién cuando Tomás reinicie (hoy sigue `0ac6b308`). Sin commit.
- Venta por anuncio: en Supabase `meta_leads` tiene 0 filas y `ventas` 1 (sin teléfono ni canal); `ventas.canal` admite anuncio/whatsapp/local/otro y `cliente_telefono` exige `549` + 10 dígitos. El bot guarda el anuncio de cada chat solo en su `estado.json`. Propuesta en pendientes; falta OK de Tomás.
- Hallazgo: ningún producto del panel se llama «laja».

## 11/11 09:20 — Erasmo probado en vivo y venta por anuncio (OK de Tomás)
- Erasmo reiniciado: `/salud` da reglas `db50529e`. Probado desde el WhatsApp de Tomás (Browser 2 = 298 440-9447, chat verificado antes de cada envío; 4 mensajes): «adoquines» lista los 4; Adoquines Ojito 15 m² $607.500 / $945.000 (verificado contra el panel: $40.500 y $63.000 el m²); tras «y con tarjeta?» contesta «Con tarjeta, en un pago, te queda en $945.000.» sin repetir la pregunta. Se cortó ahí porque Tomás empezó a usar esa pestaña.
- **Hallazgo:** lo de venta por anuncio ya estaba casi todo hecho en `E:\somos-piedra-panel` (29/10): `scripts/meta.mjs` lee `estado.json` del bot y sube `meta_leads`; la pantalla Meta cruza teléfono de la venta ↔ lead y gana el lead (no hace falta tocar `ventas.canal` ni migrar). Nunca corrió: no hay `meta.log` ni tarea de Windows. Sube los leads aunque falte `META_TOKEN`.
- Hecho en el panel (sin commit): teléfono obligatorio en Vender (`motivoSinTelefono` en `src/domain/telefono.ts`, campo fuera de «Opcional», aviso y botón apagado; `armarVenta` lo sigue aceptando vacío), test nuevo, e2e-meta y e2e-piedra ajustados, `SUBIR-TELEFONO.cmd` y `scripts/leads-oculto.vbs`. Tests de teléfono, venta y dominio de Meta en verde; `tsc` y los e2e no se pudieron correr en la VM (los corre el .cmd antes de deployar).
- Lectura en seco de los leads: 493 chats con anuncio (436 con id de anuncio, 492 con teléfono argentino).

## 11/11 09:20 — Pauta: hoy contra ayer a la misma hora
- Hasta las 09:00 (por hora, Graph desde Ads Manager, Browser 3): hoy $9.681 / 17 conv ($569) contra ayer $31.657 / 18 conv ($1.759). Hasta las 08:00: hoy $8.621 / 15, ayer $21.520 / 8. Por campaña (hoy ← ayer): ESCALA $2.842/6 ← $8.990/4; MADRE $3.016/4 ← $5.673/3; TEST CREATIVOS $3.716/7 ← $15.600/10; TEST REELS $71/0 ← $1.393/1.
- **La entrega se frenó ~08:15:** 08–09 hs $1.060 (371 impresiones contra 1.521 la hora anterior) y 0 desde las 09:00. `account_status` 9 (período de gracia); Facturación dice «Pago pendiente: no se ha podido procesar el pago», saldo pendiente $68.830,81. Ayer pasó lo mismo de ~18:10 a 20:00 (19–20 hs: $0; el registro marca «Estado de cuenta actualizado» 17:45 y tres cobros 18:00–18:11).
- En el registro de la cuenta: R21–R34 (los 14 reels nuevos) creados 09:12–09:14 en TEST CREATIVOS a $1.600, arrancan el 12/11 00:00 (no los subió este chat).

SESIÓN — somos-piedra (pauta + orgánico) — 11/11 08:50–09:55

Hecho:
- Calendario orgánico confirmado en Business Suite → Programadas: NO estaba vacío (por Graph daba 0). Había 7 publicaciones FB + IG: mié 11/11 10:30 y 13:30, jue 12/11 10:30 («La pileta, antes y después») y 13:30 («¿Cómo se cuida la piedra…?»), vie 13/11 10:30 («Tu frente, antes y después», el extra sigue) y 13:30 («¿Qué piedra sos?»), sáb 14/11 13:30 («¿Así recibís a las visitas?»). Desde el dom 15/11 no hay carrusel ni placa.
- Pauta: los 14 reels del lote-2026-11-11 (R21–R34) subidos a TEST CREATIVOS (ABO): un conjunto por reel a $1.600/día, inicio 12/11 00:00, anuncio con el formato de R11 (video + CTA WhatsApp), textos del REVISAR-codigo-2026-11-10a, tapa = cuadro del segundo 1 (se ve el hook). Videos originales (sin recomprimir). Verificado por Graph: 14 conjuntos ACTIVE con start 2026-11-12T03:00Z y 14 anuncios ACTIVE.
- Gasto programado desde el 12/11: ~$108.200/día = MADRE $35.000 + ESCALA $30.000 + 27 conjuntos de test × $1.600 ($43.200). Con el margen de Meta puede gastar más (el 10/11 fue +27%).
- Orgánico: 27 reels con código programados en FB + IG, uno por día a las 20:30, del mié 11/11 al lun 7/12. Orden (intercalando temas): 11/11 R11 · 12 R08 · 13 R21 · 14 R13 · 15 R14 · 16 R22 · 17 R17 · 18 R29 · 19 R23 · 20 R19 · 21 R16 · 22 R24 · 23 R31 · 24 R30 · 25 R25 · 26 R01 · 27 R33 · 28 R26 · 29 R32 · 30 R15 · 1/12 R27 · 2 R18 · 3 R34 · 4 R28 · 5 R12 · 6 R03 · 7 R20. Verificado en Programadas: 68 filas (34 publicaciones × FB e IG).
- Textos del orgánico: los 14 nuevos, del REVISAR (texto orgánico + hashtags). Los 13 de la 09b no tenían texto orgánico: se usó el texto del anuncio que ya corre + #Neuquén #AltoValle y 2 del tema. Sin palabras prohibidas (bolsón, %, STOCK REAL).
- Videos del orgánico: copia a 1080×1920 de menos de 3,6 MB (x264 2 pasadas, SSIM 0,979–0,992 contra el original) para subir en una sola llamada. La carpeta temporal `reels\_subida-2026-11-11` se borró al terminar (con permiso de borrado); el calendario con los textos quedó en `reels\lote-2026-11-11\organico-programado-2026-11-11.json`.
- Lectura del 11/11: agendada para las 00:05 del 12/11 en este mismo chat (cortes y escalón sin OK).

Decisiones (qué y por qué):
- Reel orgánico a las 20:30: las piezas de siempre ya ocupan 10:30 y 13:30.
- Orden intercalado (granza / frente / adoquín / stock) para no publicar 8 reels de granza seguidos.
- No se programó carrusel/placa del 15/11 en adelante: no hay piezas armadas y aprobadas; las del banco viejo (ideas-dia de octubre) pueden traer «bolsón».

Pendientes nuevos: piezas de siempre desde el 15/11; texto orgánico de los 13 de la 09b a gusto de Tomás.
Sin decidir (Tomás): regla de corte recién con $3.000 de gasto; tope real de gasto.

## 11/11 09:50 — `SUBIR-TELEFONO.cmd` corrido y verificado
- Tomás corrió el .cmd. Verificado: `meta_leads` 493 filas (436 con anuncio, 492 con teléfono argentino, 0 sin fecha), carga inicial 09:26; tarea «Leads - Piedra» andando (`meta.log`: 09:31, 09:36, 09:41, «493 leídos, 0 nuevos»); producción sirve el build nuevo (`index-D5fS_NT0.js` + `telefono-DJtbmQXa.js`). `meta_anuncios` sigue vacía (falta `META_TOKEN`).
- Commits: panel `b6cb9af` (`main`) y bot-piedra (rama `piedra/archivos-excluidos`: reglas `db50529e`, buscador, diagnóstico). Sin push. `.gitignore` del panel quedó con un cambio previo que no es de este chat.
- Pauta 09:50: sigue frenada (estado 9, 09–10 hs $0 y 0 impresiones; día $9.879 / 17 conv; saldo pendiente $69.042,72).

## 11/11 10:02 — Meta: pago hecho, cuenta activa
- Actividad de pagos: 11/11 $69.056,35 Pagado. 10/11: $52.194 Pagado (11:14), $52.194 Error, $6.543,43 + $11.451,01 + $17.176,52 Pagados (18:00–18:11), $17.176,51 Error ×2. 09/11: $31.152 ×2 Pagados.
- `account_status` 1 a las 10:00. Saldo pendiente $59.003,98 (10:00) → $59.008,30 (10:02), «No tienes ningún pago pendiente»; umbral de cobro $52.194, fecha 7/12. No se pudo reconciliar por qué quedan $59.008 después de pagar $69.056 (antes del pago la pantalla decía $68.830,81).

## 11/11 10:50–11:15 — Orgánico 15–21/11: 7 placas + 7 carruseles programados (FB + IG)
- Pedido de Tomás: «armá las placas ya» (10:07) y «hacé todo, dale» (10:50). La PC estuvo desconectada de 10:10 a 10:50: las placas se armaron en la nube y se guardaron al volver.
- **7 placas de datos con código** (1080×1350, fondo de losas oscuras, lima, Poppins, dibujo SVG; solo datos confirmados). En `E:\anuncios somos piedra\contenido\semana-15-11\` (`placas\P1…P7.jpg` + `.txt`, `gen.py`, `logo.jpg`, `bg.png`). Temas: horarios · cuántas bolsas · piedra natural · cómo medir · gris o roja · te la llevamos · qué mandarnos.
- **7 carruseles (10:30):** no se armaron nuevos; se usaron los 6 aprobados de plantillas que ya corren en pauta y no habían salido en orgánico (N1–N3 de `carruseles-2026-11-08`, N4–N6 de `carruseles-2026-11-09-ia`, con su «CAPTION (orgánico)») y el carrusel A «¿Ocre o verde bronce?» de `contenido\ideas-dia\2026-11-02\` (rehecho el 02/11 con portada partida, nunca programado). Verificado en Publicadas (139 filas, hasta el 5/10) que ninguno había salido.
- **Calendario (FB + IG juntos):**
  - Dom 15: 10:30 N3 «El frente habla de tu casa» · 13:30 P1 horarios
  - Lun 16: 10:30 N5 «Así sale tu pedido» · 13:30 P2 cuántas bolsas
  - Mar 17: 10:30 N1 «¿Tu entrada es de tierra?» · 13:30 P3 piedra natural
  - Mié 18: 10:30 N2 «Así llega tu pedido» · 13:30 P4 cómo medir
  - Jue 19: 10:30 N6 «¿No tenés cómo llevarla?» · 13:30 P5 gris o roja
  - Vie 20: 10:30 A «¿Ocre o verde bronce?» · 13:30 P6 te la llevamos
  - Sáb 21: 10:30 N4 «Te la llevamos» · 13:30 P7 qué mandarnos
- Verificado en Contenido → Programadas: 94 filas = 47 publicaciones × 2 (FB + IG). Del 15 al 21/11 cada día tiene 10:30, 13:30 y el reel de las 20:30, con 1 fila de FB y 1 de IG cada una. Textos y carpetas en `contenido\semana-15-11\programacion-15-al-21-11.json`.
- Textos validados: sin `$`, `%`, bolsón, gratis, descuento, cuotas, 25 m, STOCK REAL ni FOTO REAL.

Decisiones (qué y por qué):
- Carruseles: reusar los aprobados antes que armar nuevos (pedido «hacé todo»; N1–N6 ya traen texto para orgánico). Los envíos (N2, N4, N5, N6) se separaron en días distintos y el viernes, que la placa es de envío, va el A.
- Placa a las 13:30 y carrusel a las 10:30, como venía la tanda anterior.

Pendientes nuevos: tanda del 22/11 en adelante (carrusel + placa); el sáb 14/11 10:30 quedó sin carrusel.

CIERRE — somos-piedra — 11/11 11:20 (Erasmo, panel y lectura de la mañana)

Hecho:
- Erasmo: buscador singular/plural (`src/catalogo-piedra.js` + prueba; 613 tests en verde) y regla «cada pregunta una sola vez por chat» (`src/cerebro-reglas.md`, hash `db50529e`). Tomás reinició 08:51. Probado en vivo desde su WhatsApp (4 mensajes, chat verificado antes de cada envío): «adoquines» lista los 4; Adoquines Ojito 15 m² $607.500 / $945.000 (contra el panel); tras «y con tarjeta?» no repite la pregunta. Commit `cf5cde1` en `piedra/archivos-excluidos` (incluye lo pendiente del 10/11).
- Venta por anuncio: el panel ya la tenía armada (script que lee el bot, `meta_leads`, cruce por teléfono). Se hizo el teléfono obligatorio en Vender (`b6cb9af`), `SUBIR-TELEFONO.cmd` y la tarea «Leads - Piedra». Tomás lo corrió: deploy verificado, 493 leads cargados, la tarea corre cada 5 minutos.
- Pauta: hoy contra ayer a las 9 hs (17 conv / $9.681 contra 18 / $31.657); se encontró el pago rechazado y la entrega frenada 08:15–09:56; Tomás pagó $69.056,35 y la cuenta volvió a activa.
Decisiones (qué y por qué):
- Teléfono obligatorio en Vender, como regla de la pantalla (sin teléfono no se puede atribuir la venta).
- La venta por anuncio se atribuye sola por teléfono contra `meta_leads`; no se une `#vendido` con `ventas.canal` (ya estaba construido y el bot no escribe ventas sin monto).
- Tarea «Leads - Piedra» en solo lectura, separada de «Meta - Piedra» (los leads no esperan al token y nada prende anuncios solo).
Pendientes nuevos:
- [ ] Segunda prueba de «no repite la pregunta» + proveedor, cuotas/factura y segundo «lo pienso» — Claude
- [ ] e2e del panel después del cambio y avisarle a Fran que Vender pide el teléfono — Claude / Tomás
- [ ] Push de `E:\bot-piedra` y `E:\somos-piedra-panel` — Tomás
- [ ] Qué productos son «lajas» (ninguno se llama así en el panel) — Fran / Tomás
- [ ] Vigilar los cobros de la tarjeta en Meta (saldo $59.008 sobre el umbral de $52.194) — Tomás
Pendientes cerrados:
- Buscador singular/plural; regla de no repetir preguntas; commit en `E:\bot-piedra`; definir cómo se marca la venta por anuncio; pago de Meta; los dos de «marcar #vendido / #perdido» (reemplazados por el teléfono en Vender).
Aprendizajes (errores o trucos para no repetir):
- Leer `CONTEXTO.md` del repo antes de proponer: la propuesta inicial rehacía algo que ya existía.
- WhatsApp Web: no tocar la pestaña si Tomás la está usando; guarda de chat antes de cada envío.
- VM: `TMPDIR` y caché de npm en `/tmp`; esbuild propio para tests sueltos; `tsc` y los e2e van en un `.cmd`.
- Meta: `account_status` 9 y «Actividad de pagos» en cada lectura.
Próximo paso: en un chat nuevo, terminar las pruebas de Erasmo (con `#reset` antes) y juntar las decisiones de Fran — Modelo: —
Cambia una regla de plata o del método: no

## 11/11 11:25–11:45 — Plan de videos nuevos (ángulos + qué es viral)
- Pedido de Tomás: buscar más ángulos, ver qué es viral y plantear los videos («ahora tengo créditos para gastar»).
- Hecho: planteo de 11 videos en `claude/plan-videos-2026-11-11.md` del proyecto: 7 reales con los lentes (1 bolsa = 1 metro, cuántas bolsas entran, mojada vs. seca, vení a elegir, del chat a tu casa, antes y después real, serie una piedra por día), 2 a cámara y 2 con código (cuenta regresiva a las fiestas, el error de los 3 cm). Basado en la lectura de pauta (ganan los videos reales de entrega y la granza) y en una búsqueda web de formatos.
- La cuenta de Higgsfield conectada da 0 créditos (plan free): no se sabe a qué créditos se refiere.
- Nada producido: faltan los guiones palabra por palabra y filmar.
- 11:37 Tomás aclaró que quiere **reels con código** (no videos reales). Plan rehecho: lote de 12 reels (35 a 46) en `claude/plan-videos-2026-11-11.md`. Criterio: en la pauta rinden «un producto + un uso + un dolor» (R11 Granza gris $368; frente, laja ocre, adoquín) y no los informativos (cuántas bolsas, cuánto pesa, cómo medir). Las ideas de video real quedaron en un anexo.
- 12:04 Tomás aprobó el lote («vamos con eso») y pidió un solo prompt. Prompt de VS Code escrito: `E:\anuncios somos piedra\reels\PROMPT-vscode-2026-11-11c-formatos-nuevos.md` (copia en el proyecto, `claude/prompt-vscode-2026-11-11c-formatos-nuevos.md`). Corrida `2026-11-11c`, sesión «piedra-codigo-4», base la sesión 10a, misma voz. 12 reels (35 a 46) + 6 arranques alternativos (35, 41 y 42), salida en `reels\lote-2026-11-12\`.
- Cambios contra el plan, para no usar datos sin confirmar: el 35 no dice cuántas semanas faltan (el anuncio quedaría viejo); el 39 pasó de «camino a la pileta» a «¿Regás la tierra para que no vuele?»; el 40 es el patio de noche (el fogón es decorado, no un uso); el 46 es adoquín en la entrada, armado pieza por pieza (no vereda). No se incluyó «qué te llevás con $X» (sigue la regla del precio en el chat).

Decisiones (qué y por qué):
- Lote por formato visual distinto y no por más variaciones del mismo estilo: el lote 10a ya repite el estilo del 11 y Meta encarece creativos parecidos.
- Sin reels informativos: cuántas bolsas, cuánto pesa y cómo medir no trajeron conversaciones.

## 11/11 12:20 — Erasmo: lo que faltaba probar, dos arreglos en el bot y los e2e del panel (chat nuevo)
- `/salud`: reglas `db50529e`, modo tester, arranque 08:51. Probado desde el WhatsApp de Tomás: la cuenta 298 440-9447 está en el deviceId `dc5ada73…`, que hoy figura como «Browser 1» (identificado por `last-wid-md`, no por el nombre). 9 mensajes y 4 `#reset`; cada envío verificó el chat y mandó en un solo paso de JS (título «Somos Piedra», no grupo, autores `tomy` / `Somos Piedra`, caja vacía).
  | Mensaje | Qué hizo Erasmo | |
  |---|---|---|
  | «cuánto sale la granza blanca para 10 m2?» | Saludo, «Sí, te paso los precios:», 10 bolsas, **$200.000 / $250.000**, «Lo necesitabas para el patio, el frente o una pared?» y catálogo | bien (10 × $20.000 y 10 × $25.000) |
  | «y con factura?» | «Con factura te queda en **$242.000** en efectivo o transferencia y **$302.500** con tarjeta.» Sin repetir la pregunta | bien (+21 %) |
  | «se puede pagar en cuotas?» | «Por ahora no tenemos cuotas, con tarjeta es en un pago.» y **repite «Lo necesitabas para el patio, el frente o una pared?»** | la respuesta bien; **la pregunta repetida, mal** |
  | «bueno, lo pienso» | «Dale, no hay problema!» / «Qué es lo que te hace dudar, el precio o la piedra?» | bien |
  | «no sé, lo voy a pensar y te aviso» (segundo) | «Dale, cualquier duda me escribís por acá.» | bien: no insiste |
  | «igual en 15 días arranco la obra» | «Genial, buenísimo!» / pregunta retiro o envío. No promete escribir. **No quedó `agendar_seguimiento`** | **mal: no agenda** |
  | (reset) «precio de la granza gris para 8 m2?» | Granza gris Tandil, 8 bolsas, **$176.000 / $216.000** | bien (8 × $22.000 y 8 × $27.000) |
  | «dale, lo pienso. en 15 días arranco la obra» | Contesta igual que el ejemplo de las reglas. **Tampoco quedó `agendar_seguimiento`** (2 de 2) | **mal** |
  | (reset) «soy de Canteras del Sur, les paso la lista de precios de laja de San Juan» | Silencio y escala: «proveedor (Canteras del Sur) ofrece lista de precios de laja de San Juan» | bien |
- **Arreglo 1, pregunta repetida** (`src/salida.js`): `sinLoYaDicho` ahora saca de cada texto la pregunta que la cuenta ya hizo en el chat (igual o con otra puntuación; de 12 letras o más, así «Cómo estás?» no cuenta) y sale lo demás. No gasta otra llamada. La regla del prompt sola no alcanzó.
- **Arreglo 2, seguimiento** (`src/cerebro.js`, `pensar`): las herramientas de datos que venían en la **misma** respuesta que `responder` solo corrían si la guardia frenaba; si no, se perdían sin dejar rastro (`herramientas` decía solo `responder`). Ahora corren antes de la guardia; si una falla, no sale nada y Sonnet ve el error. **Es la causa probable** de que no agendara (Sonnet copia el ejemplo «`agendar_seguimiento` y responder»), pero no se pudo comprobar: el registro no guarda la respuesta cruda. Se confirma con la prueba en vivo después de reiniciar.
- Tests: 7 casos nuevos (4 en `test/piedra-sonnet.test.js`, 3 en `test/erasmo-tester.test.js`), escritos antes del arreglo y vistos fallar. Los 31 archivos de `npm test` en verde, corridos de a uno en la VM (la corrida entera no entra en 3 minutos). Commit `082f0b3` en `piedra/archivos-excluidos`, sin push. **Erasmo sigue con el código viejo hasta que Tomás lo reinicie.**
- Observación: «Cuotas» sigue en la lista de «Lo que siempre escalás» de `src/cerebro-reglas.md`, pero la regla de Fran del 06/11 dice contestar que no hay; Erasmo contestó (bien). Conviene sacarla de la lista cuando se unifiquen las reglas.
- **e2e del panel, los cuatro en verde sobre `b6cb9af`:** `e2e:corte` 24 pasos (44 s), `e2e:empleados` 12 (30 s), `e2e:meta` 11 (21 s), `e2e:piedra` 40 (96 s), todos con salida 0. Corrieron en una copia de Linux en `/tmp` de la VM con Chromium 153 por npm y Google Fonts reemplazado por una hoja vacía (la VM lo bloquea; sin eso los pasos daban ok y el e2e salía con 1 por el error de consola). Receta y scripts en `herramientas/e2e-panel-vm/`. No es Chrome de Windows ni producción. `CONTEXTO.md` §8 del panel actualizado (commit `28e091d`, sin push).
- Gasto de Sonnet en las pruebas: `usdHoy` pasó de US$0,059 a US$0,157.

Pendientes que deja:
- [ ] Reiniciar a Erasmo (toma `082f0b3`) — Tomás. Después Claude repite «se puede pagar en cuotas?» y «en 15 días arranco» y mira que quede `agendar_seguimiento` en el registro.

Próximo paso: con Erasmo reiniciado, las dos pruebas en vivo (3 a 5 mensajes). Si sigue sin agendar, la causa es otra (Sonnet no llama a la herramienta) y se ajusta por ahí — Modelo: —
