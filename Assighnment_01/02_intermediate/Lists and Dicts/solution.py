#  Problem #1: List Practice
def main():
    # Create a list called `fruit_list`
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print("Length of the list:", len(fruit_list))

    # Add 'mango' at the end of the list
    fruit_list.append('mango')

    # Print the updated list
    print("Updated list:", fruit_list)

if __name__ == "__main__":
    main()

#  Problem #2: Index Game (with Menu Interaction)
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range!"

def slice_list(lst, start, end):
    if start < 0 or end > len(lst):
        return "Start or end index is out of range!"
    return lst[start:end]

def main():
    my_list = [10, "hello", 42, "python", 3.14]

    while True:
        print("\nYour list:", my_list)
        print("Choose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            index = int(input("Enter index to access: "))
            result = access_element(my_list, index)
            print("Result:", result)

        elif choice == "2":
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            # Try to convert to int or float if possible
            try:
                if '.' in new_value:
                    new_value = float(new_value)
                else:
                    new_value = int(new_value)
            except ValueError:
                pass  # Keep as string
            result = modify_element(my_list, index, new_value)
            print("Updated list:", result)

        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print("Sliced list:", result)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
