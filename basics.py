import os
import re

# Services instalation


os.system('yum install named -y')
os.system('clear')

os.system('yum install httpd -y')
os.system('clear')

os.system('yum install nfs-utils -y')
os.system('clear')
os.system('yum install samba4 -y')
os.system('clear')
os.system('yum install samba samba-client')
os.system('sudo systemctl start smb.service')
os.system('sudo systemctl start nmb.service')
os.system('sudo systemctl enable smb.service')
os.system('sudo systemctl enable nmb.service')


# Disables the firewall


firewall = 'systemctl disable firewalld'
os.system(firewall)


firewall = 'systemctl stop firewalld'
os.system(firewall)


print("the firewall was successfully disabled")


# Disabled the firewall




# Desativar o Selinux


fileName = '/etc/selinux/config'

string = open(fileName).read()
new_str = re.sub('SELINUX=enforcing', 'SELINUX=disabled', string)
open (fileName,'w').write(new_str)

print ("Selinux desativado com sucesso")

# Desativar o Se linux

