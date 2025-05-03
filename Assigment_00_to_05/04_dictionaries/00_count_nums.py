def count_num(new_nums):
    user_dic = {}
    for num in new_nums:
        if num not in user_dic:
            user_dic[num] = 1
        else:
            user_dic[num] += 1
    return user_dic


def print_num(num_dic):
    for num in num_dic:
        print(f"{num} appears {num_dic[num]} times")


def main():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to stop): ")

        if user_input == "":
            break

        try:
            user_num = int(user_input)
            numbers.append(user_num)

            # Count and print updated results
            counts = count_num(numbers)
            print_num(counts)
            print("---")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
