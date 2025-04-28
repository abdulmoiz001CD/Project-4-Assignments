import random

dice_num = 6

def roll_dice():
    die1 = random.randint(1,dice_num)
    die2 = random.randint(1,dice_num)
    total =f'Total of two Dice is {die1 + die2}'
    print(total)

def main():
    die1:int = 10
    print(f'die1 in main() is {die1}')
    roll_dice()
    roll_dice()
    roll_dice()
    print(f'die1 in main() is {die1}')


if __name__ == "__main__":
    main()