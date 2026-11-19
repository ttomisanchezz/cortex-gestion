# Cotizaciones de Somos Piedra

- Generador: `python cotizacion.py <datos>.json` → `salida/Cotizacion-<N°>[-<apellido>].pdf`.
- Emite siempre: Somos Piedra · Razón social Franco Nicolás Muñoz · CUIT 20-45734050-9 · Belgrano 3090, Neuquén Capital. Firma: Somos Piedra.
- **Cliente (Tomás, 18/11/2026):** solo si nos pasan nombre o CUIT. Si no, la cotización va sin bloque CLIENTE: no se pregunta ni se completa.
- Tomás pasa el total; el precio por unidad = total ÷ cantidad. Subtotal y total los calcula el script.
- Numeración correlativa (última usada: ver los `.json` de esta carpeta).
