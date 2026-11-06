# Pendientes
Lista viva, ordenada por la prioridad de `proyectos.json`.
- La actualiza el comando `cierre`.
- Formato: `- [ ] qué — quién — desde DD/MM`.
- Acá va solo lo abierto. Lo cerrado se mueve a `pendientes-archivo.md`.

## 1. Sistema multi-negocio (`producto`)
- [ ] **Decisiones de plata de la corrida 2026-10-08a** (recomendación de Claude entre paréntesis; detalle en `bitacora/2026-10-09/producto.md` y `E:\vivero\REVISAR.md` §4 y §8) — Tomás / contador — desde 09/10
  1. ~~El crédito de IVA de las facturas A pesa dos veces~~ **Hecho el 09/10** (base de la corrida 2026-10-09a: septiembre de Piedra $583.875,20, verificado a mano).
  2. Una venta sin factura deja el IVA en $0 (e2e de Piedra: +$963.854,55 con IVA $0). **Cambió el 09/10:** Somos Piedra vende sin factura a propósito, así que la venta marca "con factura" o "sin factura". Sin factura → sin débito (correcto). Con factura pero todavía sin emitir → FALTA DATO. Ya está en el método §3.8.
  3. El sobrante del arqueo en dólares (que sume, igual que en pesos).
  4. Anular una venta con la factura pendiente (configurar ARCA antes de cargar las alícuotas, y poder descartar con nota una factura pendiente sin CAE).
  5. La factura en PDF con medios (una línea aparte de recargo o descuento; confirma el contador).
  6. Lo vendido antes de cargar los medios (aceptar FALTA DATO y cargar los medios antes de la primera venta real).
  7. El cobro posterior de una deuda (a precio de lista, sin el % del medio).
  - No son de plata: `devuelto` derivado (sin migración); cheques: vuelto no, editar datos no monetarios con nota sí, cobrar deuda con cheque más adelante; `activo = false` = solo lectura.
- [ ] Borrar a mano las carpetas vacías de `E:\vivero\.wt\` al cerrar las sesiones de VS Code de las ramas — Tomás — desde 09/10
- [ ] De la integración (`REVISAR.md` §8): CUIT de cada negocio en `negocios/*.json`, `VITE_SUPABASE_URL` y `VITE_SUPABASE_ANON_KEY` también para las funciones en Vercel, sacar `VITE_LOGIN_EMAIL` de `.env.example` — Tomás — desde 09/10
- [ ] Logos y colores de cada cliente (hoy `FALTA DATO`: la app usa un ícono con la inicial y la paleta neutra). Van en `public/marcas/<slug>/` y en `negocios.marca` — Tomás / clientes — desde 08/10
- [ ] Hosting: Vercel Pro u otro con funciones Node (Vercel Hobby no permite uso comercial). Como va un dominio por cliente, tiene que aceptar dominios propios — Tomás — desde 08/10
- [ ] Supabase: crear el proyecto único del sistema. Al crearlo, `npm run db:migrate` aplica 0001–0060 (incluidas 0050 y 0060 de la corrida 2026-10-09a) antes de que un teléfono confirme un corte — Tomás — desde 08/10
- [ ] Nombre y carpeta definitivos del repo (hoy `E:\vivero`; por ejemplo `E:\sistema-gestion`). Renombrar después de la corrida, sin sesiones corriendo — Tomás decide — desde 08/10
- [ ] Precio del abono — Tomás — desde 08/10
- [ ] Dominios, uno por cliente: quién los compra y quién los paga (el cliente, o Tomás dentro del abono) — Tomás — desde 08/10
- [ ] Avisarle a cada cliente que Tomás tiene un usuario de soporte que entra a su negocio. Va en los términos y en la política de privacidad — Tomás — desde 08/10
- [ ] Cobro del abono (transferencia o Mercado Pago Suscripciones), nombre comercial del sistema y borradores legales — Tomás — desde 08/10
- [ ] Decidir si Números estima los Ingresos Brutos como el IVA. Hoy se cargan como gasto cuando se pagan; en Somos Piedra son 5% minorista, o 2% con la escala de microempresa — Tomás — desde 08/10

## 2. Somos Piedra (`somos-piedra`)
- [ ] Confirmar pausa de L2-C2 Local con stock y VG2 (bloqueada por permisos) — Tomás — desde 05/11
- [ ] Descartar borrador ad 120251127339370411 («Nuevo anuncio de Interacción» en S0) — Claude — desde 05/11
- [ ] Sáb 7/11: leer L3-V3 Entrega granza v2 — Claude — desde 05/11
- [ ] Lun 9/11: corte de S0–S5, R5, R6, VG3, VG4 + decidir C5 / «Toda la zona – abierto» — Claude + Tomás — desde 05/11
- [x] 05/11 Los 6 carruseles (S0–S5) programados en FB + IG: jue 5 19:30, vie 6 09:00, sáb 7 19:30, dom 8 09:00, lun 9 19:30, mar 10 09:00 — Claude
- [ ] Pasar ventas desde octubre (cantidad, $ y anuncio que trajo cada una) — Tomás — desde 04/11
- [ ] Costo por cliente + presupuesto semanal con las ventas — Claude — desde 04/11
- [ ] Revisar si la Madre mejoró tras subirla a $35.000 (4/11 16:10) — Claude — desde 04/11
- [ ] 5 variaciones de hook de L1-R1 Envío Neuquén — Claude — desde 04/11
- [ ] Fran graba 10 guiones (cuántas bolsas + precio a cámara) — Fran — desde 04/11
- [ ] Subir carruseles VG3/VG4/VF3/VF4 con presupuesto bajo — Claude — desde 04/11
- [ ] Descartar borrador viejo L3-V3 (ad 120251109138600411) — Claude — desde 04/11
- [ ] Cortar carruseles V1 flojos el viernes 6/11 si siguen > $1.200/conv — Claude — desde 04/11
- [ ] Decidir "Toda la zona – abierto" el lunes 9/11 (> $1.200/conv → pausar) — Claude — desde 04/11
- [ ] **Panel — subir rediseño + Cotizaciones:** Tomás hace doble clic en `E:\somos-piedra-panel\SUBIR-COTIZACIONES.cmd` (migra la 0072 y hace `vercel --prod`; si Vercel pide login, `npx vercel login`). Después Claude prueba en el celu y la compu. A Claude el control automático no lo dejó migrar la base real — Tomás — desde 06/11
- [ ] Cotizaciones: el WhatsApp del negocio para el PDF y confirmar validez (7 días) y forma de pago (transferencia o efectivo) por defecto; `npm test` en Windows (`marca/sin-logo` y `meta/prueba` no corren en la VM) — Tomás/Claude — desde 06/11
- [ ] Panel: arreglar las funciones de `api/` en Vercel (ERR_MODULE_NOT_FOUND: sin manifest ni ícono; la factura no anda) — Claude/VS Code — desde 02/11
- [ ] Panel: apagar «Allow new users to sign up» en Supabase (Authentication → Sign In / Providers → Email) — Tomás — desde 02/11
- [ ] Panel: qué hacer con `panel@somospiedra.com` (creado sin acceso) — Tomás — desde 02/11
- [ ] Panel de Meta: arreglar los 2 hallazgos del /codex:review (CONTEXTO §7 del repo), después cargar `META_TOKEN`, `npm run meta -- --solo-lectura` y la tarea de Windows — Claude/Tomás — desde 02/11
- [ ] Panel: Supabase free se pausa a los 7 días sin uso (Pro para uso real) y el repo no tiene remoto en GitHub — Tomás — desde 02/11
- [ ] **Cyber Monday — seguimiento (sin tocar presupuestos, decidido 02/11):** ver cómo entregan las 4 variaciones de granza (conjunto 120251076731010411) y el 5/11 confirmar que todo terminó el 4/11 23:59 — Claude — desde 02/11
- [ ] **Ventas reales por anuncio:** Tomás pasa cuáles ventas vinieron de anuncio → comparar costo por venta Cyber / Madre / Test — Tomás → Claude — desde 02/11
- [ ] **Etiqueta «pago confirmado» en WhatsApp Business:** definir quién etiqueta (Erasmo no puede); después pasar la Madre a «compras por mensajes» — Tomás — desde 02/11
- [ ] **R3 Retest:** la tarea programada del 3/11 12:00 lo apaga si no funciona; revisar el aviso — Claude — desde 02/11
- [ ] Sacar el duplicado «Tu frente, antes y después» del vie 13/11 10:30 (ya sale el sáb 7/11) si Tomás confirma — Claude — desde 02/11
- [ ] Fran confirma que pórfido, ocre rectificada y riojana van en escalones exteriores (carrusel E sale el 14/11) — Tomás — desde 02/11
- [ ] No hay reels programados desde el 9/11: subir la tanda que graba Tomás — Tomás/Claude — desde 02/11
- [ ] Revisar R3 Retest y R4 Lote 3 a las 48 h: seguir < $450/chat, cortar > $900 con $3.000 gastados — Claude — desde 02/11
- [ ] Ver que R4 salga en IG con @somospiedranqn y cargar el mensaje armado de WhatsApp de R3/R4 en el Administrador — Tomás/Claude — desde 02/11
- [ ] Usar #vendido / #perdido en cada chat (225 chats con anuncio, 0 ventas marcadas) — Fran — desde 02/11
- [ ] Grabar reels con los guiones del artifact (BOFU 13, 14, 17 primero) y dejarlos en EDITADOS — Tomás — desde 02/11
- [ ] Confirmar con Fran datos de los guiones: origen de cada piedra, medidas verde bronce, formas de pago, frases técnicas, Añelo y Roca — Tomás — desde 02/11
- [ ] **Datos para la app** (no frenan la construcción: quedan `FALTA DATO`):
  - los medios de pago: nombre, cuenta, % y comisión de cada uno (efectivo, transferencia, débito, crédito, cuotas);
  - planes de cuotas, con su recargo y su comisión;
  - comisiones de MP y del posnet;
  - % de desperdicio;
  - precio del envío (fijo o por zona);
  - categorías y gastos fijos.

  — Tomás / cliente — desde 08/10
- [ ] El Excel o planilla actual, con la cobertura de cada producto (ojo: no se vende en cajas; la piedra va a granel o paletizada y la granza por m²), para el importador — cliente — desde 08/10
- [ ] **Para facturar:**
  - razón social y CUIT (verificar 33-71680803-9);
  - IIBB e inicio de actividades;
  - punto de venta para web services;
  - delegación de wsfe al CUIT de Tomás.

  — cliente — desde 08/10
- [ ] Con el contador: alícuotas de IVA de plantas, envío y parquización, y el régimen de IIBB — Tomás / contador — desde 08/10
- [ ] **Pauta:** que Fran diga qué fotos de la web son propias (hasta entonces no se usan); definir si el artifact dice "la gestión la hace Tomás, sin cargo" — Tomás / Fran — desde 09/10
- [ ] Descartar el borrador vacío "Nuevo anuncio de Interacción" (120250759520900411) en la cuenta 1945796639629607 — Tomás — desde 13/10
- [ ] Descartar los borradores de Somos Piedra en la cuenta vieja 2044879766141120 (Facebook de Somos iPhone) — Tomás — desde 13/10
- [ ] **Test 1-1-3 (A quincho, B pileta, D obras), $5.000/día:** 18 PNG listos en `E:\anuncios somos piedra\nuevos-8-angulos\`; falta subirlas a Meta (Chrome, vía del 13/10), crear campaña/conjunto/3 anuncios en borrador y activar con OK de Tomás. Textos y mensajes en `textos-y-mensajes.md`. La campaña del 13/10 ya es la **MADRE** ($5.000/día, solo C5 + C1; C2 y C3 pausados) — Claude / Tomás — desde 15/10
- [ ] Confirmar con Fran los datos de los 8 carruseles nuevos antes de publicarlos (reseñas G, pagos E, horarios/stock H, paletizado/Añelo D, Adoquín 10×10 C, % cortes F) y pasarle fotos de obras para el ángulo "antes y después" — Tomás / Fran — desde 15/10
- [x] (hecho 26 y 28/10) **Revisar la campaña MADRE y el test el lunes 20/10:** costo por chat de cada carrusel y ventas (etiqueta "anuncio" en WhatsApp Business); rotar si la frecuencia del conjunto pasa 2,5 o C5 supera ~$650/chat dos días seguidos (criterio propuesto, no del método) — Tomás / Claude — desde 13/10
- [ ] Fondos de la cuenta 1945796639629607: $30.000 cargados alcanzan ~3 días a $10.000/día; recargar antes del 16/10 (15/10: para la campaña conjunta del Día de la Madre hacen falta ~$40.000 más; Tomás recarga después de armar todo) — Tomás — desde 13/10
- [x] Autenticar la identidad en el Administrador de anuncios de la cuenta 1945796639629607 — hecho 15/10 (Tomás)
- [ ] Elegir el número de WhatsApp de la campaña conjunta: 459-0936 (el de la página) o 404-1698 (el de las tarjetas, hay que conectarlo a la página) — Tomás — desde 15/10
- [ ] **Campaña conjunta Somos Piedra + Vivero, Día de la Madre — ACTIVA desde 15/10** ($20.000/día desde 15/10 12:50, fin sáb 17/10 23:59, destino 459-0936). Anuncios v2 C1 120250807043320411, C2 120250807043650411, C3 120250807044920411, C4 120250807045860411 en revisión de Meta. Falta: (1) Tomás carga saldo (~$60.000 para esta campaña a $20.000/día) — sin eso no entrega; (2) Claude verifica a la tarde que los 4 pasaron la revisión; (3) Tomás confirma con el vivero nombres, precios y horarios (por si se vuelve a poner); (4) Tomás cobra al vivero su mitad ($15.000) y deriva los chats al vivero; (5) mirar resultados el 17/10 y cerrar — Tomás / Claude — desde 15/10
- [ ] WhatsApp de la campaña conjunta: el destino es el del vivero (299 404-1698, el de los creativos); el de la página es 299 459-0936. Hace falta el enlace wa.me — Claude / Tomás — desde 15/10
- [ ] Confirmar con el vivero: nombres de las plantas, que el precio incluye maceta y granza, y el sello "OFERTA" solo si hay oferta real — Tomás — desde 15/10
- [ ] Recargar saldo (~$40.000 para 4 días) y cobrarle al vivero su mitad ($5.000/día) — Tomás — desde 15/10
- [ ] Editar los 3 videos de los lentes Meta → campaña de Reels de $5.000/día — Tomás — desde 09/10
- [ ] **Vincular IG @somospiedranqn a la página y a la cuenta publicitaria** (a la página: hecho 29/10; falta verificar la cuenta publicitaria) (desde el 15/10 frena los anuncios del Día de la Madre: sin esto no se pueden promocionar los posts); píxel de Meta y etiqueta de Google en la web; perfil de Google (categoría, fotos, productos, horario); mensaje fuera de horario y etiqueta "anuncio" en WhatsApp Business — Tomás — desde 09/10
- [ ] Invitación pendiente a tomassanchez2018@gmail.com en el portfolio de Piedra: dejar vencer o cancelar — Tomás — desde 12/10
- [ ] Cerrar las cuentas viejas (IG @somospiedra.cipolletti, FB elijapiedrasas y ElijaPiedra) y pedir el retiro con la herramienta de Google — Tomás / dueño — desde 09/10
- [ ] Probar Somos Piedra en modo local (`npm run local`, "Piedra de prueba", recorrido de `REVISAR.md` §9) — Tomás — desde 09/10
- [ ] Fotos de obras propias (antes y después, para el carrusel 4) — Fran — desde 09/10
- [ ] **Corrida 2026-10-09a (v1.1):** leer el PARA COPIAR Y PEGAR de la integración y `E:\vivero\REVISAR.md` (sección de la corrida); verificar las cuentas — Tomás / Claude — desde 09/10
- [ ] **Decisiones de plata de las ramas** (recomendación de Claude: sí a 1–6):
  1. fecha del corte de Somos Piedra: 01/11/2026;
  2. envío en camioneta con costo $0 y nota (no FALTA DATO);
  3. con IVA sumado, IVA antes del % del medio (difiere hasta 2 centavos del orden de la spec);
  4. saldo inicial de IVA sin cargar = FALTA DATO (en el corte se carga $0);
  5. Ibero: el corte queda como constancia, sin saldos;
  6. lo anulado cuenta como "nunca pasó";
  7. los gastos con factura A no suman crédito de IVA (pide una columna en `movimientos`): hacerlo antes del 01/11 y ver con el contador qué gastos facturan A;
  8. no cargar ventas de prueba con factura en el negocio real antes del corte (una factura pendiente no se anula y deja el corte como constancia).

  — Tomás — desde 09/10
- [ ] Probar la demo para el dueño: `npm run local`, "Piedra de prueba", importar `tests/fixtures/piedra-ejemplo.csv`, probar Vender (laja 12 m² = $528.000, baldosa 83 u. = $498.000), IVA al día, Empleados y el corte. Si ya se abrió antes, usar incógnito — Tomás — desde 09/10
- [ ] Datos de empleados: cuántos, día de pago, si hay boleta de sindicato. Que el contador confirme el cambio de titular al 01/11 — Tomás / contador — desde 09/10
- [ ] Cargar la alícuota del 21 % en las categorías de piedra y la del envío (contador): sin eso "IVA sumado" queda apagado — Tomás — desde 09/10
- [ ] **Corte inicial ("día cero")** cuando la app esté lista: arqueo de cada cuenta (pesos, dólares, MP, banco), cheques en cartera, conteo de stock, deudas con proveedores y de clientes. Fecha de corte y, desde ahí, todo en la app. Copiar cómo se hizo en Somos iPhone, si Tomás deja leer ese Cortex — Tomás / Claude — desde 09/10

- [ ] Fran revisa 3 frases del carrusel "5 errores" (placas 3 a 5: pared firme, limpia y a plomo; presentar las piezas en el piso; adhesivo para piedra natural). Si cambia algo, se reemplaza el anuncio 120250865092770411 — Tomás / Fran — desde 19/10
- [ ] Revisión del TEST v2 (120250865076760411) el 26/10: apagar los 2 carruseles con peor costo por chat y meter 2 nuevos — Claude / Tomás — desde 19/10
- [ ] Ver en el Administrador si los anuncios v2 salen en Instagram (la API no ve la cuenta de IG vinculada) — Tomás — desde 19/10
- [ ] Los 5 anuncios v2 no tienen mensaje armado de WhatsApp (no se pudo por API): cargarlo desde el Administrador si se quiere — Tomás — desde 19/10
- [ ] Reels: alguien de Somos Piedra hablando a cámara en el acopio (formato Super Pedras / Piedra Urbana), para un conjunto de Reels — Tomás — desde 17/10
- [ ] Contar las ventas de los chats con la etiqueta "anuncio" en WhatsApp Business — Fran — desde 17/10

- [ ] **Bot y simulador:** cargar en el `.env` del bot `OPENAI_API_KEY` y `GEMINI_IMAGEN_API_KEY` (proyecto con facturación) y dejar 5 a 10 fotos de clientes en `E:\bot-piedra\fotos\prueba-ab\` — Tomás — desde 23/10
- [ ] **Fran, ronda 2** (`E:\bot-piedra\preguntas-fran-ronda2.md`): IVA con efectivo y con tarjeta, logo y datos del PDF, tramos de precio de la granza por cantidad de bolsas (bolsón descartado: no se vende, 03/11), seguimiento (cuándo y cuántas veces), horario final del bot, cuotas; además el Excel, las fotos de cada piedra (`guia-fotos-piedra.md`), los contactos excluidos y las cuentas — Fran — desde 23/10
- [ ] Decidir qué Cortex manda para el bot: el `CLAUDE.md` del bot apunta a `cortex-somosiphone\piedra\` y el proyecto a `cortex-gestion` — Tomás — desde 23/10
- [ ] Aprobar las reglas del bot (`E:\bot-piedra\reglas\cerebro-reglas-piedra.md`, v2 del 23/10) y la spec v1 del simulador (`E:\bot-piedra\bot\spec-simulador-v1.md`) — Tomás — desde 23/10

- [ ] Fran confirma qué calientes de anuncios compraron (lista en `claude/traspaso-2026-10-29.md`) — Fran — desde 29/10
- [ ] Anotar el origen de cada venta en el mostrador ("¿cómo nos conociste?") o con #vendido en el chat — Tomás / Fran — desde 29/10
- [ ] Que el bot de Piedra arranque solo al prender la PC (caído del 24/10 19 h al 28/10 9:41) — Tomás / Claude — desde 29/10
- [ ] Spec del agente nocturno que lee los chats y anota ventas por anuncio — Claude — desde 29/10
- [ ] Reels orgánicos con música en IG: programarlos desde la app de IG si se quiere (Business Suite solo deja música en FB) — Tomás — desde 30/10
- [ ] Medir las piezas orgánicas de la semana 30/10–5/11 (alcance, guardados, chats) y ajustar horarios — Claude / Tomás — desde 30/10
- [ ] Armar y programar la semana de contenido desde el vie 6/11 — Claude — desde 30/10

- [ ] **Programar en Business Suite las piezas del 30/10** (carpeta `contenido\ideas-dia\2026-10-30\`: 3 carruseles + 3 placas, y `extra-antes-y-despues\`: 4 carruseles; más el reel B armado con fotos reales). Desde el vie 6/11, después de la semana-30-10. Plan en `claude/traspaso-2026-10-30.md` — chat nuevo — desde 30/10
- [ ] Actualizar `contenido\ideas-dia\armar_dia.py` de la PC con soporte de escenas de IA ("escena:<id>", "split" con fotos reales, 4.º argumento con la carpeta de escenas, escenas en JPG de 1200 px para que pieza.html pese menos de 30 MB) — Claude — desde 30/10
- [ ] Elegir uno de los 3 bocetos de estilo (Tierra, Ficha de cantera, Cuaderno de obra: https://claude.ai/artifact/XD2Hrs6a6bDGiSHHqGm8ms) o rotarlos, y sumarlo al armador — Tomás — desde 30/10
- [ ] Fran: grabar el reel A (camioneta cargando y saliendo) y el C (rociador mojando la piedra); confirmar horario del sábado (9 a 14), espesores por piedra y granza roja de Olavarría en stock — Fran / Tomás — desde 30/10
- [ ] Revisar TEST REELS (120251035611560411, $16.000/día) a las 24 h: costo por chat por anuncio y por lote; si un lote recibe <20% del gasto, gasto mínimo — Claude (tarea programada sáb 31/10 12:30) — desde 30/10
- [ ] Cargar el mensaje armado de WhatsApp de cada uno de los 7 reels (Plantilla de mensaje en Ads Manager) — Tomás / Claude por Chrome — desde 30/10
- [ ] Descartar el borrador vacío "L1-R1" en Ads Manager — Tomás — desde 30/10
- [ ] Saldo de Higgsfield (API) en 0 desde el 30/10: recargar para que la tarea diaria tenga escenas (3 por día ≈ USD 0,84) — Tomás — desde 30/10

- [ ] Programar en Business Suite FB + IG los carruseles B «Esto arruina tu piedra» y C «Tu frente pide piedra a gritos» del 02/11 (aprobados) — chat — desde 02/11
- [ ] Generar 2 carruseles nuevos con la regla nueva (portada hook visual + imagen = texto, escenas por ChatGPT) — chat — desde 02/11
- [ ] Agregar a la tarea diaria el armado con `layout`/`marcas` en el PROMPT-DEL-DIA (ya está en PROMPT.md; verificar que la tarea del 03/11 lo use) — chat — desde 02/11
- [ ] Borrar los lock viejos de git del Cortex (`.git\stale-HEAD-lock-0211`, `.git\stale-HEAD-lock-0211b`) — Tomás — desde 02/11
- [ ] Cambiar el punto 3 del texto de la tarea «Ideas del día · Somos Piedra» (nombra hf.py) — Tomás — desde 02/11
- [ ] BANCO.md: marcar usado el par del frente (extra programado 13/11 10:30) — chat — desde 02/11
- [ ] Confirmar con Fran: cuidados de la piedra, granza junto a un fogón, cat-017 pizarra, cat-027 verde bronce, "a granel o paletizada" — Tomás — desde 02/11

## 3. Ibero (`ibero`)
- [ ] Probar la app en modo local (`npm run local`, negocio "Vivero de prueba") siguiendo los 6 pasos de `metodo/` §5.7, **después de la corrida 2026-10-08a**, sobre la versión multi-negocio que va a estar en línea. Pasar todo lo que cambiar en un solo mensaje. Lo cargado antes en modo local no se ve más (la base local cambia de nombre por negocio) — Tomás — desde 08/10
- [ ] Lo que falta del cliente (`E:\vivero\REVISAR.md` §4): datos fiscales, punto de venta y delegación de wsfe, alícuotas de IVA, comisiones reales, nombre, precios de los servicios y gastos fijos — Tomás / cliente — desde 08/10
- [ ] Lista "Con el contador" de `REVISAR.md` §4, incluido el arrastre del IVA a favor — Tomás — desde 08/10
- [ ] Export del sistema viejo (comprado en Mercado Libre), para probar el importador con el archivo real — cliente — desde 08/10
- [ ] Puesta en línea (etapa 8), después del multi-negocio — Claude (Sonnet 5.5 + advisor) — desde 08/10

## Cortex (`cortex`)
- [ ] Crear `.claude/agents/` (`explorer`, `researcher`, `worker`) y el advisor donde se abre VS Code, o sacarlos del bloque de delegación: en la corrida 2026-10-09a no existían y las sesiones usaron Plan/general-purpose con Opus — Tomás / Claude — desde 09/10
- [ ] `/codex:review` de la corrida 2026-10-09a después del 14/10 (Codex sin cupo hasta el 14/10 9:47) — Tomás — desde 09/10
- [ ] Crear el repo privado en GitHub para este Cortex y conectarlo (`git remote add origin <url>`): hasta entonces `sync.cmd` solo commitea — Tomás — desde 08/10
- [ ] Pegar `herramientas/instrucciones-proyectos/sistema-gestion.md` en las instrucciones del proyecto de Claude "Sistema de Gestión de Empresas" — Tomás — desde 08/10
- [ ] Sacar de las instrucciones del proyecto de Claude el prompt del bot de Somos iPhone que quedó pegado al final ("Otro modelo con la entrega ya dicha…") — Tomás — desde 08/10
- [somos-piedra] Subir VG3/VG4/VF3/VF4 a test de carruseles (decidir presupuesto) · revisar V1 · descartar borrador viejo L3-V3 (ad 120251109138600411) · confirmar entrega de L3-V3 (04/11)
