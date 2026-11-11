
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
