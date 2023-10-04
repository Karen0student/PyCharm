string1 = input()
string2 = input()
string3 = input()

mylist = []
if "зайка" in string1:
    mylist.append(string1)
if "зайка" in string2:
    mylist.append(string2)
if "зайка" in string3:
    mylist.append(string3)

mylist = sorted(mylist)
print(f"{mylist[0]} {len(mylist[0])}")
