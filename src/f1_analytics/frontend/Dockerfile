FROM python:3.13-slim

WORKDIR /app

# Kopiera in frontend
COPY frontend frontend

# Installera uv
RUN pip install --no-cache-dir uv

# Gå in i frontend-projektet
WORKDIR /app/frontend

# Installera dependencies från pyproject.toml
RUN uv export --format requirements-txt -o requirements.txt && \
    uv pip install --system -r requirements.txt

EXPOSE 8501

# Starta Streamlit
CMD ["streamlit", "run", "streamlit.py", "--server.address=0.0.0.0", "--server.port=8501"]
