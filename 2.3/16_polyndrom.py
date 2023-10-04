number = str(input())
for i in range(len(number)):
    if number[i] != number[len(number) - i - 1]:
        print("NO")
        exit(0)
    if i == (len(number) // 2):
        break

print("YES")
