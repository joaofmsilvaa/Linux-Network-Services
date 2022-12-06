#!/bin/bash
sudo chgrp sambashare2 /samba2

read -p "Insert a name for the new user:" user

mkdir /samba2/$user
useradd -M -d /samba2/$user -s /usr/sbin/nologin -G sambashare $user

chown $user:sambashare /samba2/$user
chmod 2770 /samba2/$user
echo "Insert a password for the new user:"
smbpasswd -a $user
smbpasswd -e $user
mkdir /samba2/users

useradd -M -d /samba2/users -s /usr/sbin/nologin -G samba2 admin
smbpasswd -e admin
smbpasswd -a admin

chown sadmin:sambashare /samba2/users
chmod 2770 /samba2/users

echo "[users]
    path = /samba2/users
    browseable = yes
    read only = no
    force create mode = 0660
    force directory mode = 2770
    valid users = @sambashare @admin

[$user]
    path = /samba2/$user
    browseable = no
    read only = no
    force create mode = 0660
    force directory mode = 2770
    valid users = @sambashare @admin" >> /etc/samba/smb.conf

systemctl restart smb.service
systemctl restart nmb.service
