#!/usr/bin/python3

from Defs.connection import verify_connection
from Defs.main import start_menu
from Defs.main import exit_message
from Defs.main import port_selector
from Defs.mail_input_data import getMailInput
from Defs.email_handler import EmailHandler
from Defs.startServer import start_ngrok_server
from Defs.startServer import start_serveo_server
from Defs.startServer import start_locahostrun_server

verify_connection()

if __name__ == "__main__" :
    
    try : 
        start_menu()
        port = port_selector()
        
        # print (port)
        
        frm, to, subject, body = getMailInput() # Get email inputs

        # start_server()
        url = start_locahostrun_server(port)

        email_handler = EmailHandler(url)
        response = email_handler.send_email(frm, to, subject, body)

        print("PHP response: {}".format(response))

        if "sent successfully" in response.lower():
            print ("\033[92mEmail sent successfully\033[0m") # Green
        else:
             print ("\033[91mEmail failed to send\033[0m") # Red

        print("Press Ctrl+C to exit...")

        while True :
            pass
        

    except KeyboardInterrupt:
        # ngrok_controller.stop()
        exit_message()