def main():
    curr_val = int(input("Enter a number: "))
    
    while curr_val < 100:
        curr_val *= 2
        print(curr_val, end=" ")
        
if __name__ == "__main__":
    main()
    
# The code above is a simple program that doubles a number until it reaches 100.