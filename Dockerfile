FROM python:3.11.0-slim

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the application code
COPY . /app
WORKDIR /app

# Create and activate a virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies and set permissions
RUN pip install --upgrade pip \
    && pip uninstall -y psycopg2 \
    && pip uninstall -y psycopg2-binary \
    && pip install -r requirements.txt \
    && pip install --no-cache-dir psycopg2 \
    && chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]