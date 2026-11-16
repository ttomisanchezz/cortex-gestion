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
