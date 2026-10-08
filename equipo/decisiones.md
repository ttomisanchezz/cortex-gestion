# Decisiones
Cada decisión va con su fecha, y la más nueva arriba.
Formato: `- DD/MM/AAAA — <qué se decidió> (<por qué>) — <quién> — <dónde impacta>`.
Si una decisión reemplaza a otra, la vieja se queda y se le agrega "(reemplazada el DD/MM: …)".

- 08/10/2026 — Corrida 2026-10-08a: 9 sesiones (base, marca, unidades, importador, medios, dolares, cheques, servicios, integración). Las señales llevan el id de la corrida (`base 2026-10-08a lista`, `rama <nombre> 2026-10-08a lista`) — Claude, lanzada por Tomás — `E:\vivero`, `metodo/` §6
- 08/10/2026 — Diseño multi-negocio (`E:\vivero\contexto\multinegocio.md`):
  - las migraciones 0001–0009 se reescriben en el lugar (nunca se aplicaron) y la semilla pasa a plantillas por rubro;
  - `negocio_id` en todas las tablas, con FKs compuestas y fijo; ids determinísticos con el negocio adentro;
  - RLS por acceso (dueño o soporte), sync por negocio y `editado_por` en cada fila;
  - login con mail y contraseña; el negocio sale del dominio;
  - módulos y facturación por negocio, que prende solo Tomás;
  - medios de pago separados de las cuentas, y el ajuste del medio se reparte entre los renglones;
  - USD: el monto en pesos más `monto_usd` y `cotizacion` en la cuenta Dólares;
  - IndexedDB por negocio y modo local con dos negocios de prueba;
  - ARCA: un certificado y, por negocio, los datos fiscales, el bloqueo y la numeración.

  (Claude lo propuso y Tomás lo aceptó al lanzar la corrida.) — `producto/`, `E:\vivero`
- 08/10/2026 — Cuentas: catálogo fijo (efectivo, Mercado Pago, banco, posnet, dólares, cheques) que se prende por negocio. La moneda y el tipo vienen con la cuenta. Una cuenta nueva (otro banco, Ualá) = una migración chica. Se descartaron las cuentas libres, que obligaban a reescribir caja, arqueo, ventas, compras y los 275 tests — Tomás — `producto/`, `E:\vivero`
- 08/10/2026 — Multi-negocio:
  - Tomás tiene un usuario de soporte que entra a todos los negocios;
  - el alta de negocios es a mano por ahora;
  - cada cliente ve su nombre, su logo y sus colores;
  - un dominio por cliente.

  — Tomás — `producto/`
- 08/10/2026 — Unidad, cobertura y moneda del precio van en el producto, no en el rubro. Los módulos se prenden por negocio: % por medio, USD, cheques, calculadora de m², servicios tercerizados y factura al guardar. (Somos Piedra vende por m², bolsón y planta en el mismo negocio.) — Claude lo propuso y Tomás lo aprobó con la spec — `producto/`, spec-piedra-v1 §10
- 08/10/2026 — Spec v1 de Somos Piedra aprobada. El detalle está en `clientes/somos-piedra/README.md` y en `claude/spec-piedra-v1.md` — Tomás — `somos-piedra`
- 08/10/2026 — Pago mixto: el % de cada medio se aplica a la parte de la lista que paga ese medio. Ejemplo: lista $100.000 → $45.000 en efectivo (−10%) + $57.500 en 3 cuotas (+15%) = $102.500 — Tomás — spec-piedra-v1 §2.2
- 08/10/2026 — Cheque rechazado: sale de la cartera y queda "le debe" a nombre del cliente. La venta no cambia. Si estaba endosado, vuelve a subir la deuda con el proveedor — Tomás — spec-piedra-v1 §2.5
- 08/10/2026 — Diferencia de cambio de la caja USD: suma o resta al resultado del mes. Tomás la eligió en lugar de mostrarla aparte, que era lo recomendado — Tomás — `metodo/` §3.8, CLAUDE.md, spec-piedra-v1 §2.4
- 08/10/2026 — VS Code: si el trabajo se puede dividir en ramas independientes, se mandan todos los prompts juntos en un solo mensaje (base si hace falta, uno por rama e integración). No se suma además un prompt que haga todo con subagentes — Tomás — `metodo/` §6, instrucciones del proyecto
- 08/10/2026 — Todo prompt para Claude Code empieza con el bloque "DELEGACIÓN Y PARALELIZACIÓN" y termina con "SI TENÉS QUE ELEGIR", tal cual el modelo del Cortex de Somos iPhone — Tomás — instrucciones del proyecto
- 08/10/2026 — El sistema es una sola app multi-negocio (un repo, un hosting y una base), y el rubro se configura por negocio. Se arma antes de poner Ibero en línea (un arreglo llega a todos, se paga un solo hosting y una sola base, y ARCA ya está pensado con un certificado para varios CUIT) — Tomás — `producto/`, `E:\vivero`
- 08/10/2026 — El negocio tiene su propio Cortex (`C:\Users\PC\Documents\cortex-gestion`), separado del de Somos iPhone — Tomás — todo
- 08/10/2026 — El proyecto de Claude se llama "Sistema de Gestión de Empresas" (antes "Vivero" y después "SomosPiedra"). Es para varias empresas: hoy Ibero y Somos Piedra — Tomás — instrucciones del proyecto
- 08/10/2026 — Ibero = el vivero — Tomás — `clientes/ibero/`
- 08/10/2026 — Reglas de plata: el IVA a favor no suma al resultado; la merma y las diferencias de arqueo restan; un faltante de conteo resta y un sobrante no suma; la comisión es solo de Mercado Pago y Posnet — Tomás — `metodo/` §3, `E:\vivero`
- 08/10/2026 — Spec v1 del vivero aprobada (decisiones en `clientes/ibero/README.md`) — Tomás — `E:\vivero`
