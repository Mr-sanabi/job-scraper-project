import smtplib
from email.mime.text import MIMEText
import logging

def send_email(jobs: list[dict], config: dict) -> None:
    if not jobs:
        return
    
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
        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()
        logging.info("Message sending...")
        server.login(email_from, password)
        server.sendmail(email_from, email_to, msg.as_string())
        server.quit()
        logging.info("Message sent")
    except Exception as e:
        logging.error(f"Sending error: {e}")