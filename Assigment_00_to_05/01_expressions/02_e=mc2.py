c:int = 299792458

def main():
   while True:
       try:
          user_input = input("Enter Your mass in Kg (or q to quite): ")
          if  user_input.lower() == "q":
              print("Program excited: Goodbye")
              break
          mass:float = float(user_input)
          print(f" e = m * C^2 \n m = {mass} kg \n C = {c} m/s")
          e:float = mass * (c**2)
          print(f" The Ennergy is e = {e} joule")
       except ValueError:
           print("please enter a value number or q to quite")
       
           
       



if __name__ == '__main__':
    main()