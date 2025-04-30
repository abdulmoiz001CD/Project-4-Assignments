def add_three_copies(user_input,data):
    for _ in range(3):
        data.append(user_input)

def main():
    user_input = input("Enter the text : ")
    data:list = []
    print("Before the list",data)
    add_three_copies(user_input,data)
    print("after the prompt: ", data)


if __name__ == "__main__":
    main()

    