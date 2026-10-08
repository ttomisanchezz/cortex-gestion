# Producto: el sistema multi-negocio (`producto`)

## Qué es
Una sola app de gestión de plata que usan varias empresas. Cada empresa ve solo lo suyo y el rubro se configura por negocio. El núcleo común y las reglas de plata están en `metodo/metodo-sistema-gestion.md` (§2 y §3).

- **Decidido por Tomás el 08/10/2026:** una sola app multi-negocio (la opción C de `metodo/` §8).
- **Repo:** `E:\vivero`. La v1 es de un solo negocio y en modo local tiene 275 tests en verde. El nombre y la carpeta definitivos están pendientes.
- **Stack:**
  - React + Vite + TypeScript como PWA;
  - IndexedDB + outbox + sync;
  - Supabase (Postgres, RLS, Auth);
  - funciones Node para ARCA, con `@arcasdk/core`.

## Estado (08/10/2026)
- La app del vivero (Ibero) está completa en modo local. Hoy la base deja entrar a un solo dueño (tabla `duenos`), sin `negocio_id`.
- No hay hosting ni Supabase todavía. Nada está en línea.

## Orden de trabajo
1. **Somos Piedra:** investigación y spec v1. Es el segundo rubro, y sirve para ver qué se configura por negocio.
2. **Diseño multi-negocio (Fable 5)**, antes de tocar código y con los dos rubros a la vista. Preguntas a Tomás abajo.
3. **Conversión del repo a multi-negocio**, en ramas paralelas.
   - `negocio_id` y RLS en todas las tablas;
   - sync filtrado por negocio;
   - códigos `V-0001` por negocio;
   - configuración del rubro;
   - tests de aislamiento.

   Ibero pasa a ser el negocio 1 sin perder ningún test.
4. **Lo nuevo que pida Somos Piedra**, como módulos que se prenden por negocio.
5. **Puesta en línea:** hosting, Supabase, migraciones y ARCA. Primero Ibero, después Somos Piedra.

## Preguntas para el diseño multi-negocio (hacerlas antes del prompt)
- **Usuarios:**
  - ¿Un solo dueño por negocio, o también empleados con un rol que carga ventas pero no ve ganancias ni caja total?
  - Ibero: solo el dueño. Somos Piedra: FALTA DATO.
- **Tomás como administrador:** ¿tiene un usuario que entra a todos los negocios para dar soporte? Tiene implicancias de privacidad, y conviene que el cliente lo sepa.
- **Alta de negocios:** ¿la hace Tomás a mano (por ahora) o autoservicio con suscripción?
- **Configuración por rubro:** qué se prende y qué se apaga. Para confirmar con la spec de piedra:
  - unidad (unidad, m², metro lineal, caja);
  - presupuestos y obras;
  - cheques;
  - producción propia;
  - colocación o servicios;
  - stock por lote o color.
- **Marca:**
  - ¿Cada cliente ve su nombre, su logo y sus colores?
  - ¿Un solo dominio para todos o uno por cliente?
  - ¿Cómo se llama comercialmente el sistema?
- **ARCA:** el certificado es de Tomás y cada negocio le delega wsfe desde su CUIT. Ya está pensado así.
- **Cobro del abono:** ¿transferencia a mano o Mercado Pago Suscripciones?
- **Baja de un cliente:** se le entregan sus datos en Excel y se desactiva el negocio. Nada se borra.
- **Legal:** borradores de términos, política de privacidad y contrato de encargo de datos, para que los revise un abogado.

## Costos (decide Tomás)
- **Vercel Hobby no permite uso comercial.** Hace falta Vercel Pro u otro hosting con funciones Node.
- **Supabase gratis** deja pocos proyectos activos y pausa los que no se usan. Con multi-negocio alcanza **un solo proyecto para todos los clientes**.
- Antes de decidir, chequear los precios vigentes de cada plan.
