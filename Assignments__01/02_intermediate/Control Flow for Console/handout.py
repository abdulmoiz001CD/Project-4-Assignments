import random


user_score = 0 
computer_score = 0

def generate_random_numbers():
    """Generates and returns a random number for user and computer."""
    user_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    return user_number, computer_number

def evaluate_guess(user_guess, computer_number, user_number):
    """Evaluates the user's guess and updates scores accordingly."""
    global user_score, computer_score

    user_guess = user_guess.lower()

    if user_guess not in ["higher", "lower"]:
        print("Invalid input! Please type 'higher' or 'lower'.")
        return

    print(f"The computer's number was {computer_number}.")

    if user_guess == "higher":
        if user_number > computer_number:
            user_score += 1
            print("You were right!")
        else:
            computer_score += 1
            print("Aww, that's incorrect.")
    elif user_guess == "lower":
        if user_number < computer_number:
            user_score += 1
            print("You were right!")
        else:
            computer_score += 1
            print("Aww, that's incorrect.")

    print(f"Your score: {user_score} | Computer's score: {computer_score}")
    print("-" * 40)

def display_final_result():
    """Displays the final winner after all rounds."""
    print("\nFinal Scores:")
    print(f"You: {user_score} | Computer: {computer_score}")

    if computer_score > user_score:
        print("Computer wins the match!")
    elif user_score > computer_score:
        print("You win the match!")
    else:
        print("The match is a tie!")

def main():
    print(" ")
    print("Welcome to the High-Low Game!")
    print("_" * 35)

    rounds = 5
    for round_number in range(1, rounds + 1):
        print(f"Round {round_number}")
        user_number, computer_number = generate_random_numbers()
        print(f"Your number is: {user_number}")
        guess = input("Do you think your number is higher or lower than the computer's? ").strip()
        evaluate_guess(guess, computer_number, user_number)

    display_final_result()

if __name__ == "__main__":
    main()
