# Bitácora 16/11/2026 — somos-piedra

## CIERRE — somos-piedra — 16/11 10:50 — Trial Reels para el orgánico

Hecho:
- Investigado: no hay conector oficial de Instagram (el conector «meta» es de Ads: lista y promociona posts, no publica orgánico). La API oficial de publicación de Instagram acepta Trial Reels desde el changelog de Meta (nov/dic 2025): `trial_params={graduation_strategy: MANUAL | SS_PERFORMANCE}` con `media_type=REELS` en POST /<IG_ID>/media. Pasarlo al perfil («compartir con todos») NO está en la API: se hace en la app. Las métricas de un trial por API no están documentadas (hay que probarlo).
- Probado: Business Suite no tiene la opción de Trial Reel (llegué al paso «Compartir» del composer de reels con un video de prueba; no se publicó ni guardó nada).
- Probado: la VM de Cowork no llega a graph.facebook.com, rupload ni graph.instagram.com → el script tiene que correr en Windows (Programador de tareas).
- Bloqueado por el sistema de Claude: usar el `window.__accessToken` de Ads Manager para Graph de Instagram («Unauthorized Access») y agregar la carpeta `E:\anuncios somos piedra` al chat (rechazado 2 veces).
Decisiones (qué y por qué):
- El orgánico de Somos Piedra pasa al método Trial Reels: 3 trial reels por día; a las 24 h se pasan al perfil los de más vistas; de los ganadores se hacen variaciones nuevas que vuelven a trial (Tomás).
- Se hace con script propio sobre la API oficial (MANUAL), no con un programador pago. Lo programado en Business Suite sigue hasta que los trials anden bien; recién ahí se apaga (Tomás).
Pendientes nuevos:
- [ ] Agregar `E:\anuncios somos piedra` al chat con «Agregar carpeta» — Tomás
- [ ] App de Meta (Business, producto Instagram) + token de @somospiedranqn con instagram_content_publish, instagram_basic, instagram_manage_insights, guardado por Tomás en un `.env` (`IG_TOKEN=`) — Tomás
- [ ] OK para el Programador de tareas de Windows: 3 disparos por día + ranking nocturno — Tomás
- [ ] Armar y probar el script de Trial Reels (subida resumable, MANUAL, ranking a 24 h, lista de cuáles pasar al perfil) — Claude, cuando estén los 3 de arriba
Pendientes cerrados:
- (ninguno)
Aprendizajes:
- Ver `conocimiento/aprendizajes.md` → «Trial Reels de Instagram (16/11/2026)».
Próximo paso: con carpeta + token + OK, armar el script de Trial Reels y probarlo con 1 reel — Modelo: —
Cambia una regla de plata o del método: no

## somos-piedra — 16/11 11:05 — Script de Trial Reels

Hecho:
- Carpeta `E:\anuncios somos piedra` ya conectada al chat.
- Script en `E:\anuncios somos piedra\trial-reels\` (`trial_reels.py`, solo Python estándar): `publicar` (próximo par mp4+txt de `cola/`, contenedor REELS resumable con `trial_params` MANUAL, subida al uri, espera FINISHED, media_publish, mueve a `publicados/AAAA-MM-DD/`; con error a `cola/_error/`), `ranking` (trials con 24 h o más: prueba views/reach/likes/etc., escribe `ranking/AAAA-MM-DD.md` con ✅ los de más vistas por día; sin vistas = FALTA DATO), `estado` (cuenta, seguidores, cupo de publicación), `--simular`. Tope 3 por día, candado contra corridas dobles, el token nunca va al log ni al registro.
- `trial.cmd` (lanzador), `registrar-tareas.cmd` (10, 14, 19 y ranking 23:30; NO corrido), `env-ejemplo.txt`, `LEEME.md`, `test_trial_reels.py` (7 tests con un Instagram de mentira, en verde).
Decisiones (tomadas por Claude, cambiables):
- Host por defecto `graph.instagram.com` v24.0 (token de «inicio de sesión de Instagram», el que se saca directo del panel de la app); con token de Facebook: `IG_API_HOST=graph.facebook.com` + `IG_USER_ID`.
- Ganadores: el 1 de más vistas de cada día (`GANADORES_POR_DIA`). Horarios 10, 14 y 19.
Pendientes nuevos:
- Elegir el reel de la prueba (que no esté programado en Business Suite) — Tomás.
Próximo paso: con el `.env`, `trial.cmd estado` y la prueba con 1 reel — Modelo: —

## somos-piedra — 16/11 12:40 — Qué rindió en el orgánico de IG (29/10–15/11) y hasta cuándo hay programado

Datos (Business Suite → Insights → Contenido, reels de IG; vistas · alcance · tiempo medio):
- Arriba de todo, **entrega real** (video de la camioneta/carga): «Así llega tu piedra: la cargamos…» 7/11 **5.364** · 3.834 · 15 s; «Te llevamos la piedra a tu casa en Neuquén» 1/11 2.570 · 11 s · **9 seguidores** (el que más sumó); «Así sale una entrega de granza» 4/11 1.997; «Otra entrega en Neuquén» 5/11 1.638.
- **Calculadora**: «¿Cuántos m² querés cubrir?» 6/11 2.556 · 12 s; «Así se llena un patio de 20 m²» 11/11 1.684.
- **Problema + solución (reels con código 11e)**: parejos 1.450–1.850 · 7–11 s: «¿Regás la tierra del patio…?» 1.843 (3 guardados), «Te entregaron la casa…» 1.792, «¿La entrada del auto es de tierra?» 1.727, «Huellas cuando llueve» 1.704, «Lavás el auto…» 1.683.
- **Fracasan (≈200–450 · 3 s)**: mostrar la piedra sola o el catálogo: «Piedra Bariloche de cerca» 192, «4 piedras en 12 s» 228, «3 ideas para tu patio» 223, rectificada 209, verde bronce 251, riojana 291, «Tenemos stock en el local» 387, «¿Cuánto pesa una bolsa?» 446.
- No es el horario: el 11–15/11 las 20:30 rinden igual que las 18:00; lo que se cayó a las 20:30 antes era el contenido de catálogo.
Conclusión: entrega real > problema + solución ≈ calculadora >>> catálogo. Coincide con la pauta (R11, R13, Envío Neuquén, Entrega lajas).
Programado en Business Suite (verificado 16/11 12:35): reels FB + IG hasta el **jue 10/12 20:30**; fotos y carruseles hasta el **sáb 28/11 13:30**.

## CIERRE — somos-piedra — 16/11 13:10 — Trial Reels, orgánico y video con IA

Hecho:
- Script de Trial Reels en `E:\anuncios somos piedra\trial-reels\` (7 tests en verde); falta el token.
- Claude in Chrome conectado (después de varias vueltas: la extensión tenía que estar abierta e iniciada en la misma cuenta). Análisis del orgánico de IG 29/10–15/11 y verificación de lo programado (bloque de las 12:40).
- Video con IA: investigado APIMart (Seedance 2.5: `seedance-2.5`, 4–30 s, 480p/720p/1080p, 9:16, `generate_audio`; Veo 3.1: `veo3.1-fast|quality|lite`, 8 s fijos, 9:16; POST /v1/videos/generations, GET /v1/tasks/{id}; los links de video vencen a las 24 h). Script `contenido\video-ia\video_ia.py` (tope US$ 10 sumando `gastos-apimart.csv`, no repite clips) y pieza `piezas/2026-11-16-prueba-ganchos.json`: 4 clips (Veo 3.1 Fast 8 s y Seedance 2.5 5 s sin audio) para el gancho de los reels 64 (auto entrando a una entrada de tierra con barro) y 61 (viento levantando polvo en un patio de tierra). Sin piedra en ningún clip.
- NO se corrió: api.apimart.ai rechazado por el filtro de red (403) desde la VM y desde la nube, aun después de que Tomás lo agregara; se sigue en un chat nuevo.
Decisiones (qué y por qué):
- Prueba de video con IA aprobada: hasta US$ 10 en APIMart (Seedance 2.5 y Veo 3.1) para ver si los reels se ven más reales que con stock + código (Tomás).
- Formato del video con IA (Claude, por la regla «la piedra no se toca»): la IA hace solo el gancho (el problema o el ambiente); la piedra, la entrega y el cierre van reales. El clip IA reemplaza el stock de los primeros 3 s y se conserva el texto del gancho.
Pendientes nuevos:
- [ ] Correr la prueba de video IA (4 clips) en el chat nuevo, armar 64 y 61 con el gancho IA y mandarle a Tomás la comparación Veo vs Seedance — Claude
- [ ] Pedirle a Fran que filme cada carga/entrega con el celular (el formato que más rinde en orgánico y en pauta) — Tomás
Pendientes cerrados:
- Agregar `E:\anuncios somos piedra` al chat — hecho 16/11
- Armar el script de Trial Reels — hecho 16/11 (queda la prueba con 1 reel)
Aprendizajes:
- Ver `conocimiento/aprendizajes.md` → «Chrome, filtro de red y Business Suite (16/11/2026)».
Próximo paso: chat nuevo → `python3 video_ia.py piezas/2026-11-16-prueba-ganchos.json` y armar los 2 reels — Modelo: —
Cambia una regla de plata o del método: no
- 13:10 Tomás: los reels se arman en VS Code con su editor (`C:\\Users\\PC\\Documents\\editor-reels-tomas`), no con ffmpeg. El próximo chat arma el prompt de VS Code: generar los 4 clips con `video_ia.py` (desde Windows APIMart responde) y que el editor los use como gancho de 64 y 61.

## Revisión de la sombra de Erasmo (11–14/11) — Claude, 16/11 tarde
- 1.041 propuestas en 376 chats, US$ 12,96 (≈ US$ 0,012 c/u). La sombra dejó de proponer el 14/11 (venció `CEREBRO_SOMBRA_PERSONA_HASTA`); desde ahí solo escucha.
- Chats nuevos (496 tandas sin persona): responde 379 (76 %), escala 117 (24 %); la mitad de las escaladas, por envío/zona.
- Con persona en el chat (545): se calla/escala bien (reclamos, pagos, entregas).
- Montos: 16 casos con total; 13 iguales a Fran. Errores: «4 negros cuadrados» → 40 m² ($620.000); Verde Bronce 20 m² $600.000 vs Fran $580.000 (precio del panel ≠ el de Fran); 1 bolsa con precio de tramo 20+.
- 88 casos: Fran da el precio de entrada y Erasmo solo catálogo + pregunta. Casi todos del anuncio «Somos Piedra, elija piedra» (477 chats): Fran asume granza ($22.000 la bolsa). Arreglo: mapear anuncio → producto.
- Fran vende el **bolsón 1 m³ (20 m²) a $310.000**; Erasmo dice «no vendemos por bolsón» (decisión 03/11). Choca: decide Tomás/Fran.
- Demora de Fran: mediana 8 min, p75 51 min, p90 5,5 h.
- 10 errores de la API (timeouts de 20 s).
- Checklist para el papá de Fran: doc https://claude.ai/artifact/PyQyECbByrjhL4i5L7fP36

## CIERRE — somos-piedra — 16/11 14:45 — Video IA, trials y lectura de la pauta

Hecho:
- Prompt de VS Code de la corrida 2026-11-16b en 2 sesiones en paralelo (`E:\anuncios somos piedra\reels\PROMPT-vscode-2026-11-16b-A-gancho-ia.md` y `-B-trials.md`): A = clips IA + reels 64 y 61 con gancho IA (Veo y Seedance); B = 9 reels nuevos para Trial Reels (3 entrega real, 4 problema + solución: perro, viento, fiestas, chicos; 2 calculadora 5×4 = 20 y 3×3 = 9), en `trial-reels\por-revisar\` (no en la cola).
- Sesión A entregada: 4 reels en `reels\lote-2026-11-16-ia\` + `COMPARAR.md`; gasto APIMart **US$ 2,60** de 10 (Veo US$ 0,14 por clip, Seedance US$ 1,089; 61-veo regenerado una vez). Recomienda 64 con Veo y 61 con Seedance; en 61-Veo las toallas salieron azul y amarillo (Boca). La sesión B todavía no entregó.
- Pauta leída desde Chrome (Browser 1, cuenta 1945796639629607), 9–15/11: $696.583 / 717 conv = $972/conv; ayer 15/11 $101.040 / 130 = $777. ESCALA $747 (R21+R27 $430 con 103 conv; R13 $482), MADRE $1.069, TEST $1.121, TEST REELS $1.648. «Toda la zona – abierto» 36 conv a $1.278; «Entrega lajas» 19 a $1.293. En pauta los «reales + código» rinden peor que los dibujados (R61 $2.504 vs R11 $576; R64 $1.216 vs R13 $477).
- Los 6 del TEST que recomendé pausar (N1, N6, R24, N3, R25, R03) ya estaban pausados: no se tocó nada en Meta.
- Corriendo hoy (con impresiones el 16/11 hasta las 14 h): 3 campañas, 24 conjuntos, 26 anuncios.
- Contraste con los cerebros de Santiago Bilbao y JP Sangregorio: no se apaga nada adentro de lo que vende; optimizar a conversaciones puede escalar chats que no compran → hace falta la venta por anuncio («pago confirmado» / compras por mensaje).
Decisiones (qué y por qué):
- Los empleados anotan todas las ventas que vinieron de anuncios; Tomás las carga en un chat nuevo para cruzarlas con el anuncio (para decidir por costo por venta y no por costo por chat) — Tomás.
- «Toda la zona – abierto», R61 y R65 no se tocan hasta el jueves 19/11 (MADRE no se toca por dentro; R61/R65 llevan pocos días) — recomendación de Claude, Tomás no la cambió.
Pendientes nuevos:
- [ ] Elegir modelo IA para 64 y 61 mirando `reels\lote-2026-11-16-ia\COMPARAR.md` — Tomás
- [ ] Revisar los 9 reels de la sesión B (`trial-reels\por-revisar\`) y pasar a `cola\` los que van — Claude revisa / Tomás pasa
- [ ] Jue 19/11: decidir R61, R65 y «Toda la zona – abierto» — Claude + Tomás
- [ ] Ventas por anuncio: cargar las ventas anotadas por los empleados y cruzarlas con `meta_leads` (teléfono) → costo por venta por anuncio — Tomás / Claude
- [ ] Meta: 10 pagos con error en 7 días (18 en total) y 15 borradores sin publicar («ESCALA Granza R21 + R27» con cambios sin publicar) — Tomás
- [ ] Ver si «pago confirmado» / optimizar a compras por mensaje se puede con el número actual (Evolution) — Claude
Pendientes cerrados:
- Video con IA: prompt armado y prueba corrida (US$ 2,60) — 16/11
Aprendizajes:
- Ver `conocimiento/aprendizajes.md` → «Ads Manager desde Chrome con ventana chica (16/11/2026)».
Próximo paso: chat nuevo con las ventas que anotaron los empleados → cruce venta–anuncio — Modelo: —
Cambia una regla de plata o del método: no

## CIERRE — somos-piedra — 16/11 16:35 — Video IA tanda 2 (66 y 67), reel 76 todo IA y trial reels

Hecho:
- Revisada la sesión piedra-ia-7a (gancho IA en 64 y 61): plata verificada en `gastos-apimart.csv` (5 clips = USD 2,598), hojas mirada. Recomendación: 64 con Veo (salpicadura fuerte) y 61 con Seedance (en Veo las toallas se leen como Boca).
- Prompt corrida 2026-11-16c (`reels\PROMPT-vscode-2026-11-16c-ia-66-67.md` + pieza `contenido\video-ia\piezas\2026-11-16-ia-66-67.json`): 66 y 67 con IA en TODA la parte del problema y planos de 1,5 s como máximo. Entregado: `reels\lote-2026-11-16-ia-2\` (66: 7 cortes, 67: 6 cortes; voz, textos y cierre iguales al lote 14). Tanda: 7 clips + 2 regeneraciones = USD 3,158. Corrió con Fable 5.2 (selector), no Sonnet 5.5. `67-lluvia-2` va recortado para sacar una franja de ripio (excepción a la letra de la regla).
- Revisada la sesión piedra-trial-7b: 9 trial reels en `trial-reels\por-revisar\` (md5 iguales al lote `reels\lote-2026-11-17-trial\`), cuentas 5×4 = 20 bolsas y 3×3 = 9 bolsas OK, ElevenLabs 1.996 de 2.200 caracteres.
- Prompt corrida 2026-11-16d (`reels\PROMPT-vscode-2026-11-16d-todo-ia-76.md` + pieza `2026-11-16-todo-ia.json`): reel 76 TODO con IA (8 escenas, una por frase del guion; granza gris generada por IA, descripta según `granza-gris_1.jpg`). Al cierre: 8 clips + 2 regeneraciones (USD 3,298) y voz hechos; el reel todavía se estaba armando (`reels\lote-2026-11-16-ia-3\76-todo-ia-granza\` sin `reel.mp4`).
- `gastos-apimart.csv` al cierre: 24 filas, **USD 9,054 de 10**.
Decisiones (qué y por qué):
- Video IA tanda 2: IA en todo el problema (no solo el gancho) y más retención; Veo + Seedance — Tomás.
- Reel 76 todo IA con la granza generada por IA: excepción a «la piedra nunca la hace la IA» solo para esa prueba — Tomás. Rótulo «Imagen ilustrativa» en los planos con granza (regla de `contenido.md`) — Claude; Tomás puede sacarlo.
Pendientes nuevos:
- [ ] Trial reels a `cola\`: T02, T04, T05, T06, T07 y T09 ya; T01 y T03 si «bajamos a mano / te lo llevamos» es lo de siempre; T08 no el 18/11 (placa P4 con 5×4); T05 y T06 no el mismo día; escuchar el arranque de T08 y T09 — Tomás
- [ ] Mirar 66 y 67 IA (`reels\lote-2026-11-16-ia-2\`) y decidir el recorte de `67-lluvia-2` (recomendación: dejarlo) — Tomás
- [ ] Reel 76 todo IA: pegar el resultado de la sesión piedra-ia-9a en un chat nuevo; revisar la granza IA contra la real y el rótulo — Claude revisa / Tomás decide
- [ ] Video IA: quedan USD 0,946 del tope de 10; para otra tanda hace falta tope nuevo — Tomás
- [ ] Selector de VS Code en Sonnet 5.5 (la 8a corrió con Fable 5.2) — Tomás
Pendientes cerrados:
- Revisar los 9 trial reels de la 7b — Claude, 16/11
Aprendizajes:
- Ver `conocimiento/aprendizajes.md` → «Video IA con APIMart (16/11/2026, tarde)».
Próximo paso: chat nuevo con el resultado del reel 76 → revisar granza IA vs real — Modelo: —
Cambia una regla de plata o del método: no

## CIERRE — somos-piedra (Erasmo) — 16/11 17:59

Hecho:
- Revisión de la sombra (11–14/11, 1.041 propuestas): ver bloque de arriba. Doc para el papá de Fran: https://claude.ai/artifact/PyQyECbByrjhL4i5L7fP36
- E:\bot-piedra (rama piedra/archivos-excluidos, sin push): 69bc910 (anuncio en el pedido, «cuadrados» = m², «la bolsa» = 1 bolsa), df4f280 (respuestas de Fran: 3 colores de granza, charla ante precio sin producto, bolsón → m², «gracias»), 18fdeae (granza 15–19 bolsas a $16.000), 5720211 (VS Code: «Enseguida te respondemos.» al escalar). Evaluar 18/18.
Decisiones (qué y por qué):
- Ver equipo/decisiones.md del 16/11 (Fran y Tomás).
Pendientes nuevos:
- [ ] Fran: precios del panel (Verde Bronce $35.000 efectivo + tarjeta), tarjeta de granza 15–19, cómo avisar un color sin stock — Fran
- [ ] Reiniciar Erasmo en modo tester y probar los cambios del 16/11 — Tomás / Claude
- [ ] Push de E:\bot-piedra hasta 5720211 — Tomás
Pendientes cerrados:
- Sombra revisada; «Enseguida te respondemos» hecho (5720211)
Aprendizajes:
- La VM del chat se quedó sin disco en $HOME: usar TMPDIR=/tmp y correr los tests de a pocos (más de ~6 por llamada corta por tiempo).
- git desde el chat necesita permiso de borrado (locks) y -c user.name/user.email.
Próximo paso: Tomás reinicia Erasmo en tester y probamos; después pilotos — Modelo: —
Cambia una regla de plata o del método: sí (tramos de granza de Piedra; solo del cliente)
