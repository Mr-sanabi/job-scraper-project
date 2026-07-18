import requests
import logging
import time

def fetch_page(url: str, config: dict) -> str | None:
    delay = config["scraping"]["delay"]
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        time.sleep(delay)
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None

    logging.info(f"Page fetch successfully: {url}")
    return response.text