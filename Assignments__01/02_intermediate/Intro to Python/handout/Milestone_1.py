def calculate_mars_weight(user_weight):
    MARS_PERCENT = 0.378 
    weight_on_mars = user_weight * MARS_PERCENT
    return round(weight_on_mars, 2)

def main():
    w = float(input("Enter a weight on Earth: "))
    result = calculate_mars_weight(w)
    print(f"The equivalent on Mars: {result}")

if __name__ == "__main__":
    main()
