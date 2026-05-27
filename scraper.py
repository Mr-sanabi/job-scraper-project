import requests
import logging
import time

def fetch_page(url: str, config: list[dict]) -> str | None:
    delay = config["scraping"]["delay"]
    try:
        response = requests.get(url)
        time.sleep(delay)
    except requests.exceptions.RequestException as e:
        logging.error(f"Reques failed: {e}")
        return None

    if response.status_code != 200:
        logging.error(f"Bad status code: {response.status_code}")
        return None
    
    logging.info(f"Page fetch successfully: {url}")
    return response.text