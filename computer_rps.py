################################
# COMPUTER ROCK PAPER SCISSORS #
################################
import random

RPS = ["rock", "paper", "scissors"]
end_flag = False
p1score = 0
p2score = 0

player1_choice = ''
player2_choice = ''

def solve(choice):
	global p1score, p2score
	if player2_choice == choice:
		print("DRAW")
	elif choice == RPS[0] and player2_choice != RPS[1]:
		print("Player 1 WINS!")
		p1score += 1
	elif choice == RPS[1] and player2_choice != RPS[2]:
		print("Player 1 WINS!")
		p1score += 1
	elif choice == RPS[2] and player2_choice != RPS[0]:
		print("Player 1 WINS!")
		p1score += 1
	else:
		print("Player 2 WINS!")
		p2score += 1

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

	solve(player1_choice)
	# if player1_choice == player2_choice:
	# 	print("DRAW")
	# elif player1_choice == "rock":
	# 	if player2_choice == "scissors":
	# 		print("Player 1 WINS!")
	# 		p1score += 1
	# 	elif player2_choice == "paper":
	# 		print("Player 2 WINS!")
	# 		p2score += 1
	# elif player1_choice == "paper":
	# 	if player2_choice == "rock":
	# 		print("Player 1 WINS!")
	# 		p1score += 1
	# 	elif player2_choice == "scissors":
	# 		print("Player 2 WINS!")
	# 		p2score += 1
	# elif player1_choice == "scissors":
	# 	if player2_choice == "paper":
	# 		print("Player 1 WINS!")
	# 		p1score += 1
	# 	elif player2_choice == "rock":
	# 		print("Player 2 WINS!")
	# 		p2score += 1
	# else:
	# 	print("Something went wrong.")

	print(f"\n\n-Scores p1:[{p1score}] p2:[{p2score}]-")
	continue_choice = input("Would you like to play again? (y/n) ")
	if continue_choice[0].lower() == "y":
		continue
	else:
		end_flag = True