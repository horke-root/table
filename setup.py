#!venv/bin/python
import os
import shutil
import platform
BIN = 'venv/bin/pyinstaller'
os.system('./' + BIN + " -F -c main.py")

print('[WARNING] is not setuputils app')

if platform.system() == 'Darwin':
    print("if app could not copy to /usr/local/bin/table run setup.py with sudo or root ")
    shutil.copy('dist/main', '/usr/local/bin/table')
if platform.system() == 'Linux':
    print("if app could not copy to /usr/local/bin/table run setup.py with sudo or root ")
    shutil.copy('dist/main', '/usr/local/bin/table')
if platform.system() == 'Windows':
    appdata = os.getenv('APPDATA')
    pather = appdata + '/Table'
    os.mkdir(pather)
    shutil.copy('dist/main.exe', pather+'/main.exe')
    print('[WARNING] ADD DIR TO PATH { ' + pather + ' } for use in command prompt')

print('Yesss!')