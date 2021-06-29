import platform

import os

def Pack(name, dir): # Func pack for pack a package
    if platform.system() == "Windows": # for windows
        os.system("tar -a -c -f " + name + ".zip " + dir) # zip a folder with a package with tar.exe (MinGW binaries)
    elif platform.system() == "Linux": # for linux
        os.system("zip -r " + name + ".zip " + dir) # zip a folder with a package
    elif platform.system() == "Darwin": # for Darwin (mac OS X)
        os.system("zip -r " + name + ".zip " + dir) # zip a folder with a package