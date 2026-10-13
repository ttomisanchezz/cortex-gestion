CIERRE — somos-piedra — 13/10 11:10

Hecho:
- Revisadas las 24 placas de ChatGPT (`E:\anuncios somos piedra\nuevooss`): color de la piedra sin cambios (comparado con las de código), sin precio ni "envío gratis". No faltaba la placa 6 de c3: estaba en la carpeta de c2 ("Catálogo premium…-6"). c2 = 5 tarjetas, c3 = 7. Quedó "¿Dudas entre dos?" sin tilde (Tomás: dejarlo así).
- Copia ordenada para subir: `nuevooss\_subir\` (c1-01 … c5-06). Hojas de revisión en `nuevooss\_revision\`.
- **La pauta pasó a la cuenta de Somos Piedra (1945796639629607)**, la del Facebook "Somos Piedra, elija piedra". El conector de Meta se reconectó con ese Facebook.
- En esa cuenta: campaña "Somos Piedra - WhatsApp - Test 4 carruseles - Oct 2026" (id 120250759505930411, CBO), conjunto "Toda la zona - abierto" (id 120250759509110411: WhatsApp 299 459-0936, Neuquén +40 km, Roca, Añelo y Rincón +15 km, Advantage+ audience) y 4 carruseles con su texto y mensaje armado: C1 Frente (120250759603290411, 6 tarjetas, orden fijo), C2 Piedra (120250759610680411, 5), C3 Estilo (120250759612040411, 7), C5 Granza (120250759618840411, 6, orden fijo). Aprobados por Meta.
- Las 24 placas las subió Claude desde el Chrome de Somos Piedra (editor de un anuncio → Anuncio con imagen → Subir, de a 3).
- **Publicada el 13/10 ~10:56 con $10.000/día.** Tomás cargó $30.000 de fondos en la cuenta.

Decisiones (qué y por qué):
- La pauta va en la cuenta de Somos Piedra (1945796639629607) y no en la 2044879766141120, que es del Facebook de Somos iPhone (para no mezclar).
- Presupuesto de la campaña de carruseles: $10.000/día (antes $5.000).

Pendientes nuevos:
- [ ] Descartar el borrador vacío "Nuevo anuncio de Interacción" (120250759520900411) en la cuenta 1945796639629607 — Tomás
- [ ] Descartar los borradores de Somos Piedra en la cuenta vieja 2044879766141120 (campaña, conjunto y anuncio vacío; también hay 3 imágenes c1-01…03) — Tomás
- [ ] Revisar la campaña el lunes 20/10 (7 días sin tocar): costo por chat por carrusel y ventas (etiqueta "anuncio") — Tomás / Claude
- [ ] Fondos: con $10.000/día los $30.000 alcanzan unos 3 días (más impuestos): recargar antes del 16/10 — Tomás

Pendientes cerrados:
- Lanzar los carruseles (revisar placas, subirlas, armar los 4 anuncios, publicar).

Aprendizajes (errores o trucos para no repetir):
- Antes de pautar, confirmar de qué Facebook es la cuenta publicitaria: la 2044879766141120 era del Facebook de Somos iPhone.
- El conector de Meta ve solo las cuentas del Facebook con que se conectó. Para otra empresa, reconectarlo con su Facebook.
- Subir imágenes desde Chrome sí funciona: editor de un anuncio → Configurar contenido → Anuncio con imagen → Subir, tapando `HTMLInputElement.prototype.click` para que no abra el explorador y usando `file_upload` en el input nuevo que crea cada "Subir" (máximo 10 MB por tanda, ~3 placas). La biblioteca selecciona sola: deseleccionar al llegar a 9 (tope 10). Los archivos tienen que estar en el contenedor (staging).
- Con dos Chrome conectados, la extensión puede volver al otro: verificar el `act=` de la pestaña antes de tocar nada.
- Carrusel a WhatsApp por API: `link_data` con `child_attachments`, CTA `WHATSAPP_MESSAGE`, `page_welcome_message` con el mensaje armado, `multi_share_optimized:false` para orden fijo.

Próximo paso: el 20/10 revisar costo por chat y ventas de cada carrusel; apagar los 2 peores — Modelo: —
Cambia una regla de plata o del método: no
