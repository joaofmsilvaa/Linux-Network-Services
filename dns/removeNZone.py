import os


logfile = open("/etc/named.conf", "rt")
loglist = logfile.read()

os.system('python3 ~/files/listzones.py')


zoneName = input("Insert the name of the zone that you want to remove:")

zoneName = str(zoneName)

zoneFile = "/var/named/"+zoneName+".hosts"

zonetxt = """zone \""""+zoneName+"""\" IN {
	type master;
	file \""""+zoneFile+"""\";
};"""

nWanted = "zone \""+zoneName+"\" IN {"



if str(nWanted) in loglist:

#if there's a zone text block equal to the one defined by the user it is replaced by nothing
	loglist = loglist.replace(str(zonetxt), ' ')
	os.remove(zoneFile)
	os.system('clear')
	print("Zoned removed successfully")	
	
if not loglist:
        print("Not found")

logfile.close()
	

logfile = open("/etc/named.conf", "wt")

#Inserts the updated lines
logfile.write(loglist)

logfile.close()


os.system('systemctl restart named')
print("The zone was removed successfully")
