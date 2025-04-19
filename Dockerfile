FROM python:3.13-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /code/app

WORKDIR /code/app

# CMD ["uvicorn", "app.asgi:application", "--workers", "4", "--host", "0.0.0.0", "--port", "8000"]

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--threads", "4"]
