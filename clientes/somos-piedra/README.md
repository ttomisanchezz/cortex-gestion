# Somos Piedra (revestimiento de piedra) — `somos-piedra`

Segundo cliente del sistema. Arrancó el 08/10/2026.

## Dónde vive
- **En el proyecto de Claude** "Sistema de Gestión de Empresas":
  - `claude/investigacion-piedra.md`;
  - `claude/spec-piedra-v1.md`.
- **Código:** el mismo repo del sistema (multi-negocio). Su configuración de rubro se define en la spec.

## Estado (08/10/2026)
- **Spec v1 aprobada por Tomás.** La investigación está hecha y las preguntas, contestadas (abajo).
- **Próximo paso:** se construye dentro de la corrida multi-negocio (`producto`), como ramas (spec §11).

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
  - o reconstituida, que se fabrica con moldes (cemento, arena, pigmentos), con su costo de producción y su merma.
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
