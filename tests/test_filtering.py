from src.filtering import filter_jobs

def test_filter_jobs_matches_case_insensitively_and_skips_invalid_values():
    jobs = [
        {"title": "Senior Python Developer", "link": "/jobs/1"},
        {"title": "Backend Engineer", "link": "/jobs/2"},
        {"title": None, "link": "/jobs/3"},
        {"title": "   ", "link": "/jobs/4"},
    ]

    keywords = [" PYTHON ", None, "", 123]
    result = filter_jobs(jobs, keywords)
    assert len(result) == 1
    assert result[0]["title"] == "Senior Python Developer"