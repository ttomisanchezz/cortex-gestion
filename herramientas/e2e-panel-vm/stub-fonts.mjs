// Sustituto local de Google Fonts para la VM (el proxy de la VM lo bloquea): devuelve una hoja de estilos vacía.
import https from 'node:https'
import fs from 'node:fs'
const pedidos = []
https.createServer({ key: fs.readFileSync('/tmp/stub.key'), cert: fs.readFileSync('/tmp/stub.crt') }, (req, res) => {
  pedidos.push(req.headers.host + req.url)
  fs.appendFileSync('/tmp/stub-pedidos.log', req.headers.host + req.url.slice(0, 80) + '\n')
  res.writeHead(200, { 'content-type': 'text/css', 'access-control-allow-origin': '*' })
  res.end('/* stub */')
}).listen(8443, '127.0.0.1')
