# Problem Statement
# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):


def main():
    side1 = float(input("\033[1;3m Enter the length of side 1 : \033[0m"))
    side2 = float(input("\033[1;3m Enter the length of side 2 : \033[0m"))
    side3 = float(input("\033[1;3m Enter the length of side 3 : \033[0m"))
    
    print(f" \033[1;3m The perimeter of triangle is {side1 + side2 + side3} \033[0m")
    
if __name__ == "__main__":
    main()