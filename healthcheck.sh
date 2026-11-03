#!/usr/bin/env bash
URL="${1:-http://127.0.0.1:8080}"
LOG="${2:-logs/health.log}"
mkdir -p "$(dirname "$LOG")"

CODE=000
for ATTEMPT in 1 2 3 4 5 6 7 8 9 10; do
  CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 15 "$URL" || echo 000)
  if [ "$CODE" = "200" ] || [ "$CODE" = "302" ]; then
    break
  fi
  [ "$ATTEMPT" -lt 5 ] && sleep 3
done

echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $CODE $URL" | tee -a "$LOG"

[ "$CODE" = "200" ] || [ "$CODE" = "302" ]
