def get_values():
    FIRST_NAME = input("Enter Your First Name: ")
    LAST_NAME =  input("Enter Your Last Name: ")
    EMAIL =   input("Enter Your Email: ")
    return FIRST_NAME, LAST_NAME , EMAIL

def main():
    user_data = get_values()
    print(f"Recieved user data: {user_data}")

if __name__ == "__main__":
    main()