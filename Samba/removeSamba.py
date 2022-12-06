import os


logfile = open("/etc/samba/smb.conf", "rt")
loglist = logfile.read()

os.system('python3 ~/files/listsamba.py')


print("Make sure the samba service is already disabled for the user that you want to  remove")
user = input("Insert the name of the user that you want to remove:")


user = str(user)

usertxt = """#OFF_["""+user+ """]
    path = /samba/"""+user+"""
    browseable = no
    public = no
    read only = no
    force create mode = 0660
    valid users = @"""+user+ """ @admin"""

userfile = "/samba/"+user+ ""


if str(usertxt) in loglist:
	loglist = loglist.replace(str(usertxt), ' ')
	os.rmdir(userfile)
	os.system('clear')
	print("User removed successfully")
	
if not loglist:
        print("Not found")

logfile.close()
	

logfile = open("/etc/samba/smb.conf", "wt")

logfile.write(loglist)

logfile.close()


os.system('systemctl restart nmb.service')
os.system('systemctl restart smb.service')
