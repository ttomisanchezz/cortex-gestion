#!/bin/bash
# uso: run-e2e.sh <corte|empleados|meta|piedra> [segundos]
N=$1; T=${2:-170}
cd /tmp/panel && export TMPDIR=/tmp CHROME_PATH=/tmp/chrome-wrap.sh
: > /tmp/stub-pedidos.log
node /tmp/stub-fonts.mjs & STUB=$!
sleep 1
S=$(date +%s)
timeout $T node scripts/e2e-$N.mjs > /tmp/e2e-$N.log 2>&1; RC=$?
kill $STUB 2>/dev/null
echo "e2e:$N rc=$RC seg=$(( $(date +%s) - S )) pasos_ok=$(grep -c '… ok' /tmp/e2e-$N.log) pedidos_fuente=$(wc -l < /tmp/stub-pedidos.log)"
grep -v '… ok' /tmp/e2e-$N.log | tail -15
