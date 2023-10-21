n = int(input())
Biggest_number = -9999999
for i in range(n):
    sum_of_group = 0
    count_of_group = 0
    number = input()
    while number != "next":
        number = int(number)
        count_of_group += 1
        sum_of_group += number
        number = input()

    average = sum_of_group / count_of_group
    Biggest_number = max(average, Biggest_number)

print(f"{Biggest_number:.2f}")
