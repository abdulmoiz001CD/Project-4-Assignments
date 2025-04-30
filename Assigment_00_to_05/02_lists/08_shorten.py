# def get_list_from_user():
#     items = []
#     user_input = input("Enter a value: ")
#     while user_input != "":
#         items.append(user_input)
#         user_input = input("Enter a value: ")
#     return items

MAX_LENGTH = 3
Items = ["pop", "loin", "lemon", "mom", "kite"]

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_element = lst.pop()
        print(f"Removed: {last_element}")

def main():
    shorten(Items)
    print(f"Final list: {Items}")

if __name__ == '__main__':
    main()
