def ask_order_user(fruit_prices):
    order_dic = {}
    for fruit in fruit_prices:
        user_input = input(f"How many ({fruit}) do you want?: ")
        quantity = int(user_input)
        order_dic[fruit] = quantity
    return order_dic

def calculate_total(order_dic, fruit_prices):
    total = 0
    for fruit in order_dic:
        total += order_dic[fruit] * fruit_prices[fruit]
    return total

def main():
    fruit_prices = {
        "apple": 10.5,
        "durian": 30,
        "jackfruit": 15,
        "kiwi": 12.5,
        "rambutan": 8,
        "mango": 7
    }

    orders = ask_order_user(fruit_prices)
    total_cost = calculate_total(orders, fruit_prices)
    print(f"Your total is ${total_cost}")

if __name__ == "__main__":
    main()


