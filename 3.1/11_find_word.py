quantity = int(input())
mylist = []

for _ in range(quantity):
    mylist.append(input())

find_word = input()
for string in mylist:
    string_lower = string.lower()
    find_word = find_word.lower()
    if find_word in string_lower:
        print(string)
