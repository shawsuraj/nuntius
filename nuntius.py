#!/usr/bin/env python3
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
    body = multiLineInput()

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
    return mailData

def check_path() :
    if not os.path.isdir('data'):
        os.mkdir('data')

    if not os.path.exists('data/server_config.json'):
        with open('data/server_config.json', 'w'):
            pass
        wJson('data/server_config.json',{"isConfigured" : False,})

    # if not os.path.exists('/data/email_log.json'):
    #     with open('/data/email_log.json', 'w'):
    #         pass

def baseSetup() :
    check_path()
    # rJson()



def rJson(path) :
    try :
        with open(path) as f:
            data = json.load(f)
            return data
    except :
        print ("Error occured while opening json file.")

def wJson(path, data) :
    try :
        json_object = json.dumps(data, indent = 2)
        with open(path, 'w') as f:
            print("tried")
            # configData = rJson(configPath)
            # print(configData)
            f.write(json_object)
    except :
        print ("Error occured while opening json file.")


def config() :
    check_path()    # Error handling for path

def sendMail(mail, configData) :
    encd = encData(mail)
    url = configData['url']
    req = connect(url,encd)
    if send(req) :
        return True

    # Get the url from server config json and then use the connect def


if __name__ == "__main__" :
    try :
        configPath = "data/server_config.json"
        # logPath = "data/email_log.json"
        baseSetup()

        configData = rJson(configPath)
        print(configData)
        if not configData['isConfigured']:
            wJson(configPath,config_setup())
            print("The server is not configured. Please configure it using '--setup' parameter.")
        else :
            mail = getData()
            if sendMail(mail, configData) :
                print("Success!")
            else:
                print("Failed")
    except KeyboardInterrupt:
        print("\nExiting..!!")


# email.printData()
