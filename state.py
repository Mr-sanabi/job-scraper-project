import json
import logging

def load_seen_links(filename: str) -> list[str]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.warning(f"File not found: {filename}")
        return []
        

def save_seen_links(seen_links, filename: str):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(seen_links, file, indent=4, ensure_ascii=False)
    except OSError as e:
        logging.error(f"Failed to save file: {e}")
        return

def filter_new_jobs(jobs, seen_links):
    new_jobs = []

    for job in jobs:
        link = job.get("link", "")

        if link not in seen_links:
            new_jobs.append(job)
            seen_links.append(link)
        
    return new_jobs