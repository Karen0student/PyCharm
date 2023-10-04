number = int(input())
for i in range(1, number + 1):
    print_value, first_number = i, i
    while print_value <= number * first_number:
        print(f"{print_value} ", end="")
        print_value += first_number
    print("")
