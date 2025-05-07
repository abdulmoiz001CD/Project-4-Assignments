def joke_bot(user_input): 
    PROMPT = "Joke"
    SORRY = "Sorry I only tell jokes"
    JOKE = ("Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. "
            "A programmer tells her: get a liter of milk, and if they have eggs, get 12. "
            "Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: "
            "'because they had eggs'")
    
    if user_input.lower() == PROMPT.lower():
        print(JOKE)
    else:
        print(SORRY)

def main():
    user_input = input("What do you want? ")
    joke_bot(user_input)

if __name__ == "__main__":
    main()
