MINIMUM_HEIGHT = 50

def main():
    while True:
        user_input = input("How tall are you? ")

        # If the user enters nothing, stop the loop
        if user_input == "":
            break

        # Convert input to number
        height = int(user_input)

        # Check height
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()
