# Use a slim Python image
FROM python:3.11-slim

WORKDIR /app

# Install sqlite3 and any build deps; clean up apt cache
RUN apt-get update && \
    apt-get install -y --no-install-recommends sqlite3 && \
    rm -rf /var/lib/apt/lists/*

# Copy application and DB initializer
COPY app.py /app/
COPY init.sql /app/
COPY init_db.sh /app/

# Install python deps
RUN pip install --no-cache-dir flask

# Make sure the init script is executable
RUN chmod +x /app/init_db.sh

# Create DB at build time so image contains ready DB (optional redundant step)
# This ensures the image already has a DB; the entrypoint script still checks at runtime.
RUN sqlite3 /app/flag.db < /app/init.sql || true

EXPOSE 5000

# Use entrypoint to initialize DB if needed, then run the app
ENTRYPOINT ["/app/init_db.sh"]
CMD ["python", "app.py"]
