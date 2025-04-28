def main():
    user_input: float = float(input("Enter the value in feet you want to convert to inches: "))
    feet_to_inches = user_input * 12
    print(f"{user_input} feet is equal to {feet_to_inches} inches.")

if __name__ == '__main__':
    main()
