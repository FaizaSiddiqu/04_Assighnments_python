import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Generate a list of random numbers
    random_numbers: list[int] = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    # Print the list of random numbers
    print("Random numbers:", random_numbers)
    
    # Calculate the sum of the random numbers
    total: int = sum(random_numbers)
    
    # Print the sum
    print("Sum of random numbers:", total)
    
    # Calculate the average of the random numbers
    average: float = total / N_NUMBERS
    
    # Print the average
    print("Average of random numbers:", average)
   

if __name__ == '__main__':
    main()
