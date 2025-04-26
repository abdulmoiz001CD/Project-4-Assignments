def main():
    ask_side1:float =float(input("Lenght of Triangle Side 1: "))
    ask_side2:float =float(input("Lenght of Triangle Side 2: "))
    ask_side3:float =float(input("Lenght of Triangle Side 3: "))
    perimeter =f'The perimeter of the triangle is {ask_side1+ ask_side2 + ask_side3:.2f}'
    print(perimeter)


if __name__ == "__main__":
    main()