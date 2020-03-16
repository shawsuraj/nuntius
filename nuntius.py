#!/usr/bin/env python3
import argparse
import sys
import json

from core.connect import *
# from core.config import *
# from core.log import *
# from core.ftp import *

# parser = argparse.ArgumentParser(description="Send fake emails...!!!")
# parser.add_argument('-s','--setup',
#                     action = "store_true",
#                     help = "Setup the server..")
# parser.add_argument('--newmail',
#                     action = "store_true",
#                     help = "Send a new mail via terminal")
# parser.add_argument('-l','-log',
#                     action = "store_true",
#                     help = "Keep a log of sent mails.")

class svc:
    def __init__(self, frm, to, sub, body):
        self.frm = frm
        self.to = to
        self.sub = sub
        self.body = body

    def printData(self) :
        print(self.frm,
              self.to,
              self.sub,
              self.body)

def usrInput() :
    frm = input("From :")
    to = input("To :")
    sub = input("Subject : ")
    body = multiInput()

    return frm, to, sub, body

def multiLineInput() :
    print ("Body :")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    return text

def getData() :
    frm, to, sub, body = usrInput()
    mailData = svc(frm, to, sub, body)
    return mail

def check_path() :
    if not os.path.isdir('/data'):
        os.mkdir('/data')

    if not os.path.exists('/data/server_config.json'):
        with open('/data/server_config.json, 'w'):
            pass

    # if not os.path.exists('/data/email_log.json'):
    #     with open('/data/email_log.json', 'w'):
    #         pass

def baseSetup() :
    check_path()
    # readJson()



def readJson(path) :
    try :
        with open(path) as f:
            data = json.load(f
            return data
    except :
        print ("Error occured while opening json file.")


def config() :
    check_path()    # Error handling for path

def sendMail(mail, configData) :
    encd = encData(mail)
    url = configData['url']
    req = connect(url,encd)
    if send(req)
    return True

    # Get the url from server config json and then use the connect def


if __name__ = "__main__" :
    configPath = "data/server_config.json"
    # logPath = "data/email_log.json"
    baseSetup()

    configData = readJson(configPath)
    if configData['isConfigured'] == "False" :
        print("The server is not configured. Please configure it using '--setup' parameter.")
    else :
        mail = getData()
        if sendMail(mail, configData) :
            print("Success!")
        else:
            print("Failed")

# email.printData()
