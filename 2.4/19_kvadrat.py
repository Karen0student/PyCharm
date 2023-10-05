number = int(input())

if number % 2 != 0:
    max_digits = len(str(((number - 1) // 2) + 1))
else:
    max_digits = len(str((number - 1) // 2))

for j in range(number):
    print(f"{1:{max_digits}} ", end="")
print()

for i in range(1, number - 1):
    print(f"{1:{max_digits}} ", end="")
    for j in range(1, number - 1):
        value = min(i, j, number - 1 - i, number - 1 - j) + 1
        print(f"{value:{max_digits}} ", end="")
    print(f"{1:{max_digits}}")

if number > 1:
    for j in range(number):
        print(f"{1:{max_digits}} ", end="")
    print()
