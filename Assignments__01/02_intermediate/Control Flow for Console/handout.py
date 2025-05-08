import random
SCORE = 0
def random_nums():
    user_num = random.randint(1,100)
    computer_num = random.randint(1,100)
    return user_num ,computer_num



def Higher_num(user_gues,generated_num):
      global SCORE
      _, sel_com_num = random_nums()
      if user_gues.lower() == "lower":
          if generated_num < sel_com_num:
               SCORE += 1
               print(f"You were right! The computer's number was {sel_com_num}")
               print(f"Your score is now {SCORE}")
          else:
               print(f"Aww, that's incorrect. The computer's number was {sel_com_num}")
               print(f"Your score is now {SCORE}")
     


def main():
     print(" ")
     print("Welcome to the High-Low Game!")
     print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
     for i in range(5):
        print(f"Round {i}")
        selected_num, computer_num = random_nums()
        print(f"Your number is {selected_num}")
        user_input = input("Do you think your number is higher or lower than the computer's?: ")
        Higher_num(user_input, computer_num)


if __name__ == "__main__":
     main()