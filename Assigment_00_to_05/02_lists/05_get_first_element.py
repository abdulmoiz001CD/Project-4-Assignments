def get_first_item():
    items =[]
    user_input:str = input("Enter the text or press enter to stop : ")
    while user_input != "":
        items.append(user_input)
        user_input:str = input("Enter the text or press enter to stop : ")

    return items



def first_item(items):
    print(f"The First Element of the list is {items[0]}")





def main():
   items = get_first_item()
   first_item(items)

if __name__ == '__main__':
    main()