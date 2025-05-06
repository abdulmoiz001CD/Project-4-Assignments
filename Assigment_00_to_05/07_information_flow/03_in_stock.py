def num_in_stock(fruit: str) -> int:
    fruits_stock = {
        "apple": 17,
        "banana": 9,
        "orange": 12,
        "strawberry": 56,
        "pear": 1000  
    }
    return fruits_stock.get(fruit.lower(), 0)


def main():
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)

    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")


if __name__ == "__main__":
    main()
