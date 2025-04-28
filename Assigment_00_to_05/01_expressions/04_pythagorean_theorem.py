import math

def main():
    first_side: float = float(input("Enter first perpendicular side of a right angle triangle: "))
    second_side: float = float(input("Enter second perpendicular side of a right angle triangle: "))
    print("Using Pythagoras Theorem...")
    
    third_side = math.sqrt(first_side**2 + second_side**2)
    
    print(f"The hypotenuse (third side) of the right angle triangle is {third_side}")

if __name__ == '__main__':
    main()
