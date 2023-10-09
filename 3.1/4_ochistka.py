mylist = []
while True:
    string = input()
    if string == '':
        break
    else:
        mylist.append(string)

for string in mylist:
    if "#" not in string and "@" not in string:
        print(string)
    else:
        if "#" in string[0] and "@" not in string:
            print(f"{string[2:]}")
            continue
        if "@" in string[len(string) - 1]:
            continue
        else:
            print(string)
