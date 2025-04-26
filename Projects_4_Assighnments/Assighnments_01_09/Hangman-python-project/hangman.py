print("\n Welcome to Hangman! \n")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses before you lose.")
print("Good luck!")

import random

words = ["python", "hangman", "challenge", "programming", "computer", "science"]
word = random.choice(words)
guessed_letters = []
attempts = 6

print("_" * len(word))

while attempts > 0:
    guess = input("\n guess the letter").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a one leter only")
        continue
    if guess in guessed_letters:
        print("this letter is already guessed choose another letter")
        continue
    guessed_letters.append(guess)
    
    if guess in word:
        print("Good Guess!")
    else:
        attempts -= 1
        print(f"Incorrect guess. You have {attempts} attempts left.")
        
    displayed_word =" ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)
    
    if "_" not in displayed_word:
        print(f"Congratulations! You've guessed the word '{word}'!")
        break
else:
    print(f"Game over! The word was {word}.")
    
# This is a simple hangman game where the player guesses letters in a word.
                  
    