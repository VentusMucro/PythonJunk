import os
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
PATH_TO_PIN = os.path.expanduser('~\Documents\MHW_PIN.txt')
PATH_TO_BUILDS = os.path.expanduser('~\Documents\MHW_Builds.txt')
file = None
continue_choice = None
end_flag = False
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Functions
def get_pin(path):
	if os.path.isfile(path):
		file = open(path, 'r')
		to_return = file.read()
		file.close()
		return to_return
	else:
		file = open(path, 'w')
		new_pin = input("What would you like your PIN to be?\n")
		file.write(new_pin)
		file.close()
		return new_pin

def ask_continue():
	continue_choice = input("Search for another?(y/n)\n")
	if continue_choice[0].lower() == 'y':
		return False
	else:
		return True

def run_comparison(search_term): #For potential future use, hope to store build names to a file for looping and less code duplication
	file = open(PATH_TO_BUILDS,'r')
	data = file.readlines()
	found = False
	for line in data:
		values = line.split(";")
		if found == False:
			if search_term.lower() == values[0].lower():
				print("Build found: " + values[1])
				found = True
				file.close()
				global end_flag
				end_flag = ask_continue()
				break
	return found

def list_builds():
	file = open(PATH_TO_BUILDS, 'r')
	data = file.readlines()
	for line in data:
		values = line.split(";")
		print(values[0] + '\n')

def startup():
	if not os.path.isfile(PATH_TO_BUILDS):
		file = open(PATH_TO_BUILDS, 'w')
		file.write("")
		file.close()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Program
BUILD_PIN = int(get_pin(PATH_TO_PIN).strip())
startup()

pin_check = input("Enter PIN\n") #App secured by pin, pin is defined on first use
if int(pin_check) == BUILD_PIN: #Check pin
	while end_flag != True: #Begin program
		build_to_search = input("What build do you want?\n")
		if build_to_search == "exit": #Exit program
			print("Goodbye.")
			end_flag = True
			continue
		elif build_to_search == "list":
			list_builds()
			continue
		elif build_to_search == "add":
			string_to_commit = input("What would you like to name the build?\n")
			string_to_commit += ";" + input("What is the link to the build?\n")
			file = open(PATH_TO_BUILDS, 'a')
			file.write(string_to_commit + "\n")
			file.close()
		else:
			build_found = run_comparison(build_to_search)
			if build_found:
				if end_flag == True:
					print("Goodbye.")
				continue
			else:
				print("Build not found, try typing 'list'\n")
				continue
else:
	print("Incorrect PIN. Goodbye.")