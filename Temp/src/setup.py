import table
import os # lib for a start os.sytem
table.Logger.info("[INFO] this real-time app") # log

def main(): # func for venv
    os.system(table.PYTHON() + " app.py") # start a python file from cmd

table.venv(main) # starting a venv
