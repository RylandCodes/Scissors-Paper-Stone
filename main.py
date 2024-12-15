import random

options = ["rock","paper","scissors"]

running = True

score = 0

computer_score = 0

while running:
    player_choice = input("Enter your choice [rock/paper/scissors]").lower()

    if player_choice not in options:
        print("try again")
        continue

    computer_choice = random.choice(options)

    print(f"Computer Chose {computer_choice}")
    print(f"You Chose {player_choice}")

    print("Result:")

    if player_choice == computer_choice:
        print("TIEE")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("WIN")
        score += 1
    elif player_choice == "paper" and computer_choice == "rock":
        print("WIN")
        score += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("WIN")
        score += 1
    else:
        print("LOSE")
        computer_score += 1

    print(f"Computer has {computer_choice} points")
    print(f"Player has {score} points")

    q = input("Would you like to quit [y/n]").lower()

    if q == "y":
        break

print("Quitting")