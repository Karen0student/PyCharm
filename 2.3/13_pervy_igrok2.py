quantity = int(input())
mylist = []
for _ in range(quantity):
    string = str(input())
    mylist.append(string)

mylist = sorted(mylist)
print(mylist[0])
