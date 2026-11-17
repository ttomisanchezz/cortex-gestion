
## CIERRE — somos-piedra — 17/11 11:50 (chat del 16/11 18:00 → 17/11)

Hecho:
- Erasmo en modo tester con el número 298 440-9447 (Tomás cambió `NUMEROS_TESTER`). Probado por WhatsApp Web desde el Chrome «sanchez»: «precio?» → charla; granza gris 16 bolsas efectivo $256.000 + catálogo PDF (primera vez contra Evolution real: OK); bolsón → m²; «gracias» → frase de Fran; envío a Plottier → «Enseguida te respondemos.» una vez; Verde Bronce (primer login real a Supabase: OK) → 6 versiones, Irregular 10 m² $300.000, tarjeta con factura $471.900 (verificado: 10 × $39.000 × 1,21); «en 15 días arranco» → seguimiento 01/12. `npm run pruebas -- 5492984409447`: 10 tandas, US$ 0,17. Evaluar 18/18.
- Lista completa de precios del panel (38 productos; sin precio: «Envío» y «Flete paletizado») y cuestionario para Fran. Fran contestó por escrito y en 3 audios (transcriptos con Google AI Studio desde el Chrome de Tomás).
- Excel «día a día» revisado: 97 hojas (VENTAS y GASTOS por mes desde 02/2023, con bloques de proveedores y gastos fijos; LISTADO con costo con flete, efectivo y lista).
- Prompt para VS Code: `E:\bot-piedra\bot\prompts\PROMPT-vscode-2026-11-17a-erasmo-fran.md` (corrida 2026-11-17a).
Decisiones (qué y por qué):
- Ver `equipo/decisiones.md` del 17/11 (Erasmo con lo de Fran; Excel ↔ panel; mudanza de Erasmo después).
Pendientes nuevos: ver `pendientes.md` (17/11).
Aprendizajes:
- Audios de WhatsApp: Gemini app no los transcribe ("solo genero texto"); AI Studio sí. El .ogg se sube con `file_upload` a un input propio y se re-envuelve en JS como `File` con `type: 'audio/ogg'` antes de pasarlo al input nativo (si no, «Unsupported file»).
Próximo paso: Tomás pega el prompt 2026-11-17a en VS Code; en paralelo, chat nuevo para el plan Excel ↔ panel — Modelo: Sonnet 5.5 + advisor
Cambia una regla de plata o del método: no (reglas de cobro de Erasmo, no de la app)

## CIERRE — somos-piedra — 17/11 12:32 — Reel 76, video IA por piedra y pauta (TEST apagado, MADRE baja, R31 a ESCALA)

Hecho:
- Revisado el reel 76 todo IA (`reels\lote-2026-11-16-ia-3\`): plata bien (sesión USD 3,298; CSV USD 9,054 de 10, 24 filas), controles 86/86, granza IA más gruesa que la real (se parece en metro y perro; menos en rastrillo, terminado y caída). 6 de 8 clips del reel son Veo, 2 Seedance. A Tomás le encantó.
- Costos de video IA por piedra (todo Veo, USD 0,14/clip): ~USD 1,40 por reel (8 clips + 2 regeneraciones); 5 reels nuevos ~USD 7, tope USD 10. Tomás carga USD 10 en APIMart.
- 5 formatos nuevos problema → solución diseñados (77 pantalla partida/granza gris, 78 contador «Pintada n.º 4»/Bariloche en tiras, 79 POV salir al auto/pórfido, 80 perro/granza roja, 81 un año en 10 s/verde bronce). **Las piezas JSON NO quedaron escritas** (se cortó el puente con la PC al guardarlas): hay que rehacerlas en el chat nuevo. Descripciones ajustadas mirando las fotos: Bariloche en tiras más gris-beige; granza roja 1,5–3 cm, rosa/malva/verde gris.
- Pauta leída 7 días (10–16/11): $738.467 · 810 conv · $912 (ESCALA $691, MADRE $1.088, TEST $1.110, TEST REELS $1.844). Ayer 16/11: $119.247 · 161 · $741 (ESCALA 105 a $544).
- Cambios en Meta (OK de Tomás): **TEST CREATIVOS apagada**; **MADRE $35.000 → $30.000**; **R31 a la ESCALA** (adset 120251317750180411, ad 120251317750190411). Programado: $73.200/día.
- NO hecho: sacar el mínimo de $3.500 de «Entrega lajas»: el conjunto tiene «Cambios sin publicar» de antes que no se ven; publicar los arrastraría.
- Trazabilidad: el bot ya guarda de qué anuncio vino cada chat (1.174 chats; `node herramientas/anuncios/reporte.js`), con 0 ventas marcadas. Los anuncios no tienen mensaje precargado.
Decisiones (qué y por qué):
- Reel 76 va como orgánico y como anuncio; la bolsa queda; **sin rótulo «Imagen ilustrativa»** y sin la etiqueta de IA de Instagram — Tomás.
- Reels IA por piedra: la IA arma todo, con foto de referencia y descripción; todo Veo — Tomás.
- **CBO nueva «IA – Nov 2026», $20.000/día**, con 76, 66 IA, 67 IA y 64 Veo como anuncios separados, cada uno con mensaje precargado distinto; el ganador pasa a la ESCALA — Tomás.
- Ventas por anuncio: **`#vendido <número>` en el grupo «Bot Erasmo»**, nunca en el chat del cliente (el cliente lo vería). Después: cruce automático venta del panel (teléfono) ↔ anuncio del bot — Tomás.
Pendientes nuevos: ver `pendientes.md` (17/11, pauta y video IA).
Aprendizajes:
- Ver `conocimiento/aprendizajes.md` → «Ads Manager por Chrome: leer la tabla entera (17/11/2026)» y lo de editar en Ads Manager con ventana chica.
Próximo paso: chat nuevo — re-render del 76 sin rótulo, comprimir 4 reels a <3,8 MB, armar la CBO IA a $20.000 con mensajes precargados — Modelo: —
Cambia una regla de plata o del método: no
