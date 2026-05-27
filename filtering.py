def filter_jobs(jobs: list[dict], keywords: list[str]) -> list[dict]:
    filtered_jobs = []

    for job in jobs:
        title = job.get("title", "").lower()

        for keyword in keywords:
            if keyword.lower() in title:
                filtered_jobs.append(job)
                break

    return filtered_jobs