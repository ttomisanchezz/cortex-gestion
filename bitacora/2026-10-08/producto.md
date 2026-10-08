CIERRE — producto — 08/10 18:00

Hecho:
- Leí el traspaso, el Cortex y `E:\vivero` (main en `71be644`, 275 tests).
- **Diseño multi-negocio** con los dos rubros a la vista: `E:\vivero\contexto\multinegocio.md` (decisiones, esquema, piezas de cada rama, tests con los números de la spec y reglas de la corrida).
  - En el repo también: copia de la spec de Piedra (`contexto/spec-piedra-v1.md`) y `CLAUDE.md` con las reservas por corrida. Commit `d15851d`.
  - El repo ahora tiene usuario de git local: Tomás Sánchez (antes los commits salían como `frannnn87`).
- **Corrida 2026-10-08a lanzada a las 17:48:** 9 sesiones (base, marca, unidades, importador, medios, dolares, cheques, servicios, integración). Todas reservaron sin duplicados. Estimado: termina entre las 22 y la medianoche.

Decisiones (qué y por qué):
- **Cuentas: catálogo fijo** (efectivo, MP, banco, posnet, dólares, cheques) que se prende por negocio; la moneda y el tipo vienen con la cuenta. Alcanza para Ibero (4) y Piedra (6) sin reescribir todo lo que hoy usa las cuentas fijas. Una cuenta nueva = una migración chica — Tomás.
- **Diseño** (Claude lo propuso y Tomás lo aceptó al lanzar la corrida):
  - las migraciones 0001–0009 se reescriben en el lugar (nunca se aplicaron); la semilla pasa a plantillas por rubro;
  - `negocio_id` en todas las tablas, con FKs compuestas y fijo; los ids determinísticos llevan el negocio adentro;
  - RLS por acceso (dueño del negocio o soporte); `sync_pull` y `sync_push` por negocio; `editado_por` en cada fila;
  - login con mail y contraseña (sin `VITE_LOGIN_EMAIL`); el negocio sale del dominio con una RPC pública que solo da la marca;
  - módulos y facturación por negocio: los prende solo Tomás con el script de alta;
  - medios de pago separados de las cuentas (débito y crédito en cuotas van a Posnet con su % y su comisión);
  - con medios, el ajuste se reparte entre los renglones (total = lo cobrado; factura, IVA y ganancia salen de los renglones);
  - USD: `movimientos.monto` siempre en pesos, más `monto_usd` y `cotizacion` en la cuenta Dólares;
  - IndexedDB por negocio; modo local con "Vivero de prueba" y "Piedra de prueba";
  - ARCA: un certificado, y por negocio los datos fiscales, el bloqueo y la numeración;
  - el repo sigue en `E:\vivero` durante la corrida.

Pendientes nuevos:
- [ ] Cuando termine la corrida, pegar el PARA COPIAR Y PEGAR de la integración (o el de la base si no dio la señal) en un chat nuevo de `producto` — Tomás / Claude
- [ ] Logos y colores de cada cliente (hoy `FALTA DATO`) — Tomás / clientes

Pendientes cerrados:
- Diseño de la conversión de `E:\vivero` a multi-negocio.
- Prompts de la construcción de Somos Piedra (la corrida está lanzada).

Aprendizajes (errores o trucos para no repetir):
- Las señales llevan el id de la corrida: "fase A lista" y "rama importador lista" ya estaban en el historial, y una rama nueva con el mismo nombre habría arrancado sola.
- En multi-negocio, los ids determinísticos (uuid v5) tienen que llevar el negocio adentro. Si no, dos negocios chocan en la misma pk el mismo día.
- Si varias ramas tocan la misma pantalla (Vender), la base la parte en piezas, un archivo por rama.
- Commitear desde Cowork pide permiso de borrado, porque git borra sus `.lock`.

Próximo paso: revisar el resultado de la corrida 2026-10-08a en un chat nuevo de `producto` — Modelo: —
Cambia una regla de plata o del método: método sí (§6: señales con id de corrida y piezas por rama). Reglas de plata: no.
