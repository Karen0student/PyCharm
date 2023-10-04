line = int(input())
column = int(input())
max_value = line * column
column_width = len(str(max_value))

for i in range(1, line + 1):
    for j in range(1, column + 1):
        result = i * j
        # if line < 3 and column < 3:
        #     if line == 1 and column == 1:
        #         print(f"{result}")
        #         break
        #     elif i != line:
        #
        if line * column < 10:
            print(f"{result:>{column_width + 1}}", end=" |" if j < column else "")
        else:
            print(f"{result:>{column_width + 1}}", end="  |" if j < column else "")
    print("\n" + "-" * (max_value + column - 1)) if i < line else print()
