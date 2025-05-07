def double_it(num):
    current_num = num
    while True:
        if current_num >= 100:
            break
        current_num *= 2
        print(current_num,end=" ")
    
def main():
    user_int = int(input("Enter your Number: "))
    double_it(user_int)


if __name__ == "__main__":
    main()



