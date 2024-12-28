import requests
import re

class EmailHandler :
    def __init__(self, php_url) :
        self.php_url = php_url
    
    # Email check to avoid php error 403
    def is_valid_email(email) :
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_regex, email))

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
        
        except requests.exceptions.RequestException as e :
            return "Failed to send email: {}".format(e)
        
        except Exception as e :
             return "An unexpected error occurred: {}".format(e)