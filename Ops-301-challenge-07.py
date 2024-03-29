#!/user/bin/env python3
# Geneva Knott - worked with Justin H, Sierra M & Nick A
# Python
#21 Mar 2023


import os
# Read user input

filename = input("Please enter the path to a directory: ")

# Get the absolute path of the chosen directory

root = os.path.abspath(filename)

# Get a list of subdirectories in the chosen directory

dirs = [os.path.join(filename, subdirectory) for subdirectory in os.listdir(filename) if os.path.isdir(os.path.join(filename, subdirectory))]

# Get a list of files in the chosen directory

files = [os.path.join(filename, file) for file in os.listdir(filename) if os.path.isfile(os.path.join(filename, file))]

#Array

array= (files, root, dirs)

# Function

def super(msg, com):
    print(msg + com)
    os.system(com)
    
# Loop through files and call the super function

for item in array:
    print(item)