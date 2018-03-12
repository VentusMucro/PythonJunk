continue_choice = None
end_flag = False
BUILD_PIN = 1717

pin_check = input("Enter PIN\n")
if int(pin_check) == BUILD_PIN:
	while end_flag != True:
		build_to_search = input("What build do you want?\n")
		if build_to_search == "exit":
			print("Goodbye.")
			end_flag = True
			continue
else:
	print("Incorrect PIN. Goodbye.")





#Section for functions
def ask_continue():
	continue_choice = input("Search for another?(y/n)\n")
	if continue_choice[0].lower == 'y':
		return False
	else:
		return True