################################
# COMPUTER ROCK PAPER SCISSORS #
################################
import random

RPS = ["rock", "paper", "scissors"]
end_flag = False

print("...Rock...")
print("...Paper...")
print("...Scissors...")

while end_flag == False:
	player1_choice = input("Player 1's Choice: ")
	if player1_choice:
		found_flag = False
		player1_choice = player1_choice.lower()
		for word in RPS:
			if player1_choice == word:
				found_flag = True
				break
		if found_flag == False:
			print("Please enter a valid choice.\n")
			continue

	player2_choice = random.randint(1,3)
	if player2_choice == 1:
		player2_choice = "rock"
	elif player2_choice == 2:
		player2_choice = "paper"
	else:
		player2_choice = "scissors"
	print(f"The computer chose: {player2_choice}")

	player2_choice = player2_choice.lower()

	if player1_choice == player2_choice:
		print("DRAW")
	elif player1_choice == "rock":
		if player2_choice == "scissors":
			print("Player 1 WINS!")
		elif player2_choice == "paper":
			print("Player 2 WINS!")
	elif player1_choice == "paper":
		if player2_choice == "rock":
			print("Player 1 WINS!")
		elif player2_choice == "scissors":
			print("Player 2 WINS!")
	elif player1_choice == "scissors":
		if player2_choice == "paper":
			print("Player 1 WINS!")
		elif player2_choice == "rock":
			print("Player 1 WINS!")
	else:
		print("Something went wrong.")

	continue_choice = input("\n\nWould you like to play again? ")
	if continue_choice[0].lower() == "y":
		continue
	else:
		end_flag = True