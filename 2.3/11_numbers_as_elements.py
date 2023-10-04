number = int(input())
mylist = []

while number != 0:
    new = number % 10
    number //= 10
    if new != 0:
        mylist.append(new)

result = 0
for el in mylist:
    result += el

print(result)
