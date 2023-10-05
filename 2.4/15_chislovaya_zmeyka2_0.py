line = int(input())
column = int(input())
max_len = len(str(line * column))
for i in range(1, line + 1):
    number = i
    for j in range(1, column + 1):
        num_len = len(str(number))
        print(f"{' ' * (max_len - num_len)}{number}", end=" ")
        if j % 2 != 0:
            number += 1 + (line - i) * 2
        else:
            number += 2 * i - 1
    print()
