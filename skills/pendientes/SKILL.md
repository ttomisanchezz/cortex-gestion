---
name: pendientes
description: Arma la lista de lo que Tomás tiene que hacer hoy en el Sistema de Gestión de Empresas (el producto y cada cliente), leyendo el Cortex de gestión. Usar cuando diga "pendientes", "/pendientes", "qué tengo hoy" o "en qué quedamos".
---

# Pendientes

Arma la lista del día. **Solo lee: no modifica ningún archivo.**

Cortex: `C:\Users\PC\Documents\cortex-gestion`. En Cowork, según la carpeta que esté conectada:
`$HOME/mnt/cortex-gestion` o `$HOME/mnt/Documents/cortex-gestion`.

## 1. Leer, en este orden
1. `CLAUDE.md` del Cortex.
2. `proyectos.json`: el campo `prioridad` define el orden de todo.
3. `pendientes.md`.
4. `bitacora/`: las carpetas de los últimos 3 días que existan.
5. El traspaso más reciente del proyecto de Claude (`claude/traspaso-AAAA-MM-DD.md`), si se puede leer.
6. El estado de cada proyecto activo (campo `detalle` de `proyectos.json`):
   - el README del cliente o del producto;
   - el del repo del sistema: `E:\vivero\CONTEXTO.md` §8 y `REVISAR.md` §4.

Si un archivo no se puede leer, decilo en una línea y seguí. Nunca inventes un estado.

## 2. Cruzar
- Lo que `pendientes.md` da como abierto pero el README o el repo dan como hecho (o al revés) → "Desactualizado".
- Un pendiente con más de 7 días sin movimiento en la bitácora → "Desactualizado".
- Lo que depende de otra persona (un cliente, su contador) → "Esperando".
- Las fechas que se vienen (vencimiento de certificados de ARCA, vencimientos del cliente, pruebas acordadas) → "Ojo con".

## 3. Responder con este formato
```
PENDIENTES — <día DD/MM>

HOY (máximo 5, en orden de prioridad)
1. <qué> — <proyecto o cliente> — <quién>
   Por qué hoy: <una línea>
   Si va a VS Code: Modelo: Sonnet 5.5 + advisor | Sonnet 5.5 (y si se divide en ramas)

ESPERANDO
- <qué> — <de quién>

OJO CON
- <fecha> — <qué vence>

DESACTUALIZADO
- <qué no coincide y dónde>
```

Para el modelo, aplicá la regla del CLAUDE.md: si equivocarse cuesta caro o se arrastra, Sonnet 5.5 + advisor; si no, Sonnet 5.5.

Cerrá con una sola pregunta: "¿Arrancamos por el 1?".
