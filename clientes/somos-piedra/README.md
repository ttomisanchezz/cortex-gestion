# Somos Piedra (revestimiento de piedra) — `somos-piedra`

Segundo cliente del sistema. Arrancó el 08/10/2026.

## Dónde vive
- **En el proyecto de Claude** "Sistema de Gestión de Empresas":
  - `claude/investigacion-piedra.md`;
  - `claude/spec-piedra-v1.md`.
- **Código:** el mismo repo del sistema (multi-negocio). Su configuración de rubro se define en la spec.

## Estado (08/10/2026)
- **Spec v1 aprobada por Tomás.** La investigación está hecha y las preguntas, contestadas (abajo).
- **En construcción:** corrida 2026-10-08a (lanzada el 08/10 a las 17:48), ramas unidades, importador, medios, dolares, cheques y servicios. El reparto está en `E:\vivero\contexto\multinegocio.md` §4 y §5.

## Datos del cliente
- **Nombre legal:** Elija Piedra SAS ("Somos Piedra"). El CUIT según cuitonline es 33-71680803-9: **verificar**.
- **Zona:** Belgrano 3090, Neuquén capital.
- **Condición fiscal:** Responsable Inscripto. Factura todo.
- **Quién carga:** solo el dueño, desde el celu.
- **Cómo vende:** casi todo de mostrador. Hace entrega en obra.
- **Stock y números:** Excel o planilla.
- **FALTA DATO:**
  - nombre del dueño;
  - % por medio y planes de cuotas;
  - comisiones;
  - % de desperdicio;
  - precio del envío;
  - categorías y gastos fijos;
  - IIBB e inicio de actividades;
  - punto de venta y delegación de wsfe;
  - alícuotas (contador);
  - el Excel.

## Qué se investigó (hecho el 08/10: `claude/investigacion-piedra.md`)
- **Software de referencia** para corralones, marmolerías y revestimientos.
- **El tipo de piedra:**
  - natural (laja, San Luis, Mar del Plata, París);
  - o reconstituida, que se fabrica con moldes (cemento, arena, pigmentos), con su costo de producción y su merma. **No aplica a Somos Piedra: trabaja solo piedra natural (Tomás, 09/10).**
- **Cómo se vende:**
  - la unidad: m², metro lineal (esquineros, guardas) o caja/paquete que cubre X m²;
  - el desperdicio por corte en el presupuesto.
- **Insumos de colocación:** adhesivo, pastina, hidrofugante y sellador.
- **La colocación:** si es propia o de terceros, pagada por m², y si se vende como servicio.
- **Cómo es una venta:** presupuesto → seña → entrega o colocación → saldo, con avances de obra.
- **Clientes:** particulares, arquitectos y constructoras, con cuenta corriente.
- **Medios de pago:**
  - cheques y e-cheq a plazo (posible cuenta "cheques en cartera");
  - precios en dólares;
  - cuotas.
- **Logística:** flete, peso, entrega en obra.
- **El negocio:** estacionalidad de la construcción, competencia en la zona y precios publicados.

## Lo que cambia respecto del vivero (confirmado el 08/10)
- Unidad y cobertura por producto, con calculadora de m².
- Un precio + % por medio de pago, y cuotas.
- Precios en USD y caja en dólares, con diferencia de cambio.
- Cheques y e-cheq.
- Envío cobrado y parquización tercerizada con costo.
- Factura al guardar.

**No aplican:**
- presupuestos con seña;
- obras;
- producción;
- colocación;
- cuentas corrientes de clientes.

## Respuestas de Tomás (08/10/2026, rondas 1 y 2)
- Es Elija Piedra SAS (Somos Piedra), Belgrano 3090, Neuquén capital. **Entra todo: la piedra y la parte vivero** (plantas, césped en panes, parquización).
- **Solo revende.** No fabrica: no hace falta el módulo de producción.
- **Venta casi toda de mostrador.** No arman presupuestos formales ni toman seña.
- **Medios de pago:**
  - cheques y e-cheq: los deposita y a veces los endosa a proveedores;
  - cuotas con tarjeta;
  - algunos productos con precio en USD;
  - cobra también dólares billete, así que hace falta una caja en USD.
- **No tiene cuentas corrientes de clientes.** No lo marcó en la ronda 1.
- **Proveedores en USD:** no.
- **Precio:** un solo precio por producto, más un % según el medio de pago (descuento contado o recargo con tarjeta). Los % son FALTA DATO.
- **Fiscal:** Responsable Inscripto. Factura todo (A y B por ARCA).
- La investigación está en `claude/investigacion-piedra.md` (proyecto de Claude).

## Respuestas de Tomás (08/10/2026, ronda 3)
- **Unidad por producto.** Unos productos se venden por m² suelto y otros por caja o malla que cubre X m². La venta trae una calculadora: m² + % de desperdicio → unidades, redondeando para arriba.
- **Cotización del dólar:** la carga el dueño, una por día. Cada venta guarda la del momento. Sin API.
- **Quién carga:** solo el dueño, como en Ibero.
- **Hoy:** stock y números en Excel o planilla, así que va con el importador.

## Respuestas de Tomás (08/10/2026, ronda 4)
- **Entrega en obra** con camioneta propia: se cobra como servicio en la venta. Combustible y mantenimiento van como gasto del negocio.
- **Parquización y colocación de césped:** las terceriza. Se le cobra al cliente y se le paga al parquizador. Cada trabajo carga su costo y la app muestra el margen.
- **Proveedores:** cuenta corriente con algunos. Les paga con transferencia o con cheque endosado.
- **Cheque rechazado** (decisión de plata, Tomás):
  - sale de la cartera y queda "le debe" a nombre del cliente;
  - la venta no cambia;
  - si estaba endosado, la deuda con ese proveedor vuelve a subir.

## Respuestas de Tomás (08/10/2026, ronda 5: decisiones de plata)
- **Diferencia de cambio de la caja USD:** suma o resta al resultado del mes. Se eligió contra lo recomendado, que era mostrarla aparte. Ya está en `metodo/` §3.8 y en CLAUDE.md.
- **% por medio en un pago mixto:** cada parte lleva su %.
  - Ejemplo: lista $100.000, pagada $45.000 en efectivo (−10%), que cubre $50.000 de lista, y el resto con tarjeta en 3 cuotas (+15%), $57.500.
  - Total: $102.500.

## Pauta publicitaria (08/10/2026)
- Análisis completo: `clientes/somos-piedra/pauta-piedra.md` (también en `claude/pauta-piedra.md` del proyecto). Precios y método para otras empresas: `conocimiento/pauta-precios-2026-10.md`.
- Artifact para el dueño (borrador 1): https://claude.ai/artifact/BtZvUSLkbXoehs1HzXwb9C
- **Dueño: Fran** (según Tomás). La gestión de la pauta no se cobra.
- Datos de Tomás: ticket ~$600.000 y margen ~30% (estimados); escenarios $150.000 / $300.000 / $600.000; productos a empujar: laja y pórfido, travertino y pizarra, granza; zona: Neuquén, Alto Valle hasta Roca, Añelo y Rincón.
- Redes actuales: IG @somospiedranqn; Facebook "Elija Piedra Sas" (perfil personal, no sirve para anunciar). Viejas a cerrar: IG @somospiedra.cipolletti, FB elijapiedrasas y ElijaPiedra.
- WhatsApp del negocio para anuncios: 299 459-0936. Del dueño: 299 415-2119.
- A confirmar: página FB "SomosPiedraoficial" (177 seguidores, sin publicar desde 2023); IG @viverosomospiedra, que es "Vivero Somos Piedra" de Cinco Saltos (San Lorenzo y Güemes, WhatsApp 299 463-7323) con el mismo logo; y si las fotos de la web son de obras propias.
- **Carruseles (09/10):** 5 ángulos con fotos y textos (`pauta-piedra.md` §7 a §9). Las tarjetas las arma Claude con código sobre las fotos del IG, con el precio en una etiqueta "Desde $__ el m²" vacía. Primero los carruseles 1, 2, 3 y 5. **Hechos el 09/10:** `clientes/somos-piedra/carruseles/` (un .zip por carrusel + `make-carruseles.py`), con las fotos del catálogo y el IG; faltan los precios de las etiquetas.

## Cambios del 09/10/2026 (Tomás; van a la spec v1.1)
- **Solo piedras.** El vivero es otro negocio y sale de Somos Piedra (reemplaza "entra todo" del 08/10).
- **Con y sin factura.** La mayoría de las ventas van sin factura, con transferencia o efectivo y a precio sin IVA. Con factura, el IVA va incluido o se suma (× 1,21), según la venta.
- **IVA al día:** arreglo (a). Hay que ver cuánto se debe cada mes y cuánto crédito falta.
- **Empleados:** vencimientos y pagos, con aviso en Hoy.
- **A nombre de Tomás** (falta saber con qué CUIT).
- **Corte inicial ("día cero")** antes de arrancar.
- **Solo piedra natural (todo natural).** En piedras no hay nada de cemento: ni reconstituida ni símil. Lo único de cemento que venden son **baldosas**.
- **Entrega:** la piedra va **a granel en la camioneta** o **paletizada en camión**. No se vende en cajas ni en nada cerrado.
- **Fotos del catálogo** (`Catalogo SOMOS PIEDRA.pdf`, en Descargas de Tomás): son de **obras propias** y se usan en los anuncios.
- **La "ocre" del IG es la piedra Bariloche** del catálogo.

## Respuestas de Fran (vía Tomás, 09/10/2026)
- **Precios:** Tomás va a pasar la lista de precios que ya tienen hecha. Va en las etiquetas "Desde $__ el m²" y en la carga de productos.
- **Cuotas:** se usan poco. Se cobran con el posnet de Mercado Pago, con interés, y el cliente se entera en el momento. **Pedido para la app:** una parte de **cotizaciones** para cotizar las cuotas desde ahí, sin usar el posnet para cotizar (va a la spec v1.1).
- **Granza:** se vende **por m²**. Una bolsa (~40 kg) cubre **1 m² a 3 cm** (la altura máxima de la piedra), puesta pareja. Va en bolsas con la camioneta; si es mucho, a veces en bolsón.
- **Envío:** a veces se cobra y a veces no, **siempre se consulta antes**. Añelo y esa zona van **en camión** (por el peso y el recorrido). En los anuncios: nada de "envío gratis".
- **Facebook para anunciar:** la página **"Somos Piedra, elija piedra"** https://www.facebook.com/profile.php?id=61589214484295 (es página: categoría Materiales de construcción, 4 seguidores, WhatsApp 299 459-0936, Belgrano 3090). Reemplaza a SomosPiedraoficial y al perfil "Elija Piedra Sas".
- **@viverosomospiedra (Cinco Saltos):** es el vivero del papá de Fran, un negocio familiar aparte. No tiene que ver con las piedras: **no se usan sus fotos ni su nombre**.
- **Fotos de la web:** según Fran, son ilustrativas: algunas las sacaron ellos y otras son **de Google**. Hasta saber cuáles son propias, no van en los anuncios (derechos de autor y regla de fotos reales).
- **Fotos de obras:** Fran va a buscar si tiene más.

## Respuestas de Tomás (09/10/2026, para la v1.1)
- **Titular:** desde el 01/11/2026 el negocio pasa a nombre de Tomás (persona, RI), CUIT 20-45734050-9 ("seguramente": falta que lo confirme el contador). Hasta el 31/10, la SAS.
- **Precio:** sin factura = lista; con factura e IVA incluido = lista; con factura e IVA sumado = lista × 1,21. El descuento por efectivo o transferencia **no se suma** al "sin factura".
- **Empleados:** convenio Comercio. F931: lo pagan ellos con el VEP que manda el contador. FALTA DATO: cuántos, día de pago, sindicato.
- **Spec v1.1:** `claude/spec-piedra-v1.1.md` (proyecto de Claude), borrador para aprobar. Abiertas en su §10: medios aceptados sin factura, qué viene marcado en Vender, camión del paletizado propio o de fletero.
- **Cerrado 09/10 13:50 (§10 de la v1.1):** sin factura se acepta efectivo, transferencia, dólares y cheque; tarjeta y cuotas solo con factura. En Vender viene marcado "sin factura". El paletizado va en camión de un fletero: servicio con costo y deuda con él.
- **Spec v1.1 aprobada por Tomás (09/10 13:54).** Construida en la corrida 2026-10-09a (`E:\vivero\prompts\2026-10-09a\`): base 17:25, ramas iva, catalogo, empleados y corte, integración al 21:00. Falta leer el REVISAR y probar la demo (`tests/fixtures/piedra-ejemplo.csv`).

## Publicidad conjunta con Somos Vivero — Día de la Madre (15/10/2026) — ACTIVA
- Somos Piedra y Somos Vivero (IG @somos_vivero) no son del mismo dueño pero sí de la misma familia. Propuesta conjunta por fases: 1 Día de la Madre, 2 sorteo cruzado, 3 escalar.
- 4 carruseles del Día de la Madre (zips e imágenes v2 en `E:\anuncios somos piedra\dia-de-la-madre\`; v2 en `_subir_v2\`).
- En Meta, **ACTIVA desde el 15/10**: campaña 120250805457440411 (CBO **$20.000/día**, fin sáb 17/10 23:59), conjunto 120250805473960411 "Toda la zona - abierto" (CONVERSATIONS / WHATSAPP), 4 anuncios v2 activos (C1 120250807043320411, C2 120250807043650411, C3 120250807044920411, C4 120250807045860411), en revisión de Meta al activar.
- Destino de WhatsApp: **299 459-0936 (Somos Piedra)**; Tomás deriva al vivero. La última tarjeta aún muestra el 404-1698. Vincular el 404-1698 a la página queda para Fase 2.
- Se sacó lo sin confirmar con el vivero (precios, "desde $30.000", horarios). Sello "ESPECIAL DÍA DE LA MADRE".
- Plata: ~$60.000 para esta campaña (3 días a $20.000) + $10.000/día de la del 13/10. Tomás carga el saldo y le cobra al vivero su mitad (~$30.000).
- Pendiente: verificar aprobación de los 4 anuncios; vivero confirma nombres/precios/maceta+granza/horarios; resultados el 17/10.

## Madre + test 1-1-3 y 8 carruseles nuevos (15/10/2026 noche)
- **Campaña MADRE:** la del 13/10 (120250759505930411), renombrada "Somos Piedra - MADRE - C5 Granza + C1 Frente - Oct 2026", **$5.000/día**, C2 y C3 pausados (en 2 días Meta gastó ~94% en C5 $14.212 y C1 $6.405).
- **Test 1-1-3 (por crear):** 1 campaña, 1 conjunto (mismo público "Toda la zona - abierto", conversaciones a WhatsApp 459-0936), 3 anuncios: A quincho, B pileta, D obras; $5.000/día; mensajes armados distintos para etiquetar los chats.
- **8 carruseles nuevos** (A quincho, B pileta, C entrada/pórfido, D obras, E formas de pago, F guía, G reseñas, H local): PNG 1080×1080 + HTML en `E:\anuncios somos piedra\nuevos-8-angulos\`, textos en `textos-y-mensajes.md`. Cada uno con datos a confirmar con Fran antes de publicarse. El 9 (antes y después) está bloqueado: faltan fotos propias.
- Falta: subir las 18 imágenes (Chrome), armar el test en borrador, saldo de la cuenta (no visible por API).

## Pauta en Meta (13/10/2026) — PUBLICADA
- **Cuenta de Somos Piedra: 1945796639629607** (Facebook "Somos Piedra, elija piedra"; el conector de Meta está conectado con ese Facebook). Fondos: $30.000 cargados el 13/10.
- Campaña "Somos Piedra - WhatsApp - Test 4 carruseles - Oct 2026" (id 120250759505930411), **$10.000/día**, publicada el 13/10 ~10:56. Conjunto "Toda la zona - abierto" (id 120250759509110411).
- Anuncios: C1 Frente (120250759603290411), C2 Piedra (120250759610680411), C3 Estilo (120250759612040411), C5 Granza (120250759618840411). C1 y C5 con orden fijo de tarjetas. Sin Instagram vinculado.
- Placas subidas desde `E:\anuncios somos piedra\nuevooss\_subir\`. Revisar el 20/10.
- Lo de abajo (12/10) quedó en la cuenta 2044879766141120, que es del Facebook de Somos iPhone: hay que descartarlo.

## Pauta en Meta (12/10/2026) — reemplazada
- Cuenta publicitaria **2044879766141120** (tarjeta cargada). Página "Somos Piedra, elija piedra" (id 1025898313949204), administrada por Tomás con la invitación a frantomiphones@gmail.com. WhatsApp 299 459-0936 conectado (id 1025932387279130).
- En **borrador y sin errores:** campaña "Somos Piedra - WhatsApp - Test 4 carruseles - Oct 2026" (id 120252633268900624, $5.000/día) y conjunto "Toda la zona - abierto" (id 120252633271510624: Neuquén +40 km, Roca, Añelo y Rincón +15 km, público abierto, conversaciones a WhatsApp).
- Anuncio vacío de la UI (id 120252633342820624): borrar cuando estén los 4 carruseles.
- **Placas finales:** las de ChatGPT de Tomás, en `E:\anuncios somos piedra\nuevooss\` (c1-frente, c2-piedra, c3-estilo, c5-granza). Las tarjetas de código, sin precio ("Consultá precio"), quedan en `carruseles/` y en `Descargas\piedra-tarjetas-anuncios`.
- Textos y mensajes armados de cada carrusel: `pauta-piedra.md` §7 (carrusel 1 sin "cajas"; granza: "1 bolsa (40 kg aprox.) cubre 1 m² a 3 cm", envío a consultar).
- Segunda campaña: Reels con los 3 videos de los lentes Meta (stock afuera, revestimientos adentro, el local), $5.000/día, cuando Tomás los edite.


## Pauta 17–19/10/2026 — $20.000/día
- **MADRE** (120250759505930411): $7.000/día, C5 Granza (120250759618840411) y C1 Frente (120250759603290411). Al 19/10: 86 chats a $563 desde el 13/10.
- **TEST v2 código** (120250865076760411, CBO $13.000/día), conjunto 120250865080500411 (CONVERSATIONS / WHATSAPP, misma zona que la MADRE, Advantage+). 5 carruseles activos desde el 19/10, con orden fijo: Granza 120250865085520411, Frente 120250865088950411, 5 errores 120250865092770411, Cuánta piedra 120250865095370411, Patio y pileta 120250865098250411. Placas en `E:\anuncios somos piedra\anuncios-v2\final\`.
- **Conjunta Día de la Madre** (120250805457440411): pausada el 19/10 (46 chats a $1.221).
- Estilo decidido: "v2 por código" (fotos reales + esquemas; IA solo en portadas fotorrealistas con rótulo).
- Referencias de Meta (AR, exterior, BR, MX): `claude/referencias-anuncios-2026-10-17.md` del proyecto de Claude.
- Pendiente: Fran revisa 3 frases del carrusel "5 errores"; revisión el 26/10; ver Instagram; sin mensaje armado en los v2.

## Réplicas 1-3-6 (21/10/2026)
- Spec aprobada: `clientes/somos-piedra/replicas-1-3-6.md`. Apagados TEST v2, LAB Autoridad. MADRE a $9.000/día.

## Bot de WhatsApp y simulador de fotos (23/10/2026)
- **Repo del bot:** `E:\bot-piedra` (git propio, puerto 3002, instancia de Evolution `somospiedra`). Traspasos del bot en `E:\bot-piedra\claude\`.
- **Estado:** Etapa 2 de 5 (reglas en borrador, sin aprobar). En escucha (`CEREBRO_MODO=apagado`). Poda de iPhone mergeada el 19/10. Cotizador y catálogo hechos (16/10), sin conectar al cerebro (prompt 4). El último commit guarda de qué anuncio vino cada chat.
- **Bloqueo:** `evolution.js` no deja mandar archivos. Hace falta una excepción solo para archivos que genera el bot (simulación y PDF).
- **Respuestas de Fran del 23/10:** `E:\bot-piedra\reglas\respuestas-fran-2026-10-23-agente.txt` y `...-simulador-gestion.txt`. Resumen:
  - local L a V 9 a 18 corrido, sábados 9 a 14, domingo cerrado; bot de 9 a 20 (quizás 22); lo de la madrugada se contesta desde las 9;
  - no venden pegamento ni nailon; sí tela antimaleza, piedras y lajas, granza y césped en rollo;
  - se cotiza el total con efectivo/transferencia y con tarjeta si no dice cómo paga;
  - granza: bolsa ~40 kg ≈ 1 m² a 3 cm; bolsón ≈ 1 m³ ≈ 25 m²; precio por tramos (12 m² va con el de más de 10 bolsas);
  - sin tarifa de envío (se escala); entrega 2–3 días (hasta una semana); sin seña; el bot nunca pasa alias ni CBU;
  - factura: se suma el 21 %, sale sobre todo la A; dólares: promedio de compra y venta del blue;
  - se escala desde 100 m² y con cheques, cuotas, descuentos, datos de pago, envío o cliente listo para comprar;
  - seguimiento automático (1 mensaje natural); objeción de precio: "¿tenés otro presupuesto?"; colocadores: los pasa una persona;
  - simulador: 4 o 5 fotos de referencia por piedra, 1 o 2 del cliente, solo cambia la superficie elegida, se manda y se espera;
  - gestión: la carga el padre de Tomás; Excel real por llegar; nombre interno o alias de proveedores y materiales; Cinco Saltos es otro negocio (no sucursal); stock sin inventario (conteo inicial). Proveedores en Los Menucos, Zapala, San Luis y Mar del Plata, y Alessandrini.
- **Simulador:** en paralelo, integrado al bot desde el lanzamiento. Prueba A/B de 10 fotos (Nano Banana 2 contra GPT Image 2 medium). Costo estimado ~USD 0,06–0,07 por imagen, ~USD 20/mes con 300 imágenes. Spec v1: `E:\bot-piedra\bot\spec-simulador-v1.md` (borrador para aprobar). Guía de fotos de cada piedra: `E:\bot-piedra\guia-fotos-piedra.md`.
- **Reglas del bot:** `E:\bot-piedra\reglas\cerebro-reglas-piedra.md`, borrador v2 del 23/10 con las respuestas de Fran.


## Pauta y ventas por anuncio (26 al 29/10/2026)
- **$21.700/día:** MADRE $16.800 (C5 + C1) y TEST 1-3-6 solo con T1 Granza ($4.900). T3 apagado el 26/10, T2 el 27/10.
- 23 al 28/10: 122 chats a $1.044 (C5 $923, R-A1 $922, C1 $449). 28/10: 42 chats a $481.
- Export de Evolution del 13 al 28/10: `E:\bot-piedra\data\historial\export-2026-10-28-1136`. Con anuncio identificable solo 3 ventas, por ~$316.000; el resto se cierra en el mostrador sin rastro.
- Reels (28/10): campaña de test nueva a $4.900/día que reemplaza al 1-3-6; precio en el chat; ángulos: Neuquén + envío, el local con stock, una entrega a un cliente.
- Bot caído del 24/10 19 h al 28/10 9:41 (la PC no lo levantó).

## Contenido orgánico programado (29/10/2026)
- IG @somospiedranqn vinculado a la página el 29/10. Semana `contenido\semana-30-10\` programada completa en Business Suite (29/10 al 5/11): 3 piezas por día (carrusel mañana, placa 13:30, reel 20:30), FB + IG; reels con música solo en FB.
- Próximo: semana desde el 6/11 y medir resultados.

## Contenido 30/10/2026
- Ideas del día 30/10 en `E:\anuncios somos piedra\contenido\ideas-dia\2026-10-30\` (carruseles A ⭐ Antes y después: chau patio de cemento, B 4 cosas al elegir piedra, C Frases del que va a revestir; placas A ⭐ ¿Cálida o fría?, B El sábado también abrimos, C Si buscás esto; reels A camioneta, B 4 piedras en 12 s, C Mojala).
- 4 carruseles extra de antes y después (frente, quincho, entrada, pileta) en `...\2026-10-30\extra-antes-y-despues\`.
- Banco de 15 escenas IA en `contenido\salidas\ideas-2026-10-30\escenas\` (`BANCO.md` dice cuál está usada y su fidelidad). Saldo Higgsfield en 0.
- Bocetos de 3 estilos con otras tipografías: https://claude.ai/artifact/XD2Hrs6a6bDGiSHHqGm8ms (sin elegir).


## Pauta 30/10/2026 — $32.800/día
- MADRE 120250759505930411: $16.800/día (C5 Granza + C1 Frente). No se toca.
- TEST REELS 120251035611560411: CBO $16.000/día. R1 Lote 1 (120251035617360411): L1-R1 Envío Neuquén, L1-R2 Local con stock, L1-R3 Entrega cliente, L1-R4 Medida m². R2 Lote 2 (120251035618120411): L2-C1 Envío, L2-C2 Local, L2-C3 Entrega. Videos en `E:\anuncios somos piedra\EDITADOS\_para-meta\`.
- TEST 1-3-6 120250912907900411: pausado entero.
- 23-28/10 (releído el 30/10): $147.358, 162 chats, $910/chat. 29/10: $19.939, 22 chats, $906.
- Orgánico: los 7 reels programados en FB + IG a las 18:00 del 31/10 al 6/11.

## Contenido 02/11/2026 — escenas con ChatGPT
- Higgsfield sin saldo: las escenas IA pasan a ChatGPT Image (proyecto «Somos Piedra · escenas»; fuentes e instrucciones en `E:\anuncios somos piedra\contenido\chatgpt-proyecto\`). La tarea diaria deja `ideas-dia\AAAA-MM-DD\chatgpt\PROMPT-DEL-DIA.txt`.
- Ideas del 02/11: `ideas-dia\2026-11-02\`, página https://claude.ai/artifact/JUWbuU5Wq5LGgqFRgFUMV8. Placa A con la primera escena de ChatGPT (fogón con granza gris, fidelidad buena).
- Programado: carrusel extra «Tu frente, antes y después» el vie 13/11 10:30 (FB + IG).

## Pauta 02/11/2026 — $38.800/día
- **MADRE** (120250759505930411) $19.800: granza + frente + conjunto «Envío Neuquén» (120251070313580411) con L1-R1 y L2-C1 (el ganador: 38 chats a $337–448 del 31/10 al 2/11).
- **TEST REELS** (120251035611560411) $19.000: R2 (L2-C2), R3 Retest (120251068348720411, los 4 reels sin gasto, mín. $3.000) y R4 Lote 3 (120251070334890411, entrega a domicilio + pedido de granza, mín. $3.000).
- Reglas: pasa a la madre < $450/chat en 48 h; se corta > $900/chat con $3.000 gastados; 12–15 creativos nuevos por semana.
- Guiones (21, con locución completa): https://claude.ai/artifact/QmZm2ja42oa42w6v25t28D
- Orgánico por día: reel de fotos + carrusel + video real. Videos del 02/11 programados el 7/11 y 8/11 a las 18:00.
- Ventas por anuncio: el bot ya registra el anuncio de cada chat (225); falta que Fran marque #vendido/#perdido.



## Cyber Monday 02/11/2026 — campaña aparte, $20.000/día hasta el 4/11 23:59
- Campaña 120251071669960411 (activa desde 15:15): Gente nueva $15.000/día + Ya interactuaron 60 días $5.000/día. 6 carruseles (A–F) + 2 reels (L1-R1, L2-C1) con cinta en cada conjunto.
- Oferta: 20% OFF desde 2 m²; bolsón de granza $20.000 (antes $27.000). Piezas en `E:\anuncios somos piedra\contenido\cyber-2026\`; IDs en `meta-campana.md`.
- Pauta total hasta el 4/11: $58.800/día (madre $19.800 + test $19.000 + Cyber $20.000).
