import os



#Creates a file to store the value of the hostname -I value (userIP)
os.system('touch ip.txt')
os.remove ('ip.txt')
os.system('touch ip.txt')
os.system('hostname -I >> ip.txt')
os.system('clear')



file = open('ip.txt', 'r')

leitor = file.readlines()


#Edits the ip to fit in the normal format without extra characters
userIP = str(leitor)
userIP = userIP.replace("\"", "")
userIP = userIP.replace("[", "")
userIP = userIP.replace("]", "")
userIP = userIP.replace("'", "")
userIP = userIP.replace("\\n", "")
userIP = userIP.split('.')
userIP = userIP[0] + "." + userIP[1] + "." + userIP[2] + "." + "0"


print("---------------------------------------------------------------------------------------------------")
print("""                                             NFS

                                What do you want to configure?
                                [1] Share a folder
                                [2] Disable a folders sharing
				[3] Enable a folders sharing
				[4] Delete the folders sharing
                                [5] Go back to the main menu\n""")
print("---------------------------------------------------------------------------------------------------")



escolha = input("Enter your choice:")

if escolha == "1":

	pasta = input("Insert the path of the folder that you want to share: ")


#Appends the nfs txt into the exports file
	exportConfig = open ('/etc/exports', 'a')
	exportConfig.write (''+pasta+' '+userIP+'/24(rw,hide,sync)\n')
	exportConfig.close()

	os.system('systemctl restart nfs')
	os.system('systemctl start nfs')
	os.system('systemctl enable nfs') 
	os.system('clear')
	print("The folder \""+pasta+"\" was successfully mounted.")

if escolha == "2":
#Opens the file in a reading format and stores all of it in a variable
	file = open("/etc/exports", "rt")
	line = file.read()
	
	print("path / network ip / permissions")
	print("\n" + str(line))

	pasta = input("Insert the path of the folder that you want to disable the sharing:")

	pasta = str(pasta)

	exporttxt = "" + pasta + " " + userIP + "/24(rw,hide,sync)"
	exportdisable = "#" + pasta + " " + userIP + "/24(rw,hide,sync)"	


#Reads all the exports file and if there´s a line equal to the one said by the user, changes it to a commented version disabeling it 

	if str(exporttxt) in line:

#If there's a line equal to the normal export line its replaced by a commented one disabeling it
		line = line.replace(str(exporttxt), str(exportdisable))
		os.system('clear')
		print("The sharing of the folder "+pasta+" was successfully disabled.")

	if not line:
		print("Folder not found")

	file.close()
	file = open("/etc/exports", "wt")

#Writes the disabled line to the exports file
	file.write(line)
	file.close()
	

if escolha == "3":


	file = open("/etc/exports", "rt")
	line = file.read()

	print("\n" + str(line))

	pasta = input("Insert the path of the folder that you want to enable the sharing:")

	pasta = str(pasta)

	enabled = """"""+pasta+"""""" """ """ """"""+userIP+"""""""/24(rw,hide,sync)"""
	exporttxt = """#"""+pasta+"""""" """ """ """"""+userIP+"""""""/24(rw,hide,sync)"""


	if str(exporttxt) in line:
#if there's a disabled line equal to the one endicated by the user it is replaced by a enabled version
		line = line.replace(str(exporttxt), str(enabled))
		os.system('clear')
		print("The sharing of the folder "+pasta+" was successfully enabled.")

	if not line:
		print("Folder not found")

	file.close()
	file = open("/etc/exports", "wt")

#writes the updated version
	file.write(line)
	file.close()
	

if escolha == "4":
        file = open("/etc/exports", "rt")
        line = file.read()

        print("\n" + str(line))

        pasta = input("Insert the name of the folder that you want to remove the service from:")

        pasta = str(pasta)

        exporttxt = "" + pasta + " " + userIP + "/24(rw,hide,sync)"

        if str(exporttxt) in line:

#replaces the indicated line by nothing, deleting it
                line = line.replace(str(exporttxt), '')
                os.system('clear')
                print("The nfs service was stopped for the folder "+pasta+"")

        if not line:
                print("Folder not found")

        file.close()
        file = open("/etc/exports", "wt")

#writes the updated version
        file.write(line)
        file.close()
        


if escolha == "5":

	os.system('python3 script.py')


#Recreated the ip.txt file reseting it
os.system('touch ip.txt')
os.remove('ip.txt')	
