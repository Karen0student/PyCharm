# print index of string
quantity = int(input())
mylist = []
for _ in range(quantity):
    mylist.append(input())

for string in mylist:
    if "зайка" in string:
        print(string.index("зайка") + 1)
    else:
        print("Заек нет =(")
