CIERRE — somos-piedra — 08/10 16:32

Hecho:
- **Investigación del rubro** con dos agentes en paralelo: software de referencia, y cómo funciona el negocio en Argentina y en Neuquén.
  - Los datos clave se chequearon contra la fuente: Guía Cores, la Ley Impositiva 3541 de Neuquén y el ABC de AFIP.
  - Está en `claude/investigacion-piedra.md`.
- **Se identificó al cliente:** Elija Piedra SAS, Belgrano 3090, Neuquén. Vende piedra natural y además tiene vivero.
- **Cinco rondas de preguntas.** Las respuestas están en `clientes/somos-piedra/README.md`.
- **Spec v1** en `claude/spec-piedra-v1.md`, **aprobada por Tomás**. Las cuentas de los ejemplos se verificaron con código.
- **Preguntas del diseño multi-negocio contestadas** (`producto/README.md`).
- Método §3.8 y CLAUDE.md: la diferencia de cambio entra en el resultado.

Decisiones (qué y por qué):
- **Somos Piedra:**
  - entra todo, piedra y vivero;
  - solo revende;
  - venta casi toda de mostrador;
  - unidad por producto, con una calculadora de m² que redondea para arriba;
  - un solo precio + % por medio de pago, y en un pago mixto cada parte lleva su %;
  - cuotas con tarjeta;
  - algunos precios en USD y caja en dólares, con la cotización cargada por el dueño;
  - cheques: se depositan o se endosan, y uno rechazado vuelve como "le debe" del cliente (y como deuda con el proveedor si estaba endosado);
  - envío con camioneta propia, cobrado;
  - parquización tercerizada, con costo por trabajo;
  - Responsable Inscripto, factura todo, al guardar;
  - solo el dueño carga;
  - hoy trabajan con un Excel.
- **Diferencia de cambio de la caja USD:** suma o resta al resultado del mes. Tomás la eligió en lugar de mostrarla aparte, que era lo recomendado.
- **Multi-negocio:**
  - Tomás tiene un usuario de soporte que entra a todos los negocios;
  - el alta de negocios es a mano por ahora;
  - cada cliente ve su nombre, su logo y sus colores;
  - un dominio por cliente.

Pendientes nuevos:
- [ ] Diseño multi-negocio y corrida de VS Code (base + ramas de Somos Piedra + integración) — Claude (Fable 5), chat de `producto`
- [ ] Dominios por cliente: quién los compra y los paga — Tomás
- [ ] Avisarles a los clientes que existe el usuario de soporte — Tomás
- [ ] Decidir si Números estima Ingresos Brutos — Tomás
- [ ] Datos de Somos Piedra para la app y para facturar, y su Excel — Tomás / cliente
- [ ] Con el contador: alícuotas de plantas, envío y parquización, e IIBB — Tomás
- [ ] Sacar el prompt de Somos iPhone que quedó pegado en las instrucciones del proyecto — Tomás

Pendientes cerrados:
- Investigación, preguntas y spec v1 de Somos Piedra.
- Datos básicos del cliente.
- Preguntas del diseño multi-negocio.

Aprendizajes (errores o trucos para no repetir):
- Buscar primero la presencia pública del cliente. En Somos Piedra mostró el vivero y las muchas unidades, y eso cambió el diseño.
- Una SAS no puede ser monotributista: es Responsable Inscripto.

Próximo paso: chat nuevo de `producto` para el diseño multi-negocio leyendo `E:\vivero`, y la corrida completa en un solo mensaje — Modelo: Fable 5
Cambia una regla de plata o del método: sí.
- Resultado del mes ± diferencia de cambio, solo en negocios con caja en dólares.
- La tienen copiada `spec-piedra-v1`, el método §3.8 y CLAUDE.md.
- Ibero no tiene dólares: su código no cambia.
