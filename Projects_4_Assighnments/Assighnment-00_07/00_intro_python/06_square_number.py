# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

def main():
    num = float(input("\033[1;3m Type a number to see its square : \033[0m"))   
    print(str(num) + " square is " + str(num ** 2)) 

if __name__ == '__main__':
    main()