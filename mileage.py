MILES_CONSTANT = 0.621371
FOOT_CONSTANT = 3280.84
INCH_CONSTANT = 39370.1
YARD_CONSTANT = 1093.61
end_flag = False
output_data	= None
input_data = input("How many kilometers?\n") #First question to get starting kilometer data for conversion
while end_flag != True: #loop allowing for input until a conversion choice is valid
	convert_type = input("To what? Miles, Feet, Inches, Yards?\n") #user's choice of conversion
	if convert_type[0].lower() == 'm':
		output_data = round(float(input_data) * MILES_CONSTANT,2) #convert to miles and round
		print(f"{input_data} kilometers is {output_data} miles.")
		end_flag = True
	elif convert_type[0].lower() == 'f':
		output_data = round(float(input_data) * FOOT_CONSTANT,2) #conver to feet and round
		print(f"{input_data} kilometers is {output_data} feet.")
		end_flag = True
	elif convert_type[0].lower() == 'i':
		output_data = round(float(input_data) * INCH_CONSTANT,2) #convert to inches and round
		print(f"{input_data} kilometers is {output_data} inches.")
		end_flag = True
	elif convert_type[0].lower() == 'y':
		output_data = round(float(input_data) * YARD_CONSTANT,2) #convert to yards and round
		print(f"{input_data} kilometers is {output_data} yards.")
		end_flag = True
	else:
		wasted = input("That is not a valid choice.") #feedback for user
		continue #continue loop to prompt for another choice