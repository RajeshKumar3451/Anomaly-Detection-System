FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

COPY requirements-api.txt .

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements-api.txt

COPY . .

# Create pipeline during build
RUN python -m src.models.train_ml

EXPOSE 8000

CMD ["sh", "-c", "uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000}"]