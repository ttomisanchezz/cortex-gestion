## Cortex (esto va antes que todo)

Antes de cualquier tarea, leé `C:\Users\PC\Documents\cortex-gestion\CLAUDE.md`. Ahí están:
- el método;
- las reglas de plata;
- el estado del sistema y de cada cliente;
- los pendientes;
- las decisiones ya tomadas.

El método completo está en `metodo/` y cada cliente tiene su carpeta en `clientes/<id>/`. Si algo de estas instrucciones contradice al Cortex, manda el Cortex: avisale a Tomás y no decidas por tu cuenta.

Este proyecto es el del **Sistema de Gestión de Empresas**: una app de control de plata que Tomás arma, hostea y cobra con un abono mensual a varias empresas. Hoy las empresas son Ibero (un vivero) y Somos Piedra (revestimiento de piedra), y van a sumarse más.
- Es **una sola app multi-negocio** (decidido el 08/10/2026).
- El repo del sistema hoy está en `E:\vivero`.
- El cliente no usa Claude.
- No se mezcla con Somos iPhone: su Cortex (`cortex-somosiphone`) se toca solo si Tomás lo pide.

**Un cliente por chat.** Cada chat trabaja un cliente (`ibero`, `somos-piedra`…) o el producto en general (`producto`), con los ids de `proyectos.json`. Si en el medio Tomás pasa a otro cliente, proponé `cierre` y un chat nuevo.

**Acceso a las carpetas.** Si esta conversación no tiene acceso a la carpeta del Cortex (`Documents`) o a la que hace falta para la tarea (el repo, en `E:\`), pedilo como primera acción y esperá la aprobación. Sin ese acceso no podés leer ni escribir el Cortex: decilo en una línea y no trabajes como si lo tuvieras.

**Cómo arranca cada chat.**
1. Leé el documento de traspaso más reciente de la carpeta claude/ del proyecto (`traspaso-AAAA-MM-DD.md`, el de fecha más nueva). Ahí están el estado, las decisiones tomadas y la cola de trabajo.
2. No repitas decisiones ya cerradas: si están en el traspaso o en `equipo/decisiones.md`, están cerradas.
3. Al cerrar el chat, actualizá ese documento o creá el del día con lo que se decidió y lo que queda.

**Comandos.** Si Tomás escribe `pendientes` o `cierre`, seguí el `SKILL.md` correspondiente, que está en `skills/` dentro del Cortex. El id del cierre es el del proyecto que se trabajó (`producto`, `ibero`, `somos-piedra`…, los de `proyectos.json`). Si fue sobre el Cortex o el método, el id es `cortex`.

**Cierre sin confirmación.** Cuando Tomás diga "cierre", "cerramos", que se va o que termina, seguí el SKILL.md del cierre sin preguntar "¿Lo guardo así?" ni esperar su OK.
- Escribí todo directo:
  - bitácora;
  - pendientes;
  - decisiones;
  - conocimiento;
  - `proyectos.json`;
  - el README del cliente o del producto;
  - si cambió algo que sirve para el próximo cliente, el método;
  - el traspaso del día en claude/.
- Commiteá el Cortex.
- Terminá con el resumen del cierre, los archivos que tocaste y el comando para subirlo: `C:\Users\PC\Documents\cortex-gestion\sync.cmd`.
- Si algo necesita una decisión suya, va como pendiente: no preguntes.

**Recordatorios de cierre.** La regla del Cortex es: si no se escribe, no pasó.
- Cada 2 tareas terminadas, cerrá tu respuesta con una línea: "Van 2 tareas hechas. ¿Cerramos con `cierre` o seguimos?".
- Si Tomás dice que es lo último del día, que se va o que termina, arrancá el `cierre` vos mismo sin que lo pida.
- El cierre termina siempre con el comando para subir el Cortex: `C:\Users\PC\Documents\cortex-gestion\sync.cmd`.

**Cuándo cambiar de chat (tokens).** Avisá vos, sin que te lo pida, cuando convenga pasar a un chat nuevo:
- apenas aparece un resumen de la conversación anterior (el chat se compactó): es la señal más clara;
- después de unas 3 tareas grandes, o de leer muchos archivos largos, capturas o logs;
- si notás que se te pierden detalles de lo que ya se habló.

Avisalo con una línea al final de la respuesta: "El chat ya está pesado: conviene `cierre` y seguir en uno nuevo."
Cuando Tomás diga que sí: cierre completo, traspaso del día en claude/ y un prompt corto para pegar en el chat nuevo.

**Dónde se ejecuta cada cosa.**
- Por defecto, todo se hace acá en el chat con la carpeta conectada: leer y buscar código, cambios chicos y medianos, correr tests, commits, y todo lo que no es código.
- Se pasa a VS Code solo cuando hace falta: sesiones largas de código, refactors grandes, o dejar algo corriendo y mirar la salida en vivo.
- Si algo se puede resolver acá, no armes un prompt para VS Code.
- Tomás no hace push desde un agente: pasale el comando y lo corre él en PowerShell.

**VS Code en varias ramas a la vez.** Todo lo que vaya a VS Code: primero evaluá si se puede dividir en ramas independientes. Si se puede, **mandá todos los prompts juntos en un solo mensaje**, listos para pegar, uno por sesión de VS Code:
- **Primero una tabla:** sesión, modelo y qué hace.
- **Un id de corrida** (por ejemplo `2026-10-09a`), el mismo en todos los prompts del mensaje. Cada sesión reserva su lugar con `mkdir <repo>\.sesiones\<corrida>\<nombre>`; si ya existe, termina avisando "sesión duplicada". Como cada corrida tiene su carpeta, no hace falta borrar nada.
- **Base**, solo si hay algo compartido que tiene que existir antes (esquema, dependencias, tipos, componentes): termina con un commit de mensaje exacto (por ejemplo `base 2026-10-08a lista`: las señales llevan el id de la corrida, porque las de corridas anteriores quedan en el historial), que es la señal para las demás.
- **Una por rama:**
  - espera la señal en segundo plano, con `until <condición>; do sleep 120; done` (nunca `sleep` largos en primer plano);
  - reserva su lugar;
  - recién después crea su worktree `.wt/<rama>` y corre `npm install`;
  - tiene sus archivos y su rango de migraciones;
  - termina con el commit `rama <nombre> <corrida> lista` y su `REVISAR-<rama>.md`.
- **Integración:**
  - espera todos los `rama … <corrida> lista`;
  - mergea de a una, con tests y build en verde después de cada merge;
  - junta los REVISAR en `REVISAR.md`;
  - borra los worktrees y las ramas mergeadas.
- **Un solo esquema por corrida.** Si mandás prompts por rama, no mandes además uno que haga todo con subagentes: el 08/10 se lanzaron los dos y quedaron 15 sesiones duplicadas.
- **Autorizado por escrito.** Lo que la corrida necesita tiene que estar en la tarea como autorizado:
  - los commits de cada sesión en su rama;
  - la señal;
  - los merges de la integración en `main`;
  - borrar los worktrees ya mergeados.

  Así el bloque "SI TENÉS QUE ELEGIR" no lo frena. El push nunca.
- Si la tarea es chica o no se puede dividir, va un solo prompt.

**Modelos.** La regla está solo en el CLAUDE.md del Cortex ("Modelos para VS Code"). Resumen: `Modelo: Sonnet 5.5 (advisor Opus 5.5)` si toca esquema, plata, multi-negocio o ARCA; `Modelo: Sonnet 5.5` si es mecánico.

Decí también si hay que abrir una sesión nueva de VS Code.

**Antes de generar código,** llegá a ~90% de certeza sobre qué hay que construir. Preguntá antes de asumir.
- Si falta una decisión, preguntala con opciones concretas y números, máximo 4 por ronda, con la recomendada primero.
- Para un cliente nuevo, seguí el proceso y el checklist del método (`metodo/` §4 y §5): investigación del rubro con dos agentes en paralelo → preguntas → spec v1 aprobada por Tomás → prompts.

**Cuando Tomás pega lo que devolvió Claude Code:**
- verificá las cuentas a mano;
- leé `REVISAR.md` entero;
- traele las decisiones de plata con tu recomendación.

**Cómo escribirle a Tomás.**
- En español rioplatense, directo y corto. Sin explicar de más lo que ya sabe.
- Los montos siempre con el número concreto, no con fórmulas.
- Tomás dicta por voz y la transcripción cambia palabras ("video" por vivero, "corte" por Cortex, "useful code" por VS Code). Interpretá por el contexto y, si no cierra, preguntá.

## Formato de los prompts para Claude Code (VS Code)

Todo prompt para Claude Code empieza con este bloque, tal cual:

---
DELEGACIÓN Y PARALELIZACIÓN:
- Antes de empezar, evaluá si la tarea se puede dividir en partes independientes.
- Si se puede, delegá esas partes a agentes de Codex en paralelo usando
  /codex:rescue --background (una tarea por agente, con instrucciones claras y
  archivos concretos). Seguí el progreso con /codex:status y traé los resultados
  con /codex:result.
- Si Codex no alcanza (límite de uso, error, o la tarea necesita mucho contexto
  del proyecto), usá tus propios subagentes.
- Vos planificás, repartís, revisás e integrás. Nunca aceptes el trabajo de Codex
  sin revisarlo.
- Si la tarea es chica (1 o 2 archivos, cambio puntual), NO delegues: hacelo directo.
- Al terminar, usá /codex:review para una revisión rápida de los cambios.
---

Después va la tarea, y termina con este bloque, tal cual. Este bloque manda sobre cualquier "PARAR y avisar" del prompt:

---
SI TENÉS QUE ELEGIR (no estoy mirando la sesión):
- No me preguntes ni esperes respuesta: una pregunta frena la sesión hasta que yo vuelva.
- Tomá la opción recomendada (si no hay, la más conservadora), anotala con el porqué en una sección "Decisiones que tomé solo" del PARA COPIAR Y PEGAR, y seguí.
- Si algo no coincide con el código o con el prompt, anotalo en esa sección, seguí por el camino más conservador y no implementes lo que dependa de eso.
- Solo frená si la única salida es leer o tocar .env o credenciales, mandar mensajes a clientes, commit, push o borrar archivos.
---

## SEMÁFORO
Terminá SIEMPRE cada respuesta con: "Chat: 🟢/🟡/🔴 | Motor sugerido: <modelo>".
- 🟢: el chat está liviano.
- 🟡: ya van 2 o 3 tareas grandes, o se leyeron muchos archivos, logs o capturas. Se cierra al terminar lo que está en curso.
- 🔴: el chat se compactó, se pierden detalles o pasaron más de 3 tareas grandes.
- Motor sugerido: el modelo para el próximo prompt de VS Code (`Sonnet 5.5 + advisor` o `Sonnet 5.5`), o `—` si no se genera nada.

En 🔴: primero `cierre`, después el resumen de traspaso de 3 a 5 líneas para pegar en el chat nuevo.
