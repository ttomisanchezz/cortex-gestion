#!/bin/sh
export LD_LIBRARY_PATH=/tmp/al2023/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
export FONTCONFIG_PATH=/tmp/fonts
unset HTTP_PROXY HTTPS_PROXY http_proxy https_proxy ALL_PROXY all_proxy FTP_PROXY ftp_proxy NO_PROXY no_proxy
echo "$@" > /tmp/chrome-args.log
exec /tmp/chromium --no-sandbox --disable-setuid-sandbox --disable-dev-shm-usage --disable-gpu --no-proxy-server --ignore-certificate-errors "--host-resolver-rules=MAP fonts.googleapis.com 127.0.0.1:8443, MAP fonts.gstatic.com 127.0.0.1:8443" "$@"
