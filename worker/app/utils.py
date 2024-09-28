import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def send_product_to_server(product: dict):
    """
    Method will sent product details to main server via an internal api.
    """
    try:
        response = requests.post(
            url="http://server/internal/handle_products/",
            json=product,
            timeout=10
        )
        response.raise_for_status()
        logger.info(f"Product sent to server. Status: {response.status_code}")
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}, {http_err.response.json()}")
    except requests.exceptions.RequestException as err:
        logger.error(f"Error occurred while sending product: {err}")
