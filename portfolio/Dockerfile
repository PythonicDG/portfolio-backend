FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev postgresql-client && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput || true

CMD ["hypercorn", "portfolio.asgi:application", "-b", "0.0.0.0:8002", "-w", "4"]

