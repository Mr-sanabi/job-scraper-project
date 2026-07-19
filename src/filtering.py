def filter_jobs(jobs: list[dict], keywords: list[str]) -> list[dict]:
    filtered_jobs = []

    for job in jobs:
        title = job.get("title", "")

        if not isinstance(title, str) or not title.strip():
            continue
        
        normalized_strip = title.strip().lower()
        for keyword in keywords:
            if not isinstance(keyword, str):
                continue
            
            normalized_keyword = keyword.strip().lower()

            if not normalized_keyword:
                continue
            
            if normalized_keyword in normalized_strip:
                filtered_jobs.append(job)
                break

    return filtered_jobs