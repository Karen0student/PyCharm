Length = int(input())
quantity = int(input())
mylist = []

for _ in range(quantity):
    mylist.append(input())

for string in mylist:
    if len(string) < Length:
        print(string)
    else:
        print(f"{string[0:Length - 3]}...")
print()
