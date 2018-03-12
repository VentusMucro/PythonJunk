import os
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
PATH_TO_PIN = os.path.expanduser('~\Documents\MHW_PIN.txt')
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
		new_pin = input("What would you like your PIN to be?")
		file.write(new_pin)
		file.close()
		return new_pin
		
def run_comparison(search_term, comparator): #For potential future use, hope to store build names to a file for looping and less code duplication
	if search_term == comparator:
		print("")
		end_flag = ask_continue()
		#Need to finish this if/when file system is in place

def ask_continue():
	continue_choice = input("Search for another?(y/n)\n")
	if continue_choice[0].lower == 'y':
		return False
	else:
		return True
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Program
BUILD_PIN = int(get_pin(PATH_TO_PIN).strip())

pin_check = input("Enter PIN\n") #App secured by pin, pin is defined on first use
if int(pin_check) == BUILD_PIN: #Check pin
	while end_flag != True: #Begin program
		build_to_search = input("What build do you want?\n")
		if build_to_search == "exit": #Exit program
			print("Goodbye.")
			end_flag = True
			continue
else:
	print("Incorrect PIN. Goodbye.")