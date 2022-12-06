import os 

os.system('clear')
print("---------------------------------------------------------------------------------------------------")
print("""                                            SAMBA

                                What do you want to configure?\n
                                [1] Add a user
                                [2] Remove a user
				[3] Disable the file sharing for a user
				[4] Enable the file sharing for a user
                                [5] Go back to the main menu\n""")
print("---------------------------------------------------------------------------------------------------")


escolha = input("Insira a opção desejada: ")
if escolha == "1":
	os.system('./files/newSamba.sh')
if escolha == "2":
	os.system('python3 files/removeSamba.py')
	print("The user was successfully removed")
if escolha == "3":
	os.system('python3 files/disableSamba.py')
if escolha == "4":
        os.system('python3 files/enableSamba.py')
if escolha == "5":
	os.system('python3 script.py')


