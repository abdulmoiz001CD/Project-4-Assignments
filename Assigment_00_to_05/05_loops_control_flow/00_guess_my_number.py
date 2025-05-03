import random

def main():
    secret_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")
    print("Type 'skip' if you want to exit the game.")

    while True:
        user_input = input("Enter a guess (or type 'skip'): ")

        if user_input.lower() == "skip":
            print("You skipped the game. Goodbye!")
            break

        # Check if the input is a number
        if not user_input.isdigit():
            print("Please enter a valid number or 'skip'.")
            continue

        guess = int(user_input)

        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break

if __name__ == "__main__":
    main()
