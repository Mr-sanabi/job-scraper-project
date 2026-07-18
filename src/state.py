import json
import logging
from pathlib import Path

def load_seen_links(filename: str) -> list[str]:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            rows = json.load(file)
            if not isinstance(rows, list):
                logging.warning("Rows is not list")
                return []
            else:
                normalized_rows = []
                for row in rows:
                    if not isinstance(row, str):
                        continue
                    else:
                        normalized_row = row.strip()
                        if not normalized_row:
                            continue
                        else:
                            normalized_rows.append(normalized_row)
        
        return normalized_rows

    except FileNotFoundError:
        logging.warning(f"File not found: {filename}")
        return []
    except json.JSONDecodeError:
        logging.warning(f"File is empty or invalid JSON: {filename}")
        return []
    except OSError:
        logging.error("Error")
        return []

def save_sent_links(jobs_to_send: list[dict], filename: str) -> bool:
    try:
        old_links = load_seen_links(filename)

        new_links = []

        for job in jobs_to_send:
            link = job.get("link")

            if not isinstance(link, str):
                continue
            
            normalized_link = link.strip()
            if not normalized_link:
                continue


            if normalized_link and normalized_link not in old_links and normalized_link not in new_links:
                new_links.append(normalized_link)

        
        update_links = old_links + new_links

        path = Path(filename)
        path.parent.mkdir(parents=True, exist_ok=True)

        temporary_path = path.with_suffix(path.suffix + ".tmp")
        with open(temporary_path, "w", encoding="utf-8") as file:
            json.dump(update_links, file, indent=4, ensure_ascii=False)
        temporary_path.replace(path)

        logging.info(f"Saved {len(new_links)} new sent links")
        return True
    
    except OSError as e:
        logging.error(f"Failed to save file: {e}")
        return False
