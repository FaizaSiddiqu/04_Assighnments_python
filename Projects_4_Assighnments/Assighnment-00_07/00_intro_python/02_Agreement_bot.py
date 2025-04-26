# Write a program which asks the user what their favorite animal is, and then always 
# responds with "My favorite animal is also ___!" (the blank should be filled in with the
# user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space
# between the prompt and the user input!):

def main():
    user_input = input("\033[1;3m What is yuour favoriute animal___? \033[0m")
    print(f"My favorite animal is also {user_input}!")
    
if __name__ == "__main__":              # This line ensures that the main function is called only when the script is run directly, not when imported as a module.
    main()                               # This line calls the main function to execute the program.