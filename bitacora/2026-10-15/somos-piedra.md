CIERRE — somos-piedra — 15/10 10:26

Hecho:
- 4 carruseles del Día de la Madre hechos y publicados en Instagram. Zips en `E:\anuncios somos piedra\dia-de-la-madre\`; textos y mensajes de WhatsApp de cada carrusel en `LEEME-textos.txt`.
- Propuesta conjunta Somos Piedra + Somos Vivero (doc + PDF): Fase 1 Día de la Madre, Fase 2 sorteo cruzado, Fase 3 escalar.
- Meta ya ve la cuenta de Piedra (1945796639629607) y su página "Somos Piedra, elija piedra" (1025898313949204). El IG @somospiedranqn NO está vinculado a la cuenta ni a la página (`ads_get_ig_accounts` = []).
- En Meta, en BORRADOR (nada activo, no gasta): campaña 120250805457440411 "Somos Piedra + Vivero - Día de la Madre - WhatsApp - Oct 2026" (OUTCOME_ENGAGEMENT, CBO $10.000/día, fin sáb 17/10 23:59) y conjunto 120250805473960411 "Toda la zona - abierto" (CONVERSATIONS / WHATSAPP, misma zona que la campaña del 13/10). Faltan los 4 anuncios.

Decisiones (qué y por qué):
- Presupuesto $10.000/día en total: $5.000 de Somos Piedra y $5.000 de Somos Vivero.
- La campaña termina el sábado 17/10 a las 23:59 (Día de la Madre).
- El destino de WhatsApp es el del vivero (299 404-1698, el de los creativos).
- La campaña de Piedra del 13/10 (120250759505930411, $10.000/día) sigue corriendo y no se toca.
- Tomás carga el saldo después: primero se arma toda la campaña. Se activa solo con su OK.

Pendientes nuevos:
- [ ] Vincular el IG @somospiedranqn a la página y a la cuenta publicitaria en Business Suite (o subir las imágenes a la Biblioteca de Ads Manager) y avisar — Tomás
- [ ] Armar los 4 anuncios (mensaje de WhatsApp precargado distinto por carrusel), mostrar el plan y activar solo con el OK de Tomás — Claude
- [ ] Número de WhatsApp: el de la página es 299 459-0936 y el de los creativos 299 404-1698; hace falta el enlace wa.me del del vivero — Claude / Tomás
- [ ] Confirmar con el vivero: nombres de las plantas, que el precio incluye maceta y granza, y el sello "OFERTA" solo si hay oferta real — Tomás
- [ ] Recargar saldo (~$40.000 para 4 días) y cobrarle al vivero su mitad — Tomás

Pendientes cerrados:
- Ninguno.

Aprendizajes (errores o trucos para no repetir):
- Para promocionar posts de IG hay que vincular el IG a la cuenta publicitaria y a la página. Si el post es collab con otra cuenta (el vivero), además hace falta el permiso de partnership (`ads_ig_partnership_permission_manager`).
- Meta solo sube imágenes por URL pública y la subida local no está habilitada para esta cuenta; el contenedor no tiene salida a internet. La vía que sí anduvo es subirlas desde Chrome (ver 13/10).

Próximo paso: Tomás vincula el IG (o sube las imágenes) y avisa; Claude arma los 4 anuncios y activa solo con su OK — Modelo: —
Cambia una regla de plata o del método: no

Actualización 15/10 ~11:30 (misma sesión, campaña conjunta):
- El IG sigue sin vincularse, pero no hace falta: las 21 tarjetas del Día de la Madre se suben como carruseles nuevos. Quedaron en JPG en `E:\anuncios somos piedra\dia-de-la-madre\_subir\` (dm-c1-01 … dm-c4-05; c1=6, c2=5, c3=5, c4=5 tarjetas).
- En Chrome: el Browser 2 abre la cuenta de Somos iPhone (2044879766141120); la de Somos Piedra (1945796639629607) abre en el Browser 1. Hay que verificar `act=` y reseleccionar el Browser 1 si la extensión vuelve al otro.
- Creado el anuncio vacío en borrador 120250806149670411 "C1 Rincon verde - pack para mama" en el conjunto 120250805473960411 (formato Secuencia, CTA Enviar mensaje de WhatsApp).
- **BLOQUEO:** Meta pide autenticar la identidad (error #3858385, por actividad reciente de inicio de sesión): no deja crear ni modificar anuncios hasta que Tomás la complete en el Administrador de anuncios. Los anuncios actuales siguen en circulación.
- El número de WhatsApp se elige en el conjunto de anuncios, no en el anuncio. Decisión abierta: el 459-0936 de la página o el 404-1698 del vivero (el de las tarjetas).

Actualización 15/10 ~12:00 (campaña conjunta — anuncios armados, SIN activar):
- Tomás autenticó la identidad en Meta: el bloqueo #3858385 se levantó.
- 21 tarjetas subidas a la biblioteca de la cuenta 1945796639629607 (dm-c1-01 … dm-c4-05). Se subieron desde Chrome (Browser 1) con file_upload.
- 4 anuncios creados por API en el conjunto 120250805473960411, en pausa: C1 120250806315930411, C2 120250806300780411, C3 120250806306350411, C4 120250806307720411 (carruseles a WhatsApp, `multi_share_optimized:false`, título de tarjeta "Escribinos por WhatsApp", mensaje precargado distinto por carrusel). Sin errores de entrega.
- El conjunto manda los chats al WhatsApp 299 459-0936 (el de la página), NO al 404-1698 del vivero que figura en las tarjetas.
- Queda además un borrador de la interfaz, sin publicar, con el mismo C1 (id 120250806149670411): conviene descartarlo para no duplicar.
- La tarjeta 1 del carrusel 1 tiene sello "OFERTA DÍA DE LA MADRE": solo si hay oferta real (LEEME-textos).
- Aprendizajes: la API ve solo los anuncios publicados; lo que se arma en el editor queda como borrador de la interfaz. Para varios anuncios, subir las imágenes desde el editor (Subir + `file_upload`, parcheando `HTMLInputElement.prototype.click`, enganchando el input al DOM con un aria-label para poder usar `find`) y crear los anuncios por API con los hashes de `ads_get_ad_images`. La extensión de Chrome vuelve sola al Browser 2 (cuenta de Somos iPhone): reselecionar Browser 1 y verificar `act=1945796639629607` antes de tocar nada. Los screenshots fallan si la ventana no está en primer plano.

Actualización 15/10 ~14:45 (campaña conjunta — decisiones de Tomás y ajustes):
- Tomás respondió: el WhatsApp de destino tiene que ser el 299 404-1698 (vivero); el sello "OFERTA" se cambia (lo hace Claude); él confirma con el vivero nombres, precios y horarios; el borrador duplicado se descarta.
- Hecho: borrador de la interfaz 120250806149670411 eliminado (quedan 4 anuncios en el conjunto).
- Hecho: fecha de fin cargada en el conjunto 120250805473960411: sáb 17/10 23:59 (ART) = 2026-10-18T02:59:00+0000. Antes no tenía fin y habría corrido sin parar.
- Hecho: sello cambiado a "ESPECIAL DÍA DE LA MADRE" en la tarjeta 1 del C1 (imagen E:\anuncios somos piedra\dia-de-la-madre\_subir\dm-c1-01-especial.jpg, hash 4612c88258067157b9ee3634c87149a1). C1 nuevo = 120250806591170411; el C1 viejo con "OFERTA" (120250806315930411) quedó archivado.
- Estado de revisión: C2, C3 y C4 pasaron la revisión de Meta; el C1 nuevo está en proceso. Campaña y conjunto siguen en pausa.
- BLOQUEADO: el número de WhatsApp del conjunto no se puede cambiar ni por API (promoted_object no lo expone) ni en el editor ("Destino manual" de solo lectura). El conjunto manda los chats al 299 459-0936 (el de la página) y las tarjetas dicen 299 404-1698. Para resolverlo hay que vincular el 404-1698 a la página/portfolio (Tomás, con el código de WhatsApp) y crear un conjunto nuevo eligiéndolo, o bien cambiar el número de la última tarjeta a 459-0936.
- Aprendizaje: para subir una imagen a la biblioteca desde Chrome sin dejar nada publicado: abrir el editor de un anuncio, parchear HTMLInputElement.prototype.click, "Cambiar imagen" > "Subir", enganchar el input al DOM con aria-label, find + file_upload, y salir sin publicar; el hash sale de ads_get_ad_images. Para cambiar una imagen de un carrusel: crear el anuncio nuevo por API con el hash y archivar el viejo (los creativos son inmutables). Con un desplegable nativo abierto los screenshots se cuelgan: cerrarlo o navegar.

Actualización 15/10 ~12:00: Tomás decidió dejar todo como está: los chats van al 299 459-0936 (Somos Piedra) y él ve después cómo derivarlos al vivero. No se cambian las imágenes (la última tarjeta sigue con el 404-1698). No se vincula el 404-1698 por ahora (riesgo de afectar la campaña del 13/10); queda para la Fase 2.

Actualización 15/10 ~13:00 — CAMPAÑA CONJUNTA ACTIVADA (OK de Tomás):
- Tomás dijo: ACTIVA; el saldo lo carga él después; sacar de los carruseles los datos sin confirmar con el vivero (precios y horarios).
- Cambios en las tarjetas (11 imágenes nuevas en E:\anuncios somos piedra\dia-de-la-madre\_subir_v2\v2-*.jpg): se sacó la tarjeta de precios del C1 (ahora 5 tarjetas, contador n/5), el botón "Packs desde $30.000" de la tarjeta 1 pasó a "Escribinos por WhatsApp", se sacó "Horarios: 10 a 18 h" de la última tarjeta de los 4, y el sello OFERTA pasó a ESPECIAL en los 4. Textos de los anuncios sin precio ("Pack: planta + maceta + granza.").
- Anuncios nuevos (v2) ACTIVOS en el conjunto 120250805473960411: C1 120250807043320411, C2 120250807043650411, C3 120250807044920411, C4 120250807045860411. Esperando revisión de Meta (PENDING_REVIEW). Los 4 anteriores quedaron archivados (120250806315930411, 120250806591170411, 120250806300780411, 120250806306350411, 120250806307720411).
- Campaña 120250805457440411 y conjunto 120250805473960411 ACTIVOS. Presupuesto $10.000/día, fin sáb 17/10 23:59 verificado. Campaña del 13/10 (120250759505930411) sigue ACTIVA sin tocar.
- Destino de WhatsApp: 299 459-0936 (Somos Piedra). Tomás deriva al vivero.
- Saldo: lo carga Tomás después. Ojo: si no hay saldo la campaña no entrega. ~$30.000 para 15, 16 y 17/10; el vivero paga $15.000.
- Aprendizaje: sacar un dato de un carrusel obliga a recrear los anuncios (creativos inmutables) y a renumerar las tarjetas (n/N) si se saca una. Editar imágenes con PIL: tapar con el color plano, redibujar con Poppins; para fondos con foto usar cv2.inpaint. Subir varias imágenes juntas: poner multiple=true al input capturado.

Actualización 15/10 ~13:00: Tomás subió el presupuesto de la campaña conjunta a $20.000/día (antes $10.000). Verificado en Meta: 20.000 ARS. Ojo: el cambio de presupuesto por API pausó la campaña sola; se reactivó y quedó ACTIVA (campaña y conjunto). Aprendizaje: ads_update_entity recibe daily_budget en unidades menores (ARS x100: $20.000 = 2000000) y pausa la campaña al cambiarlo: reactivar siempre después y verificar. En el Administrador, "En preparación" es el estado de una campaña recién activada mientras Meta termina de procesarla/revisarla.

CIERRE — somos-piedra — 15/10 22:40 (sesión de estrategia creativa + madre/test)

Hecho:
- Estado de la campaña del 13/10 (sin analizar el Día de la Madre, a pedido de Tomás).
- Investigación (Google + Biblioteca de anuncios) y **8 ángulos nuevos** de carrusel en HTML + PNG 1080×1080 con fotos reales: A quincho, B pileta, C entrada/pórfido, D obras, E formas de pago, F guía "5 cosas antes de revestir", G reseñas, H local (47 PNG). En `E:\anuncios somos piedra\nuevos-8-angulos\` (textos, titulares y mensajes armados en `textos-y-mensajes.md`; generador `make-nuevos-8-angulos.py`). El ángulo 9 (antes y después) queda bloqueado: no hay fotos propias del "antes".
- Análisis de la campaña 120250759505930411: 4 anuncios en 1 conjunto; Meta concentró ~94% del gasto en C5 Granza + C1 Frente (C5 $14.212, C1 $6.405, C2 $1.035, C3 $437).
- Reestructura en Meta, **ya aplicada**: campaña 120250759505930411 renombrada "Somos Piedra - MADRE - C5 Granza + C1 Frente - Oct 2026", presupuesto $10.000 → **$5.000/día** (verificado en Meta), C2 (120250759610680411) y C3 (120250759612040411) **pausados**. C5 y C1 siguen activos; campaña ACTIVA.
Decisiones (qué y por qué):
- Estructura de testeo **1-1-3** (1 campaña, 1 conjunto, 3 anuncios) con todo el presupuesto en el conjunto, para que Meta elija el que mejor anda; **$5.000/día test + $5.000/día madre**; madre = C5 + C1; creativos nuevos = A quincho, B pileta, D obras.
Pendientes nuevos:
- [ ] Crear la campaña de test 1-1-3 con A, B y D ($5.000/día; mismo público y destino que "Toda la zona - abierto"; mensajes armados distintos por carrusel) — Claude — falta subir las 18 imágenes
- [ ] Subir las imágenes a Meta desde Chrome (vía del 13/10) o que las suba Tomás — Claude / Tomás
- [ ] Chequear saldo de la cuenta 1945796639629607 antes de activar — Tomás
- [ ] Confirmar con Fran lo de `textos-y-mensajes.md` (reseñas G, formas de pago E, horarios y stock H, "paletizado/Añelo" D, "Adoquín 10×10" C, % de cortes F) antes de publicar esos carruseles — Tomás / Fran
- [ ] Probar la generación de carruseles con la API de Higgsfield (saldo en 0,15 créditos; recargar) — Tomás / Claude
Pendientes cerrados:
- Ninguno.
Aprendizajes:
- El conector de Higgsfield mostraba 0,15 créditos aun cuando Tomás dice tener crédito por API: son cuentas/créditos distintos; con ese conector no se puede generar.
- Pausar anuncios y cambiar `daily_budget` por API no pausó la campaña esta vez (efectivo ACTIVA); igual verificar siempre.
Próximo paso: subir las 18 imágenes por Chrome y armar la campaña de test en borrador — Modelo: Sonnet 5.5
Cambia una regla de plata o del método: no

