def count_even(lst):
    even_count = 0
    for i in lst:
        if i % 2 == 0:
            even_count += 1
    print(f"Total even numbers: {even_count}")


def get_even_lst():
    lst = []
    user_input = input("Enter a number or press Enter to finish: ")
    while user_input != "":
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Please enter a valid number.")
        user_input = input("Enter a number or press Enter to finish: ")
    return lst


def main():
    even_lst = get_even_lst()
    count_even(even_lst)


if __name__ == "__main__":
    main()
