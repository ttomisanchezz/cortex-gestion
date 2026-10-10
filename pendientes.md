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
- [ ] **Antes de pautar:** cuenta publicitaria con tarjeta en la página "Somos Piedra, elija piedra" (https://www.facebook.com/profile.php?id=61589214484295), vincular @somospiedranqn y el WhatsApp Business 299 459-0936 (mensaje fuera de horario, etiqueta "anuncio"), píxel de Meta y etiqueta de Google en la web, perfil de Google (categoría, fotos, productos, horario) — Tomás — desde 09/10
- [ ] Cerrar las cuentas viejas (IG @somospiedra.cipolletti, FB elijapiedrasas y ElijaPiedra) y pedir el retiro con la herramienta de Google — Tomás / dueño — desde 09/10
- [ ] Probar Somos Piedra en modo local (`npm run local`, "Piedra de prueba", recorrido de `REVISAR.md` §9) — Tomás — desde 09/10
- [ ] **Lista de precios** de Somos Piedra, para completar las etiquetas "Desde $__ el m²" de los 4 carruseles y la carga de productos — Tomás — desde 09/10
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
