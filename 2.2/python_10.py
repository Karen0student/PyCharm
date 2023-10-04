number = int(input())

first = number % 10
number //= 10
second = number % 10
number //= 10
third = number % 10

mylist = []
first_couple = first + second
second_couple = third + second

mylist.append(first_couple)
mylist.append(second_couple)

mylist = sorted(mylist, reverse=True)
print(f"{mylist[0]}{mylist[1]}")
