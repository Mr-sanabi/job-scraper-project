from unittest.mock import MagicMock
from src.notifier import send_email
import src.notifier as notifier_module

def test_send_email_sends_limited_jobs(monkeypatch):
    fake_smtp = MagicMock()
    fake_server = fake_smtp.return_value.__enter__.return_value

    monkeypatch.setattr(notifier_module.smtplib, "SMTP", fake_smtp)

    jobs = [
        {"title": "Python Developer", "link": "https://example.com/jobs/1"},
        {"title": "Backend Developer", "link": "https://example.com/jobs/2"},
        {"title": "Data Engineer", "link": "https://example.com/jobs/3"},
    ]

    config = {
        "email": {
            "from": "sender@example.com",
            "to": "receiver@example.com",
            "password": "test-password",
            "limit": 2,
        }
    }

    result = send_email(jobs, config)
    assert result is True
    fake_server.starttls.assert_called_once_with()
    fake_server.login.assert_called_once_with(
        "sender@example.com",
        "test-password",
    )
    fake_server.sendmail.assert_called_once()

    sent_message = fake_server.sendmail.call_args.args[2]
    assert "Python Developer" in sent_message
    assert "Backend Developer" in sent_message
    assert "Data Engineer" not in sent_message


def test_send_email_returns_false_for_empty_jobs(monkeypatch):
    fake_smtp = MagicMock()

    monkeypatch.setattr(notifier_module.smtplib, "SMTP", fake_smtp)

    config = {
        "email": {
            "from": "sender@example.com",
            "to": "receiver@example.com",
            "password": "test-password",
            "limit": 2,
        }
    }
    result = send_email([], config)
    assert result == False
    fake_smtp.assert_not_called()


def test_send_email_returns_false_when_smtp_fails():
    fake_smtp = MagicMock()

    jobs = [
        {"title": "Python Developer", "link": "https://example.com/jobs/1"},
    ]
    config = {
        "email": {
            "from": "sender@example.com",
            "to": "receiver@example.com",
            "password": "test-password",
            "limit": 2,
        }
    }    

    fake_smtp.side_effect = OSError("SMTP unavailable")
    result = send_email(jobs, config)
    assert result == False