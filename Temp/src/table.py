import os
import platform
import sys


class pip:
    @staticmethod
    def install(package):
        Logger.info('installing package pip: ' + package)
        os.system(PYTHON() + " -m pip install " + package)
class Logger:
    @staticmethod
    def info(text):
        print("[INFO] " + text)
    @staticmethod
    def warning(text):
        print("[WARNING] " + text)
    @staticmethod
    def error(text):
        print("[ERROR] " + text)
def windows(func):
    if platform.system() == "Windows":
        func()
def linux(func):
    if platform.system() == "Linux":
        func()
def darwin(func):
    if platform.system() == "Darwin":
        func()

def venv(func):
    os.system('python -m venv .')
    func()

def gethome():
    return os.path.expanduser("~")

def PYTHON():
    PYTHON = 'not found system'
    def sub():
        PYTHON = 'bin/python.exe'
    def subl():
        PYTHON = './bin/python'
    windows(sub)
    linux(subl)
    darwin(subl)
    return PYTHON
