import os


logfile = open("/etc/samba/smb.conf", "rt")
loglist = logfile.read()

os.system('python3 ~/files/listsamba.py')


user = input("Insert the name of the user you want to enable the file sharing:")

user = str(user)


enabled = """["""+user+"""]
    path = /samba/"""+user+"""
    browseable = yes
    public = yes
    readable = yes
    read only = no
    force create mode = 0660
    force directory mode = 2770
    valid users = @"""+user+""" @admin"""

userfile = "/samba/"+user+ ""

usertxt = """
#OFF_["""+user+ """]
    path = /samba/"""+user+"""
    browseable = no
    public = no
    read only = no
    force create mode = 0660
    valid users = @"""+user+ """ @admin"""
    

if str(usertxt) in loglist:
    loglist = loglist.replace(str(usertxt), str(str(enabled)))
    print("The file sharing from the user "+user+" was enabled ")

else:
    print("Not found")

logfile.close()
	

logfile = open("/etc/samba/smb.conf", "wt")

logfile.write(loglist)

logfile.close()


os.system('systemctl restart nmb.service')
os.system('systemctl restart smb.service')

