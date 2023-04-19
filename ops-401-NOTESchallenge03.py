#!/usr/bin/python3
#Geneva Knott

#Import libraries

import smtplib
import datetime, time, os
from getpass import getpass

#declare variables
up = "Network is active"
down = "Network in down"
last = 0
ping_result = 0
email = input("please provide your email")
password = getpass("please provide your password")

#Declare functions
#Function to handle the up alert
def send_upAlert():
    #gather a time stamp
    
    #SMTP seesison and send email
    
#fuction to hadle the down alert
def send_downAlert():
    
#Function that does the ping test
def ping_test():
    if ((ping_result != last) and (ping_result == up)):
        last=up
        send_upAlert()
    elif ((ping_result != last) and (ping_result == down)):
        send_downAlert()
        last=down
        
    
#Ask the user for an email address and password to use for sending notifications
#Send an email to the administator if a host 
#Clearly indicate in the message which host status changed, the status before and after, and a timestamp




# Prompt the user for a password
password = getpass.getpass("Enter your password: ")

# Test the email fucntionality
password = getpass("please provide your password")
#create the SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)  

#start TLS for secuirty
s.starttls()

#authentication
s.login("knottgeneva@gmail.com", password)

#message to be sent
s.sendmail("knottgeneva@gmail.com", email, "your server is on fire")

#Terminate the session

# Use the password in your email code
# Note: Do not store or print the password in plain text!
# Use appropriate encryption and security measures to protect the password.


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