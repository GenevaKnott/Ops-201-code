#!/usr/bin/python3
#Geneva Knott
#Import Libraries
#https://realpython.com/python-sleep/ , https://docs.python.org/3/library/datetime.html

# Perform a single ping
#import os

#target = "8.8.8.8"
#ping = os.system("ping -c 1 " + target)  
#print(ping)
#time.sleep(2)

#Infinite loops
#while True:
#    print("we are stuck here forever")
    
# get a timestamp
#currentTime = datetime.now()
#print(currentTime)

# Transmit a single ICMP (ping) packet to a specific IP every two seconds.
#Evaulate the response either success or failure
#Assign sucess or failure to a status variable
#For every ICMP tranmission attempted, print the status variable along with a comprehensive timestamp 

import os
import datetime
import time

target = "8.8.8.8"

def ping_Status(target):
    
  # Evaluate the response and assign success or failure to the status variable
    ping = os.system("ping -c 1 " + target)
    if ping == 0:
        status = "sucess"
        print(f"{target} is up!")
    else:
        status = "failure"
        print(f"{target} is down!")
    # Get the current timestamp and print the status and timestamp
    currenttime = datetime.datetime.now()
    print(f"{currenttime} - Status: {status}")
    return status
while True:
    # Transmit a single ICMP ping packet to the target
    ping_Status(target)
    # Wait for 2 seconds before transmitting another ping packet
    time.sleep(2)