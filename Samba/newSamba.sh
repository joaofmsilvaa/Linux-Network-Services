#!/bin/bash
clear

read -p "Insert a name for the new user:" user

mkdir /samba/$user
useradd -M -d /samba/users -s /usr/sbin/nologin -G sambashare $user


echo "Insert a password for the new user"
smbpasswd -a $user
smbpasswd -e $user


chown $user:sambashare /samba/users
chmod 2770 /samba/users

echo "[users]
    path = /samba/users
    browseable = yes
    readable = yes
    public = yes
    read only = no
    force create mode = 0660
    force directory mode = 2770
    valid users = @sambashare @$adm

[$user]
    path = /samba/$user
    browseable = yes
    public = yes
    readable = yes
    read only = no
    force create mode = 0660
    force directory mode = 2770
    valid users = @$user @admin" >> /etc/samba/smb.conf

systemctl restart smb.service
systemctl restart nmb.service
