from src.parser import parse_job

def test_parse_job_skips_invalid_and_duplicate_jobs():
    html = """
    <ul>
        <li>
            <h2><a href="/jobs/1/">Python Developer</a></h2>
        </li>
        <li>
            <h2><a href="/jobs/1/">Python Developer Duplicate</a></h2>
        </li>
        <li>
            <h2><a>Missing Link</a></h2>
        </li>
        <li>
            <h2></h2>
        </li>
    </ul>
    """
    result = parse_job(html)
    assert len(result) == 1
    assert result[0]["title"] == "Python Developer"
    assert result[0]["link"] == "https://www.python.org/jobs/1/"