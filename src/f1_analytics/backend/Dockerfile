FROM python:3.13-slim

# App-root i containern
WORKDIR /app

# Kopiera in backend + knowledge_base (lärar-likt)
COPY backend backend
COPY knowledge_base knowledge_base

# Installera uv
RUN pip install --no-cache-dir uv

# Gå in i backend-projektet
WORKDIR /app/backend

# Installera dependencies från pyproject.toml
RUN uv export --format requirements-txt -o requirements.txt && \
    uv pip install --system -r requirements.txt

# Starta FastAPI på port 80
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
