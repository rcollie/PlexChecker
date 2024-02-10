# Written by Rob Collie
# Based on Plex Checker written by Gavin Fuller (https://gitlab.com/Flaming_Keyboard/plex-checker)
# This repository can be found at https://github.com/rcollie/PlexChecker/
# MIT License applies

# MIT License
# 
# Copyright (c) 2024 Rob Collie
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.




logging = True  # If you would like the script to log events to a file. Default is True.
computer = "192.168.x.x:32400"  # IP address of the Plex server to be monitored.
maxRetries = 4  # If it fails to connect, the script will retry this many times.
sleepRetries = 12  # If it fails to connect, the script wait this many seconds before retrying again.

import os
import time
import datetime
from platform import python_version

pyver = python_version()

if int(pyver[0]) < 3:
    import httplib
else:
    import http.client

def checkInternet():
    reply = False
    for x in range(maxRetries):
        if not reply:
            if logging:
                with open("log.txt", "a") as log_file:
                    log_file.write("\n" + (datetime.datetime.now().strftime("%b %d, %Y")) + " at " + (datetime.datetime.now().strftime("%I:%M:%S %p")) + " | testing connection to " + computer)
            
            conn = http.client.HTTPConnection(computer, timeout=5) if int(pyver[0]) >= 3 else httplib.HTTPConnection(computer, timeout=5)
            
            try:
                conn.request("HEAD", "/")
                reply = True
                if logging:
                    with open("log.txt", "a") as log_file:
                        log_file.write("\n" + (datetime.datetime.now().strftime("%b %d, %Y")) + " at " + (datetime.datetime.now().strftime("%I:%M:%S %p")) + " | reply is " + str(reply).lower())
            except:
                pass
            finally:
                conn.close()

            if logging and not reply:
                with open("log.txt", "a") as log_file:
                    log_file.write("\n" + (datetime.datetime.now().strftime("%b %d, %Y")) + " at " + (datetime.datetime.now().strftime("%I:%M:%S %p")) + " | failed to establish a connection, attempt " + str(x+1) + "/" + str(maxRetries))

            if sleepRetries > 0.0:
                time.sleep(sleepRetries)

    return reply

def killPlex():
    os.system("pkill -9 Plex")
    return True

def startPlex():
    os.system("open -a Plex\\ Media\\ Server")

def restartPlex():
    if logging:
        with open("log.txt", "a") as log_file:
            log_file.write("\n" + (datetime.datetime.now().strftime("%b %d, %Y")) + " at " + (datetime.datetime.now().strftime("%I:%M:%S %p")) + " | restarting plex process")
    killPlex()
    startPlex()
    if logging:
        restartLogger()

def restartLogger():
    with open("log.txt", "a") as log_file:
        log_file.write("\n" + (datetime.datetime.now().strftime("%b %d, %Y")) + " at " + (datetime.datetime.now().strftime("%I:%M:%S %p")) + " | restarted plex process")

def successLogger():
    with open("log.txt", "a") as log_file:
        log_file.write("\n" + (datetime.datetime.now().strftime("%b %d, %Y")) + " at " + (datetime.datetime.now().strftime("%I:%M:%S %p")) + " | successfully communicated with plex process")

def logStarter():
    try:
        open("log.txt").close()
    except IOError:
        with open("log.txt", "w+") as log_file:
            log_file.write("DATE & TIME                 | DETAILS\n===========================================================================\n")

def main():
    if not checkInternet():
        restartPlex()
    elif logging:
        successLogger()

if logging:
    logStarter()

while True:
    main()
    time.sleep(300)  # Checks status every 5 minutes.
