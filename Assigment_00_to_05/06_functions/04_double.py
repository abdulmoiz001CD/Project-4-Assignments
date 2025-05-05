def double_num(num):
    return num * 2

def main():
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        doubled = double_num(number)
        print(f"The double of {user_input} is {doubled}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
