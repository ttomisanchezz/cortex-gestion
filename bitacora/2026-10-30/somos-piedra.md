CIERRE — somos-piedra — 30/10 14:50

Hecho:
- Tarea programada «Ideas del día» (6:53): 9 ideas del 30/10 en `E:\anuncios somos piedra\contenido\ideas-dia\2026-10-30\` (3 carruseles y 3 placas en JPG + HTML, 3 reels en guion). A la mañana Higgsfield no tenía saldo: todo salió con fotos reales.
- Bocetos de 3 estilos con otras tipografías de Google (Tierra: Bricolage + Instrument Serif; Ficha de cantera: Big Shoulders + Plex Mono + Work Sans; Cuaderno de obra: Caveat Brush + Rubik): artifact https://claude.ai/artifact/XD2Hrs6a6bDGiSHHqGm8ms. Ninguno elegido todavía.
- Tomás cargó USD 5 en la API de Higgsfield y pidió generar todo lo posible: 15 escenas high 2k (~USD 4,20), en `contenido\salidas\ideas-2026-10-30\escenas\` con `BANCO.md`. Saldo en 0 al final (falló jardin-antes-yuyos).
- Carrusel A «Antes y después: chau patio de cemento» rearmado: portada partida antes (cemento) / después (granza gris) del mismo patio, opciones 2 y 3 en el mismo patio con laja ocre y granza roja. Placa A «¿Cálida o fría?» con la misma galería en ocre y verde bronce (escenas).
- 4 carruseles extra de antes y después con el banco: frente (ocre), quincho (verde bronce), entrada (adoquín) y pileta (riojana), en `ideas-dia\2026-10-30\extra-antes-y-despues\` (5 placas + texto.txt cada uno, indice.html).
Decisiones (qué y por qué):
- Antes y después con IA: se genera primero el «después» con la piedra real de referencia y el «antes» a partir del «después» (misma casa y luz, cambia solo la superficie). Siempre con el rótulo «Idea de diseño». Tope diario de la tarea: sigue en 3 escenas («no sumar por ahora»).
Pendientes nuevos:
- [ ] Programar en Business Suite las piezas del 30/10 (6 armadas + 4 extra + reel B) desde el vie 6/11 — chat nuevo
- [ ] Actualizar `ideas-dia\armar_dia.py` de la PC con soporte de escenas ("escena:<id>", "split" con fotos, carpeta de escenas, JPG livianos) — Claude
- [ ] Elegir uno de los 3 bocetos de estilo (o rotarlos) para sumarlo al armador — Tomás
- [ ] Fran: grabar reels A (camioneta) y C (rociador); confirmar horario del sábado, espesores y granza roja de Olavarría en stock — Fran / Tomás
Pendientes cerrados:
- Probar generación con la API de Higgsfield (15/10): hecho, fidelidad buena.
Aprendizajes:
- hf.py le agrega a todo prompt la regla de "la piedra igual a la referencia": para el «antes» hay que llamar a la API sin esa regla.
- En device_bash los procesos en segundo plano mueren al terminar la llamada: una escena por llamada (~2 min).
- El disco de la VM (/sessions) puede estar lleno: scripts temporales en /tmp.
- pieza.html con PNG de 2k pesa >30 MB y device_commit_files lo rechaza: pasar las escenas a JPG de 1200 px.
Próximo paso: programar las piezas del 30/10 en Business Suite desde el 6/11 — Modelo: —
Cambia una regla de plata o del método: no


CIERRE — somos-piedra — 30/10 14:55 (chat pauta y reels)

Hecho:
- Resumen de anuncios 29 y 30/10 vs 23-28/10 (Meta, por anuncio y día). 23-28/10 releído hoy: $147.358, 162 chats, $910/chat (el traspaso decía $127.363 y 122; la atribución de 7 días sumó chats). 29/10: $19.939, 22 chats, $906. C5 $981, C1 $744, R-A1 $727. Frecuencia 1,1-1,2 en todo.
- Plan de acción con /lauty-cardozo y /fran-doglio (bases leídas en E:\lauty-cardozo y E:\fran-doglio): no subir presupuesto a lo viejo; apagar R-A2 a R-A6; renovar con reels; medir ventas por anuncio (Doglio).
- Pausados R-A2 a R-A6 (con OK de Tomás) y después el TEST 1-3-6 entero (120250912907900411).
- Campaña nueva **TEST REELS** 120251035611560411 (CBO, WhatsApp, misma zona que T1): conjunto R1 Lote 1 (120251035617360411) con 4 reels y R2 Lote 2 (120251035618120411) con 3 nuevos clips. 7 anuncios con texto, título y botón de WhatsApp; salen en FB e IG. Prendida a $10.000 y subida a **$16.000/día** a pedido de Tomás.
- Total de pauta: MADRE $16.800 + TEST REELS $16.000 = **$32.800/día**.
- Orgánico: los 7 reels programados en Business Suite (FB + IG) a las 18:00, del sáb 31/10 al vie 6/11, con texto y hashtags (ver `contenido.md` o el traspaso).
- Videos comprimidos (<10 MB, 720x960) en `E:\anuncios somos piedra\EDITADOS\_para-meta\`.
Decisiones (qué y por qué):
- Reels en una CBO con dos conjuntos (lote 1 y lote 2) y no en dos campañas (Lauty: una CBO a la que se le suman conjuntos). Presupuesto $16.000/día (Tomás: "escalar drásticamente"). Reemplaza los $4.900 del 28/10.
- Se apagó todo el TEST 1-3-6; la MADRE sigue igual.
- Reels orgánicos: uno por día a las 18:00, para no pisar los de las 20:30.
Pendientes nuevos:
- [ ] Revisar TEST REELS a las 24 h (sáb 31/10 12:30, tarea programada): costo por chat por anuncio y lote; si un lote recibe <20% del gasto, gasto mínimo — Claude
- [ ] Mensaje armado de WhatsApp de cada reel ("Plantilla de mensaje" en Ads Manager; el conector no lo deja cargar) — Tomás o Claude por Chrome
- [ ] Descartar el borrador vacío "L1-R1" que quedó en Ads Manager de la prueba en la interfaz — Tomás
- [ ] Revisar el título de los reels orgánicos 2 a 7 (quedó vacío; es opcional) — nadie, solo si se quiere
Pendientes cerrados:
- Reels del 28/10: campaña de test armada y prendida, TEST 1-3-6 apagado.
Aprendizajes:
- Subir archivos a Meta desde Chrome sin que Tomás elija nada: stagear el archivo al contenedor (device_stage_files, queda en /mnt/user-data/uploads/...) y, en la página, interceptar con JS el click() del input file (HTMLInputElement.prototype.click y dispatchEvent) para dejarlo visible; después file_upload con ese ref. Tope 10 MB por llamada: comprimir antes con ffmpeg.
- El conector de Meta no sube archivos locales ni los videos de la PC; con los videos en la biblioteca de la cuenta sí crea creativos y anuncios.
- Cada cambio de presupuesto por el conector pausa la campaña: reactivar y verificar.
- El conector no muestra la cuenta de IG vinculada, pero los anuncios igual se publican en IG (effective_instagram_media_id).
Próximo paso: chat nuevo — programar las 10 piezas del 30/10 + reel B desde el 6/11 (ojo: el 6/11 ya tiene un reel a las 18:00) — Modelo: —
Cambia una regla de plata o del método: no
