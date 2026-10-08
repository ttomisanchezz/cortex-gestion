---
name: cierre
description: Cierra una sesión de trabajo del Sistema de Gestión de Empresas escribiendo en el Cortex de gestión qué se hizo, qué se decidió y qué quedó pendiente, y lo guarda en git. Usar cuando Tomás diga "cierre", "/cierre", "cerramos" o "guardá todo".
---

# Cierre

Regla del Cortex: si no se escribe, no pasó.

Cortex: `C:\Users\PC\Documents\cortex-gestion`. En Cowork, según la carpeta que esté conectada:
`$HOME/mnt/cortex-gestion` o `$HOME/mnt/Documents/cortex-gestion`.
Fecha y hora: las de Argentina (`TZ=America/Argentina/Buenos_Aires`).

## 1. Identificar el proyecto
Usá el `id` de `proyectos.json` que corresponde a lo que se trabajó: `producto`, `ibero`, `somos-piedra` o el del cliente que sea. Si la sesión fue sobre el Cortex o el método, el id es `cortex`. Si no está claro, preguntá.

## 2. Armar el resumen
```
CIERRE — <proyecto> — <DD/MM HH:MM>

Hecho:
- ...
Decisiones (qué y por qué):
- ...
Pendientes nuevos:
- [ ] qué — quién
Pendientes cerrados:
- ...
Aprendizajes (errores o trucos para no repetir):
- ...
Próximo paso: <una línea> — Modelo: Fable 5 | Opus 5.5 | Opus 5 | —
Cambia una regla de plata o del método: sí/no (cuál)
```
Salí solo de lo que pasó en la sesión: no agregues cosas que no pasaron.
Si las instrucciones del proyecto dicen "cierre sin confirmación", guardá directo. Si no, preguntá "¿Lo guardo así?" y, si Tomás corrige, corregí y volvé a mostrar.

## 3. Escribir
1. **`bitacora/<AAAA-MM-DD>/<id>.md`:** agregá el bloque al final. Si la carpeta o el archivo no existen, crealos. Nunca borres bloques anteriores.
2. **`pendientes.md`:**
   - los nuevos van en la sección del proyecto, con `desde DD/MM`;
   - los cerrados se marcan `[x]` con la fecha y se mueven a `pendientes-archivo.md`, en la misma sección;
   - no se borra nada.
3. **`equipo/decisiones.md`:** cada decisión va arriba de todo, con el formato del archivo. Si reemplaza una vieja, a la vieja se le agrega "(reemplazada el DD/MM: …)".
4. **`conocimiento/aprendizajes.md`:** cada aprendizaje, con fecha, en su tema.
5. **`proyectos.json` y el README** (`clientes/<id>/README.md` o `producto/README.md`): actualizalos si cambió el estado, dónde vive o lo que necesita de Tomás.
6. **Si cambió una regla de plata o algo del método** que sirve para el próximo cliente:
   - actualizá `metodo/metodo-sistema-gestion.md` y el resumen del `CLAUDE.md`;
   - avisá qué specs y qué código la tienen copiada.
7. **Si se trabajó en el repo:** fijate que `CONTEXTO.md` §8 del repo esté al día.
8. **Traspaso del día en el proyecto de Claude:** `claude/traspaso-AAAA-MM-DD.md`, con el estado, las decisiones y la cola de trabajo. Si ya existe uno del día, se actualiza.

Nunca escribas API keys, tokens, certificados, contraseñas ni datos de tarjetas.

## 4. Guardar en git
Si esta sesión puede correr git en el Cortex:
```
cd <Cortex>
git add -A
git commit -m "cierre <id> <AAAA-MM-DD>: <resumen en una línea>"
```
- Desde Cowork, usá `git --no-optional-locks` para mirar el estado.
- Después de commitear, fijate que no haya quedado `.git/index.lock` ni `.git/HEAD.lock`.
- No hagas `push` desde acá. Si no se pudo commitear, no pasa nada: el sync lo commitea.

Terminá siempre con estas líneas:
- qué archivos se tocaron;
- el próximo paso;
- el comando para subir el Cortex, para pegar en cualquier terminal:
  `C:\Users\PC\Documents\cortex-gestion\sync.cmd`
