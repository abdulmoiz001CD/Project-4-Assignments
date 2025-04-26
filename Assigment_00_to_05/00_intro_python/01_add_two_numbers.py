def main():
    first_num:str = input("Enter The First Number: ")
    convert_int1:int = int(first_num)
    second_num:str = input("Enter The First Number: ")
    convert_int2:int = int(second_num)
    total:int = f"The Total sum is {convert_int1 + convert_int2}"
    print(total)


if __name__ == '__main__':
    main()