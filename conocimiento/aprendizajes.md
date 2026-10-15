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
## Investigación de clientes
- **08/10/2026 — Buscar primero la presencia pública del cliente** (web, Guía Cores, Facebook, CUIT). En Somos Piedra mostró que también tiene vivero y que vende por m², bolsón, unidad y planta. Eso llevó la unidad al producto y cambió el diseño multi-negocio.
- **08/10/2026 — Una SAS no puede ser monotributista:** solo pueden las personas humanas y las sucesiones indivisas. Si el cliente es una SAS, es Responsable Inscripto.

## Plata
- **08/10/2026 — El IVA a favor no es ganancia.** En la prueba de punta a punta del vivero, el resultado ($35.563) daba más que la ganancia bruta ($28.773), porque el IVA a favor sumaba. Corregido: queda en $16.440.
- **08/10/2026 — La merma y los faltantes de arqueo son pérdidas reales.** La spec no los restaba y se corrigió. En cada spec nueva, chequear la fórmula del resultado contra el método §3.
- **08/10/2026 — Recibir una transferencia no tiene comisión.** Pedir un % para Banco dejaba el saldo en FALTA DATO sin motivo.

## Técnica
- **08/10/2026 — Hosting:** Vercel Hobby no permite uso comercial.
- **08/10/2026 — Supabase gratis:** deja pocos proyectos activos y pausa los que no se usan.
- **08/10/2026 — La identidad git global de la PC es `frannnn87` (de Fran).** Los commits del vivero salieron con ese autor. En cada repo nuevo hay que configurar `user.name` y `user.email` locales.
- **08/10/2026 — Datos de prueba viejos:** en modo local, después de cambiar el esquema o las reglas, hay que borrar los datos del sitio en el navegador.
- **08/10/2026 — El Edge de la PC no está donde se esperaba.** La prueba de punta a punta usa Chrome: el script busca los dos.
- **08/10/2026 — Multi-negocio: los ids determinísticos llevan el negocio adentro.** `idArqueo(fecha)` o `idConfig(clave)` darían la misma pk para Ibero y Piedra el mismo día.
- **08/10/2026 — Commitear desde Cowork** pide permiso de borrado en la carpeta, porque git borra sus propios `.lock`.

## Trabajo con Tomás
- **09/10/2026 — Si Tomás pega una plantilla de respuestas sin completar, preguntar antes de armar nada** (llegó "factura [persona / SAS] con el CUIT [__]").
- **09/10/2026 — Antes de armar prompts, cruzar las instrucciones del proyecto con el CLAUDE.md del Cortex.** Los modelos estaban contradichos (Sonnet vs. Fable/Opus) y no se avisó a tiempo. Ahora la regla vive solo en CLAUDE.md.
- **08/10/2026 — Tomás dicta por voz.** La transcripción cambia palabras: "video" por vivero, "corte" o "xottex" por Cortex, "Diphons" por iPhones, "useful code" por VS Code. Se interpreta por el contexto y, si no cierra, se pregunta.
- **08/10/2026 — Tomás quiere los prompts listos para pegar**, todos juntos, y ver en la tabla qué modelo va en cada sesión.

## Pauta para clientes
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

## Verificar una corrida
- **09/10/2026 — Mirar también los e2e.** El de Piedra mostró el IVA en $0 por ventas sin factura (alícuotas en FALTA DATO), y ninguna rama lo había marcado.
