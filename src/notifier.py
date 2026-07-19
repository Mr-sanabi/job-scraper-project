import smtplib
from email.mime.text import MIMEText
import logging

def send_email(jobs: list[dict], config: dict) -> bool:
    if not jobs:
        logging.error("job list is empty")
        return False
    
    try:
        email_from = config["email"]["from"]
        email_to = config["email"]["to"]
        password = config["email"]["password"]
        limit = config["email"]["limit"]

        text = ""

        for job in jobs[:limit]:
            text += f"title: {job['title']}\n"
            text += f"link: {job['link']}\n\n"
            text += "--------------------\n"
            
        msg = MIMEText(text)
        msg["From"] = email_from
        msg["To"] = email_to
        msg["Subject"] = "Вакансии за сегодня:"

        logging.info("Connecting to SMTP...")
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            logging.info("Message sending...")
            server.login(email_from, password)
            server.sendmail(email_from, email_to, msg.as_string())
        logging.info("Message sent")
        return True
    except Exception as e:
        logging.error(f"Sending error: {e}")
        return False