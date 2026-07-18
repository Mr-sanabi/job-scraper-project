import json
import csv
import logging

def save_json(data: list[dict], filename: str) -> bool:
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except OSError as e:
        logging.error(f"Failed to save file: {e}")
        return
    
    logging.info(f"Output saved to: {filename}")
    return True
 

def save_csv(data: list[dict], filename: str) -> bool:
    if not data:
        return
        
    fields = data[0].keys()
    try:    
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

    except OSError as e:
            logging.error(f"Failed to save file: {e}")
            return False    
        
    logging.info(f"Output saved to: {filename}")
    return True