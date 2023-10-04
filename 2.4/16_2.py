# {---} = line * column + column - 1
line = int(input())
column = int(input())
count = 0
space_count = len(str(line * column))
for number in range(1, line + 1):
    print_number = number
    print_quantity = 0
    if line * column < 10:
        while print_quantity != column - 1:
            print(f" {print_number:>{space_count - 1}}", end=' |')
            print_number += number
            print_quantity += 1
    else:
        while print_quantity != column - 1:
            print(f" {print_number:>{space_count}}", end='  |')
            print_number += number
            print_quantity += 1
    if line * column < 10:
        print(f" {print_number:>{space_count - 1}}")
    else:
        print(f" {print_number:>{space_count}}")

    # if line * column < 10:
    #     new_line_separation = (line * column) + column - 1
    # else:
    new_line_separation = (line * column) + column - 1
    while new_line_separation != 0 and number != line:
        print("-", end='')
        new_line_separation -= 1
    print('')
