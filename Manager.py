#   Created by: Maxim Keda
#
#   // Manage.py
#
import argparse
import Pack
import Install

version = "0"
date = '0'
buildAuthor = '(unofficial build)'
block = False

class varl:
    block = False
    @staticmethod
    def __init__(self, i):
        self.block = i

mk = varl

mk(mk, False)

def startArg(): #main manager argparse func
    parser = argparse.ArgumentParser(description="Table app for cross-platform installing apps")
    parser.add_argument('-a', "--author", action='store_true', help="print a build author")
    parser.add_argument('-t', "--time", action='store_true', help='print a build time')
    parser.add_argument("-v", "--version", action="store_true", help='print a version build = {day:month:year:type(debug or release)}')
    parser.add_argument("-p" , '--pack', type=str, help="pack a package", action='store')
    parser.add_argument("-i", "--install", type=str, help="install the package", action='store')
    parser.add_argument('-n', '--no_remove_temp', action='store_true')
    args = parser.parse_args()

    if args.version: # if -v
        print('Table version: ' + version + "\nBuilded at: " + date + '\nBuild Author : ' + buildAuthor)
    elif args.author: # if -a
        print('Build Author : ' + buildAuthor)
    elif args.time: # if -t
        print("Builded at: " + date)
    else: # if command -v -t -a not started
        if args.install != None and mk.block == False: # if -i
            print('start package: ' + str(args.install)) # log
            Install.Install(str(args.install), str(args.install)) # started Install.Install(name, dir) func
            mk.block = True # block func pack
        elif args.pack != None and mk.block == False: # if -p
            print('pack a package: ' + args.pack) # log
            Pack.Pack(str(args.pack), str(args.pack)) # started Pack.Pack(name, dir) func
            mk.block = True # block func install
        if args.no_remove_temp:
            print('This not work wait to new update') # empty func
        else:
            if mk.block == False:
                parser.print_help() # print help if is empty




