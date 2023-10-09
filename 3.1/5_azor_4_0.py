string = input()
for index in range(len(string) // 2):
    if string[index] != string[len(string) - 1 - index]:
        print("NO")
        exit(0)

print("YES")
