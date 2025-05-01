def main():
    # Define voting ages
    Peturksbouipo = 16
    Stanlau = 25
    Mayengua = 48

    # Ask user for age and convert to integer
    user_input = input("How old are you? ")
    age = int(user_input)

    # Check eligibility for Peturksbouipo
    if age >= Peturksbouipo:
        print(f"You can vote in Peturksbouipo where the voting age is {Peturksbouipo}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {Peturksbouipo}.")

    # Check eligibility for Stanlau
    if age >= Stanlau:
        print(f"You can vote in Stanlau where the voting age is {Stanlau}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {Stanlau}.")

    # Check eligibility for Mayengua
    if age >= Mayengua:
        print(f"You can vote in Mayengua where the voting age is {Mayengua}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {Mayengua}.")

if __name__ == "__main__":
    main()
