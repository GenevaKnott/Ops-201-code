#!/bin/bash

# Script: Ops 201 Class 05 Ops Challenge Solution
# Author:Geneva Knott
# Date of latest revision:02132023
# Purpose: Conditionals

#Create a script that detects if a file or directory exists, then creates it if it does not exist.
#Your script must use at least one array, one loop, and one conditional.


# I worked with Justin H and Sierra

# Main

paths=("./kenji" "./kai" "./donovan" "./sean")
for path in "${paths[@]}"; do
    if [ ! -e "$path/iexist.md" ]; then
    touch "$path/iexist.md"
     else
     echo "file_path already made"
fi
done


# End