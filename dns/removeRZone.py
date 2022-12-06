import os


logfile = open("/etc/named.conf", "rt")
loglist = logfile.read()

os.system('python3 ~/files/listzones.py')

zoneName = input("Insert the ip of the zone that you want to remove:")
print(zoneName)


zoneName = str(zoneName)

zoneFile = "/var/named/"+zoneName+".in-addr.arpa.hosts"


zonetxt = """zone \""""+zoneName+""".in-addr.arpa\" IN {
        type master;
        file \""""+zoneFile+"""\";
};"""

print(zonetxt)
nWanted = "zone \""+zoneName+".in-addr.arpa\" IN {"


if str(nWanted) in loglist:
	loglist = loglist.replace(str(zonetxt), ' ')
	os.remove(zoneFile)
	os.system('clear')
	print("Zone removed successfully")
	
	
if not loglist:
        print("Not found")

logfile.close()
	

logfile = open("/etc/named.conf", "wt")

logfile.write(loglist)

logfile.close()


os.system('systemctl restart named')
