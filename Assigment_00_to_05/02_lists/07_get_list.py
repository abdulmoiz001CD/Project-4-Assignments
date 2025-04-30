def get_list_from_user():
    items = []
    user_input = input("Enter a value: ")
    while user_input != "":
        items.append(user_input)
        user_input = input("Enter a value: ")
    return items

def print_list(lst):
    print(f"Here's the list: {lst}")

def main():
    items = get_list_from_user()
    print_list(items)

if __name__ == '__main__':
    main()
