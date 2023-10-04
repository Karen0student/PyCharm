mylist = []
for _ in range(2):
    string1, string2 = str(input())
    number1 = int(string1)
    number2 = int(string2)
    mylist.append(number1)
    mylist.append(number2)

mylist = sorted(mylist)
print(f"{mylist[-1]}{(mylist[1] + mylist[2]) % 10}{mylist[0]}")
