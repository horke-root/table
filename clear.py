import os

TEMP = ['build', 'dist']

def main():
    for n in TEMP:
        os.system('rm -rf ' + n)
        print(n + " : deleted")
main()