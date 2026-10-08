# Cortex — Sistema de Gestión de Empresas

Cerebro externo del negocio de Tomás: armar, hostear y cobrar por abono una app de gestión de plata para empresas.
**Acá vive todo**: el método, el estado del sistema, cada cliente, los pendientes y las decisiones.
Leelo entero antes de cualquier tarea.
Regla madre: **cada sesión termina escribiendo al Cortex. Si no se escribe, no pasó.**

## Qué es el negocio
Una app mobile-first (PWA que funciona sin señal) para que el dueño de una empresa sepa en todo momento:
- cuánta plata hay en cada cuenta;
- cuánto gana;
- cuánto debe y cuánto le deben;
- en qué se le va.

Tomás la arma, la hostea y cobra un abono mensual. **El cliente no usa Claude**: para él solo existe la app.

- **Arquitectura (decidida el 08/10/2026): una sola app multi-negocio.** Un repo, un hosting y una base de datos. Cada empresa ve solo lo suyo y el rubro se configura por negocio.
- **Repo del sistema:** `E:\vivero`. Hoy tiene la v1 del vivero, que es de un solo negocio. Se pasa a multi-negocio antes de ponerla en línea.
- **Método completo:** `metodo/metodo-sistema-gestion.md`. Tiene el núcleo común, las reglas de plata, el checklist por rubro, el proceso, cómo lanzar sesiones y la parte técnica.
- **Producto:** `producto/README.md`. Tiene la arquitectura, el estado, lo que falta decidir y los costos.

## Clientes (al 08/10/2026)
| # | Cliente | Rubro | id | Estado |
|---|---|---|---|---|
| 1 | Ibero | Vivero (Alto Valle) | `ibero` | v1 completa en modo local (`E:\vivero`, 275 tests en verde). Falta que Tomás la pruebe, pasarla a multi-negocio y ponerla en línea |
| 2 | Somos Piedra | Revestimiento de piedra | `somos-piedra` | Arrancando: faltan la investigación del rubro y la spec |

- El detalle de cada cliente está en `clientes/<id>/README.md`.
- El registro con las prioridades está en `proyectos.json`, y **ese orden manda** cuando se pregunta "qué tengo pendiente".

## Cómo trabajo con Claude
**Se hace solo:**
- leer, buscar e investigar;
- armar specs, prompts y borradores;
- verificar cuentas;
- actualizar el Cortex.

**Requiere el OK de Tomás:**
- mandar cualquier cosa a un cliente;
- gastar plata (hosting, Supabase pago, APIs);
- deploy o push;
- tocar datos reales de un cliente en producción;
- cambiar una regla de plata;
- borrar archivos o registros.

**Dónde se ejecuta cada cosa.**
- Por defecto, todo se hace en el chat con la carpeta conectada: leer y buscar código, cambios chicos y medianos, tests, commits, y todo lo que no es código.
- Se pasa a VS Code solo para sesiones largas de código, refactors grandes o para dejar algo corriendo.
- Tomás no hace push desde un agente: se le pasa el comando y lo corre él.

**VS Code en paralelo.** Si el trabajo se puede dividir en ramas independientes, se mandan **todos los prompts juntos en un solo mensaje**:
- uno de base (si hace falta);
- uno por rama;
- uno de integración.

El detalle está en `metodo/` §6.

## Modelos para VS Code (Claude Code)
Tres: **Fable 5**, **Opus 5.5** y **Opus 5**.

| Va con **Fable 5** | Va con **Opus 5.5 / Opus 5** |
|---|---|
| Esquema de base, arquitectura, multi-negocio | Pantallas, componentes, endpoints |
| Todo lo que toca plata: costo, IVA, comisiones, caja, Números | Fixes y ajustes chicos |
| Factura ARCA | Cambios mecánicos y migraciones con verificación |
| El buscador tolerante, diagnósticos | Lo que los tests atajarían si sale mal |

Regla corta: **si equivocarse cuesta caro o se arrastra, Fable 5. El resto, Opus.**
Cada prompt lleva arriba de todo la línea `Modelo: …`.

## Reglas de plata (resumen; el detalle está en `metodo/` §3)
1. Venta y caja son cosas distintas.
2. Nada se borra: se anula con nota. Una factura emitida se anula con nota de crédito.
3. Nunca se completa un dato que falta: `FALTA DATO` en rojo. Nunca 0, promedio ni estimación.
4. Fecha real. Montos en centavos enteros.
5. Resultado del mes = ganancia bruta − gastos del negocio − comisiones − IVA a pagar (≥ 0) − merma ± diferencias de arqueo.
   - El IVA a favor va aparte y no suma.
   - Un faltante de conteo resta; un sobrante no suma.
6. Comisión solo en las cuentas que la cobran (Mercado Pago, posnet).
7. Tres gastos separados: pago a proveedor, gasto del negocio y retiro personal. Un retiro nunca es gasto.

## Reglas fijas
1. Nunca se manda nada a un cliente sin que Tomás lo lea.
2. Nunca se completa un dato que falta (costo, precio, alícuota): se marca `FALTA DATO`.
3. Nada se borra: se anula con nota.
4. Nunca se guardan API keys, tokens, certificados ni contraseñas en el Cortex ni en git: van en `.env`.
5. Sin presupuesto para APIs pagas: primero lo gratuito. Si algo cuesta plata, decide Tomás.
6. Si no sabés algo del negocio de un cliente, preguntá. No inventes.
7. Antes de generar código, llegá a ~90% de certeza sobre qué construir.
8. Un cliente por chat. No se mezcla con Somos iPhone: su Cortex (`cortex-somosiphone`) no se toca salvo que Tomás lo pida.
9. Todo en español rioplatense.

## Semáforo del chat
Cada respuesta termina con `Chat: 🟢/🟡/🔴 | Motor sugerido: <modelo>`.

| Estado | Cuándo |
|---|---|
| 🟢 | El chat está liviano. |
| 🟡 | Ya van 2 o 3 tareas grandes, o se leyeron muchos archivos, logs o capturas. Se cierra al terminar lo que está en curso. |
| 🔴 | El chat se compactó, se pierden detalles o pasaron más de 3 tareas grandes. Primero `cierre`, después un traspaso de 3 a 5 líneas para el chat nuevo. |

**Motor sugerido** es el modelo del próximo prompt de VS Code. Si no se genera ninguno, va `—`.

## Comandos
- **`pendientes`**: lo que hay que hacer hoy, en orden de prioridad. Solo lee. Instrucciones en `skills/pendientes/SKILL.md`.
- **`cierre`**: escribe bitácora, pendientes, decisiones y aprendizajes, commitea y deja el comando de sync. Instrucciones en `skills/cierre/SKILL.md`.

**Sync (subir el Cortex a GitHub):** pegar `C:\Users\PC\Documents\cortex-gestion\sync.cmd` en cualquier terminal.
Hasta que exista el repo en GitHub, solo commitea (ver `pendientes.md`).

## Dónde vive cada cosa
- `metodo/`: el método. Se actualiza cada vez que se aprende algo que sirve para el próximo cliente.
- `producto/`: el sistema en sí (arquitectura, estado, decisiones abiertas, costos, roadmap).
- `clientes/<id>/`: una carpeta por cliente, con estado, decisiones, datos que faltan y dónde vive su spec.
- `proyectos.json`: registro de todo lo que se trabaja, en orden de prioridad (ids para el cierre).
- `pendientes.md`: lista viva por prioridad. Lo cerrado va a `pendientes-archivo.md`.
- `equipo/decisiones.md`: decisiones con fecha, la más nueva arriba.
- `conocimiento/`: aprendizajes y errores que no queremos repetir.
- `bitacora/AAAA-MM-DD/<id>.md`: qué pasó en cada sesión.
- `herramientas/instrucciones-proyectos/`: lo que va pegado en las instrucciones de los proyectos de Claude.
- `skills/`: `pendientes` y `cierre`.
- `sync.cmd`: el comando para subir el Cortex.

## El loop
- **Al arrancar:** abrir el chat del cliente que toca (o el del producto) y escribir `pendientes`.
- **Durante:** un cliente por chat. Cada prompt para VS Code lleva el modelo arriba. Si la sesión se pone pesada, `cierre` y chat nuevo.
- **Al cerrar:** `cierre`. Sin cierre, la sesión no existió para el Cortex.
- **Al final del día:** `sync.cmd`.
- **Cuando cambia una regla de plata o del método:**
  1. primero se cambia en `metodo/`;
  2. después en el resumen de este archivo;
  3. después en la spec del cliente y en el código (vía prompt).
