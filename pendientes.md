# Pendientes
Lista viva, ordenada por la prioridad de `proyectos.json`.
- La actualiza el comando `cierre`.
- Formato: `- [ ] qué — quién — desde DD/MM`.
- Acá va solo lo abierto. Lo cerrado se mueve a `pendientes-archivo.md`.

## 1. Sistema multi-negocio (`producto`)
- [ ] **Corrida 2026-10-08a en curso** (lanzada el 08/10 a las 17:48; 9 sesiones; diseño en `E:\vivero\contexto\multinegocio.md`).
  - Cuando termine, pegar en un chat nuevo de `producto` el PARA COPIAR Y PEGAR de la integración (o el de la base si no dio la señal).
  - Claude verifica las cuentas a mano, lee `REVISAR.md` y trae las decisiones de plata con su recomendación.
  - Tomás / Claude — desde 08/10
- [ ] Logos y colores de cada cliente (hoy `FALTA DATO`: la app usa un ícono con la inicial y la paleta neutra). Van en `public/marcas/<slug>/` y en `negocios.marca` — Tomás / clientes — desde 08/10
- [ ] Hosting: Vercel Pro u otro con funciones Node (Vercel Hobby no permite uso comercial). Como va un dominio por cliente, tiene que aceptar dominios propios — Tomás — desde 08/10
- [ ] Supabase: crear el proyecto único del sistema — Tomás — desde 08/10
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
- [ ] El Excel o planilla actual, con la cobertura de cada producto (m² por caja o malla), para el importador — cliente — desde 08/10
- [ ] **Para facturar:**
  - razón social y CUIT (verificar 33-71680803-9);
  - IIBB e inicio de actividades;
  - punto de venta para web services;
  - delegación de wsfe al CUIT de Tomás.

  — cliente — desde 08/10
- [ ] Con el contador: alícuotas de IVA de plantas, envío y parquización, y el régimen de IIBB — Tomás / contador — desde 08/10

## 3. Ibero (`ibero`)
- [ ] Probar la app en modo local (`npm run local`, negocio "Vivero de prueba") siguiendo los 6 pasos de `metodo/` §5.7, **después de la corrida 2026-10-08a**, sobre la versión multi-negocio que va a estar en línea. Pasar todo lo que cambiar en un solo mensaje. Lo cargado antes en modo local no se ve más (la base local cambia de nombre por negocio) — Tomás — desde 08/10
- [ ] Lo que falta del cliente (`E:\vivero\REVISAR.md` §4): datos fiscales, punto de venta y delegación de wsfe, alícuotas de IVA, comisiones reales, nombre, precios de los servicios y gastos fijos — Tomás / cliente — desde 08/10
- [ ] Lista "Con el contador" de `REVISAR.md` §4, incluido el arrastre del IVA a favor — Tomás — desde 08/10
- [ ] Export del sistema viejo (comprado en Mercado Libre), para probar el importador con el archivo real — cliente — desde 08/10
- [ ] Puesta en línea (etapa 8), después del multi-negocio — Claude (Fable 5) — desde 08/10

## Cortex (`cortex`)
- [ ] Crear el repo privado en GitHub para este Cortex y conectarlo (`git remote add origin <url>`): hasta entonces `sync.cmd` solo commitea — Tomás — desde 08/10
- [ ] Pegar `herramientas/instrucciones-proyectos/sistema-gestion.md` en las instrucciones del proyecto de Claude "Sistema de Gestión de Empresas" — Tomás — desde 08/10
- [ ] Sacar de las instrucciones del proyecto de Claude el prompt del bot de Somos iPhone que quedó pegado al final ("Otro modelo con la entrega ya dicha…") — Tomás — desde 08/10
