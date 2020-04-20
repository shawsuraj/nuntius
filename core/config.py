import json

def config_tmeplate(url = None, hostname = None, username = None, password = None) :
    data = {"isConfigured" : True,
            'url':url,
            'ftp': {
                'host': hostname,
                'username': username,
                'password': password
                }
            }
    return data

def config_setup() :
    return config_tmeplate(input("Url: "),
                    input("Hostname: "),
                    input("Username: "),
                    input("Password: "))
