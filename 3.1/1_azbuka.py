quantity = int(input())
mylist = []
words = ["А", "Б", "В", "а", "б", "в"]
for index in range(quantity):
    string = input()
    mylist.append(string)

for element in mylist:
    if element[0] in words:
        continue
    else:
        print("NO")
        exit(0)
print("YES")
