SENTENCE_START : str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    adjective: str = input("Enter an adjective: ")
    noun: str = input("Enter a noun: ")
    verb: str = input("Enter a verb: ")
    
    print(f"{SENTENCE_START} {adjective} {noun} and {verb}")

if __name__ == "__main__":
    main()