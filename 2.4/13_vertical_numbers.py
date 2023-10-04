line = int(input())
column = int(input())
space_count = len(str(line * column))
multiplier = 10
number = 1
count = 0
number_value_modifier = 1
for _ in range(1, (line * column) + 1):
    if count == column:
        number_value_modifier += 1
        count = 0
        number = number_value_modifier
        print('')

    if line * column < 10:
        print(f"{number:>{space_count - 1}}", end=' ')
        number += line
        count += 1
    else:
        print(f"{number:>{space_count}}", end=' ')
        number += line
        count += 1
