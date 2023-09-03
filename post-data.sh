#!/bin/bash

set -e

cd "$(dirname "$0")"
source "./.env/bin/activate"

INVERTER_ADDRESS="192.168.178.58"

echo "[`date`] Collecting data from ${INVERTER_ADDRESS}"

python3 invert-client.py 192.168.178.58 | curl -s --request POST "localhost:8086/api/v2/write?org=solar-watch&bucket=solar-data&precision=s" \
        --header "Authorization: Token top-secret-auth-token" \
        --header "Content-Type: text/plain; charset=utf-8" \
        --header "Accept: application/json" \
        --data-binary @-
