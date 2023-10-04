number = int(input())
if number == 0 or number == 1:
    print("NO")
    exit(0)

for i in range(2, (number // 2) + 1):
    if number % i == 0:
        print("NO")
        exit(0)

print("YES")
