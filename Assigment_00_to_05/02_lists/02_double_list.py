def main():
    num:list[int] = [11, 22, 33, 44, 55, 66]  
    for i in range(len(num)):
        element_at_index = num[i]
        num[i] = element_at_index * 2

    print(f"The double of each number is {num}")

if __name__ == "__main__":
    main()
