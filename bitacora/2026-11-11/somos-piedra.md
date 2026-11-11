
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
