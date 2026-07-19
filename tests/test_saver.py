from src.saver import save_json, save_csv
import json
import csv

def test_save_json_creates_file_and_preserves_data(tmp_path):
    jobs = [
        {"title": "Python Developer", "link": "https://example.com/jobs/1"},
        {"title": "Backend Developer", "link": "https://example.com/jobs/2"},
    ]

    output_path = tmp_path / "nested" / "jobs.json"

    result = save_json(jobs, str(output_path))
    assert result is True
    assert output_path.exists()
    loaded_file = json.loads(output_path.read_text(encoding="utf-8"))
    assert loaded_file == jobs
    temporary_path = output_path.with_suffix(output_path.suffix + ".tmp")
    assert not temporary_path.exists()


def test_save_csv_creates_file_and_preserves_rows(tmp_path):
    jobs = [
        {"title": "Python Developer", "link": "https://example.com/jobs/1"},
        {"title": "Backend Developer", "link": "https://example.com/jobs/2"},
    ]

    output_path = tmp_path / "nested" / "jobs.csv"
    result = save_csv(jobs, str(output_path))
    assert result is True
    assert output_path.exists()
    with open (output_path, "r",encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    
    assert rows == jobs
    temporary_path = output_path.with_suffix(output_path.suffix + ".tmp")
    assert not temporary_path.exists()

def test_save_csv_returns_false_for_empty_data(tmp_path):
    jobs = {}
    output_path = tmp_path / "nested" / "jobs.csv"
    result = save_csv(jobs, str(output_path))
    assert result == False