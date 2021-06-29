#   Created by: Maxim Keda
#
#   // main file
#
import Manager
import time


t = time.localtime() # get a time
Manager.buildAuthor = "Maxim Keda(official)" # build author ( if you changed a build please edit this variable and set unofficial )
Manager.date = time.strftime("Date : [%d/%m/%Y] Time : [%H:%M:%S]") # set a date of build
current_time = time.strftime("%d%m%Y", t) # set a version
dtype = "debug" # build version {debug or release}
Manager.version = current_time + dtype # set a version
Manager.startArg() # start a main ArgParser and Manager
