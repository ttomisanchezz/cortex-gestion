
TAREA PROGRAMADA — somos-piedra — 20/11 10:25 — Reels 11e (11–17/12) en Business Suite

Hecho:
- Leído el Cortex y los aprendizajes de Business Suite. Los 14 videos (L14-64…75, 42b, 42c) y el json de textos quedaron stageados.
- NO se programó nada: no hay ningún Chrome conectado a la extensión (list_connected_browsers vacío durante ~5 min; el b74c0df9… no aparece). Sin Chrome no hay sesión de Business Suite ni la ayuda h14.
Ojo antes de reintentar:
- Según pendientes (19/11 08:35), los 14 ya están programados en **Instagram** por Upload-Post (perfil SOMOSPIEDRA, 18:00 y 20:30). Si además se programan FB + IG en Business Suite, IG sale duplicado. Recomendado: en Business Suite programar **solo Facebook** (página «Somos Piedra, elija piedra»), que es lo que falta desde el 11/12.
- En textos-L14-2026-11-12.json, 42b y 42c tienen el mismo texto que el 42: armar las primeras frases a mano («Pedir granza te lleva 3 mensajes.» / «¿Nunca pediste granza? Es así de fácil.»).
Pendiente:
- [ ] Programar en Business Suite los 14 reels de la 11e para FB (11–17/12, 18:00 y 20:30) con Chrome Browser 1 conectado — Claude (Tomás: abrir Chrome con la extensión)
Cambia una regla de plata o del método: no

CIERRE — somos-piedra — 20/11 13:30 — Panel: Excel ↔ panel bloqueado y Supabase del panel sin encontrar (chat de repuesto 19–20/11)

Hecho:
- Panel: lo bloquea la corrida 2026-11-17b (Excel ↔ panel). Sus 7 prompts están en `E:\somos-piedra-panel\prompts\2026-11-17b\`. Cortó 2 veces porque `datos\dia-a-dia\` está vacía. Los intentos quedaron apartados en `.sesiones\_2026-11-17b-intento1` e `_intento2`: se relanza limpio con `LANZAR.md` cuando esté el Excel.
- Supabase del panel `msanpdcnkroqczwosocr`: no aparece en ninguna cuenta revisada (la del conector, la de Franco, tomassanchez2018, tominicoaxel). Vercel → Storage está vacío. `appsomospiedra` NO es el panel. Falta probar sciollatomas@gmail.com (cuenta de Vercel del panel) y GitHub ttomisanchezz.
Decisiones (qué y por qué):
- Ninguna. Queda SIN decidir una propuesta: Google Sheets en vez del Excel, para que la sincronización sea instantánea en las dos direcciones y no dependa de una PC prendida. Costo: el papá de Fran abre la planilla en Sheets. Si Tomás dice Sheets, se reescribe la 17b; si dice Excel, copia el archivo y se relanza.
- Si el Supabase no aparece: Supabase nuevo y mudar el panel, solo con OK de Tomás.
Pendientes nuevos:
- [ ] Encontrar la cuenta de Supabase `msanpdcnkroqczwosocr` (probar sciollatomas@gmail.com y GitHub ttomisanchezz) — Claude (Tomás: login/2FA si hace falta)
- [ ] Decidir Sheets o Excel para sincronizar con el panel — Tomás
- [ ] Pasar el Excel a `E:\somos-piedra-panel\datos\dia-a-dia\` (si es Excel) y relanzar la 17b limpia — Tomás → Claude
- [ ] Prompt para arreglar `api/` de Vercel (no urge) — Claude
Pendientes cerrados:
- ninguno
Aprendizajes:
- Anotar siempre con qué cuenta se crea cada servicio (Supabase, Vercel, Upload-Post, etc.): hoy no se sabe en qué cuenta quedó el Supabase del panel.
Próximo paso: encontrar la cuenta del Supabase y que Tomás decida Sheets o Excel — Modelo: Sonnet 5.5 + advisor (esquema y sincronización del panel)
Cambia una regla de plata o del método: sí, una línea en `metodo/` §7 (anotar la cuenta de cada servicio)
