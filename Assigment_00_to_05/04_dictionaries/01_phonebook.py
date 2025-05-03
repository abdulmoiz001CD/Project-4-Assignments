def get_num_name(): 
    phone_book = {}
    while True:
        user_input = input("Enter a name (or press Enter to finish): ")
        if user_input == "":
            break
        user_input_num = input("Enter the number: ")
        phone_book[user_input] = user_input_num
    return phone_book

def print_phonebook(phone_book):
    for name in phone_book:
        print(f"{name} = {phone_book[name]}")

def lookup(phone_book):
    while True:
        user_input = input("Enter the name to look up (or press Enter to quit): ")
        if user_input == "":
            break
        if user_input not in phone_book:
            print("No number found.")
        else:
            print(f"{user_input} : {phone_book[user_input]}")

def main():
    number_name = get_num_name()
    print_phonebook(number_name)
    lookup(number_name)

if __name__ == "__main__":
    main()



