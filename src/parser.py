import logging

from bs4 import BeautifulSoup

def parse_job(html: str) -> list[dict]:
    logging.info("Start scraping")
    soup = BeautifulSoup(html, "html.parser")

    job_blocks = soup.find_all("li")
    jobs = []

    for block in job_blocks:
        title_element = block.find("h2")

        if title_element is None:
            continue

        link_element = title_element.find("a")

        if link_element is None:
            continue

        title = link_element.get_text(strip=True)
        link = link_element.get("href", "")

        jobs.append({
            "title": title,
            "link": "https://www.python.org" + link
        })
    logging.info(f"Python jobs collected: {len(jobs)}")
    return jobs