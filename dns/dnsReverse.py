import os
import re
import subprocess as sp


# Select a mask

print("Options: /24  /16  /8")
mask = input("Insert a mask for your zone:")

# Select a mask



# Create a zone



if mask == "/24":
	os.system('python3 ~/files/dnsR24.py')

elif mask == "/16":
	os.system('python3 ~/files/dnsR16.py')

elif mask == "/8":
	os.system('python3 ~/files/dnsR8.py')



# start / restart the named service


os.system('systemctl enable named')
os.system('systemctl start named')
os.system('systemctl restart named')
print("\nServiço de DNS reiniciado")


# start / restart the named service


