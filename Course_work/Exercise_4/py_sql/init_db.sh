#!/usr/bin/env bash
set -e

DB_FILE="/app/flag.db"
INIT_SQL="/app/init.sql"

# If sqlite3 isn't installed at runtime the script will fail — Dockerfile installs sqlite3.
if ! command -v sqlite3 >/dev/null 2>&1; then
  echo "sqlite3 not found in container. Exiting."
  exit 1
fi

# Initialize DB if it doesn't exist
if [ ! -f "$DB_FILE" ]; then
  echo "Initializing database at $DB_FILE..."
  sqlite3 "$DB_FILE" < "$INIT_SQL"
  echo "Database created."
else
  echo "Database already exists at $DB_FILE — skipping init."
fi

# Exec the passed command (this will be `python app.py` from Dockerfile/CMD)
exec "$@"
