#!/usr/bin/env python3
# Geneva Knott- worked with Justin H, Sierra & Nick A
# Python File Handling
#24Mar23


# main

import os

# Create a new file if it does not exist

f = open("testfile.txt", "w")

# Append three lines

f = open("testfile.txt", "a")
f.write("Today is 24March23 \n")
f.write("I have a three kids\n")
f.write("They are all boys")

# Print the first line

f = open("testfile.txt", "r")
print(f.read(1))

# Close a file when you're finished

f = open("testfile.txt", "r")
print(f.readline())

 #Delete the file

os.remove("testfile.txt")

# End