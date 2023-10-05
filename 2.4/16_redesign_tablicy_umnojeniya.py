line = int(input())
column = int(input())

for i in range(1, line + 1):
    for j in range(1, line + 1):
        num = str(i * j)
        ends = "" if j == line else "|"
        print(f"{num:^{column}}", end=ends)
    if i != line:
        print('\n' + '-' * (line * column + line - 1))
