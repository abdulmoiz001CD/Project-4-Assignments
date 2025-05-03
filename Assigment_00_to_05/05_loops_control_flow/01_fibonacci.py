MAX = 10000

def main():
    a = 0
    b = 1

    while a < MAX:
        print(a, end=" ")
        next_term = a + b
        a = b
        b = next_term

if __name__ == "__main__":
    main()
