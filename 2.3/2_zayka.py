mylist = []
while True:
    string = str(input())
    if string == "Приехали!":
        break
    else:
        mylist.append(string)

count = 0
for i in range(len(mylist)):
    if "зайка" in mylist[i]:
        count += 1

print(count)
