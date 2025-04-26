import random
import string

print(" \n Random Password Generated \n")

def generated_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# user input
length = int(input("Enter the lentgh of your desired password :"))

if length < 8:
    print("Password length should be at least 8 characters.")
else:
    password = generated_password(length)
    print("Your Desired Generated Password is : ", password)
