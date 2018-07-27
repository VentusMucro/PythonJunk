for num in range(1,21):
	if num != 4 and num != 13:
		if num % 2 == 0:
			print(f"{num} is even.")
		else:
			print(f"{num} is odd.")
	else:
		print(f"{num} is unlucky!")