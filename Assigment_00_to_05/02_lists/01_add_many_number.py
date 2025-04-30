def add_many_numbers(numbers)-> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
     
    total_so_far:int = 0

    for num in numbers:
        total_so_far += num

    return total_so_far

def main():
    num:int=[1,2,3,4,5,6]
    sum_of_numbers = add_many_numbers(num)
    print(f"The total sum of numbers is {sum_of_numbers}")


if __name__ == "__main__":
    main()




    