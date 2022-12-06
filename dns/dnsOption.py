import os

os.system('clear')
print("---------------------------------------------------------------------------------------------------")
print("""                                     DNS

                             What do you want to configure?\n
                                [1] Normal DNS
                                [2] Reverse DNS
                                [3] Go back to the main menu\n""")
print("---------------------------------------------------------------------------------------------------")
escolha = input("Enter your choice: ")


#Enters in a second menu based on the users input in the variable "escolha"
if escolha == "1":
	os.system('clear')

	print("---------------------------------------------------------------------------------------------------")
	print("""                                      Normal DNS

                              What do you want to configure?\n
                                [1] Create a zone
                                [2] Delete a zone
                                [3] Go back to the main menu\n""")
	print("---------------------------------------------------------------------------------------------------")
	
	
	escolha1 = input("Enter your choice: ")


#Executes the needed script based on the users choice in the variable escolha
	if escolha1 == "1":
		os.system('python3 ~/files/dns.py')


	if escolha1 == "2":
		os.system('python3 ~/files/removeNZone.py')


	if escolha1 == "3":
#Executes the main script, going back to the main menu
		os.system('python3 script.py')
	
if escolha == "2":
	os.system('clear')
	
	print("---------------------------------------------------------------------------------------------------")
	print("""                                         Reverse DNS
                                What do you wish to configure?\n
                                [1] Create a reverse zone
                                [2] Delete a reverse zone
                                [3] Go back to the main menu\n""")
	print("---------------------------------------------------------------------------------------------------")
	
	escolha = input("Enter your choice: ")

	if escolha == "1":
        	os.system('python3 ~/files/dnsReverse.py')


	if escolha == "2":
        	os.system('python3 ~/files/removeRZone.py')


	if escolha == "3":
		os.system('clear')
		os.system('python3 script.py')
