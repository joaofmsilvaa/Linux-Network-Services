import os

#get file object
file1 = open("/etc/named.conf", "rt")



#read all lines
lines = file1.read()



#Variable to store the default setting
default53 = "        listen-on port 53 { 127.0.0.1;};"



#replace the default setting by the new one and store it in lines 
lines = lines.replace(str(default53), '        listen-on port 53 { 127.0.0.1;any;};') 

#close
file1.close()

#open and write the new lines
file1 = open("/etc/named.conf" , "wt")


file1.write(lines)

file1.close()





#add the querry setting

file1 = open("/etc/named.conf", "rt")

lines = file1.read()


defaultQuerry = "        allow-query     { localhost;};"


lines = lines.replace(str(defaultQuerry), '        allow-query     { localhost;any;};')



file1.close()



file1 = open("/etc/named.conf" , "wt")

file1.write(lines)

file1.close()
