################################
BASIC ROCK PAPER SCISSORS
################################

print("...Rock...")
print("...Paper...")
print("...Scissors...")

player1_choice = input("Player 1's Choice: ")
player2_choice = input("Player 2's Choice: ")

print("SHOOT!")

player1_choice = player1_choice.lower()
player2_choice = player2_choice.lower()
if player1_choice != player2_choice:
	if player1_choice == "rock":
		if player2_choice == "scissors":
			print("Player 1 WINS!")
		elif player2_choice == "paper":
			print("Player 2 WINS!")
		else:
			print("Something went wrong.")
	elif player1_choice == "paper":
		if player2_choice == "rock":
			print("Player 1 WINS!")
		elif player2_choice == "scissors":
			print("Player 2 WINS!")
		else:
			print("Something went wrong.")
	elif player1_choice == "scissors":
		if player2_choice == "paper":
			print("Player 1 WINS!")
		elif player2_choice == "rock":
			print("Player 1 WINS!")
		else:
			print("Something went wrong.")
else:
	print("Draw")