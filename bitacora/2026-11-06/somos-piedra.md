CIERRE — somos-piedra — 06/11 13:50 (cotizaciones)

Hecho:
- Cotización mejorada en PDF (v2): logo, N°, Emite con CUIT 20-45734050-9, cliente, tabla cantidad × precio, total, condiciones y firma. Presupuesto formal para Santiago Braidotti (CUIT 20-39128602-8): 42 m² de pórfido adoquín × $85.000 = $3.570.000 SIN IVA.
- Panel (E:\somos-piedra-panel): pantalla «Cotizaciones» con historial, PDF, compartir, duplicar y anular. Migración 0072 (tabla presupuestos, fuera del sync), dominio, datos, PDF y 13 tests. Commits 80ac718 y 6fc5d06 (SUBIR-COTIZACIONES.cmd). tsc y vite build en verde; 109/111 archivos de tests en la VM (los otros 2 se cuelgan ahí también sin el cambio).
- La migración en la base real la frenó el control automático (2 veces): queda en el .cmd para Tomás. No se deployó.
Decisiones (qué y por qué):
- Cotizaciones siempre «SIN IVA», sin calcular el IVA (Tomás, para siempre).
- Rediseño Mostrador aprobado para producción (Tomás).
- Historial con número correlativo; renglones del catálogo (precio EFECTIVO, editable) o libres (recomendadas y elegidas por Tomás).
Pendientes nuevos:
- [ ] Doble clic en SUBIR-COTIZACIONES.cmd (migrar + deploy) — Tomás
- [ ] WhatsApp del negocio para el PDF; confirmar validez y forma de pago por defecto; npm test en Windows — Tomás/Claude
Pendientes cerrados:
- Revisar y aprobar la corrida 2026-11-02a (rediseño) — aprobado
- Commitear scripts/cambiar-dueno.mjs — ya estaba (a0e9fba)
Aprendizajes (errores o trucos para no repetir):
- Tests desde la VM de Linux (esbuild/rollup de Linux en /tmp, TMPDIR, tandas de 180 s). Migrar la base real desde el chat lo frena el control: .cmd para Tomás. El panel vive en E:\somos-piedra-panel.
Próximo paso: Tomás corre SUBIR-COTIZACIONES.cmd y Claude prueba el panel en línea con el login de soporte — Modelo: —
Cambia una regla de plata o del método: no

