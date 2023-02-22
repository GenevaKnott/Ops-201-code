#!/bin/bash

# Script: Ops 201 Class 13 Ops Challenge Solution
# Author:Geneva Knott
# Date of latest revision:02/22/2023
# Purpose: #!/bin/bash

# I worked with Justin H and Sierra M-N-M

# [whois](https://www.howtogeek.com/680086/how-to-use-the-whois-command-on-linux/)

#Install whois on your Ubuntu VM.



read -p "enter website" domain
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
domain_info 