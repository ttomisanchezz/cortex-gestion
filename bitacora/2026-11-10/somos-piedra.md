
CIERRE — somos-piedra (Erasmo) — 10/11 21:25

Hecho:
- Erasmo no recibía mensajes en vivo: causa = bug de Baileys (WhatsApp manda los estados como stanza <status> de nivel superior, Baileys no la confirma y el servidor retiene lo entrante; "stream errored out" ack class="status", evolution-api #2778). Se aplicó el parche de 3 líneas (ack de CB:status) adentro del contenedor evolution_api (Baileys 7.0.0-rc14) y se reinició: recibe en vivo, sin QR. El webhook global a Chiara (403) NO era el problema.
- Herramientas de diagnóstico en E:\bot-piedra\herramientas\diagnostico\ (DIAGNOSTICO-EVOLUTION, LOG-RECIENTE, REINICIAR-INSTANCIA-PIEDRA, APLICAR-PARCHE-STATUS).
- ERASMO_PASSWORD del .env era el texto de ejemplo: Supabase devolvía 400 y Erasmo solo cotizaba granza. Tomás cargó la clave; login 200 y lee los 41 productos del panel.
- Tester nuevo 298 440-9447 (WhatsApp Web en el Chrome «Browser 3»); NUMEROS_TESTER=5492994295806,5492984409447. Claude testea desde ahí.
- Reglas de Erasmo (src/cerebro-reglas.md + aviso de cotizar en src/herramientas-erasmo.js), formato de Fran: cotización en un mensaje con emojis 🪨📦💵💳🧾, solo totales (sin c/u), nunca "sin factura" (cierra "🧾 + IVA si necesitás factura"), sin desperdicio, la línea 📦 solo en granza/cajas; charla: saludo + "Sí, te paso los precios:" + cotización + "¿para qué lo necesitabas?" + catálogo; repreguntas de tarjeta/factura = una línea; sin cuotas por ahora; no dice "una persona del local"; modo setter (no da ventas por perdidas: "caro" y "lo pienso" siguen con preguntas de la obra).
- Test (13 casos) con montos correctos: granza 6/12/25 m², adoquines ojito 10 m², pizarra 4 x 2,8, tarjeta, factura, envío y cheque (escala), caro, lo pienso, "quiero más información", bolsón, pegamento.

Decisiones (qué y por qué):
- Formato de cotización de Fran (10/11): totales sin c/u; nunca "sin factura" (por AFIP) → "+ IVA si necesitás factura"; sin desperdicio en ninguna venta.
- Charla tipo Chiara y rol de setter (Tomás, 10/11): saludo cálido, precios, pregunta de uso, catálogo; no se da una venta por perdida.
- Cuotas: por ahora no hay (Fran 06/11, posnet en trámite).

Pendientes nuevos:
- [ ] Reiniciar a Erasmo y testear las reglas de setter ("caro", "lo pienso") — Tomás reinicia / Claude testea
- [ ] Fran decide: mensaje de espera al escalar, recomendaciones por uso, preguntar variante, tramos de granza, velocidad (60–90 s) — Fran
- [ ] Reactivación de Erasmo (como Chiara: 2 mensajes al cliente que dejó de contestar) — Claude, con OK de Tomás
- [ ] Sumar el parche de Baileys a la imagen evolution-api-baileys-fix (si se recrea el contenedor se pierde) — Claude arma, Tomás corre
- [ ] Commit en E:\bot-piedra de reglas, herramientas-erasmo y herramientas\diagnostico — Tomás (git desde Cowork deja locks)
- [ ] reglas/cerebro-reglas-piedra.md (texto aprobado 06/11) quedó desfasado de src/cerebro-reglas.md — decidir cuál es la fuente — Tomás
- [ ] Buscador: "adoquines" no encuentra "Micosa Adoquin"/"Porfido Adoquin" (singular/plural) — Claude
- [ ] Fotos de productos por WhatsApp (hoy solo catálogo PDF) — Tomás decide prioridad

Pendientes cerrados:
- Erasmo a tester: precios del panel, tester, cerebro ↔ cotizador, catálogo, escalado al grupo (cerrado 10/11).
- Darle empresa/rol al usuario de Erasmo (ya es miembro bot de somos-piedra).

Aprendizajes:
- Instancia "open" que no recibe = mirar el log de Evolution por "stream errored out" con ack class="status": es Baileys sin ack de <status>, no el webhook. Reiniciar la instancia solo entrega la ráfaga retenida.
- Antes de culpar al cerebro cuando "no figura un producto", mirar el login del panel en los logs de Supabase (400 en /auth/v1/token).
- Las reglas del cerebro se leen al arrancar: cada cambio necesita reiniciar a Erasmo; verificar el hash en /salud.
- Desde Cowork, npm test necesita TMPDIR=/tmp (el disco de la sesión se llena y los mnt no dejan borrar).

Próximo paso: chat nuevo, reiniciar Erasmo y seguir el test (setter + casos nuevos) — Modelo: —
Cambia una regla de plata o del método: no

## Lectura del 10/11 cerrado (00:10 del 11/11, sin OK por pedido de Tomás)
- Día: $138.231 / 104 conv = $1.329 (> $1.200) → ESCALA NO sube (sigue $30.000).
- ESCALA: L1-R1 $33.950/31 ($1.095), L2-C1 $7.233/4 ($1.808), L3-V3 $387/0 (no tocados: CBO de 1 día). MADRE $39.683/34, no se toca.
- Pasan a la ESCALA (mismo post, < $800 con 2+ conv): R11 Granza gris ($368, 7), R14 Laja ocre ($774, 3), R08 Tu frente ($732, 3). Siguen también en el test.
- Pausados (> $1.200/conv): R03, N2, N4, R01, R15, R12, R20 (1 conv con ~$1.750–2.480) y TEST REELS «R4 Lote 3» ($14.386/8 = $1.798) → TEST REELS queda sin gasto.
- Siguen sin conv pero bajo $3.000 (se juzgan con el 11/11): N1, N3, N6, R16, R18, R19, VG3-H1. Siguen: R13 ($833/3), N5 ($1.074/2), R17 ($1.060/2).
- Inconsistencia de la regla para revisar con Tomás: con 1 conv y >$1.200 se corta, con 0 conv se espera a $3.000.
- Prompt nuevo listo: reels\PROMPT-vscode-2026-11-10a-variaciones-granza.md (14 reels: 8 granza + 2 de R08, R13, R14), lote-2026-11-11.
