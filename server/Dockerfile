FROM python:3.11-slim

WORKDIR /app

# install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["daphne", "-p", "80", "-b", "0.0.0.0", "config.asgi:application"]
