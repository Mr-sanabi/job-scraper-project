from src.state import save_sent_links, load_seen_links

def test_save_and_load_seen_links_normalizes_and_deduplicates(tmp_path):
    jobs = [
        {"link": " https://example.com/jobs/1 "},
        {"link": "https://example.com/jobs/1"},
        {"link": ""},
        {"link": None},
        {"link": "https://example.com/jobs/2"},
    ]
    file_path = tmp_path / "nested" / "seen.json"

    result = save_sent_links(jobs, str(file_path))
    assert result == True
    loaded_links = load_seen_links(str(file_path))
    assert set(loaded_links) == {
    "https://example.com/jobs/1",
    "https://example.com/jobs/2",
    }