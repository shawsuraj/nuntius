#!/usr/bin/env python3
#Version - v2.0.1

import argparse
import sys
import os
import json

from core.connect import *
from core.config import *
# from core.log import *
# from core.ftp import *

parser = argparse.ArgumentParser(description="Send fake emails...!!!")
parser.add_argument('-s','--setup',
                    action = "store_true",
                    help = "Setup the server..")
parser.add_argument('-v', '--verbose',
                    action="store_true",
                    help = "Show progress")
# parser.add_argument('--newmail',
#                     action = "store_true",
#                     help = "Se ] nd a new mail via terminal")
# parser.add_argument('-l','-log',
#                     action = "store_true",
#                     help = "Keep a log of sent mails.")

args = parser.parse_args()

class mailT:
    def __init__(self):
        self.frm = None
        self.to = None
        self.sub = None
        self.body = None

    def printData(self) :
        print(self.frm,
              self.to,
              self.sub,
              self.body)

def banner() :
    os.system('clear')
    print(''' _ __  _   _ _ __ | |_(_)_   _ ___    _
| '_ \| | | | '_ \| __| | | | / __|  | |
| | | | |_| | | | | |_| | |_| \__ \  |_|
|_| |_|\__,_|_| |_|\__|_|\__,_|___/  (_)
    ''')

def getMailInput(mail) :
    mail.frm = input("From :")
    mail.to = input("To :")
    mail.sub = input("Subject : ")
    mail.body = multiLineInput()

    return frm, to, sub, body

def multiLineInput() :
    print ("Body :\n")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    return text

# check all the reuired paths
def check_path() :
    if not os.path.isdir('data'):
        if args.verbose:
            print('[*] Creating data folder.')
        os.mkdir('data')

    if not os.path.exists('data/server_config.json') :
        if args.verbose:
            print('[*] Creating configuration file(json).')
        with open('data/server_config.json', 'w'):
            pass
        wJson('data/server_config.json',{"isConfigured" : False})

    # if not os.path.exists('/data/email_log.json'):
    #     with open('/data/email_log.json', 'w'):
    #         pass

# basic setup
def baseSetup(configPath) :
    check_path()

    if args.setup :
        wJson('data/server_config.json',{"isConfigured" : False})

    configData = rJson(configPath)

    if not configData['isConfigured']:
        print("The server is not configured. Enter the server detials (You can skip username and password options) :")
        wJson(configPath,config_setup())
    else :
        if args.verbose:
            print("Server is Configured. Proceeding...")
    # rJson()

# read jsonfile
def rJson(path) :
    try :
        with open(path) as f:
            data = json.load(f)
            return data
    except :
        print ("Error occured while reading {} json file.".fromat(path))

# wrtie to jsonfile
def wJson(path, data) :
    try :
        json_object = json.dumps(data, indent = 2)
        with open(path, 'w') as f:
            print("tried")
            # configData = rJson(configPath)
            # print(configData)
            f.write(json_object)
    except :
        print ("Error occured while writing to {} json file.".format(path))

# send mail
def sendMail(mail, configData) :
    encd = encData(mail)
    url = configData['url']
    if args.verbose:
        print('[*] Connectiing to the server.')
    req = connect(url,encd)
    if args.verbose:
        print('[*] Sending mail')
    if send(req) :
        return True

    # Get the url from server config json and then use the connect def


if __name__ == "__main__" :
    try :
        banner()
        configPath = "data/server_config.json"
        # logPath = "data/email_log.json"
        baseSetup(configPath)

        mail = mailT()
        getMailInput(mail)

        if sendMail(mail, rJson(configPath)) :
            print("Mail sent successfully! :)")
        else:
            print("Failed :(")

    except KeyboardInterrupt:
        banner()
        print("\nExiting..!!")


# email.printData()
