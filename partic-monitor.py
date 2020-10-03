#!/usr/bin/env python3
from timeMonitor import *
import sys

#assigning terminal arguments
importFile = sys.argv[1] #import file
masterFile = sys.argv[2] #master database file
flag = 'None'   ##FIX FLAG ASSGN LATER

if flag == '-t':
    pass
elif flag == '-r':
    pass
elif flag == 'i':
    pass

#START INPUT MONITOR FUNCTION

def allParticipation(importFile):
    #name and input dict
    chatContr = {}

    #reject inputs containing a greeting
    greetings = ['good morning', "morning", 'hi', 'hello', 'hey', 'thank you', 'bye', "have a good", "have a nice"]

    #reject inputs == an interjection
    interjections = ['oh', 'lol']

    #import chat log
    inputFile = open(importFile, 'r')

    #collecting data from chat log
    for line in inputFile.readlines():
        if line == '\n':
            continue                            #NEED TO TEST
        #parse name and input, returns list of strings
        spl1 = line.split(' ', 1)
            #spl1[0] = time
            #spl1[1] = "From (name) : (message)"
        spl2 = spl1[1].split(':', 1)
            #spl2[0] = "From (name)"
            #spl2[1] = message
        text = spl2[1]                          #All messages end in '\n'
        spl3 = spl2[0].split(' ', 1)
            #spl3[0] = "From"
            #spl3[1] = name
        name = spl3[1]

        #if student already participated at least once, no need to check again
        if name in chatContr and chatContr[name] >= 1:
            continue

        #if name does not already exist, add to dict
        if name not in chatContr:
            chatContr[name] = 0

        #check validity of input (to optimize, skip keys with value of 1)
        temp = [x for x in greetings if(x in text)]
        #if input valid,
        if bool(temp) == False:
            chatContr[name] = chatContr[name] + 1

    print(*chatContr.items(), sep='\n')                        #TESTING


def timeMonitor(importFile, start, end):
    #name and input dict
    chatContr = {}

    #import chat log
    inputFile = open(importFile, 'r')

    #collecting data from chat log
    for line in inputFile.readlines():
        if line == '\n':
            continue                            #NEED TO TEST
        #parse name and input, returns list of strings
        spl1 = line.split(' ', 1)
            #spl1[0] = time
            #spl1[1] = "From (name) : (message)"

        #skip out of bounds times
        #if spl[0] >                #START HERE

        spl2 = spl1[1].split(':', 1)
            #spl2[0] = "From (name)"
            #spl2[1] = message
        text = spl2[1]                          #All messages end in '\n'
        spl3 = spl2[0].split(' ', 1)
            #spl3[0] = "From"
            #spl3[1] = name
        name = spl3[1]

        #if student already participated at least once, no need to check again
        if name in chatContr and chatContr[name] >= 1:
            continue

        #if name does not already exist, add to dict
        if name not in chatContr:
            chatContr[name] = 0

        #check validity of input (to optimize, skip keys with value of 1)
        temp = [x for x in greetings if(x in text)]
        #if input valid,
        if bool(temp) == False:
            chatContr[name] = chatContr[name] + 1

    print(*chatContr.items(), sep='\n')                        #TESTING

#allParticipation(importFile)
timeMonitor(importFile, 0, 0)

#When adding to master list:
#- Increment total number of classes
#- Check if name is already in file
#- If name already exists, increment the count
#- Else (name does not exist), add the name and assign a value of 1
#- Final count at end of semester would be # of classes worthy of participation points
#- Student count/total number of classes = participation grade

#Potential algorithm:
#   1) write dictionary keys and values to a temporary file
#   2) run bash script to combine the temporary file and the masterFile?


#POTENTIAL CHANGES/ADDITIONS:
# 1) User input of how participation will be tracked
#       - 't' (2 args) = only records input between specified time stamps
#                        (actually 4 args with files)
#       - 'r' (3 args) = chat will be monitored for inappropriate language
#                       specified in given .txt file, reading from given
#                       chat log and outputting names and messages to
#                       provided file
#       - 'i' (2 args) = inspect the messages of a specific participant
