mylist = []
for _ in range(3):
    el1, el2 = input()
    first = str(el1)
    second = str(el2)
    mylist.append(first)
    mylist.append(second)

index = 0
for index in range(2):
    result = mylist.count(mylist[index]) >= (len(mylist) / 2)
    if result:
        print(mylist[index])
        break
