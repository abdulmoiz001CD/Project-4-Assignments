def main():
  divided:float = float(input("Enter the numer you want to divided: "))
  divided_by:float = float(input("Enter the numer you want to divided by: "))
  quotient = divided // divided_by
  reminder = divided %  divided_by
 
  print(f"The result of this division is {int(quotient)} with a remainder of {int(reminder)}")


if __name__ == '__main__':
    main()