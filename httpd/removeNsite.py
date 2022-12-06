import os

#Creates a file to store the users ip
os.system('touch ip.txt')
os.remove ('ip.txt')
os.system('touch ip.txt')
os.system('hostname -I >> ip.txt')
os.system('clear')

file = open('ip.txt', 'r')
leitor = file.readlines()


#Edits the ip to fit in the normal format without extra characters
userIP = str(leitor)
userIP = userIP.replace("\"", "")
userIP = userIP.replace("[", "")
userIP = userIP.replace("]", "")
userIP = userIP.replace("'", "")
userIP = userIP.replace("\\n", "")
userIP = userIP.split('.')
userIP = userIP[0] + "." + userIP[1] + "." + userIP[2] + "." + "0"

logfile = open("/etc/named.conf", "rt")
loglist = logfile.read()

os.system('python3 ~/files/listzones.py')


zoneName = input("Insert the url of the website that you want to remove:")

zoneName = str(zoneName)

zoneFile = "/var/named/"+zoneName+".hosts"

zonetxt = """zone \""""+zoneName+"""\" IN {
        type master;
        file \""""+zoneFile+"""\";
};"""

nWanted = "zone \""+zoneName+"\" IN {"


if str(nWanted) in loglist:
	loglist = loglist.replace(str(zonetxt), ' ')
	os.remove(zoneFile)
	os.system('clear')
	print("Your website was removed")	
	
if not loglist:
        print("Not found")

logfile.close()
	

logfile = open("/etc/named.conf", "wt")

logfile.write(loglist)

logfile.close()

logfile = open("/etc/httpd/conf/httpd.conf", "rt")
loglist = logfile.read()


file.close()


sitetxt = """NameVirtualHost """+userIP+""":80
<VirtualHost """+userIP+ """>
        DocumentRoot \"/home/"""+zoneName+""".pt/\"
        ServerName """+zoneName+ """.pt
        ServerAlias """+zoneName+""".pt
<Directory \"/home/"""+zoneName+ """.pt\">
        Options Indexes FollowSymLinks
        AllowOverride All
        Order allow,deny
        Allow from all
        Require method GET POST OPTIONS
</Directory>
</VirtualHost>
"""

if str(sitetxt) in loglist:
	loglist = loglist.replace(str(sitetxt), ' ')

logfile = open("/etc/httpd/conf/httpd.conf", "wt")
logfile.write(loglist)
logfile.close()

os.system('touch ip.txt')
os.remove('ip.txt')

	

os.system('systemctl restart httpd')
os.system('systemctl restart named')
