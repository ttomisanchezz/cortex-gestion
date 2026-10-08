# Ibero (vivero) — `ibero`

Vivero minorista del Alto Valle. Es el primer cliente del sistema, y con él se armó el método.

## Dónde vive
- **Código:** `E:\vivero`.
  - El estado está en `CONTEXTO.md` §8.
  - Lo que hay que mirar está en `REVISAR.md`.
  - La especificación del repo está en `contexto/spec-v1.md`, y es la que manda.
- **En el proyecto de Claude:** `claude/spec-vivero-v1.md` y `claude/investigacion-vivero.md` (copias).

## Estado (08/10/2026)
- La **v1 está completa en modo local**: 275 tests, build y prueba de punta a punta en verde.
- Incluye:
  - stock con buscador tolerante;
  - vender y caja;
  - compras y gastos;
  - clientes y arqueo;
  - Números y el Excel para el contador;
  - el importador;
  - factura A/B con ARCA, probada con mocks.
- **Falta:**
  - pasarla a multi-negocio: en curso (corrida 2026-10-08a);
  - que Tomás la pruebe después de la corrida ("Vivero de prueba" en modo local);
  - la puesta en línea (etapa 8).

## Decisiones del cliente
| Fecha | Decisión |
|---|---|
| 08/10/2026 | Carga solo el dueño, que ve todo. Celu y compu |
| 08/10/2026 | Stock completo: cantidades por planta y tamaño, bajas, merma |
| 08/10/2026 | Buscador tolerante, con nombres alternativos y que aprende |
| 08/10/2026 | Cuentas: Efectivo, Mercado Pago, Banco y Posnet |
| 08/10/2026 | La v1 incluye deudas con proveedores, clientes que deben y arqueo diario |
| 08/10/2026 | El dueño es Responsable Inscripto. Factura A y B solo cuando la piden |
| 08/10/2026 | El stock actual está en un sistema comprado en Mercado Libre (nombre: sin dato): se importa |
| 08/10/2026 | El IVA a favor no suma al resultado. La merma y las diferencias de arqueo restan |
| 08/10/2026 | La comisión es solo de Mercado Pago y Posnet (migración 0009) |

## Lo que falta del cliente (detalle en `REVISAR.md` §4)
- **Fiscal:**
  - datos fiscales (razón social, CUIT, domicilio, IIBB, inicio de actividades);
  - punto de venta "RECE para aplicativo y Web Services";
  - delegación de wsfe al CUIT de Tomás.
- **Del contador:** alícuotas de IVA por categoría, y la lista "Con el contador".
- **Del negocio:**
  - comisiones reales (qué posnet usa y qué plan de Mercado Pago tiene);
  - nombre comercial en la app;
  - precio y costo de los servicios;
  - gastos fijos;
  - export del sistema viejo.
