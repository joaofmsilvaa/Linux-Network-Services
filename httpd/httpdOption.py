import os

os.system('clear')


print("---------------------------------------------------------------------------------------------------")	
print("""                                           HTTP

                                What do you want to configure?
                                [1] Create a website
                                [2] Delete a website
                                [3] Go back to the main menu\n""")
print("---------------------------------------------------------------------------------------------------")
	
	
escolha = input("Enter your choice: ")
if escolha == "1":
	os.system('python3 ~/files/httpd.py')
if escolha == "2":
	os.system('python3 ~/files/removeNsite.py')
if escolha == "3":
	os.system('clear')
	os.system('python3 script.py')
