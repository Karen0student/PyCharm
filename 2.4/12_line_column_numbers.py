line = int(input())
column = int(input())
new_line_number = column
space_count = len(str(line * column))
multiplier = 10

for number in range(1, (line * column) + 1):
    if number > new_line_number:
        new_line_number += column
        print('')

    if line * column < 10:
        print(f"{number:>{space_count - 1}}", end=' ')
    else:
        print(f"{number:>{space_count}}", end=' ')
