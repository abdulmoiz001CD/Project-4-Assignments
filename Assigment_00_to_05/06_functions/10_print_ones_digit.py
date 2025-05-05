def print_ones_digit(num):
    ones = abs(num) % 10 
    print(f"The ones digit is {ones}")

def main():
    user_num = int(input("Enter a number: "))
    print_ones_digit(user_num)

if __name__ == '__main__':
    main()
