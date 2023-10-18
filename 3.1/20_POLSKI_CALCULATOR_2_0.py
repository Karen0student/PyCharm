import math

input_list = list(input().split())
mylist = [int(input_list[0])]
for i in input_list[1:]:
    if i.isdigit():
        mylist.append(int(i))
    elif i == "/":
        elem = mylist.pop()
        mylist[-1] //= elem
    elif i == "!":
        mylist[-1] = math.factorial(mylist[-1])
    elif i == "#":
        mylist.append(mylist[-1])
    elif i == "@":
        mylist.append(mylist.pop(-3))
    elif i == "~":
        mylist[-1] = -mylist[-1]
    else:
        elem = mylist.pop()
        exec("mylist[-1] " + i + "= elem")
print(mylist[0])
