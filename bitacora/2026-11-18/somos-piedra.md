# Bitácora 18/11/2026 — Somos Piedra

## CIERRE — somos-piedra — 18/11 00:40 (Erasmo sale para todos)

Hecho:
- Prueba en vivo desde el WhatsApp del tester (chat Somos Piedra +54 9 2994 59-0936 confirmado antes de escribir), todo OK: 10 bolsas granza gris a Plottier $200.000 + $45.000 = $245.000; General Roca escala; 15 bolsas granza roja con tarjeta $285.000; "necesito factura" después de tarjeta → $344.800 aclarando "con tarjeta en un pago"; envío Neuquén capital $35.000 → $379.800; primer "lo pienso" → pregunta qué lo hace dudar; segundo → las 2 frases de Fran tal cual.
- Con el OK de Tomás: `.env` de Erasmo con `CEREBRO_MODO=nuevos` y `NUMEROS_PILOTO=todos`; sin claves repetidas (quedan escucha/borrador false, un NUMEROS_TESTER y un GRUPO_AVISOS_JID). Respaldo en `E:\bot-piedra\data\env-respaldo-20261118.txt` (fuera de git).
- Audios: el código lee `GEMINI_API_KEY` y el `.env` solo tenía `GEMINI_IMAGEN_API_KEY` (el comentario del 02/11 decía que se había agregado, pero la línea no estaba) → "transcripción apagada". Se agregó `GEMINI_API_KEY` con el mismo valor. Sin probar (la VM no llega a Google; la key empieza con "AQ.").
- Crédito de Gemini (AI Studio, tomassanchez2018): USD 3,81. Estimado de audios: US$0,50–1,50 por semana.
- **Bug al prender `nuevos`:** anotar el anuncio (`state.obtener`) creaba el chat antes de `esChatNuevo`, así que NINGÚN chat nuevo contaba como nuevo y quedaban en sombra (le pasó al …6673 a las 00:25). Arreglado: se decide antes de anotar el anuncio. Test `test/piedra-nuevos-anuncio.test.js` (falló antes, pasa después), suite completa en verde. Commit `d19e0b7` en bot-piedra (sin push). Reiniciado con `ARRANCAR-PIEDRA.cmd` a las 00:35: EN VIVO PARA TODOS, modo nuevos.
- Tomás decidió no hacer `#sonnet-si` / `#sigue` al …6673: Erasmo solo contesta a los chats nuevos que lleguen desde ahora.

Decisiones (qué y por qué):
- Erasmo en vivo para todos los chats nuevos (18/11 00:35).
- Los chats que entraron antes del arreglo no se reactivan.

Pendientes nuevos: ver `pendientes.md` (18/11).
Pendientes cerrados: prueba de 10 min; "prendé para todos" y limpiar el `.env`.
Aprendizajes: ver `conocimiento/aprendizajes.md` (18/11).
Próximo paso: Claude mira el log (`data\consola.log`) a la mañana: primeras respuestas a clientes nuevos, que no queden en sombra, y la primera transcripción de audio — Modelo: —
Cambia una regla de plata o del método: no

---
CIERRE — somos-piedra — 19/11 07:40 (chat del 18/11 09:35; sin trabajo de Piedra)

Hecho:
- Favor para un amigo de Tomás (fuera del negocio): prompt para su Claude para conectar WhatsApp (Evolution API) a su dashboard de una petrolera, leer grupos en lista blanca y cargar las salidas al campo en el panel (extracción a JSON con FALTA_DATO, "a revisar", modo borrador, webhook con secreto, dedupe).
- Su Claude le pidió un servidor: se explicó que Evolution necesita estar prendido 24 h con URL pública (VPS de USD 5–7/mes, recomendado; o PC + Cloudflare Tunnel para probar). No usar el Evolution de Tomás (compartido con Somos iPhone y Erasmo, en vivo).
- No se pudo transcribir el audio del amigo (ver aprendizaje).

Decisiones (qué y por qué):
- Ninguna del negocio.
Pendientes nuevos: ninguno.
Pendientes cerrados: ninguno.
Aprendizajes: ver `conocimiento/aprendizajes.md` (19/11, audios).
Próximo paso: el de la entrada anterior (mirar el log de Erasmo) — Modelo: —
Cambia una regla de plata o del método: no


CIERRE — somos-piedra — 19/11 07:40 (sesión del 18/11, cotizaciones)

Hecho:
- Generador de cotizaciones en PDF rehecho copiando el diseño de la Cotización 0001 (Braidotti): `clientes/somos-piedra/presupuestos/cotizacion.py` + un `.json` por cotización + `README.md`. El generador de la otra sesión no apareció.
- Emite: Somos Piedra · Razón social Franco Nicolás Muñoz · CUIT 20-45734050-9 · Belgrano 3090, Neuquén Capital; firma «Somos Piedra» (antes Jesús R. Muñoz).
- Cotizaciones: 0001 Braidotti rehecha ($3.570.000, sin IVA); 0002 Comisión de Fomento El Sauce, 100 m² granza blanca MDP 10-30 mm, $1.625.000 «PRECIO FINAL»; 0003 El Sauce, 10 m² piedra ocre 10 cm, $250.000 «PRECIO FINAL» (Tomás no dijo el cliente: se asumió El Sauce).
- Bloque CLIENTE opcional: sin nombre ni CUIT, no va.
Decisiones (qué y por qué):
- Cliente en la cotización solo si Tomás lo pasa (los clientes cambian; no gastar tokens preguntando).
Pendientes nuevos:
- [ ] Confirmar el dígito verificador del CUIT (20-45734050-9; Tomás pasó 2045734050) — Tomás
- [ ] «Precio final» = ¿IVA incluido? (0002 y 0003) y si la granza va también en bolsas — Tomás
- [ ] 0003: ¿era para El Sauce o sin cliente? — Tomás
Pendientes cerrados:
- (ninguno)
Aprendizajes:
- Para cotizar: total que pasa Tomás ÷ cantidad = precio por unidad; el script calcula subtotal y total.
- No hacer grep sobre carpetas enteras de E:\ o el Cortex por la VM: se cuelga (timeout 120 s). Buscar en carpetas puntuales.
Próximo paso: las próximas cotizaciones salen con `cotizacion.py` (datos → PDF) — Modelo: —
Cambia una regla de plata o del método: no
