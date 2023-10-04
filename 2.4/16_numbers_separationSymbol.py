line = int(input())
column = int(input())
count = 0
space_count = len(str(line * column))
number = 0
print_number = 0
for number in range(1, (line * column) + 1):
    if count == column - 1 and line * column < 10:
        count = 0
        print(f"{print_number:>{space_count - 1}}")
        print_number = number + 1
        continue
    elif count == column - 1:
        count = 0
        print(f"{print_number:>{space_count}}")
        print_number = number + 1
        continue
    if line * column < 10:
        print(f"{print_number:>{space_count - 1}}", end=' | ')
        print_number += number
        count += 1

    else:
        print(f"{number + sum_coefficient:>{space_count}}", end=' ')
        sum_coefficient += 1
        count += 1
