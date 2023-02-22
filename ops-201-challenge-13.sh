#!/bin/bash

# Script: Ops 201 Class 13 Ops Challenge Solution
# Author:Geneva Knott
# Date of latest revision:02/22/2023
# Purpose: #!/bin/bash

# [whois](https://www.howtogeek.com/680086/how-to-use-the-whois-command-on-linux/)

#Install whois on your Ubuntu VM.

#For this challenge you must use at least one variable and one function.
#Add to your bash script a sixth option that calls a function to:
#Take a user input string. Presumably the string is a domain name such as Google.com.
#Run whois against a user input string.
#Run dig against the user input string.
#Run host against the user input string.
#Run nslookup against the user input string.
#Output the results to a single .txt file and open it with your favorite text editor.

read -p "Enter website address" domain
# Define domain_info function
function domain_info() {
    echo "WHOIS information for $domain:"
    whois $domain
    echo ""
    echo "DNS information for $domain:"
    dig $domain
    echo ""
    echo "Host information for $domain:"
    host $domain
    echo ""
    echo "NSLOOKUP information for $domain:"
    nslookup $domain
    echo ""
}
domain_info > "/home/geneva/info.txt"