# e2e del panel desde la VM del chat (11/11/2026)

Los e2e de `E:\somos-piedra-panel` (`e2e:corte`, `e2e:empleados`, `e2e:meta`, `e2e:piedra`) se pueden correr desde el chat,
sin pedirle un `.cmd` a Tomás. La carpeta montada tiene el `node_modules` de Windows y la VM no trae Chromium ni llega al
CDN de Playwright, así que se arma una copia en `/tmp`:

```bash
# 1. Copia del repo, sin node_modules ni .env.local (el modo local no usa Supabase)
mkdir -p /tmp/panel && cd "$HOME/mnt/somos-piedra-panel" && \
  tar --exclude=./node_modules --exclude=./dist --exclude=./.git --exclude=./capturas --exclude=./prompts --exclude=./.env.local -cf - . | (cd /tmp/panel && tar xf -)
# 2. Dependencias de Linux (18 s) y Chromium por npm (11 s). Cada paso en su propia llamada: al terminar la llamada se mata todo lo que quedó corriendo.
cd /tmp/panel && npm ci --cache /tmp/npm-cache --no-audit --no-fund
cd /tmp/panel && npm i --no-save @sparticuz/chromium --cache /tmp/npm-cache --no-audit --no-fund
# 3. Desempaquetar Chromium en /tmp (TMPDIR=/tmp: /sessions no tiene lugar)
cd /tmp/panel && TMPDIR=/tmp AWS_LAMBDA_JS_RUNTIME=nodejs22.x node --input-type=module -e "import c from '@sparticuz/chromium'; console.log(await c.executablePath())"
# 4. Certificado del sustituto de Google Fonts (la VM bloquea fonts.googleapis.com y el e2e corta por el error de consola)
openssl req -x509 -newkey rsa:2048 -nodes -keyout /tmp/stub.key -out /tmp/stub.crt -days 2 -subj "/CN=fonts.googleapis.com" -addext "subjectAltName=DNS:fonts.googleapis.com,DNS:fonts.gstatic.com"
# 5. Copiar estos tres archivos a /tmp y correr (un e2e por llamada: e2e:piedra tarda ~100 s y el tope es 180 s)
cp run-e2e.sh chrome-wrap.sh stub-fonts.mjs /tmp/ && chmod +x /tmp/run-e2e.sh /tmp/chrome-wrap.sh
/tmp/run-e2e.sh corte 80; /tmp/run-e2e.sh empleados 85
/tmp/run-e2e.sh meta 160
/tmp/run-e2e.sh piedra 172
```

Qué es cada archivo:
- `chrome-wrap.sh`: lo que va en `CHROME_PATH`. Lanza `/tmp/chromium` sin sandbox, sin el proxy de la VM y con Google Fonts apuntando al sustituto.
- `stub-fonts.mjs`: el sustituto (https en 127.0.0.1:8443, devuelve una hoja de estilos vacía).
- `run-e2e.sh <nombre> [segundos]`: levanta el sustituto, corre `scripts/e2e-<nombre>.mjs` y muestra el código de salida, los pasos ok y lo que no fue ok.

Límite: es Chromium 153 de Linux sobre una copia, no el Chrome de Windows ni producción. Sirve para saber si un cambio rompió un recorrido.
Resultado del 11/11 sobre `b6cb9af`: corte 24 pasos, empleados 12, meta 11, piedra 40, los cuatro con salida 0.
