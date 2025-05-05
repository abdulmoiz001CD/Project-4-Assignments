def print_multiple(message, number):
    for i in range(number):
        print(f"{message}")
        
def main():
    user_mess = input("Please type a message: ")
    num = int(input("Hello! Enter a number of times to repeat your message: "))
    print_multiple(user_mess, num)

if __name__ == '__main__':
    main()
