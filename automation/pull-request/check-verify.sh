#! /bin/bash

FILE=$1

if [[ -z "$FILE" ]]; then
  echo "Usage: $0 <path-to-gradle-file>"
  exit 1
fi

# Extract verifyInstrumentation block
block=$(awk '/verifyInstrumentation[[:space:]]*\{/,/\}/' "$FILE")

if [[ -z "$block" ]]; then
  echo "  Error: verifyInstrumentation block not found."
  exit 1
fi

if !(echo "$block" | grep -q 'passesOnly') ; then
  echo "  Error: passesOnly not found inside verifyInstrumentation block."
  exit 1
fi