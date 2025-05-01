import random

def main():
    values: list[int] = []

    for _ in range(10):
        value = random.randint(1, 100)
        values.append(value)

    # Print all numbers in one line, space-separated
    for num in values:
        print(num, end=" ")

if __name__ == "__main__":
    main()
