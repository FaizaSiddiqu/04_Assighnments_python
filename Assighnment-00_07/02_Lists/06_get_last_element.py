def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    print("Last element in the list is:", lst[-1])  # More readable


def get_lst():
    """
    Prompts the user to enter one element of the list at a time 
    and returns the resulting list.
    """
    lst = []
    while True:
        elem = input("Enter a list element (or press Enter to finish): ")
        if elem == "":
            break
        lst.append(elem)
    return lst


def main():
    lst = get_lst()
    if lst:  # extra safety check, though list is guaranteed to be non-empty
        get_last_element(lst)


if __name__ == '__main__':
    main()
