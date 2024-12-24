import requests

class EmailHandler :
    def __init__(self, php_url) :
        self.php_url = php_url

    def send_email(self, frm, to, subject, body) :
        data = {
            "from" : frm,
            "to": to,
            "subject": subject,
            "body": body,
        }

        try :
            response = requests.post(self.php_url, data=data)
            return response.txt
        except Exception as e :
            return "Failed to send email: {}".format(e)
