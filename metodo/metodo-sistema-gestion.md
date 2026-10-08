# Método: sistema de gestión de plata para empresas

Lo aprendimos armando la app del vivero Ibero (07 y 08/10/2026). Sirve para cualquier cliente nuevo.
Si algo cambia, se actualiza acá con la fecha. Esta es la versión que manda: la copia en el proyecto de Claude es solo de lectura.

## 1. Qué es el producto
Una sola app multi-negocio (decidido el 08/10/2026). Es mobile-first: una PWA que funciona sin señal. Le sirve al dueño de cada empresa para saber en todo momento:
- cuánta plata hay en cada cuenta;
- cuánto gana;
- cuánto debe y cuánto le deben;
- en qué se le va.

Tomás la hostea y cobra un abono mensual. El cliente no usa Claude.

**Primer caso: Ibero (vivero).**
- Repo `E:\vivero`, con la v1 completa en modo local.
- Su spec y su `REVISAR.md` son el ejemplo de cómo se escribe todo.

## 2. El núcleo (va en todos los clientes)
- **Vender** en menos de 30 segundos:
  - buscador tolerante a errores, con nombres alternativos y que aprende;
  - ítem libre;
  - servicios sin stock;
  - pagos mixtos;
  - "queda debiendo".
- **Caja** separada por cuenta (efectivo, Mercado Pago, banco, posnet a acreditar).
  - Pasar plata entre cuentas.
  - Arqueo diario al estilo Fudo.
- **Comprar:**
  - comprobante A, B/C o sin factura;
  - flete repartido;
  - costo promedio;
  - a cuenta del proveedor.
- **Tres gastos** en botones separados, sin selector: pago a proveedor, gasto del negocio y retiro personal.
  - Gastos fijos y punto de equilibrio.
- **Cuentas corrientes** de proveedores y de clientes.
- **Stock:**
  - bajas con motivo;
  - conteo;
  - merma valorizada.
- **Números del mes:**
  - la cuenta renglón por renglón;
  - comparativo de 12 meses;
  - Excel para el contador.
- **Factura ARCA:**
  - A y B, o C si el cliente es monotributista, con `@arcasdk/core`;
  - cada negocio delega wsfe al CUIT de Tomás;
  - nota de crédito para anular.
- **Importador** de CSV o Excel con mapeo de columnas.
- **Hoy:** saldos y avisos.

## 3. Reglas de plata que no se discuten
1. **Venta y caja son cosas distintas.** La venta se registra el día que se cierra; la caja, cuando la plata se mueve.
2. **Nada se borra.** Se anula con nota y un contraasiento con la fecha del día. Una factura emitida se anula con nota de crédito.
3. **Nunca se completa un dato que falta.** Queda `FALTA DATO` en rojo, con "con lo cargado: $X". Nunca 0, promedio ni estimación.
4. **Fecha real.**
5. **Montos en centavos enteros.** El IVA se redondea una vez por alícuota y por comprobante.
6. **El costo promedio se actualiza con cada compra.** Con factura A, el costo va sin IVA y el IVA queda como crédito.
7. **Precios de venta con IVA incluido.**
8. **Resultado del mes** = ganancia bruta − gastos del negocio − comisiones − IVA a pagar (≥ 0) − merma a costo ± diferencias de arqueo ± diferencia de cambio (solo en negocios con caja en dólares).
   - Diferencia de cambio del mes = valor en pesos de la caja USD al cierre (a la última cotización del mes) − valor al inicio − entradas en USD (a la cotización de cada día) + salidas en USD (a la cotización de cada día). Suma o resta al resultado. Sin cotización de cierre: `FALTA DATO`. Decidido por Tomás el 08/10/2026 (Somos Piedra).
   - El IVA a favor va aparte, no suma y no se arrastra solo al mes siguiente.
   - Un faltante de conteo resta. Un sobrante se muestra pero no suma.
   - Decidido por Tomás el 08/10/2026.
9. **Comisión solo en las cuentas que la cobran** (Mercado Pago, posnet). Efectivo y banco no la llevan (08/10/2026).
10. **Los tres gastos no se mezclan.**
    - Un retiro nunca es gasto.
    - Un pago a proveedor baja la deuda, no es gasto.
    - La mercadería pasa a ser gasto recién cuando se vende.
11. **El stock sale del libro** (compras + ajustes − ventas). No se guarda en el producto.
12. **Se puede vender aunque no alcance el stock:** la app avisa y lo marca "a contar".

## 4. Lo que cambia por rubro (checklist de la primera sesión)
- **Qué vende y en qué unidad:** unidad, m², metro lineal, caja o paquete, kg. ¿Se fracciona?
  - La unidad va en el producto, no en el negocio: uno solo puede vender por m², bolsón y planta (Somos Piedra, 08/10/2026).
- **Si produce o solo revende.** Si produce: insumos, mano de obra, merma de producción y costo por unidad producida.
- **Servicios** (instalación, colocación, envío, mano de obra): si son propios o de terceros, y cómo se costean.
- **Si vende por presupuesto u obra:** presupuesto → seña → entrega → saldo, con avances.
- **Medios de pago:** cheques y e-cheq a plazo, dólares, cuotas, cuenta corriente.
- **Lo fiscal:** condición (RI o monotributo), alícuotas de IVA y si factura todo.
- **Proveedores:** cuenta corriente, moneda y cómo llega la mercadería.
- **Quién carga:** solo el dueño o también empleados con permisos. Desde el celu, la compu o los dos.
- **Dónde está hoy el stock:** sistema, Excel o papel. Define el importador.
- **Estacionalidad y merma típica del rubro.**
- **Competencia local y software de referencia del rubro.**

## 5. El proceso, en orden
1. **Investigación del rubro**, con dos agentes en paralelo:
   - el software de referencia;
   - cómo funciona el negocio en Argentina y en la zona;
   - antes que nada, la presencia pública del cliente (web, Guía Cores, Facebook, CUIT). En Somos Piedra mostró que también tenía vivero y que vendía en muchas unidades, y eso cambió el diseño (08/10/2026).

   Va a `claude/investigacion-<cliente>.md` (proyecto de Claude), con fuentes.
2. **Preguntas hasta el 90%**, con AskUserQuestion (máximo 4 por ronda, la recomendada primero) y el checklist de §4.
3. **Spec v1** en `claude/spec-<cliente>-v1.md`: decisiones con fecha, pantallas, datos, reglas, lo que queda afuera y los pendientes. La aprueba Tomás.
4. **Kit en la carpeta del código:**
   - `CONTEXTO.md`, `CLAUDE.md` y `AGENTS.md`;
   - `contexto/` con la spec, la investigación y ARCA;
   - los prompts.

   Con multi-negocio, la forma exacta (qué va por cliente dentro del repo) se define en el diseño (`producto/`).
5. **Construcción en Claude Code:** todos los prompts juntos (§6). `REVISAR.md` junta las decisiones.
6. **Revisión de `REVISAR.md` con Tomás.**
   - Cuando Tomás pega lo que devolvió Claude Code, se verifican las cuentas a mano y se lee `REVISAR.md` entero.
   - Toda decisión de plata la confirma Tomás.
7. **Prueba local guiada:**
   1. cargar productos reales con nombres difíciles;
   2. buscarlos mal escritos;
   3. hacer una venta mixta tomando el tiempo;
   4. cargar una compra A con flete;
   5. hacer una baja y un arqueo con faltante;
   6. mirar Números y Hoy.
8. **Puesta en línea:** hosting, Supabase y ARCA.

## 6. Sesiones de Claude Code (VS Code)
- **Todos los prompts juntos (Tomás, 08/10/2026).** Si el trabajo se puede dividir en ramas independientes, se mandan en un solo mensaje, listos para pegar, uno por sesión de VS Code.
  - Arriba va una tabla: sesión, modelo y qué hace.
  - **Un id de corrida** (por ejemplo `2026-10-09a`), igual en todos los prompts. Cada sesión reserva `mkdir <repo>\.sesiones\<corrida>\<nombre>`; si ya existe, termina avisando "sesión duplicada". Así no hace falta borrar nada entre corridas.
  - **Base**, si hay algo compartido que tiene que existir antes (esquema, dependencias, tipos, componentes): termina con un commit de mensaje exacto (por ejemplo `fase A lista`).
  - **Una por rama:**
    - espera la señal en segundo plano (`until <condición>; do sleep 120; done`);
    - reserva su lugar;
    - recién después crea su worktree `.wt/<rama>` y corre `npm install`;
    - tiene sus archivos y su rango de migraciones;
    - termina con el commit `rama <nombre> lista` y su `REVISAR-<rama>.md`.
  - **Integración:**
    - espera todos los `rama … lista`;
    - mergea de a una con tests y build en verde;
    - junta los REVISAR;
    - borra los worktrees y las ramas mergeadas.
  - Si la tarea es chica o no se puede dividir, va un solo prompt.
- **Un solo esquema por corrida.** Si se mandan prompts por rama, no se suma además uno que haga todo con subagentes. El 08/10 se lanzaron los dos y quedaron unas 15 sesiones duplicadas.
- **Bloques fijos:** todo prompt empieza con "DELEGACIÓN Y PARALELIZACIÓN" y termina con "SI TENÉS QUE ELEGIR". El texto está en `herramientas/instrucciones-proyectos/sistema-gestion.md`. Además lleva `Modelo:` arriba.
- **Autorizado en la tarea.** "SI TENÉS QUE ELEGIR" frena ante commits y borrados. Por eso la tarea tiene que autorizar por escrito lo que la corrida necesita:
  - los commits de cada sesión en su rama;
  - la señal;
  - los merges de la integración;
  - borrar los worktrees ya mergeados.

  El push, nunca.
- **Sin nadie mirando:**
  - lo que la spec no cubre, con la opción recomendada o la más conservadora, anotada;
  - los datos del negocio nunca se inventan;
  - nada fuera del repo;
  - sin deploy, push ni ARCA real.
- **Reparto del trabajo:**
  - el esquema completo y las dependencias se resuelven en la base;
  - los tests corren con un glob;
  - cada pantalla nueva es una línea en `nav.ts`.
- **Modelos:**
  - **Fable 5:** esquema, plata, buscador, ARCA, diagnósticos.
  - **Opus 5.5 u Opus 5:** pantallas y ajustes.

## 7. Técnica y costos
- **Stack:**
  - React + Vite + TypeScript como PWA;
  - IndexedDB + outbox + sync;
  - Supabase (Postgres, RLS, Auth);
  - funciones Node para ARCA;
  - modo local para probar sin Supabase (el build de producción falla si está prendido).
- **Hosting y base:**
  - Vercel Hobby no permite uso comercial: hace falta Vercel Pro u otro hosting con Node;
  - Supabase gratis deja pocos proyectos activos, pero con multi-negocio alcanza uno solo.
- **Git:** la identidad global de la PC es `frannnn87`. En cada repo nuevo, configurar `user.name` y `user.email` locales.
- **Modo local:** después de cambiar el esquema, borrar los datos del sitio en el navegador.

## 8. Arquitectura: decidida
**08/10/2026 — Tomás eligió la opción C: una sola app multi-negocio.**
- Las opciones que se descartaron:
  - A: copiar el repo por cliente;
  - B: plantilla más un repo por cliente.
- Se hace antes de poner Ibero en línea: todavía no hay datos reales, así que migrar sale barato.
- El diseño, las preguntas abiertas y el orden de trabajo están en `producto/README.md`.
