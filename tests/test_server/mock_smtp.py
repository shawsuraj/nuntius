import responses

def mock_smtp_service(success=True, error_code = 200):
    if success:
        responses.add(
            responses.POST,
            "http://localhost:8000/mail.php",
            json={"message": "Mail sent successfully"},
            status=200,
        )
    else:
        responses.add(
            responses.POST,
            "http://localhost:8000/mail.php",
            json={"error": "SMTP service error"},
            status=error_code,
        )