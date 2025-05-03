def main():
    value_limit = 100
    user_input = int(input("Enter a number: "))
    num = user_input

    while num <= value_limit:
        print(num, end=" ")
        num *= 2 

if __name__ == "__main__":
    main()

