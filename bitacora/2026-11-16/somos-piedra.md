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
