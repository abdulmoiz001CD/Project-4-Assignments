def main():
    user_input = input("Tell me the year you want to check: ")
    given_year = int(user_input)

    if (given_year % 4 == 0 and given_year % 100 != 0) or (given_year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

if __name__ == "__main__":
    main()
