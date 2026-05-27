
# Job Scraper with Email Alerts

## Overview

Python automation tool that scrapes job listings from Python.org Jobs, filters them by keywords, tracks already seen listings, saves results to JSON/CSV, and sends email alerts for new matching jobs.

## Problem

Manually checking job boards is repetitive and inefficient. This tool automates job monitoring and notifies the user only when new relevant jobs appear.

## Features

- Scrapes real job listings from Python.org Jobs
- Extracts job title and link
- Filters jobs by keywords
- Tracks seen jobs using `seen_jobs.json`
- Saves results to JSON and CSV
- Sends email alerts for new jobs
- Uses `config.json` for settings
- Includes timeout handling
- Includes logging and error handling
- Uses modular project structure

## Tech Stack

- Python
- requests
- BeautifulSoup
- JSON / CSV
- smtplib
- logging
- venv

## Project Structure

- main.py
- scraper.py
- parser.py
- cleaner.py
- saver.py
- state.py
- notifier.py
- config.example.json
- requirements.txt

## Configuration

Create a local `config.json` based on `config.example.json`.

Do not commit `config.json` because it contains private email credentials.

## How to Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Example Output

```json
{
  "title": "Python Developer",
  "link": "https://www.python.org/jobs/..."
}
```

## What I Learned

* Building a modular scraper
* Parsing real HTML
* Filtering structured data
* Saving JSON/CSV output
* Tracking seen links
* Sending email alerts
* Using config files
* Adding logging and error handling

    