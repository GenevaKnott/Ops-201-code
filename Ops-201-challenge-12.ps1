# Geneva Knott 
# 21 Feb 2023
#Select-String 

# I worked with Justin H and Sierra M-N-M

#main

# Create a local file called network_report.txt that holds the contents of an ipconfig /all command.

ipconfig /all > C:\Users\Geneva\Documents\network_report.txt

# Use Select-String to search network_report.txt and return only the IP version 4 address.

function File_Network {
   $File = "C:\Users\Geneva\Documents\network_report.txt"
   Select-String -Path $File -Pattern "IPv4"
}
File_Network

# Remove the network_report.txt when you are finished searching it.

Remove-Item C:\Users\Geneva\Documents\network_report.txt
#end