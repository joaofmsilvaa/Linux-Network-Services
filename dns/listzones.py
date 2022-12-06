import os
  
named = open("/etc/named.conf", "r")
  
lines = named.readlines()
 
print("Zone list:") 
for line in lines:
          
        if "zone \"" in line:
                x = line
                y = x.split( )
                print("\n" + y[1])
                
                  
named.close()
  
