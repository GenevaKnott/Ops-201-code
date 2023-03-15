#!/bin/bash
# Geneva Knott - worked with Justin H, Sierra & Nick A
# File permissions


#main

#Prompt user for Doc

read -p "Which Document would you like to edit permissions?" Directory

#Prompt user for Command code

read -p "Type the command code to change the permissons" Code

# Check File permissions

ls -l "$Directory"

# Change file permissions

chmod "$code" "$Directory"

echo "File permissions updated successfully"

# end


#[packt](https://subscription.packtpub.com/book/networking-and-servers/9781785286216/1/ch01lvl1sec17/working-with-permissions)
#[Linux Training academy](https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/)
