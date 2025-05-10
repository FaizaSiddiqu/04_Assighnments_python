def main():
    user1 = int(input("Please enter an integer to be divided: "))
    user2 = int(input("Please enter an integer to divide by: "))

    result = user1 // user2
    remainder = user1 % user2

    print("The Result of the division is ", str(result), "with a remainder of ", str(remainder))

if __name__ == "__main__":
    main()

