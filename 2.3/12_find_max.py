number = int(input())
mylist = []

while number != 0:
    new = number % 10
    number //= 10
    if new != 0:
        mylist.append(new)

mylist = sorted(mylist, reverse=True)
print(mylist[0])
