import os
import re
import subprocess as sp

# Zone creation


zoneName = input("Insert a name for the new zone: ")

zone_file = open('/etc/named.conf', 'a')
zone_file.write('\nzone \"'+zoneName + '\" IN {\n	type master;\n	file "/var/named/'+zoneName+'.hosts";\n};')

zone_file.close()


# Zone creation






# IP configuration
ipINPUT = input("Insert an ip address for your domain:")

inputToString = str(ipINPUT)

x = inputToString.split(".")

lOCT = x[3]

lOCTint = (int(lOCT))

wwwIPoct = (lOCTint + 1)
ftpIPoct = (wwwIPoct + 1)

wwwLast = str(wwwIPoct)
ftpLAST = str(ftpIPoct)

ipDOMAIN = x[0] + "." + x[1] + "." + x[2] + "." + x[3]

wwwIP = x[0] + "." + x[1] + "." + x[2] + "." + wwwLast

ftpIP = x[0] + "." + x[1] + "." + x[2] + "." + ftpLAST

# ip configuration



# Zone configuration

host = sp.getoutput('hostname')
os.system('touch /var/named/'+zoneName+'.hosts')

zoneConfig = open ('/var/named/'+zoneName+'.hosts', 'w')

zoneConfig.write ('$ttl 38400\n')
zoneConfig.write ('@ IN SOA '+ host +'. mail.'+ zoneName +'.pt (\n')
zoneConfig.write ('			1165190726 ;serial\n')
zoneConfig.write ('			10800 ;refresh\n')
zoneConfig.write ('			3600 ; retry\n')
zoneConfig.write ('			604800 ; expire\n')
zoneConfig.write ('			38400 ; minimum\n')
zoneConfig.write ('			)\n')
zoneConfig.write ('	IN	NS	'+ host +'.\n')
zoneConfig.write ('	IN	A	'+ipDOMAIN+'\n')
zoneConfig.write ('www	IN	A	'+wwwIP+'\n')
zoneConfig.write ('ftp	IN	A	'+ftpIP+'\n')
zoneConfig.close()

os.system('clear')
print("Your domains are:\n"+zoneName+" - "+ipDOMAIN+"\nwww."+zoneName+" - "+wwwIP+"\nftp."+zoneName+" - "+ftpIP+"")



# Zone configuration







# Starting / restarting the named service


os.system('systemctl enable named')
os.system('systemctl start named')
os.system('systemctl restart named')

print("The DNS service was successfully ")


# Starting / restarting the named service 


