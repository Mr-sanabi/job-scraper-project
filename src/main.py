from scraper import fetch_page
from parser import parse_job
from filtering import filter_jobs
from saver import save_json, save_csv
from state import load_seen_links, save_sent_links
from notifier import send_email
import json
import logging


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
    
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("scraper.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
config = load_config("config.json")
URL = "https://www.python.org/jobs/"
KEYWORDS = ["python", "remote", "developer", "backend"]
EMAIL_LIMIT = config["email"]["limit"]
NOTIFIED_LINKS_FILE = "notified_links.json"
 
def main() -> None:
    html = fetch_page(URL, config)
    
    if html is None:
        logging.error("No HTML received. Program stopped")
        return
    
    all_jobs = parse_job(html)

    if all_jobs is None:
        logging.error("No jobs(list) received. Program stopped")
        return
    
    filtered_jobs = filter_jobs(all_jobs, KEYWORDS)
    sent_links = load_seen_links(NOTIFIED_LINKS_FILE)
    new_for_email = [
        job for job in filtered_jobs
        if job["link"] not in sent_links
    ]

    jobs_to_send = new_for_email[:EMAIL_LIMIT]

    if jobs_to_send:
        send_email(jobs_to_send, config)
        save_sent_links(jobs_to_send, NOTIFIED_LINKS_FILE)
    else:
        logging.error("No new jobs to send.")

    save = save_json(all_jobs, "all_jobs.json")
    save_csv(all_jobs, "all_jobs.csv")

    if not save:
        logging.error("Output was not saved")
        return 

    logging.info(f"All jobs: {len(all_jobs)}")
    logging.info(f"Seen links: {len(sent_links)}")
    logging.info(f"Filtered jobs: {len(filtered_jobs)}")
    
    logging.info("Program finished successfully")

if __name__ == "__main__":
    main()