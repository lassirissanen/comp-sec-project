# Stage 1: Base build stage
FROM python:3.13-slim AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production stage
FROM python:3.13-slim

# 1. Create a non-root user
RUN useradd -m -r appuser

# 2. Create app directory, owned by root
RUN mkdir /app

WORKDIR /app

# 3. Copy Python dependencies from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# 4. Copy application code as root (default)
COPY . .

# 5. Create writable logs and media directories, owned by appuser
RUN mkdir -p /var/log/django /app/project/media/profile_pics \
    && chown appuser:appuser /var/log/django /app/project/media/profile_pics

# 6. Make entrypoint executable
RUN chmod +x /app/entrypoint.prod.sh

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 7. Switch to non-root user for runtime
USER appuser

EXPOSE 8000

WORKDIR /app/project
CMD ["/app/entrypoint.prod.sh"]
