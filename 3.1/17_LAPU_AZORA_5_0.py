string = input()
string = string.replace(" ", "")
string = string.lower()

first_index = 0

for last_index in range(len(string) - 1, (len(string) - 1) // 2, -1):
    if string[first_index] == string[last_index]:
        first_index += 1
    else:
        print("NO")
        exit(0)

print("YES")
