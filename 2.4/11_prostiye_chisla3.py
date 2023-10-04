quantity = int(input())
mylist = []

for _ in range(quantity):
    mylist.append(int(input()))

count = 0
for element in mylist:
    divider = 2
    if element == 1:
        count += 1
        continue
    while True:
        if divider == element and element != 2:
            count += 1
            break
        elif element % divider == 0:
            break
        divider += 1

print(count)
