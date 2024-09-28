# e-commerce-platform-scraper

This project is an asynchronous web scraper built with Django, Scrapy, and Celery. It scrapes product information from the https://www.digimart.net a Japanese e-commerce platform and sends the data to the frontend via WebSocket.

## Getting Started

### Prerequisites

- Docker

### Setup

1. **Rename .env.sample to .env**:
    ```bash
    mv .env.sample .env
    ```

2. **Build and Start the Services**:
   ```bash
   docker compose up --build
   ```

3. **Run Database Migrations**:    
    ```bash
    docker compose exec server python manage.py migrate
    ```

4. **Access the Application**:
    Open your web browser and go to
    ```
    http://localhost:8000
    ```
5. **Start Scraping**:
    Click the button labeled "Start Scraping" to initiate the scraping process. The application will begin scraping product details and display them in real-time through the WebSocket connection.