age = input("How old are you?\n")
if age:
	age = int(age)
	if age >= 18 and age < 21:
		print("You can enter with a wristband.")
	elif age >= 21:
		print("Go on in.")
	else:
		print("No entry.")
else:
	print("You didn't enter an age. FAIL!")