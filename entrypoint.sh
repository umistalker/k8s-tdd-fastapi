#!/bin/bash

echo "Waiting for postgres..."
while ! nc -z web-db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

case "$1" in
  "web")
   uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
    ;;
  *)
    echo "Unknown command: $1"
    exit 1
    ;;
esac
