import os
import subprocess as sp

zone_file = open("/etc/named.conf", "rt")
zonelist = zone_file.read()



zoneIP = input("Insert an ip for your zones domain: ")

octetos = zoneIP.split(".")

oct1 = octetos[0]
oct2 = octetos[1]
oct3 = octetos[2]
oct4 = octetos[3]


ip = ("\""  + str(oct3) + "." + str(oct2) +"."+ str(oct1) +".in-addr.arpa\"")

ipFile = (str(oct3)  + "."  + str(oct2)  + "." + str(oct1)  + "."  + "in-addr.arpa.hosts")

ipZoneLine =  ("zone \"" + str(oct3)  + "."  + str(oct2)  + "." + str(oct1)  + "."  + "in-addr.arpa\" IN {")
#print(ipZoneLine)

#zone_file.write('\nzone '+ip+' IN {\n        type master;\n        file "/var/named/'+ipFile+'";\n};')

if str(ipZoneLine) not in zonelist:


        zonefile = open('/etc/named.conf', 'a')

        zonefile.write('\nzone '+ip+' IN {\n        type master;\n        file "/var/named/'+ipFile+'";\n};')

        zonefile.close()

        domName = input("Insert a domain name: ")
        host = sp.getoutput('hostname')
        os.system('touch /var/named/'+ipFile+'')

        oct4www = int(oct4)

        oct4ftp = oct4www + 1

        oct4www = str(oct4www)
        oct4ftp = str(oct4ftp)


        host = sp.getoutput('hostname')
        os.system('touch /var/named/'+ipFile+'')

        zone_file.close()

        zoneConfig = open ('/var/named/'+ipFile+'', 'wt')

        zoneConfig.write ('$ttl 38400\n')
        zoneConfig.write ('@ IN SOA '+ host +'. mail.'+ domName +'.pt (\n')
        zoneConfig.write ('                     1165190726 ;serial\n')
        zoneConfig.write ('                     10800 ;refresh\n')
        zoneConfig.write ('                     3600 ; retry\n')
        zoneConfig.write ('                     604800 ; expire\n')
        zoneConfig.write ('                     38400 ; minimum\n')
        zoneConfig.write ('                     )\n')
        zoneConfig.write ('     IN      NS      '+ host +'.\n')
        zoneConfig.write (''+oct4www+'  IN      PTR     www.'+domName+'.pt.\n')
        zoneConfig.write (''+oct4ftp+'  IN      PTR     ftp.'+domName+'.pt.\n')
        zoneConfig.close()

        ipwww = oct1 + "." + oct2 + "." + oct3 + "." + oct4www
        ipftp = oct1 + "." + oct2 + "." + oct3 + "." + oct4ftp
        
        os.system('clear')
        print("Your domains are:\nwww."+domName+".pt - "+ipwww+"\nftp."+domName+".pt - "+ipftp+"")

        zoneConfig.close()

if str(ipZoneLine) in zonelist:
        zoneConfig = open('/var/named/'+ipFile+'','r')
		
        zonelines = zoneConfig.readlines()
	
        zoneConfig.close()	

        domName = input("Insert a domain name: ")

        oct4www = int(oct4)

        oct4ftp = oct4www + 1

        oct4www = str(oct4www)
        oct4ftp = str(oct4ftp)

        zoneConfig = open('/var/named/'+ipFile+'', 'a')
	
        zoneConfig.write(''+oct4www+'	IN	PTR	www.'+domName+'.pt.\n')
        zoneConfig.write(''+oct4ftp+'	IN	PTR	ftp.'+domName+'.pt.\n')	
	
        ipwww = oct1 + "." + oct2 + "." + oct3 + "." + oct4www
        ipftp = oct1 + "." + oct2 + "." + oct3 + "." + oct4ftp

        os.system('clear')
        print("Your domains are:\nwww."+domName+".pt - "+ipwww+"\nftp."+domName+".pt - "+ipftp+"")

        zoneConfig.close()
