import dirbpy
import ipaddress
import os
import re

def runTerminal(command,name):
    os.system("gnome-terminal --tab -e 'bash -c \"" + command+" > "+name+"\"'")

testName = input("Enter the name of the current test: ")

URL = input("Enter the URL: ")
print ("Current test: " + testName + " using host: "+ URL) 



#Web Content Scanner
print ("Running Dirb...")
dirbCommand = " dirb "+str(URL)
runTerminal(dirbCommand,testName+"Dirb.txt")