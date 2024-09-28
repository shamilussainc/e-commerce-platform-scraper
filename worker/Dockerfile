FROM python:3.11-slim

WORKDIR /app

# Install the dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app

# Run Celery worker with your app
CMD ["celery", "-A", "app.main", "worker", "--loglevel=info"]
