#!/bin/bash

# Script: Ops 201 Class 05 Ops Challenge Solution
# Author:Geneva Knott
# Date of latest revision:02102023
# Purpose: Loops

# Write a script that displays running processes, asks the user for a PID, then kills the process with that PID.
# Use a loop in your script.

# I worked with Justin H and Sierra

# Main
last

while true; do
echo "ps -ef"
ps -ef
# Ask user for PID
read -p "Enter the PID of the process you want to kill" pid
#kill the process
kill -9 $pid 
# confirm the process was killed
# End