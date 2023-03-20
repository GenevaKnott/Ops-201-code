#!/user/bin/env python3
# Geneva Knott - worked with Justin H, Sierra M & Nick A
# Python
#20 Mar 2023

# https://www.geeksforgeeks.org/os-module-python-examples/

# main

#print the current working directory

print("Current working directory")

#Import os module

import os

# Execute bash commands

Oliver= os.system("ls")
Haku= os.system("whoami")
Donovan= os.system("lshw -short")

# Use Print 3x

print (Oliver, Haku, Donovan)
print ("this is my last print")

#end