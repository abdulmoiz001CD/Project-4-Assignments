def print_divisor(num):
    print(f"Divisors of {num} are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

def main():
    user_input = int(input("Enter a number: "))
    print_divisor(user_input)

if __name__ == '__main__':
    main()

