import os
import platform
import sys



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
    print('System : ' + platform.system())
    def sub():
        PYTHONl = 'bin/python.exe'
        return PYTHONl
    def subl():
        PYTHONl = './bin/python'
        return PYTHONl
    windows(sub)
    linux(subl)
    darwin(subl)
class pip:
    @staticmethod
    def install(package):
        Logger.info('installing package pip: ' + package)
        os.system(PYTHON() + " -m pip install " + package)
