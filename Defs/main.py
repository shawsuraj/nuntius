import os
from shutil import rmtree
from shutil import copyfile

from Defs.realtor import renewDir

clear_screen = os.system("clear")
logo = """
███╗   ██╗██╗   ██╗███╗   ██╗████████╗██╗██╗   ██╗███████╗
████╗  ██║██║   ██║████╗  ██║╚══██╔══╝██║██║   ██║██╔════╝
██╔██╗ ██║██║   ██║██╔██╗ ██║   ██║   ██║██║   ██║███████╗
██║╚██╗██║██║   ██║██║╚██╗██║   ██║   ██║██║   ██║╚════██║
██║ ╚████║╚██████╔╝██║ ╚████║   ██║   ██║╚██████╔╝███████║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝ ╚═════╝ ╚══════╝                                                         
"""

def start_menu() :
    clear_screen
    print(logo)

    print("\n1. Send spoofed email")
    print("\n2. Spam spoofed emails (Incoming)")

    option = input("\nnuntius >>> ")

    if option == "1" :
        start_spoof()
    
    else : 
        print("\nChoose correct option")
        start_menu()

def start_spoof() :
    pass
    # os.system("chmod -R 777 Server")
    # renewDir("Server/www")
    # copyfile("WebServer/php/mail.php", "Server/www/mail.php")

def port_selector() :
    print("\nEnter a port number between 1-65535, eg : 8080, 1337")
    option = input("\nnuntius >>> ")

    try:
        if int(option) > 65535 or int(option) < 1:
            return port_selector()
        else:
            return option
    except:
        return port_selector()


def exit_message() :
    clear_screen
    print(logo)
    print("\n Exiting")
