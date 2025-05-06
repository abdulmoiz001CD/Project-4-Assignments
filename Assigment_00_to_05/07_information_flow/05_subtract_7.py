def subtract_seven(num:int):
    return num - 7

def main():
    user_num = int(input("Enter you number: "))
    num = subtract_seven(user_num)
    print(f"The subtract number is {num}")

if __name__ == "__main__":
    main()
