from os.path import isdir
from os import mkdir
from shutil import rmtree

def check_path(path) :
    return True if isdir(path) else False

def create_file(path, filename) :
    try :
        with open(path, "w"):
            pass
    except :
        print ("Failed to create {0} in {1}, create it manually to proceed".format(filename, path))

def create_folder(path) :
    mkdir(path)

def renewDir(path) :
    if check_path(path) :
        rmtree (path)

    create_folder(path)
