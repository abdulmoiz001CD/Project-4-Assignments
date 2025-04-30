def get_list_from_user():
    items = []
    user_input = input("Enter text (press Enter to stop): ")
    while user_input != "":
        items.append(user_input)
        user_input = input("Enter text (press Enter to stop): ")
    return items

def get_last_element(lst):
    print(f"The last element of the list is: {lst[-1]}")

def main():
    items = get_list_from_user()
    get_last_element(items)

if __name__ == '__main__':
    main()
