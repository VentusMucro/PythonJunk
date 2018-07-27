import random


end_flag = False

number = 0

def randomize():
	return random.randint(1,10)

number = randomize()

while end_flag == False:
	guess = input("Pick a number between 1 and 10: ")

	if guess: #Confirm that a valid guess was made
		guess = int(guess)
		if guess > 10 or guess < 1:
			continue

	if guess > number:
		print("Too high, try again.")
	elif guess < number:
		print("Too low, try again.")
	else:
		print("Correct! You win.")
		choice = input("Do you want to play again? y/n: ")
		if choice[0].lower() == 'y':
			number = randomize()
		else:
			print("Thanks for playing. Bye.")
			end_flag = True 