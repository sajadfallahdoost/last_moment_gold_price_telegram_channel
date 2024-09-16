import requests
from .config import API_URL
from .logger import setup_logger

logger = setup_logger()


def fetch_latest_prices():
    logger.info("Fetching latest prices from the API.")
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            logger.info("Successfully fetched the data.")
            return data
        else:
            logger.error(f"Failed to fetch data: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"Error occurred during API call: {str(e)}")
        return None
