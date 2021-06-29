import platform
import json
import os
import shutil


def Install(name, dir): # func Install() for a validating install package
    if platform.system() == "Windows": # for windows
        os.system("tar -x -v -f " + name + ".zip") # unzip with tar.exe
        with open(name + '/table.json') as json_file: # opening a table.json file in a package
            data = json.load(json_file) # get a data with dict type from file

            # Print the type of data variable
            print("Type:", type(data))

            # Print the data of dictionary
            print("src-dir => { " + data["src-dir"] + " }")

            path = name + "/" + data["src-dir"] # path to src
            os.chdir(path) # go to dir src
            os.system("python setup.py") # opening a main file
            os.chdir('../..')
            shutil.rmtree(name)
    elif platform.system() == "Linux": # for a linux
        os.system("unzip " + name + ".zip") # unzip


        # Opening JSON file
        with open(name + '/table.json') as json_file: # opening a table.json file in a package
            data = json.load(json_file) # get a data with dict type from file

            # Print the type of data variable
            print("Type:", type(data))

            # Print the data of dictionary
            print("src-dir => { " + data["src-dir"] + " }")

            path = name + "/" + data["src-dir"] # seting a path to src dir
            os.chdir(path) # go to src
            os.system("sudo python setup.py") # starting a main file
            os.chdir('../..') # leave from dir
            shutil.rmtree(name) # deleting a dir
    elif platform.system() == "Darwin": # for a darwin (MAC OS X)
        os.system("unzip " + name + ".zip") #unzip

        # Opening JSON file
        with open(name + '/table.json') as json_file: # opening a table.json file in a package
            data = json.load(json_file) # get a data with dict type from file

            # Print the type of data variable
            print("Type:", type(data))

            # Print the data of dictionary
            print("src-dir => { " + data["src-dir"] + " }")

            path = name + "/" + data["src-dir"] # go to main src dir
            os.chdir(path) # go to
            os.system("sudo python setup.py") # start a main file
            os.chdir('../..') # leave from src dir
            shutil.rmtree(name) # deleting a package dir
