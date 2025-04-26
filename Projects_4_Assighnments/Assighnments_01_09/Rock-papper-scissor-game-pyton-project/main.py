
print(" \n Welcome to the Rock, Paper, Scissors game! \n")

import random

# choices
choices = ["rock", "paper", "scissors"]

# player choice
player_choice = input("Enter your choice(rock, paper, scissors):").lower()

# computer choice
computer_choice = random.choice(choices)

# winner decision
print(f"Player choice: {player_choice}")
print(f"Computer choice: {computer_choice}")

if player_choice == computer_choice:
    print("Its a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print(f"You win! {player_choice} beats {computer_choice}.")

elif player_choice == "paper" and computer_choice == "rock":
    print(f"Player wins! {player_choice} beats {computer_choice}.")

elif player_choice == "scissors" and computer_choice == "paper":
    print(f"Player wins! {player_choice} beats {computer_choice}.")

else:
    print(f"Computer choice Wins! {computer_choice} beats {player_choice}.")