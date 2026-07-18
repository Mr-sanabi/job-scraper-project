import json
import csv
import logging
from pathlib import Path

def save_json(data: list[dict], filename: str) -> bool:
    path = Path(filename)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = path.with_suffix(path.suffix + ".tmp")

        with open(temporary_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        temporary_path.replace(path)
    except OSError as e:
        logging.error(f"Failed to save file: {e}")
        return False
    
    logging.info(f"Output saved to: {filename}")
    return True
 

def save_csv(data: list[dict], filename: str) -> bool:
    if not data:
        return False
    

    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    temporary_path = path.with_suffix(path.suffix + ".tmp")
    fields = data[0].keys()
    try:    
        with open(temporary_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
        temporary_path.replace(path)
    except OSError as e:
            logging.error(f"Failed to save file: {e}")
            return False    
        
    logging.info(f"Output saved to: {filename}")
    return True