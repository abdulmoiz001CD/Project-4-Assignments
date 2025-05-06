def greet(name:str): 
   print(f"Greetings {name}!")
    
def main():
    user_name = input("How old is this person?: ")
    greet(user_name)

if __name__ == "__main__":
    main()
