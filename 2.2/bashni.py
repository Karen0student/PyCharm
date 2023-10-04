number = int(input())

el3 = number % 10
el2 = (number // 10) % 10
el1 = ((number // 10) // 10) % 10

mylist = sorted([el1, el2, el3])

if mylist[0] == 0:
    print(f"{mylist[1]}{mylist[0]}  {mylist[2]}{mylist[1]}")
else:
    print(f"{mylist[0]}{mylist[1]}  {mylist[2]}{mylist[1]}")
