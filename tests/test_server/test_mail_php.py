import pytest
import requests
import responses

from tests.test_server import mock_smtp

localhost_url = "http://localhost:8000/mail.php"  #localhost localhost_url

@pytest.fixture
def valid_email_data():
    return {
        "fromemail": "valid.sender@example.com",
        "toemail": "valid.recipient@example.com",
        "subject": "Test Email",
        "body": "This is a test email sent via pytest.",
    }

@pytest.fixture
def invalid_email_data():
    return {
        "fromemail": "invalid_email",
        "toemail": "invalid_email",
        "subject": "Invalid Email Test",
        "body": "Testing invalid email addresses.",
    }

@pytest.fixture
def missing_fields_data():
    return {
        "fromemail": "",
        "toemail": "",
        "subject": "",
        "body": "",
    }

def test_successful_email(valid_email_data):
    response = requests.post(localhost_url, data=valid_email_data)
    assert response.status_code == 200, "Expected HTTP 200 for successful email."
    assert "Email sent successfully" in response.text, "Expected success message."

def test_invalid_email_addresses(invalid_email_data):
    response = requests.post(localhost_url, data=invalid_email_data)
    assert response.status_code == 422, "Expected HTTP 422 for invalid input."
    assert "Invalid input" in response.text, "Expected invalid input message."

def test_missing_fields(missing_fields_data):
    response = requests.post(localhost_url, data=missing_fields_data)
    assert response.status_code == 400, "Expected HTTP 400 for missing fields."
    assert "Missing required fields" in response.text, "Expected missing fields message."

@responses.activate
def test_mail_php_smtp_error():
    mock_smtp(success=False)

    response = requests.post(localhost_url, data=valid_email_data)
    assert response.status_code == 500, "Expected HTTP status 500 for SMTP error"
    assert "SMTP service error" in response.json()["error"], "Expected SMTP error message"

@responses.activate
def test_mail_php_service_unavailable(valid_email_data):
    mock_smtp.mock_smtp_service(success=False, error_code=503)

    response = requests.post(localhost_url, data=valid_email_data)

    assert response.status_code == 503, "Expected HTTP 503 for service unavailable"
    assert "Service unavailable" in response.json()["error"], "Expected 'Service unavailable' error message"