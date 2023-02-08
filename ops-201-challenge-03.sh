#!/bin/bash

# Script: Ops 201 Class 02 Ops Challenge Solution
# Author:Geneva Knott
# Date of latest revision:02082023
# Purpose: Functions

+ Write a script that prints the login history of users on this computer.
+ Your script must use at least one function and one variable.

# Main
print_function () {
    cat /var/log/auth.log
}
print_functions
var_change () {
    local var1=local 1
}
# End