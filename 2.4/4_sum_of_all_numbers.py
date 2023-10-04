quantity = int(input())
mylist = []
for _ in range(quantity):
    mylist.append(int(input()))

result = 0
for element in mylist:
    while element != 0:
        result += element % 10
        element //= 10

print(result)
