mylist = []
while True:
    string = input()
    if string == '':
        break
    else:
        mylist.append(string)

for string in mylist:
    if string[0] == "#" or string[1] == "#":
        continue
    if "#" in string:
        for digit in string:
            if digit == "#":
                break
            else:
                print(digit, end="")
        print()
    else:
        print(string)
