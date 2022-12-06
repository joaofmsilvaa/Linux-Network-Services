import os
  
named = open("/etc/samba/smb.conf", "r")
  
lines = named.readlines()
 
print("Users list:") 
for line in lines:
          
        if "[" in line and "[users]" not in line and "[admin]" not in line and "[printers]" not in line and "[homes]" not in line and "[global]" not in line and "[print$]" not in line:

                x = line
                y = x.split()   
                print("\n" + y[0])
 
named.close()
  
