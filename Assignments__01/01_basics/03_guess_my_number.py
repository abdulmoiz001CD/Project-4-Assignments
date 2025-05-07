import random
def guess_num():
   random_num = random.randint(0,100)
   print("I am thinking a number between 0 to 100")
   user_num = int(input("Please Guess The Number"))

   while random_num != user_num:
        if user_num < random_num:
         print("Your guess is too low")
        else:
         print("Your guess is too High")
         print("")
         user_num = int(input("Please Guess The Number"))
   print(f"Congrats! The number was: {random_num}")
     
         
guess_num()
           
      