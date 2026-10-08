# Aprendizajes
Errores que no queremos repetir y trucos que funcionaron. Cada uno con su fecha.

## Sesiones de Claude Code
- **08/10/2026 — No lanzar dos esquemas a la vez.** Se largaron a la vez `PROMPT-todo.md` (una sesión con subagentes) y los 9 prompts de `prompts/` (una sesión por rama). Quedaron unas 15 sesiones duplicadas. Una segunda "base" pisó `package.json` unos minutos, y varios `npm install` chocaron en el mismo worktree (`ENOTEMPTY`, paquetes incompletos). **Un solo esquema por corrida.**
- **08/10/2026 — La guarda `.sesiones/` funcionó.**
  - Cada sesión hace `mkdir <repo>\.sesiones\<nombre>` antes de tocar nada. Si ya existe, termina avisando "sesión duplicada".
  - El `npm install` va **después** de reservar, nunca antes.
  - Desde el 08/10 cada corrida tiene su id (`.sesiones\<corrida>\<nombre>`), así no hace falta borrar nada: el bloque "SI TENÉS QUE ELEGIR" frena ante los borrados.
- **08/10/2026 — Esperas en segundo plano.** `sleep 540` en primer plano gasta un turno cada 9 minutos. Hay que usar `until <condición>; do sleep 120; done` en segundo plano: no gasta turnos hasta que termina.
- **08/10/2026 — Señales con commits de mensaje exacto.** "fase A lista" para la base y "rama <nombre> lista" para cada rama. La integración espera los 7 con `git log --all --grep`.

## Plata
- **08/10/2026 — El IVA a favor no es ganancia.** En la prueba de punta a punta del vivero, el resultado ($35.563) daba más que la ganancia bruta ($28.773), porque el IVA a favor sumaba. Corregido: queda en $16.440.
- **08/10/2026 — La merma y los faltantes de arqueo son pérdidas reales.** La spec no los restaba y se corrigió. En cada spec nueva, chequear la fórmula del resultado contra el método §3.
- **08/10/2026 — Recibir una transferencia no tiene comisión.** Pedir un % para Banco dejaba el saldo en FALTA DATO sin motivo.

## Técnica
- **08/10/2026 — Hosting:** Vercel Hobby no permite uso comercial.
- **08/10/2026 — Supabase gratis:** deja pocos proyectos activos y pausa los que no se usan.
- **08/10/2026 — La identidad git global de la PC es `frannnn87` (de Fran).** Los commits del vivero salieron con ese autor. En cada repo nuevo hay que configurar `user.name` y `user.email` locales.
- **08/10/2026 — Datos de prueba viejos:** en modo local, después de cambiar el esquema o las reglas, hay que borrar los datos del sitio en el navegador.
- **08/10/2026 — El Edge de la PC no está donde se esperaba.** La prueba de punta a punta usa Chrome: el script busca los dos.

## Trabajo con Tomás
- **08/10/2026 — Tomás dicta por voz.** La transcripción cambia palabras: "video" por vivero, "corte" o "xottex" por Cortex, "Diphons" por iPhones, "useful code" por VS Code. Se interpreta por el contexto y, si no cierra, se pregunta.
- **08/10/2026 — Tomás quiere los prompts listos para pegar**, todos juntos, y ver en la tabla qué modelo va en cada sesión.
