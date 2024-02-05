import time
import sys

runtime = 1
with open("log.txt", "a") as file:
    while(runtime == 1):
        itemForLog = input("] ")
        if itemForLog == ("exit"):
            file.close()
            sys.exit()
        else:
            seconds = time.time()
            localTime = time.ctime(seconds)
            logItem = localTime + " " + itemForLog + "\n"
            file.write(logItem)