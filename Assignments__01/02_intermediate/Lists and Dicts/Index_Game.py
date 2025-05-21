friut_list = ['apple', 'banana', 'orange', 'grape', 'pineapple',98,89]

def acces(item):
    user_input = int(input("Write a index num"))
    if user_input <= len(item):
        return  friut_list[item]
    else:
        print("sorry out of stock")
    
    return user_input

def modifying(item):
    user_index = acces(friut_list)
    
    user_item = input("Write a item you want to replace")
    if user_index in item:
        friut_list.insert(user_index,user_item)
        print(friut_list)
    else:
        print("sorry")

def main():
    modifying(friut_list)


if __name__ == "__main__":
    main()