import os
import re
import subprocess as sp

# Zone creation


zoneName = input("Insert a url for your website: ")

zone_file = open('/etc/named.conf', 'a')
zone_file.write('\nzone \"'+zoneName + '\" IN {\n        type master;\n        file "/var/named/'+zoneName+'.hosts";\n};')

zone_file.close()


# Zone creation


# ip 
os.system('touch ip.txt')
os.remove ('ip.txt')
os.system('touch ip.txt')
os.system('hostname -I >> ip.txt')
os.system('clear')

file = open('ip.txt', 'r')
leitor = file.readlines()

userIP = str(leitor)
userIP = userIP.replace("\"", "")
userIP = userIP.replace("[", "")
userIP = userIP.replace("]", "")
userIP = userIP.replace("'", "")
userIP = userIP.replace("\\n", "")
userIP = userIP.replace(" ", "")

# ip 



# Zone configuration



host = sp.getoutput('hostname')
os.system('touch /var/named/'+zoneName+'.hosts')



zoneConfig = open ('/var/named/'+zoneName+'.hosts', 'w')

zoneConfig.write ('$ttl 38400\n')
zoneConfig.write ('@ IN SOA '+ host +'. mail.'+ zoneName +' (\n')
zoneConfig.write ('			1165190726 ;serial\n')
zoneConfig.write ('			10800 ;refresh\n')
zoneConfig.write ('			3600 ; retry\n')
zoneConfig.write ('			604800 ; expire\n')
zoneConfig.write ('			38400 ; minimum\n')
zoneConfig.write ('			)\n')
zoneConfig.write ('	IN	NS	'+host+'.\n')
zoneConfig.write ('	IN	A	'+userIP+'\n')
zoneConfig.write ('www	IN	A	'+userIP+'\n')
zoneConfig.write ('ftp	IN	A	'+userIP+'\n')
zoneConfig.close()

# Zone configuration 



# Virtualhost configuration

virtualConfig = open('/etc/httpd/conf/httpd.conf', 'a')

virtualConfig.write('NameVirtualHost '+userIP+':80\n')
virtualConfig.write('<VirtualHost '+userIP+':80>\n')
virtualConfig.write('	DocumentRoot "/home/'+zoneName+'/"\n')
virtualConfig.write('	ServerName '+zoneName+'\n')
virtualConfig.write('	ServerAlias '+zoneName+'\n')
virtualConfig.write('<Directory "/home/'+zoneName+'">\n')
virtualConfig.write('	Options Indexes FollowSymLinks\n')
virtualConfig.write('	AllowOverride All\n')
virtualConfig.write('	Order allow,deny\n')
virtualConfig.write('	Allow from all\n')
virtualConfig.write('	Require method GET POST OPTIONS\n')
virtualConfig.write('</Directory>\n')
virtualConfig.write('</VirtualHost>\n')
virtualConfig.close()

# Virtualhost configuration


# HTML configuration

os.system('mkdir /home/'+zoneName+'')
os.system('touch /home/'+zoneName+'/index.html')

htmlConfig = open('/home/'+zoneName+'/index.html', 'w')

htmlConfig.write('<h1> Bem-vindo ao '+zoneName+'</h1>')
htmlConfig.close()

# HTML configuration


# starting / restarting named and httpd


os.system('systemctl enable named')
os.system('systemctl start named')
os.system('systemctl restart named')

os.system('systemctl enable httpd')
os.system('systemctl start httpd')
os.system('systemctl restart httpd')
print("O seu site está pronto")
print("Acess your website following domains:\n"+zoneName+"\nwww."+zoneName+"\nftp."+zoneName+"")



# starting / restarting named and httpd

os.system('touch ip.txt')    
os.remove('ip.txt')                            
