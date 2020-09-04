#!/usr/bin/env python3
import sys

importFile = sys.argv[1] = #import file
masterFile = sys.argv[2] = #master database file

#name and input dict
chatContr = {}

#import chat log
inputFile = open(importFile, 'r'):
    #for every entry
    for line in inputFile.readlines():
        #parse name and input, returns list of strings
        #maxSplit will be determined with test data
        line.split(' ', maxSplit)     #Change this based on sample data
            #name = line[#nameIndex]
            #input = line[#messageIndex]
        #if name does not already exist, add to dict
        if name not in chatContr:
            chatContr[name] = 0
        #check validity of input (to optimize, skip keys with value of 1)
        #if input valid,
            #if value != 1, set it to one

#iterate over dictionary
    #if value == 1:
        #participation point = 1
    #else:
        #participation point = 0

#write dictionary keys and values to a temporary file

#run bash script to combine the temporary file and the masterFile


main()
