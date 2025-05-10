import random

DONE_LIKELIHOOD = 0.3  # Adjust this value to increase/decrease randomness

def chaotic_counting():
    for i in range(1, 11):  # Counting from 1 to 10
        if done():
            return  # Stop counting early
        print(i)


def done():
    """Returns True with a probability of DONE_LIKELIHOOD."""
    return random.random() < DONE_LIKELIHOOD


def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")


if __name__ == '__main__':
    main()
