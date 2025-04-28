import random 

number_side = 6

first_Dice = random.randint(1,number_side)
second_Dice = random.randint(1,number_side)

total:int = first_Dice + second_Dice

print(f"Total number of each side is {number_side}")
print(f"The first Side of dice is  {first_Dice}")
print(f"The Seocod Side of dice is  {second_Dice}")
print(f"The Sum of Two Dice is {total}")

