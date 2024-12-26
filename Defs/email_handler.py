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
            "submit": "send"
        }

        try :
            response = requests.post(self.php_url, 
                                     data=data, 
                                     timeout = 10)
            
            response.raise_for_status()

            return response.text
        
        except Exception as e :
            return "Failed to send email: {}".format(e)
