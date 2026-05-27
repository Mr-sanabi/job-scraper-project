from scraper import fetch_page
from parser import parse_job
from filtering import filter_jobs
from saver import save_json, save_csv
from state import load_seen_links, save_seen_links, filter_new_jobs
from notifier import send_email
import json
import logging

URL = "https://www.python.org/jobs/"
KEYWORDS = ["python", "remote", "developer", "backend"]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("scraper.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
    

def load_config(filename: str) -> dict | None:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return
    except json.JSONDecodeError:
        print(f"Config file is not valid JSON: {filename}")
        return
    
def main() -> None:
    config = load_config("config.json")
    html = fetch_page(URL, config)
    

    if html is None:
        logging.error("No HTML received. Program stopped")
        return
    
    jobs = parse_job(html)

    if jobs is None:
        logging.error("No jobs(list) received. Program stopped")
        return
    
    filtered_jobs = filter_jobs(jobs, KEYWORDS)
    seen_links = load_seen_links("seen_jobs.json")
    new_jobs = filter_new_jobs(jobs, seen_links)


    save = save_json(new_jobs, "new_jobs.json")
    # save_csv(filtered_jobs, "new_jobs.csv")

    if not save:
        logging.error("Output was not saved")
        return 
    
    save_seen_links(seen_links, "seen_jobs.json")

    send_email(new_jobs, config)

    logging.info(f"All jobs: {len(jobs)}")
    logging.info(f"Seen links: {len(seen_links)}")
    logging.info(f"Filtered jobs: {len(filtered_jobs)}")
    
    logging.info("Program finished successfully")

if __name__ == "__main__":
    main()