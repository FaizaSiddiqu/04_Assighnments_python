#  Guess the number game python (user)

import random

print("Guess the Number game!")

# Generate random  number
number = random.randint(1, 100)

while True:
    guess = int(input("Enter a number between 1 and 100: "))
    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too High")
    else:
        print("Congratulations! You guessed it Right!")
        break
print("The number was: ", number)

        