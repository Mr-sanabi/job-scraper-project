# Job Scraper with Email Alerts

A Python 3.11+ script that checks Python.org jobs and emails new keyword matches. It also saves the parsed listings to CSV and JSON.

## Run

Copy `config.example.json` to `config.json` and fill in the email settings. Use a Gmail app password and never commit the config.

```bash
python -m pip install -r requirements.txt
python -m src.main
```

Outputs: `all_jobs.csv`, `all_jobs.json`, `notified_links.json`, and `scraper.log`.

The source and keywords are set in `src/main.py`. Uses Gmail SMTP and depends on the site's HTML. Run it manually or with an external scheduler; notification state updates after a successful send.

## Tests

```bash
python -m pip install pytest
python -m pytest -q
```

Tests mock SMTP and do not send real email.
