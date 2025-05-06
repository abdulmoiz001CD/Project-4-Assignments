def is_adult(age): 
    ADULT_AGE = 18
    if age >= ADULT_AGE:
        return True
    else:
        return False
    
def main():
    user_age = int(input("How old is this person?: "))
    print(is_adult(user_age)) 

if __name__ == "__main__":
    main()
