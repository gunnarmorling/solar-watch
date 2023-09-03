#!/bin/sh

python3 invert-client.py 192.168.178.58 | curl --request POST "localhost:8086/api/v2/write?org=solar-watch&bucket=solar-data&precision=s" \
        --header "Authorization: Token top-secret-auth-token" \
        --header "Content-Type: text/plain; charset=utf-8" \
        --header "Accept: application/json" \
        --data-binary @-