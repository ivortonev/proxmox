#!/bin/bash

export TELEGRAM_BOT_TOKEN="9090909090:ABABABABABABABABABABABABABABABABABA"
export CHAT_ID="-1010101010101"
MESSAGE="$*"

curl -X POST -H "Content-Type: application/json" \
     -d "{\"chat_id\": \"${CHAT_ID}\", \"text\": \"${MESSAGE}\", \"parse_mode=\'HTML\'\"}" \
     "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage"
