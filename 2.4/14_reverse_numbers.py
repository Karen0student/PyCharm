line = int(input())
column = int(input())
space_count = len(str(line * column))
count = 0
reverse = False
reverse_number = column * 2
for number in range(1, (line * column) + 1):
    if reverse is True and count == column:
        reverse = False
        count = 0
        print('')
    if count == column:
        count = 0
        reverse = True
        print('')
    if line * column < 10 and reverse is False:
        print(f"{number:>{space_count - 1}}", end=' ')
        count += 1
    elif line * column < 10 and reverse is True:
        print(f"{reverse_number:>{space_count - 1}}", end=' ')
        reverse_number -= 1
        count += 1

    elif reverse is False:
        print(f"{number:>{space_count}}", end=' ')
        reverse_number = number + column
        count += 1
    else:
        print(f"{reverse_number:>{space_count}}", end=' ')
        reverse_number -= 1
        count += 1
