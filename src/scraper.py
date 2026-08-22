import requests
import logging

def fetch_page(url: str) -> str | None:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return None

    logging.info(f"Page fetch successfully: {url}")
    return response.text