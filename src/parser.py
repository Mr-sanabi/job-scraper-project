import logging
from urllib.parse import urljoin

from bs4 import BeautifulSoup

def parse_job(html: str) -> list[dict]:
    logging.info("Start scraping")
    soup = BeautifulSoup(html, "html.parser")
    seen_link = set()

    base_url = "https://www.python.org"
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
        if not title:
            continue
        link = link_element.get("href", "")
        if not link:
            continue

        full_url = urljoin(base_url, link)

        if full_url in seen_link:
            continue

        seen_link.add(full_url)

        jobs.append({
            "title": title,
            "link": full_url
        })
    logging.info(f"Python jobs collected: {len(jobs)}")
    return jobs