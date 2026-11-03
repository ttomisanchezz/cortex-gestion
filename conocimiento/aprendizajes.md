# Aprendizajes
Errores que no queremos repetir y trucos que funcionaron. Cada uno con su fecha.

## Sesiones de Claude Code
- **08/10/2026 — No lanzar dos esquemas a la vez.** Se largaron a la vez `PROMPT-todo.md` (una sesión con subagentes) y los 9 prompts de `prompts/` (una sesión por rama). Quedaron unas 15 sesiones duplicadas. Una segunda "base" pisó `package.json` unos minutos, y varios `npm install` chocaron en el mismo worktree (`ENOTEMPTY`, paquetes incompletos). **Un solo esquema por corrida.**
- **08/10/2026 — La guarda `.sesiones/` funcionó.**
  - Cada sesión hace `mkdir <repo>\.sesiones\<nombre>` antes de tocar nada. Si ya existe, termina avisando "sesión duplicada".
  - El `npm install` va **después** de reservar, nunca antes.
  - Desde el 08/10 cada corrida tiene su id (`.sesiones\<corrida>\<nombre>`), así no hace falta borrar nada: el bloque "SI TENÉS QUE ELEGIR" frena ante los borrados.
- **08/10/2026 — Esperas en segundo plano.** `sleep 540` en primer plano gasta un turno cada 9 minutos. Hay que usar `until <condición>; do sleep 120; done` en segundo plano: no gasta turnos hasta que termina.
- **08/10/2026 — Señales con commits de mensaje exacto.** "fase A lista" para la base y "rama <nombre> lista" para cada rama. La integración espera los 7 con `git log --all --grep`.
- **08/10/2026 — Las señales llevan el id de la corrida.** "fase A lista" y "rama importador lista" ya estaban en el historial de `E:\vivero`: una rama nueva con el mismo nombre habría arrancado sola, sin esperar a la base. Desde la corrida 2026-10-08a: `base <corrida> lista` y `rama <nombre> <corrida> lista`.
- **08/10/2026 — Una pantalla que tocan varias ramas** (Vender, con 5 ramas) se parte en piezas en la base, un archivo por rama, para que los merges no choquen.

- **09/10/2026 — Corrida 2026-10-09a: unas 6 horas.** Base 2 h 10 (15:16 → 17:25), ramas de 40 min a 2 h 10, integración hasta las 21:00 aprox. Para estimar, sumar la base, la rama más larga y la integración.
- **09/10/2026 — `.claude/agents/` no existía en `E:\vivero`.** Las sesiones usaron `Plan` o `general-purpose` con Opus como advisor. Antes de la próxima corrida, crearlos o sacarlos del bloque de delegación.
- **09/10/2026 — Codex sin cupo** (hasta el 14/10): las sesiones lo reemplazaron con un revisor Opus de solo lectura. `/codex:review` lo lanza solo una persona.
- **09/10/2026 — Los prompts de las ramas tienen que nombrar el contrato de la base** (`contexto/multinegocio.md` §8 y su REVISAR), no solo la spec.
- 02/11/2026 — El control automático bloquea un `.cmd` que lanza `claude.cmd` con `--dangerously-skip-permissions`: las corridas se pegan a mano en VS Code, una sesión por prompt.
- 02/11/2026 — Antes de responder el estado de un sistema, mirar el repo real: el Cortex estaba atrasado (el panel de Piedra se había movido a `E:\somos-piedra-panel` y ya estaba en línea).

## Investigación de clientes
- **08/10/2026 — Buscar primero la presencia pública del cliente** (web, Guía Cores, Facebook, CUIT). En Somos Piedra mostró que también tiene vivero y que vende por m², bolsón, unidad y planta. Eso llevó la unidad al producto y cambió el diseño multi-negocio.
- **08/10/2026 — Una SAS no puede ser monotributista:** solo pueden las personas humanas y las sucesiones indivisas. Si el cliente es una SAS, es Responsable Inscripto.

## Plata
- **08/10/2026 — El IVA a favor no es ganancia.** En la prueba de punta a punta del vivero, el resultado ($35.563) daba más que la ganancia bruta ($28.773), porque el IVA a favor sumaba. Corregido: queda en $16.440.
- **08/10/2026 — La merma y los faltantes de arqueo son pérdidas reales.** La spec no los restaba y se corrigió. En cada spec nueva, chequear la fórmula del resultado contra el método §3.
- **08/10/2026 — Recibir una transferencia no tiene comisión.** Pedir un % para Banco dejaba el saldo en FALTA DATO sin motivo.

## Técnica
- 30/10/2026 — **Escenas de IA con hf.py (Somos Piedra):** hf.py suma a todo prompt la regla "la piedra igual a la referencia"; para un «antes» (sacar la piedra) hay que llamar a la API sin esa regla, usando hf.py como librería. Para que antes y después sean el mismo lugar, el «antes» se genera con el «después» como referencia.
- 30/10/2026 — **device_bash:** los procesos en segundo plano mueren al terminar la llamada (una escena por llamada, ~2 min); si /sessions está lleno, los scripts temporales van en /tmp.
- 30/10/2026 — **device_commit_files rechaza archivos de más de 30 MB:** un pieza.html con escenas PNG de 2k pesa ~42 MB; pasar las escenas a JPG de 1200 px (queda en ~5 MB).
- **08/10/2026 — Hosting:** Vercel Hobby no permite uso comercial.
- **08/10/2026 — Supabase gratis:** deja pocos proyectos activos y pausa los que no se usan.
- **08/10/2026 — La identidad git global de la PC es `frannnn87` (de Fran).** Los commits del vivero salieron con ese autor. En cada repo nuevo hay que configurar `user.name` y `user.email` locales.
- **08/10/2026 — Datos de prueba viejos:** en modo local, después de cambiar el esquema o las reglas, hay que borrar los datos del sitio en el navegador.
- **08/10/2026 — El Edge de la PC no está donde se esperaba.** La prueba de punta a punta usa Chrome: el script busca los dos.
- **08/10/2026 — Multi-negocio: los ids determinísticos llevan el negocio adentro.** `idArqueo(fecha)` o `idConfig(clave)` darían la misma pk para Ibero y Piedra el mismo día.
- **08/10/2026 — Commitear desde Cowork** pide permiso de borrado en la carpeta, porque git borra sus propios `.lock`.
- 02/11/2026 — La VM de Cowork no llega a Supabase (ni Postgres ni HTTPS: EAI_AGAIN). Para la base de un panel: el conector de Supabase (`execute_sql`) o un script del repo que corre Tomás en su PC (la contraseña la escribe él).

## Trabajo con Tomás
- **09/10/2026 — Si Tomás pega una plantilla de respuestas sin completar, preguntar antes de armar nada** (llegó "factura [persona / SAS] con el CUIT [__]").
- **09/10/2026 — Antes de armar prompts, cruzar las instrucciones del proyecto con el CLAUDE.md del Cortex.** Los modelos estaban contradichos (Sonnet vs. Fable/Opus) y no se avisó a tiempo. Ahora la regla vive solo en CLAUDE.md.
- **08/10/2026 — Tomás dicta por voz.** La transcripción cambia palabras: "video" por vivero, "corte" o "xottex" por Cortex, "Diphons" por iPhones, "useful code" por VS Code. Se interpreta por el contexto y, si no cierra, se pregunta.
- **08/10/2026 — Tomás quiere los prompts listos para pegar**, todos juntos, y ver en la tabla qué modelo va en cada sesión.

- 02/11/2026 — Antes de usar una escena del banco de IA, buscá su id en todas las carpetas de `ideas-dia` (incluidos los extra) y mirá el planificador: BANCO.md puede decir "libre" aunque ya esté en otra pieza.
- 02/11/2026 — ChatGPT Image cambia la piedra si solo le adjuntás las fotos: describila con palabras (forma, color, tamaño, "NOT rounded pebbles"). Con eso la granza salió fiel.
- 02/11/2026 — Business Suite desde Claude in Chrome: el input de archivo se crea al hacer clic. Parcheá `HTMLInputElement.prototype.click` para atraparlo, usá `file_upload` y después restaurá el original.

## Pauta para clientes
- 02/11/2026 — Subida de imágenes a Meta (ads_creative_upload_local_image): el `image_name` tiene que ser IGUAL al nombre del archivo que se sube (si no, «uploaded file metadata changed» y la sesión muere). Guardar el completion_token en `window` y leerlo de a 2 (la salida JS se corta ~400 caracteres). El fetch a rupload anda desde cualquier pestaña de business.facebook.com, aunque esté deslogueada.
- 02/11/2026 — Caption en el editor de Business Suite: pegarlo con un evento `paste` (DataTransfer text/plain) al elemento enfocado; respeta saltos de línea y emojis. Programar: fecha con el calendario y hora/minutos con un clic en cada campo (escribir «1100» de corrido pisa la hora).
- 02/11/2026 — `file_upload` de Chrome solo acepta archivos de /mnt/user-data/uploads (staged desde E:), no de outputs ni rutas de E: directo.
- 02/11/2026 — Meta API, CBO: crear el conjunto con `daily_min_spend_target` hace fallar la activación («minimum spend higher than budget»). Crear sin mínimo, activar y después ponerlo (centavos: 300000 = $3.000).
- 02/11/2026 — Videos para anuncios por API: comprimir a < 10 MB (ffmpeg CRF 30), subir a Higgsfield (`media_upload` + PUT + `media_confirm`) y pasar esa URL de cloudfront a `ads_creative_upload_media`. La API no ve la cuenta de IG ni carga el mensaje armado de WhatsApp.
- 02/11/2026 — Reels en Business Suite: «Crear reel» → interceptar input file → `file_upload` → texto → Siguiente ×2 → pestaña Programar → fecha dd/mm/aaaa y horas/minutos por separado (FB e IG).
- **30/10/2026 — Subir archivos a Meta o Business Suite desde Chrome sin que Tomás elija el archivo:** stagear el archivo al contenedor (`device_stage_files` → `/mnt/user-data/uploads/...`), en la página interceptar con JS `HTMLInputElement.prototype.click` y `dispatchEvent` del input file para dejarlo visible en el DOM, tocar el botón de subir y hacer `file_upload` con el ref del input. Tope 10 MB por llamada: comprimir antes (ffmpeg, 720 px, ~1,5 Mbps). Las rutas `E:\...` no sirven en `file_upload`.
- **30/10/2026 — Conector de Meta:** no sube archivos locales; con el video ya en la biblioteca de la cuenta crea creativo y anuncio. Cada cambio de presupuesto pausa la campaña (reactivar y verificar). Aunque no liste la cuenta de IG, los anuncios salen en IG.
- **09/10/2026 — Precios, impuestos, fees de gestión y método:** `conocimiento/pauta-precios-2026-10.md`.
- **09/10/2026 — Ver si el Facebook del cliente es una página o un perfil personal** antes de proponer anuncios: con un perfil no se puede anunciar.
- **09/10/2026 — Tarjetas de anuncios con código sobre fotos reales, no generadas con IA:** la IA cambia el color y las vetas de la piedra y equivoca letras. La IA, solo para retoques puntuales.
- **09/10/2026 — Links de Instagram:** al leerlos por JS salen bloqueados. Sirve abrir cada publicación en su pestaña con `location.href` desde la página; la URL aparece en el contexto de las pestañas.

- 09/10/2026 — **Bajar fotos de Instagram y Facebook para trabajar con código** (el contenedor no tiene red):
  - en la página de la publicación, las URLs originales están en el JSON de los `<script>` (`image_versions2`, con `carousel_media`); la API `web_profile_info` da 429;
  - en FB, abrir la foto y tomar el `<img>` más grande;
  - con JS: `fetch` → achicar a 1600 px con OffscreenCanvas → armar un .zip en la página → un solo `a.download` a Descargas;
  - pedir acceso a la carpeta Descargas y subir el zip al contenedor.
  No devolver URLs de fbcdn o cdninstagram en la salida: las bloquea el filtro.
- 09/10/2026 — **Fotos de la pauta:** el cliente prefiere ver la piedra **ya colocada** (paredes, frentes, pisos) antes que en la mano. Buscar primero un catálogo o PDF con obras. Los flyers del IG suelen tener imágenes de stock o IA: no usarlas. Preguntar siempre cómo se entrega (granel, pallet, cajas) antes de escribir textos de cantidades.
- 12/10/2026 (reemplazada el 13/10: desde Chrome sí se puede) — **Claude no puede subir imágenes a Meta:** rupload.facebook.com está bloqueado en el contenedor y en la PC, y GitHub no deja crear repos. Las sube Tomás a mano en el Administrador o se usa una URL pública.
- 12/10/2026 — **Página en un portfolio empresarial:** se suma gente por invitación de mail (Business Suite → Configuración → Personas). Los clics que dan permisos los bloquea el sistema de Claude: los termina Tomás.
- 12/10/2026 — **Conjunto de anuncios:** `location_types: home` y la edad sugerida con Advantage+ dan error; usar solo `custom_locations`. Un anuncio creado desde la UI toma por defecto el IG de otra cuenta: revisar Identidad.
- 12/10/2026 — **Archivos que "no aparecen":** buscar por hora de modificación; el reloj del Linux de Cowork está en UTC (+3 h respecto de Argentina).

- 13/10/2026 — **Confirmar de qué Facebook es la cuenta publicitaria** antes de pautar para un cliente: la 2044879766141120 resultó ser del Facebook de Somos iPhone. El conector de Meta ve solo las cuentas del Facebook con que se conectó: para otra empresa, reconectarlo con su Facebook.
- 13/10/2026 — **Claude sí puede subir imágenes a Meta desde Chrome** (reemplaza la del 12/10): editor de un anuncio → Configurar contenido → Anuncio con imagen → Subir. Tapar `HTMLInputElement.prototype.click` para que no abra el explorador, y en cada "Subir" usar `file_upload` sobre el input nuevo (máx. 10 MB por tanda, ~3 placas; los archivos tienen que estar en el contenedor). La biblioteca selecciona sola: deseleccionar al llegar a 9 (tope 10).
- 13/10/2026 — **Con dos Chrome conectados** la extensión puede volver al otro: verificar el `act=` de la pestaña antes de tocar nada.
- 13/10/2026 — **Carrusel a WhatsApp por API:** `link_data` con `child_attachments`, CTA `WHATSAPP_MESSAGE` (`app_destination: WHATSAPP`), `page_welcome_message` con el mensaje armado y `multi_share_optimized: false` para orden fijo.

- 15/10/2026 — **Promocionar un post de Instagram** requiere el IG vinculado a la cuenta publicitaria y a la página (Business Suite); `ads_get_ig_accounts` = [] significa que no está vinculado. Si el post es collab con otra cuenta, además el permiso de partnership (`ads_ig_partnership_permission_manager`).
- 15/10/2026 — **Imágenes a Meta:** por la API solo se suben por URL pública (la subida local no está habilitada para la cuenta de Piedra) y el contenedor no tiene salida a internet; la vía que anda es Chrome (ver 13/10).

- 15/10/2026 — **Meta Ads por API:** `daily_budget` va en unidades menores (ARS x100: $20.000 = 2000000; 20000 da "Budget Too Low"). Cambiar el presupuesto de una campaña la pasa a PAUSADA: reactivar con `ads_activate_entity` y verificar. En el Administrador "En preparación" es el estado transitorio mientras Meta procesa.
- 15/10/2026 — **Creativos de Meta son inmutables:** para cambiar imágenes o texto hay que crear un anuncio nuevo y archivar el viejo. El número de WhatsApp del conjunto toma el de la página y no se cambia por API ni en el editor.

- 19/10/2026 — Meta por API: cambiar el presupuesto de una campaña la pausa (`status_forced_to_paused`): reactivarla y verificar el estado.
- 19/10/2026 — En la cuenta de Somos Piedra, `ads_create_creative` rechaza el CTA WHATSAPP_MESSAGE. Funciona `ads_create_ad` con `object_story_spec` inline: `link_data` + `child_attachments` con `picture` (URL pública), CTA WHATSAPP_MESSAGE y `multi_share_optimized: false` para el paso a paso.
- 19/10/2026 — URL pública para subir placas a Meta: subirlas a Higgsfield (`/files/generate-upload-url`) da una URL de cloudfront que Meta acepta. GPT Image 2 no está en la API de Higgsfield con la clave de Tomás (`model_not_found`).
- 17/10/2026 — Biblioteca de anuncios (AR, exterior, BR, MX): lo que más tiempo dura es foto real de obra sin texto (Via Stone, desde 01/2024) y persona a cámara en el acopio (Super Pedras); lo hecho con IA y lleno de texto es nuevo y sin prueba. Para ver las piezas hace falta Chrome. Detalle: `claude/referencias-anuncios-2026-10-17.md` del proyecto.

- 29/10/2026 — Somos Piedra: la venta se cierra en el mostrador y WhatsApp solo muestra las de envío o transferencia, así que el costo por chat no elige al ganador: hace falta anotar el origen en el local.
- 29/10/2026 — En un test 1-3-6, Meta le da ~90% del gasto al primer anuncio de cada conjunto: los demás quedan sin probar, no perdidos.
- 29/10/2026 — Apagar un anuncio por API sin una orden explícita ("apagá X") lo frena el clasificador: pedir la frase antes.

## Verificar una corrida
- **09/10/2026 — Mirar también los e2e.** El de Piedra mostró el IVA en $0 por ventas sin factura (alícuotas en FALTA DATO), y ninguna rama lo había marcado.

- 15/10/2026 — **Para repartir presupuesto entre creativos, 1 conjunto con varios anuncios:** Meta concentra el gasto en 1-2 (94% en C5+C1 en 2 días). Sirve para elegir ganador rápido, pero los otros no reciben prueba justa: por eso la madre queda con los 2 mejores y los nuevos se prueban aparte.
- 15/10/2026 — **Antes de decir que un conector no tiene saldo, aclarar de qué cuenta es:** el conector de Higgsfield de la sesión mostraba 0,15 créditos; Tomás tiene crédito por API en otro lado. Pedirle que confirme cuál conector usar antes de planear gastos de generación.
- 15/10/2026 — **Carruseles de código vs. generación con IA:** los de código (HTML + Playwright sobre fotos reales) mantienen fiel la piedra; para la IA, usar fotos del catálogo como referencia y validar color/textura antes de publicar.
- 30/10/2026 — Business Suite: un IG que está en el porfolio pero no conectado a la página no aparece en "Publicar en". Se conecta desde Configuración → Páginas → Conectar activos → Cuenta de Instagram (pide login de IG, lo hace Tomás).
- 30/10/2026 — Reels en Business Suite: con música agregada solo se programan para FB ("Tu reel de Instagram editado no se puede programar"). Para IG: sin música, o desde la app.
- 30/10/2026 — Subir archivos con Chrome: `file_upload` solo acepta lo que está en /mnt/user-data/uploads (no outputs). Para un archivo generado en el contenedor: commit a la carpeta del usuario y volver a stagearlo. Tope 10 MB por tanda (recomprimir reels con ffmpeg a ~4,5 Mbps).
- 30/10/2026 — El editor de texto de Business Suite puede dar timeout de 30 s al escribir pero el texto entra: verificar con captura y no repetir.

## Contenido con IA (Somos Piedra, 02/11/2026)
- 02/11/2026 — Bajar imágenes de ChatGPT desde Claude in Chrome: scrollear al final, tomar el `<img>` visible con `elementsFromPoint` y hacer fetch del blob; la lista de imágenes reusa blobs. El JS corta a los 45 s y Chrome bloquea descargas seguidas: de a una.
- 02/11/2026 — ChatGPT Image espeja la escena al pedir "misma casa, cambiá solo la piedra": se corrige dándola vuelta con PIL.
- 02/11/2026 — En las placas con texto arriba, el protagonista de la imagen tiene que estar en la mitad de abajo (la sombra superior lo tapa).
- Subir imágenes a la cuenta publicitaria sin URL pública: `ads_creative_upload_local_image` → POST a rupload.facebook.com desde la pestaña de Business Suite (input file propio + fetch con Authorization, offset 0, X-Entity-Length, X-Entity-Name, X-Entity-Type) → `ads_finalize_local_ad_image_upload`. Desde la nube o la PC el proxy lo bloquea (02/11).
- Sin Tomás en la PC, Chrome deja las descargas como `.tmp` con «Guardar como» abierto: el `.tmp` ya es la imagen completa (02/11).
- Los nombres «Browser 1/2» de Chrome cambian entre sesiones: identificar por lo que tiene abierto (02/11).


- 02/11/2026 — **Subir creativos a Meta cuando la PC no llega a Facebook:** la VM de Cowork no ve facebook.com ni pypi y la nube no ve E:. Tomás arrastra los archivos al chat → `file_upload` (Chrome) a un `<input type=file>` creado en una pestaña de Business Suite (máx. ~10 MB por llamada, por eso los videos van a < 6,5 MB) → fetch POST al `upload_url` de `ads_creative_upload_local_image` → `ads_finalize_local_ad_image_upload`. Leer los tokens de a 2 (la salida de JS se corta ~1.000 caracteres).
- 02/11/2026 — **Render de placas en la PC sin Playwright:** `npm i puppeteer-core@23 @sparticuz/chromium@131` en /tmp, con HOME y TMPDIR apuntando a /tmp (el home de la VM está lleno). `build_html.py` en `cyber-2026\` arma el HTML con `armar.py` del kit.
- 02/11/2026 — **Presupuestos en ARS por la API de Meta van en centavos:** 1500000 = $15.000/día (la lectura los muestra en pesos).
