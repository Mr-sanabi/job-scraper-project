import json
import logging

def load_seen_links(filename: str) -> list[str]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.warning(f"File not found: {filename}")
        return []
    except json.JSONDecodeError:
        logging.warning(f"File is empty or invalid JSON: {filename}")
        return []

def save_sent_links(jobs_to_send: list[dict], filename: str) -> bool:
    try:
        old_links = load_seen_links(filename)

        new_links = []

        for job in jobs_to_send:
            link = job.get("link")

            if link and link not in old_links and link not in new_links:
                new_links.append(link)

        
        update_links = old_links + new_links

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(update_links, file, indent=4, ensure_ascii=False)

        logging.info(f"Saved {len(new_links)} new sent links")
        return True
    
    except OSError as e:
        logging.error(f"Failed to save file: {e}")
        return False
